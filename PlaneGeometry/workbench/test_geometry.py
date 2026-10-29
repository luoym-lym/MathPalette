"""Geometry invariants and isolated review fixtures; never touch real C outputs."""
from __future__ import annotations

import copy
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

import numpy as np
from matplotlib.colors import to_hex
from matplotlib.path import Path as MplPath
from matplotlib.transforms import Affine2D

from drawing_board import _pixel_paths
from mathvision_adapter import RendererAdapter
from renderer_adapter import scene_png
from mathvision_plugins import PluginRenderer
from review_store import Workbench
from replay_archived import render_special_recipe
from workbench_io import (ROOT, WorkbenchError, canonical_hash, file_hash, load_config,
                          pixel_hash, read_json)

PROJECT = ROOT.parents[1]
FIXTURES = PROJECT / ".runtime/plane_workbench_tests"
COLORS = ["#DC2626", "#2563EB", "#16A34A", "#EA580C"]


def plugin(qid, *actions):
    return {"plugin_schema_version": "1.0.0", "question_id": qid, "category": "C",
            "operation": "C_manual", "description": "TEMPORARY SOFTWARE TEST FIXTURE",
            "intent": "temporary isolated regression only", "params": {"actions": list(actions)}}


class GeometryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.config = load_config()
        cls.adapter = RendererAdapter(cls.config)
        cls.metadata = {qid: cls.adapter.inspect_question(qid) for qid in cls.adapter.records}
        cls.renderer = PluginRenderer(cls.config, cls.adapter, cls.metadata)

    def test_added_solid_and_dashed_lines(self):
        qid = "Plane01"
        points = self.metadata[qid]["snap_points"]
        action = {"type": "add_line", "id": "fixture_line",
                  "endpoints": [points[0]["xy"], points[1]["xy"]]}
        implicit, _, default_digest = self.renderer.render(plugin(qid, action))
        digests = {}
        for style in ("solid", "dashed"):
            action["linestyle"] = style
            scene = self.adapter.scene(qid)
            with patch.object(self.adapter, "scene", return_value=scene):
                normalized, _, digests[style] = self.renderer.render(plugin(qid, action))
            line = scene.ax.lines[-1]
            self.assertEqual(line.is_dashed(), style == "dashed")
            self.assertEqual(line.get_linewidth(), 1)
            self.assertEqual("dash_pattern_pt" in normalized["params"]["actions"][0], style == "dashed")
            self.assertEqual(self.renderer.render(normalized, frozen=True)[2], digests[style])
        self.assertEqual(default_digest, digests["dashed"])
        self.assertEqual(implicit, self.renderer.normalize(plugin(qid, action)))
        self.assertNotEqual(digests["solid"], digests["dashed"])
        action.update(linestyle="solid", dash_pattern_pt=[3.7, 1.6])
        with self.assertRaises(WorkbenchError):
            self.renderer.normalize(plugin(qid, action))
        self.assertEqual(self.adapter.inspect_question(qid)["original_pixel_sha256"],
                         self.metadata[qid]["original_pixel_sha256"])

    def test_all_formal_baselines_and_real_paths(self):
        # The approved catalog grows; every canonical formal row must be checked.
        expected_ids = {json.loads(line)["id"] for line in
                        Path(self.config["dataset_file"]).read_text(encoding="utf-8-sig").splitlines()
                        if line.strip()}
        self.assertEqual(set(self.metadata), expected_ids)
        self.assertTrue(expected_ids)
        for qid, meta in self.metadata.items():
            self.assertEqual(meta["original_pixel_sha256"], pixel_hash(self.adapter.original_paths[qid]))
            canvas = meta["canvas"]
            self.assertEqual((canvas["width"], canvas["height"]), (768, 768))
            self.assertEqual({o["id"] for o in meta["objects"] if o["styleable"]},
                             {o["id"] for o in canvas["targets"]})
            self.assertTrue(all(t["paths"] for t in canvas["targets"]))
            self.assertTrue(np.allclose(np.array(canvas["data_to_pixel"]) @ np.array(canvas["pixel_to_data"]), np.eye(3)))
            for point in canvas["snap_points"]:
                xy = np.array(canvas["pixel_to_data"]) @ [*point["pixel"], 1]
                self.assertTrue(np.allclose(xy[:2], point["xy"], rtol=0, atol=1e-12))

    def test_every_target_colors_all_fragments_without_changing_geometry_fill_labels(self):
        count = 0
        for qid, meta in self.metadata.items():
            for target in meta["canvas"]["targets"]:
                with self.subTest(qid=qid, target=target["id"]):
                    scene = self.adapter.scene(qid)
                    artists = scene.artists[target["id"]]
                    original_styles = [a.get_linestyle() for a in artists]
                    fills = [(p, p.get_facecolor()) for p in scene.ax.patches]
                    labels = [(t.get_text(), t.get_position(), t.get_color()) for t in scene.ax.texts]
                    paths = [a.get_path().vertices.copy() for a in artists]
                    with patch.object(self.adapter, "scene", return_value=scene):
                        _, data, digest = self.renderer.render(plugin(qid, {
                            "type": "set_object_style", "target": target["id"], "color": COLORS[0]}))
                    self.assertNotEqual(digest, meta["original_pixel_sha256"])
                    self.assertEqual(digest, pixel_hash(data))
                    self.assertEqual([a.get_linestyle() for a in artists], original_styles)
                    for artist, path in zip(artists, paths):
                        color = artist.get_color() if hasattr(artist, "get_color") else artist.get_edgecolor()
                        self.assertEqual(to_hex(color).upper(), COLORS[0])
                        np.testing.assert_array_equal(artist.get_path().vertices, path)
                    for fill, original in fills:
                        self.assertEqual(fill.get_facecolor(), original)
                    self.assertEqual([(t.get_text(), t.get_position(), t.get_color()) for t in scene.ax.texts], labels)
                    count += 1
        self.assertGreater(count, 100)

    def test_explicit_styles_and_four_color_fixed_annotations(self):
        qid = "Plane01"
        points = self.metadata[qid]["snap_points"]
        for color in COLORS:
            p = plugin(qid, {"type": "add_point", "id": "fixture_point", "xy": points[0]["xy"], "color": color},
                       {"type": "add_line", "id": "fixture_line", "endpoints": [points[0]["xy"], points[1]["xy"]], "color": color})
            normalized, _, _ = self.renderer.render(p)
            point, line = normalized["params"]["actions"]
            self.assertEqual((point["size_pt2"], point["filled"], point["edge_linewidth_pt"]), (50, True, 1))
            self.assertEqual((line["linestyle"], line["linewidth_pt"], line["dash_pattern_pt"]), ("dashed", 1, [3.7, 1.6]))
            self.assertEqual(line["endpoints"], [points[0]["xy"], points[1]["xy"]])
        for style in ("solid", "dashed"):
            qid, target = "Plane02", "AQ_dimension"
            scene = self.adapter.scene(qid)
            with patch.object(self.adapter, "scene", return_value=scene):
                self.renderer.render(plugin(qid, {"type": "set_object_style", "target": target,
                                                 "color": COLORS[1], "linestyle": style}))
            for artist in scene.artists[target]:
                self.assertEqual(artist.get_linestyle(), "--" if style == "dashed" else "-")
        # Removing the override recreates exactly the original, with no mutation.
        self.assertEqual(self.adapter.inspect_question(qid)["original_pixel_sha256"], self.metadata[qid]["original_pixel_sha256"])

    def test_strict_whitelist_and_coordinates(self):
        valid = {"type": "add_point", "id": "fixture_point", "xy": self.metadata["Plane01"]["snap_points"][0]["xy"]}
        invalid = [dict(valid, color="#000000"), dict(valid, color="#FFFFFF"), dict(valid, size_pt2=51),
                   dict(valid, filled=False), dict(valid, edge_linewidth_pt=2), dict(valid, xy=[float("nan"), 0]),
                   dict(valid, xy=[float("inf"), 0]), dict(valid, xy=[True, 0]), dict(valid, xy=[1e300, 0]),
                   dict(valid, id="A"), dict(valid, text="no"), dict(valid, type="add_text"),
                   {"type": "set_object_style", "target": "unknown", "color": COLORS[0]},
                   {"type": "set_object_style", "target": "AB", "linewidth_pt": 4},
                   {"type": "set_object_style", "target": "AB"},
                   {"type": "add_line", "id": "line", "endpoints": [[0, 0], [1, 1]], "linestyle": "dotted"},
                   {"type": "add_line", "id": "line", "endpoints": [[0, 0], [1, 1]], "dash_pattern_pt": [4, 3]},
                   {"type": "add_line", "id": "line", "endpoints": [[0, 0], [0, 0]]}]
        for action in invalid:
            with self.subTest(action=repr(action)), self.assertRaises(WorkbenchError):
                self.renderer.normalize(plugin("Plane01", action))
        for qid in ("Ana01", "Solid01", "Plane00", "Plane999999"):
            with self.subTest(qid=qid), self.assertRaises(WorkbenchError):
                self.renderer.normalize(plugin(qid, valid))

    def test_snap_identity_and_no_construction_points(self):
        def ids(qid):
            return {p["id"] for p in self.metadata[qid]["snap_points"]}
        self.assertEqual(ids("Plane02"), {"A", "P", "Q", "B", "C"})
        self.assertEqual(ids("Plane08"), {"A", "B", "C", "F"})
        self.assertIn("O", ids("Plane03"))
        self.assertTrue(all("_ul_" not in name or name.endswith(("_0", "_32")) for name in ids("Plane13")))
        self.assertFalse(ids("Plane16") & {"C0", "C1", "C2", "C3", "C4", "C5", "TopC", "RightC"})
        self.assertIn("inner_touch0", ids("Plane16"))

    def test_path_breaks_are_never_joined(self):
        path = MplPath([[1, 1], [2, 2], [10, 10], [11, 11]],
                       [MplPath.MOVETO, MplPath.LINETO, MplPath.MOVETO, MplPath.LINETO])
        self.assertEqual(len(_pixel_paths(path, Affine2D(), 768, 768)), 2)
        path = MplPath([[1, 1], [2, 2], [np.nan, np.nan], [10, 10], [11, 11]])
        self.assertEqual(len(_pixel_paths(path, Affine2D(), 768, 768)), 2)


