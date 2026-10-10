"""Deterministic redraw of locally collected, previously reviewed A/B variants."""
from pathlib import Path
import json
import sys

_HELPERS = Path(__file__).resolve().parents[2] / "dataset_generator"
if str(_HELPERS) not in sys.path:
    sys.path.insert(0, str(_HELPERS))
from render_variants import render_recipe

def _draw(slot_id, output_path=None):
    recipes = json.loads(Path(__file__).with_name("recipes.json").read_text(encoding="utf-8"))
    recipe = next(r for r in recipes if r["slot_id"] == slot_id)
    return render_recipe(recipe, output_path)

def draw_A01(output_path=None):
    return _draw("A01", output_path)

def draw_A02(output_path=None):
    return _draw("A02", output_path)

def draw_A03(output_path=None):
    return _draw("A03", output_path)

def draw_A04(output_path=None):
    return _draw("A04", output_path)

def draw_A05(output_path=None):
    return _draw("A05", output_path)

def draw_B01(output_path=None):
    return _draw("B01", output_path)

def draw_B02(output_path=None):
    return _draw("B02", output_path)

def draw_B03(output_path=None):
    return _draw("B03", output_path)

def draw_B04(output_path=None):
    return _draw("B04", output_path)

def draw_B05(output_path=None):
    return _draw("B05", output_path)

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Redraw reviewed A/B variants from frozen parameters')
    parser.add_argument('slot_id', choices=['A01', 'A02', 'A03', 'A04', 'A05', 'B01', 'B02', 'B03', 'B04', 'B05'])
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    print(_draw(args.slot_id, args.output))
