"""Special completion regression in isolated runtime fixtures; no real approvals.

Run separately for each branch:
    python -B dataset_tools/check_special_cases.py Analytics
The adapter is synthetic; real persistence, recovery and HTTP handlers are exercised.
Use --serve PORT for manual browser checks against the same disposable fixture.
"""
from __future__ import annotations

import copy
import json
from pathlib import Path
import sys
import tempfile
import threading
import unittest
from http.server import ThreadingHTTPServer
from types import SimpleNamespace
from unittest.mock import patch
from urllib.error import HTTPError
from urllib.request import Request, urlopen

PROJECT = Path(__file__).resolve().parents[1]
BRANCH = sys.argv.pop(1)
assert BRANCH in ("Analytics", "PlaneGeometry", "SolidGeometry")
sys.path.insert(0, str(PROJECT / BRANCH / "workbench"))
import review_store
from review_store import Workbench
from server import make_handler
from workbench_io import (WorkbenchError, atomic_json, canonical_hash, file_hash,
                          load_config, pixel_hash, read_json)

PREFIX = {"Analytics": "Ana", "PlaneGeometry": "Plane", "SolidGeometry": "Solid"}[BRANCH]
Q1, Q2 = PREFIX + "01", PREFIX + "02"
FIXTURES = PROJECT / ".runtime" / "special_case_tests"


class FixtureAdapter:
    def __init__(self, config):
        self.records = {qid: {"id": qid, "question": "Isolated software test fixture; not a user-approved question.",
                             "answer": "fixture", "answer_type": "text"} for qid in (Q1, Q2)}
        self.original_paths = {qid: PROJECT / BRANCH / "image" / (qid + ".png") for qid in self.records}
        self.sources = {qid: {"source_file": str(PROJECT / "fixture.py")} for qid in self.records}
        self.manifest = {"fingerprint": "isolated-test-baseline", "files": {
            "common_renderer.py": "fixture", "protocol.json": "fixture", "question_classes/fixture.py": "fixture",
            **{f"image/{qid}.png": "fixture" for qid in self.records}}}

    def inspect_question(self, qid):
        return {"objects": [], "snap_points": [], "canvas": {}}

    def dependencies(self, qid):
        return list(self.manifest["files"])

    question_dependencies = dependencies


