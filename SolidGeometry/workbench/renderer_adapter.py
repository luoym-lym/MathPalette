"""Read-only adapter for frozen solid scenes and their exact projected artists."""
from __future__ import annotations

import copy
import importlib.util
import io
import sys
import threading
from dataclasses import dataclass
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

from workbench_io import (WorkbenchError, canonical_hash, contained_path, environment_versions,
                          file_hash, parse_json, pixel_hash, read_json)

RENDER_LOCK = threading.RLock()


@dataclass
class Scene:
    fig: object
    ax: object
    objects: list
    artists: dict
    snap_points: list
    settings: dict

    def close(self):
        plt.close(self.fig)


def scene_png(scene):
    stream = io.BytesIO()
    with matplotlib.rc_context(scene.settings):
        scene.fig.savefig(stream, format="png", dpi=100, facecolor="#FFFFFF",
                          transparent=False, bbox_inches=None, pad_inches=0,
                          metadata={"Software": "MathPalette SolidGeometry 1.0.0"})
    data = stream.getvalue()
    with Image.open(io.BytesIO(data)) as image:
        if image.size != (768, 768) or image.convert("RGBA").getextrema()[3] != (255, 255):
            raise WorkbenchError("渲染必须产生不透明的 768×768 PNG。", code="invalid_render")
        digest = pixel_hash(image)
    return data, digest


