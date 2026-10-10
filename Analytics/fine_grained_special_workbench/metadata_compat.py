"""Accept only the recorded, metadata-only source correction from 2026-10-09."""
from pathlib import Path

from workbench_io import file_hash, read_json


def _migration(config):
    folder = Path(config["dataset_root"]) / "provenance/source_metadata_20261009"
    path = folder / "migration.json"
    if not path.is_file():
        return folder, {}
    record = read_json(path)
    if record.get("kind") != "source_dataset_only" or record.get("version") != 1:
        return folder, {}
    return folder, record


def source_metadata_compatible(config, name, before, after):
    folder, record = _migration(config)
    entry = record.get("sources", {}).get(name)
    if not entry or before != entry["before_sha256"] or after != entry["after_sha256"]:
        return False
    filename = Path(name).name
    original = folder / "before/fine_grained_dataset/dataset_generator/dataset_generator" / filename
    current = Path(config["question_class_dir"]) / filename
    return (original.is_file() and current.is_file() and
            file_hash(original) == before and file_hash(current) == after)


def renderer_metadata_compatible(config, before, after):
    folder, record = _migration(config)
    entry = record.get("renderer", {})
    if not entry or before != entry["before_sha256"] or after != entry["after_sha256"]:
        return False
    original = folder / "before/fine_grained_special_workbench/renderer_adapter.py"
    current = Path(__file__).with_name("renderer_adapter.py")
    return (original.is_file() and file_hash(original) == entry["adapter_before_sha256"] and
            file_hash(current) == entry["adapter_after_sha256"])
