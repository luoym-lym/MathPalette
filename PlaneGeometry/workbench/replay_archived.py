"""Replay saved C recipes independently of edits to other questions."""
from __future__ import annotations

import copy
from pathlib import Path

from renderer_adapter import RendererAdapter
from render_plugins import render_special_recipe as _render
from workbench_io import (WorkbenchError, canonical_hash, contained_path, load_config,
                          read_json, renderer_fingerprint)


def render_special_recipe(recipe, output_path=None, config_path=None):
    config = load_config(config_path)
    adapter = RendererAdapter(config)
    current = adapter.manifest
    recipe = copy.deepcopy(recipe)
    current_renderer = renderer_fingerprint()
    if current["fingerprint"] != recipe["baseline_fingerprint"]:
        archive = contained_path(Path(config["output_dir"]),
                                 f"_baselines/{recipe['baseline_fingerprint']}.json")
        if not archive.is_file():
            raise WorkbenchError("缺少这份已保存变体的输入基线记录。", 409, "baseline_missing")
        original = read_json(archive)
        qid = recipe["question_id"]
        source_name = Path(adapter.sources[qid]["source_file"]).name
        dependencies = adapter.dependencies(qid)
        if (original.get("fingerprint") != recipe["baseline_fingerprint"] or
                canonical_hash({"files": original["files"], "environment": original["environment"]}) != original["fingerprint"] or any(
                original["files"].get(name) != current["files"].get(name) for name in dependencies)):
            raise WorkbenchError("这道题本身的绘图输入已改变，不能按旧参数重绘。", 409, "baseline_changed")
        # The original immutable recipe stays intact. The renderer still verifies
        # schema, environment, parameters and exact saved pixels before writing.
        recipe["baseline_fingerprint"] = current["fingerprint"]
    return _render(recipe, output_path, config_path)
