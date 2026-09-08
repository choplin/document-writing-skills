"""Shared artifact-lineage types and validation constants."""

from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Optional


REVISION_NAME = re.compile(r"^(?P<revision>[0-9]{3,})\.md$")
DIGEST = re.compile(r"^sha256:[0-9a-f]{64}$")
ARTIFACT_NAME = re.compile(r"^[a-z0-9][a-z0-9-]*$")


class ArtifactError(Exception):
    """An invalid request or artifact tree."""


@dataclass(frozen=True)
class BasedOn:
    """One exact upstream file and its recorded whole-file digest."""

    path: str
    digest: str


@dataclass(frozen=True)
class Revision:
    """The deterministic fields parsed from one published revision."""

    path: str
    artifact: str
    revision: int
    supersedes: Optional[str]
    based_on: tuple[BasedOn, ...]
