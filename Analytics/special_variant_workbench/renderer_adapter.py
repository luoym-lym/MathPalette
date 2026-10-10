"""Capture frozen original scenes; no original save or batch entry is run."""
from __future__ import annotations

import ast
import importlib.util
import inspect
import io
import sys
import threading
from contextlib import contextmanager
from dataclasses import dataclass
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.collections import PathCollection
from PIL import Image

from workbench_io import (WorkbenchError, canonical_hash, environment_versions,
                          file_hash, parse_json, pixel_hash, read_json)

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


@dataclass
class Scene:
    fig: object
    ax: object
    objects: list
    artists: dict

    def close(self):
        plt.close(self.fig)


def scene_png(scene):
    stream = io.BytesIO()
    scene.fig.savefig(stream, dpi=100, facecolor="#FFFFFF", transparent=False, bbox_inches=None)
    data = stream.getvalue()
    with Image.open(io.BytesIO(data)) as image:
        if image.size != (768, 768) or image.convert("RGBA").getextrema()[3] != (255, 255):
            raise WorkbenchError("渲染必须产生不透明的 768×768 PNG。", code="invalid_render")
        digest = pixel_hash(image)
    return data, digest


def geometry_summary(vertices):
    vertices = np.asarray(vertices, dtype=float).reshape(-1, 2)
    finite = vertices[np.isfinite(vertices).all(axis=1)]
    if not len(finite):
        return {"finite_vertex_count": 0, "bounds": None, "samples": []}
    indices = np.unique(np.linspace(0, len(finite) - 1, min(33, len(finite))).astype(int))
    return {"finite_vertex_count": len(finite),
            "bounds": [finite.min(axis=0).tolist(), finite.max(axis=0).tolist()],
            "samples": finite[indices].tolist()}


