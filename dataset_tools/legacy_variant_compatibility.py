"""Explicit, fail-closed replay bridge for the pre-MathVerse executors.

The registry is a reviewed transition, not a list of hashes to ignore. It pins
both code and the complete dependencies/record of each eligible old question.
Updating executors requires a new explicit registration and pixel regression.
This module never changes recipes, approvals, or saved renderer fingerprints.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REGISTRY = Path(__file__).with_name("legacy_variant_compatibility.json")


def _hash(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, ensure_ascii=False,
                                    separators=(",", ":"), allow_nan=False).encode()).hexdigest()


def _transition(component, previous, current):
    try:
        registry = json.loads(REGISTRY.read_text(encoding="utf-8"))
        if registry.get("schema_version") != 1:
            return None
        entry = registry["transitions"][component]
        if previous != entry["previous_renderer_sha256"] or current != entry["current_renderer_sha256"]:
            return None
        for name, expected in entry["code_sha256"].items():
            path = (ROOT / name).resolve()
            if not path.is_relative_to(ROOT) or hashlib.sha256(path.read_bytes()).hexdigest() != expected:
                return None
        return entry
    except (OSError, ValueError, TypeError, KeyError):
        return None


def legacy_renderer_matches(component, previous, current, record, files):
    """Only registered legacy records may use one precisely tested transition."""
    entry = _transition(component, previous, current)
    if entry is None or record.get("runtime_dependencies") or record.get("renderer_family"):
        return False
    expected = entry["questions"].get(record.get("id"))
    return bool(expected and _hash(record) == expected["record_sha256"] and
                expected["dependencies"] and all(
                    name in files and files[name] == digest
                    for name, digest in expected["dependencies"].items()))


def legacy_progress_matches(component, previous, current, records, manifest, old_manifest, old_records):
    """Allow startup migration only with intact old state and every old input.

    The review store retains accepted recipes, collection history and candidate
    packages. Existing input-change logic still invalidates stale candidates.
    """
    if not isinstance(old_manifest, dict) or not isinstance(old_records, dict) or not old_records:
        return False
    try:
        entry = _transition(component, previous["renderer_sha256"], current["renderer_sha256"])
        if (entry is None or set(old_records) != set(entry["questions"]) or
                old_manifest["files"].get("dataset.jsonl") != entry["previous_dataset_sha256"] or
                any(old_manifest["files"].get(name) != digest
                    for question in entry["questions"].values()
                    for name, digest in question["dependencies"].items())):
            return False
        original = {"files": old_manifest["files"], "environment": old_manifest["environment"]}
        if (old_manifest["fingerprint"] != previous["baseline_fingerprint"] or
                _hash(original) != old_manifest["fingerprint"] or
                old_manifest["environment"] != manifest["environment"]):
            return False
        # The dataset may acquire new rows; old rows and all old files must stay.
        if any(name != "dataset.jsonl" and manifest["files"].get(name) != digest
               for name, digest in old_manifest["files"].items()):
            return False
        return all(qid in records and records[qid] == row and
                   legacy_renderer_matches(component, previous["renderer_sha256"],
                                           current["renderer_sha256"], row, manifest["files"])
                   for qid, row in old_records.items())
    except (ValueError, TypeError, KeyError):
        return False
