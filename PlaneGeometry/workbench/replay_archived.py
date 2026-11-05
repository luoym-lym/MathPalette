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
    from dataset_tools.source_labels import compatible_record_hash
    qid = recipe.get('question_id')
    if qid in adapter.records and compatible_record_hash('PlaneGeometry', recipe.get('question_record_sha256'), adapter.records[qid]):
        recipe = {**recipe, 'question_record_sha256': canonical_hash(adapter.records[qid])}
    from extensions95_adapter import is_extensions95_record
    if is_extensions95_record(adapter.records.get(recipe.get("question_id"))):
        from extensions95_replay import render_special_recipe as render_extensions95
        return render_extensions95(recipe, output_path, config_path)
    from expand24_adapter import is_expand24_record
    if is_expand24_record(adapter.records.get(recipe.get("question_id"))):
        from expand24_replay import render_special_recipe as render_expand24
        return render_expand24(recipe, output_path, config_path)
    from author_adapter import is_author_record
    if is_author_record(adapter.records.get(recipe.get("question_id"))):
        from author_replay import render_special_recipe as render_author
        return render_author(recipe, output_path, config_path)
    if adapter.records.get(recipe.get("question_id"), {}).get("source_dataset") == "MathVision":
        from mathvision_replay import render_special_recipe as render_native
        return render_native(recipe, output_path, config_path)
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
        from workflow_compatibility import compatible_workflow_input
        if (original.get("fingerprint") != recipe["baseline_fingerprint"] or
                canonical_hash({"files": original["files"], "environment": original["environment"]}) != original["fingerprint"] or any(
                not compatible_workflow_input(name, original["files"].get(name), current["files"].get(name)) for name in dependencies)):
            raise WorkbenchError("这道题本身的绘图输入已改变，不能按旧参数重绘。", 409, "baseline_changed")
        # The original immutable recipe stays intact. The renderer still verifies
        # schema, environment, parameters and exact saved pixels before writing.
        recipe["baseline_fingerprint"] = current["fingerprint"]
    return _render(recipe, output_path, config_path)
