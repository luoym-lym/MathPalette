"""Dispatch imported MathVision rows to their unchanged native renderers."""
from __future__ import annotations

import io
from pathlib import Path

import numpy as np
from matplotlib.patches import Patch
from PIL import Image

from renderer_adapter import (RENDER_LOCK, RendererAdapter as LegacyAdapter,
                              scene_png as legacy_scene_png)
from workbench_io import WorkbenchError, pixel_hash


def scene_png(scene):
    if not getattr(scene, "native", False):
        return legacy_scene_png(scene)
    from dataset_tools.mathvision_workbench import png_bytes
    data = png_bytes(scene)
    with Image.open(io.BytesIO(data)) as image:
        if image.size != (768, 768) or image.convert("RGBA").getextrema()[3] != (255, 255):
            raise WorkbenchError("渲染必须产生不透明的 768×768 PNG。", code="invalid_render")
        return data, pixel_hash(image)


class RendererAdapter(LegacyAdapter):
    def is_mathvision(self, qid):
        return self.records.get(qid, {}).get("source_dataset") == "MathVision"

    def native_dependencies(self, qid):
        return (*self.records[qid].get("runtime_dependencies", ()),
                "../dataset_tools/mathvision_workbench.py",
                "workbench/mathvision_adapter.py", "workbench/mathvision_plugins.py",
                "workbench/replay_archived.py", "workbench/drawing_board.py")

    def make_manifest(self):
        # LegacyAdapter calls this once while constructing its original inputs.
        # Add only native dependencies; legacy question_dependencies stays exact.
        branch = Path(self.config["dataset_file"]).resolve().parent
        for qid in self.records:
            if self.is_mathvision(qid):
                for name in self.native_dependencies(qid):
                    self.input_files[name] = (branch / name).resolve()
        return super().make_manifest()

    def question_dependencies(self, qid):
        original = super().question_dependencies(qid)
        return (*original, *self.native_dependencies(qid)) if self.is_mathvision(qid) else original

    def scene(self, qid):
        if qid not in self.records:
            raise WorkbenchError("不存在此立体题号。")
        if not self.is_mathvision(qid):
            return super().scene(qid)
        from dataset_tools.mathvision_workbench import build_scene
        with RENDER_LOCK:
            return build_scene(Path(self.config["dataset_file"]).resolve().parent, self.records[qid])

    def inspect_question(self, qid):
        if not self.is_mathvision(qid):
            return super().inspect_question(qid)
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
        if not self.is_mathvision(qid):
            return super().highlight(qid, oid)
        with RENDER_LOCK:
            scene = self.scene(qid)
            try:
                obj = next((o for o in scene.objects if o["id"] == oid), None)
                if not obj or not obj["styleable"]:
                    raise WorkbenchError("请选择可修改的原始棱线或轮廓。")
                for artist in scene.artists[oid]:
                    if isinstance(artist, Patch):
                        artist.set_edgecolor("#06B6D4")
                    else:
                        artist.set_color("#06B6D4")
                    artist.set_linewidth(3)
                scene.fig.text(.02, .98, f"REFERENCE ONLY: {qid} / {oid}", color="#06B6D4", fontsize=11, va="top")
                return scene_png(scene)[0]
            finally:
                scene.close()
