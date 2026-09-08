"""Derive, validate, and publish immutable artifact lineages."""

from __future__ import annotations

import os
import tempfile
from pathlib import Path, PurePosixPath
from typing import Any, Optional, Sequence

from .frontmatter import discover, render_revision, sha256
from .models import ARTIFACT_NAME, ArtifactError, BasedOn, Revision


def resolve_reference(root: Path, reference: str) -> tuple[str, Path, bool]:
    """Return a canonical recorded path, resolved file, and internal flag."""
    value = Path(reference)
    root = root.resolve()
    if value.is_absolute():
        resolved = value.resolve()
        try:
            normalized = resolved.relative_to(root).as_posix()
        except ValueError:
            return resolved.as_posix(), resolved, False
        return normalized, resolved, True

    # Internal references use one canonical POSIX spelling. Rejecting aliases
    # prevents an equivalent `..` path from bypassing supersession checks.
    if "\\" in reference:
        raise ArtifactError(f"relative based_on path uses a backslash: {reference}")
    parts = reference.split("/")
    if any(part in {"", ".", ".."} for part in parts):
        raise ArtifactError(f"relative based_on path is not canonical: {reference}")
    normalized = PurePosixPath(*parts).as_posix()
    resolved = (root / normalized).resolve()
    try:
        resolved.relative_to(root)
    except ValueError as error:
        raise ArtifactError(
            f"relative based_on path escapes the artifact root: {reference}"
        ) from error
    return normalized, resolved, True


def analyze(root: Path) -> dict[str, Any]:
    """Derive heads and validate lineage and upstream digests."""
    revisions, errors = discover(root)
    by_path = {revision.path: revision for revision in revisions}
    superseded: set[str] = set()

    for item in revisions:
        if item.revision == 1 and item.supersedes is not None:
            errors.append(
                {
                    "code": "first_revision_has_predecessor",
                    "path": item.path,
                    "supersedes": item.supersedes,
                }
            )
        if item.revision > 1 and item.supersedes is None:
            errors.append({"code": "missing_predecessor", "path": item.path})
        if item.supersedes is None:
            continue
        predecessor_path = PurePosixPath(item.supersedes)
        if predecessor_path.is_absolute() or ".." in predecessor_path.parts:
            errors.append(
                {
                    "code": "invalid_predecessor_path",
                    "path": item.path,
                    "supersedes": item.supersedes,
                }
            )
            continue
        predecessor = by_path.get(item.supersedes)
        if predecessor is None:
            errors.append(
                {
                    "code": "missing_predecessor",
                    "path": item.path,
                    "supersedes": item.supersedes,
                }
            )
            continue
        if predecessor.artifact != item.artifact:
            errors.append(
                {
                    "code": "cross_artifact_supersedes",
                    "path": item.path,
                    "supersedes": item.supersedes,
                }
            )
        if predecessor.revision >= item.revision:
            errors.append(
                {
                    "code": "non_forward_supersedes",
                    "path": item.path,
                    "supersedes": item.supersedes,
                }
            )
        superseded.add(item.supersedes)

    by_artifact: dict[str, list[Revision]] = {}
    for item in revisions:
        by_artifact.setdefault(item.artifact, []).append(item)

    heads: dict[str, list[str]] = {}
    for artifact, items in sorted(by_artifact.items()):
        actual_revisions = sorted(item.revision for item in items)
        # Compare existing numbers directly; constructing range(max_revision)
        # would let one malformed filename force an enormous allocation.
        contiguous = all(
            revision == expected
            for expected, revision in enumerate(actual_revisions, start=1)
        )
        if not contiguous:
            errors.append(
                {
                    "code": "non_contiguous_revisions",
                    "artifact": artifact,
                    "revisions": actual_revisions,
                }
            )
        artifact_heads = sorted(
            item.path for item in items if item.path not in superseded
        )
        heads[artifact] = artifact_heads
        if len(artifact_heads) > 1:
            errors.append(
                {
                    "code": "ambiguous_heads",
                    "artifact": artifact,
                    "heads": artifact_heads,
                }
            )

    stale: list[dict[str, Any]] = []
    current_paths = {
        path for artifact_heads in heads.values() for path in artifact_heads
    }
    for item in revisions:
        # Historical revisions remain evidence. Only current heads feed active
        # work, so repairing a stale head must be able to make the tree valid.
        if item.path not in current_paths:
            continue
        seen_references: set[str] = set()
        for reference in item.based_on:
            if reference.path in seen_references:
                errors.append(
                    {
                        "code": "duplicate_upstream",
                        "path": item.path,
                        "upstream": reference.path,
                    }
                )
                continue
            seen_references.add(reference.path)
            try:
                normalized, resolved, internal = resolve_reference(
                    root, reference.path
                )
            except ArtifactError as error:
                errors.append(
                    {
                        "code": "invalid_upstream_path",
                        "path": item.path,
                        "upstream": reference.path,
                        "detail": str(error),
                    }
                )
                continue
            if not resolved.is_file():
                errors.append(
                    {
                        "code": "missing_upstream",
                        "path": item.path,
                        "upstream": reference.path,
                    }
                )
                continue
            try:
                actual = sha256(resolved)
            except ArtifactError as error:
                errors.append(
                    {
                        "code": "unreadable_upstream",
                        "path": item.path,
                        "upstream": reference.path,
                        "detail": str(error),
                    }
                )
                continue
            if actual != reference.digest:
                stale.append(
                    {
                        "code": "digest_mismatch",
                        "path": item.path,
                        "upstream": reference.path,
                        "expected": reference.digest,
                        "actual": actual,
                    }
                )
            if internal and normalized in superseded:
                upstream = by_path.get(normalized)
                stale.append(
                    {
                        "code": "superseded_upstream",
                        "path": item.path,
                        "upstream": reference.path,
                        "heads": heads.get(upstream.artifact, []) if upstream else [],
                    }
                )

    return {
        "valid": not errors and not stale,
        "heads": heads,
        "stale_references": stale,
        "errors": errors,
    }


