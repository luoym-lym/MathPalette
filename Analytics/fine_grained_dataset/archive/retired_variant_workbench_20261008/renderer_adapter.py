"""Load the frozen scene without ever running its original save entry point.

The four source modules are private instances. Their finalize binding is changed
only while one draw runs, under RENDER_LOCK, and restored in a finally block.
Integer verification replays the *same* draw arithmetic at integer arguments;
it never interpolates a raster or rounds a nearby curve sample onto a grid.
"""

from __future__ import annotations

import ast
import importlib.util
import inspect
import io
import json
import sys
import textwrap
import threading
from contextlib import contextmanager
from dataclasses import dataclass
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.collections import LineCollection, PathCollection
from matplotlib.patches import Circle, Ellipse, Polygon
from PIL import Image

from workbench_io import WorkbenchError, canonical_hash, file_hash, pixel_hash, read_json

RENDER_LOCK = threading.RLock()


@contextmanager
def bindings(module, replacements):
    previous = {name: getattr(module, name) for name in replacements}
    try:
        for name, value in replacements.items():
            setattr(module, name, value)
        yield
    finally:
        for name, value in previous.items():
            setattr(module, name, value)


def manifest_for(source):
    files = {
        path.relative_to(source).as_posix(): file_hash(path)
        for path in sorted(source.rglob("*"))
        if path.is_file() and "__pycache__" not in path.parts and path.suffix != ".pyc"
    }
    return {"files": files, "fingerprint": canonical_hash(files)}


def visible(xy, tolerance=1e-8):
    return bool(np.isfinite(xy).all() and all(-8 - tolerance <= v <= 8 + tolerance for v in xy))


@dataclass
class Scene:
    fig: object
    ax: object
    points: list
    segments: list
    curves: list
    texts: list

    def close(self):
        plt.close(self.fig)


def scene_png(scene, background="#FFFFFF"):
    stream = io.BytesIO()
    scene.fig.savefig(stream, dpi=100, facecolor=background, transparent=False)
    data = stream.getvalue()
    with Image.open(io.BytesIO(data)) as image:
        if image.size != (768, 768) or image.convert("RGBA").getextrema()[3] != (255, 255):
            raise WorkbenchError("渲染输出必须为不透明的 768×768 PNG。")
        digest = pixel_hash(image)
    return data, digest


def new_segment(scene, endpoints, tolerance=1e-8):
    """Reject a stroke entirely covered by original straight geometry or axes."""
    start, end = np.asarray(endpoints, dtype=float)
    delta = end - start
    length2 = float(delta @ delta)
    if length2 <= tolerance ** 2:
        return False
    if (abs(start[0]) < tolerance and abs(end[0]) < tolerance) or (
        abs(start[1]) < tolerance and abs(end[1]) < tolerance
    ):
        return False
    intervals = []
    for a, b in scene.segments:
        a, b = np.asarray(a), np.asarray(b)
        cross_a = delta[0] * (a - start)[1] - delta[1] * (a - start)[0]
        cross_b = delta[0] * (b - start)[1] - delta[1] * (b - start)[0]
        if max(abs(cross_a), abs(cross_b)) > tolerance * max(1, np.sqrt(length2)):
            continue
        lo, hi = sorted([float((a - start) @ delta / length2), float((b - start) @ delta / length2)])
        if hi >= 0 and lo <= 1:
            intervals.append((max(0, lo), min(1, hi)))
    covered = 0.0
    for lo, hi in sorted(intervals):
        if lo > covered + tolerance:
            return True
        covered = max(covered, hi)
    return covered < 1 - tolerance


