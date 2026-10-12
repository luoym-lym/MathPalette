"""Read-only adapter for frozen PlaneGeometry scenes and their real artists."""
from __future__ import annotations

import copy
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
from matplotlib.axes import Axes
from matplotlib.patches import Patch
from PIL import Image

from workbench_io import (WorkbenchError, canonical_hash, contained_path, environment_versions,
                          file_hash, parse_json, pixel_hash, read_json)

RENDER_LOCK = threading.RLock()
BRANCH = "PlaneGeometry"
STYLEABLE = {"segment", "circle", "arc", "polygon", "angle_arc", "right_angle", "equal_tick", "parallel_mark", "ellipse"}
# Plane02 predates dimension roles. These legacy measurement/extension points
# are not mathematical vertices. The original frozen scene stays untouched.
SNAP_EXCLUDED = {"Plane02": {"aq1", "aq2", "P_extension", "Q_extension"},
                 "Plane09": {"P_horizontal_left", "P_horizontal_right"}}


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
    snap_points: list

    def close(self):
        plt.close(self.fig)


def scene_png(scene):
    stream = io.BytesIO()
    with matplotlib.rc_context({"savefig.bbox": None, "savefig.transparent": False}):
        scene.fig.savefig(stream, format="png", dpi=100, facecolor="#FFFFFF", transparent=False,
                          bbox_inches=None, pad_inches=0)
    data = stream.getvalue()
    with Image.open(io.BytesIO(data)) as image:
        if image.size != (768, 768) or image.convert("RGBA").getextrema()[3] != (255, 255):
            raise WorkbenchError("渲染必须产生不透明的 768×768 PNG。", code="invalid_render")
        digest = pixel_hash(image)
    return data, digest


def snap_points(frozen):
    """Expose displayed vertices and named/marked points, never inferred points.

    Dense polygons are sampled curved fills, whose construction samples are not
    vertices. Their actual edge endpoints occur in independent scene segments.
    """
    exposed = {}
    def add(value, reason):
        if isinstance(value, str) and value in frozen["points"]:
            exposed.setdefault(value, set()).add(reason)
    for item in frozen["objects"]:
        if item["type"] == "point":
            add(item["point"], "point_symbol")
        elif item.get("role") != "dimension" and (item["type"] == "segment" or
                item["type"] == "polygon" and len(item["points"]) <= 16):
            for value in item["points"]:
                add(value, "vertex")
    for label in frozen["labels"]:
        if label["type"] == "vertex":
            add(label["point"], "named_point")
    excluded = SNAP_EXCLUDED.get(frozen["id"], set())
    return [{"id": name, "label": name, "xy": copy.deepcopy(xy), "kind": "original_point",
             "reasons": sorted(exposed[name])} for name, xy in frozen["points"].items()
            if name in exposed and name not in excluded]


