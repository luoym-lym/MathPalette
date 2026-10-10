"""Behavioral checks. Every synthetic review is confined to a temporary store.

Run: python -B -m unittest -v test_workbench
The full collection test exercises 800 simulated decisions and all 800 public
redraw functions, then deletes that isolated temporary collection.
"""

from __future__ import annotations

import ast
import copy
import importlib.util
import io
import json
import random
import tempfile
import threading
import unittest
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from unittest import mock
from urllib.error import HTTPError
from urllib.request import Request, urlopen

import numpy as np
from PIL import Image, ImageColor

import generate_variants
import review_store
from generate_variants import GROUPS, OPERATIONS, VariantGenerator
from renderer_adapter import RendererAdapter, manifest_for, scene_png
from review_store import Workbench
from server import ThreadingHTTPServer, make_handler
from workbench_io import (GENERATOR_VERSION, ROOT, WorkbenchError, atomic_json, atomic_write,
                          canonical_hash, contained_path, environment_versions, load_config, pixel_hash, read_json)

_RUNTIME = None


def runtime():
    global _RUNTIME
    if _RUNTIME is None:
        config = load_config()
        adapter = RendererAdapter(config["source_dir"], read_json(ROOT / "state" / "baseline_manifest.json"))
        signature = {"generator_version": GENERATOR_VERSION, "environment": environment_versions(),
                     "baseline_fingerprint": adapter.manifest["fingerprint"], "config_fingerprint": canonical_hash(config)}
        cached_path = ROOT / "state" / "availability.json"
        cached = read_json(cached_path) if cached_path.exists() else {}
        if cached.get("signature") != signature:
            cached = {"signature": signature, "prechecks": {qid: adapter.inspect_question(qid) for qid in adapter.records}}
        _RUNTIME = config, adapter, cached
    return _RUNTIME


