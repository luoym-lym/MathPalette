"""Read-only native/legacy regression; every output is an isolated QA artifact."""
from __future__ import annotations

import copy
from pathlib import Path
import tempfile
from types import SimpleNamespace
import unittest
from unittest.mock import patch

import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from matplotlib.path import Path as VectorPath
from matplotlib.patches import PathPatch

from drawing_board import PRESETS, describe_scene
from mathvision_adapter import RendererAdapter, scene_png
from mathvision_plugins import PluginRenderer
from partial_style import object_paths
from renderer_adapter import RendererAdapter as LegacyAdapter
from replay_archived import render_special_recipe
from workbench_io import (GENERATOR_VERSION, ROOT, SCHEMA_VERSION, WorkbenchError,
                          atomic_json, canonical_hash, environment_versions,
                          file_hash, load_config, read_json, renderer_fingerprint)

PROJECT = Path(__file__).resolve().parents[2]
QA_ROOT = PROJECT / ".runtime/mathvision_workbench_sync_20261029/solid_qa"


def plugin(qid, actions):
    return {"plugin_schema_version": "1.0.0", "question_id": qid, "category": "C",
            "operation": "C_manual", "description": "ISOLATED QA FIXTURE; NOT USER APPROVAL",
            "intent": "software verification", "params": {"actions": actions}}


class MathVisionIntegrationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.config = load_config()
        cls.adapter = RendererAdapter(cls.config)
        cls.metadata = {}
        cls.native_ids = [qid for qid in cls.adapter.records if cls.adapter.is_mathvision(qid)]
        QA_ROOT.mkdir(parents=True, exist_ok=True)

    def metadata_for(self, qid):
        if qid not in self.metadata:
            self.metadata[qid] = self.adapter.inspect_question(qid)
        return self.metadata[qid]

    def test_all_native_baselines_and_target_paths(self):
        self.assertEqual(len(self.native_ids), 170)
        for qid in self.native_ids:
            with self.subTest(qid=qid):
                metadata = self.metadata_for(qid)
                board = describe_scene(self.adapter, qid)
                self.assertEqual((board["width"], board["height"]), (768, 768))
                self.assertEqual(board["presets"], PRESETS)
                self.assertTrue(board["targets"], "Native solid outlines must remain editable")
                styleable = {obj["id"] for obj in metadata["objects"] if obj["styleable"]}
                self.assertEqual({target["id"] for target in board["targets"]}, styleable)
                for target in board["targets"]:
                    self.assertTrue(target["paths"])
                    self.assertTrue(target["partial_paths"])
                for obj in metadata["objects"]:
                    if obj["kind"] in ("face", "text", "arrow"):
                        self.assertFalse(obj["styleable"])
                dependencies = self.adapter.question_dependencies(qid)
                for name in self.adapter.records[qid]["runtime_dependencies"]:
                    self.assertIn(name, dependencies)
                    self.assertIn(name, self.adapter.manifest["files"])
                for name in ("../dataset_tools/mathvision_workbench.py", "workbench/mathvision_adapter.py",
                             "workbench/mathvision_plugins.py", "workbench/replay_archived.py"):
                    self.assertIn(name, dependencies)

    def test_native_actions_preserve_faces_labels_and_frozen_inputs(self):
        # Include both straight and curved native outlines, selected from the
        # frozen catalog rather than assumptions about artist ordering.
        chosen = ["Solid79", "Solid80", "Solid133"]
        for qid in self.native_ids:
            if any(item["type"] == "circular_arc" for item in self.adapter.scenes[qid]["objects"]):
                chosen.append(qid)
                break
        for qid in chosen:
            with self.subTest(qid=qid):
                metadata = self.metadata_for(qid)
                if qid == "Solid133":
                    self.assertEqual(sum(obj["styleable"] for obj in metadata["objects"]), 18)
                    self.assertEqual(len(metadata["snap_points"]), 14)
                    self.assertTrue(all(len(point["world_xyz"]) == 3 for point in metadata["snap_points"]))
                renderer = PluginRenderer(self.config, self.adapter, {qid: metadata})
                scene = self.adapter.scene(qid)
                frozen = copy.deepcopy(self.adapter.scenes[qid])
                try:
                    scene.fig.canvas.draw()
                    target = next(obj for obj in scene.objects if obj["styleable"])
                    oid = target["id"]
                    faces = [(a, a.get_facecolor()) for a in scene.ax.patches]
                    labels = [(a, a.get_text(), a.get_position(), a.get_color()) for a in scene.ax.texts]
                    paths = object_paths(scene, oid)
                    self.assertTrue(paths)
                    interval = {"path_id": paths[0]["id"], "path_sha256": paths[0]["sha256"],
                                "start": .2, "end": .8, "wrap": False}
                    actions = [{"type": "set_object_style", "target": oid, "color": "#DC2626"}]
                    normalized = renderer.normalize(plugin(qid, actions))
                    renderer.apply_actions(scene, normalized)
                    current_paths = object_paths(scene, oid)
                    self.assertEqual([[segment["style"]["dash"] for segment in path["segments"]] for path in current_paths],
                                     [[segment["style"]["dash"] for segment in path["segments"]] for path in paths])
                    self.assertEqual([[segment["control"].tolist() for segment in path["segments"]] for path in current_paths],
                                     [[segment["control"].tolist() for segment in path["segments"]] for path in paths])
                    for artist, expected in faces:
                        self.assertEqual(artist.get_facecolor(), expected)
                    self.assertEqual(labels, [(a, a.get_text(), a.get_position(), a.get_color()) for a in scene.ax.texts])
                    local = renderer.normalize(plugin(qid, [{"type": "set_object_style", "target": oid,
                                                            "color": "#2563EB", "linewidth_pt": 1.5,
                                                            "interval": interval}]))
                    renderer.apply_actions(scene, local)
                    self.assertNotEqual(scene_png(scene)[1], metadata["original_pixel_sha256"])
                    self.assertEqual(self.adapter.scenes[qid], frozen)
                finally:
                    scene.close()
                x0, x1 = map(float, metadata["xlim"])
                y0, y1 = map(float, metadata["ylim"])
                actions = [{"type": "add_point", "id": "qa_point", "xy": [(x0 + x1) / 2, (y0 + y1) / 2]},
                           {"type": "add_line", "id": "qa_line", "endpoints": [[x0, y0], [x1, y1]], "linestyle": "solid"}]
                normalized, _, digest = renderer.render(plugin(qid, actions))
                self.assertEqual(renderer.render(normalized, frozen=True)[2], digest)
                self.assertNotEqual(digest, metadata["original_pixel_sha256"])
                style_digests = [renderer.render(plugin(qid, [{"type": "set_object_style", "target": oid,
                    "color": "#16A34A", "linestyle": style}]))[2] for style in ("solid", "dashed")]
                self.assertNotEqual(*style_digests)
                for obj in metadata["objects"]:
                    if not obj["styleable"]:
                        with self.assertRaises(WorkbenchError):
                            renderer.normalize(plugin(qid, [{"type": "set_object_style", "target": obj["id"], "color": "#DC2626"}]))

    def test_dependency_changes_are_rejected(self):
        dependency = self.adapter.records["Solid79"]["runtime_dependencies"][0]
        real_hash = file_hash
        target = self.adapter.input_files[dependency]
        with patch("renderer_adapter.file_hash", side_effect=lambda path: "changed" if Path(path) == target else real_hash(path)):
            with self.assertRaises(WorkbenchError) as raised:
                self.adapter.assert_baseline()
            self.assertEqual(raised.exception.code, "baseline_changed")

    def test_native_patch_and_collection_paths(self):
        fig, ax = plt.subplots(figsize=(7.68, 7.68), dpi=100)
        ax.set(xlim=(0, 10), ylim=(0, 10))
        patch_artist = PathPatch(VectorPath([[1, 1], [3, 6], [5, 1]], [1, 3, 3]),
                                 facecolor="#E6E6E6", edgecolor="black", linewidth=2, linestyle=(0, [4, 3]))
        ax.add_patch(patch_artist)
        collection = LineCollection([[[1, 7], [5, 7]], [[1, 8], [5, 8]]],
                                    colors="black", linewidths=[2, 3], linestyles=["solid", (0, [4, 3])])
        ax.add_collection(collection)
        label = ax.text(7, 7, "frozen label", color="black")
        objects = [{"id": name, "kind": kind, "styleable": True, "source_call": {}, "frozen_visibility": None}
                   for name, kind in (("curve", "circular_arc"), ("edges", "polyline"))]
        scene = SimpleNamespace(fig=fig, ax=ax, artists={"curve": [patch_artist], "edges": [collection]},
                                objects=objects, snap_points=[], settings={}, native=True, close=lambda: None)
        renderer = PluginRenderer(self.config, self.adapter, {})
        try:
            fig.canvas.draw()
            board = describe_scene(SimpleNamespace(scene=lambda qid: scene), "Solid79")
            self.assertEqual(board["targets"][1]["linestyle"], "mixed")
            self.assertEqual(len(board["targets"][1]["partial_paths"]), 2)
            patch_dashes = copy.deepcopy(patch_artist._dash_pattern)
            collection_dashes = [(offset, tuple(pattern) if pattern is not None else None)
                                  for offset, pattern in collection.get_linestyles()]
            self.assertEqual(patch_dashes, (0, [8, 6]))
            self.assertEqual(collection_dashes, [(0, None), (0, (12, 9))])
            renderer.apply_actions(scene, plugin("Solid79", [{"type": "set_object_style", "target": target,
                                                               "linewidth_pt": 3} for target in ("curve", "edges")]))
            self.assertEqual(patch_artist._dash_pattern, patch_dashes)
            self.assertEqual([(offset, tuple(pattern) if pattern is not None else None)
                             for offset, pattern in collection.get_linestyles()], collection_dashes)
            fill = patch_artist.get_facecolor()
            renderer.apply_actions(scene, plugin("Solid79", [{"type": "set_object_style", "target": "curve", "color": "#DC2626"}]))
            self.assertEqual(patch_artist.get_facecolor(), fill)
            for target in ("curve", "edges"):
                path = object_paths(scene, target)[0]
                action = {"type": "set_object_style", "target": target, "color": "#2563EB",
                          "interval": {"path_id": path["id"], "path_sha256": path["sha256"],
                                       "start": .2, "end": .8, "wrap": False}}
                renderer.apply_actions(scene, plugin("Solid79", [action]))
            self.assertEqual(patch_artist.get_facecolor(), fill)
            self.assertEqual((label.get_text(), label.get_position(), label.get_color()), ("frozen label", (7, 7), "black"))
        finally:
            plt.close(fig)

    def test_dense_curves_do_not_create_sample_snap_points(self):
        expected_counts = {"Solid93": 8, "Solid154": 0, "Solid212": 20}
        for qid, count in expected_counts.items():
            with self.subTest(qid=qid):
                metadata = self.metadata_for(qid)
                self.assertEqual(len(metadata["snap_points"]), count)
                self.assertTrue(all("visible_face_vertex" not in point.get("reasons", [])
                                    for point in metadata["snap_points"]))
                if qid == "Solid93":
                    self.assertTrue(all(abs(point["world_xyz"][0] - 1) > 1e-10
                                        for point in metadata["snap_points"]))

    def test_short_polyline_keeps_actual_corner_snap_points(self):
        metadata = self.metadata_for("Solid142")
        points = {point["id"]: point for point in metadata["snap_points"]}
        for name in ("p95", "p96", "p97"):
            self.assertIn(name, points)
            self.assertEqual(points[name]["world_xyz"], self.adapter.scenes["Solid142"]["points"][name])

    def test_transparent_artists_are_not_outline_or_snap_sources(self):
        from dataset_tools.mathvision_workbench import _outline, _visible_artist
        fig, ax = plt.subplots()
        try:
            line, = ax.plot([0, 1], [0, 1], color="black", alpha=0)
            self.assertFalse(_outline(line))
            self.assertFalse(_visible_artist(line))
            fill = PathPatch(VectorPath([[0, 0], [1, 0], [1, 1], [0, 0]], [1, 2, 2, 79]),
                             facecolor="black", edgecolor="none", alpha=0)
            ax.add_patch(fill)
            self.assertFalse(_outline(fill))
            self.assertFalse(_visible_artist(fill))
            fill.set_alpha(None)
            fill.set_facecolor((0, 0, 0, 0))
            self.assertFalse(_visible_artist(fill))
            fill.set_facecolor("black")
            self.assertTrue(_visible_artist(fill))
            collection = LineCollection([[[0, 0], [1, 1]]], colors="black", alpha=0)
            ax.add_collection(collection)
            self.assertFalse(_outline(collection))
            self.assertFalse(_visible_artist(collection))
        finally:
            plt.close(fig)

    def test_native_hidden_dash_lengths_are_fixed_in_points(self):
        renderer = PluginRenderer(self.config, self.adapter, {})
        for qid in ("Solid80", "Solid96"):
            with self.subTest(qid=qid):
                scene = self.adapter.scene(qid)
                try:
                    obj, artist = next((obj, artist) for obj in scene.objects if obj["styleable"]
                        for artist in scene.artists[obj["id"]] if getattr(artist, "_dash_pattern", (0, None))[1] is not None)
                    before = copy.deepcopy(artist._dash_pattern)
                    self.assertEqual(before, (0, [4, 3]))
                    import matplotlib as mpl
                    with mpl.rc_context(scene.settings):
                        renderer.apply_actions(scene, plugin(qid, [{"type": "set_object_style", "target": obj["id"], "linewidth_pt": 3}]))
                    self.assertEqual(artist.get_linewidth(), 3)
                    self.assertEqual(artist._dash_pattern, before)
                    with mpl.rc_context(scene.settings):
                        renderer.apply_actions(scene, plugin(qid, [{"type": "set_object_style", "target": obj["id"],
                            "linewidth_pt": 3, "linestyle": "dashed"}]))
                    self.assertEqual(artist._dash_pattern, (0, [3.7, 1.6]))
                    with mpl.rc_context(scene.settings):
                        renderer.apply_actions(scene, plugin(qid, [{"type": "set_object_style", "target": obj["id"], "linewidth_pt": .5}]))
                    self.assertEqual(artist._dash_pattern, (0, [3.7, 1.6]))
                finally:
                    scene.close()

    def test_native_replay_and_archived_runtime_tampering(self):
        qid = "Solid79"
        metadata = self.metadata_for(qid)
        renderer = PluginRenderer(self.config, self.adapter, {qid: metadata})
        x0, x1 = map(float, metadata["xlim"])
        y0, y1 = map(float, metadata["ylim"])
        normalized, _, digest = renderer.render(plugin(qid, [{"type": "add_line", "id": "qa_line",
            "endpoints": [[x0, y0], [x1, y1]]}]))
        recipe = {**normalized, "generator_version": GENERATOR_VERSION, "plugin_schema_version": SCHEMA_VERSION,
                  "status": "passed", "slot_id": "QA_ONLY", "environment": environment_versions(),
                  "renderer_sha256": renderer_fingerprint(), "schema_sha256": file_hash(ROOT / "plugin.schema.json"),
                  "baseline_fingerprint": self.adapter.manifest["fingerprint"],
                  "parameter_key": canonical_hash(normalized), "pixel_sha256": digest}
        with tempfile.TemporaryDirectory(prefix="native_replay_", dir=QA_ROOT) as temp:
            root = Path(temp)
            config = {**self.config, "runtime_dir": str(root / "runtime"), "output_dir": str(root / "output")}
            config_path = root / "config.json"
            atomic_json(config_path, config)
            output = root / "replayed.png"
            self.assertTrue(render_special_recipe(recipe, output, config_path)["matches_accepted"])
            archived = copy.deepcopy(self.adapter.manifest)
            dependency = self.adapter.records[qid]["runtime_dependencies"][0]
            archived["files"][dependency] = "altered_frozen_dependency"
            archived["fingerprint"] = canonical_hash({"files": archived["files"], "environment": archived["environment"]})
            atomic_json(root / "output/_baselines" / f"{archived['fingerprint']}.json", archived)
            recipe["baseline_fingerprint"] = archived["fingerprint"]
            with self.assertRaises(WorkbenchError) as raised:
                render_special_recipe(recipe, root / "rejected.png", config_path)
            self.assertEqual(raised.exception.code, "baseline_changed")
            self.assertFalse((root / "rejected.png").exists())

    def test_legacy_dependencies_and_accepted_replay(self):
        legacy = LegacyAdapter(self.config)
        for qid in ("Solid01", "Solid07", "Solid78"):
            self.assertEqual(self.adapter.question_dependencies(qid), legacy.question_dependencies(qid))
            self.assertEqual(self.adapter.inspect_question(qid), legacy.inspect_question(qid))
        recipes = [recipe for path in sorted(Path(self.config["output_dir"]).glob("*/recipes.json"))
                   for recipe in read_json(path)]
        self.assertEqual(len(recipes), 30)
        with tempfile.TemporaryDirectory(prefix="accepted_replay_", dir=QA_ROOT) as temp:
            for index, recipe in enumerate(recipes):
                with self.subTest(qid=recipe["question_id"], slot=recipe["slot_id"]):
                    output = Path(temp) / f"{index}.png"
                    self.assertTrue(render_special_recipe(recipe, output)["matches_accepted"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
