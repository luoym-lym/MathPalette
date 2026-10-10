"""Regression checks for spatial truth, projection, visibility and reproducibility."""
import copy
import io
import json
import math
from pathlib import Path
import tempfile
import unittest

import numpy as np
from PIL import Image

import common_renderer as renderer


def independent_scene():
    q = math.sqrt(0.5)
    camera = {"kind": "orthographic", "matrix": [[1, 0, 0], [0, q, -q]],
              "origin": [0, 0, 0], "offset": [0, 0], "toward_viewer": [0, q, q]}
    return {
        "scene_schema_version": "1.0.0", "protocol_version": renderer.read_json(renderer.PROTOCOL_PATH)["protocol_version"],
        "id": "SyntheticTest",
        "status": "test_fixture", "subject": "SolidGeometry", "source_dataset": "Custom",
        "source_image": "unused.png", "source_note": "Independent synthetic geometry for tests.", "world_unit": "m",
        "projection": camera, "visibility": {"mode": "frozen_intervals", "projection_sha256": renderer.projection_fingerprint(camera)},
        "view": {"xlim": [-3, 3], "ylim": [-3, 3]},
        "points": {"O": [0, 0, 0], "X": [1, 0, 0], "Y": [0, 1, 0], "Z": [0, 0, 1], "Q": [1, 1, 0]},
        "objects": [
            {"id": "section", "type": "face", "role": "region", "points": ["O", "X", "Q", "Y"],
             "visibility": "visible", "semantic_fill_reason": "Highlighted synthetic section."},
            {"id": "depth", "type": "segment", "role": "edge", "points": ["O", "Z"], "visibility": "hidden"},
            {"id": "path", "type": "polyline", "role": "auxiliary", "points": ["O", "Y", "Q"],
             "visibility": "visible", "linestyle": "dashed"},
            {"id": "mark", "type": "point", "role": "given_point", "point": "X", "visibility": "visible"},
            {"id": "circle", "type": "circular_arc", "role": "edge", "center": "O", "radius": 1,
             "u": [1, 0, 0], "v": [0, 1, 0], "domain_deg": [0, 360],
             "intervals": [{"start_deg": 0, "end_deg": 360, "samples": 361, "visibility": "visible"}]}],
        "dimensions": [{"id": "true_depth", "type": "distance", "points": ["O", "Z"], "value": 1,
                        "unit": "m", "decimals": 2, "offset_pt": [-110, 0], "label_offset_pt": [-8, 0],
                        "ha": "right", "basis": "synthetic true 3D length"}],
        "labels": [{"id": "name_X", "type": "vertex", "anchor": "X", "text": "X", "offset_pt": [10, -12]}],
        "constraints": [
            {"id": "angle_xyz", "type": "angle", "points": ["X", "O", "Z"], "degrees": 90, "basis": "synthetic"},
            {"id": "in_xy_plane", "type": "coplanar", "points": ["O", "X", "Y", "Q"], "basis": "synthetic"},
            {"id": "circle_y", "type": "on_circle", "point": "Y", "circle": "circle", "basis": "synthetic"}]}


