"""Strict native MathVision replay with per-question executable input hashes."""
from __future__ import annotations

import copy
from pathlib import Path

from mathvision_adapter import RendererAdapter
from mathvision_plugins import PluginRenderer
from workbench_io import (GENERATOR_VERSION, ROOT, SCHEMA_VERSION, WorkbenchError, atomic_write,
                          canonical_hash, contained_path, environment_versions, file_hash,
                          load_config, protect_output_paths, read_json, renderer_fingerprint)


def render_special_recipe(recipe, output_path=None, config_path=None):
    config = load_config(config_path)
    protect_output_paths(config)
    if (recipe.get("generator_version") != GENERATOR_VERSION or
            recipe.get("plugin_schema_version") != SCHEMA_VERSION or recipe.get("status") != "passed"):
        raise WorkbenchError("recipe 不是当前版本的人工作品；拒绝跨版本重绘。", 409, "version_mismatch")
    if recipe.get("environment") != environment_versions():
        raise WorkbenchError("重绘依赖版本与通过时不同。", 409, "environment_changed")
    # MathVision has no historical executor compatibility allowance. Extension
    # executable files are additionally checked in the native question baseline.
    if (recipe.get("renderer_sha256") != renderer_fingerprint() or
            recipe.get("schema_sha256") != file_hash(ROOT / "plugin.schema.json")):
        raise WorkbenchError("重绘执行器或 schema 文件与通过时不同。", 409, "renderer_changed")
    adapter = RendererAdapter(config)
    qid = recipe.get("question_id")
    if not adapter.is_native(qid) or recipe.get("question_record_sha256") != canonical_hash(adapter.records[qid]):
        raise WorkbenchError("本题正式记录与通过时不一致。", 409, "baseline_changed")
    current = adapter.manifest
    if current["fingerprint"] != recipe["baseline_fingerprint"]:
        archive = contained_path(Path(config["output_dir"]), f"_baselines/{recipe['baseline_fingerprint']}.json")
        if not archive.is_file():
            raise WorkbenchError("缺少这份已保存变体的输入基线记录。", 409, "baseline_missing")
        original = read_json(archive)
        if (original.get("fingerprint") != recipe["baseline_fingerprint"] or
                canonical_hash({"files": original["files"], "environment": original["environment"]}) != original["fingerprint"] or
                original["environment"] != current["environment"] or any(
                    original["files"].get(name) != current["files"].get(name)
                    for name in adapter.dependencies(qid))):
            raise WorkbenchError("这道题本身的绘图输入已改变，不能按旧参数重绘。", 409, "baseline_changed")
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
    protected = [Path(config[key]).resolve() for key in ("original_image_dir", "question_class_dir", "output_dir")]
    protected.append(Path(config["dataset_root"]) / "base_variant")
    if any(target.is_relative_to(path) for path in protected) or target in adapter.input_files.values():
        raise WorkbenchError("重绘不能覆盖只读输入、A/B 或正式 C 文件。", code="unsafe_path")
    runtime = Path(config["runtime_dir"])
    if (target.suffix.lower() != ".png" or
            target.is_relative_to(runtime) and not target.is_relative_to(runtime / "reproduced") or
            target.is_relative_to(ROOT) and not target.is_relative_to(ROOT / "reproduced")):
        raise WorkbenchError("重绘须写入 PNG，且不能覆盖工作台程序、状态、草稿或候选。", code="unsafe_path")
    atomic_write(target, data)
    return {"image_path": str(target), "pixel_sha256": digest, "matches_accepted": True}
