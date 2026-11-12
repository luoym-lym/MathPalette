"""Unified Analytics entry; question classes own construction."""
from pathlib import Path
import sys,json
_PROJECT_ROOT=Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:sys.path.insert(0,str(_PROJECT_ROOT))
from dataset_tools.drawing import *

def draw(scene_path, output_path=None):
    from dataset_tools.draw_question import draw_question
    scene=json.loads(Path(scene_path).read_text(encoding='utf-8-sig'))
    rows=[json.loads(line) for line in (_PROJECT_ROOT / 'Analytics' / 'dataset.jsonl').read_text().splitlines()]
    row=next((r for r in rows if r['id']==scene['id']),None)
    if row is None or not row.get('scene') or scene!=json.loads((_PROJECT_ROOT / 'Analytics' / row['scene']).read_text()):
        raise ValueError('Use the frozen formal scene; edit construction in the question class for new drawings')
    return draw_question('Analytics',scene['id'],output_path)
