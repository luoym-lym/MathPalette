"""Lightweight fail-closed tests; no rendering or approval/recipe writes.

Run: python -B -m unittest review_workbench.tests.test_legacy_variant_compatibility
Full 184 Base + 95 Special pixel regression is a separate release check.
"""
from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
from dataset_tools import legacy_variant_compatibility as compat


class LegacyVariantCompatibility(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.entries = json.loads(compat.REGISTRY.read_text(encoding="utf-8"))["transitions"]
        cls.records = {branch: {row["id"]: row for line in
                              (ROOT / branch / "dataset.jsonl").read_text(encoding="utf-8").splitlines()
                              if line.strip() for row in [json.loads(line)]}
                       for branch in ("Analytics", "PlaneGeometry", "SolidGeometry")}

    def sample(self, component, entry):
        qid = next(iter(entry["questions"]))
        return self.records[component.split("/")[0]][qid], entry["questions"][qid]["dependencies"]

    def matches(self, component, entry, record, files):
        return compat.legacy_renderer_matches(component, entry["previous_renderer_sha256"],
                                              entry["current_renderer_sha256"], record, files)

    def test_registered_code_and_old_dependencies_are_exact(self):
        for component, entry in self.entries.items():
            branch, category = component.split("/")
            directory, names = (("dataset_generator", ("generate_base_variants.py", "base_support.py"))
                                if category == "Base" else
                                ("workbench", ("renderer_adapter.py", "render_plugins.py", "workbench_io.py")))
            actual_renderer = compat._hash({name: hashlib.sha256(
                (ROOT / branch / directory / name).read_bytes()).hexdigest() for name in names})
            self.assertEqual(actual_renderer, entry["current_renderer_sha256"])
            for name, digest in entry["code_sha256"].items():
                with self.subTest(component=component, code=name):
                    self.assertEqual(hashlib.sha256((ROOT / name).read_bytes()).hexdigest(), digest)
            for qid, scope in entry["questions"].items():
                with self.subTest(component=component, question=qid):
                    record = self.records[branch][qid]
                    actual = {}
                    for name in scope["dependencies"]:
                        if category == "Base" or name.startswith("image/"):
                            path = ROOT / branch / name
                        elif name == "geometry_dataset.py":
                            path = ROOT / "dataset_tools" / name
                        elif name.startswith("question_classes/"):
                            path = ROOT / branch / record["script"]
                        elif name.startswith("scenes/"):
                            path = ROOT / branch / record["scene"]
                        else:
                            path = ROOT / branch / "dataset_generator" / name
                        actual[name] = hashlib.sha256(path.read_bytes()).hexdigest()
                    self.assertEqual(actual, scope["dependencies"])
                    self.assertTrue(self.matches(component, entry, record, actual))

    def test_unknown_versions_new_paths_and_changed_records_are_rejected(self):
        for component, entry in self.entries.items():
            record, files = self.sample(component, entry)
            for field, value in (("runtime_dependencies", ["runtime/new.py"]),
                                 ("renderer_family", "new_family"), ("id", "Unknown999"),
                                 ("question", record["question"] + " changed")):
                with self.subTest(component=component, field=field):
                    self.assertFalse(self.matches(component, entry, {**record, field: value}, files))
            for field in ("previous_renderer_sha256", "current_renderer_sha256"):
                with self.subTest(component=component, version=field):
                    self.assertFalse(self.matches(component, {**entry, field: "0" * 64}, record, files))

    def test_missing_or_changed_old_dependency_is_rejected(self):
        for component, entry in self.entries.items():
            record, files = self.sample(component, entry)
            for name in files:
                with self.subTest(component=component, dependency=name):
                    missing = dict(files)
                    missing.pop(name)
                    self.assertFalse(self.matches(component, entry, record, missing))
                    self.assertFalse(self.matches(component, entry, record, {**files, name: "0" * 64}))

    def test_every_future_executor_edit_is_rejected(self):
        for component, entry in self.entries.items():
            record, files = self.sample(component, entry)
            with tempfile.TemporaryDirectory(prefix="mathpalette_compat_code_") as directory:
                clone = Path(directory)
                for name in entry["code_sha256"]:
                    path = clone / name
                    path.parent.mkdir(parents=True, exist_ok=True)
                    path.write_bytes((ROOT / name).read_bytes())
                with patch.object(compat, "ROOT", clone):
                    self.assertTrue(self.matches(component, entry, record, files))
                    for name in entry["code_sha256"]:
                        with self.subTest(component=component, code=name):
                            path = clone / name
                            original = path.read_bytes()
                            path.write_bytes(original + b"\n# unreviewed future change\n")
                            self.assertFalse(self.matches(component, entry, record, files))
                            path.write_bytes(original)

    def test_progress_requires_complete_unchanged_old_snapshot(self):
        for component, entry in self.entries.items():
            if not component.endswith("/Special"):
                continue
            branch = component.split("/")[0]
            old_rows = {qid: self.records[branch][qid] for qid in entry["questions"]}
            files = {name: digest for scope in entry["questions"].values()
                     for name, digest in scope["dependencies"].items()}
            files["dataset.jsonl"] = entry["previous_dataset_sha256"]
            original = {"files": files, "environment": {"test": "unchanged"}}
            manifest = {**original, "fingerprint": compat._hash(original)}
            previous = {"renderer_sha256": entry["previous_renderer_sha256"],
                        "baseline_fingerprint": manifest["fingerprint"]}
            current = {**previous, "renderer_sha256": entry["current_renderer_sha256"]}
            args = [component, previous, current, old_rows, manifest, manifest, old_rows]
            with self.subTest(component=component):
                self.assertTrue(compat.legacy_progress_matches(*args))
                for index, invalid in ((5, None), (6, None), (6, {}),
                                       (6, {next(iter(old_rows)): next(iter(old_rows.values()))})):
                    modified = copy.deepcopy(args)
                    modified[index] = invalid
                    self.assertFalse(compat.legacy_progress_matches(*modified))
                # Even a recomputed manifest fingerprint cannot hide a missing input.
                modified = [copy.deepcopy(value) for value in args]
                modified[5]["files"].pop("common_renderer.py")
                modified[5]["fingerprint"] = compat._hash({"files": modified[5]["files"],
                                                          "environment": modified[5]["environment"]})
                modified[1]["baseline_fingerprint"] = modified[5]["fingerprint"]
                self.assertFalse(compat.legacy_progress_matches(*modified))


if __name__ == "__main__":
    unittest.main()