class ReviewTests(unittest.TestCase):
    def test_launcher_resolves_paths_before_changing_child_directory(self):
        from launch_workbench import absolute_path_arguments
        result = absolute_path_arguments(["--check", "--data-dir", ".runtime/state",
                                          "--output-dir=.runtime/output", "--config", "config.json"])
        self.assertEqual(result[2], str(Path(".runtime/state").resolve()))
        self.assertEqual(result[3], "--output-dir=" + str(Path(".runtime/output").resolve()))
        self.assertEqual(result[5], str(Path("config.json").resolve()))

    def test_isolated_workflow_recovery_and_offline_entry(self):
        FIXTURES.mkdir(parents=True, exist_ok=True)
        with tempfile.TemporaryDirectory(prefix="review-fixture-", dir=FIXTURES) as temporary:
            root = Path(temporary).resolve()
            self.assertTrue(root.is_relative_to(FIXTURES.resolve()))
            branch = root / "PlaneGeometry"
            copied_workbench = branch / "workbench"
            shutil.copytree(ROOT, copied_workbench, ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
            config = load_config()
            config.update(runtime_dir=str(root / "runtime"), output_dir=str(branch / "special_variant"),
                          dataset_root=str(branch), config_path=str(copied_workbench / "config.json"))
            (copied_workbench / "config.json").write_text(json.dumps(config), encoding="utf-8")
            root_index = file_hash(PROJECT / "question_bank.jsonl")
            real_output = PROJECT / "PlaneGeometry/special_variant"
            real_files = {str(p): file_hash(p) for p in real_output.rglob("*") if p.is_file()}
            bench = Workbench(config)
            try:
                self.assertFalse(Path(config["output_dir"]).exists())
                first = bench.context()
                self.assertIn("scenes/Plane01.json", bench.adapter.dependencies("Plane01"))
                self.assertIn("geometry_dataset.py", bench.adapter.dependencies("Plane01"))
                self.assertEqual(first["branch"], "PlaneGeometry")
                self.assertTrue(first["snap_points"] and first["canvas"]["targets"])
                p = plugin("Plane01", {"type": "add_point", "id": "fixture_point", "xy": first["snap_points"][0]["xy"]},
                           {"type": "add_line", "id": "fixture_solid", "linestyle": "solid",
                            "endpoints": [first["snap_points"][0]["xy"], first["snap_points"][1]["xy"]]})
                preview = bench.drawing_preview(p, first["context_token"])
                self.assertFalse(bench.progress["candidates"])
                with self.assertRaises(WorkbenchError):
                    bench.drawing_submit(p, first["context_token"], None, "wrong", preview["parameter_key"])
                candidate = bench.drawing_submit(p, first["context_token"], None,
                    preview["pixel_sha256"], preview["parameter_key"])["candidate"]
                with self.assertRaises(WorkbenchError):
                    bench.drawing_preview(p, first["context_token"])
                token = bench.context_token()
                with self.assertRaises(WorkbenchError):
                    bench.drawing_preview(p, token)
                p["params"]["actions"][0]["color"] = COLORS[2]
                preview = bench.drawing_preview(p, token, candidate["candidate_id"])
                replacement = bench.drawing_submit(p, token, candidate["candidate_id"],
                    preview["pixel_sha256"], preview["parameter_key"])["candidate"]
                self.assertEqual(bench.status(candidate["candidate_id"])["status"], "superseded")
                with self.assertRaises(WorkbenchError):
                    bench.review("Plane01", candidate["candidate_id"], "pass", bench.context_token(),
                                 candidate["pixel_sha256"], candidate["parameter_key"], "TEMPORARY TEST FIXTURE")
                bench.review("Plane01", replacement["candidate_id"], "reject", bench.context_token(),
                             replacement["pixel_sha256"], replacement["parameter_key"], "TEMPORARY TEST FIXTURE")
                preview = bench.drawing_preview(p, bench.context_token())
                accepted = bench.drawing_submit(p, bench.context_token(), None,
                    preview["pixel_sha256"], preview["parameter_key"])["candidate"]
                # Simulate a crash after writing the transaction but before files.
                with patch.object(bench, "_apply_transaction", side_effect=OSError("fixture interrupted save")):
                    with self.assertRaises(OSError):
                        bench.review("Plane01", accepted["candidate_id"], "pass", bench.context_token(),
                            accepted["pixel_sha256"], accepted["parameter_key"], "TEMPORARY TEST FIXTURE")
                bench.close()
                bench = Workbench(config)
                recipe = bench.snapshot()["accepted"][0]
                self.assertEqual(recipe["slot_id"], "C01")
                result = render_special_recipe(recipe, config_path=config["config_path"])
                self.assertTrue(result["matches_accepted"])
                script = branch / "special_variant/Plane01/draw_variants.py"
                completed = subprocess.run([sys.executable, "-X", "utf8", "-B", str(script), "C01"],
                                           capture_output=True, text=True, encoding="utf-8", timeout=30)
                self.assertEqual(completed.returncode, 0, completed.stderr)
                self.assertTrue(json.loads(completed.stdout)["matches_accepted"])
                self.assertTrue((branch / "special_variant/_baselines" / (recipe["baseline_fingerprint"] + ".json")).is_file())
                bench.collect("Plane01", bench.context_token())
                self.assertEqual(bench.snapshot()["collected_total"], 1)
                bench.close()
                # Clean runtime state, then restore solely from durable fixtures.
                config["runtime_dir"] = str(root / "cold_runtime")
                bench = Workbench(config)
                self.assertEqual(bench.snapshot()["collected_total"], 1)
                bench.reopen("Plane01", bench.context_token())
                self.assertEqual(bench.snapshot()["question_id"], "Plane01")
                recipe = bench.snapshot()["accepted"][0]
                with patch.object(bench, "_apply_transaction", side_effect=OSError("fixture interrupted delete")):
                    with self.assertRaises(OSError):
                        bench.delete_accepted("Plane01", recipe["candidate_id"], recipe["slot_id"], bench.context_token(),
                                              recipe["pixel_sha256"], recipe["parameter_key"])
                bench.close()
                bench = Workbench(config)
                self.assertEqual(bench.snapshot()["accepted_total"], 0)
                self.assertFalse((branch / "special_variant/Plane01/images/C01.png").exists())
            finally:
                bench.close()
            self.assertEqual(file_hash(PROJECT / "question_bank.jsonl"), root_index)
            self.assertEqual({str(p): file_hash(p) for p in real_output.rglob("*") if p.is_file()}, real_files)


if __name__ == "__main__":
    unittest.main()
