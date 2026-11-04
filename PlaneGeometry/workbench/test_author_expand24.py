"""Exercise native author scenes through the real workbench; never Pass/Collect."""
from __future__ import annotations

import copy
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import numpy as np

from expand24_adapter import RendererAdapter, is_expand24_record
from expand24_plugins import PluginRenderer
from replay_archived import render_special_recipe
from workbench_io import WorkbenchError, load_config, pixel_hash, read_json


class ExpandedAuthorTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.config = load_config()
        cls.adapter = RendererAdapter(cls.config)
        cls.ids = [qid for qid, row in cls.adapter.records.items()
                   if row.get("source_key", "").startswith("author-expand24:")]
        if not cls.ids:
            raise AssertionError("No installed author-expand24 originals")
        # A native construction must never reach the generic constraint validator.
        with patch.object(cls.adapter.renderer, "render_scene",
                          side_effect=AssertionError("Native scene reached generic renderer")):
            cls.metadata = {qid: cls.adapter.inspect_question(qid) for qid in cls.ids}
        cls.renderer = PluginRenderer(cls.config, cls.adapter, cls.metadata)

    def plugin(self, qid, actions):
        return {"plugin_schema_version": "1.0.0", "question_id": qid, "category": "C",
                "operation": "C_manual", "description": "TEMPORARY SOFTWARE TEST FIXTURE",
                "params": {"actions": actions}}

    def test_noop_pixels_board_transforms_and_exact_snap_points(self):
        for qid in self.ids:
            with self.subTest(qid=qid):
                self.assertTrue(self.adapter.is_author(qid))
                meta = self.metadata[qid]
                self.assertEqual(meta["original_pixel_sha256"], pixel_hash(self.adapter.original_paths[qid]))
                board = meta["canvas"]
                self.assertEqual((board["width"], board["height"]), (768, 768))
                np.testing.assert_allclose(np.array(board["data_to_pixel"]) @ board["pixel_to_data"],
                                           np.eye(3), atol=1e-10)
                item = self.adapter.branch / "dataset_generator/author_expand24_v1/items" / qid
                frozen_snaps = read_json(item / "drawing_context.json").get("snap_points", [])
                self.assertEqual([p["xy"] for p in meta["snap_points"]], [p["xy"] for p in frozen_snaps])
                self.assertEqual({o["id"] for o in meta["objects"]}, {t["id"] for t in board["targets"]})
                self.assertTrue(all(t["paths"] and t["partial_paths"] for t in board["targets"]))

    def test_actions_preserve_original_geometry_labels_and_fills(self):
        # One example of each native family, including protected dot arrays.
        for qid in ("Plane512", "Plane515", "Plane518", "Plane521", "Plane524", "Plane527"):
            with self.subTest(qid=qid):
                scene = self.adapter.scene(qid)
                labels = [(t.get_text(), t.get_position(), t.get_color()) for t in scene.ax.texts]
                fills = [p.get_facecolor() for p in scene.ax.patches]
                paths = [p.get_path().vertices.copy() for p in scene.ax.patches]
                dots = [p.get_offsets().copy() for p in scene.ax.collections]
                limits = (scene.ax.get_xlim(), scene.ax.get_ylim())
                snaps = self.metadata[qid]["snap_points"]
                if snaps:
                    a, b = snaps[0]["xy"], snaps[-1]["xy"]
                else:
                    # Coin centers are intentionally absent from snap points.
                    (xmin, xmax), (ymin, ymax) = limits
                    a = [float(xmin + .2 * (xmax - xmin)), float(ymin + .2 * (ymax - ymin))]
                    b = [float(xmin + .8 * (xmax - xmin)), float(ymin + .7 * (ymax - ymin))]
                actions = [{"type": "add_line", "id": "fixture_line", "endpoints": [a, b]},
                           {"type": "add_point", "id": "fixture_point", "xy": a}]
                if scene.objects:
                    actions.append({"type": "set_object_style", "target": scene.objects[0]["id"],
                                    "color": "#DC2626", "linestyle": "dashed", "linewidth_pt": 2})
                else:
                    self.assertEqual(self.metadata[qid]["canvas"]["targets"], [])
                with patch.object(self.adapter, "scene", return_value=scene):
                    normalized, data, digest = self.renderer.render(self.plugin(qid, actions))
                self.assertEqual(normalized["params"]["actions"][0]["dash_pattern_pt"], [3.7, 1.6])
                self.assertEqual(pixel_hash(data), digest)
                self.assertNotEqual(digest, self.metadata[qid]["original_pixel_sha256"])
                self.assertEqual(limits, (scene.ax.get_xlim(), scene.ax.get_ylim()))
                self.assertEqual(labels, [(t.get_text(), t.get_position(), t.get_color()) for t in scene.ax.texts])
                self.assertEqual(fills, [p.get_facecolor() for p in scene.ax.patches])
                for original, artist in zip(paths, scene.ax.patches):
                    np.testing.assert_array_equal(original, artist.get_path().vertices)
                for original, artist in zip(dots, scene.ax.collections):
                    np.testing.assert_array_equal(original, artist.get_offsets())
                normalized2, data2, digest2 = self.renderer.render(normalized, frozen=True)
                self.assertEqual(normalized2, normalized)
                self.assertEqual(digest2, digest)
                self.assertEqual(pixel_hash(data2), digest)
                self.assertEqual(self.adapter.inspect_question(qid)["original_pixel_sha256"],
                                 self.metadata[qid]["original_pixel_sha256"])

    def test_partial_style_and_path_hash_guard(self):
        for qid in ("Plane512", "Plane515", "Plane518", "Plane521"):
            with self.subTest(qid=qid):
                target = self.metadata[qid]["canvas"]["targets"][0]
                path = target["partial_paths"][0]
                interval = {"path_id": path["id"], "path_sha256": path["sha256"],
                            "start": .2, "end": .6, "wrap": False}
                plugin = self.plugin(qid, [{"type": "set_object_style", "target": target["id"],
                                           "color": "#2563EB", "interval": interval}])
                normalized, _, digest = self.renderer.render(plugin)
                self.assertNotEqual(digest, self.metadata[qid]["original_pixel_sha256"])
                self.assertEqual(self.renderer.render(normalized, frozen=True)[2], digest)
                invalid = copy.deepcopy(plugin)
                invalid["params"]["actions"][0]["interval"]["path_sha256"] = "0" * 64
                with self.assertRaises(WorkbenchError):
                    self.renderer.render(invalid)

    def test_unregistered_dependencies_and_wrong_identity_are_rejected(self):
        qid = self.ids[0]
        invalid = copy.deepcopy(self.adapter.records[qid])
        invalid["runtime_dependencies"].pop()
        self.assertFalse(is_expand24_record(invalid))
        read = read_json

        def wrong_identity(path):
            value = read(path)
            if Path(path).name == "identity.json":
                value["id"] = "Plane01"
            return value

        with patch("expand24_adapter.read_json", side_effect=wrong_identity):
            with self.assertRaises(WorkbenchError) as raised:
                self.adapter.scene(qid)
        self.assertEqual(raised.exception.code, "baseline_changed")

    def test_existing_promote15_originals_and_saved_variants_still_reproduce(self):
        temporary = Path(self.config["runtime_dir"]).parent / "plane_workbench_tests"
        temporary.mkdir(parents=True, exist_ok=True)
        # Reuse the actual current manifest; retain all per-question input,
        # parameter and saved-pixel checks in the real replay functions.
        with tempfile.TemporaryDirectory(prefix="expand24_replay_", dir=temporary) as directory, \
                patch("replay_archived.RendererAdapter", return_value=self.adapter), \
                patch("author_replay.RendererAdapter", return_value=self.adapter):
            count = 0
            for qid in (f"Plane{i}" for i in range(506, 512)):
                self.adapter.inspect_question(qid)
                saved = Path(self.config["output_dir"]) / qid / "recipes.json"
                for recipe in read_json(saved) if saved.is_file() else []:
                    target = Path(directory) / f"{qid}_{recipe['slot_id']}.png"
                    result = render_special_recipe(recipe, target)
                    self.assertTrue(result["matches_accepted"])
                    self.assertEqual(pixel_hash(target), recipe["pixel_sha256"])
                    count += 1
            self.assertGreater(count, 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
