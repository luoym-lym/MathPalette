"""Generic A/B sampling, fixed-parameter rendering, and standalone redraw CLI."""

from __future__ import annotations

import argparse
import itertools
import json
import math
import random
from pathlib import Path

import numpy as np
from matplotlib.patches import Ellipse, Polygon

from renderer_adapter import RENDER_LOCK, RendererAdapter, new_segment, scene_png
from workbench_io import (GENERATOR_VERSION, ROOT, WorkbenchError, atomic_write,
                          canonical_hash, environment_versions, load_config, read_json)

OPERATIONS = {
    "A1": "修改背景网格", "A2": "隐藏全部刻度数字", "A3": "添加独立形状", "A4": "修改背景颜色",
    "B1": "添加游离点", "B2": "随机添加线", "B3": "连接原有点与原点",
    "B4": "向坐标轴添加投影", "B5": "在原曲线上添加整数点",
}
GROUPS = {"A": ["A1", "A2", "A3", "A4"], "B": ["B1", "B2", "B3", "B4", "B5"]}
FINITE = {"A1", "A2", "A4", "B3", "B4", "B5"}


def parameter_key(operation, params):
    return canonical_hash({"operation": operation, "params": params})


def style(config, dashed=False):
    return {"color": config["color"], "linewidth_pt": config["linewidth_pt"],
            "linestyle": "dashed" if dashed else "solid",
            "dash_pattern_pt": list(config["dash_pattern_pt"]) if dashed else []}


