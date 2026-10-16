"""Meaningful solid-workbench regression; temporary approvals are test fixtures only."""
from __future__ import annotations

import copy
import json
from pathlib import Path
import shutil
import tempfile
import unittest
from unittest.mock import patch

import numpy as np
from matplotlib.colors import to_hex

from drawing_board import describe_scene
from render_plugins import PluginRenderer
from renderer_adapter import RendererAdapter, scene_png
from replay_archived import render_special_recipe
from review_store import Workbench
from workbench_io import (WorkbenchError, atomic_json, file_hash, load_config, read_json)

PROJECT = Path(__file__).resolve().parents[2]
FIXTURES = PROJECT / ".runtime/solid_workbench_tests"
TEST_NOTE = "TEMPORARY AUTOMATED TEST FIXTURE; NOT USER APPROVAL"
COLORS = ["#DC2626", "#2563EB", "#16A34A", "#EA580C"]


def plugin(qid, actions):
    return {"plugin_schema_version": "1.0.0", "question_id": qid, "category": "C", "operation": "C_manual",
            "description": TEST_NOTE, "intent": "isolated software regression only", "params": {"actions": actions}}


class GeometryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.config = load_config()
        cls.adapter = RendererAdapter(cls.config)
        cls.metadata = {qid: cls.adapter.inspect_question(qid) for qid in cls.adapter.records}
        cls.renderer = PluginRenderer(cls.config, cls.adapter, cls.metadata)

    def test_added_solid_and_dashed_lines(self):
        qid = "Solid01"
        points = self.metadata[qid]["snap_points"]
        action = {"type": "add_line", "id": "fixture_line",
                  "endpoints": [points[0]["xy"], points[1]["xy"]]}
        implicit, _, default_digest = self.renderer.render(plugin(qid, [action]))
        digests = {}
        for style in ("solid", "dashed"):
            action["linestyle"] = style
            scene = self.adapter.scene(qid)
            with patch.object(self.adapter, "scene", return_value=scene):
                normalized, _, digests[style] = self.renderer.render(plugin(qid, [action]))
            line = scene.ax.lines[-1]
            self.assertEqual(line.is_dashed(), style == "dashed")
            self.assertEqual(line.get_linewidth(), 1)
            self.assertEqual("dash_pattern_pt" in normalized["params"]["actions"][0], style == "dashed")
            self.assertEqual(self.renderer.render(normalized, frozen=True)[2], digests[style])
        self.assertEqual(default_digest, digests["dashed"])
        self.assertEqual(implicit, self.renderer.normalize(plugin(qid, [action])))
        self.assertNotEqual(digests["solid"], digests["dashed"])
        action.update(linestyle="solid", dash_pattern_pt=[3.7, 1.6])
        with self.assertRaises(WorkbenchError):
            self.renderer.normalize(plugin(qid, [action]))
        self.assertEqual(self.adapter.inspect_question(qid)["original_pixel_sha256"],
                         self.metadata[qid]["original_pixel_sha256"])

    def test_every_baseline_path_and_projection(self):
        # The approved catalog grows; every canonical formal row must be checked.
        expected_ids = {json.loads(line)["id"] for line in
                        Path(self.config["dataset_file"]).read_text(encoding="utf-8-sig").splitlines()
                        if line.strip()}
        self.assertEqual(set(self.metadata), expected_ids)
        self.assertTrue(expected_ids)
        before = self.adapter.make_manifest()
        for qid, meta in self.metadata.items():
            with self.subTest(qid=qid):
                board = describe_scene(self.adapter, qid)
                self.assertEqual((board["width"], board["height"]), (768, 768))
                self.assertEqual(len(board["targets"]), sum(o["styleable"] for o in meta["objects"]))
                scene = self.adapter.scene(qid)
                try:
                    for target in board["targets"]:
                        self.assertEqual(len(target["fragment_linestyles"]), len(scene.artists[target["id"]]))
                        self.assertGreaterEqual(len(target["paths"]), len(scene.artists[target["id"]]))
                        for path in target["paths"]:
                            self.assertGreaterEqual(len(path), 2)
                            self.assertTrue(np.isfinite(path).all())
                    for point in board["snap_points"]:
                        self.assertEqual(point["xy"], self.adapter.renderer.project(
                            self.adapter.scenes[qid], point["world_xyz"]).tolist())
                        self.assertTrue(np.allclose((np.array(board["pixel_to_data"]) @ [*point["pixel"], 1])[:2], point["xy"]))
                finally:
                    scene.close()
        self.assertEqual(before, self.adapter.make_manifest())

    def test_all_styleable_objects_and_multifragment_visibility(self):
        multifragment, mixed = 0, 0
        for qid in self.metadata:
            scene = self.adapter.scene(qid)
            frozen = copy.deepcopy(self.adapter.scenes[qid])
            try:
                for obj in scene.objects:
                    if not obj["styleable"]:
                        continue
                    artists = scene.artists[obj["id"]]
                    paths = [a.get_xydata().copy() for a in artists]
                    originals = [(a.get_linestyle(), a._unscaled_dash_pattern) for a in artists]
                    multifragment += len(artists) > 1
                    mixed += len({a.is_dashed() for a in artists}) > 1
                    for color in COLORS:
                        p = self.renderer.normalize(plugin(qid, [{"type": "set_object_style", "target": obj["id"], "color": color}]))
                        self.renderer.apply_actions(scene, p)
                        self.assertEqual([to_hex(a.get_color()).upper() for a in artists], [color] * len(artists))
                        self.assertEqual(originals, [(a.get_linestyle(), a._unscaled_dash_pattern) for a in artists])
                    p = self.renderer.normalize(plugin(qid, [{"type": "set_object_style", "target": obj["id"], "linestyle": "solid"}]))
                    self.renderer.apply_actions(scene, p)
                    self.assertTrue(all(not a.is_dashed() for a in artists))
                    self.assertTrue(self.renderer.appearance_changes(p)["rendered_line_styles_changed"])
                    for a, expected in zip(artists, paths):
                        self.assertTrue(np.array_equal(a.get_xydata(), expected))
                self.assertEqual(frozen, self.adapter.scenes[qid])
            finally:
                scene.close()
        self.assertGreater(multifragment, 0)
        self.assertGreater(mixed, 0)

    def test_snap_does_not_expose_construction_anchors(self):
        names = {p["id"] for p in self.metadata["Solid01"]["snap_points"]}
        self.assertEqual(names, set("ABCDEFGH"))
        for qid in ("Solid12", "Solid13"):
            points = {p["id"] for p in self.metadata[qid]["snap_points"]}
            markers = {ref for obj in self.adapter.scenes[qid]["objects"]
                       if obj["id"].startswith(("equal_tick_", "right_angle_"))
                       for ref in obj["points"] if isinstance(ref, str)}
            actual = {ref for obj in self.adapter.scenes[qid]["objects"]
                      if not obj["id"].startswith(("equal_tick_", "right_angle_"))
                      for ref in obj.get("points", []) if isinstance(ref, str)}
            self.assertFalse(points & (markers - actual))
        self.assertIn("O", {p["id"] for p in self.metadata["Solid12"]["snap_points"]})

    def test_schema_and_semantics_are_strict(self):
        p = {"type": "add_point", "id": "test_point", "xy": [0, 0]}
        invalid = [{**p, "color": "#000000"}, {**p, "color": "#FF0000"}, {**p, "size_pt2": 51},
                   {**p, "filled": False}, {**p, "edge_linewidth_pt": 2}, {**p, "xy": [True, 1]},
                   {**p, "xy": [float("inf"), 1]}, {**p, "xy": [float("nan"), 1]},
                   {**p, "xy": [100000, 1]}, {**p, "text": "disallowed"},
                   {"type": "add_text", "id": "text", "xy": [0, 0], "text": "no"},
                   {"type": "set_object_style", "target": "unknown", "color": COLORS[0]},
                   {"type": "set_object_style", "target": "AB"},
                   {"type": "set_object_style", "target": "AB", "linewidth_pt": 4},
                   {"type": "set_object_style", "target": "AB", "linestyle": "dotted"}]
        line = {"type": "add_line", "id": "test_line", "endpoints": [[0, 0], [1, 1]]}
        invalid += [{**line, "linestyle": "dotted"}, {**line, "linewidth_pt": 2},
                    {**line, "dash_pattern_pt": [4, 3]}, {**line, "color": "#000000"},
                    {**line, "endpoints": [[0, 0], [0, 0]]}]
        for action in invalid:
            with self.subTest(action=action), self.assertRaises(WorkbenchError):
                self.renderer.normalize(plugin("Solid01", [action]))
        for wrong in ("Ana01", "Plane01", "Solid00", "Solid999"):
            with self.assertRaises(WorkbenchError):
                self.renderer.normalize(plugin(wrong, [p]))
        for color in COLORS:
            normalized, data, digest = self.renderer.render(plugin("Solid01", [{**p, "color": color}, {**line, "color": color}]))
            self.assertNotEqual(digest, self.metadata["Solid01"]["original_pixel_sha256"])
            self.assertTrue(data.startswith(b"\x89PNG"))
            self.assertEqual(normalized["params"]["actions"][1]["dash_pattern_pt"], [3.7, 1.6])

    def test_restore_original_style_reproduces_baseline(self):
        first = self.adapter.scene("Solid14")
        try:
            before = scene_png(first)[1]
            target = next(o["id"] for o in first.objects if o["styleable"])
            self.renderer.apply_actions(first, plugin("Solid14", [{"type": "set_object_style", "target": target, "color": COLORS[2]}]))
            self.assertNotEqual(scene_png(first)[1], before)
        finally:
            first.close()
        restored = self.adapter.scene("Solid14")
        try:
            self.assertEqual(scene_png(restored)[1], before)
        finally:
            restored.close()