class RendererAdapter:
    def __init__(self, config, expected_manifest=None):
        self.config = config
        dataset = Path(config["dataset_file"]).resolve()
        self.branch_root, self.project = dataset.parent, dataset.parent.parent
        if str(self.project) not in sys.path:
            sys.path.insert(0, str(self.project))
        from dataset_tools.catalog import assert_formal_dataset
        assert_formal_dataset(dataset)
        records = [parse_json(line) for line in dataset.read_text(encoding="utf-8-sig").splitlines() if line.strip()]
        if not records or [r["id"] for r in records] != [f"Plane{i:02d}" for i in range(1, len(records) + 1)]:
            raise WorkbenchError("平面正式 dataset.jsonl 须从 Plane01 连续编号并按顺序排列。")
        self.records = {record["id"]: record for record in records}
        self.original_paths = {qid: contained_path(self.branch_root, r["image"]) for qid, r in self.records.items()}
        self.scene_paths = {qid: contained_path(self.branch_root, r["scene"]) for qid, r in self.records.items()}
        self.source_paths = {qid: contained_path(self.branch_root, r["script"]) for qid, r in self.records.items()}
        self.source_files = list(self.source_paths.values())
        self.input_files = {"dataset.jsonl": dataset,
                            "common_renderer.py": Path(config["common_renderer_file"]),
                            "protocol.json": Path(config["protocol_file"]),
                            "geometry_dataset.py": self.project / "dataset_tools/geometry_dataset.py",
                            **{f"image/{qid}.png": p for qid, p in self.original_paths.items()},
                            **{f"scenes/{qid}.json": p for qid, p in self.scene_paths.items()},
                            **{f"question_classes/{p.name}": p for p in self.source_files}}
        for row in self.records.values():
            for dependency in row.get("runtime_dependencies", []):
                self.input_files["runtime_dependencies/" + dependency] = contained_path(self.branch_root, dependency)
        self.manifest = self.make_manifest()
        if expected_manifest and self.manifest != expected_manifest:
            raise WorkbenchError("输入基线或依赖版本变化；请恢复已审核环境。", 409, "baseline_changed")
        renderer_path = Path(config["common_renderer_file"])
        if renderer_path.with_name("protocol.json").resolve() != Path(config["protocol_file"]).resolve():
            raise WorkbenchError("公共绘图器要求 protocol.json 与自身同目录。")
        spec = importlib.util.spec_from_file_location("_plane_special_original_renderer", renderer_path)
        self.renderer = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(self.renderer)
        self.family_renderers = {}
        for row in self.records.values():
            family = row.get("renderer_family")
            if not family or family in self.family_renderers:
                continue
            if family not in {"plane", "plane_extended", "plane_arrows", "plane_curves"}:
                raise WorkbenchError("不支持的平面冻结绘图器家族。")
            relative = f"dataset_generator/mathverse_renderers/{family}/common_renderer.py"
            protocol = f"dataset_generator/mathverse_renderers/{family}/protocol.json"
            if not {relative, protocol}.issubset(row.get("runtime_dependencies", [])):
                raise WorkbenchError("冻结绘图器与协议必须列入审核依赖。")
            spec = importlib.util.spec_from_file_location("_plane_special_" + family,
                                                        contained_path(self.branch_root, relative))
            renderer = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(renderer)
            self.family_renderers[family] = renderer
        self.frozen_scenes = {qid: read_json(p) for qid, p in self.scene_paths.items()}
        self.sources = {qid: {"source_file": str(self.source_paths[qid]), "source_class": qid,
                              "source_dataset": r["source_dataset"], "scene_path": str(self.scene_paths[qid]),
                              "branch": BRANCH} for qid, r in self.records.items()}

    def dependencies(self, qid):
        return ("common_renderer.py", "protocol.json", "geometry_dataset.py", f"image/{qid}.png",
                f"scenes/{qid}.json", f"question_classes/{self.source_paths[qid].name}") + tuple(
                    "runtime_dependencies/" + p for p in self.records[qid].get("runtime_dependencies", []))

    def make_manifest(self):
        values = {"files": {name: file_hash(p) for name, p in sorted(self.input_files.items())},
                  "environment": environment_versions()}
        return {**values, "fingerprint": canonical_hash(values)}

    def assert_baseline(self):
        if self.make_manifest() != self.manifest:
            raise WorkbenchError("原始输入或依赖在运行期间改变，请恢复基线后重启。", 409, "baseline_changed")

    def scene(self, qid):
        if qid not in self.records:
            raise WorkbenchError("不存在此平面题号。")
        with RENDER_LOCK:
            frozen = self.frozen_scenes[qid]
            renderer = self.family_renderers.get(self.records[qid].get("renderer_family"), self.renderer)
            by_id = {item["id"]: item for item in frozen["objects"]}
            captured = {oid: [] for oid in by_id}
            render_code = renderer.render_scene.__code__

            def tracked(method):
                original = getattr(Axes, method)
                def add(ax, artist, *args, **kwargs):
                    result = original(ax, artist, *args, **kwargs)
                    frame = inspect.currentframe().f_back
                    try:
                        while frame and frame.f_code is not render_code:
                            frame = frame.f_back
                        item = frame.f_locals.get("item") if frame else None
                        if item and item.get("id") in by_id:
                            # Semantic polygons have separate fill and outline;
                            # never recolor the fill alongside its opaque stroke.
                            if item["type"] in {"region", "curved_region"} or not (
                                    isinstance(artist, Patch) and artist.get_edgecolor()[3] == 0):
                                captured[item["id"]].append(artist)
                    finally:
                        del frame
                    return result
                return add

            with bindings(Axes, {method: tracked(method) for method in ("add_line", "add_patch", "add_collection")}):
                fig, _ = renderer.render_scene(frozen)
            objects = [{"id": item["id"], "type": "curve" if item["type"] in STYLEABLE else item["type"],
                        "kind": item["type"], "styleable": item["type"] in STYLEABLE,
                        "source_call": {"scene_object_id": item["id"]},
                        "geometry": copy.deepcopy(item), "artist_count": len(captured[item["id"]])}
                       for item in frozen["objects"]]
            if any(not captured[obj["id"]] for obj in objects):
                plt.close(fig)
                raise WorkbenchError("冻结场景对象未映射到实际绘图对象。", 409, "object_changed")
            return Scene(fig, fig.axes[0], objects, captured, snap_points(frozen))

    def inspect_question(self, qid):
        with RENDER_LOCK:
            scene = self.scene(qid)
            try:
                _, digest = scene_png(scene)
                original_digest = pixel_hash(self.original_paths[qid])
                if digest != original_digest:
                    raise WorkbenchError(f"{qid} 无操作重绘与原图像素不同；保留原图并停止。", 409, "baseline_mismatch")
                from drawing_board import describe_captured_scene
                return {"original_pixel_sha256": original_digest, "objects": scene.objects,
                        "snap_points": scene.snap_points, "canvas": describe_captured_scene(scene, qid)}
            finally:
                scene.close()

    def highlight(self, qid, oid):
        with RENDER_LOCK:
            scene = self.scene(qid)
            try:
                if oid not in scene.artists:
                    raise WorkbenchError("未知原对象。")
                for artist in scene.artists[oid]:
                    if isinstance(artist, Patch):
                        artist.set_edgecolor("#E11D48")
                    else:
                        artist.set_color("#E11D48")
                    artist.set_linewidth(3)
                scene.fig.text(.02, .98, f"REFERENCE ONLY: {qid} / {oid}", color="#E11D48", fontsize=11, va="top")
                return scene_png(scene)[0]
            finally:
                scene.close()
