"""Read and write the documented artifact revision header subset."""

from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path
from typing import Any, Iterable

from .models import DIGEST, REVISION_NAME, ArtifactError, BasedOn, Revision


def sha256(path: Path) -> str:
    """Return the SHA-256 digest of the complete file."""
    hasher = hashlib.sha256()
    try:
        with path.open("rb") as source:
            for chunk in iter(lambda: source.read(1024 * 1024), b""):
                hasher.update(chunk)
    except OSError as error:
        raise ArtifactError(f"cannot read {path}: {error}") from error
    return f"sha256:{hasher.hexdigest()}"


def decode_scalar(value: str, location: str) -> str:
    """Decode an unquoted or JSON-quoted scalar from the contract subset."""
    value = value.strip()
    if not value:
        raise ArtifactError(f"{location}: empty scalar")
    if value.startswith('"'):
        try:
            decoded = json.loads(value)
        except json.JSONDecodeError as error:
            raise ArtifactError(f"{location}: invalid quoted scalar") from error
        if not isinstance(decoded, str) or not decoded:
            raise ArtifactError(f"{location}: scalar must be a non-empty string")
        return decoded
    return value


def parse_revision(path: Path, root: Path) -> Revision:
    """Parse the documented, intentionally small YAML frontmatter subset."""
    try:
        text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as error:
        raise ArtifactError(f"cannot read {path}: {error}") from error
    lines = text.splitlines()
    if not lines or lines[0] != "---":
        raise ArtifactError(f"{path}: missing opening YAML delimiter")
    try:
        end = lines.index("---", 1)
    except ValueError as error:
        raise ArtifactError(f"{path}: missing closing YAML delimiter") from error

    # A narrow parser keeps the helper dependency-free while making unsupported
    # YAML features fail explicitly instead of being interpreted inconsistently.
    scalars: dict[str, str] = {}
    based_on: list[dict[str, str]] = []
    in_based_on = False
    for number, line in enumerate(lines[1:end], start=2):
        location = f"{path}:{number}"
        if not line.strip():
            continue
        if line == "based_on:":
            if in_based_on or "based_on" in scalars:
                raise ArtifactError(f"{location}: duplicate based_on")
            in_based_on = True
            scalars["based_on"] = "present"
            continue
        if in_based_on:
            match = re.fullmatch(r"  - path: (.+)", line)
            if match:
                based_on.append({"path": decode_scalar(match.group(1), location)})
                continue
            match = re.fullmatch(r"    digest: (.+)", line)
            if match and based_on and "digest" not in based_on[-1]:
                based_on[-1]["digest"] = decode_scalar(match.group(1), location)
                continue
            if line.startswith(" "):
                raise ArtifactError(f"{location}: invalid based_on entry")
            in_based_on = False

        match = re.fullmatch(r"([a-z_]+): (.+)", line)
        if not match:
            raise ArtifactError(f"{location}: unsupported frontmatter syntax")
        key, value = match.groups()
        if key not in {"artifact", "revision", "supersedes"}:
            raise ArtifactError(f"{location}: unsupported field {key!r}")
        if key in scalars:
            raise ArtifactError(f"{location}: duplicate field {key!r}")
        scalars[key] = decode_scalar(value, location)

    if "artifact" not in scalars or "revision" not in scalars:
        raise ArtifactError(f"{path}: artifact and revision are required")
    try:
        revision = int(scalars["revision"])
    except ValueError as error:
        raise ArtifactError(f"{path}: revision must be an integer") from error
    if revision < 1:
        raise ArtifactError(f"{path}: revision must be positive")

    parsed_based_on: list[BasedOn] = []
    if "based_on" in scalars and not based_on:
        raise ArtifactError(f"{path}: based_on must not be empty")
    for entry in based_on:
        if set(entry) != {"path", "digest"}:
            raise ArtifactError(f"{path}: every based_on item needs path and digest")
        if not DIGEST.fullmatch(entry["digest"]):
            raise ArtifactError(f"{path}: invalid SHA-256 digest for {entry['path']}")
        parsed_based_on.append(BasedOn(entry["path"], entry["digest"]))

    relative = path.relative_to(root).as_posix()
    return Revision(
        path=relative,
        artifact=scalars["artifact"],
        revision=revision,
        supersedes=scalars.get("supersedes"),
        based_on=tuple(parsed_based_on),
    )


def discover(root: Path) -> tuple[list[Revision], list[dict[str, Any]]]:
    """Read every numbered Markdown revision below an artifact root."""
    revisions: list[Revision] = []
    errors: list[dict[str, Any]] = []
    if not root.is_dir():
        return [], [{"code": "missing_root", "path": str(root)}]
    for path in sorted(root.rglob("*.md")):
        match = REVISION_NAME.fullmatch(path.name)
        if not match:
            continue
        try:
            item = parse_revision(path, root)
            expected_artifact = path.parent.relative_to(root).as_posix()
            if item.artifact != expected_artifact:
                raise ArtifactError(
                    f"{path}: artifact {item.artifact!r} does not match "
                    f"directory {expected_artifact!r}"
                )
            if item.revision != int(match.group("revision")):
                raise ArtifactError(
                    f"{path}: revision {item.revision} does not match filename"
                )
            revisions.append(item)
        except ArtifactError as error:
            errors.append(
                {"code": "invalid_revision", "path": str(path), "detail": str(error)}
            )
    return revisions, errors


def render_revision(
    plan: dict[str, Any], based_on: Iterable[BasedOn], body: str
) -> bytes:
    """Render a revision using JSON-compatible YAML scalars."""
    lines = [
        "---",
        f"artifact: {json.dumps(plan['artifact'], ensure_ascii=False)}",
        f"revision: {plan['revision']}",
    ]
    if plan["supersedes"] is not None:
        lines.append(f"supersedes: {json.dumps(plan['supersedes'])}")
    references = list(based_on)
    if references:
        lines.append("based_on:")
        for reference in references:
            lines.append(f"  - path: {json.dumps(reference.path, ensure_ascii=False)}")
            lines.append(f"    digest: {reference.digest}")
    lines.extend(["---", "", body.rstrip("\n"), ""])
    return "\n".join(lines).encode("utf-8")