class RendererAdapter:
    def __init__(self, config, expected_manifest=None):
        self.config = config
        branch = Path(config["dataset_file"]).resolve().parent
        project = branch.parent
        if str(project) not in sys.path:
            sys.path.insert(0, str(project))
        from dataset_tools.catalog import assert_formal_dataset
        assert_formal_dataset(config["dataset_file"])
        records = [parse_json(line) for line in Path(config["dataset_file"]).read_text(
            encoding="utf-8-sig").splitlines() if line.strip()]
        if not records or [r["id"] for r in records] != [f"Solid{i:02d}" for i in range(1, len(records) + 1)]:
            raise WorkbenchError("正式 dataset.jsonl 须从 Solid01 连续编号并按顺序排列。")
        self.records = {record["id"]: record for record in records}
        self.original_paths = {qid: branch / r["image"] for qid, r in self.records.items()}
        self.scene_paths = {qid: branch / r["scene"] for qid, r in self.records.items()}
        self.source_files = [branch / r["script"] for r in records]
        self.input_files = {"dataset.jsonl": Path(config["dataset_file"]),
                            "common_renderer.py": Path(config["common_renderer_file"]),
                            "protocol.json": Path(config["protocol_file"]),
                            "geometry_dataset.py": project / "dataset_tools/geometry_dataset.py",
                            **{f"image/{qid}.png": p for qid, p in self.original_paths.items()},
                            **{f"scenes/{qid}.json": p for qid, p in self.scene_paths.items()},
                            **{f"question_classes/{p.name}": p for p in self.source_files}}
        for row in self.records.values():
            for dependency in row.get("runtime_dependencies", []):
                self.input_files["runtime_dependencies/" + dependency] = contained_path(branch, dependency)
        self.manifest = self.make_manifest()
        if expected_manifest and self.manifest != expected_manifest:
            raise WorkbenchError("输入基线或依赖版本变化；请恢复已审核环境。", 409, "baseline_changed")
        path = Path(config["common_renderer_file"])
        if path.with_name("protocol.json").resolve() != Path(config["protocol_file"]).resolve():
            raise WorkbenchError("冻结公共渲染器要求 protocol.json 与自身同目录。")
        spec = importlib.util.spec_from_file_location("_solid_special_original_renderer", path)
        self.renderer = importlib.util.module_from_spec(spec)
        old_bytecode = sys.dont_write_bytecode
        try:
            sys.dont_write_bytecode = True
            spec.loader.exec_module(self.renderer)
        finally:
            sys.dont_write_bytecode = old_bytecode
        self.protocol = read_json(config["protocol_file"])
        self.family_renderers = {}
        for row in self.records.values():
            family = row.get("renderer_family")
            if not family or family in self.family_renderers:
                continue
            if family != "solid":
                raise WorkbenchError("不支持的立体冻结绘图器家族。")
            relative = f"dataset_generator/mathverse_renderers/{family}/common_renderer.py"
            protocol = f"dataset_generator/mathverse_renderers/{family}/protocol.json"
            if not {relative, protocol}.issubset(row.get("runtime_dependencies", [])):
                raise WorkbenchError("冻结绘图器与协议必须列入审核依赖。")
            spec = importlib.util.spec_from_file_location("_solid_special_" + family, contained_path(branch, relative))
            renderer = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(renderer)
            self.family_renderers[family] = (renderer, read_json(contained_path(branch, protocol)))
        self.scenes = {qid: read_json(path) for qid, path in self.scene_paths.items()}
        self.sources = {}
        for qid, record in self.records.items():
            frozen = self.scenes[qid]
            if frozen["id"] != qid or frozen["subject"] != "SolidGeometry":
                raise WorkbenchError("冻结场景身份与正式题号不一致。")
            self.sources[qid] = {"source_file": str((branch / record["script"]).resolve()),
                "source_class": qid, "source_dataset": record["source_dataset"],
                "scene_file": str(self.scene_paths[qid].resolve()),
                "projection": copy.deepcopy(frozen["projection"]),
                "coordinate_system": "frozen_projected_2d"}

    def make_manifest(self):
        values = {"files": {name: file_hash(path) for name, path in sorted(self.input_files.items())},
                  "environment": environment_versions()}
        return {**values, "fingerprint": canonical_hash(values)}

    def question_dependencies(self, qid):
        return ("common_renderer.py", "protocol.json", "geometry_dataset.py", f"image/{qid}.png",
                f"scenes/{qid}.json", f"question_classes/{Path(self.sources[qid]['source_file']).name}") + tuple(
                    "runtime_dependencies/" + p for p in self.records[qid].get("runtime_dependencies", []))

    def assert_baseline(self):
        if self.make_manifest() != self.manifest:
            raise WorkbenchError("原始输入或依赖在运行期间改变，请恢复基线后重启。", 409, "baseline_changed")

    def snap_points(self, qid):
        """Only displayed vertices/point labels; never all construction anchors."""
        frozen = self.scenes[qid]
        renderer, _ = self.family_renderers.get(self.records[qid].get("renderer_family"), (self.renderer, self.protocol))
        refs = set()
        for item in frozen["objects"]:
            # Existing relation-symbol corners are drawing construction anchors,
            # not vertices of the solid or independently named diagram points.
            if item["id"].startswith(("equal_tick_", "right_angle_")):
                continue
            if item["type"] in ("segment", "polyline", "face"):
                refs.update(ref for ref in item["points"] if isinstance(ref, str))
            elif item["type"] == "point" and isinstance(item["point"], str):
                refs.add(item["point"])
            elif item["type"] == "circular_arc":
                for interval in item["intervals"]:
                    for key in ("start_point", "end_point"):
                        if isinstance(interval.get(key), str):
                            refs.add(interval[key])
        names = {}
        for label in frozen["labels"]:
            if label["type"] == "vertex" and isinstance(label["anchor"], str):
                refs.add(label["anchor"])
                names[label["anchor"]] = label["text"]
        return [{"id": ref, "label": names.get(ref, ref), "source": "frozen_scene",
                 "world_xyz": copy.deepcopy(frozen["points"][ref]),
                 "xy": renderer.project(frozen, renderer.point(frozen, ref)).tolist()}
                for ref in frozen["points"] if ref in refs]

    def scene(self, qid):
        if qid not in self.records:
            raise WorkbenchError("不存在此立体题号。")
        with RENDER_LOCK:
            frozen = self.scenes[qid]
            renderer, protocol = self.family_renderers.get(self.records[qid].get("renderer_family"), (self.renderer, self.protocol))
            # Invoke the original renderer unchanged. Its frozen object order
            # maps 1:n actual artists back to each stable scene ID.
            fig, _ = renderer.render_scene(frozen, protocol)
            try:
                ax = fig.axes[0]
                lines, patches = iter(ax.lines), iter(ax.patches)
                objects, artists = [], {}
                for item in frozen["objects"]:
                    kind, oid = item["type"], item["id"]
                    owned, expected = [], []
                    if kind == "circular_arc":
                        expected = [xy for _, xy in renderer.arc_parts(frozen, item)]
                    elif kind in ("segment", "polyline"):
                        expected = [renderer.project(frozen, [renderer.point(frozen, r) for r in item["points"]])]
                    if expected:
                        for xy in expected:
                            artist = next(lines)
                            if not np.array_equal(artist.get_xydata(), xy):
                                raise WorkbenchError("冻结对象与实际渲染路径不一致。", 409, "object_changed")
                            owned.append(artist)
                    elif kind == "point":
                        owned.append(next(lines))
                    elif kind == "face":
                        owned.append(next(patches))
                    else:
                        raise WorkbenchError(f"未知冻结对象类型：{kind}")
                    styleable = kind in ("circular_arc", "segment", "polyline")
                    artists[oid] = owned
                    objects.append({"id": oid, "type": "curve" if styleable else kind, "kind": kind,
                        "role": item["role"], "styleable": styleable,
                        "source_call": {"scene_object": oid},
                        "geometry": {"paths": [xy.tolist() for xy in expected]},
                        "frozen_visibility": copy.deepcopy(item.get("intervals", item.get("visibility"))),
                        "artist_count": len(owned)})
                # Dimensions and labels stay on the original figure and are
                # deliberately not exposed as editable geometry.
                return Scene(fig, ax, objects, artists, self.snap_points(qid), renderer.render_settings(protocol))
            except Exception:
                plt.close(fig)
                raise

    def inspect_question(self, qid):
        with RENDER_LOCK:
            scene = self.scene(qid)
            try:
                _, digest = scene_png(scene)
                original_digest = pixel_hash(self.original_paths[qid])
                if digest != original_digest:
                    raise WorkbenchError(f"{qid} 无操作重绘与原图像素不同；保留原图并停止。", 409, "baseline_mismatch")
                scene.fig.canvas.draw()
                width, height = scene.fig.canvas.get_width_height()
                transform = np.array([[1, 0, 0], [0, -1, height], [0, 0, 1]]) @ scene.ax.transData.get_affine().get_matrix()
                return {"original_pixel_sha256": original_digest, "objects": scene.objects,
                        "snap_points": scene.snap_points,
                        "canvas": {"width": width, "height": height, "data_to_pixel": transform.tolist(),
                                   "pixel_to_data": np.linalg.inv(transform).tolist(),
                                   "coordinate_system": "frozen_projected_2d"},
                        "xlim": list(scene.ax.get_xlim()), "ylim": list(scene.ax.get_ylim())}
            finally:
                scene.close()

    def highlight(self, qid, oid):
        with RENDER_LOCK:
            scene = self.scene(qid)
            try:
                obj = next((o for o in scene.objects if o["id"] == oid), None)
                if not obj or not obj["styleable"]:
                    raise WorkbenchError("请选择可修改的原始棱线或轮廓。")
                for artist in scene.artists[oid]:
                    artist.set_color("#06B6D4")
                    artist.set_linewidth(3)
                scene.fig.text(.02, .98, f"REFERENCE ONLY: {qid} / {oid}", color="#06B6D4", fontsize=11, va="top")
                return scene_png(scene)[0]
            finally:
                scene.close()
