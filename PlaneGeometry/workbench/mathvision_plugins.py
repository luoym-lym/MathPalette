"""Apply the unchanged Special schema to captured native MathVision scenes."""
from __future__ import annotations

import copy

import matplotlib as mpl
from matplotlib.collections import LineCollection
from matplotlib.patches import Patch

from partial_style import apply_partial_styles
from render_plugins import PluginRenderer as LegacyPluginRenderer, check_schema
from renderer_adapter import RENDER_LOCK
from workbench_io import WorkbenchError, pixel_hash


def _set_linewidth_preserving_dashes(artist, width):
    """Linewidth overrides keep existing dash lengths and offsets in points."""
    if isinstance(artist, LineCollection):
        patterns = copy.deepcopy(artist.get_linestyles())
    else:
        pattern = copy.deepcopy(getattr(artist, "_dash_pattern", None))
        patterns = [pattern] if pattern is not None and pattern[1] is not None else None
    with mpl.rc_context({"lines.scale_dashes": False}):
        artist.set_linewidth(width)
        if patterns is not None:
            artist.set_linestyle(patterns if isinstance(artist, LineCollection) else patterns[0])


class PluginRenderer(LegacyPluginRenderer):
    def render(self, plugin, frozen=False):
        if not self.adapter.is_native(plugin.get("question_id") if isinstance(plugin, dict) else None):
            return super().render(plugin, frozen=frozen)
        # Reuse the exact schema, defaults, target validation, path fingerprints,
        # and fixed action sizes of the existing Plane Special implementation.
        normalized = self.normalize(plugin)
        if frozen and normalized != plugin:
            raise WorkbenchError("冻结插件缺少规范化参数。", 409, "integrity_error")
        plugin = normalized
        check_schema(plugin, self.schema, self.schema)
        qid = plugin["question_id"]
        from dataset_tools.mathvision_workbench import png_bytes
        with RENDER_LOCK:
            scene = self.adapter.scene(qid)
            try:
                original_digest = pixel_hash(png_bytes(scene))
                if original_digest != self.metadata[qid]["original_pixel_sha256"]:
                    raise WorkbenchError(f"{qid} 原场景已改变。", 409, "baseline_mismatch")
                partial_targets = apply_partial_styles(scene, plugin["params"]["actions"])
                for action in plugin["params"]["actions"]:
                    typ = action["type"]
                    if typ == "set_object_style":
                        if action["target"] in partial_targets:
                            continue
                        artists = scene.artists.get(action["target"])
                        if not artists:
                            raise WorkbenchError("冻结参数的目标对象不存在。", 409, "object_changed")
                        for artist in artists:
                            if "linewidth_pt" in action:
                                _set_linewidth_preserving_dashes(artist, action["linewidth_pt"])
                            if "color" in action:
                                if isinstance(artist, Patch):
                                    artist.set_edgecolor(action["color"])
                                else:
                                    artist.set_color(action["color"])
                            if "linestyle" in action:
                                with mpl.rc_context({"lines.scale_dashes": False}):
                                    artist.set_linestyle((0, [3.7, 1.6])
                                                         if action["linestyle"] == "dashed" else "-")
                    elif typ == "add_point":
                        scene.ax.scatter(*action["xy"], s=action["size_pt2"], marker="o",
                                         facecolors=action["color"] if action["filled"] else "#FFFFFF",
                                         edgecolors=action["color"], linewidths=action["edge_linewidth_pt"],
                                         zorder=10, clip_on=True)
                    elif typ == "add_line":
                        a, b = action["endpoints"]
                        line, = scene.ax.plot([a[0], b[0]], [a[1], b[1]], color=action["color"],
                                              linewidth=action["linewidth_pt"], marker=None,
                                              linestyle="--" if action["linestyle"] == "dashed" else "-",
                                              solid_capstyle="butt", dash_capstyle="butt",
                                              zorder=9, clip_on=True)
                        if "dash_pattern_pt" in action:
                            with mpl.rc_context({"lines.scale_dashes": False}):
                                line.set_linestyle((0, action["dash_pattern_pt"]))
                # Keep native serialization settings; never rerun the original
                # finalizer after adding Special marks to the frozen viewport.
                data = png_bytes(scene)
                digest = pixel_hash(data)
                if digest == original_digest:
                    raise WorkbenchError("候选没有实际像素变化：标记可能全在视窗外、被遮挡或样式相同。",
                                         code="no_visual_change")
                return plugin, data, digest
            finally:
                scene.close()