class WorkflowTests(unittest.TestCase):
    def test_isolated_review_replay_recovery_and_cold_restore(self):
        FIXTURES.mkdir(parents=True, exist_ok=True)
        before_formal = file_hash(PROJECT / "question_bank.jsonl")
        with tempfile.TemporaryDirectory(prefix="workflow-fixture-", dir=FIXTURES) as directory:
            root = Path(directory)
            config = load_config()
            config.update(runtime_dir=str(root / "runtime"), output_dir=str(root / "dataset/special_variant"),
                          dataset_root=str(root / "dataset"), config_path=str(root / "config.json"))
            atomic_json(root / "config.json", config)
            bench = Workbench(config)
            try:
                self.assertFalse(Path(config["output_dir"]).exists(), "startup must not create formal output")
                qid = "Solid01"
                p = plugin(qid, [{"type": "set_object_style", "target": "AB", "color": COLORS[0]}])
                token = bench.context_token()
                preview = bench.drawing_preview(p, token)
                self.assertFalse(Path(config["output_dir"]).exists())
                candidate = bench.drawing_submit(p, token, None, preview["pixel_sha256"], preview["parameter_key"])["candidate"]
                with self.assertRaises(WorkbenchError):
                    bench.drawing_preview(p, token)
                points = bench.context()["snap_points"]
                p2 = plugin(qid, [{"type": "set_object_style", "target": "AB", "color": COLORS[2], "linestyle": "dashed"},
                                  {"type": "add_line", "id": "fixture_solid", "linestyle": "solid",
                                   "endpoints": [points[0]["xy"], points[1]["xy"]]}])
                preview2 = bench.drawing_preview(p2, bench.context_token(), candidate["candidate_id"])
                replacement = bench.drawing_submit(p2, bench.context_token(), candidate["candidate_id"],
                    preview2["pixel_sha256"], preview2["parameter_key"])["candidate"]
                self.assertEqual(bench.status(candidate["candidate_id"])["status"], "superseded")
                with self.assertRaises(WorkbenchError):
                    bench.review(qid, candidate["candidate_id"], "pass", bench.context_token(), candidate["pixel_sha256"], candidate["parameter_key"], TEST_NOTE)
                bench.review(qid, replacement["candidate_id"], "pass", bench.context_token(), replacement["pixel_sha256"], replacement["parameter_key"], TEST_NOTE)
                recipe = copy.deepcopy(bench.progress["questions"][qid]["accepted"][0])
                self.assertTrue(recipe["appearance_changes"]["rendered_line_styles_changed"])
                self.assertFalse(recipe["appearance_changes"]["frozen_visibility_intervals_changed"])
                result = render_special_recipe(recipe, root / "replay.png", root / "config.json")
                self.assertTrue(result["matches_accepted"])
                bench.collect(qid, bench.context_token())
                self.assertNotIn(qid, bench.active_questions())
                bench.reopen(qid, bench.context_token())
                with patch.object(bench, "_apply_transaction", side_effect=OSError("TEST interruption")):
                    with self.assertRaises(OSError):
                        bench.delete_accepted(qid, recipe["candidate_id"], recipe["slot_id"], bench.context_token(), recipe["pixel_sha256"], recipe["parameter_key"])
                self.assertTrue((bench.state_dir / "pending_transaction.json").exists())
            finally:
                bench.close()
            recovered = Workbench(config)
            try:
                self.assertEqual(recovered.progress["questions"][qid]["accepted"], [])
                self.assertFalse((recovered.state_dir / "pending_transaction.json").exists())
                # Create a second explicitly temporary review fixture to verify
                # recovery from durable passed/collected records after cache loss.
                preview = recovered.drawing_preview(p, recovered.context_token())
                candidate = recovered.drawing_submit(p, recovered.context_token(), None,
                    preview["pixel_sha256"], preview["parameter_key"])["candidate"]
                recovered.review(qid, candidate["candidate_id"], "pass", recovered.context_token(), candidate["pixel_sha256"], candidate["parameter_key"], TEST_NOTE)
                recovered.collect(qid, recovered.context_token())
            finally:
                recovered.close()
            runtime = Path(config["runtime_dir"]).resolve()
            self.assertTrue(runtime.is_relative_to(FIXTURES.resolve()))
            shutil.rmtree(runtime)
            restored = Workbench(config)
            try:
                self.assertTrue(restored.progress["questions"][qid]["collected"])
                self.assertEqual(len(restored.progress["questions"][qid]["accepted"]), 1)
                self.assertEqual(restored.snapshot()["accepted_total"], 1)
            finally:
                restored.close()
        self.assertEqual(before_formal, file_hash(PROJECT / "question_bank.jsonl"))


if __name__ == "__main__":
    unittest.main()