class VariantGenerator:
    def __init__(self, config=None, adapter=None, metadata=None):
        self.config = config or load_config()
        self.adapter = adapter or RendererAdapter(self.config["source_dir"], tolerance=self.config["integer_tolerance"])
        self.metadata = metadata if metadata is not None else {}

    def info(self, qid):
        if qid not in self.metadata:
            self.metadata[qid] = self.adapter.inspect_question(qid)
        return self.metadata[qid]

    def point(self, xy, filled=True, **extra):
        return {"xy": list(xy), "filled": filled, "size_pt2": self.config["point_size_pt2"],
                "color": self.config["color"], **extra}

    def finite_params(self, qid, operation):
        if operation == "A1":
            for mode in ("off", "half_density"):
                yield {"mode": mode, "grid_positions": [] if mode == "off" else list(range(-8, 9, 2))}
        elif operation == "A2":
            yield {"hidden": ["x_tick_labels", "y_tick_labels", "origin_zero"]}
        elif operation == "A4":
            for color in self.config["background_colors"]:
                yield {"background_color": color}
        elif operation in ("B3", "B4"):
            for source in self.info(qid)["b3_sources" if operation == "B3" else "b4_sources"]:
                yield {**source, **style(self.config, dashed=True)}
        elif operation == "B5":
            # Collapse shared intersection coordinates across curves: one point
            # on two curves still makes only one visible marker.
            unique = {tuple(p["xy"]): p for p in reversed(self.info(qid)["b5_points"])}
            available = [unique[xy] for xy in sorted(unique)]
            for count in range(1, min(3, len(available)) + 1):
                for selected in itertools.combinations(available, count):
                    yield {"points": [self.point(p["xy"], curve_id=p["curve_id"],
                                                 verification=p["verification"], tolerance=p["tolerance"])
                                      for p in selected], **style(self.config)}

    def remaining_finite(self, qid, operation, tried):
        return any(parameter_key(operation, params) not in tried
                   for params in self.finite_params(qid, operation))

    def sample(self, qid, operation, rng, tried):
        if operation in FINITE:
            # Reservoir sampling selects uniformly without storing all point
            # combinations. Finite modes are always exhausted exactly.
            selected, count = None, 0
            for params in self.finite_params(qid, operation):
                if parameter_key(operation, params) in tried:
                    continue
                count += 1
                if rng.randrange(count) == 0:
                    selected = params
            return selected
        if operation == "A3":
            kind = rng.choice(["ellipse", "rectangle", "triangle"])
            center = [rng.uniform(*self.config["shape_center_range"]) for _ in range(2)]
            width, height = [rng.uniform(*self.config["shape_size_range"]) for _ in range(2)]
            angle = rng.uniform(0, 360)
            params = {"shape": kind, "center": center, "angle_deg": angle,
                      "width": width, "height": height, "fill": False, **style(self.config)}
            theta = math.radians(angle)
            rotation = np.array([[math.cos(theta), -math.sin(theta)], [math.sin(theta), math.cos(theta)]])
            if kind == "ellipse":
                params["width"], params["height"] = sorted([width, height], reverse=True)
                params["major_axis"] = params["width"]
                params["minor_axis"] = params["height"]
            else:
                local = [[-width / 2, -height / 2], [width / 2, -height / 2],
                         [width / 2, height / 2], [-width / 2, height / 2]]
                if kind == "triangle":
                    local = [local[0], local[1], [rng.uniform(-width / 3, width / 3), height / 2]]
                params["vertices"] = (np.array(local) @ rotation.T + center).tolist()
            return params
        if operation == "B1":
            points = self.info(qid)["original_points"]
            lo, hi = self.config["free_point_range"]
            options = [[x, y] for x in range(lo, hi + 1) for y in range(lo, hi + 1)
                       if not any(np.linalg.norm(np.array(p["xy"]) - [x, y]) <= self.config["integer_tolerance"] for p in points)]
            if not options:
                return None
            count = rng.randint(1, min(3, len(options)))
            selected = sorted(rng.sample(options, count))
            return {"points": [self.point(xy, filled=rng.choice([True, False])) for xy in selected], **style(self.config)}
        if operation == "B2":
            kind = rng.choice(["horizontal", "vertical", "oblique"])
            if kind == "horizontal":
                value = rng.uniform(-7, 7)
                endpoints = [[-8.0, value], [8.0, value]]
            elif kind == "vertical":
                value = rng.uniform(-7, 7)
                endpoints = [[value, -8.0], [value, 8.0]]
            else:
                slope = rng.choice([-1, 1]) * rng.uniform(0.15, 3)
                intercept = rng.uniform(-6, 6)
                candidates = []
                for x in (-8.0, 8.0):
                    y = slope * x + intercept
                    if -8 <= y <= 8:
                        candidates.append([x, y])
                for y in (-8.0, 8.0):
                    x = (y - intercept) / slope
                    if -8 <= x <= 8 and [x, y] not in candidates:
                        candidates.append([x, y])
                if len(candidates) < 2:
                    return None
                endpoints = [candidates[0], candidates[-1]]
            return {"orientation": kind, "endpoints": endpoints, **style(self.config, rng.choice([True, False]))}
        raise WorkbenchError(f"未知操作：{operation}")

    def validate(self, qid, operation, params, scene):
        if operation not in OPERATIONS:
            raise WorkbenchError("只支持 A1～A4、B1～B5。")
        if operation == "A1":
            expected = [] if params.get("mode") == "off" else list(range(-8, 9, 2))
            if params.get("mode") not in ("off", "half_density") or params.get("grid_positions") != expected:
                raise WorkbenchError("A1 网格模式或实际网格位置无效。")
        if operation == "A2" and params.get("hidden") != ["x_tick_labels", "y_tick_labels", "origin_zero"]:
            raise WorkbenchError("A2 只能隐藏轴刻度数字和独立原点 0。")
        if operation == "A3":
            if params["shape"] not in ("ellipse", "rectangle", "triangle") or params["fill"]:
                raise WorkbenchError("A3 形状必须为无填充椭圆、矩形或三角形。")
            if params["shape"] == "ellipse":
                theta = math.radians(params["angle_deg"])
                a, b = params["width"] / 2, params["height"] / 2
                bounds = [math.sqrt((a * math.cos(theta)) ** 2 + (b * math.sin(theta)) ** 2),
                          math.sqrt((a * math.sin(theta)) ** 2 + (b * math.cos(theta)) ** 2)]
                if min(a, b) <= 0 or any(abs(c) + d > 8 for c, d in zip(params["center"], bounds)):
                    raise WorkbenchError("椭圆尺寸无效或超出视窗。")
            else:
                vertices = np.array(params["vertices"])
                if vertices.shape != (3 if params["shape"] == "triangle" else 4, 2) or np.max(abs(vertices)) > 8:
                    raise WorkbenchError("多边形顶点无效或超出视窗。")
                x, y = vertices.T
                area = abs(float(x @ np.roll(y, 1) - y @ np.roll(x, 1))) / 2
                if area <= 1e-8:
                    raise WorkbenchError("不能绘制退化多边形。")
        if operation == "A4" and params.get("background_color") not in self.config["background_colors"]:
            raise WorkbenchError("A4 必须使用配置中的两种浅色背景。")
        if operation in ("B1", "B5"):
            points = params["points"]
            coordinates = [tuple(p["xy"]) for p in points]
            if not 1 <= len(points) <= 3 or len(set(coordinates)) != len(points):
                raise WorkbenchError("新增点须为 1～3 个不同位置。")
            for point in points:
                xy = point["xy"]
                if not all(float(v).is_integer() and -8 <= v <= 8 for v in xy):
                    raise WorkbenchError("B1/B5 两个坐标均须为视窗内整数。")
                if operation == "B1" and any(np.linalg.norm(np.array(p["xy"]) - xy) <= 1e-8 for p in scene.points):
                    raise WorkbenchError("B1 不能与原有点完全重合。")
                if operation == "B5" and not any(p["xy"] == xy and p["curve_id"] == point["curve_id"]
                                                   for p in self.info(qid)["b5_points"]):
                    raise WorkbenchError("B5 点没有通过对应原曲线的数学验证。")
        if operation in ("B2", "B3", "B4"):
            if not new_segment(scene, params["endpoints"]):
                raise WorkbenchError("新增线退化、与坐标轴或原有线条完全重合。")
            if operation in ("B3", "B4"):
                options = self.info(qid)["b3_sources" if operation == "B3" else "b4_sources"]
                if not any(all(params.get(key) == value for key, value in option.items()) for option in options):
                    raise WorkbenchError("起点来源或投影方向没有通过原场景验证。")

    def render(self, qid, operation, params):
        """No RNG is used anywhere on the rendering path."""
        with RENDER_LOCK:
            self.adapter.assert_baseline()
            scene = self.adapter.scene(qid)
            try:
                self.validate(qid, operation, params, scene)
                ax, background = scene.ax, "#FFFFFF"
                if operation == "A1":
                    positions = params["grid_positions"]
                    for axis in (ax.xaxis, ax.yaxis):
                        for tick, location in zip(axis.get_major_ticks(), axis.get_majorticklocs()):
                            tick.gridline.set_visible(location in positions)
                elif operation == "A2":
                    ax.tick_params(axis="both", labelbottom=False, labeltop=False, labelleft=False, labelright=False)
                    ax._mp_origin_zero.set_visible(False)
                elif operation == "A3":
                    kwargs = {"fill": False, "edgecolor": params["color"], "linewidth": params["linewidth_pt"],
                              "linestyle": "-", "zorder": 3, "gid": "variant_addition"}
                    if params["shape"] == "ellipse":
                        patch = Ellipse(params["center"], params["width"], params["height"], angle=params["angle_deg"], **kwargs)
                    else:
                        patch = Polygon(params["vertices"], closed=True, **kwargs)
                    ax.add_patch(patch)
                elif operation == "A4":
                    background = params["background_color"]
                    scene.fig.patch.set_facecolor(background)
                    ax.set_facecolor(background)
                    for text in [*ax.get_xticklabels(), *ax.get_yticklabels(), ax._mp_origin_zero]:
                        if text.get_bbox_patch() is not None:
                            text.get_bbox_patch().set_facecolor(background)
                elif operation in ("B1", "B5"):
                    for point in params["points"]:
                        x, y = point["xy"]
                        ax.scatter([x], [y], s=point["size_pt2"], marker="o",
                                   facecolors=point["color"] if point["filled"] else background,
                                   edgecolors=point["color"], linewidths=params["linewidth_pt"],
                                   zorder=4, gid="variant_addition")
                elif operation in ("B2", "B3", "B4"):
                    endpoints = np.asarray(params["endpoints"])
                    line_style = "-" if params["linestyle"] == "solid" else (0, tuple(params["dash_pattern_pt"]))
                    ax.plot(endpoints[:, 0], endpoints[:, 1], color=params["color"],
                            linewidth=params["linewidth_pt"], linestyle=line_style,
                            zorder=3, solid_capstyle="butt", gid="variant_addition")
                # Do not call original finalize/lock_view here: it would restore
                # the labels and white background after A2/A4.
                return scene_png(scene, background)
            finally:
                scene.close()


