"""Replay saved C recipes independently of edits to other questions."""
from __future__ import annotations

import copy
from pathlib import Path

from mathvision_adapter import RendererAdapter
from renderer_adapter import RendererAdapter as LegacyAdapter
from mathvision_plugins import render_special_recipe as _render_native
from render_plugins import render_special_recipe as _render_legacy
from workbench_io import (WorkbenchError, canonical_hash, contained_path, load_config,
                          parse_json, read_json)


def render_special_recipe(recipe, output_path=None, config_path=None):
    config = load_config(config_path)
    # Select from the formal source record, preserving the old manifest and
    # executor for legacy rows even when new native runtimes are present.
    records = (parse_json(line) for line in Path(config["dataset_file"]).read_text(
        encoding="utf-8-sig").splitlines() if line.strip())
    record = next((row for row in records if row["id"] == recipe["question_id"]), None)
    if record is None:
        raise WorkbenchError("不存在此立体题号。")
    native = record.get("source_dataset") == "MathVision"
    adapter = RendererAdapter(config) if native else LegacyAdapter(config)
    current = adapter.manifest
    recipe = copy.deepcopy(recipe)
    if current["fingerprint"] != recipe["baseline_fingerprint"]:
        archive = contained_path(Path(config["output_dir"]),
                                 f"_baselines/{recipe['baseline_fingerprint']}.json")
        if not archive.is_file():
            raise WorkbenchError("缺少这份已保存变体的输入基线记录。", 409, "baseline_missing")
        original = read_json(archive)
        qid = recipe["question_id"]
        dependencies = adapter.question_dependencies(qid)
        if (original.get("fingerprint") != recipe["baseline_fingerprint"] or
                canonical_hash({"files": original["files"], "environment": original["environment"]}) != original["fingerprint"] or any(
                original["files"].get(name) != current["files"].get(name) for name in dependencies)):
            raise WorkbenchError("这道题本身的绘图输入已改变，不能按旧参数重绘。", 409, "baseline_changed")
        # The original immutable recipe stays intact. The renderer still verifies
        # schema, environment, parameters and exact saved pixels before writing.
        recipe["baseline_fingerprint"] = current["fingerprint"]
    if native:
        return _render_native(recipe, output_path, config_path)
    return _render_legacy(recipe, output_path, config_path)