class RendererAdapter:
    def __init__(self, config, expected_manifest=None):
        self.config = config
        self.source_files = sorted(Path(config["question_class_dir"]).glob("function_plot*.py"))
        records = [parse_json(line) for line in Path(config["dataset_file"]).read_text(
            encoding="utf-8-sig").splitlines() if line.strip()]
        if [r["id"] for r in records] != [f"Ana{i:02d}" for i in range(1, 81)]:
            raise WorkbenchError("dataset.jsonl 必须恰有 Ana01～Ana80，且按顺序排列。")
        self.records = {record["id"]: record for record in records}
        self.original_paths = {qid: Path(config["original_image_dir"]) / f"{qid}.png" for qid in self.records}
        self.input_files = {"dataset.jsonl": Path(config["dataset_file"]),
                            "common_renderer.py": Path(config["common_renderer_file"]),
                            "protocol.json": Path(config["protocol_file"]),
                            **{f"image/{qid}.png": p for qid, p in self.original_paths.items()},
                            **{f"question_classes/{p.name}": p for p in self.source_files}}
        self.manifest = self.make_manifest()
        if expected_manifest and self.manifest != expected_manifest:
            changes = [name for name in set(expected_manifest["files"]) | set(self.manifest["files"])
                       if expected_manifest["files"].get(name) != self.manifest["files"].get(name)]
            raise WorkbenchError("输入基线或依赖版本变化：" + ", ".join(sorted(changes)[:12]) +
                                 "；请恢复已审核环境。", 409, "baseline_changed")
        self.questions, self.modules, self.sources = {}, {}, {}
        self._load()

    def make_manifest(self):
        files = {name: file_hash(path) for name, path in sorted(self.input_files.items())}
        values = {"files": files, "environment": environment_versions()}
        return {**values, "fingerprint": canonical_hash(values)}

    def assert_baseline(self):
        if self.make_manifest() != self.manifest:
            raise WorkbenchError("原始输入或依赖在运行期间改变，请恢复基线后重启。", 409, "baseline_changed")

    def _load(self):
        with RENDER_LOCK:
            old_path, old_bytecode = sys.path[:], sys.dont_write_bytecode
            old_module = sys.modules.get("common_renderer")
            try:
                sys.dont_write_bytecode = True
                path = Path(self.config["common_renderer_file"])
                # The original renderer loads this adjacent protocol; refuse a misleading separate config.
                if path.with_name("protocol.json").resolve() != Path(self.config["protocol_file"]).resolve():
                    raise WorkbenchError("当前公共渲染器要求 protocol.json 与自身同目录。")
                spec = importlib.util.spec_from_file_location("_special_original_renderer", path)
                self.renderer = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(self.renderer)
                sys.modules["common_renderer"] = self.renderer
                for path in self.source_files:
                    spec = importlib.util.spec_from_file_location("_special_" + path.stem.replace("-", "_"), path)
                    module = importlib.util.module_from_spec(spec)
                    spec.loader.exec_module(module)
                    for qid in self.records:
                        cls = getattr(module, qid, None)
                        if cls:
                            if qid in self.questions:
                                raise WorkbenchError(f"重复题目类：{qid}")
                            self.questions[qid], self.modules[qid] = cls(), module
                            self.sources[qid] = {"source_file": str(path.resolve()), "source_class": qid,
                                                 "source_id": self.questions[qid].source_id,
                                                 "constants": vars(self.questions[qid])}
            finally:
                sys.path[:] = old_path
                sys.dont_write_bytecode = old_bytecode
                if old_module is None:
                    sys.modules.pop("common_renderer", None)
                else:
                    sys.modules["common_renderer"] = old_module
        if set(self.questions) != set(self.records):
            raise WorkbenchError("原题类与数据题号不一致，请检查嵌套 question_class_dir。")

    def scene(self, qid):
        if qid not in self.records:
            raise WorkbenchError("不存在此题号。")
        with RENDER_LOCK:
            module = self.modules[qid]
            captured, objects, artists, counters = [], [], {}, {}
            before = set(plt.get_fignums())
            source = Path(self.sources[qid]["source_file"]).read_text(encoding="utf-8")
            calls = {node.lineno: ast.get_source_segment(source, node)
                     for node in ast.walk(ast.parse(source)) if isinstance(node, ast.Call)
                     and isinstance(node.func, ast.Name)}

            def register(prefix, kind, artist, geometry, styleable=False, call=None):
                counters[prefix] = counters.get(prefix, 0) + 1
                oid = f"{prefix}_{counters[prefix]:03d}"
                objects.append({"id": oid, "type": prefix, "kind": kind,
                                "styleable": styleable, "geometry": geometry, "source_call": call})
                artists[oid] = artist

            def wrap(helper):
                original = getattr(module, helper)

                def tracked(*args, **kwargs):
                    frame = inspect.currentframe().f_back
                    call = {"line": frame.f_lineno, "expression": calls.get(frame.f_lineno, helper)}
                    del frame
                    surface = args[0]
                    fig = surface if helper == "figure_label" else surface.figure
                    ax = fig.axes[0]
                    old = {"lines": len(ax.lines), "collections": len(ax.collections),
                           "patches": len(ax.patches), "texts": len(ax.texts), "fig_texts": len(fig.texts)}
                    result = original(*args, **kwargs)
                    for line in list(ax.lines)[old["lines"]:]:
                        vertices = np.column_stack([line.get_xdata(), line.get_ydata()])
                        register("curve", "function_curve", line, geometry_summary(vertices), True, call)
                    for patch in list(ax.patches)[old["patches"]:]:
                        vertices = patch.get_path().transformed(patch.get_patch_transform()).vertices
                        geometry = {"shape": type(patch).__name__, **geometry_summary(vertices)}
                        for attribute in ("center", "radius", "width", "height", "angle"):
                            value = getattr(patch, attribute, None)
                            if value is not None:
                                geometry[attribute] = np.asarray(value).tolist()
                        outline = helper == "add_styled_patch"
                        register("curve" if outline else "region", "geometric_outline" if outline else "region_fill",
                                 patch, geometry, outline, call)
                    for collection in list(ax.collections)[old["collections"]:]:
                        if isinstance(collection, PathCollection):
                            faces = collection.get_facecolors()
                            filled = not (len(faces) and np.allclose(faces[0][:3], 1))
                            for xy in collection.get_offsets():
                                register("point", "original_point", collection,
                                         {"xy": [float(v) for v in xy], "filled": filled}, False, call)
                        elif helper in ("aux_vline", "aux_hline"):
                            register("curve", "line_segment", collection,
                                     {"segments": [v.tolist() for v in collection.get_segments()]}, True, call)
                        elif helper == "slope_segments":
                            register("slope", "slope_field", collection,
                                     geometry_summary(collection.get_offsets()), False, call)
                        else:
                            register("region", "region_fill", collection, {}, False, call)
                    texts = list(ax.texts)[old["texts"]:] + list(fig.texts)[old["fig_texts"]:]
                    for text in texts:
                        register("text", "original_label", text,
                                 {"xy": [float(v) for v in text.get_position()], "text": text.get_text(),
                                  "coordinates": "figure_fraction" if helper == "figure_label" else "data"}, False, call)
                    return result
                return tracked

            def capture(fig, destination):
                if captured or len(fig.axes) != 1:
                    raise WorkbenchError("原题必须仅产生一个单坐标轴场景。")
                self.renderer.lock_view(fig.axes[0])
                captured.append(fig)
                return {"captured": True}

            replacements = {name: wrap(name) for name in (
                "plot_curve", "scatter_points", "add_styled_patch", "aux_vline", "aux_hline",
                "label", "figure_label", "fill_polygon", "fill_region", "slope_segments")}
            replacements["finalize"] = capture
            try:
                with bindings(module, replacements):
                    self.questions[qid].draw(int(qid[3:]))
                if not captured:
                    raise WorkbenchError("未截获 finalize，拒绝运行原始保存流程。")
                fig, ax = captured[0], captured[0].axes[0]
                objects.extend([{"id": "axis_x", "type": "axis", "kind": "coordinate_axis", "styleable": False},
                                {"id": "axis_y", "type": "axis", "kind": "coordinate_axis", "styleable": False},
                                {"id": "grid", "type": "grid", "kind": "coordinate_grid", "styleable": False},
                                {"id": "origin_zero", "type": "text", "kind": "coordinate_label", "styleable": False}])
                return Scene(fig, ax, objects, artists)
            except Exception:
                for number in set(plt.get_fignums()) - before:
                    plt.close(number)
                raise

    def inspect_question(self, qid):
        with RENDER_LOCK:
            scene = self.scene(qid)
            try:
                _, digest = scene_png(scene)
                original_digest = pixel_hash(self.original_paths[qid])
                if digest != original_digest:
                    raise WorkbenchError(f"{qid} 无操作重绘与原图像素不同；保留原图并停止。", 409, "baseline_mismatch")
                return {"original_pixel_sha256": original_digest, "objects": scene.objects}
            finally:
                scene.close()

    def highlight(self, qid, oid):
        with RENDER_LOCK:
            scene = self.scene(qid)
            try:
                obj = next((o for o in scene.objects if o["id"] == oid), None)
                if not obj or oid not in scene.artists:
                    raise WorkbenchError("该对象不提供高亮；请选择曲线、轮廓、点或原标签。")
                artist = scene.artists[oid]
                if obj["type"] == "curve":
                    from matplotlib.patches import Patch
                    if isinstance(artist, Patch):
                        artist.set_edgecolor("#E11D48")
                    else:
                        artist.set_color("#E11D48")
                    artist.set_linewidth(3)
                elif obj["type"] == "point":
                    scene.ax.scatter(*obj["geometry"]["xy"], s=150, facecolors="none", edgecolors="#E11D48", zorder=20)
                elif obj["type"] == "text":
                    artist.set_color("#E11D48")
                else:
                    artist.set_color("#E11D48")
                scene.fig.text(.02, .98, f"REFERENCE ONLY: {qid} / {oid}", color="#E11D48", fontsize=11, va="top")
                return scene_png(scene)[0]
            finally:
                scene.close()
