"""Offline redraw of frozen, human-reviewed C variants only."""
import json
import sys
from pathlib import Path

_WORKBENCH = Path(__file__).resolve().parents[2] / "workbench"
if not (_WORKBENCH / "render_plugins.py").is_file():
    raise RuntimeError("Keep PlaneGeometry/special_variant and PlaneGeometry/workbench together.")
if str(_WORKBENCH) not in sys.path:
    sys.path.insert(0, str(_WORKBENCH))
from replay_archived import render_special_recipe

def _draw(slot_id, output_path=None):
    recipes = json.loads(Path(__file__).with_name("recipes.json").read_text(encoding="utf-8"))
    recipe = next(r for r in recipes if r["slot_id"] == slot_id)
    return render_special_recipe(recipe, output_path)

def draw_C01(output_path=None):
    return _draw("C01", output_path)

def draw_C02(output_path=None):
    return _draw("C02", output_path)

def draw_C03(output_path=None):
    return _draw("C03", output_path)

def draw_C04(output_path=None):
    return _draw("C04", output_path)

def draw_C05(output_path=None):
    return _draw("C05", output_path)

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='确定性重绘人工通过 C 图')
    parser.add_argument('slot_id', choices=['C01', 'C02', 'C03', 'C04', 'C05'])
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    print(json.dumps(_draw(args.slot_id, args.output), ensure_ascii=False))
