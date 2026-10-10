"""Render locally frozen seeds, without changing their dataset records."""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

HELPERS = Path(__file__).resolve().parents[1]
if str(HELPERS) not in sys.path:
    sys.path.insert(0, str(HELPERS))
from base_support import ROOT, Dataset, atomic_write, dataset_lock


def main():
    parser = argparse.ArgumentParser(description="Verify deterministic original-image redraws for this dataset.")
    parser.add_argument("--output-dir", type=Path, help="Separate redraw directory; defaults to reproduced/originals")
    parser.add_argument("--question", action="append", help="Verify only this ID; repeat for multiple questions.")
    args = parser.parse_args()
    destination = args.output_dir.resolve() if args.output_dir else ROOT / "reproduced/originals"
    if destination.is_relative_to(ROOT) and not destination.is_relative_to(ROOT / "reproduced"):
        raise ValueError("Original redraws cannot overwrite accepted dataset inputs.")
    if destination.is_relative_to(ROOT.parent / "construct_dataset"):
        raise ValueError("Original redraws cannot overwrite the source dataset.")
    destination.mkdir(parents=True, exist_ok=True)
    with dataset_lock(ROOT):
        dataset = Dataset(ROOT)
        for qid in args.question or dataset.records:
            data = dataset.verify_original(qid)
            atomic_write(destination / f"{qid}.png", data)
            print(f"{qid}: original pixels match")


if __name__ == "__main__":
    main()