def clean_artifact_name(value: str) -> str:
    """Validate a root-relative artifact directory name."""
    if not ARTIFACT_NAME.fullmatch(value):
        raise ArtifactError(
            "artifact must be one lowercase name containing letters, digits, or hyphens"
        )
    return value


def next_revision(root: Path, artifact: str) -> dict[str, Any]:
    """Derive the next identity from a valid, unambiguous tree."""
    artifact = clean_artifact_name(artifact)
    if not root.exists():
        return {
            "artifact": artifact,
            "revision": 1,
            "path": f"{artifact}/001.md",
            "supersedes": None,
        }
    report = analyze(root)
    if report["errors"]:
        raise ArtifactError("artifact tree is invalid; run inspect for details")
    revisions, _ = discover(root)
    items = [item for item in revisions if item.artifact == artifact]
    if not items:
        revision = 1
        supersedes = None
    else:
        artifact_heads = report["heads"].get(artifact, [])
        if len(artifact_heads) != 1:
            raise ArtifactError(f"artifact {artifact!r} does not have exactly one head")
        revision = max(item.revision for item in items) + 1
        supersedes = artifact_heads[0]
    return {
        "artifact": artifact,
        "revision": revision,
        "path": f"{artifact}/{revision:03d}.md",
        "supersedes": supersedes,
    }


def reference_digest(root: Path, reference: str) -> tuple[BasedOn, bool]:
    """Resolve one recorded reference and compute its whole-file digest."""
    normalized, resolved, internal = resolve_reference(root, reference)
    if not resolved.is_file():
        raise ArtifactError(f"based_on path does not exist: {reference}")
    return BasedOn(normalized, sha256(resolved)), internal


def publish(
    root: Path, artifact: str, body_file: Path, references: Sequence[str]
) -> dict[str, Any]:
    """Create one new revision without rewriting an existing target."""
    root = root.resolve()
    root.mkdir(parents=True, exist_ok=True)
    plan = next_revision(root, artifact)
    try:
        body = body_file.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as error:
        raise ArtifactError(f"cannot read body file {body_file}: {error}") from error
    if body.startswith("---\n") or body.startswith("---\r\n"):
        raise ArtifactError("body file must not contain revision frontmatter")

    # Finish every fallible lineage check before assigning a numbered file.
    # A failed candidate must never become an immutable published revision.
    report = analyze(root)
    current_paths = {
        path for artifact_heads in report["heads"].values() for path in artifact_heads
    }
    revisions, _ = discover(root)
    revision_paths = {revision.path for revision in revisions}
    based_on: list[BasedOn] = []
    seen_references: set[str] = set()
    for reference in references:
        item, internal = reference_digest(root, reference)
        if item.path in seen_references:
            raise ArtifactError(f"duplicate based_on path: {item.path}")
        seen_references.add(item.path)
        if internal and item.path in revision_paths and item.path not in current_paths:
            raise ArtifactError(f"based_on revision is not a current head: {item.path}")
        based_on.append(item)
    content = render_revision(plan, based_on, body)
    target = root / plan["path"]
    if target.parent.is_symlink():
        raise ArtifactError(
            f"artifact directory must not be a symbolic link: {target.parent}"
        )
    target.parent.mkdir(parents=True, exist_ok=True)
    if target.parent.is_symlink() or target.parent.resolve() != target.parent:
        raise ArtifactError(
            f"artifact directory escapes the artifact root: {target.parent}"
        )

    # Flush an unnumbered temporary file, then link it into place atomically.
    # The hard link both prevents overwrite and avoids exposing partial content.
    temporary_path: Optional[Path] = None
    try:
        with tempfile.NamedTemporaryFile(
            mode="wb", dir=target.parent, prefix=".artifact-lineage-", delete=False
        ) as destination:
            temporary_path = Path(destination.name)
            destination.write(content)
            destination.flush()
            os.fsync(destination.fileno())
        os.link(temporary_path, target, follow_symlinks=False)
    except FileExistsError as error:
        raise ArtifactError(
            f"refusing to overwrite published revision {target}"
        ) from error
    finally:
        if temporary_path is not None:
            temporary_path.unlink(missing_ok=True)
    try:
        directory = os.open(target.parent, os.O_RDONLY)
    except OSError:
        directory = None
    if directory is not None:
        try:
            os.fsync(directory)
        finally:
            os.close(directory)
    if not target.is_file():
        raise ArtifactError(f"published revision could not be verified: {target}")
    return {
        **plan,
        "based_on": [reference.__dict__ for reference in based_on],
        "digest": sha256(target),
    }
