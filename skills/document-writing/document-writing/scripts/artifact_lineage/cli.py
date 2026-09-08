"""Command-line interface for artifact lineage operations."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any, Optional, Sequence

from .frontmatter import sha256
from .lineage import analyze, next_revision, publish
from .models import ArtifactError


def print_json(value: Any, stream: Any = sys.stdout) -> None:
    """Emit stable machine-readable output."""
    json.dump(value, stream, indent=2, sort_keys=True)
    stream.write("\n")


def build_parser() -> argparse.ArgumentParser:
    """Build the command-line interface."""
    parser = argparse.ArgumentParser(
        description="Publish and inspect immutable document-writing artifacts."
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    digest_parser = subparsers.add_parser("digest", help="hash one complete file")
    digest_parser.add_argument("path", type=Path)

    inspect_parser = subparsers.add_parser("inspect", help="inspect an artifact tree")
    inspect_parser.add_argument("root", type=Path)

    next_parser = subparsers.add_parser("next", help="derive the next revision")
    next_parser.add_argument("root", type=Path)
    next_parser.add_argument("artifact")

    publish_parser = subparsers.add_parser("publish", help="publish one revision")
    publish_parser.add_argument("root", type=Path)
    publish_parser.add_argument("artifact")
    publish_parser.add_argument("--body-file", required=True, type=Path)
    publish_parser.add_argument("--based-on", action="append", default=[])
    return parser


def main(argv: Optional[Sequence[str]] = None) -> int:
    """Run one CLI operation."""
    arguments = build_parser().parse_args(argv)
    try:
        if arguments.command == "digest":
            print_json({"path": str(arguments.path), "digest": sha256(arguments.path)})
            return 0
        if arguments.command == "inspect":
            report = analyze(arguments.root)
            print_json(report)
            return 0 if report["valid"] else 1
        if arguments.command == "next":
            print_json(next_revision(arguments.root, arguments.artifact))
            return 0
        if arguments.command == "publish":
            print_json(
                publish(
                    arguments.root,
                    arguments.artifact,
                    arguments.body_file,
                    arguments.based_on,
                )
            )
            return 0
    except (ArtifactError, OSError, UnicodeError) as error:
        print_json({"error": str(error)}, sys.stderr)
        return 1
    raise AssertionError(f"unhandled command: {arguments.command}")
