"""Replay the four frozen Base plugins for this question."""
import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "dataset_generator"))
from generate_base_variants import redraw

def _draw(slot, output_path=None):
    return redraw(ROOT, Path(__file__).resolve().parent.name, slot, output_path)

def draw_base_1(output_path=None):
    return _draw("base_1", output_path)

def draw_base_2(output_path=None):
    return _draw("base_2", output_path)

def draw_base_3(output_path=None):
    return _draw("base_3", output_path)

def draw_base_4(output_path=None):
    return _draw("base_4", output_path)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("slot_id", choices=["base_1", "base_2", "base_3", "base_4"])
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    print(_draw(args.slot_id, args.output))
