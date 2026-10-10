"""Evaluate the four generated Base variants of each dataset question once.

Run: python -B MathPalette/Analytics/val_script/evaluate_variants.py
Uses the original questions and answers, and shares the original evaluation protocol.
Full successful trajectories: trace_variants.json. Report: accuracy_variants.txt.
"""

from __future__ import annotations

import argparse
import base64
import json
import os
import sys
import threading
from concurrent.futures import CancelledError, ThreadPoolExecutor, as_completed
from pathlib import Path

from evaluate import (
    DATASET_ROOT, DEFAULT_ENV_FILE, JUDGE_PROMPT, MODEL, SOLVER_PROMPT, MiMo, RunLock, Trace,
    atomic_write, digest, evaluate_trial, load_dataset, load_key, now, remove_error_records,
)


SLOTS = tuple(f"base_{i}" for i in range(1, 5))


def load_variants(dataset):
    originals, _, dataset_hash = load_dataset(dataset)
    root = dataset.parent.resolve()
    variant_root = root / "base_variant"
    expected_dirs = {row["id"] for row in originals}
    actual_dirs = {path.name for path in variant_root.iterdir() if path.is_dir()}
    if actual_dirs != expected_dirs:
        raise ValueError("base_variant folders must match the dataset question IDs.")
    rows, images, recipe_hashes = [], {}, {}
    for original in originals:
        question_id = original["id"]
        folder = variant_root / question_id
        recipe_bytes = (folder / "recipes.json").read_bytes()
        recipes = json.loads(recipe_bytes.decode("utf-8-sig"))
        if not isinstance(recipes, list) or len(recipes) != len(SLOTS):
            raise ValueError(f"Expected four generated Base recipes: {question_id}")
        by_slot = {recipe.get("slot_id"): recipe for recipe in recipes}
        if set(by_slot) != set(SLOTS):
            raise ValueError(f"Missing or duplicate variant slot: {question_id}")
        actual_images = {path.name for path in (folder / "images").glob("*.png")}
        names = {f"{question_id}_base_variant_{i}" for i in range(1, 5)}
        if actual_images != {f"{name}.png" for name in names}:
            raise ValueError(f"Expected exactly four Base PNGs: {question_id}")
        if {p.name for p in (folder / "plugins").glob("*.json")} != {f"{name}.json" for name in names}:
            raise ValueError(f"Expected exactly four Base plugins: {question_id}")
        operations = {recipe.get("operation") for recipe in recipes}
        if len(operations) != 4 or not operations <= {f"Base{i}" for i in range(1, 7)}:
            raise ValueError(f"Expected four distinct Base operations: {question_id}")
        recipe_hashes[question_id] = digest(recipe_bytes)
        for slot in SLOTS:
            recipe = by_slot[slot]
            if (recipe.get("question_id") != question_id or recipe.get("status") != "generated"
                    or recipe.get("category") != "Base" or recipe.get("protocol_version") != "2.0.0"):
                raise ValueError(f"Variant recipe is not a matching Base recipe: {question_id}/{slot}")
            name = f"{question_id}_base_variant_{slot.split('_')[1]}"
            expected_image = f"base_variant/{question_id}/images/{name}.png"
            expected_plugin = f"base_variant/{question_id}/plugins/{name}.json"
            if recipe.get("image_path") != expected_image or recipe.get("plugin_path") != expected_plugin:
                raise ValueError(f"Unexpected Base artifact path: {question_id}/{slot}")
            image_path = (root / expected_image).resolve()
            if not image_path.is_relative_to(root) or not image_path.is_file():
                raise ValueError(f"Missing or invalid variant image: {question_id}/{slot}")
            content = image_path.read_bytes()
            if not content.startswith(b"\x89PNG\r\n\x1a\n"):
                raise ValueError(f"Expected a PNG variant: {question_id}/{slot}")
            plugin_path = (root / expected_plugin).resolve()
            if not plugin_path.is_relative_to(root):
                raise ValueError("Base plugin path escapes dataset.")
            plugin_bytes = plugin_path.read_bytes()
            plugin = json.loads(plugin_bytes.decode("utf-8-sig"))
            frozen = {key: recipe[key] for key in (
                "plugin_schema_version", "protocol_version", "question_id", "category", "operation", "params")}
            if (plugin != frozen or digest(plugin_bytes) != recipe.get("plugin_sha256") or
                    digest(content) != recipe.get("png_sha256")):
                raise ValueError(f"Base artifact integrity failure: {question_id}/{slot}")
            baseline = recipe["baseline"]
            if baseline["record"] != {key: original[key] for key in ("id", "question", "answer", "image")}:
                raise ValueError(f"Base question record changed: {question_id}")
            if slot == SLOTS[0]:
                for relative, expected_hash in baseline["files"].items():
                    source = (root / relative).resolve()
                    if not source.is_relative_to(root) or digest(source.read_bytes()) != expected_hash:
                        raise ValueError(f"Base original input changed: {relative}")
            variant_id = f"{question_id}_{slot}"
            rows.append({
                "id": variant_id, "question": original["question"], "answer": original["answer"],
                "image": image_path.relative_to(root).as_posix(), "image_sha256": digest(content),
                "variant_metadata": {
                    "original_question_id": question_id, "slot_id": slot,
                    "category": recipe["category"], "operation": recipe["operation"],
                    "candidate_id": recipe["candidate_id"],
                    "recipe_path": (folder / "recipes.json").relative_to(root).as_posix(),
                },
            })
            images[variant_id] = "data:image/png;base64," + base64.b64encode(content).decode("ascii")
    if len(rows) != len(originals) * 4 or len(images) != len(rows):
        raise ValueError("Expected exactly four unique variants per original question.")
    return rows, images, dataset_hash, recipe_hashes


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dataset", type=Path, default=DATASET_ROOT / "dataset.jsonl")
    parser.add_argument("--trace", type=Path, default=Path(__file__).with_name("trace_variants.json"))
    parser.add_argument("--report", type=Path, default=Path(__file__).with_name("accuracy_variants.txt"))
    parser.add_argument("--env-file", type=Path, default=DEFAULT_ENV_FILE)
    parser.add_argument("--base-url", default=os.environ.get("MIMO_BASE_URL", "https://token-plan-cn.xiaomimimo.com/v1"))
    parser.add_argument("--concurrency", type=int, default=5, help="One solver then one judge per worker; maximum five.")
    parser.add_argument("--rpm", type=int, default=90, help="Shared rolling 60-second limit, including judges and retries.")
    parser.add_argument("--timeout", type=float, default=300)
    parser.add_argument("--max-attempts", type=int, default=6)
    parser.add_argument("--answer-max-tokens", type=int, default=16384)
    parser.add_argument("--judge-max-tokens", type=int, default=128)
    args = parser.parse_args()
    if not 1 <= args.concurrency <= 5:
        parser.error("Concurrency must be between one and five.")
    if min(args.rpm, args.timeout, args.max_attempts, args.answer_max_tokens, args.judge_max_tokens) <= 0:
        parser.error("Rate, timeout, retry count, and token limits must be positive.")
    args.dataset, args.trace, args.report = (path.resolve() for path in (args.dataset, args.trace, args.report))
    if args.trace == args.report or args.dataset in (args.trace, args.report):
        parser.error("Dataset, trace, and report must be separate files.")
    key = load_key(args.env_file)
    rows, images, dataset_hash, recipe_hashes = load_variants(args.dataset)
    config = {
        "dataset_kind": "base_variants_v2", "original_questions": len(rows) // 4, "variants_per_original": 4,
        "model": MODEL, "base_url": args.base_url, "solver_thinking": "enabled",
        "judge_thinking": "disabled", "trials_per_question": 1,
        "numeric_relative_tolerance": 0.10, "zero_absolute_tolerance": 1e-8,
        "answer_max_tokens": args.answer_max_tokens, "judge_max_tokens": args.judge_max_tokens,
        "solver_system_prompt": SOLVER_PROMPT, "judge_system_prompt": JUDGE_PROMPT,
        "dataset": str(args.dataset), "dataset_sha256": dataset_hash,
        "recipes_sha256": recipe_hashes,
        "images_sha256": {row["id"]: row["image_sha256"] for row in rows},
    }
    signature = digest(json.dumps(config, ensure_ascii=False, sort_keys=True, allow_nan=False).encode("utf-8"))
    lock = RunLock(args.trace.with_suffix(".lock"))
    stop, trace = threading.Event(), None
    try:
        trace = Trace(args.trace, signature, config, rows)
        trace.data.setdefault("execution", {})["concurrency"] = args.concurrency
        trace.save()
        api = MiMo(args, key, trace, stop)
        failures = []
        # Each worker makes its solver and judge calls sequentially. There is no
        # nested executor, so all HTTP requests combined stay within the limit.
        with ThreadPoolExecutor(max_workers=args.concurrency, thread_name_prefix="variant") as executor:
            futures = {
                executor.submit(evaluate_trial, i, 0, row, images[row["id"]], api, trace): row["id"]
                for i, row in enumerate(rows)
                if trace.get_trial(i, 0)["status"] != "completed"
            }
            for future in as_completed(futures):
                try:
                    future.result()
                    with trace.lock:
                        completed = trace.data["summary"]["completed_trials"]
                    if completed % 10 == 0 or completed == len(rows):
                        print(f"Variants completed: {completed}/{len(rows)}", file=sys.stderr, flush=True)
                except CancelledError:
                    continue
                except Exception as error:
                    failures.append(f"{futures[future]}: {api.redact(str(error))}")
                    print(failures[-1], file=sys.stderr, flush=True)
                    if stop.is_set():
                        for pending in futures:
                            pending.cancel()
        if failures or trace.data["summary"]["completed_trials"] != len(rows):
            trace.data["status"] = "incomplete"
            trace.save()
            print("Evaluation incomplete; rerun the same command to resume. No final report was written.", file=sys.stderr)
            return 1
        trace.data["status"] = "completed"
        trace.data["completed_at"] = now()
        remove_error_records(trace.data)
        trace.save()
        number = f"{trace.data['summary']['mean_accuracy'] * 100:.2f}%"
        atomic_write(args.report, number + "\n")
        print(number, flush=True)
        return 0
    finally:
        stop.set()
        lock.close()


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (ValueError, OSError) as error:
        print(str(error), file=sys.stderr)
        raise SystemExit(1)