class RendererAdapter:
    def __init__(self, source_dir, expected_manifest=None, tolerance=1e-8):
        self.source = Path(source_dir).resolve()
        self.tolerance = tolerance
        self.manifest = manifest_for(self.source)
        if expected_manifest and self.manifest["files"] != expected_manifest["files"]:
            changed = sorted(set(self.manifest["files"]) | set(expected_manifest["files"]))
            changed = [p for p in changed if self.manifest["files"].get(p) != expected_manifest["files"].get(p)]
            raise WorkbenchError("已审核基线哈希发生变化：" + ", ".join(changed[:8]), 409)
        records = [json.loads(line) for line in
                   (self.source / "dataset.jsonl").read_text(encoding="utf-8").splitlines() if line.strip()]
        self.records = {record["id"]: record for record in records}
        if list(self.records) != [f"Ana{i:02d}" for i in range(1, 81)]:
            raise WorkbenchError("dataset.jsonl 必须恰有按顺序排列的 Ana01～Ana80。")
        self.questions = {}
        self.modules = {}
        self._load()

    def _load(self):
        with RENDER_LOCK:
            old_path = sys.path[:]
            old_module = sys.modules.get("common_renderer")
            old_bytecode = sys.dont_write_bytecode
            try:
                sys.dont_write_bytecode = True
                spec = importlib.util.spec_from_file_location("_variant_original_renderer", self.source / "common_renderer.py")
                self.renderer = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(self.renderer)
                sys.modules["common_renderer"] = self.renderer
                for path in sorted((self.source / "dataset_generator").glob("function_plot*.py")):
                    spec = importlib.util.spec_from_file_location("_variant_" + path.stem.replace("-", "_"), path)
                    module = importlib.util.module_from_spec(spec)
                    spec.loader.exec_module(module)
                    for qid in self.records:
                        cls = getattr(module, qid, None)
                        if cls:
                            if qid in self.questions:
                                raise WorkbenchError(f"重复的题目类：{qid}")
                            self.questions[qid] = cls()
                            self.modules[qid] = module
            finally:
                sys.path[:] = old_path
                sys.dont_write_bytecode = old_bytecode
                if old_module is None:
                    sys.modules.pop("common_renderer", None)
                else:
                    sys.modules["common_renderer"] = old_module
        if set(self.questions) != set(self.records):
            raise WorkbenchError("原题类和 dataset.jsonl 的题号不一致。")

    def assert_baseline(self):
        current = manifest_for(self.source)
        if current["files"] != self.manifest["files"]:
            raise WorkbenchError("原始输入在运行期间发生变化，请恢复原基线后重启。", 409)

    def scene(self, qid):
        with RENDER_LOCK:
            captured = []
            before = set(plt.get_fignums())

            def capture(fig, destination):
                if captured or not fig.axes:
                    raise WorkbenchError("原题必须只产生一个含坐标轴的场景。")
                self.renderer.lock_view(fig.axes[0])
                captured.append(fig)
                return {"captured": True}

            try:
                with bindings(self.modules[qid], {"finalize": capture}):
                    self.questions[qid].draw(int(qid[3:]))
                if not captured:
                    raise WorkbenchError("未截获原题 finalize，已停止生成。")
                fig = captured[0]
                ax = fig.axes[0]
                points, segments, curves = [], [], []
                for collection in ax.collections:
                    if isinstance(collection, PathCollection):
                        faces = collection.get_facecolors()
                        filled = not (len(faces) and np.allclose(faces[0][:3], 1))
                        for xy in collection.get_offsets():
                            xy = [float(v) for v in xy]
                            if visible(xy):
                                points.append({"id": f"point_{len(points) + 1:03d}", "xy": xy, "filled": filled})
                    elif isinstance(collection, LineCollection):
                        for vertices in collection.get_segments():
                            segments.extend(zip(vertices[:-1], vertices[1:]))
                for line in ax.lines:
                    vertices = np.column_stack([line.get_xdata(), line.get_ydata()])
                    segments.extend((a, b) for a, b in zip(vertices[:-1], vertices[1:])
                                    if np.isfinite([a, b]).all())
                    curves.append({"id": f"curve_{len(curves) + 1:03d}", "kind": "function"})
                for patch in ax.patches:
                    if isinstance(patch, Polygon):
                        vertices = patch.get_xy()
                        segments.extend(zip(vertices[:-1], vertices[1:]))
                    curves.append({"id": f"curve_{len(curves) + 1:03d}", "kind": type(patch).__name__})
                return Scene(fig, ax, points, segments, curves, list(ax.texts) + list(fig.texts))
            except Exception:
                for number in set(plt.get_fignums()) - before:
                    plt.close(number)
                raise

    def integer_geometry(self, qid, scene):
        """Replay y=f(x) expressions on an integer grid and validate outlines."""
        verified, unsupported, curve_counter = [], [], [0]
        tolerance = self.tolerance
        tree = ast.parse(textwrap.dedent(inspect.getsource(self.questions[qid].draw)))
        domain_names = {n.targets[0].id for n in ast.walk(tree)
                        if isinstance(n, ast.Assign) and len(n.targets) == 1 and isinstance(n.targets[0], ast.Name)
                        and isinstance(n.value, ast.Call) and isinstance(n.value.func, ast.Name)
                        and n.value.func.id == "domain_linspace"}
        direct_functions = all(isinstance(n.args[1], ast.Name) and n.args[1].id in domain_names
                               for n in ast.walk(tree) if isinstance(n, ast.Call)
                               and isinstance(n.func, ast.Name) and n.func.id == "plot_curve")

        def grid(start, stop, num=200, endpoint=True):
            original = self.renderer.domain_linspace(start, stop, num, endpoint)
            finite = original[np.isfinite(original)]
            if not len(finite):
                return np.array([np.nan])
            lo, hi = float(min(finite)), float(max(finite))
            return np.arange(np.ceil(lo), np.floor(hi) + 1, dtype=float)

        def record_points(curve_id, coordinates, method):
            for x, y in coordinates:
                if not visible([x, y], tolerance):
                    continue
                ix, iy = int(round(x)), int(round(y))
                if abs(x - ix) > tolerance or abs(y - iy) > tolerance:
                    continue
                # Open endpoints are not members of that branch. Do not use
                # their coordinates for a projection or a new on-curve marker.
                if any(not p["filled"] and np.linalg.norm(np.array(p["xy"]) - [ix, iy]) <= tolerance
                       for p in scene.points):
                    continue
                verified.append({"xy": [ix, iy], "curve_id": curve_id,
                                 "verification": method, "tolerance": tolerance})

        def record_curve(ax, x, y):
            curve_counter[0] += 1
            curve_id = f"curve_{curve_counter[0]:03d}"
            if not direct_functions:
                unsupported.append(f"{curve_id}：不支持该参数曲线的完整几何验证")
                return
            x, y = np.broadcast_arrays(np.asarray(x), np.asarray(y))
            if np.iscomplexobj(y):
                y = np.where(np.abs(y.imag) <= tolerance, y.real, np.nan)
            record_points(curve_id, zip(x.flatten(), y.flatten()), "original_draw_integer_evaluation")

        def record_patch(ax, patch):
            if isinstance(patch, Circle) and patch.radius <= self.renderer.MARKER_CIRCLE_RADIUS:
                return
            curve_counter[0] += 1
            curve_id = f"curve_{curve_counter[0]:03d}"
            matches = []
            for x in range(-8, 9):
                for y in range(-8, 9):
                    if isinstance(patch, Ellipse):
                        width, height = patch.width / 2, patch.height / 2
                        if width <= 0 or height <= 0:
                            continue
                        theta = np.deg2rad(patch.angle)
                        dx, dy = np.array([x, y]) - patch.center
                        u = dx * np.cos(theta) + dy * np.sin(theta)
                        v = -dx * np.sin(theta) + dy * np.cos(theta)
                        belongs = abs((u / width) ** 2 + (v / height) ** 2 - 1) <= tolerance
                    elif isinstance(patch, Polygon):
                        belongs = False
                        vertices = patch.get_xy()
                        for a, b in zip(vertices[:-1], vertices[1:]):
                            delta = b - a
                            length2 = float(delta @ delta)
                            if length2 <= tolerance ** 2:
                                continue
                            distance = abs(delta[0] * (y - a[1]) - delta[1] * (x - a[0])) / np.sqrt(length2)
                            position = float((np.array([x, y]) - a) @ delta / length2)
                            belongs |= distance <= tolerance and -tolerance <= position <= 1 + tolerance
                    else:
                        unsupported.append(f"{curve_id}：不支持该几何验证 ({type(patch).__name__})")
                        return
                    if belongs:
                        matches.append((x, y))
            record_points(curve_id, matches, "analytic_" + type(patch).__name__)

        def noop(*args, **kwargs):
            return None

        replacements = {name: noop for name in (
            "scatter_points", "label", "figure_label", "fill_polygon", "fill_region",
            "aux_vline", "aux_hline", "slope_segments", "finalize")}
        replacements.update({"open_canvas": lambda *a, **k: (None, None), "domain_linspace": grid,
                             "plot_curve": record_curve, "add_styled_patch": record_patch})
        with RENDER_LOCK, bindings(self.modules[qid], replacements), np.errstate(all="ignore"):
            try:
                self.questions[qid].draw(int(qid[3:]))
            except Exception as error:
                unsupported.append(f"不支持该几何验证：{type(error).__name__}: {error}")
        if not scene.curves and scene.segments:
            unsupported.append("不支持将辅助线推断为原函数；未验证其数学定义")
        unique = {(p["curve_id"], *p["xy"]): p for p in verified}
        return list(unique.values()), sorted(set(unsupported))

    def inspect_question(self, qid):
        with RENDER_LOCK:
            scene = self.scene(qid)
            try:
                _, rendered_hash = scene_png(scene)
                original = self.source / self.records[qid]["image"]
                original_hash = pixel_hash(original)
                if rendered_hash != original_hash:
                    raise WorkbenchError(f"输入不一致：{qid} 源代码无操作重绘与已审核原图像素不同。不会建立新基线。", 409)
                integers, unsupported = self.integer_geometry(qid, scene)
                b3 = [{"source": {"kind": "original_point", **point},
                       "endpoints": [point["xy"], [0.0, 0.0]]}
                      for point in scene.points if new_segment(scene, [point["xy"], [0, 0]])]
                starts = [{"kind": "original_point", **point} for point in scene.points]
                starts += [{"kind": "verified_curve_integer", **point} for point in integers]
                b4, seen = [], set()
                for start in starts:
                    x, y = start["xy"]
                    for axis, end in (("x", [x, 0.0]), ("y", [0.0, y])):
                        key = (float(x), float(y), axis)
                        if key not in seen and new_segment(scene, [[x, y], end]):
                            seen.add(key)
                            b4.append({"source": start, "projection_axis": axis, "endpoints": [[x, y], end]})
                b5 = []
                for point in integers:
                    if not any(p["filled"] and np.linalg.norm(np.array(p["xy"]) - point["xy"]) <= self.tolerance
                               for p in scene.points):
                        b5.append(point)
                status = lambda options, reason: {"status": "available" if options else "unavailable",
                                                   "reason": "" if options else reason}
                operations = {op: {"status": "available", "reason": ""} for op in ("A1", "A2", "A3", "A4", "B1", "B2")}
                operations["B3"] = status(b3, "原图没有可见、非原点且能产生新线段的显式点标记。")
                note = "；".join(unsupported)
                operations["B4"] = status(b4, note or "原有点与已验证整数点均无有效的新投影线。")
                operations["B5"] = status(b5, note or "原曲线上没有可新增的、通过数学验证的整数点。")
                return {"original_pixel_sha256": original_hash, "original_point_count": len(scene.points),
                        "original_points": scene.points, "curves": scene.curves, "integer_points": integers,
                        "unsupported_geometry": unsupported, "b3_sources": b3, "b4_sources": b4,
                        "b5_points": b5, "operations": operations}
            finally:
                scene.close()
