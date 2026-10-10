"""Sample four distinct Base operations per question and replay frozen plugins.

python -B Analytics/dataset_generator/generate_base_variants.py generate
python -B Analytics/dataset_generator/generate_base_variants.py check --redraw
"""
from __future__ import annotations

import argparse
import copy
import json
import math
import random
import sys
import tempfile
import uuid
from pathlib import Path

import numpy as np
from matplotlib.patches import Ellipse, Polygon

from base_support import (
    ROOT, Dataset, atomic_write, canonical_hash, dataset_lock, digest, environment,
    inside, json_bytes, now, pixel_hash, png_bytes, question_id, read_json,
)

GENERATOR_VERSION = "Base-2.0.0"
OPERATIONS = tuple(f"Base{i}" for i in range(1, 7))
SLOTS = tuple(f"base_{i}" for i in range(1, 5))
PLUGIN_FIELDS = ("plugin_schema_version", "protocol_version", "question_id", "category", "operation", "params")


def stable_seed(master_seed, qid, purpose):
    # A 52-bit integer round-trips through JavaScript JSON without precision loss.
    return int(canonical_hash([master_seed, qid, purpose])[:13], 16)


def line_endpoints(anchor, direction, view):
    """Clip the infinite line through an in-view anchor to the square viewport."""
    low, high = view
    intervals = []
    for coordinate, component in zip(anchor, direction):
        if abs(component) > 1e-12:
            intervals.append(sorted(((low - coordinate) / component, (high - coordinate) / component)))
    begin = max(pair[0] for pair in intervals)
    end = min(pair[1] for pair in intervals)
    return [[float(np.clip(anchor[i] + t * direction[i], low, high)) for i in range(2)]
            for t in (begin, end)]


def sample_params(operation, rng, policy):
    config = policy["operations"][operation]
    if operation == "Base1":
        mode = rng.choice(config["modes"])
        return {"mode": mode, "grid_positions": [] if mode == "off" else list(range(-8, 9, 2))}
    if operation == "Base2":
        return copy.deepcopy(config)
    if operation == "Base3":
        return copy.deepcopy(config)
    if operation == "Base4":
        orientation = rng.choice(config["orientations"])
        anchor = [rng.uniform(*policy["view"]) for _ in range(2)]
        if orientation == "horizontal":
            direction, angle = [1.0, 0.0], 0.0
        elif orientation == "vertical":
            direction, angle = [0.0, 1.0], 90.0
        else:
            angle = rng.uniform(*config["oblique_angle_deg"]) * rng.choice([-1, 1])
            radians = math.radians(angle)
            direction = [math.cos(radians), math.sin(radians)]
        return {"orientation": orientation, "anchor": anchor, "angle_deg": angle,
                "endpoints": line_endpoints(anchor, direction, policy["view"]),
                "color": rng.choice(config["colors"]), "linestyle": "dashed",
                "linewidth_pt": config["linewidth_pt"], "dash_pattern_pt": config["dash_pattern_pt"]}
    if operation == "Base5":
        shape = rng.choice(config["shapes"])
        center = [rng.uniform(*config["center_range"]) for _ in range(2)]
        width, height = rng.uniform(*config["width_range"]), rng.uniform(*config["height_range"])
        angle = rng.uniform(*config["angle_range_deg"])
        params = {"shape": shape, "center": center, "width": width, "height": height,
                  "angle_deg": angle, "color": config["color"], "linewidth_pt": config["linewidth_pt"],
                  "linestyle": "solid", "fill": False}
        if shape != "ellipse":
            local = [[-width / 2, -height / 2], [width / 2, -height / 2]]
            if shape == "rectangle":
                local += [[width / 2, height / 2], [-width / 2, height / 2]]
            else:
                local += [[rng.uniform(-width / 3, width / 3), height / 2]]
            theta = math.radians(angle)
            rotation = np.array([[math.cos(theta), -math.sin(theta)], [math.sin(theta), math.cos(theta)]])
            params["vertices"] = (np.asarray(local) @ rotation.T + center).tolist()
        return params
    if operation == "Base6":
        low, high = config["integer_range"]
        positions = [(x, y) for x in range(low, high + 1) for y in range(low, high + 1)]
        points = [{"xy": list(xy), "filled": rng.choice(config["filled_choices"]),
                   "size_pt2": config["size_pt2"], "color": config["color"],
                   "open_facecolor": config["open_facecolor"], "edge_linewidth_pt": config["edge_linewidth_pt"]}
                  for xy in rng.sample(positions, rng.randint(*config["count_range"]))]
        return {"points": points}
    raise ValueError(f"Unknown operation: {operation}")


