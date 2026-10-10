"""Register frozen new questions, render originals, generate Base, and report Special pending."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from base_support import ROOT, Dataset, atomic_write, dataset_lock, inside, pending_special, pixel_hash, question_id
from generate_base_variants import BaseGenerator


def prepare(root, qids, seed=20261008):
    if not 0 <= seed < 2**53:
        raise ValueError("Seed must be in [0, 2**53).")
    with dataset_lock(root):
        dataset = Dataset(root)
        for qid in qids:
            question_id(qid)
            _, question, row = dataset.load_question(qid)
            if not all(isinstance(getattr(question, name, None), str) and getattr(question, name).strip()
                       for name in ("source_id", "answer_type", "subject", "level")):
                raise ValueError(f"{qid}: define source_id, answer_type, subject, and level for Special compatibility.")
            if qid not in dataset.records and qid != f"Ana{len(dataset.records) + 1:02d}":
                raise ValueError(f"Next new question must be Ana{len(dataset.records) + 1:02d}.")
            first, second = dataset.original(qid), dataset.original(qid)
            if pixel_hash(first) != pixel_hash(second):
                raise ValueError(f"{qid}: original rendering is not deterministic; freeze all parameters.")
            image_path = inside(dataset.root, row["image"])
            if image_path.exists():
                if pixel_hash(image_path) != pixel_hash(first):
                    raise ValueError(f"{qid}: existing original differs; explicitly resolve the input change first.")
            else:
                atomic_write(image_path, first)
            if qid not in dataset.records:
                dataset.records[qid] = row
                atomic_write(dataset.root / "dataset.jsonl", "".join(
                    json.dumps(record, ensure_ascii=False, allow_nan=False) + "\n" for record in dataset.records.values()))
                print(f"{qid}: registered question and original image", flush=True)
            else:
                print(f"{qid}: existing question and original verified", flush=True)
            generator = BaseGenerator(dataset.root)
            generator.generate_question(qid, seed)
            generator.check_question(qid, redraw_pixels=True)
            generator.write_index()
        pending = pending_special(dataset.root)
        for qid in qids:
            print(f"{qid}: " + ("pending Special; restart the Special workbench to load it"
                               if qid in pending else "Special already collected; existing status retained"), flush=True)
        return pending


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("questions", nargs="*", help="Example: Ana21 Ana22, in increasing order.")
    parser.add_argument("--dataset-root", type=Path, default=ROOT)
    parser.add_argument("--seed", type=int, default=20261008)
    parser.add_argument("--pending", action="store_true", help="List derived Special pending IDs without editing workbench state.")
    args = parser.parse_args()
    if not args.questions and not args.pending:
        parser.error("Specify at least one question ID, or --pending.")
    if args.questions:
        prepare(args.dataset_root, args.questions, args.seed)
    if args.pending:
        print(json.dumps({"pending_special": pending_special(args.dataset_root)}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    try:
        main()
    except (ValueError, OSError, KeyError, AttributeError) as error:
        print(str(error), file=sys.stderr)
        raise SystemExit(1)
