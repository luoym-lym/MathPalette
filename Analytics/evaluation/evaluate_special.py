"""Evaluate every accepted special variant once, with up to twenty concurrent requests.

Run: python -B MathPalette/Analytics/evaluation/evaluate_special.py
Uses the original questions and answers, and shares the original evaluation protocol.
Full successful trajectories: trace_special.json. Report: accuracy_special.txt.
"""

from __future__ import annotations

import argparse
import base64
import copy
import json
import os
import sys
import threading
from concurrent.futures import CancelledError, ThreadPoolExecutor, as_completed
from pathlib import Path

import evaluate
from evaluate import (
    DATASET_ROOT, DEFAULT_ENV_FILE, JUDGE_PROMPT, MODEL, SOLVER_PROMPT, MiMo, RunLock, Trace,
    atomic_write, digest, evaluate_trial, load_dataset, load_key, now, remove_error_records,
)


def load_special(dataset):
    originals, _, dataset_hash = load_dataset(dataset)
    root = dataset.parent.resolve()
    variant_root = root / "special_variant"
    rows, images, recipe_hashes = [], {}, {}
    for original in originals:
        question_id = original["id"]
        folder = variant_root / question_id
        if not folder.is_dir():
            continue  # A formal original may not have human-passed C variants yet.
        recipe_path = folder / "recipes.json"
        recipe_bytes = recipe_path.read_bytes()
        recipes = json.loads(recipe_bytes.decode("utf-8-sig"))
        if not isinstance(recipes, list) or not recipes:
            raise ValueError(f"Expected accepted special recipes: {question_id}")
        slots = [recipe.get("slot_id") for recipe in recipes]
        if len(slots) != len(set(slots)) or any(not isinstance(slot, str) or not slot.startswith("C") for slot in slots):
            raise ValueError(f"Missing, duplicate, or non-C variant slot: {question_id}")
        actual_images = {path.name for path in (folder / "images").glob("*.png")}
        if actual_images != {f"{slot}.png" for slot in slots}:
            raise ValueError(f"Special images do not match accepted recipes: {question_id}")
        recipe_hashes[question_id] = digest(recipe_bytes)
        for recipe in sorted(recipes, key=lambda item: item["slot_id"]):
            slot = recipe["slot_id"]
            if (recipe.get("question_id") != question_id or recipe.get("status") != "passed"
                    or recipe.get("category") != "C" or recipe.get("category") != slot[0]):
                raise ValueError(f"Variant recipe is not an accepted matching recipe: {question_id}/{slot}")
            image_path = (folder / "images" / f"{slot}.png").resolve()
            if not image_path.is_relative_to(root) or not image_path.is_file():
                raise ValueError(f"Missing or invalid variant image: {question_id}/{slot}")
            content = image_path.read_bytes()
            if not content.startswith(b"\x89PNG\r\n\x1a\n"):
                raise ValueError(f"Expected a PNG variant: {question_id}/{slot}")
            variant_id = f"{question_id}_{slot}"
            rows.append({
                "id": variant_id, "question": original["question"], "answer": original["answer"],
                "image": image_path.relative_to(root).as_posix(), "image_sha256": digest(content),
                "variant_metadata": {
                    "original_question_id": question_id, "slot_id": slot,
                    "category": recipe["category"], "operation": recipe["operation"],
                    "candidate_id": recipe["candidate_id"],
                    "recipe_path": recipe_path.relative_to(root).as_posix(),
                },
            })
            images[variant_id] = "data:image/png;base64," + base64.b64encode(content).decode("ascii")
    if not rows or len(rows) != len(images):
        raise ValueError("Expected a non-empty set of unique special variants.")
    return rows, images, dataset_hash, recipe_hashes


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dataset", type=Path, default=DATASET_ROOT / "dataset.jsonl")
    parser.add_argument("--trace", type=Path, default=DATASET_ROOT.parent / ".runtime/evaluation" / "trace_special.json")
    parser.add_argument("--report", type=Path, default=DATASET_ROOT.parent / ".runtime/evaluation" / "accuracy_special.txt")
    parser.add_argument("--env-file", type=Path, default=DEFAULT_ENV_FILE)
    parser.add_argument("--model", default=MODEL, help="Solver model.")
    parser.add_argument("--judge-model", default=None, help="Defaults to the solver model.")
    parser.add_argument("--base-url", default=os.environ.get("MIMO_BASE_URL", "https://token-plan-cn.xiaomimimo.com/v1"))
    parser.add_argument("--solver-base-url", default=None, help="Defaults to --base-url.")
    parser.add_argument("--judge-base-url", default=None, help="Defaults to --base-url.")
    parser.add_argument("--solver-key-env", default="MIMO_API_KEY")
    parser.add_argument("--judge-key-env", default="MIMO_API_KEY")
    parser.add_argument("--solver-thinking", choices=("enabled", "omitted"), default="enabled",
                        help="omitted sends an OpenAI-style request without a thinking field.")
    parser.add_argument("--concurrency", type=int, default=5, help="One solver then one judge per worker; maximum 36.")
    parser.add_argument("--rpm", type=int, default=90, help="Shared rolling 60-second limit, including judges and retries.")
    parser.add_argument("--timeout", type=float, default=300)
    parser.add_argument("--max-attempts", type=int, default=6)
    parser.add_argument("--answer-max-tokens", type=int, default=16384)
    parser.add_argument("--judge-max-tokens", type=int, default=128)
    args = parser.parse_args()
    if not 1 <= args.concurrency <= 36:
        parser.error("Concurrency must be between one and 36.")
    if min(args.rpm, args.timeout, args.max_attempts, args.answer_max_tokens, args.judge_max_tokens) <= 0:
        parser.error("Rate, timeout, retry count, and token limits must be positive.")
    args.dataset, args.trace, args.report = (path.resolve() for path in (args.dataset, args.trace, args.report))
    if args.trace == args.report or args.dataset in (args.trace, args.report):
        parser.error("Dataset, trace, and report must be separate files.")
    solver_base = args.solver_base_url or args.base_url
    judge_base = args.judge_base_url or args.base_url
    judge_model = args.judge_model or args.model
    solver_key = load_key(args.env_file, args.solver_key_env)
    judge_key = solver_key if args.judge_key_env == args.solver_key_env else load_key(args.env_file, args.judge_key_env)
    evaluate.MODEL = args.model
    rows, images, dataset_hash, recipe_hashes = load_special(args.dataset)
    total = len(rows)
    split = not (
        solver_base == judge_base == args.base_url
        and args.model == judge_model and args.solver_thinking == "enabled"
        and args.solver_key_env == args.judge_key_env == "MIMO_API_KEY"
    )
    config = {
        "dataset_kind": "special_variants", "variant_count": total,
        "model": args.model,
        "base_url": args.base_url if not split else solver_base,
        "solver_thinking": "enabled" if not split else args.solver_thinking,
        "judge_thinking": "disabled", "trials_per_question": 1,
        "numeric_relative_tolerance": 0.10, "zero_absolute_tolerance": 1e-8,
        "answer_max_tokens": args.answer_max_tokens, "judge_max_tokens": args.judge_max_tokens,
        "solver_system_prompt": SOLVER_PROMPT, "judge_system_prompt": JUDGE_PROMPT,
        "dataset": str(args.dataset), "dataset_sha256": dataset_hash,
        "recipes_sha256": recipe_hashes,
        "images_sha256": {row["id"]: row["image_sha256"] for row in rows},
    }
    if split:
        config["judge_model"] = judge_model
        config["judge_base_url"] = judge_base
    signature = digest(json.dumps(config, ensure_ascii=False, sort_keys=True, allow_nan=False).encode("utf-8"))
    lock = RunLock(args.trace.with_suffix(".lock"))
    stop, trace = threading.Event(), None
    try:
        trace = Trace(args.trace, signature, config, rows)
        trace.data.setdefault("execution", {})["concurrency"] = args.concurrency
        trace.save()
        solver_args = copy.copy(args)
        solver_args.base_url = solver_base
        judge_args = copy.copy(args)
        judge_args.base_url = judge_base
        solver_api = MiMo(solver_args, solver_key, trace, stop, name="Solver")
        same_endpoint = (
            solver_base == judge_base and solver_key == judge_key
            and args.model == judge_model and args.solver_thinking == "enabled"
        )
        judge_api = solver_api if same_endpoint else MiMo(judge_args, judge_key, trace, stop, name="Judge")
        trial_kwargs = {}
        if not same_endpoint:
            trial_kwargs = {
                "solver_api": solver_api, "judge_api": judge_api,
                "solver_model": args.model, "judge_model": judge_model,
                "solver_thinking": args.solver_thinking,
            }
        failures = []
        # Each worker makes its solver and judge calls sequentially. There is no
        # nested executor, so in-flight HTTP requests stay within --concurrency.
        with ThreadPoolExecutor(max_workers=args.concurrency, thread_name_prefix="special") as executor:
            futures = {
                executor.submit(evaluate_trial, i, 0, row, images[row["id"]], solver_api, trace, **trial_kwargs): row["id"]
                for i, row in enumerate(rows)
                if trace.get_trial(i, 0)["status"] != "completed"
            }
            for future in as_completed(futures):
                try:
                    future.result()
                    with trace.lock:
                        completed = trace.data["summary"]["completed_trials"]
                    if completed % 10 == 0 or completed == total:
                        print(f"Variants completed: {completed}/{total}", file=sys.stderr, flush=True)
                except CancelledError:
                    continue
                except Exception as error:
                    message = judge_api.redact(solver_api.redact(str(error)))
                    failures.append(f"{futures[future]}: {message}")
                    print(failures[-1], file=sys.stderr, flush=True)
                    if stop.is_set():
                        for pending in futures:
                            pending.cancel()
        if failures or trace.data["summary"]["completed_trials"] != total:
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