_DEFAULT_GENERATOR = None


def render_recipe(recipe, output_path=None):
    """Public entry used by every generated draw_Axx/draw_Bxx function."""
    global _DEFAULT_GENERATOR
    if recipe["status"] != "passed" or recipe["generator_version"] != GENERATOR_VERSION:
        raise WorkbenchError("重绘只接受当前生成器版本的人工通过方案。")
    if recipe["environment"] != environment_versions():
        raise WorkbenchError("依赖版本与通过时不同，请按 requirements.txt 恢复原环境后重绘。")
    if _DEFAULT_GENERATOR is None:
        config = load_config()
        manifest = read_json(ROOT / "state" / "baseline_manifest.json")
        _DEFAULT_GENERATOR = VariantGenerator(config, RendererAdapter(config["source_dir"], manifest, config["integer_tolerance"]))
    generator = _DEFAULT_GENERATOR
    if recipe["baseline_fingerprint"] != generator.adapter.manifest["fingerprint"]:
        raise WorkbenchError("重绘方案与当前已审核基线不一致。")
    destination = Path(output_path or ROOT / "reproduced" / recipe["question_id"] / f"{recipe['slot_id']}.png").resolve()
    if destination.is_relative_to(generator.adapter.source) or destination.is_relative_to(ROOT / "accepted"):
        raise WorkbenchError("重绘输出不得覆盖原始输入或人工通过图。")
    data, digest = generator.render(recipe["question_id"], recipe["operation"], recipe["params"])
    if digest != recipe["pixel_sha256"]:
        raise WorkbenchError("重绘像素与通过图不一致，未写入输出文件。", 409)
    atomic_write(destination, data)
    return destination


