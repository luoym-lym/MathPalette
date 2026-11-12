"""Frozen question Ana294; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[3]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Ana294:

    def __init__(self):
        self.id = 'Ana294'
        self.source_dataset = 'We-Math2.0-Standard'
        self.source_key = 'standard/3785'
        self.question = 'Find the reflection of F in the point E. Read positions from the unit grid.'
        self.answer = '(-1, -2)'
        self.answer_type = 'expression'
        self.query = self.question
        self.subject = 'Analytics'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'Analytics' / 'dataset_generator/scenes/Ana294.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Analytics' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('Analytics', self.id, variant, output_path)
        with Canvas(ANALYTICS, xlim=[-8, 8], ylim=[-8, 8], xlabel='x', ylabel='y') as c:
            c.point([[0, -1]], filled=True, id='object_000')
            c.point([[1, 0]], filled=True, id='object_001')
            c.text('E', [0.4, -1.65], ha='left', va='bottom')
            c.text('F', [1.22, 0.43], ha='left', va='bottom')
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Ana294().draw(sys.argv[1] if len(sys.argv) > 1 else None))