def make_plugin(qid, operation, seed, policy):
    return {"plugin_schema_version": policy["plugin_schema_version"],
            "protocol_version": policy["protocol_version"], "question_id": qid,
            "category": "Base", "operation": operation,
            "params": sample_params(operation, random.Random(seed), policy)}


def apply_plugin(fig, plugin):
    """Pure replay: draw only the concrete values saved in the plugin; never sample."""
    operation, params = plugin["operation"], plugin["params"]
    ax, background = fig.axes[0], "#FFFFFF"
    if operation == "Base1":
        for axis in (ax.xaxis, ax.yaxis):
            for tick, position in zip(axis.get_major_ticks(), axis.get_majorticklocs()):
                tick.gridline.set_visible(position in params["grid_positions"])
    elif operation == "Base2":
        ax.tick_params(axis="both", labelbottom=False, labeltop=False, labelleft=False, labelright=False)
        ax._mp_origin_zero.set_visible(False)
    elif operation == "Base3":
        background = params["background_color"]
        fig.patch.set_facecolor(background)
        ax.set_facecolor(background)
        for label in [*ax.get_xticklabels(), *ax.get_yticklabels(), ax._mp_origin_zero]:
            if label.get_bbox_patch() is not None:
                label.get_bbox_patch().set_facecolor(background)
    elif operation == "Base4":
        endpoints = np.asarray(params["endpoints"])
        ax.plot(endpoints[:, 0], endpoints[:, 1], color=params["color"],
                linewidth=params["linewidth_pt"], linestyle=(0, tuple(params["dash_pattern_pt"])),
                solid_capstyle="butt", zorder=3, gid="base_addition")
    elif operation == "Base5":
        style = {"fill": False, "edgecolor": params["color"], "linewidth": params["linewidth_pt"],
                 "linestyle": "-", "zorder": 3, "gid": "base_addition"}
        if params["shape"] == "ellipse":
            patch = Ellipse(params["center"], params["width"], params["height"], angle=params["angle_deg"], **style)
        else:
            patch = Polygon(params["vertices"], closed=True, **style)
        ax.add_patch(patch)
    elif operation == "Base6":
        for point in params["points"]:
            ax.scatter(*point["xy"], s=point["size_pt2"], marker="o",
                       facecolors=point["color"] if point["filled"] else point["open_facecolor"],
                       edgecolors=point["color"], linewidths=point["edge_linewidth_pt"],
                       zorder=4, gid="base_addition")
    else:
        raise ValueError(f"Unsupported Base operation: {operation}")
    return background


def drawing_functions():
    return '''"""Replay the four frozen Base plugins for this question."""
import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "dataset_generator"))
from generate_base_variants import redraw

def _draw(slot, output_path=None):
    return redraw(ROOT, Path(__file__).resolve().parent.name, slot, output_path)

def draw_base_1(output_path=None):
    return _draw("base_1", output_path)

def draw_base_2(output_path=None):
    return _draw("base_2", output_path)

def draw_base_3(output_path=None):
    return _draw("base_3", output_path)

def draw_base_4(output_path=None):
    return _draw("base_4", output_path)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("slot_id", choices=["base_1", "base_2", "base_3", "base_4"])
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    print(_draw(args.slot_id, args.output))
'''