class IsolatedStore(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="mathpalette-test-")
        self.root = Path(self.temp.name).resolve()
        self.assertTrue(self.root.is_relative_to(Path(tempfile.gettempdir()).resolve()))
        self.assertTrue(self.root.name.startswith("mathpalette-test-"))
        config, _, cached = runtime()
        atomic_json(self.root / "state" / "availability.json", cached)
        self.store = Workbench(self.root, config)
        self.store.ensure_candidate()

    def tearDown(self):
        self.store.close()
        self.temp.cleanup()

    def current(self):
        return self.store.snapshot()["candidate"]

    def reject(self):
        return self.store.review(self.current()["candidate_id"], "reject")

    def accept(self):
        return self.store.review(self.current()["candidate_id"], "pass")

    def skip(self):
        return self.store.skip(self.current()["candidate_id"])

    def test_initial_order_and_finite_rejection(self):
        self.assertEqual(self.current()["operation"], "A1")
        first = self.current()
        first_path = self.root / first["image_path"]
        second = self.reject()["candidate"]
        self.assertFalse(first_path.exists())
        self.assertEqual(second["operation"], "A1")
        self.assertNotEqual(first["pixel_sha256"], second["pixel_sha256"])
        self.assertEqual(self.reject()["candidate"]["operation"], "A2")
        a2 = self.current()
        result = self.reject()
        self.assertFalse((self.root / a2["image_path"]).exists())
        self.assertEqual(result["candidate"]["operation"], "A3")
        self.assertEqual(result["operations"]["A1"]["status"], "exhausted")
        self.assertEqual(result["operations"]["A2"]["status"], "exhausted")
        self.assertEqual(result["counts"], {"A": 0, "B": 0})

    def test_pass_uses_exact_png_and_is_idempotent(self):
        candidate = self.current()
        png = (self.root / candidate["image_path"]).read_bytes()
        # Make every redraw fail: accepting the displayed image must still
        # commit. Only the attempt to prepare the next candidate should fail.
        with mock.patch.object(self.store.generator, "render", side_effect=WorkbenchError("injected next-render failure")) as renderer:
            result = self.accept()
        self.assertEqual(result["counts"]["A"], 1)
        self.assertTrue(result["error"])
        self.assertEqual(renderer.call_args.args[1], "A2")
        recipe = result["accepted"][0]
        self.assertEqual((self.root / recipe["image_path"]).read_bytes(), png)
        self.assertFalse((self.root / candidate["image_path"]).exists())
        duplicate = self.store.review(candidate["candidate_id"], "pass")
        self.assertEqual(duplicate["counts"]["A"], 1)
        with self.assertRaises(WorkbenchError):
            self.store.review(candidate["candidate_id"], "reject")
        with self.assertRaises(WorkbenchError):
            self.store.review("expired-unknown-id", "pass")
        self.assertEqual(self.store.retry()["candidate"]["operation"], "A2")

    def test_parallel_double_click_counts_once(self):
        cid = self.current()["candidate_id"]
        with ThreadPoolExecutor(max_workers=2) as executor:
            results = list(executor.map(lambda _: self.store.review(cid, "pass"), range(2)))
        self.assertEqual([r["counts"]["A"] for r in results], [1, 1])
        self.assertEqual(len(list((self.root / "accepted" / "Ana01" / "images").glob("*.png"))), 1)

    def test_navigation_restart_and_candidate_recovery(self):
        initial = self.current()
        self.store.navigate("Ana02")
        with self.assertRaises(WorkbenchError):
            self.store.review(initial["candidate_id"], "pass")
        self.store.navigate("Ana01")
        self.assertEqual(self.current()["candidate_id"], initial["candidate_id"])
        self.store.close()
        self.store = Workbench(self.root, load_config())
        self.assertEqual(self.current()["params"], initial["params"])
        self.assertEqual(self.current()["candidate_id"], initial["candidate_id"])
        (self.root / initial["image_path"]).unlink()
        with mock.patch.object(self.store.generator, "sample", side_effect=AssertionError("must not resample")):
            self.store.ensure_candidate()
        self.assertEqual(pixel_hash(self.root / initial["image_path"]), initial["pixel_sha256"])

    def test_skip_block_resume_without_passing(self):
        for _ in range(3):
            self.skip()
        self.assertEqual(self.current()["operation"], "A4")
        first = self.current()
        second = self.reject()["candidate"]
        self.assertNotEqual(first["params"]["background_color"], second["params"]["background_color"])
        state = self.reject()
        self.assertTrue(state["plan"]["blocked"])
        self.assertEqual(state["counts"], {"A": 0, "B": 0})
        self.assertIsNone(state["candidate"])
        self.assertEqual(self.store.retry("A3")["candidate"]["operation"], "A3")
        self.assertEqual(self.store.snapshot()["global"]["accepted"], 0)

    def test_generation_failure_is_bounded_and_skippable(self):
        self.skip()  # A2 is now current.
        self.reject()  # A3 is now current.
        with mock.patch.object(self.store.generator, "render", side_effect=WorkbenchError("injected invalid geometry")) as render:
            result = self.reject()
        self.assertEqual(render.call_count, self.store.config["max_candidate_attempts"])
        self.assertTrue(result["error"])
        self.assertIsNone(result["candidate"])
        state = self.store.skip(operation="A3")
        self.assertEqual(state["candidate"]["operation"], "A4")

    def test_restoring_skipped_finite_type_does_not_treat_it_as_rejected(self):
        self.skip()
        a2 = self.current()
        self.assertEqual(a2["operation"], "A2")
        self.skip()
        self.store.retry("A2")
        result = self.reject()  # Finish the already displayed A3 candidate.
        self.assertEqual(result["candidate"]["operation"], "A2")
        self.assertEqual(result["candidate"]["pixel_sha256"], a2["pixel_sha256"])
        self.assertNotEqual(result["candidate"]["candidate_id"], a2["candidate_id"])
        self.assertEqual(result["counts"], {"A": 0, "B": 0})

    def test_pixel_duplicates_are_excluded_even_with_different_parameters(self):
        self.skip()
        self.reject()
        original_hash = self.store.metadata["Ana01"]["original_pixel_sha256"]
        original_bytes = (self.store.adapter.source / "image" / "Ana01.png").read_bytes()
        with mock.patch.object(self.store.generator, "render", return_value=(original_bytes, original_hash)):
            result = self.reject()
        self.assertEqual(result["global"]["accepted"], 0)
        self.assertIsNone(result["candidate"])
        self.assertTrue(result["error"])
        records = self.store.progress["questions"]["Ana01"]["history"]
        self.assertTrue(any(r["decision"] == "discarded_duplicate" for r in records))

    def test_io_generation_error_keeps_the_operation_skippable(self):
        self.skip()
        self.reject()
        with mock.patch.object(self.store.generator, "render", side_effect=OSError("injected PNG write failure")):
            result = self.reject()
        self.assertEqual(result["current_operation"], "A3")
        self.assertIsNone(result["candidate"])
        self.assertTrue(result["error"])
        self.assertEqual(self.store.skip(operation="A3")["candidate"]["operation"], "A4")

    def test_save_failure_recovers_on_restart(self):
        candidate = self.current()
        actual_write = review_store.atomic_write

        def fail_function(path, data):
            if Path(path).name == "draw_variants.py":
                raise OSError("injected disk failure")
            return actual_write(path, data)

        with mock.patch("review_store.atomic_write", side_effect=fail_function):
            with self.assertRaises(OSError):
                self.accept()
        self.assertEqual(self.store.snapshot()["counts"]["A"], 0)
        self.assertTrue(self.store.snapshot()["recovery_required"])
        self.assertIsNone(self.store.snapshot()["candidate"])
        self.store.close()
        self.store = Workbench(self.root, load_config())
        self.assertEqual(self.store.snapshot()["counts"]["A"], 1)
        self.assertFalse((self.root / candidate["image_path"]).exists())
        self.assertEqual(self.store.review(candidate["candidate_id"], "pass")["counts"]["A"], 1)
        self.assertTrue((self.root / "accepted" / "Ana01" / "draw_variants.py").exists())
        self.assertEqual(len((self.root / "accepted_index.jsonl").read_text(encoding="utf-8").splitlines()), 1)

    def test_failed_deletion_preserves_review_until_recovery(self):
        candidate = self.current()
        with mock.patch.object(self.store, "_delete_candidate", side_effect=PermissionError("injected locked PNG")):
            with self.assertRaises(PermissionError):
                self.reject()
        self.assertTrue((self.root / candidate["image_path"]).is_file())
        self.assertTrue(self.store.snapshot()["recovery_required"])
        result = self.store.retry()
        self.assertFalse((self.root / candidate["image_path"]).exists())
        self.assertNotEqual(result["candidate"]["candidate_id"], candidate["candidate_id"])
        self.assertEqual(result["counts"]["A"], 0)

    def test_writer_lock_and_path_boundaries(self):
        with self.assertRaises(WorkbenchError):
            Workbench(self.root, load_config())
        with self.assertRaises(WorkbenchError):
            contained_path(self.root / "candidates", "../accepted/Ana01/images/A01.png")
        with self.assertRaises(WorkbenchError):
            self.store._delete_candidate({"image_path": "candidates/../../first_process/image/Ana01.png"})
        self.assertTrue((self.store.adapter.source / "image" / "Ana01.png").exists())

    def test_full_collection_800_functions_and_pixel_reproduction(self):
        initial_manifest = self.store.adapter.manifest["files"]
        for question_index in range(80):
            expected = f"Ana{question_index + 1:02d}"
            self.assertEqual(self.store.snapshot()["current_question"], expected)
            for _ in range(10):
                candidate = self.current()
                self.assertIsNotNone(candidate, self.store.snapshot()["error"])
                self.accept()
            recipes = read_json(self.root / "accepted" / expected / "recipes.json")
            self.assertEqual([r["slot_id"] for r in recipes], [f"{group}{i:02d}" for group in "AB" for i in range(1, 6)])
            self.assertEqual([r["phase"] for r in recipes[:4]], ["coverage"] * 4)
            self.assertEqual(recipes[4]["phase"], "fill")
            self.assertEqual(len({r["pixel_sha256"] for r in recipes}), 10)
            self.assertTrue(all(r["category"] == r["operation"][0] for r in recipes))
            function_path = self.root / "accepted" / expected / "draw_variants.py"
            tree = ast.parse(function_path.read_text(encoding="utf-8"))
            names = [n.name for n in tree.body if isinstance(n, ast.FunctionDef) and n.name.startswith("draw_")]
            self.assertEqual(len(names), 10)
            spec = importlib.util.spec_from_file_location(f"test_redraw_{expected}", function_path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            # Execute the real 10 delivered function entries, with outputs in
            # this same temporary store, to prove that they are not stubs.
            for recipe in recipes:
                destination = self.root / "reproduced" / expected / f"{recipe['slot_id']}.png"
                getattr(module, "draw_" + recipe["slot_id"])(destination)
                self.assertEqual(pixel_hash(destination), recipe["pixel_sha256"])
            if (question_index + 1) % 10 == 0:
                print(f"\nIsolated collection: {question_index + 1}/80 questions, {(question_index + 1) * 10}/800 functions reproduced", flush=True)
        state = self.store.snapshot()
        self.assertEqual(state["global"]["accepted"], 800)
        self.assertEqual(state["global"]["completed_questions"], 80)
        self.assertEqual(state["global"]["pending_slots"], 0)
        self.assertEqual(state["global"]["shortages"], [])
        self.assertEqual(len(list((self.root / "accepted").glob("*/images/*.png"))), 800)
        self.assertEqual(len((self.root / "accepted_index.jsonl").read_text(encoding="utf-8").splitlines()), 800)
        self.assertEqual(manifest_for(self.store.adapter.source)["files"], initial_manifest)


class RendererTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.config, cls.adapter, cached = runtime()
        cls.metadata = cached["prechecks"]
        cls.generator = VariantGenerator(cls.config, cls.adapter, cls.metadata)

    def capture_render(self, qid, operation, params, check):
        def capture(scene, background="#FFFFFF"):
            check(scene, background)
            return scene_png(scene, background)
        with mock.patch("generate_variants.scene_png", side_effect=capture):
            return self.generator.render(qid, operation, params)

    def test_integer_geometry_and_explicit_point_provenance(self):
        meta = self.metadata["Ana01"]
        self.assertEqual(meta["original_point_count"], 0)
        self.assertEqual(meta["operations"]["B3"]["status"], "unavailable")
        self.assertEqual([p["xy"] for p in meta["integer_points"]], [[0, 0]])
        circle = self.metadata["Ana09"]["integer_points"]
        self.assertEqual(len(circle), 12)
        self.assertTrue(all(x * x + y * y == 25 for x, y in [p["xy"] for p in circle]))
        self.assertIn("不支持", self.metadata["Ana48"]["operations"]["B5"]["reason"])
        for meta in self.metadata.values():
            ids = {p["id"] for p in meta["original_points"]}
            self.assertTrue(all(source["source"]["id"] in ids for source in meta["b3_sources"]))
            for option in meta["b4_sources"]:
                start, end = option["endpoints"]
                self.assertNotEqual(start, end)
                self.assertTrue(start[0] != 0 and start[1] != 0)
                if option["source"]["kind"] == "verified_curve_integer":
                    self.assertTrue(all(float(v).is_integer() for v in start))
            for point in meta["integer_points"]:
                self.assertTrue(all(float(v).is_integer() for v in point["xy"]))

    def test_grid_changes_do_not_change_ticks(self):
        for params in self.generator.finite_params("Ana04", "A1"):
            def check(scene, background):
                for axis in (scene.ax.xaxis, scene.ax.yaxis):
                    for tick, loc in zip(axis.get_major_ticks(), axis.get_majorticklocs()):
                        self.assertEqual(tick.gridline.get_visible(), loc in params["grid_positions"])
                        self.assertTrue(tick.tick1line.get_visible())
                        self.assertTrue(tick.label1.get_visible())
                    self.assertEqual(list(axis.get_majorticklocs()), list(range(-8, 9)))
            self.capture_render("Ana04", "A1", params, check)

    def test_hide_only_tick_numbers_and_independent_origin(self):
        def check(scene, background):
            self.assertFalse(scene.ax._mp_origin_zero.get_visible())
            self.assertEqual(scene.ax.get_xticklabels(), [])
            self.assertEqual(scene.ax.get_yticklabels(), [])
            names = [text.get_text() for text in scene.texts if text.get_visible()]
            self.assertIn("y1", names)
            self.assertIn("y2", names)
            self.assertIn("x", names)
            self.assertIn("y", names)
            self.assertTrue(all(t.gridline.get_visible() and t.tick1line.get_visible() for t in scene.ax.xaxis.get_major_ticks()))
        params = next(self.generator.finite_params("Ana04", "A2"))
        self.capture_render("Ana04", "A2", params, check)

    def test_background_and_number_masks_remain_tinted(self):
        for params in self.generator.finite_params("Ana46", "A4"):
            expected = np.array(ImageColor.getrgb(params["background_color"])) / 255
            def check(scene, background):
                self.assertEqual(background, params["background_color"])
                np.testing.assert_allclose(scene.fig.get_facecolor()[:3], expected)
                np.testing.assert_allclose(scene.ax.get_facecolor()[:3], expected)
                for label in [*scene.ax.get_xticklabels(), *scene.ax.get_yticklabels(), scene.ax._mp_origin_zero]:
                    np.testing.assert_allclose(label.get_bbox_patch().get_facecolor()[:3], expected)
                for collection in scene.ax.collections:
                    if collection.get_alpha() == .45:
                        np.testing.assert_allclose(collection.get_facecolors()[0][:3], np.array([208, 208, 208]) / 255)
            png, _ = self.capture_render("Ana46", "A4", params, check)
            with Image.open(io.BytesIO(png)) as image:
                self.assertEqual(image.convert("RGBA").getpixel((0, 0)), (*ImageColor.getrgb(params["background_color"]), 255))

    def test_all_three_shapes_and_no_rng_during_redraw(self):
        found = {}
        for seed in range(50):
            params = self.generator.sample("Ana01", "A3", random.Random(seed), set())
            found[params["shape"]] = params
        self.assertEqual(set(found), {"ellipse", "rectangle", "triangle"})
        for params in found.values():
            first = self.generator.render("Ana01", "A3", params)
            with mock.patch("random.Random", side_effect=AssertionError("random redraw")), mock.patch("random.choice", side_effect=AssertionError("random redraw")):
                second = self.generator.render("Ana01", "A3", params)
            self.assertEqual(first[1], second[1])
        # A nearby coordinate must not be accepted as a verified integer point.
        params = next(self.generator.finite_params("Ana09", "B5"))
        params["points"][0]["xy"][0] += .000001
        with self.assertRaises(WorkbenchError):
            self.generator.render("Ana09", "B5", params)

    def test_original_finalize_binding_and_input_files_restored_after_failure(self):
        module = self.adapter.modules["Ana01"]
        original_finalize = module.finalize
        with mock.patch.object(self.adapter.renderer, "lock_view", side_effect=RuntimeError("injected lock failure")):
            with self.assertRaises(RuntimeError):
                self.adapter.scene("Ana01")
        self.assertIs(module.finalize, original_finalize)
        self.assertEqual(manifest_for(self.adapter.source)["files"], self.adapter.manifest["files"])


class HttpBehavior(unittest.TestCase):
    def test_api_stale_ids_and_media_deletion(self):
        with tempfile.TemporaryDirectory(prefix="mathpalette-test-http-") as name:
            root = Path(name).resolve()
            self.assertTrue(root.is_relative_to(Path(tempfile.gettempdir()).resolve()))
            config, _, cached = runtime()
            atomic_json(root / "state" / "availability.json", cached)
            store = Workbench(root, config)
            store.ensure_candidate()
            server = ThreadingHTTPServer(("127.0.0.1", 0), make_handler(store))
            thread = threading.Thread(target=server.serve_forever, daemon=True)
            thread.start()
            base = f"http://127.0.0.1:{server.server_port}"
            try:
                with urlopen(base + "/api/state") as response:
                    state = json.load(response)
                cid, url = state["candidate"]["candidate_id"], state["candidate"]["image_url"]
                request = Request(base + "/api/review", json.dumps({"candidate_id": cid, "decision": "reject"}).encode(),
                                  {"Content-Type": "application/json", "X-Workbench-Token": state["api_token"]})
                with urlopen(request) as response:
                    after = json.load(response)
                self.assertNotEqual(after["candidate"]["candidate_id"], cid)
                with self.assertRaises(HTTPError) as error:
                    urlopen(base + url)
                self.assertEqual(error.exception.code, 404)
                wrong = Request(base + "/api/review", json.dumps({"candidate_id": "stale-id", "decision": "pass"}).encode(),
                                {"Content-Type": "application/json", "X-Workbench-Token": state["api_token"]})
                with self.assertRaises(HTTPError) as error:
                    urlopen(wrong)
                self.assertEqual(error.exception.code, 409)
                missing_token = Request(base + "/api/retry", b"{}", {"Content-Type": "application/json"})
                with self.assertRaises(HTTPError) as error:
                    urlopen(missing_token)
                self.assertEqual(error.exception.code, 403)
            finally:
                server.shutdown()
                server.server_close()
                thread.join(timeout=5)
                store.close()


if __name__ == "__main__":
    unittest.main(verbosity=2)
