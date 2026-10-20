"""Schema validation, frozen C actions and offline deterministic redraw."""
from __future__ import annotations

import copy
import math
import re
from pathlib import Path

from matplotlib.patches import Patch
from partial_style import apply_partial_styles, object_paths, validate_interval
from workbench_io import compatible_style_renderer

from renderer_adapter import RENDER_LOCK, RendererAdapter, scene_png
from workbench_io import (GENERATOR_VERSION, ROOT, SCHEMA_VERSION, WorkbenchError, atomic_write,
                          canonical_hash, contained_path, environment_versions, file_hash,
                          load_config, protect_output_paths, read_json, renderer_fingerprint)


def check_schema(value, rule, schema, path="plugin"):
    """Validate the exact keyword subset used by the bundled JSON Schema.

    No remote schema loading or executable expressions. Booleans are not numbers;
    every numeric value must be finite, including JSON numeric overflow.
    """
    if "$ref" in rule:
        return check_schema(value, schema["$defs"][rule["$ref"].split("/")[-1]], schema, path)
    if "oneOf" in rule:
        matches, errors = 0, []
        for option in rule["oneOf"]:
            try:
                check_schema(value, option, schema, path)
                matches += 1
            except WorkbenchError as error:
                errors.append(str(error))
        if matches != 1:
            action_type = value.get("type") if isinstance(value, dict) else None
            supported = ("add_point", "add_line", "set_object_style")
            if action_type in supported:
                return check_schema(value, schema["$defs"][action_type], schema, path)
            raise WorkbenchError(f"{path}.type：未知动作 {action_type!r}；支持 {', '.join(supported)}。")
        return
    typ = rule.get("type")
    try:
        finite_number = type(value) in (int, float) and math.isfinite(value)
    except OverflowError:
        finite_number = False
    valid = {"object": isinstance(value, dict), "array": isinstance(value, list),
             "string": isinstance(value, str), "boolean": type(value) is bool,
             "number": finite_number}
    if typ and not valid.get(typ, False):
        raise WorkbenchError(f"{path}：需要 {typ}，数值必须有限。")
    if "const" in rule and (type(value) is not type(rule["const"]) or value != rule["const"]):
        raise WorkbenchError(f"{path}：必须为 {rule['const']!r}。")
    if "enum" in rule and value not in rule["enum"]:
        raise WorkbenchError(f"{path}：允许值为 {rule['enum']}。")
    if typ == "object":
        missing = set(rule.get("required", [])) - value.keys()
        extra = value.keys() - rule.get("properties", {}).keys()
        if missing:
            raise WorkbenchError(f"{path}：缺少字段 {', '.join(sorted(missing))}。")
        if extra and rule.get("additionalProperties") is False:
            raise WorkbenchError(f"{path}：不允许字段 {', '.join(sorted(extra))}。")
        for key, item in value.items():
            if key in rule.get("properties", {}):
                check_schema(item, rule["properties"][key], schema, f"{path}.{key}")
    elif typ == "array":
        if not rule.get("minItems", 0) <= len(value) <= rule.get("maxItems", math.inf):
            raise WorkbenchError(f"{path}：数组长度须在 {rule.get('minItems', 0)}～{rule.get('maxItems', '∞')}。")
        for index, item in enumerate(value):
            check_schema(item, rule["items"], schema, f"{path}[{index}]")
    elif typ == "string":
        if not rule.get("minLength", 0) <= len(value) <= rule.get("maxLength", math.inf):
            raise WorkbenchError(f"{path}：文字长度不符合要求。")
        if "pattern" in rule and re.search(rule["pattern"], value) is None:
            raise WorkbenchError(f"{path}：格式不符合 {rule['pattern']}。")
    elif typ == "number":
        if value < rule.get("minimum", -math.inf) or value > rule.get("maximum", math.inf):
            raise WorkbenchError(f"{path}：数值超出允许范围。")
        if "exclusiveMinimum" in rule and value <= rule["exclusiveMinimum"]:
            raise WorkbenchError(f"{path}：必须大于 {rule['exclusiveMinimum']}。")