class BaseGenerator:
    def __init__(self, root=ROOT):
        self.dataset = Dataset(root)
        self.root = self.dataset.root
        self.policy_path = inside(self.root, "dataset_generator/base_protocol.json")
        self.policy = read_json(self.policy_path)
        if self.policy["protocol_version"] != "2.0.0" or self.policy["variants_per_question"] != 4:
            raise ValueError("Unsupported Base protocol version or variant count.")
        self.policy_hash = canonical_hash(self.policy)
        self.execution_hash = canonical_hash({name: digest(Path(__file__).with_name(name).read_bytes())
                                             for name in ("generate_base_variants.py", "base_support.py")})
        self.env = environment()

    def render(self, plugin):
        if set(plugin) != set(PLUGIN_FIELDS) or plugin["category"] != "Base" or plugin["operation"] not in OPERATIONS:
            raise ValueError("Invalid Base plugin schema.")
        if (plugin["protocol_version"] != self.policy["protocol_version"] or
                plugin["plugin_schema_version"] != self.policy["plugin_schema_version"]):
            raise ValueError("Plugin version mismatch.")
        question_id(plugin["question_id"])
        json_bytes(plugin)
        with self.dataset.scene(plugin["question_id"]) as fig:
            background = apply_plugin(fig, plugin)
            return png_bytes(fig, background)

    def check_question(self, qid, redraw_pixels=False):
        folder = inside(self.root, f"base_variant/{question_id(qid)}")
        recipes = read_json(folder / "recipes.json")
        if not isinstance(recipes, list) or len(recipes) != 4 or [r["slot_id"] for r in recipes] != list(SLOTS):
            raise ValueError(f"Expected four ordered base_1..base_4 recipes: {qid}")
        operations = [r["operation"] for r in recipes]
        if len(set(operations)) != 4 or any(op not in OPERATIONS for op in operations):
            raise ValueError(f"Expected four distinct Base operations: {qid}")
        expected_images, expected_plugins, pixels = set(), set(), set()
        baseline_hash = canonical_hash(self.dataset.baseline(qid))
        for index, recipe in enumerate(recipes, 1):
            if recipe["question_id"] != qid or recipe["status"] != "generated" or recipe["category"] != "Base":
                raise ValueError(f"Invalid generated recipe: {qid}")
            if (recipe["baseline_fingerprint"] != baseline_hash or
                    canonical_hash(recipe["baseline"]) != baseline_hash):
                raise ValueError(f"Original input changed: {qid}; regenerate explicitly with --replace.")
            if (recipe["protocol_sha256"] != self.policy_hash or recipe["environment"] != self.env or
                    recipe["generator_version"] != GENERATOR_VERSION or recipe["renderer_sha256"] != self.execution_hash):
                raise ValueError(f"Base protocol, renderer, or environment changed: {qid}.")
            name = f"{qid}_base_variant_{index}"
            expected_image = f"base_variant/{qid}/images/{name}.png"
            expected_plugin = f"base_variant/{qid}/plugins/{name}.json"
            if recipe["image_path"] != expected_image or recipe["plugin_path"] != expected_plugin:
                raise ValueError(f"Invalid artifact paths: {qid}/{index}")
            image_path, plugin_path = inside(self.root, expected_image), inside(self.root, expected_plugin)
            plugin_data, image_data = plugin_path.read_bytes(), image_path.read_bytes()
            plugin = read_json(plugin_path)
            if plugin != {key: recipe[key] for key in PLUGIN_FIELDS}:
                raise ValueError(f"Recipe/plugin mismatch: {qid}/{index}")
            if (digest(plugin_data) != recipe["plugin_sha256"] or canonical_hash(plugin) != recipe["parameter_key"] or
                    digest(image_data) != recipe["png_sha256"] or pixel_hash(image_data) != recipe["pixel_sha256"]):
                raise ValueError(f"Artifact hash mismatch: {qid}/{index}")
            if redraw_pixels and pixel_hash(self.render(plugin)) != recipe["pixel_sha256"]:
                raise ValueError(f"Frozen plugin redraw mismatch: {qid}/{index}")
            expected_images.add(image_path.name)
            expected_plugins.add(plugin_path.name)
            pixels.add(recipe["pixel_sha256"])
        if (set(p.name for p in (folder / "images").iterdir()) != expected_images or
                set(p.name for p in (folder / "plugins").iterdir()) != expected_plugins or len(pixels) != 4):
            raise ValueError(f"Extra/missing/duplicate Base artifacts: {qid}")
        if (folder / "draw_variants.py").read_text(encoding="utf-8") != drawing_functions():
            raise ValueError(f"Base redraw entry points changed: {qid}")
        return recipes

    def generate_question(self, qid, master_seed, replace=False):
        question_id(qid)
        if qid not in self.dataset.records:
            raise ValueError(f"Register this question in dataset.jsonl first: {qid}")
        target = inside(self.root, f"base_variant/{qid}")
        if target.exists() and not replace:
            recipes = self.check_question(qid)
            if any(r["master_seed"] != master_seed for r in recipes):
                raise ValueError(f"Different seed requested for existing {qid}; use --replace to archive and regenerate.")
            print(f"{qid}: existing four Base variants verified; skipped", flush=True)
            return recipes
        original = self.dataset.verify_original(qid)
        baseline = self.dataset.baseline(qid)
        selection_seed = stable_seed(master_seed, qid, "operation_selection")
        operations = random.Random(selection_seed).sample(list(OPERATIONS), 4)
        used_pixels = {pixel_hash(original)}
        recipes, artifacts = [], {}
        for index, operation in enumerate(operations, 1):
            for attempt in range(32):
                seed = stable_seed(master_seed, qid, f"{operation}:{attempt}")
                plugin = make_plugin(qid, operation, seed, self.policy)
                data = self.render(plugin)
                pixels = pixel_hash(data)
                if pixels not in used_pixels:
                    break
                if operation in ("Base2", "Base3"):
                    raise ValueError(f"{qid}/{operation} has no visible effect; original protocol mismatch.")
            else:
                raise ValueError(f"Unable to make a visibly distinct {operation}: {qid}")
            used_pixels.add(pixels)
            name = f"{qid}_base_variant_{index}"
            plugin_data = json_bytes(plugin)
            recipe = {**plugin, "slot_id": f"base_{index}", "candidate_id": uuid.uuid4().hex,
                      "master_seed": master_seed, "selection_seed": selection_seed, "seed": seed,
                      "sampling_attempt": attempt, "selection": "uniform_without_replacement",
                      "parameter_key": canonical_hash(plugin), "pixel_sha256": pixels,
                      "png_sha256": digest(data), "plugin_sha256": digest(plugin_data),
                      "generator_version": GENERATOR_VERSION, "environment": self.env,
                      "baseline": baseline, "baseline_fingerprint": canonical_hash(baseline),
                      "protocol_sha256": self.policy_hash, "renderer_sha256": self.execution_hash,
                      "created_at": now(), "status": "generated", "review_mode": "automatic",
                      "image_path": f"base_variant/{qid}/images/{name}.png",
                      "plugin_path": f"base_variant/{qid}/plugins/{name}.json"}
            recipes.append(recipe)
            artifacts[f"images/{name}.png"] = data
            artifacts[f"plugins/{name}.json"] = plugin_data
        artifacts["recipes.json"] = json_bytes(recipes)
        artifacts["draw_variants.py"] = drawing_functions().encode("utf-8")
        # Build the complete four-image package before replacing any existing folder.
        stage_root = inside(self.root, ".base_staging")
        stage_root.mkdir(exist_ok=True)
        stage = Path(tempfile.mkdtemp(prefix=qid + "_", dir=stage_root)).resolve()
        for relative, data in artifacts.items():
            atomic_write(inside(stage, relative), data)
        if canonical_hash(self.dataset.baseline(qid)) != canonical_hash(baseline):
            raise ValueError(f"Original input changed during generation: {qid}")
        archive = None
        if target.exists():
            # Both resolved targets are inside the dataset before moving a directory.
            archive = inside(self.root, f"archive/base_variant/{qid}_{now().replace(':', '').replace('+', '_')}_{uuid.uuid4().hex[:8]}")
            archive.parent.mkdir(parents=True, exist_ok=True)
            target.rename(archive)
        try:
            target.parent.mkdir(parents=True, exist_ok=True)
            stage.rename(target)
        except BaseException:
            if archive is not None and not target.exists():
                archive.rename(target)
            raise
        print(f"{qid}: generated four variants ({', '.join(operations)})" +
              (f"; previous package archived at {archive.relative_to(self.root)}" if archive else ""), flush=True)
        return recipes

    def write_index(self):
        rows = []
        for qid in self.dataset.records:
            path = inside(self.root, f"base_variant/{qid}/recipes.json")
            if not path.exists():
                continue
            recipes = read_json(path)
            # During migration, old A/B packages remain outside the new index.
            if isinstance(recipes, list) and recipes and recipes[0].get("category") == "Base":
                rows.extend(self.check_question(qid))
        destination = inside(self.root, "base_variant/generated_index.jsonl")
        atomic_write(destination, "".join(json.dumps(row, ensure_ascii=False, allow_nan=False) + "\n" for row in rows))
        return len(rows)

    def check_index(self):
        expected = []
        for qid in self.dataset.records:
            path = inside(self.root, f"base_variant/{qid}/recipes.json")
            if path.exists():
                rows = read_json(path)
                if rows and rows[0].get("category") == "Base":
                    expected.extend(rows)
        path = inside(self.root, "base_variant/generated_index.jsonl")
        actual = [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]
        if actual != expected:
            raise ValueError("generated_index.jsonl differs from per-question recipes; run generate to rebuild it.")


