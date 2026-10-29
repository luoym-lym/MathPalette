"""Native MathVision integration QA; all generated artifacts stay in .runtime/."""
from __future__ import annotations

import copy
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import matplotlib as mpl
from matplotlib.collections import LineCollection
from matplotlib.lines import Line2D
from matplotlib.patches import PathPatch
from matplotlib.path import Path as MplPath
import numpy as np

from mathvision_adapter import RendererAdapter
from mathvision_plugins import PluginRenderer, _set_linewidth_preserving_dashes
from mathvision_replay import render_special_recipe
from renderer_adapter import RendererAdapter as LegacyRendererAdapter
from render_plugins import PluginRenderer as LegacyPluginRenderer
from workbench_io import (GENERATOR_VERSION, ROOT, SCHEMA_VERSION, WorkbenchError, atomic_json,
                          canonical_hash, environment_versions, file_hash, load_config,
                          pixel_hash, renderer_fingerprint)


FIXTURES = ROOT.parents[1] / ".runtime/mathvision_workbench_sync_20261029/plane_tests"
NATIVE_EXAMPLES = ("Plane140", "Plane141", "Plane145", "Plane225", "Plane268",
                   "Plane327", "Plane338", "Plane465", "Plane477")


def plugin(qid, *actions):
    return {"plugin_schema_version": SCHEMA_VERSION, "question_id": qid, "category": "C",
            "operation": "C_manual", "description": "TEMPORARY SOFTWARE TEST FIXTURE",
            "intent": "isolated native renderer QA only", "params": {"actions": list(actions)}}


class MathVisionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.config = load_config()
        cls.adapter = RendererAdapter(cls.config)
        cls.metadata = {}

    def metadata_for(self, qid):
        if qid not in self.metadata:
            self.metadata[qid] = self.adapter.inspect_question(qid)
        return self.metadata[qid]

    def renderer_for(self, qid):
        return PluginRenderer(self.config, self.adapter, {qid: self.metadata_for(qid)})

    def test_all_native_formal_baselines_and_canvas(self):
        native = [qid for qid in self.adapter.records if self.adapter.is_native(qid)]
        self.assertEqual(native, [f"Plane{i}" for i in range(140, 491)])
        for qid in native:
            with self.subTest(qid=qid):
                meta = self.metadata_for(qid)
                self.assertEqual(meta["original_pixel_sha256"], pixel_hash(self.adapter.original_paths[qid]))
                canvas = meta["canvas"]
                self.assertEqual((canvas["width"], canvas["height"]), (768, 768))
                self.assertEqual({obj["id"] for obj in meta["objects"] if obj["styleable"]},
                                 {target["id"] for target in canvas["targets"]})
                self.assertTrue(all(target["paths"] and target["partial_paths"]
                                    for target in canvas["targets"]))
                self.assertTrue(np.allclose(np.array(canvas["data_to_pixel"]) @
                                            np.array(canvas["pixel_to_data"]), np.eye(3)))
                for point in canvas["snap_points"]:
                    xy = np.array(canvas["pixel_to_data"]) @ [*point["pixel"], 1]
                    self.assertTrue(np.allclose(xy[:2], point["xy"], rtol=0, atol=1e-12))

    def test_legacy_dispatch_and_dependencies_are_exact(self):
        legacy = LegacyRendererAdapter(self.config)
        for qid in legacy.records:
            if not self.adapter.is_native(qid):
                self.assertEqual(self.adapter.dependencies(qid), legacy.dependencies(qid))
        for qid in ("Plane01", "Plane72", "Plane139"):
            old_meta = legacy.inspect_question(qid)
            self.assertEqual(self.adapter.inspect_question(qid), old_meta)
            target = old_meta["canvas"]["targets"][0]["id"]
            value = plugin(qid, {"type": "set_object_style", "target": target, "color": "#DC2626"})
            expected = LegacyPluginRenderer(self.config, legacy, {qid: old_meta}).render(value)
            actual = self.renderer_for(qid).render(value)
            self.assertEqual(actual, expected)

    def test_extension_executables_are_native_question_inputs(self):
        for relative in ("mathvision_workbench.py", "workbench/mathvision_adapter.py",
                         "workbench/mathvision_plugins.py", "workbench/mathvision_replay.py",
                         "workbench/replay_archived.py", "workbench/review_store.py",
                         "workbench/drawing_board.py"):
            self.assertIn(relative, self.adapter.dependencies("Plane140"))
            self.assertNotIn(relative, self.adapter.dependencies("Plane01"))
            self.assertIn(relative, self.adapter.manifest["files"])

    def test_fixed_added_marks_and_deterministic_native_serialization(self):
        for qid in NATIVE_EXAMPLES:
            canvas = self.metadata_for(qid)["canvas"]
            xmin, xmax = canvas["xlim"]
            ymin, ymax = canvas["ylim"]
            a = [xmin + (xmax - xmin) * .25, ymin + (ymax - ymin) * .45]
            b = [xmin + (xmax - xmin) * .75, ymin + (ymax - ymin) * .55]
            renderer = self.renderer_for(qid)
            for style in ("solid", "dashed"):
                with self.subTest(qid=qid, style=style):
                    value = plugin(qid, {"type": "add_point", "id": "qaPoint", "xy": a},
                                   {"type": "add_line", "id": "qaLine", "endpoints": [a, b], "linestyle": style})
                    normalized, data, digest = renderer.render(value)
                    self.assertEqual(pixel_hash(data), digest)
                    self.assertEqual(renderer.render(normalized, frozen=True), (normalized, data, digest))
                    point, line = normalized["params"]["actions"]
                    self.assertEqual((point["size_pt2"], point["edge_linewidth_pt"], point["filled"]), (50, 1, True))
                    self.assertEqual(line["linewidth_pt"], 1)
                    self.assertEqual(line.get("dash_pattern_pt"), [3.7, 1.6] if style == "dashed" else None)

    def test_whole_and_partial_styles_keep_geometry_fills_and_labels(self):
        for qid in NATIVE_EXAMPLES:
            target = self.metadata_for(qid)["canvas"]["targets"][0]
            path = target["partial_paths"][0]
            renderer = self.renderer_for(qid)
            for partial in (False, True):
                with self.subTest(qid=qid, partial=partial):
                    action = {"type": "set_object_style", "target": target["id"],
                              "color": "#16A34A", "linewidth_pt": 2, "linestyle": "dashed"}
                    if partial:
                        action["interval"] = {"path_id": path["id"], "path_sha256": path["sha256"],
                                              "start": .2, "end": .7, "wrap": False}
                    scene = self.adapter.scene(qid)
                    fills = [(artist, artist.get_facecolor()) for artist in scene.ax.patches]
                    labels = [(text, text.get_text(), text.get_position(), text.get_color()) for text in scene.ax.texts]
                    original_geometry = copy.deepcopy(scene.objects)
                    with patch.object(self.adapter, "scene", return_value=scene):
                        normalized, _, digest = renderer.render(plugin(qid, action))
                    self.assertNotEqual(digest, self.metadata_for(qid)["original_pixel_sha256"])
                    self.assertEqual(scene.objects, original_geometry)
                    for artist, color in fills:
                        self.assertEqual(artist.get_facecolor(), color)
                    for text, content, position, color in labels:
                        self.assertEqual((text.get_text(), text.get_position(), text.get_color()), (content, position, color))
                    self.assertEqual(renderer.render(normalized, frozen=True)[2], digest)

    def test_unchanged_schema_rejects_invalid_actions_and_stale_paths(self):
        qid = "Plane140"
        renderer = self.renderer_for(qid)
        target = self.metadata_for(qid)["canvas"]["targets"][0]
        invalid = [
            {"type": "add_text", "id": "qaText", "xy": [0, 0], "text": "forbidden"},
            {"type": "add_point", "id": "qaPoint", "xy": [0, 0], "size_pt2": 51},
            {"type": "set_object_style", "target": target["id"], "color": "#FFFFFF"},
            {"type": "set_object_style", "target": target["id"], "linewidth_pt": 4},
            {"type": "set_object_style", "target": target["id"], "color": "#DC2626",
             "interval": {"path_id": "p0", "path_sha256": "0" * 64, "start": .2, "end": .7, "wrap": False}},
        ]
        for action in invalid:
            with self.subTest(action=action), self.assertRaises(WorkbenchError):
                renderer.normalize(plugin(qid, action))
        for value in (None, [], {"question_id": []}):
            with self.subTest(value=value), self.assertRaises(WorkbenchError):
                renderer.render(value)

    def test_linewidth_only_keeps_absolute_native_dash_patterns(self):
        def patterns(artist):
            styles = artist.get_linestyles() if isinstance(artist, LineCollection) else [artist._dash_pattern]
            return [(float(offset), None if dash is None else tuple(float(v) for v in dash))
                    for offset, dash in styles]

        # Exercise actual native Line2D and Patch subclasses emitted by the
        # frozen Plane renderers, including sequential overlapping overrides.
        for qid, target in (("Plane144", "source_grid0_10_0"), ("Plane173", "o11"),
                            ("Plane183", "ring_guide"), ("Plane215", "o5")):
            renderer = self.renderer_for(qid)
            for explicit_style in (False, True):
                with self.subTest(qid=qid, explicit_style=explicit_style):
                    scene = self.adapter.scene(qid)
                    original = [patterns(artist) for artist in scene.artists[target]]
                    self.assertTrue(any(dash is not None for artist in original for _, dash in artist))
                    actions = [{"type": "set_object_style", "target": target, "linewidth_pt": 3}]
                    if explicit_style:
                        actions[0]["linestyle"] = "dashed"
                    actions.append({"type": "set_object_style", "target": target, "linewidth_pt": .5})
                    with patch.object(self.adapter, "scene", return_value=scene), mpl.rc_context({"lines.scale_dashes": True}):
                        normalized, _, digest = renderer.render(plugin(qid, *actions))
                    for index, artist in enumerate(scene.artists[target]):
                        self.assertEqual(artist.get_linewidth(), .5)
                        self.assertEqual(patterns(artist), [(0., (3.7, 1.6))] if explicit_style else original[index])
                    self.assertEqual(renderer.render(normalized, frozen=True)[2], digest)

        # No native Plane renderer currently emits LineCollection. This covers
        # its per-fragment patterns and already-scaled non-unit source widths.
        with mpl.rc_context({"lines.scale_dashes": True}):
            examples = [
                Line2D([0, 1], [0, 1], linewidth=2, linestyle=(1, (2, 1))),
                PathPatch(MplPath([[0, 0], [1, 1]]), linewidth=2, linestyle=(1, (2, 1))),
                LineCollection([[[0, 0], [1, 1]], [[1, 0], [0, 1]]], linewidths=[2, 3],
                               linestyles=[(1, (2, 1)), (2, (4, 2))]),
            ]
            for artist in examples:
                expected = patterns(artist)
                for width in (3, .5, 2):
                    _set_linewidth_preserving_dashes(artist, width)
                    self.assertEqual(patterns(artist), expected)

    def test_native_offline_replay_and_changed_extension_rejection(self):
        # This in-memory recipe is a software fixture, never a human approval.
        # There is no Pass/Collect call and no write to special_variant/.
        qid = "Plane140"
        target = self.metadata_for(qid)["canvas"]["targets"][0]["id"]
        normalized, _, digest = self.renderer_for(qid).render(plugin(qid, {
            "type": "set_object_style", "target": target, "color": "#DC2626"}))
        recipe = {**normalized, "generator_version": GENERATOR_VERSION, "status": "passed",
                  "slot_id": "C01", "environment": environment_versions(),
                  "renderer_sha256": renderer_fingerprint(), "schema_sha256": file_hash(ROOT / "plugin.schema.json"),
                  "question_record_sha256": canonical_hash(self.adapter.records[qid]),
                  "baseline_fingerprint": self.adapter.manifest["fingerprint"],
                  "parameter_key": canonical_hash(normalized), "pixel_sha256": digest}
        FIXTURES.mkdir(parents=True, exist_ok=True)
        with tempfile.TemporaryDirectory(prefix="replay-", dir=FIXTURES) as temporary:
            directory = Path(temporary)
            config = copy.deepcopy(self.config)
            config.update(runtime_dir=str(directory / "runtime"), output_dir=str(directory / "output"),
                          dataset_root=str(ROOT.parent))
            # Replay reads only this isolated archive and writes reproduced/.
            config_path = directory / "config.json"
            atomic_json(config_path, config)
            first = render_special_recipe(recipe, config_path=config_path)
            self.assertEqual(first["pixel_sha256"], digest)
            self.assertTrue(Path(first["image_path"]).is_relative_to(directory))
            archive = copy.deepcopy(self.adapter.manifest)
            archive["files"]["workbench/mathvision_plugins.py"] = "0" * 64
            archive["fingerprint"] = canonical_hash({"files": archive["files"], "environment": archive["environment"]})
            changed = {**recipe, "baseline_fingerprint": archive["fingerprint"]}
            atomic_json(directory / "output/_baselines" / f"{archive['fingerprint']}.json", archive)
            with self.assertRaises(WorkbenchError) as error:
                render_special_recipe(changed, config_path=config_path)
            self.assertEqual(error.exception.code, "baseline_changed")
            changed = {**recipe, "renderer_sha256": "0" * 64}
            with self.assertRaises(WorkbenchError) as error:
                render_special_recipe(changed, config_path=config_path)
            self.assertEqual(error.exception.code, "renderer_changed")


if __name__ == "__main__":
    unittest.main()