class PluginRenderer:
    def __init__(self, config, adapter, metadata):
        self.config, self.adapter, self.metadata = config, adapter, metadata
        self.schema = read_json(ROOT / "plugin.schema.json")
        self.interval_paths = {}

    def normalize(self, plugin):
        check_schema(plugin, self.schema, self.schema)
        qid = plugin["question_id"]
        if qid not in self.metadata:
            raise WorkbenchError(f"不存在题目 {qid}。")
        objects = {obj["id"]: obj for obj in self.metadata[qid]["objects"]}
        used = set(objects)
        normalized = copy.deepcopy(plugin)
        normalized.setdefault("description", "")
        normalized.setdefault("intent", "")
        for index, action in enumerate(normalized["params"]["actions"]):
            action_type = action["type"]
            for key, value in self.config["defaults"][action_type].items():
                if action_type == "add_line" and key == "dash_pattern_pt" and action.get("linestyle") == "solid":
                    continue
                action.setdefault(key, copy.deepcopy(value))
            if action_type == "set_object_style":
                target = objects.get(action["target"])
                if not target or not target.get("styleable"):
                    raise WorkbenchError(f"actions[{index}].target：{action['target']} 不是可修改的原曲线/轮廓。")
                if not any(key in action for key in ("color", "linestyle", "linewidth_pt")):
                    raise WorkbenchError("原对象样式操作至少需要 color、linestyle 或 linewidth_pt。")
                if "interval" in action:
                    key = (qid, action["target"])
                    if key not in self.interval_paths:
                        with RENDER_LOCK:
                            scene = self.adapter.scene(qid)
                            try:
                                scene.fig.canvas.draw()
                                self.interval_paths[key] = [{k: p[k] for k in ("id", "sha256", "closed")}
                                                            for p in object_paths(scene, action["target"])]
                            finally:
                                scene.close()
                    validate_interval(action["interval"], self.interval_paths[key])
            else:
                if action["id"] in used:
                    raise WorkbenchError(f"actions[{index}].id：{action['id']} 与原对象或已有动作冲突。")
                used.add(action["id"])
            coordinates = ([action["xy"]] if action_type == "add_point" else
                           action["endpoints"] if action_type == "add_line" else [])
            bounds = self.metadata[qid]
            for xy in coordinates:
                if not (bounds["xlim"][0] <= xy[0] <= bounds["xlim"][1] and
                        bounds["ylim"][0] <= xy[1] <= bounds["ylim"][1]):
                    raise WorkbenchError("新增标记坐标必须位于冻结绘图视窗内。")
            if action_type == "add_line":
                if action["endpoints"][0] == action["endpoints"][1]:
                    raise WorkbenchError(f"actions[{index}]：线段端点不能相同。")
                if "dash_pattern_pt" in action:
                    if action["linestyle"] != "dashed" or len(action["dash_pattern_pt"]) % 2:
                        raise WorkbenchError(f"actions[{index}]：dash_pattern_pt 需偶数个长度且 linestyle=dashed。")
                elif action["linestyle"] == "dashed":
                    action["dash_pattern_pt"] = [3.7, 1.6]
            if "color" in action:
                action["color"] = action["color"].upper()
        check_schema(normalized, self.schema, self.schema)
        return normalized

    def appearance_changes(self, plugin):
        """Keep rendered line-style changes distinct from frozen visibility."""
        overrides = [{"target": a["target"], "rendered_linestyle": a["linestyle"],
                      **({"interval": copy.deepcopy(a["interval"])} if "interval" in a else {})}
                     for a in plugin["params"]["actions"]
                     if a["type"] == "set_object_style" and "linestyle" in a]
        return {"world_geometry_changed": False, "projection_changed": False,
                "frozen_visibility_intervals_changed": False,
                "rendered_visibility_style_overrides": overrides,
                "rendered_line_styles_changed": bool(overrides)}

    def apply_actions(self, scene, plugin):
        partial_targets = apply_partial_styles(scene, plugin["params"]["actions"])
        for action in plugin["params"]["actions"]:
            if action["type"] == "set_object_style" and action["target"] in partial_targets:
                continue
            typ = action["type"]
            if typ == "set_object_style":
                owned = scene.artists.get(action["target"])
                if not owned:
                    raise WorkbenchError("冻结参数的目标对象不存在。", 409, "object_changed")
                for artist in owned:
                    if "linewidth_pt" in action:
                        artist.set_linewidth(action["linewidth_pt"])
                    if "color" in action:
                        artist.set_color(action["color"])
                    # Color-only overrides preserve each visible/hidden fragment.
                    if "linestyle" in action:
                        artist.set_linestyle((0, [3.7, 1.6]) if action["linestyle"] == "dashed" else "solid")
            elif typ == "add_point":
                scene.ax.scatter(*action["xy"], s=50, marker="o", facecolors=action["color"],
                                 edgecolors=action["color"], linewidths=1, zorder=10, clip_on=True)
            elif typ == "add_line":
                a, b = action["endpoints"]
                scene.ax.plot([a[0], b[0]], [a[1], b[1]], color=action["color"], linewidth=1,
                              marker=None, linestyle=(0, [3.7, 1.6]) if action["linestyle"] == "dashed" else "solid",
                              solid_capstyle="butt",
                              dash_capstyle="butt", zorder=9, clip_on=True)

    def render(self, plugin, frozen=False):
        # Even archived/frozen recipes must obey current semantic validation.
        plugin = self.normalize(plugin)
        qid = plugin["question_id"]
        with RENDER_LOCK:
            scene = self.adapter.scene(qid)
            try:
                _, original_digest = scene_png(scene)
                if original_digest != self.metadata[qid]["original_pixel_sha256"]:
                    raise WorkbenchError(f"{qid} 原场景已改变。", 409, "baseline_mismatch")
                import matplotlib as mpl
                with mpl.rc_context(scene.settings):
                    self.apply_actions(scene, plugin)
                data, digest = scene_png(scene)
                if digest == original_digest:
                    raise WorkbenchError("候选没有实际像素变化：标记可能全在视窗外、被遮挡或样式相同。", code="no_visual_change")
                return plugin, data, digest
            finally:
                scene.close()