def redraw(root, qid, slot_id, output_path=None):
    if slot_id not in SLOTS:
        raise ValueError("Slot must be base_1..base_4.")
    generator = BaseGenerator(root)
    recipes = generator.check_question(qid)
    recipe = next(row for row in recipes if row["slot_id"] == slot_id)
    data = generator.render({key: recipe[key] for key in PLUGIN_FIELDS})
    if pixel_hash(data) != recipe["pixel_sha256"]:
        raise ValueError("Frozen plugin does not reproduce the saved image.")
    destination = Path(output_path).resolve() if output_path else (
        generator.root / "reproduced/base_variant" / qid / Path(recipe["image_path"]).name)
    if destination.suffix.lower() != ".png":
        raise ValueError("Redraw output must end in .png.")
    if destination.is_relative_to(generator.root) and not destination.is_relative_to(generator.root / "reproduced"):
        raise ValueError("Use reproduced/ or an external PNG path; do not overwrite formal dataset artifacts.")
    atomic_write(destination, data)
    return destination


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    for name in ("generate", "check"):
        child = commands.add_parser(name)
        child.add_argument("questions", nargs="*", help="Default: every dataset question.")
        child.add_argument("--dataset-root", type=Path, default=ROOT)
        if name == "generate":
            child.add_argument("--seed", type=int, default=20261008)
            child.add_argument("--replace", action="store_true", help="Archive existing packages, then regenerate.")
        else:
            child.add_argument("--redraw", action="store_true", help="Also replay all frozen plugins and compare pixels.")
    child = commands.add_parser("redraw")
    child.add_argument("question_id")
    child.add_argument("slot_id", choices=SLOTS)
    child.add_argument("--dataset-root", type=Path, default=ROOT)
    child.add_argument("--output", type=Path)
    args = parser.parse_args()
    if args.command == "redraw":
        print(redraw(args.dataset_root, args.question_id, args.slot_id, args.output))
        return
    if args.command == "generate" and not 0 <= args.seed < 2**53:
        parser.error("--seed must be an integer in [0, 2**53).")
    with dataset_lock(args.dataset_root):
        generator = BaseGenerator(args.dataset_root)
        qids = args.questions or list(generator.dataset.records)
        for qid in qids:
            if args.command == "generate":
                generator.generate_question(qid, args.seed, args.replace)
            else:
                generator.check_question(qid, args.redraw)
                print(f"{qid}: four Base artifacts verified" + ("; redraw pixels match" if args.redraw else ""), flush=True)
        if args.command == "generate":
            print(f"Index: {generator.write_index()} variants")
        else:
            generator.check_index()
            print("Global Base index matches per-question recipes")


if __name__ == "__main__":
    try:
        main()
    except (ValueError, OSError, KeyError) as error:
        print(str(error), file=sys.stderr)
        raise SystemExit(1)
