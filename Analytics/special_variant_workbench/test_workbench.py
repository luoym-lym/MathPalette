"""Meaningful integration checks; every simulated review uses disposable data."""
from __future__ import annotations

import copy
import importlib.util
import json
import shutil
import subprocess
import sys
import tempfile
import threading
import unittest
from http.server import ThreadingHTTPServer
from pathlib import Path
from unittest.mock import patch
from urllib.error import HTTPError
from urllib.request import Request, urlopen

from render_plugins import render_special_recipe
from review_store import Workbench
from server import make_handler
from workbench_io import (ROOT, WorkbenchError, atomic_json, canonical_hash, contained_path,
                          file_hash, load_config, parse_json, pixel_hash, read_json)


class WorkbenchTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.sandbox = tempfile.TemporaryDirectory(prefix="mathpalette-c-tests-")
        cls.base = Path(cls.sandbox.name)
        cls.seed_config = load_config()
        cls.seed_config.update(runtime_dir=str(cls.base / "seed"),
                               dataset_root=str(cls.base / "seed-dataset"),
                               output_dir=str(cls.base / "seed-dataset" / "special_variant"))
        # A full real-source, 80-image preflight once; subsequent cases share only this validated cache.
        seed = Workbench(cls.seed_config)
        cls.cache = read_json(seed.state_dir / "scene_metadata.json")
        cls.manifest = copy.deepcopy(seed.adapter.manifest)
        cls.adapter, cls.metadata = seed.adapter, seed.metadata
        seed.close()
        cls.counter = 0

    @classmethod
    def tearDownClass(cls):
        cls.sandbox.cleanup()

    def setUp(self):
        type(self).counter += 1
        self.case = self.base / f"case-{self.counter}"
        self.config = load_config()
        self.config.update(runtime_dir=str(self.case / "runtime"),
                           dataset_root=str(self.case / "construct_dataset"),
                           output_dir=str(self.case / "construct_dataset" / "special_variant"))
        config_path = self.case / "test-config.json"
        self.config["config_path"] = str(config_path)
        atomic_json(config_path, self.config)
        atomic_json(Path(self.config["runtime_dir"]) / "state" / "scene_metadata.json", self.cache)
        self.w = Workbench(self.config)
        self.plugin_path = self.case / "draft.json"
        self.plugin = {"plugin_schema_version": "1.0.0", "question_id": "Ana01", "category": "C",
                       "operation": "C_manual", "description": "test only", "params": {"actions": [
                           {"type": "add_point", "id": "decoy", "xy": [0.4, 1.2]}]}}
        self.write()

    def tearDown(self):
        self.w.close()

    def write(self, plugin=None):
        atomic_json(self.plugin_path, plugin or self.plugin)

    def submit(self, replace=None, token=None):
        return self.w.submit(self.plugin_path, token or self.w.context()["context_token"], replace)

    def review(self, candidate, decision="pass", note="", token=None):
        return self.w.review(candidate["question_id"], candidate["candidate_id"], decision,
                             token or self.w.context_token(), candidate["pixel_sha256"], candidate["parameter_key"], note)

    def restart(self):
        self.w.close()
        self.w = Workbench(self.config)

    def test_all_eighty_originals_exact_and_manifest_explicit(self):
        self.assertEqual(len(self.metadata), 80)
        self.assertEqual(len(self.manifest["files"]), 87)
        self.assertFalse(any("special_variant" in name or "base_variant" in name for name in self.manifest["files"]))
        self.assertTrue(all(meta["original_pixel_sha256"] for meta in self.metadata.values()))

    def test_context_reads_are_pure(self):
        before = file_hash(self.w.state_dir / "progress.json")
        first, second = self.w.context(), self.w.context()
        self.assertEqual(first["context_token"], second["context_token"])
        self.assertEqual(before, file_hash(self.w.state_dir / "progress.json"))
        self.assertIsNone(first["candidate"])
        self.assertFalse(self.w.output.exists())

    def test_drawing_scene_all_questions_coordinates_and_targets(self):
        import numpy as np
        from drawing_board import describe_scene
        for qid in self.metadata:
            with self.subTest(question=qid):
                scene = describe_scene(self.adapter, qid)
                self.assertEqual((scene["width"], scene["height"]), (768, 768))
                np.testing.assert_allclose(np.array(scene["pixel_to_data"]) @ np.array(scene["data_to_pixel"]), np.eye(3), atol=1e-12)
                left, top, right, bottom = scene["plot_bounds"]
                np.testing.assert_allclose(np.array(scene["data_to_pixel"]) @ [-8, 8, 1], [left, top, 1], atol=1e-9)
                np.testing.assert_allclose(np.array(scene["data_to_pixel"]) @ [8, -8, 1], [right, bottom, 1], atol=1e-9)
                expected = {o["id"] for o in self.metadata[qid]["objects"] if o["styleable"]}
                self.assertEqual({o["id"] for o in scene["targets"]}, expected)
                for target in scene["targets"]:
                    for path in target["paths"]:
                        self.assertTrue(np.isfinite(path).all())

    def test_drawing_paths_preserve_nan_gaps_and_flatten_outlines(self):
        from drawing_board import _pixel_paths
        from matplotlib.path import Path as MplPath
        from matplotlib.transforms import Affine2D
        paths = _pixel_paths(MplPath([[1, 1], [2, 2], [float("nan"), 0], [5, 5], [6, 6]]), Affine2D(), 768, 768)
        self.assertEqual(paths, [[[1, 767], [2, 766]], [[5, 763], [6, 762]]])
        circle = _pixel_paths(MplPath.unit_circle(), Affine2D().scale(40).translate(300, 300), 768, 768)
        self.assertGreater(len(circle[0]), 20)

    def test_drawing_preview_pass_same_format_pixels_and_offline_redraw(self):
        from drawing_board import PRESETS
        self.plugin["params"]["actions"] = [
            {**PRESETS["point"], "id": "board_point_1", "xy": [1, 3]},
            {**PRESETS["line"], "id": "board_line_1", "endpoints": [[-2, 1], [2, 4]]},
            {"type": "set_curve_style", "target": "curve_001", "color": "#DC2626", "linestyle": "dashed", "linewidth_pt": 1.0}]
        before = file_hash(self.w.state_dir / "progress.json")
        preview = self.w.drawing_preview(self.plugin, self.w.context_token())
        self.assertEqual(before, file_hash(self.w.state_dir / "progress.json"))
        self.assertFalse(self.w.output.exists())
        self.assertIsNone(self.w.context()["candidate"])
        result = self.w.drawing_submit(preview["plugin"], self.w.context_token(), None, preview["pixel_sha256"], preview["parameter_key"])
        candidate = result["candidate"]
        self.assertEqual(candidate["pixel_sha256"], preview["pixel_sha256"])
        self.assertFalse(self.w.output.exists())
        self.review(candidate)
        recipe = self.w.snapshot()["accepted"][0]
        self.assertEqual(recipe["phase"], "manual")
        self.assertEqual(recipe["operation"], "C_manual")
        self.assertEqual(recipe["params"], preview["plugin"]["params"])
        self.assertTrue(render_special_recipe(recipe, config_path=self.config["config_path"])["matches_accepted"])
        self.restart()
        self.assertEqual(self.w.snapshot()["accepted"][0]["pixel_sha256"], preview["pixel_sha256"])

    def test_drawing_agent_handoff_and_stale_preview_protection(self):
        agent = self.submit()
        token = self.w.context_token()
        plugin = self.w._verify_package(agent)
        plugin["params"]["actions"].append({"type": "add_point", "id": "board_point_1", "xy": [2, 5]})
        preview = self.w.drawing_preview(plugin, token, agent["candidate_id"])
        self.assertEqual(self.w.context()["candidate"]["candidate_id"], agent["candidate_id"])
        with self.assertRaises(WorkbenchError) as error:
            self.w.drawing_submit(plugin, token, agent["candidate_id"], "not-displayed", preview["parameter_key"])
        self.assertEqual(error.exception.code, "stale_preview")
        self.assertEqual(self.w.context()["candidate"]["candidate_id"], agent["candidate_id"])
        result = self.w.drawing_submit(plugin, token, agent["candidate_id"], preview["pixel_sha256"], preview["parameter_key"])
        self.assertEqual(self.w.status(agent["candidate_id"])["status"], "superseded")
        self.assertEqual(len(result["candidate"]["params"]["actions"]), 2)
        with self.assertRaises(WorkbenchError): self.w.drawing_preview(plugin, token, agent["candidate_id"])
        self.review(result["candidate"], "reject")
        self.assertFalse(Path(result["candidate"]["image_path"]).exists())
        self.assertFalse(self.w.output.exists())

    def test_drawing_http_requires_page_session(self):
        server = ThreadingHTTPServer(("127.0.0.1", 0), make_handler(self.w))
        thread = threading.Thread(target=server.serve_forever, daemon=True); thread.start()
        url = f"http://127.0.0.1:{server.server_port}"
        try:
            with urlopen(url + "/api/drawing-scene/Ana01") as response:
                self.assertEqual(json.load(response)["presets"]["point"]["color"], "#DC2626")
            data = json.dumps({"plugin": self.plugin, "context_token": self.w.context_token()}).encode()
            headers = {"Content-Type": "application/json"}
            with self.assertRaises(HTTPError) as error: urlopen(Request(url + "/api/drawing-preview", data=data, headers=headers))
            self.assertEqual(error.exception.code, 403)
            headers["X-Review-Token"] = self.w.review_token
            with urlopen(Request(url + "/api/drawing-preview", data=data, headers=headers)) as response:
                self.assertTrue(json.load(response)["image_url"].startswith("data:image/png;base64,"))
        finally:
            server.shutdown(); server.server_close(); thread.join()

    def test_schema_unknown_action_unknown_fields_and_missing_values(self):
        changes = [{"status": "passed"}, {"params": {"actions": [{"type": "python", "code": "eval()"}]}},
                   {"question_id": "Ana81"}, {"category": "B"}, {"params": {"actions": []}}]
        for change in changes:
            with self.subTest(change=change):
                plugin = {**self.plugin, **change}
                with self.assertRaises(WorkbenchError): self.w.renderer.normalize(plugin)

    def test_schema_rejects_nonfinite_bool_as_number_duplicate_keys(self):
        for value in (float("nan"), float("inf"), 10**1000, True, "right 0.2"):
            plugin = copy.deepcopy(self.plugin)
            plugin["params"]["actions"][0]["xy"][0] = value
            with self.subTest(value=value), self.assertRaises(WorkbenchError): self.w.renderer.normalize(plugin)
        for text in ('{"a":1,"a":2}', '{"a":NaN}', '{"a":Infinity}'):
            with self.assertRaises(WorkbenchError): parse_json(text)

    def test_object_ids_stable_original_artists_mapped(self):
        for qid in ("Ana04", "Ana09", "Ana48", "Ana80"):
            a, b = self.adapter.scene(qid), self.adapter.scene(qid)
            try:
                self.assertEqual(a.objects, b.objects)
                for obj in a.objects:
                    if obj.get("styleable"):
                        self.assertIn(obj["id"], a.artists)
                        self.assertNotIn(obj["kind"], ("coordinate_axis", "coordinate_grid"))
            finally: a.close(); b.close()

    def test_invalid_targets_and_duplicate_ids(self):
        for actions in ([{"type": "set_curve_style", "target": "curve_999"}],
                        [{"type": "set_curve_style", "target": "axis_x"}],
                        [{"type": "add_point", "id": "curve_001", "xy": [1, 1]}],
                        [self.plugin["params"]["actions"][0]] * 2):
            with self.subTest(actions=actions), self.assertRaises(WorkbenchError):
                self.w.renderer.normalize({**self.plugin, "params": {"actions": actions}})

    def test_four_actions_alone_and_combined(self):
        example = read_json(ROOT / "examples" / "Ana04_combined.json")
        for action in example["params"]["actions"]:
            _, data, digest = self.w.renderer.render({**example, "params": {"actions": [action]}})
            self.assertNotEqual(digest, self.metadata["Ana04"]["original_pixel_sha256"])
            self.assertEqual(digest, pixel_hash(data))
        _, _, digest = self.w.renderer.render(example)
        self.assertNotEqual(digest, self.metadata["Ana04"]["original_pixel_sha256"])

    def test_invalid_dash_zero_line_and_no_pixel_change(self):
        for action in ({"type": "add_line", "id": "line", "endpoints": [[1, 1], [1, 1]]},
                       {"type": "add_line", "id": "line", "endpoints": [[1, 1], [2, 2]], "dash_pattern_pt": [4, 2]},
                       {"type": "add_line", "id": "line", "endpoints": [[1, 1], [2, 2]], "linestyle": "dashed", "dash_pattern_pt": [4, 2, 1]}):
            with self.assertRaises(WorkbenchError):
                self.w.renderer.normalize({**self.plugin, "params": {"actions": [action]}})
        outside = copy.deepcopy(self.plugin)
        outside["params"]["actions"][0]["xy"] = [40, 40]
        with self.assertRaisesRegex(WorkbenchError, "像素变化"): self.w.renderer.render(outside)

    def test_freeze_draft_edits_do_not_change_candidate_or_pass(self):
        candidate = self.submit()
        png = Path(candidate["image_path"]).read_bytes()
        frozen = Path(candidate["plugin_path"]).read_bytes()
        self.plugin["params"]["actions"][0]["xy"] = [2, 2]
        self.write()
        self.assertEqual(png, Path(candidate["image_path"]).read_bytes())
        self.review(candidate)
        recipe = self.w.snapshot()["accepted"][0]
        self.assertEqual(png, self.w._accepted_path(recipe["image_path"]).read_bytes())
        self.assertEqual(frozen, self.w._accepted_path(recipe["plugin_path"]).read_bytes())
        self.assertEqual(recipe["params"]["actions"][0]["xy"], [0.4, 1.2])

    def test_reject_deletes_only_current_png_and_keeps_feedback(self):
        candidate = self.submit()
        sentinel = self.w.root / "candidates" / "untouched.png"
        sentinel.write_bytes(b"sentinel")
        self.review(candidate, "reject", "point too low")
        context = self.w.context()
        self.assertIsNone(context["candidate"])
        self.assertEqual(context["last_review"]["note"], "point too low")
        self.assertEqual(context["last_review"]["plugin"]["params"]["actions"][0]["xy"], [0.4, 1.2])
        self.assertIsNone(self.w.status(candidate["candidate_id"])["image_path"])
        self.assertTrue(Path(candidate["plugin_path"]).exists())
        self.assertEqual(sentinel.read_bytes(), b"sentinel")
        self.assertEqual(self.w.snapshot()["status"], "waiting")
        self.assertFalse(self.w.output.exists())

    def test_default_pending_no_overwrite_and_replace_supersedes(self):
        old = self.submit()
        with self.assertRaises(WorkbenchError) as error: self.submit()
        self.assertEqual(error.exception.code, "pending_candidate")
        new = self.submit(replace=old["candidate_id"])
        self.assertEqual(self.w.status(old["candidate_id"])["status"], "superseded")
        self.assertEqual(self.w.context()["candidate"]["candidate_id"], new["candidate_id"])
        with self.assertRaises(WorkbenchError): self.review(old)

    def test_failed_replacement_preserves_pending(self):
        old = self.submit()
        self.plugin["params"]["actions"][0]["xy"] = [90, 90]
        self.write()
        with self.assertRaises(WorkbenchError): self.submit(replace=old["candidate_id"])
        self.assertEqual(self.w.context()["candidate"]["candidate_id"], old["candidate_id"])
        self.assertEqual(self.w.status(old["candidate_id"])["status"], "pending")
        self.assertTrue(Path(old["image_path"]).is_file())

    def test_navigation_roundtrip_restores_pending_and_invalidates_context(self):
        old = self.submit()
        token = self.w.context_token()
        self.w.navigate("Ana02")
        self.assertIsNone(self.w.context()["candidate"])
        with self.assertRaises(WorkbenchError): self.review(old)
        self.w.navigate("Ana01")
        self.assertEqual(self.w.context()["candidate"]["candidate_id"], old["candidate_id"])
        with self.assertRaises(WorkbenchError): self.submit(replace=old["candidate_id"], token=token)

    def test_navigation_during_render_cannot_publish(self):
        token = self.w.context_token()
        original = self.w.renderer.render
        def interleaved(*args, **kwargs):
            value = original(*args, **kwargs)
            self.w.navigate("Ana02")
            return value
        with patch.object(self.w.renderer, "render", side_effect=interleaved):
            with self.assertRaises(WorkbenchError) as error: self.submit(token=token)
        self.assertEqual(error.exception.code, "stale_context")
        self.assertEqual(len(self.w.progress["candidates"]), 0)
        self.assertEqual(self.w.context()["question_id"], "Ana02")

    def test_review_during_replacement_render_cannot_publish(self):
        old = self.submit()
        original = self.w.renderer.render
        def interleaved(*args, **kwargs):
            value = original(*args, **kwargs)
            self.review(old, "reject")
            return value
        with patch.object(self.w.renderer, "render", side_effect=interleaved):
            with self.assertRaises(WorkbenchError) as error: self.submit(replace=old["candidate_id"])
        self.assertEqual(error.exception.code, "stale_context")
        self.assertEqual(len(self.w.progress["candidates"]), 1)
        self.assertEqual(self.w.status(old["candidate_id"])["status"], "rejected")

    def test_pass_idempotent_sequential_slots_and_stays_current(self):
        first = self.submit()
        self.review(first)
        self.assertTrue(self.review(first)["idempotent"])
        second = self.submit()
        self.review(second)
        snapshot = self.w.snapshot()
        self.assertEqual([r["slot_id"] for r in snapshot["accepted"]], ["C01", "C02"])
        self.assertEqual(snapshot["question_id"], "Ana01")
        self.assertIsNone(snapshot["candidate"])
        index = (self.w.output / "accepted_index.jsonl").read_text(encoding="utf-8").splitlines()
        self.assertEqual(len(index), 2)
        self.assertEqual(self.manifest, self.w.adapter.make_manifest())

    def test_no_quota_after_six_passes(self):
        for _ in range(6): self.review(self.submit())
        self.assertEqual(self.w.snapshot()["accepted"][-1]["slot_id"], "C06")

    def test_tampered_candidate_png_and_plugin_block_review(self):
        candidate = self.submit()
        image = Path(candidate["image_path"])
        data = image.read_bytes()
        image.write_bytes(b"corrupt")
        with self.assertRaises(WorkbenchError): self.review(candidate)
        image.write_bytes(data)
        plugin = read_json(candidate["plugin_path"])
        plugin["description"] = "modified"
        atomic_json(candidate["plugin_path"], plugin)
        with self.assertRaises(WorkbenchError): self.review(candidate)
        self.assertFalse(self.w.output.exists())

    def test_request_display_hash_must_match(self):
        candidate = self.submit()
        with self.assertRaises(WorkbenchError):
            self.w.review("Ana01", candidate["candidate_id"], "pass", self.w.context_token(), "fake", candidate["parameter_key"])
        self.assertIsNotNone(self.w.context()["candidate"])

    def test_restart_pending_rejected_and_accepted(self):
        first = self.submit(); self.review(first)
        second = self.submit(); self.review(second, "reject", "feedback")
        third = self.submit(); token = self.w.context_token()
        self.restart()
        self.assertEqual(self.w.context()["candidate"]["candidate_id"], third["candidate_id"])
        self.assertEqual(self.w.context()["last_review"]["note"], "feedback")
        self.assertEqual(len(self.w.snapshot()["accepted"]), 1)
        with self.assertRaises(WorkbenchError): self.submit(replace=third["candidate_id"], token=token)

    def test_pass_transaction_recovery_after_materialize_failure(self):
        candidate = self.submit()
        with patch.object(self.w, "_materialize", side_effect=OSError("simulated disk failure")):
            with self.assertRaises(OSError): self.review(candidate)
        self.assertTrue((self.w.state_dir / "pending_transaction.json").exists())
        self.restart()
        self.assertEqual(len(self.w.snapshot()["accepted"]), 1)
        self.assertTrue(self.review(candidate)["idempotent"])
        self.assertFalse((self.w.state_dir / "pending_transaction.json").exists())

    def test_reject_transaction_recovery_after_png_deletion(self):
        candidate = self.submit()
        import review_store
        real_write = review_store.atomic_json
        def fail_progress(path, data):
            if Path(path).name == "progress.json": raise OSError("simulated progress write failure")
            return real_write(path, data)
        with patch.object(review_store, "atomic_json", side_effect=fail_progress):
            with self.assertRaises(OSError): self.review(candidate, "reject", "retry")
        self.assertFalse(Path(candidate["image_path"]).exists())
        self.restart()
        self.assertEqual(self.w.status(candidate["candidate_id"])["status"], "rejected")
        self.assertEqual(self.w.context()["last_review"]["note"], "retry")

    def test_submit_transaction_recovery_after_progress_failure(self):
        import review_store
        real_write = review_store.atomic_json
        def fail_progress(path, data):
            if Path(path).name == "progress.json": raise OSError("simulated disk failure")
            return real_write(path, data)
        with patch.object(review_store, "atomic_json", side_effect=fail_progress):
            with self.assertRaises(OSError): self.submit()
        self.restart()
        self.assertEqual(self.w.context()["candidate"]["status"], "pending")
        self.assertTrue(Path(self.w.context()["candidate"]["image_path"]).is_file())

    def test_single_writer_process(self):
        with self.assertRaises(WorkbenchError) as error: Workbench(self.config)
        self.assertEqual(error.exception.code, "writer_locked")

    def test_path_traversal_and_windows_candidate_symlink_containment(self):
        with self.assertRaises(WorkbenchError): contained_path(self.w.root / "candidates", "../elsewhere.png")
        candidate = self.submit()
        candidate["candidate_id"] = "../../construct_dataset"
        with self.assertRaises(WorkbenchError): self.w._package_file(candidate, "image.png")

    def test_formal_file_tamper_blocks_restart(self):
        candidate = self.submit(); self.review(candidate)
        recipe = self.w.snapshot()["accepted"][0]
        self.w._accepted_path(recipe["image_path"]).write_bytes(b"corrupt")
        self.w.close()
        with self.assertRaises(WorkbenchError): Workbench(self.config)

    def test_redraw_matches_pixels_defaults_changes_do_not_matter(self):
        candidate = self.submit(); self.review(candidate)
        recipe = self.w.snapshot()["accepted"][0]
        changed_config = copy.deepcopy(self.config)
        changed_config["defaults"]["add_point"]["color"] = "#0000FF"
        changed_config["defaults"]["add_point"]["size_pt2"] = 300
        atomic_json(self.config["config_path"], changed_config)
        result = render_special_recipe(recipe, config_path=self.config["config_path"])
        self.assertTrue(result["matches_accepted"])
        self.assertEqual(result["pixel_sha256"], candidate["pixel_sha256"])
        self.assertEqual(pixel_hash(result["image_path"]), candidate["pixel_sha256"])
        self.assertTrue(Path(result["image_path"]).is_relative_to(self.w.root / "reproduced"))
        with self.assertRaises(WorkbenchError): render_special_recipe(recipe, self.w._accepted_path(recipe["image_path"]), self.config["config_path"])
        for unsafe in (self.w.root / "state" / "progress.png", self.w.root / "drafts" / "plugin.png", self.case / "overwrite.py"):
            with self.subTest(target=unsafe), self.assertRaises(WorkbenchError):
                render_special_recipe(recipe, unsafe, self.config["config_path"])

    def test_redraw_rejects_version_or_parameter_changes(self):
        candidate = self.submit(); self.review(candidate)
        recipe = self.w.snapshot()["accepted"][0]
        for key, value in (("generator_version", "C-next"), ("baseline_fingerprint", "changed"),
                           ("parameter_key", "changed"), ("renderer_sha256", "changed"), ("schema_sha256", "changed")):
            with self.subTest(key=key), self.assertRaises(WorkbenchError):
                render_special_recipe({**recipe, key: value}, config_path=self.config["config_path"])

    def test_generated_functions_and_portable_relative_root(self):
        self.review(self.submit())
        code = (self.w.output / "Ana01" / "draw_variants.py").read_text(encoding="utf-8")
        self.assertIn("def draw_C01(output_path=None)", code)
        self.assertNotIn("draw_C02", code)
        self.assertNotIn(str(ROOT), code)
        self.assertNotIn("first_process", code)
        # Build a relocated layout with symlink-free copies of all read-only inputs.
        moved = self.case / "relocated" / "MathPalette"
        shutil.copytree(ROOT, moved / "special_variant_workbench", ignore=shutil.ignore_patterns(
            "state", "candidates", "drafts", "reproduced", "verification", "__pycache__"))
        shutil.copytree(Path(load_config()["dataset_root"]), moved / "construct_dataset", ignore=shutil.ignore_patterns(
            "base_variant", "special_variant", "val_script", "__pycache__"))
        shutil.copytree(self.w.output, moved / "construct_dataset" / "special_variant")
        result = subprocess.run([sys.executable, "-B", str(moved / "construct_dataset" / "special_variant" / "Ana01" / "draw_variants.py"), "C01"],
                                cwd=tempfile.gettempdir(), capture_output=True, text=True, encoding="utf-8", timeout=30)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertTrue(json.loads(result.stdout)["matches_accepted"])

    def test_http_and_cli_from_another_cwd(self):
        server = ThreadingHTTPServer(("127.0.0.1", 0), make_handler(self.w))
        thread = threading.Thread(target=server.serve_forever, daemon=True); thread.start()
        url = f"http://127.0.0.1:{server.server_port}"
        def cli(*args):
            result = subprocess.run([sys.executable, "-B", str(ROOT / "agent_cli.py"), "--url", url, *args],
                                    cwd=tempfile.gettempdir(), capture_output=True, text=True, encoding="utf-8", timeout=30)
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            return json.loads(result.stdout)
        try:
            context = cli("context")
            self.assertEqual(context["question_id"], "Ana01")
            self.assertTrue(cli("validate", "--plugin", str(self.plugin_path))["valid"])
            candidate = cli("submit", "--plugin", str(self.plugin_path), "--context-token", context["context_token"])
            self.assertEqual(cli("status", "--candidate", candidate["candidate_id"])["status"], "pending")
            with urlopen(url + "/api/state") as response:
                self.assertEqual(json.load(response)["candidate"]["candidate_id"], candidate["candidate_id"])
            with urlopen(url + candidate["image_url"]) as response:
                self.assertEqual(pixel_hash(response.read()), candidate["pixel_sha256"])
            with self.assertRaises(HTTPError) as error:
                urlopen(Request(url + "/api/review", data=b"{}", headers={"Content-Type": "application/json"}))
            self.assertEqual(error.exception.code, 403)
            ref = cli("highlight", "--object", "curve_001")
            self.assertTrue(ref["reference_only"])
            self.assertFalse(self.w.output.exists())
        finally:
            server.shutdown(); server.server_close(); thread.join()


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"): sys.stdout.reconfigure(encoding="utf-8")
    unittest.main(verbosity=2)
