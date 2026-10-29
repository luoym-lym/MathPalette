"""Read-only MathVision dispatch, preserving the legacy Plane adapter."""
from __future__ import annotations

from matplotlib.patches import Patch

from renderer_adapter import RENDER_LOCK, RendererAdapter as LegacyRendererAdapter
from workbench_io import ROOT, WorkbenchError, pixel_hash


class RendererAdapter(LegacyRendererAdapter):
    """Extend the input manifest only for native MathVision execution."""

    def __init__(self, config, expected_manifest=None):
        super().__init__(config)
        # These are executable inputs to native scene capture, rendering, and
        # replay. Legacy recipe dependencies intentionally remain unchanged.
        self.native_dependencies = {
            "mathvision_workbench.py": self.project / "dataset_tools/mathvision_workbench.py",
            **{f"workbench/{name}": ROOT / name for name in (
                "mathvision_adapter.py", "mathvision_plugins.py", "mathvision_replay.py",
                "replay_archived.py", "review_store.py", "drawing_board.py")},
        }
        self.input_files.update(self.native_dependencies)
        self.manifest = self.make_manifest()
        if expected_manifest and self.manifest != expected_manifest:
            raise WorkbenchError("输入基线或依赖版本变化；请恢复已审核环境。", 409, "baseline_changed")

    def is_native(self, qid):
        return isinstance(qid, str) and self.records.get(qid, {}).get("source_dataset") == "MathVision"

    def dependencies(self, qid):
        dependencies = super().dependencies(qid)
        return dependencies + tuple(self.native_dependencies) if self.is_native(qid) else dependencies

    def scene(self, qid):
        if not self.is_native(qid):
            return super().scene(qid)
        from dataset_tools.mathvision_workbench import build_scene
        with RENDER_LOCK:
            return build_scene(self.branch_root, self.records[qid])

    def inspect_question(self, qid):
        if not self.is_native(qid):
            return super().inspect_question(qid)
        from dataset_tools.mathvision_workbench import png_bytes
        from drawing_board import describe_captured_scene
        with RENDER_LOCK:
            scene = self.scene(qid)
            try:
                digest = pixel_hash(png_bytes(scene))
                original_digest = pixel_hash(self.original_paths[qid])
                if digest != original_digest:
                    raise WorkbenchError(f"{qid} 无操作重绘与原图像素不同；保留原图并停止。",
                                         409, "baseline_mismatch")
                return {"original_pixel_sha256": original_digest, "objects": scene.objects,
                        "snap_points": scene.snap_points, "canvas": describe_captured_scene(scene, qid)}
            finally:
                scene.close()

    def highlight(self, qid, oid):
        if not self.is_native(qid):
            return super().highlight(qid, oid)
        from dataset_tools.mathvision_workbench import png_bytes
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
                scene.fig.text(.02, .98, f"REFERENCE ONLY: {qid} / {oid}", color="#E11D48",
                               fontsize=11, va="top")
                return png_bytes(scene)
            finally:
                scene.close()
