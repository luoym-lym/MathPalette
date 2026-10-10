"""Check geometric truth, relation markers and deterministic output."""
import copy
import unittest
from common_renderer import image_bytes, validate_scene


class GeometryRendererTests(unittest.TestCase):
    def setUp(self):
        self.scene = {
            "scene_schema_version": "1.0.0", "protocol_version": "1.0.0",
            "source_dataset": "Custom", "view": {"xlim": [-2, 5], "ylim": [-2, 5]},
            "points": {"R": [0, 0], "S": [3, 0], "T": [0, 3], "U": [3, 3]},
            "objects": [
                {"id": "side_RS", "type": "segment", "points": ["R", "S"]},
                {"id": "side_RT", "type": "segment", "points": ["R", "T"]},
                {"id": "diagonal_ST", "type": "segment", "points": ["S", "T"]},
                {"id": "diagonal_RU", "type": "segment", "points": ["R", "U"]},
                {"id": "side_TU", "type": "segment", "points": ["T", "U"]}],
            "labels": [
                {"id": "angle_R", "type": "angle", "points": ["S", "R", "T"], "degrees": 90},
                {"id": "angle_S", "type": "angle", "points": ["R", "S", "T"], "degrees": 45}],
            "constraints": [
                {"id": "right_angle", "type": "angle", "points": ["S", "R", "T"], "degrees": 90},
                {"id": "acute_angle", "type": "angle", "points": ["R", "S", "T"], "degrees": 45},
                {"id": "side_length", "type": "distance", "points": ["R", "S"], "value": 3},
                {"id": "diagonal_crossing", "type": "intersection", "segments": [["R", "U"], ["S", "T"]], "intersects": True},
                {"id": "separate_sides", "type": "intersection", "segments": [["R", "S"], ["T", "U"]], "intersects": False},
                {"id": "equal_sides", "type": "equal_length", "segments": [["R", "S"], ["R", "T"]]}],
        }

    def test_scene_is_exact_and_repeatable(self):
        first, checks = image_bytes(self.scene)
        repeated, _ = image_bytes(self.scene)
        self.assertEqual(first, repeated)
        self.assertEqual(len(checks), 6)
        self.assertTrue(all(check["passed"] for check in checks))
        svg, _ = image_bytes(self.scene, vector=True)
        svg_again, _ = image_bytes(self.scene, vector=True)
        self.assertEqual(svg, svg_again)
        self.assertIn(b"<svg", svg)

    def test_changed_angles_and_wrong_annotations_fail(self):
        changed = copy.deepcopy(self.scene)
        changed["points"]["T"][0] += 0.1
        with self.assertRaisesRegex(ValueError, "Geometry constraint failed"):
            validate_scene(changed)
        changed = copy.deepcopy(self.scene)
        changed["labels"][-1]["degrees"] = 46
        with self.assertRaisesRegex(ValueError, "Angle label disagrees"):
            validate_scene(changed)

    def test_unknown_objects_and_constraints_fail(self):
        changed = copy.deepcopy(self.scene)
        changed["objects"][0]["type"] = "unsupported"
        with self.assertRaisesRegex(ValueError, "Unsupported object"):
            image_bytes(changed)
        changed = copy.deepcopy(self.scene)
        changed["constraints"][0]["type"] = "unsupported"
        with self.assertRaisesRegex(ValueError, "Unsupported constraint"):
            validate_scene(changed)

    def test_reflex_angle_and_true_right_angle_markers(self):
        scene = {"scene_schema_version": "1.0.0", "protocol_version": "1.0.0", "source_dataset": "Custom",
                 "view": {"xlim": [-2, 6], "ylim": [-2, 6]},
                 "points": {"A": [0, 0], "B": [4, 0], "C": [0, 4], "M": [2, 0], "D": [4, 4]},
                 "objects": [
                     {"id": "triangle", "type": "polygon", "points": ["A", "B", "C"], "semantic_fill": True},
                     {"id": "circle", "type": "circle", "center": "A", "radius": 1},
                     {"id": "arc", "type": "arc", "center": "D", "radius": 0.5, "start_deg": 0, "end_deg": 90},
                     {"id": "point", "type": "point", "point": "M", "filled": False},
                     {"id": "right", "type": "right_angle", "points": ["B", "A", "C"]},
                     {"id": "angle", "type": "angle_arc", "points": ["B", "A", "C"], "radius_pt": 22},
                     {"id": "tick", "type": "equal_tick", "points": ["A", "B"], "count": 2},
                     {"id": "parallel", "type": "parallel_mark", "points": ["C", "D"], "count": 2}],
                 "labels": [{"id": "reflex", "type": "angle", "points": ["B", "A", "C"], "degrees": 270, "reflex": True}],
                 "constraints": [
                     {"id": "angle", "type": "angle", "points": ["B", "A", "C"], "degrees": 270, "reflex": True},
                     {"id": "distance", "type": "distance", "points": ["A", "B"], "value": 4},
                     {"id": "collinear", "type": "collinear", "points": ["A", "M", "B"]},
                     {"id": "between", "type": "between", "points": ["A", "M", "B"]},
                     {"id": "parallel", "type": "parallel", "segments": [["A", "B"], ["C", "D"]]},
                     {"id": "perpendicular", "type": "perpendicular", "segments": [["A", "B"], ["A", "C"]]},
                     {"id": "equal_length", "type": "equal_length", "segments": [["A", "B"], ["A", "C"]]},
                     {"id": "on_circle", "type": "on_circle", "point": "B", "center": "A", "radius": 4}]}
        first, checks = image_bytes(scene)
        self.assertTrue(all(check["passed"] for check in checks))
        self.assertEqual(first, image_bytes(scene)[0])
        scene["objects"][4]["points"] = ["A", "B", "C"]
        with self.assertRaisesRegex(ValueError, "requires a true right angle"):
            image_bytes(scene)

    def test_invalid_view_and_topology_fail(self):
        changed = copy.deepcopy(self.scene)
        changed["view"]["ylim"][1] += 1
        with self.assertRaisesRegex(ValueError, "must be square"):
            validate_scene(changed)
        changed = copy.deepcopy(self.scene)
        changed["constraints"][3]["intersects"] = False
        with self.assertRaisesRegex(ValueError, "Geometry constraint failed"):
            validate_scene(changed)


if __name__ == "__main__":
    unittest.main(verbosity=2)
