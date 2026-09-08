from __future__ import annotations

import hashlib
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


REPOSITORY = Path(__file__).resolve().parents[1]
HELPER = (
    REPOSITORY
    / "skills"
    / "document-writing"
    / "document-writing"
    / "scripts"
    / "artifact-lineage.py"
)


def run_helper(*arguments: object) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(HELPER), *(str(argument) for argument in arguments)],
        cwd=REPOSITORY,
        check=False,
        capture_output=True,
        text=True,
    )


def publish(
    root: Path, artifact: str, body: Path, *based_on: str
) -> subprocess.CompletedProcess[str]:
    arguments: list[object] = ["publish", root, artifact, "--body-file", body]
    for reference in based_on:
        arguments.extend(["--based-on", reference])
    return run_helper(*arguments)


class ArtifactLineageTest(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary_directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary_directory.cleanup)
        self.tmp_path = Path(self.temporary_directory.name)
        self.root = self.tmp_path / "writing"
        self.body = self.tmp_path / "body.md"

    def write_body(self, value: str) -> None:
        self.body.write_text(value, encoding="utf-8")

    def test_publish_derives_revision_predecessor_and_digest(self) -> None:
        self.write_body("First candidate\n\n## Revision note\n\nInitial.\n")
        first = publish(self.root, "plot", self.body)
        self.assertEqual(first.returncode, 0, first.stderr)
        first_result = json.loads(first.stdout)
        self.assertEqual(first_result["path"], "plot/001.md")
        self.assertIsNone(first_result["supersedes"])

        self.write_body("Second candidate\n\n## Revision note\n\nRevised.\n")
        second = publish(self.root, "plot", self.body)
        self.assertEqual(second.returncode, 0, second.stderr)
        second_result = json.loads(second.stdout)
        self.assertEqual(second_result["path"], "plot/002.md")
        self.assertEqual(second_result["supersedes"], "plot/001.md")
        self.assertTrue(
            (self.root / "plot/001.md")
            .read_text(encoding="utf-8")
            .endswith("Initial.\n")
        )

        digest = run_helper("digest", self.root / "plot/002.md")
        expected = "sha256:" + hashlib.sha256(
            (self.root / "plot/002.md").read_bytes()
        ).hexdigest()
        self.assertEqual(digest.returncode, 0)
        self.assertEqual(json.loads(digest.stdout)["digest"], expected)

    def test_next_derives_first_revision_before_root_exists(self) -> None:
        result = run_helper("next", self.root, "plot")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(
            json.loads(result.stdout),
            {
                "artifact": "plot",
                "path": "plot/001.md",
                "revision": 1,
                "supersedes": None,
            },
        )
        self.assertFalse(self.root.exists())

    def test_publish_records_based_on_and_inspect_reports_heads(self) -> None:
        self.write_body("Focus\n")
        self.assertEqual(publish(self.root, "focus", self.body).returncode, 0)
        self.write_body("Plot\n")
        result = publish(self.root, "plot", self.body, "focus/001.md")
        self.assertEqual(result.returncode, 0, result.stderr)
        published = json.loads(result.stdout)
        self.assertEqual(published["based_on"][0]["path"], "focus/001.md")

        inspection = run_helper("inspect", self.root)
        self.assertEqual(inspection.returncode, 0, inspection.stdout)
        report = json.loads(inspection.stdout)
        self.assertTrue(report["valid"])
        self.assertEqual(
            report["heads"],
            {"focus": ["focus/001.md"], "plot": ["plot/001.md"]},
        )

    def test_inspect_reports_digest_mismatch(self) -> None:
        self.write_body("Focus\n")
        self.assertEqual(publish(self.root, "focus", self.body).returncode, 0)
        self.write_body("Plot\n")
        self.assertEqual(
            publish(self.root, "plot", self.body, "focus/001.md").returncode, 0
        )
        (self.root / "focus/001.md").write_text(
            "changed after publication\n", encoding="utf-8"
        )

        inspection = run_helper("inspect", self.root)
        self.assertEqual(inspection.returncode, 1)
        stale = json.loads(inspection.stdout)["stale_references"]
        self.assertEqual([item["code"] for item in stale], ["digest_mismatch"])

    def test_inspect_reports_superseded_upstream(self) -> None:
        self.write_body("Focus one\n")
        self.assertEqual(publish(self.root, "focus", self.body).returncode, 0)
        self.write_body("Plot\n")
        self.assertEqual(
            publish(self.root, "plot", self.body, "focus/001.md").returncode, 0
        )
        self.write_body("Focus two\n")
        self.assertEqual(publish(self.root, "focus", self.body).returncode, 0)

        inspection = run_helper("inspect", self.root)
        self.assertEqual(inspection.returncode, 1)
        stale = json.loads(inspection.stdout)["stale_references"]
        self.assertEqual(
            stale,
            [
                {
                    "code": "superseded_upstream",
                    "heads": ["focus/002.md"],
                    "path": "plot/001.md",
                    "upstream": "focus/001.md",
                }
            ],
        )

        self.write_body("Plot two\n")
        repaired = publish(self.root, "plot", self.body, "focus/002.md")
        self.assertEqual(repaired.returncode, 0, repaired.stderr)
        inspection = run_helper("inspect", self.root)
        self.assertEqual(inspection.returncode, 0, inspection.stdout)
        self.assertTrue(json.loads(inspection.stdout)["valid"])

    def test_ambiguous_heads_block_inspection_and_next_revision(self) -> None:
        artifact = self.root / "plot"
        artifact.mkdir(parents=True)
        (artifact / "001.md").write_text(
            "---\nartifact: plot\nrevision: 1\n---\nOne\n", encoding="utf-8"
        )
        for revision in (2, 3):
            (artifact / f"{revision:03d}.md").write_text(
                "---\n"
                "artifact: plot\n"
                f"revision: {revision}\n"
                "supersedes: plot/001.md\n"
                "---\n"
                f"Branch {revision}\n",
                encoding="utf-8",
            )

        inspection = run_helper("inspect", self.root)
        self.assertEqual(inspection.returncode, 1)
        errors = json.loads(inspection.stdout)["errors"]
        self.assertEqual([error["code"] for error in errors], ["ambiguous_heads"])

        next_result = run_helper("next", self.root, "plot")
        self.assertEqual(next_result.returncode, 1)
        self.assertIn(
            "artifact tree is invalid", json.loads(next_result.stderr)["error"]
        )

    def test_publish_refuses_frontmatter_body(self) -> None:
        self.write_body("---\ntitle: accidental\n---\nBody\n")
        result = publish(self.root, "plot", self.body)
        self.assertEqual(result.returncode, 1)
        self.assertFalse((self.root / "plot" / "001.md").exists())

    def test_publish_rejects_noncanonical_and_duplicate_upstream_paths(self) -> None:
        self.write_body("Focus\n")
        self.assertEqual(publish(self.root, "focus", self.body).returncode, 0)
        self.write_body("Plot\n")

        noncanonical = publish(
            self.root, "plot", self.body, "focus/../focus/001.md"
        )
        self.assertEqual(noncanonical.returncode, 1)
        self.assertIn("not canonical", noncanonical.stderr)

        duplicate = publish(
            self.root, "plot", self.body, "focus/001.md", "focus/001.md"
        )
        self.assertEqual(duplicate.returncode, 1)
        self.assertIn("duplicate based_on", duplicate.stderr)
        self.assertFalse((self.root / "plot" / "001.md").exists())

    def test_publish_rejects_superseded_upstream_before_writing(self) -> None:
        self.write_body("Focus one\n")
        self.assertEqual(publish(self.root, "focus", self.body).returncode, 0)
        self.write_body("Focus two\n")
        self.assertEqual(publish(self.root, "focus", self.body).returncode, 0)
        self.write_body("Plot\n")

        result = publish(self.root, "plot", self.body, "focus/001.md")
        self.assertEqual(result.returncode, 1)
        self.assertIn("not a current head", result.stderr)
        self.assertFalse((self.root / "plot" / "001.md").exists())

    def test_absolute_internal_upstream_is_recorded_canonically(self) -> None:
        self.write_body("Focus\n")
        self.assertEqual(publish(self.root, "focus", self.body).returncode, 0)
        self.write_body("Plot\n")

        result = publish(
            self.root, "plot", self.body, str(self.root / "focus" / "001.md")
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        based_on = json.loads(result.stdout)["based_on"]
        self.assertEqual(based_on[0]["path"], "focus/001.md")

    def test_publish_rejects_symlink_artifact_directory(self) -> None:
        outside = self.tmp_path / "outside"
        outside.mkdir()
        self.root.mkdir()
        (self.root / "plot").symlink_to(outside, target_is_directory=True)
        self.write_body("Plot\n")

        result = publish(self.root, "plot", self.body)
        self.assertEqual(result.returncode, 1)
        self.assertIn("symbolic link", result.stderr)
        self.assertFalse((outside / "001.md").exists())

    def test_publish_rejects_cross_platform_escape_name(self) -> None:
        self.write_body("Plot\n")
        for artifact in ("../escape", r"..\escape", "nested/plot"):
            with self.subTest(artifact=artifact):
                result = publish(self.root, artifact, self.body)
                self.assertEqual(result.returncode, 1)

    def test_filesystem_errors_use_the_json_error_contract(self) -> None:
        root_file = self.tmp_path / "not-a-directory"
        root_file.write_text("occupied\n", encoding="utf-8")
        self.write_body("Plot\n")

        result = publish(root_file, "plot", self.body)
        self.assertEqual(result.returncode, 1)
        self.assertEqual(set(json.loads(result.stderr)), {"error"})

    def test_frontmatter_fields_after_based_on_are_accepted(self) -> None:
        focus = self.root / "focus"
        plot = self.root / "plot"
        focus.mkdir(parents=True)
        plot.mkdir()
        (focus / "001.md").write_text(
            "---\nartifact: focus\nrevision: 1\n---\nFocus\n", encoding="utf-8"
        )
        digest = "sha256:" + hashlib.sha256(
            (focus / "001.md").read_bytes()
        ).hexdigest()
        (plot / "001.md").write_text(
            "---\n"
            "artifact: plot\n"
            "based_on:\n"
            "  - path: focus/001.md\n"
            f"    digest: {digest}\n"
            "revision: 1\n"
            "---\n"
            "Plot\n",
            encoding="utf-8",
        )

        inspection = run_helper("inspect", self.root)
        self.assertEqual(inspection.returncode, 0, inspection.stdout)

    def test_huge_revision_number_is_reported_without_dense_allocation(self) -> None:
        artifact = self.root / "plot"
        artifact.mkdir(parents=True)
        huge = "9" * 40
        (artifact / f"{huge}.md").write_text(
            f"---\nartifact: plot\nrevision: {huge}\n---\nPlot\n", encoding="utf-8"
        )

        inspection = run_helper("inspect", self.root)
        self.assertEqual(inspection.returncode, 1)
        errors = json.loads(inspection.stdout)["errors"]
        self.assertIn("non_contiguous_revisions", [error["code"] for error in errors])

    def test_missing_revision_predecessor_is_invalid(self) -> None:
        artifact = self.root / "plot"
        artifact.mkdir(parents=True)
        (artifact / "001.md").write_text(
            "---\nartifact: plot\nrevision: 1\n---\nOne\n", encoding="utf-8"
        )
        (artifact / "002.md").write_text(
            "---\nartifact: plot\nrevision: 2\n---\nTwo\n", encoding="utf-8"
        )

        inspection = run_helper("inspect", self.root)
        self.assertEqual(inspection.returncode, 1)
        errors = json.loads(inspection.stdout)["errors"]
        self.assertIn("missing_predecessor", [error["code"] for error in errors])


if __name__ == "__main__":
    unittest.main()
