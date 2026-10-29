"""The existing Special actions on exact native MathVision artists."""
from __future__ import annotations

import copy
from pathlib import Path

import matplotlib as mpl
from matplotlib.collections import LineCollection
from matplotlib.patches import Patch

from mathvision_adapter import RendererAdapter, scene_png
from partial_style import apply_partial_styles
from render_plugins import PluginRenderer as LegacyPluginRenderer
from render_plugins import render_special_recipe as legacy_render_special_recipe
from renderer_adapter import RENDER_LOCK
from workbench_io import (GENERATOR_VERSION, ROOT, SCHEMA_VERSION, WorkbenchError, atomic_write,
                          canonical_hash, contained_path, environment_versions, file_hash,
                          load_config, protect_output_paths, renderer_fingerprint)


class PluginRenderer(LegacyPluginRenderer):
    def apply_actions(self, scene, plugin):
        if not getattr(scene, "native", False):
            return super().apply_actions(scene, plugin)
        partial_targets = apply_partial_styles(scene, plugin["params"]["actions"])
        additions = []
        for action in plugin["params"]["actions"]:
            if action["type"] != "set_object_style":
                additions.append(action)
                continue
            if action["target"] in partial_targets:
                continue
            owned = scene.artists.get(action["target"])
            if not owned:
                raise WorkbenchError("冻结参数的目标对象不存在。", 409, "object_changed")
            for artist in owned:
                if "color" in action:
                    # Patch.set_color would also recolor its frozen face fill.
                    if isinstance(artist, Patch):
                        artist.set_edgecolor(action["color"])
                    else:
                        artist.set_color(action["color"])
                # The protocol specifies dash lengths in points. Native figures
                # may have scale_dashes=True; changing width must preserve each
                # fragment's actual visible/hidden spacing and phase.
                dashes = copy.deepcopy(artist.get_linestyles() if isinstance(artist, LineCollection)
                                       else getattr(artist, "_dash_pattern", (0, None)))
                with mpl.rc_context({"lines.scale_dashes": False}):
                    if "linewidth_pt" in action:
                        artist.set_linewidth(action["linewidth_pt"])
                        if "linestyle" not in action:
                            artist.set_linestyle(dashes)
                    if "linestyle" in action:
                        artist.set_linestyle((0, [3.7, 1.6]) if action["linestyle"] == "dashed" else "solid")
        if additions:
            super().apply_actions(scene, {**plugin, "params": {"actions": additions}})

    def render(self, plugin, frozen=False):
        if not self.adapter.is_mathvision(plugin["question_id"]):
            return super().render(plugin, frozen=frozen)
        plugin = self.normalize(plugin)
        qid = plugin["question_id"]
        with RENDER_LOCK:
            scene = self.adapter.scene(qid)
            try:
                _, original_digest = scene_png(scene)
                if original_digest != self.metadata[qid]["original_pixel_sha256"]:
                    raise WorkbenchError(f"{qid} 原场景已改变。", 409, "baseline_mismatch")
                with mpl.rc_context(scene.settings):
                    self.apply_actions(scene, plugin)
                data, digest = scene_png(scene)
                if digest == original_digest:
                    raise WorkbenchError("候选没有实际像素变化：标记可能全在视窗外、被遮挡或样式相同。", code="no_visual_change")
                return plugin, data, digest
            finally:
                scene.close()


def render_special_recipe(recipe, output_path=None, config_path=None):
    """Strict native replay; the legacy implementation stays byte-for-byte frozen."""
    config = load_config(config_path)
    protect_output_paths(config)
    adapter = RendererAdapter(config)
    qid = recipe["question_id"]
    if not adapter.is_mathvision(qid):
        # replay_archived supplies the legacy adapter's matching global baseline.
        return legacy_render_special_recipe(recipe, output_path, config_path)
    if (recipe.get("generator_version") != GENERATOR_VERSION or
            recipe.get("plugin_schema_version") != SCHEMA_VERSION or recipe.get("status") != "passed"):
        raise WorkbenchError("recipe 不是当前版本的人工作品；拒绝跨版本重绘。", 409, "version_mismatch")
    if recipe.get("environment") != environment_versions():
        raise WorkbenchError("重绘依赖版本与通过时不同。", 409, "environment_changed")
    if (recipe.get("renderer_sha256") != renderer_fingerprint() or
            recipe.get("schema_sha256") != file_hash(ROOT / "plugin.schema.json")):
        raise WorkbenchError("重绘执行器或 schema 文件与通过时不同。", 409, "renderer_changed")
    if adapter.manifest["fingerprint"] != recipe["baseline_fingerprint"]:
        raise WorkbenchError("重绘输入基线不一致。", 409, "baseline_changed")
    plugin = {key: copy.deepcopy(recipe[key]) for key in (
        "plugin_schema_version", "question_id", "category", "operation", "description", "intent", "params")}
    if canonical_hash(plugin) != recipe["parameter_key"]:
        raise WorkbenchError("recipe 参数与冻结哈希不符。", 409, "integrity_error")
    renderer = PluginRenderer(config, adapter, {qid: adapter.inspect_question(qid)})
    _, data, digest = renderer.render(plugin, frozen=True)
    if digest != recipe["pixel_sha256"]:
        raise WorkbenchError("重绘像素不等于已通过图；没有写入输出。", 409, "reproduction_mismatch")
    target = Path(output_path).resolve() if output_path else contained_path(
        Path(config["runtime_dir"]) / "reproduced", f"{qid}/{recipe['slot_id']}.png")
    protected = [Path(config[k]).resolve() for k in ("original_image_dir", "question_class_dir", "output_dir")]
    protected.append(Path(config["dataset_root"]) / "base_variant")
    if any(target.is_relative_to(p) for p in protected) or target in adapter.input_files.values():
        raise WorkbenchError("重绘不能覆盖只读输入、A/B 或正式 C 文件。", code="unsafe_path")
    runtime = Path(config["runtime_dir"])
    if (target.suffix.lower() != ".png" or
            target.is_relative_to(runtime) and not target.is_relative_to(runtime / "reproduced") or
            target.is_relative_to(ROOT) and not target.is_relative_to(ROOT / "reproduced")):
        raise WorkbenchError("重绘须写入 PNG，且不能覆盖工作台程序、状态、草稿或候选。", code="unsafe_path")
    atomic_write(target, data)
    return {"image_path": str(target), "pixel_sha256": digest, "matches_accepted": True}
