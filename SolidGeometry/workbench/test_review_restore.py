"""Restart regression fixtures under .runtime; never create real Pass records."""
import copy
import json
import shutil
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch

from review_store import Workbench
from workbench_io import (GENERATOR_VERSION, ROOT, SCHEMA_VERSION, WorkbenchError,
                          atomic_json, environment_versions, file_hash, load_config,
                          read_json, renderer_fingerprint)

PROJECT = ROOT.parents[1]
FIXTURES = PROJECT / ".runtime/solid_workbench_tests"


class ReviewRestoreTests(unittest.TestCase):
    def setUp(self):
        FIXTURES.mkdir(parents=True, exist_ok=True)
        temporary = tempfile.TemporaryDirectory(prefix="restore-fixture-", dir=FIXTURES)
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name).resolve()
        self.assertTrue(self.root.is_relative_to(FIXTURES.resolve()))
        self.branch = self.root / "SolidGeometry"
        self.output = self.branch / "special_variant"
        self.runtime = self.root / "runtime"
        self.config = load_config()
        self.config.update(dataset_root=str(self.branch), output_dir=str(self.output),
                           runtime_dir=str(self.runtime))
        ids = ("Solid01", "Solid249", "Solid251", "Solid252")
        records = [json.loads(line) for line in Path(self.config["dataset_file"]).read_text(
            encoding="utf-8-sig").splitlines() if line.strip()]
        self.records = {r["id"]: r for r in records if r["id"] in ids}
        self.adapter = SimpleNamespace(records=self.records,
            manifest={"files": {}, "environment": environment_versions(), "fingerprint": "fixture"},
            inspect_question=lambda qid: {}, question_dependencies=lambda qid: (f"scenes/{qid}.json",))
        # Reuse exact existing saved files inside an isolated fixture, without
        # calling a review API or generating an artificial formal approval.
        self.recipes = []
        for qid in ("Solid249", "Solid251"):
            shutil.copytree(PROJECT / "SolidGeometry/special_variant" / qid, self.output / qid)
            self.recipes.extend(read_json(self.output / qid / "recipes.json"))
        (self.output / "accepted_index.jsonl").write_text("".join(
            json.dumps(r, ensure_ascii=False, allow_nan=False) + "\n" for r in self.recipes), encoding="utf-8")
        self.previous = {"revision": 7, "candidate_id": None, "accepted": [],
                         "last_review": {"note": "TEMPORARY SOFTWARE TEST FIXTURE"}, "collected": False}
        self.progress = {
            "signature": {"generator_version": GENERATOR_VERSION, "plugin_schema_version": SCHEMA_VERSION,
                "environment": environment_versions(), "baseline_fingerprint": "fixture",
                "schema_sha256": file_hash(ROOT / "plugin.schema.json"),
                "renderer_sha256": renderer_fingerprint()},
            "output_relative": "special_variant", "current_question": "Solid01", "navigation_revision": 4,
            "questions": {"Solid01": copy.deepcopy(self.previous)}, "candidates": {},
        }

    def write_progress(self):
        atomic_json(self.runtime / "state/progress.json", self.progress)

    def open_bench(self):
        # Exercise real initialization and integrity validation; rendering itself
        # is verified separately by replaying the unchanged saved recipes.
        with patch("review_store.RendererAdapter", return_value=self.adapter), \
                patch("review_store.PluginRenderer"):
            return Workbench(self.config)

    def saved_bytes(self):
        return {p.relative_to(self.output).as_posix(): p.read_bytes()
                for p in self.output.rglob("*") if p.is_file()}

    def test_existing_cache_restores_new_questions_and_restart_is_idempotent(self):
        self.write_progress()
        before = self.saved_bytes()
        for _ in range(2):
            bench = self.open_bench()
            try:
                self.assertEqual(bench.progress["questions"]["Solid01"], self.previous)
                self.assertEqual(bench.progress["current_question"], "Solid01")
                self.assertEqual(bench.progress["navigation_revision"], 4)
                self.assertEqual(bench.progress["candidates"], {})
                self.assertEqual(bench.progress["questions"]["Solid252"]["accepted"], [])
                for qid in ("Solid249", "Solid251"):
                    self.assertEqual(bench.progress["questions"][qid]["accepted"],
                                     read_json(self.output / qid / "recipes.json"))
                    self.assertFalse(bench.progress["questions"][qid]["collected"])
            finally:
                bench.close()
        self.assertEqual(self.saved_bytes(), before)

    def test_cold_start_still_restores_saved_recipes(self):
        before = self.saved_bytes()
        bench = self.open_bench()
        try:
            for qid in ("Solid249", "Solid251"):
                self.assertEqual(bench.progress["questions"][qid]["accepted"],
                                 read_json(self.output / qid / "recipes.json"))
        finally:
            bench.close()
        self.assertEqual(self.saved_bytes(), before)

    def test_new_question_restores_special_case_collection(self):
        self.write_progress()
        record = {"question_id": "Solid252", "collected_at": "2026-11-03T00:00:00+00:00",
                  "special_case": True, "review_status": "pending",
                  "note": "TEMPORARY SOFTWARE TEST FIXTURE"}
        atomic_json(self.output / "Solid252/collection.json",
                    {"question_id": "Solid252", "status": "collected", "current": record, "history": []})
        (self.output / "collected_index.jsonl").write_text(
            json.dumps(record, ensure_ascii=False) + "\n", encoding="utf-8")
        before = self.saved_bytes()
        bench = self.open_bench()
        try:
            question = bench.progress["questions"]["Solid252"]
            self.assertTrue(question["collected"])
            self.assertEqual(question["collection_record"], record)
            self.assertEqual(question["collection_history"], [])
            self.assertNotIn("Solid252", bench.active_questions())
        finally:
            bench.close()
        self.assertEqual(self.saved_bytes(), before)

    def test_existing_question_conflict_is_still_rejected(self):
        self.progress["questions"]["Solid249"] = copy.deepcopy(self.previous)
        self.write_progress()
        before = self.saved_bytes()
        with self.assertRaisesRegex(WorkbenchError, "Solid249/recipes.json 与审核状态不一致"):
            self.open_bench()
        self.assertEqual(self.saved_bytes(), before)
        self.assertEqual(read_json(self.runtime / "state/progress.json"), self.progress)

    def test_corrupt_saved_image_is_still_rejected(self):
        self.write_progress()
        (self.output / "Solid249/images/C01.png").write_bytes(b"TEMPORARY CORRUPT TEST FIXTURE")
        before = self.saved_bytes()
        with self.assertRaisesRegex(WorkbenchError, "Solid249/C01 正式图或参数丢失/损坏"):
            self.open_bench()
        self.assertEqual(self.saved_bytes(), before)
        self.assertEqual(read_json(self.runtime / "state/progress.json"), self.progress)

    def pending_restart(self, change_scene=False, change_record=False):
        self.progress["signature"]["baseline_fingerprint"] = "previous-fixture"
        self.progress["questions"]["Solid01"]["candidate_id"] = "temporary-fixture"
        self.progress["candidates"]["temporary-fixture"] = {"status": "pending"}
        self.adapter.manifest["files"] = {"scenes/Solid01.json": "current-scene"}
        previous_manifest = copy.deepcopy(self.adapter.manifest)
        previous_manifest["fingerprint"] = "previous-fixture"
        if change_scene:
            previous_manifest["files"]["scenes/Solid01.json"] = "previous-scene"
        previous_records = {"Solid01": copy.deepcopy(self.records["Solid01"])}
        if change_record:
            previous_records["Solid01"]["answer"] = "TEMPORARY DIFFERENT TEST FIXTURE"
        atomic_json(self.runtime / "state/baseline_manifest.json", previous_manifest)
        atomic_json(self.runtime / "state/dataset_snapshot.json", previous_records)
        self.write_progress()
        with patch.object(Workbench, "_verify_package"):
            bench = self.open_bench()
        self.addCleanup(bench.close)
        return bench

    def test_catalog_growth_preserves_pending_question_with_unchanged_inputs(self):
        bench = self.pending_restart()
        self.assertEqual(bench.progress["questions"]["Solid01"], self.progress["questions"]["Solid01"])
        self.assertEqual(bench.progress["candidates"]["temporary-fixture"]["status"], "pending")
        self.assertEqual(len(bench.progress["questions"]["Solid249"]["accepted"]), 1)

    def test_changed_scene_still_invalidates_pending_candidate(self):
        bench = self.pending_restart(change_scene=True)
        self.assertIsNone(bench.progress["questions"]["Solid01"]["candidate_id"])
        self.assertEqual(bench.progress["candidates"]["temporary-fixture"]["status"], "stale_input")

    def test_changed_formal_record_still_invalidates_pending_candidate(self):
        bench = self.pending_restart(change_record=True)
        self.assertIsNone(bench.progress["questions"]["Solid01"]["candidate_id"])
        self.assertEqual(bench.progress["candidates"]["temporary-fixture"]["status"], "stale_input")


if __name__ == "__main__":
    unittest.main(verbosity=2)
