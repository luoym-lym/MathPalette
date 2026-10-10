"""Isolated tests of Base semantics, frozen replay, and new-question Special discovery."""
from __future__ import annotations

import io
import json
import math
import random
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

import numpy as np
from PIL import Image

from base_support import ROOT, Dataset, canonical_hash, pending_special, pixel_hash, read_json
from generate_base_variants import BaseGenerator, OPERATIONS, apply_plugin, make_plugin, redraw, sample_params
from prepare_question import prepare


class BasePipelineTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory(prefix="mathpalette_base_test_")
        self.temporary_path = Path(self.temporary.name).resolve()
        self.assertTrue(self.temporary_path.is_relative_to(Path(tempfile.gettempdir()).resolve()))
        self.root = self.temporary_path / "dataset"
        helpers = self.root / "dataset_generator"
        (helpers / "dataset_generator").mkdir(parents=True)
        (self.root / "image").mkdir()
        for name in ("common_renderer.py", "protocol.json", "base_protocol.json"):
            shutil.copy2(ROOT / "dataset_generator" / name, helpers / name)
        shutil.copy2(ROOT / "dataset_generator/dataset_generator/function_plot01.py",
                     helpers / "dataset_generator/function_plot01.py")
        shutil.copy2(ROOT / "image/Ana01.png", self.root / "image/Ana01.png")
        row = Dataset(ROOT).records["Ana01"]
        (self.root / "dataset.jsonl").write_text(json.dumps(row) + "\n", encoding="utf-8")
        self.generator = BaseGenerator(self.root)

    def tearDown(self):
        self.temporary.cleanup()

    def test_rendering_semantics_and_pure_blue(self):
        generator = self.generator
        original = generator.dataset.verify_original("Ana01")
        for mode, count in (("off", 0), ("half_density", 9)):
            with generator.dataset.scene("Ana01") as fig:
                apply_plugin(fig, {"operation": "Base1", "params": {
                    "mode": mode, "grid_positions": [] if mode == "off" else list(range(-8, 9, 2))}})
                for axis in (fig.axes[0].xaxis, fig.axes[0].yaxis):
                    self.assertEqual(sum(t.gridline.get_visible() for t in axis.get_major_ticks()), count)
                    self.assertEqual(list(axis.get_majorticklocs()), list(range(-8, 9)))
        with generator.dataset.scene("Ana01") as fig:
            apply_plugin(fig, make_plugin("Ana01", "Base2", 1, generator.policy))
            ax = fig.axes[0]
            self.assertFalse(ax._mp_origin_zero.get_visible())
            self.assertFalse(ax.get_xticklabels())
            self.assertFalse(ax.get_yticklabels())
            self.assertTrue(ax.spines["left"].get_visible())
        for operation in OPERATIONS:
            plugin = make_plugin("Ana01", operation, 123, generator.policy)
            first = generator.render(plugin)
            self.assertEqual(pixel_hash(first), pixel_hash(generator.render(plugin)))
            self.assertNotEqual(pixel_hash(first), pixel_hash(original))
            with Image.open(io.BytesIO(first)) as image:
                self.assertEqual(image.size, (768, 768))
                if operation == "Base3":
                    self.assertEqual(image.convert("RGB").getpixel((0, 0)), (0, 0, 255))
                    self.assertEqual(image.convert("RGB").getpixel((120, 110)), (0, 0, 255))

    def test_geometry_ranges_and_sampling_coverage(self):
        shapes, orientations, colors, fills, counts = set(), set(), set(), set(), set()
        for seed in range(200):
            shape = sample_params("Base5", random.Random(seed), self.generator.policy)
            shapes.add(shape["shape"])
            self.assertTrue(all(-6 <= c <= 6 for c in shape["center"]))
            self.assertTrue(0.8 <= shape["width"] <= 2.5 and 0.8 <= shape["height"] <= 2.5)
            if shape["shape"] == "ellipse":
                theta = math.radians(shape["angle_deg"])
                a, b = shape["width"] / 2, shape["height"] / 2
                extent = [math.hypot(a * math.cos(theta), b * math.sin(theta)),
                          math.hypot(a * math.sin(theta), b * math.cos(theta))]
                self.assertTrue(all(abs(c) + e <= 8 for c, e in zip(shape["center"], extent)))
            else:
                self.assertLessEqual(np.abs(shape["vertices"]).max(), 8)
                x, y = np.asarray(shape["vertices"]).T
                self.assertGreater(abs(x @ np.roll(y, 1) - y @ np.roll(x, 1)), 0)
            line = sample_params("Base4", random.Random(seed), self.generator.policy)
            orientations.add(line["orientation"])
            colors.add(line["color"])
            self.assertEqual(line["linestyle"], "dashed")
            self.assertNotEqual(line["endpoints"][0], line["endpoints"][1])
            for endpoint in line["endpoints"]:
                self.assertTrue(all(-8 <= v <= 8 for v in endpoint))
                self.assertAlmostEqual(max(abs(v) for v in endpoint), 8)
            points = sample_params("Base6", random.Random(seed), self.generator.policy)["points"]
            counts.add(len(points))
            self.assertEqual(len(points), len({tuple(p["xy"]) for p in points}))
            for point in points:
                fills.add(point["filled"])
                self.assertTrue(all(type(v) is int and -8 <= v <= 8 for v in point["xy"]))
        self.assertEqual(shapes, {"ellipse", "rectangle", "triangle"})
        self.assertEqual(orientations, {"horizontal", "vertical", "oblique"})
        self.assertEqual(colors, {"#00FF00", "#FF0000", "#FFFF00"})
        self.assertEqual(fills, {True, False})
        self.assertEqual(counts, {1, 2, 3})

    def test_generation_replay_idempotency_and_tamper_detection(self):
        generator = self.generator
        first = generator.generate_question("Ana01", 20261008)
        generator.write_index()
        self.assertEqual(len({r["operation"] for r in first}), 4)
        self.assertEqual(len({r["pixel_sha256"] for r in first}), 4)
        self.assertEqual(first, generator.generate_question("Ana01", 20261008))
        generator.check_question("Ana01", redraw_pixels=True)
        generator.check_index()
        output = redraw(self.root, "Ana01", "base_1")
        self.assertEqual(pixel_hash(output), first[0]["pixel_sha256"])
        with self.assertRaises(ValueError):
            redraw(self.root, "Ana01", "base_1", self.root / first[0]["image_path"])
        second = generator.generate_question("Ana01", 20261008, replace=True)
        self.assertEqual([r["pixel_sha256"] for r in first], [r["pixel_sha256"] for r in second])
        self.assertEqual(len(list((self.root / "archive/base_variant").iterdir())), 1)
        generator.write_index()
        plugin_path = self.root / second[0]["plugin_path"]
        plugin_path.write_bytes(plugin_path.read_bytes() + b" ")
        with self.assertRaisesRegex(ValueError, "hash mismatch"):
            generator.check_question("Ana01")

    def test_new_question_registers_without_invalidating_previous_base_and_enters_special(self):
        self.generator.generate_question("Ana01", 20261008)
        self.generator.write_index()
        previous = (self.root / "base_variant/Ana01/recipes.json").read_bytes()
        workbench_root = ROOT.parent / "fine_grained_special_workbench"
        sys.path.insert(0, str(workbench_root))
        from workbench_io import load_config
        from review_store import Workbench
        config = load_config(workbench_root / "config.json")
        for key, value in {
            "dataset_root": self.root, "dataset_file": self.root / "dataset.jsonl",
            "original_image_dir": self.root / "image", "common_renderer_file": self.root / "dataset_generator/common_renderer.py",
            "protocol_file": self.root / "dataset_generator/protocol.json",
            "question_class_dir": self.root / "dataset_generator/dataset_generator",
            "runtime_dir": self.temporary_path / "runtime", "output_dir": self.root / "special_variant",
        }.items():
            config[key] = str(value)
        workbench = Workbench(config)
        try:
            self.assertEqual(workbench.active_questions(), ["Ana01"])
        finally:
            workbench.close()
        source = (ROOT / "dataset_generator/dataset_generator/function_plot20.py").read_text(encoding="utf-8")
        (self.root / "dataset_generator/dataset_generator/function_plot02.py").write_text(
            source.replace("Ana20", "Ana02").replace("custom_20", "custom_02"), encoding="utf-8")
        prepare(self.root, ["Ana02"])
        self.assertEqual(previous, (self.root / "base_variant/Ana01/recipes.json").read_bytes())
        generator = BaseGenerator(self.root)
        generator.check_question("Ana01", redraw_pixels=True)
        generator.check_question("Ana02", redraw_pixels=True)
        generator.check_index()
        self.assertIn("Ana02", pending_special(self.root))
        workbench = Workbench(config)
        try:
            self.assertEqual(workbench.active_questions(), ["Ana01", "Ana02"])
            self.assertEqual(workbench.progress["questions"]["Ana02"]["accepted"], [])
            self.assertFalse(workbench.progress["questions"]["Ana02"]["collected"])
        finally:
            workbench.close()
            sys.path.remove(str(workbench_root))

    def test_changed_original_input_is_rejected(self):
        self.generator.generate_question("Ana01", 20261008)
        path = self.root / "dataset_generator/dataset_generator/function_plot01.py"
        path.write_bytes(path.read_bytes() + b"\n# input changed\n")
        with self.assertRaisesRegex(ValueError, "Original input changed"):
            BaseGenerator(self.root).check_question("Ana01")


if __name__ == "__main__":
    unittest.main(verbosity=2)