def main():
    parser = argparse.ArgumentParser(description="生成未审核候选，或按冻结参数确定性重绘。不会自动 Pass。")
    sub = parser.add_subparsers(dest="command", required=True)
    candidate = sub.add_parser("candidate")
    candidate.add_argument("question_id")
    candidate.add_argument("operation", choices=OPERATIONS)
    candidate.add_argument("--seed", type=int, default=None)
    candidate.add_argument("--output", required=True, type=Path)
    redraw = sub.add_parser("redraw")
    redraw.add_argument("recipes", type=Path)
    redraw.add_argument("slot_id")
    redraw.add_argument("--output", type=Path)
    args = parser.parse_args()
    if args.command == "redraw":
        recipes = read_json(args.recipes)
        recipe = next((r for r in recipes if r["slot_id"] == args.slot_id), None)
        if recipe is None:
            raise WorkbenchError("该槽位没有人工通过的方案。")
        print(render_recipe(recipe, args.output))
    else:
        import secrets
        import uuid
        config = load_config()
        manifest_path = ROOT / "state" / "baseline_manifest.json"
        adapter = RendererAdapter(config["source_dir"], read_json(manifest_path) if manifest_path.exists() else None)
        generator = VariantGenerator(config, adapter)
        if args.question_id not in adapter.records:
            raise WorkbenchError("不存在此题号。")
        if generator.info(args.question_id)["operations"][args.operation]["status"] != "available":
            raise WorkbenchError(generator.info(args.question_id)["operations"][args.operation]["reason"])
        output = args.output.resolve()
        if output.is_relative_to(adapter.source) or output.is_relative_to(ROOT / "accepted"):
            raise WorkbenchError("候选不得写入原始输入或正式通过目录。")
        seed = args.seed if args.seed is not None else secrets.randbits(63)
        rng = random.Random(seed)
        params = generator.sample(args.question_id, args.operation, rng, set())
        if params is None:
            raise WorkbenchError("没有可构造的合法参数。")
        data, digest = generator.render(args.question_id, args.operation, params)
        if digest == generator.info(args.question_id)["original_pixel_sha256"]:
            raise WorkbenchError("候选与原图像素相同。")
        atomic_write(output, data)
        from workbench_io import atomic_json
        atomic_json(output.with_suffix(".json"), {"question_id": args.question_id, "operation": args.operation,
                    "seed": seed, "params": params, "candidate_id": uuid.uuid4().hex,
                    "pixel_sha256": digest, "status": "unreviewed", "generator_version": GENERATOR_VERSION,
                    "baseline_fingerprint": adapter.manifest["fingerprint"], "environment": environment_versions()})
        print(output)


if __name__ == "__main__":
    try:
        main()
    except WorkbenchError as error:
        raise SystemExit(str(error))
