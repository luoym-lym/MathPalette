"""Redraw frozen geometry without importing historical batch state."""
from __future__ import annotations
import argparse
import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BRANCHES = ('PlaneGeometry', 'SolidGeometry')

def read_json(path):
    return json.loads(Path(path).read_text(encoding='utf-8-sig'))

def write_json(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')

def renderer_for(branch):
    if branch not in BRANCHES:
        raise ValueError('Unknown geometry branch')
    path = ROOT / branch / 'dataset_generator/common_renderer.py'
    spec = importlib.util.spec_from_file_location('_'+branch+'_renderer', path)
    renderer = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(renderer)
    return renderer

def draw_question(branch, scene_path, output_path=None):
    if branch not in BRANCHES:
        raise ValueError('Unknown geometry branch')
    scene_path = Path(scene_path).resolve()
    scene = read_json(scene_path)
    target = Path(output_path).resolve() if output_path else ROOT / '.runtime/reproduced' / branch / (scene['id']+'.png')
    if target.is_relative_to(ROOT) and not target.is_relative_to(ROOT/'.runtime/reproduced'):
        raise ValueError('Redraw into .runtime/reproduced or an external output directory.')
    return renderer_for(branch).draw(scene_path, target)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('branch', choices=BRANCHES)
    parser.add_argument('question_id')
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    records = [json.loads(s) for s in (ROOT/args.branch/'dataset.jsonl').read_text(encoding='utf-8').splitlines() if s.strip()]
    row = next((r for r in records if r['id']==args.question_id), None)
    if row is None:
        parser.error('Unknown formal question ID')
    print(json.dumps(draw_question(args.branch, ROOT/args.branch/row['scene'], args.output), ensure_ascii=False))