def render_special_recipe(recipe, output_path=None, config_path=None):
    """Offline redraw from a reviewed, frozen recipe; never consult drafts."""
    config = load_config(config_path)
    protect_output_paths(config)
    if (recipe.get("generator_version") != GENERATOR_VERSION or
            recipe.get("plugin_schema_version") != SCHEMA_VERSION or recipe.get("status") != "passed"):
        raise WorkbenchError("recipe 不是当前版本的人工作品；拒绝跨版本重绘。", 409, "version_mismatch")
    if recipe.get("environment") != environment_versions():
        raise WorkbenchError("重绘依赖版本与通过时不同。", 409, "environment_changed")
    if (recipe.get("renderer_sha256") != renderer_fingerprint() or
            recipe.get("schema_sha256") != file_hash(ROOT / "plugin.schema.json")):
        if (not compatible_style_renderer(recipe) or any(
                "interval" in a or a["type"] == "set_object_style" and "linewidth_pt" in a
                for a in recipe["params"]["actions"])):
            raise WorkbenchError("重绘执行器或 schema 文件与通过时不同。", 409, "renderer_changed")
    adapter = RendererAdapter(config)
    if adapter.manifest["fingerprint"] != recipe["baseline_fingerprint"]:
        raise WorkbenchError("重绘输入基线不一致。", 409, "baseline_changed")
    plugin = {key: copy.deepcopy(recipe[key]) for key in (
        "plugin_schema_version", "question_id", "category", "operation", "description", "intent", "params")}
    if canonical_hash(plugin) != recipe["parameter_key"]:
        raise WorkbenchError("recipe 参数与冻结哈希不符。", 409, "integrity_error")
    metadata = {recipe["question_id"]: adapter.inspect_question(recipe["question_id"])}
    renderer = PluginRenderer(config, adapter, metadata)
    _, data, digest = renderer.render(plugin, frozen=True)
    if digest != recipe["pixel_sha256"]:
        raise WorkbenchError("重绘像素不等于已通过图；没有写入输出。", 409, "reproduction_mismatch")
    target = Path(output_path).resolve() if output_path else contained_path(
        Path(config["runtime_dir"]) / "reproduced", f"{recipe['question_id']}/{recipe['slot_id']}.png")
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