class SpecialCases(unittest.TestCase):
    def setUp(self):
        FIXTURES.mkdir(parents=True, exist_ok=True)
        self.temp = tempfile.TemporaryDirectory(prefix=BRANCH + "-", dir=FIXTURES)
        self.addCleanup(self.temp.cleanup)
        self.home = Path(self.temp.name)
        self.config = load_config()
        self.config.update(dataset_root=str(self.home / "dataset"),
                           output_dir=str(self.home / "dataset" / "special_variant"),
                           runtime_dir=str(self.home / "runtime"))
        self.adapter_patch = patch.object(review_store, "RendererAdapter", FixtureAdapter)
        self.renderer_patch = patch.object(review_store, "PluginRenderer")
        self.adapter_patch.start()
        self.renderer_patch.start()
        self.addCleanup(self.adapter_patch.stop)
        self.addCleanup(self.renderer_patch.stop)
        self.store = Workbench(self.config)
        self.addCleanup(lambda: self.store.close())

    def reopen_store(self, fresh_cache=False):
        self.store.close()
        if fresh_cache:
            self.config["runtime_dir"] = str(self.home / "fresh_runtime")
        self.store = Workbench(self.config)

    def add_candidate(self):
        plugin = {"description": "ISOLATED AUTOMATED TEST ONLY", "params": {"actions": []}}
        package = self.store.root / "candidates" / "test-candidate"
        package.mkdir(parents=True)
        atomic_json(package / "plugin.json", plugin)
        (package / "image.png").write_bytes(self.store.adapter.original_paths[Q1].read_bytes())
        candidate = {"candidate_id": "test-candidate", "question_id": Q1, "status": "pending",
                     "params": plugin["params"], "description": plugin["description"],
                     "parameter_key": canonical_hash(plugin), "plugin_sha256": file_hash(package / "plugin.json"),
                     "png_sha256": file_hash(package / "image.png"), "pixel_sha256": pixel_hash(package / "image.png")}
        atomic_json(package / "manifest.json", candidate)
        self.store.progress["candidates"][candidate["candidate_id"]] = candidate
        self.store.progress["questions"][Q1]["candidate_id"] = candidate["candidate_id"]
        return copy.deepcopy(candidate)

    def add_accepted_fixture(self):
        candidate = self.add_candidate()
        recipe = {**candidate, "status": "passed", "slot_id": "C01",
                  "image_path": f"special_variant/{Q1}/images/C01.png",
                  "plugin_path": f"special_variant/{Q1}/plugins/C01.json"}
        for source, field in (("image.png", "image_path"), ("plugin.json", "plugin_path")):
            target = self.store.dataset_root / recipe[field]
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(self.store._package_file(candidate, source).read_bytes())
        question = self.store.progress["questions"][Q1]
        question["accepted"] = [recipe]
        question["candidate_id"] = None
        self.store._materialize(self.store.progress, Q1)
        return recipe

    def test_zero_variants_complete_idempotently_and_survive_both_restarts(self):
        token = self.store.context_token()
        result = self.store.mark_special(Q1, token)
        self.assertEqual(result["question_id"], Q2)
        self.assertEqual((result["collected_total"], result["special_case_total"], result["accepted_total"]), (1, 1, 0))
        entry = result["completed_questions"][0]
        self.assertTrue(entry["special_case"])
        self.assertEqual(entry["review_status"], "pending")
        collection = self.store.output / Q1 / "collection.json"
        saved = collection.read_bytes()
        record = read_json(collection)["current"]
        self.assertEqual(record["slots"], [])
        self.assertEqual(record["accepted_count"], 0)
        self.assertEqual(record["status"], "collected")
        self.assertFalse((self.store.output / Q1 / "recipes.json").exists())
        self.store.mark_special(Q1, token)
        self.assertEqual(saved, collection.read_bytes())
        for fresh in (False, True):
            self.reopen_store(fresh)
            self.assertEqual(self.store.snapshot()["special_case_total"], 1)
            self.assertEqual(self.store.active_questions(), [Q2])
            self.assertEqual(saved, collection.read_bytes())

    def test_pending_candidate_is_preserved_and_reopened_without_approval(self):
        before = self.add_candidate()
        package = self.store.root / "candidates" / before["candidate_id"]
        files = {p.name: p.read_bytes() for p in package.iterdir()}
        token = self.store.context_token()
        with self.assertRaises(WorkbenchError) as error:
            self.store.collect(Q1, token)
        self.assertEqual(error.exception.code, "pending_candidate")
        self.store.mark_special(Q1, token)
        self.reopen_store()
        reopened = self.store.reopen(Q1, self.store.context_token())
        self.assertEqual(reopened["candidate"]["candidate_id"], before["candidate_id"])
        self.assertEqual(reopened["candidate"]["status"], "pending")
        self.assertEqual(reopened["accepted_total"], 0)
        self.assertEqual(reopened["special_case_total"], 0)
        self.assertEqual(self.store.progress["candidates"][before["candidate_id"]], before)
        self.assertEqual(files, {p.name: p.read_bytes() for p in package.iterdir()})
        history = read_json(self.store.output / Q1 / "collection.json")["history"]
        self.assertTrue(history[0]["special_case"])
        self.assertIn("reopened_at", history[0])

    def test_normal_collect_still_requires_pass_and_keeps_accepted_files(self):
        with self.assertRaises(WorkbenchError):
            self.store.collect(Q1, self.store.context_token())
        recipe = self.add_accepted_fixture()
        before = {p: (self.store.dataset_root / p).read_bytes() for p in (recipe["image_path"], recipe["plugin_path"])}
        self.store.mark_special(Q1, self.store.context_token())
        self.reopen_store(True)
        self.store.reopen(Q1, self.store.context_token())
        result = self.store.collect(Q1, self.store.context_token())
        self.assertEqual(result["special_case_total"], 0)
        self.assertFalse(result["completed_questions"][0]["special_case"])
        saved = read_json(self.store.output / Q1 / "collection.json")
        self.assertTrue(saved["history"][0]["special_case"])
        self.assertEqual(saved["current"]["collection_number"], 2)
        self.assertEqual(before, {p: (self.store.dataset_root / p).read_bytes() for p in before})
        self.reopen_store()
        self.assertEqual(self.store.snapshot()["accepted_total"], 1)

    def test_stale_context_and_unknown_question_cannot_complete(self):
        with self.assertRaises(WorkbenchError) as error:
            self.store.mark_special(Q1, "expired")
        self.assertEqual(error.exception.code, "stale_context")
        with self.assertRaises(WorkbenchError):
            self.store.mark_special("unknown", self.store.context_token())
        old = self.store.context_token()
        self.store.navigate(Q2)
        with self.assertRaises(WorkbenchError):
            self.store.mark_special(Q1, old)
        self.assertEqual(self.store.snapshot()["collected_total"], 0)

    def test_interrupted_save_recovers_on_restart(self):
        original = review_store.atomic_write
        def fail_index(path, data):
            if Path(path).name == "collected_index.jsonl":
                raise OSError("simulated interrupted collection")
            return original(path, data)
        with patch.object(review_store, "atomic_write", side_effect=fail_index):
            with self.assertRaises(OSError):
                self.store.mark_special(Q1, self.store.context_token())
        self.assertTrue((self.store.state_dir / "pending_transaction.json").exists())
        self.reopen_store()
        self.assertEqual(self.store.snapshot()["special_case_total"], 1)
        self.assertFalse((self.store.state_dir / "pending_transaction.json").exists())
        self.store._validate_saved_files()

    def test_last_question_special_completion_and_reopen(self):
        self.store.mark_special(Q1, self.store.context_token())
        result = self.store.mark_special(Q2, self.store.context_token())
        self.assertEqual(result["status"], "completed")
        self.assertEqual(result["special_case_total"], 2)
        self.assertEqual(result["questions"], [])
        self.assertIsNone(result["question_id"])
        reopened = self.store.reopen(Q1, result["context_token"])
        self.assertEqual(reopened["question_id"], Q1)
        self.assertEqual(reopened["special_case_total"], 1)

    def test_http_special_route_requires_session_and_current_context(self):
        quick = SimpleNamespace(snapshot=lambda state: None)
        server = ThreadingHTTPServer(("127.0.0.1", 0), make_handler(self.store, quick))
        thread = threading.Thread(target=server.serve_forever, daemon=True)
        thread.start()
        try:
            url = f"http://127.0.0.1:{server.server_port}/api/mark-special"
            def post(session, context):
                body = json.dumps({"question_id": Q1, "context_token": context}).encode()
                request = Request(url, data=body, headers={"Content-Type": "application/json", "X-Review-Token": session})
                with urlopen(request) as response:
                    return json.load(response)
            with self.assertRaises(HTTPError) as error:
                post("wrong", self.store.context_token())
            self.assertEqual(error.exception.code, 403)
            with self.assertRaises(HTTPError) as error:
                post(self.store.review_token, "stale")
            self.assertEqual(error.exception.code, 409)
            result = post(self.store.review_token, self.store.context_token())
            self.assertEqual(result["special_case_total"], 1)
            self.assertEqual(result["accepted_total"], 0)
        finally:
            server.shutdown()
            server.server_close()
            thread.join()


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--serve":
        fixture = SpecialCases()
        fixture.setUp()
        server = ThreadingHTTPServer(("127.0.0.1", int(sys.argv[2])),
                                    make_handler(fixture.store, SimpleNamespace(snapshot=lambda state: None)))
        print(f"ISOLATED {BRANCH} browser fixture on {server.server_port}", flush=True)
        try:
            server.serve_forever()
        finally:
            server.server_close()
            fixture.doCleanups()
    else:
        unittest.main(verbosity=2)