class SolidRendererTests(unittest.TestCase):
    def setUp(self):
        self.scene = independent_scene()

    def test_scene_is_opaque_and_repeatable_in_both_formats(self):
        first, checks = renderer.image_bytes(self.scene)
        self.assertEqual(first, renderer.image_bytes(self.scene)[0])
        self.assertTrue(all(check["passed"] for check in checks))
        with Image.open(io.BytesIO(first)) as image:
            self.assertEqual(image.size, (768, 768))
            self.assertEqual(image.convert("RGBA").getextrema()[3], (255, 255))
        svg, _ = renderer.image_bytes(self.scene, vector=True)
        self.assertEqual(svg, renderer.image_bytes(self.scene, vector=True)[0])
        self.assertIn(b"<svg", svg)

    def test_independent_orthographic_circle_and_world_dimension(self):
        scene = independent_scene()
        q = math.sqrt(0.5)
        np.testing.assert_allclose(renderer.project(scene, scene["points"]["Y"]), [0, q])
        np.testing.assert_allclose(renderer.project(scene, scene["points"]["Z"]), [0, -q])
        circle = scene["objects"][-1]
        _, xy = next(renderer.arc_parts(scene, circle))
        self.assertAlmostEqual(np.ptp(xy[:, 0]), 2)
        self.assertAlmostEqual(np.ptp(xy[:, 1]), 2 * q)
        # A unit world segment projects to sqrt(1/2); the dimension must remain 1 m.
        png, checks = renderer.image_bytes(scene)
        dimension = next(check for check in checks if check["type"] == "dimension")
        self.assertEqual(dimension["text"], "1.00 m")
        self.assertEqual(dimension["measured_world_length"], 1)
        self.assertGreater(len(png), 1000)

    def test_dimension_must_match_world_length(self):
        self.scene["dimensions"][0]["value"] = 2
        with self.assertRaisesRegex(ValueError, "Dimension disagrees"):
            renderer.validate_scene(self.scene)

    def test_distance_range_has_dashes_and_connected_projected_endpoints(self):
        fig, checks = renderer.render_scene(self.scene)
        try:
            lines = {line.get_gid(): line for line in fig.axes[0].lines}
            distance = self.scene["dimensions"][0]
            a, b = renderer.project(self.scene, [self.scene["points"][ref] for ref in distance["points"]])
            start, end, span = [lines["true_depth" + suffix] for suffix in ("_start", "_end", "_range")]
            np.testing.assert_allclose(start.get_xydata()[0], a)
            np.testing.assert_allclose(end.get_xydata()[0], b)
            np.testing.assert_allclose(span.get_xydata(), [start.get_xydata()[1], end.get_xydata()[1]])
            np.testing.assert_allclose(start.get_xydata()[1] - a, end.get_xydata()[1] - b)
            self.assertAlmostEqual(float(np.dot(start.get_xydata()[1] - a, b - a)), 0)
            self.assertTrue(span.is_dashed())
            self.assertFalse(start.is_dashed())
            self.assertFalse(end.is_dashed())
            self.assertEqual(next(c for c in checks if c["type"] == "dimension")["style"], "Plane02_parallel_dashed")
        finally:
            renderer.plt.close(fig)

    def test_distance_range_rejects_zero_or_nonperpendicular_offset(self):
        for offset in ([0, 0], [3, 1]):
            self.scene["dimensions"][0]["offset_pt"] = offset
            with self.assertRaisesRegex(ValueError, "perpendicular in projection"):
                renderer.validate_scene(self.scene)

    def test_symbolic_distance_label_does_not_expose_construction_value(self):
        self.scene["dimensions"][0]["text"] = "h m"
        _, checks = renderer.image_bytes(self.scene)
        self.assertEqual(next(c for c in checks if c["type"] == "dimension")["text"], "h m")

    def test_changed_projection_invalidates_frozen_visibility(self):
        self.scene["projection"]["offset"][0] = 0.1
        with self.assertRaisesRegex(ValueError, "Visibility is stale"):
            renderer.validate_scene(self.scene)

    def test_projection_models_are_checked(self):
        self.scene["projection"]["kind"] = "perspective"
        with self.assertRaisesRegex(ValueError, "Unsupported projection"):
            renderer.validate_scene(self.scene)
        self.scene["projection"]["kind"] = "orthographic"
        self.scene["projection"]["matrix"][0][0] = 2
        with self.assertRaisesRegex(ValueError, "must be orthonormal"):
            renderer.validate_scene(self.scene)

    def test_projected_tangent_rejects_a_secant(self):
        tangent = {"id": "tangent_at_X", "type": "projected_tangent", "point": "X",
                   "circle": "circle", "segment": ["X", "Q"], "basis": "synthetic"}
        self.scene["constraints"].append(tangent)
        renderer.validate_scene(self.scene)
        tangent["segment"] = ["X", "Y"]
        with self.assertRaisesRegex(ValueError, "Geometry constraint failed: tangent_at_X"):
            renderer.validate_scene(self.scene)

    def test_unknown_visibility_is_rejected(self):
        self.scene["objects"][-1]["intervals"][0]["visibility"] = "unknown"
        with self.assertRaisesRegex(ValueError, "Unsupported visibility"):
            renderer.validate_scene(self.scene)

    def test_arc_gaps_and_coarse_sampling_are_rejected(self):
        scene = copy.deepcopy(self.scene)
        scene["objects"][-1]["intervals"][0]["start_deg"] += 0.5
        with self.assertRaisesRegex(ValueError, "without gaps or overlaps"):
            renderer.validate_scene(scene)
        self.scene["objects"][-1]["intervals"][0]["samples"] = 2
        with self.assertRaisesRegex(ValueError, "sampling is too coarse"):
            renderer.validate_scene(self.scene)

    def test_nonfinite_points_and_unsupported_types_are_rejected(self):
        scene = copy.deepcopy(self.scene)
        scene["points"]["Z"][2] = float("nan")
        with self.assertRaisesRegex(ValueError, "Expected finite"):
            renderer.validate_scene(scene)
        scene = copy.deepcopy(self.scene)
        scene["objects"][0]["type"] = "unknown"
        with self.assertRaisesRegex(ValueError, "Unsupported object"):
            renderer.validate_scene(scene)
        self.scene["constraints"][0]["type"] = "unknown"
        with self.assertRaisesRegex(ValueError, "Unsupported constraint"):
            renderer.validate_scene(self.scene)

    def test_annotations_cannot_cover_edges_or_leave_margin(self):
        self.scene["dimensions"][0]["label_offset_pt"] = [-1000, 0]
        with self.assertRaisesRegex(ValueError, "outer margin"):
            renderer.image_bytes(self.scene)
        self.scene = independent_scene()
        self.scene["dimensions"][0]["label_offset_pt"] = [0, 0]
        self.scene["dimensions"][0]["ha"] = "center"
        with self.assertRaisesRegex(ValueError, "overlaps a diagram line"):
            renderer.image_bytes(self.scene)

    def test_source_cannot_be_overwritten_via_relative_alias(self):
        with tempfile.TemporaryDirectory() as folder:
            directory = Path(folder)
            (directory / "assets").mkdir()
            source = directory / "unused.png"
            original = b"synthetic source fixture"
            source.write_bytes(original)
            self.scene["source_image"] = "assets/../unused.png"
            scene_path = directory / "scene.json"
            scene_path.write_text(json.dumps(self.scene), encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "cannot overwrite"):
                renderer.draw(scene_path, directory / self.scene["source_image"])
            self.assertEqual(source.read_bytes(), original)

    def test_draw_api_writes_only_the_requested_output(self):
        with tempfile.TemporaryDirectory() as folder:
            scene_path = Path(folder) / "scene.json"
            scene_path.write_text(json.dumps(self.scene), encoding="utf-8")
            target = Path(folder) / "render.svg"
            result = renderer.draw(scene_path, target)
            self.assertEqual(result["image_path"], str(target.resolve()))
            self.assertEqual({p.name for p in Path(folder).iterdir()}, {"scene.json", "render.svg"})


if __name__ == "__main__":
    unittest.main(verbosity=2)
