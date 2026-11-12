"""Frozen question Ana310; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[3]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Ana310:

    def __init__(self):
        self.id = 'Ana310'
        self.source_dataset = 'We-Math2.0-Standard'
        self.source_key = 'standard/3807'
        self.question = 'Triangle ABC is folded across its side AC. Find the coordinates of the image of B. Read positions from the unit grid.'
        self.answer = '(1, -4)'
        self.answer_type = 'expression'
        self.query = self.question
        self.subject = 'Analytics'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'Analytics' / 'dataset_generator/scenes/Ana310.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Analytics' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('Analytics', self.id, variant, output_path)
        with Canvas(ANALYTICS, xlim=[-8, 8], ylim=[-8, 8], xlabel='x', ylabel='y') as c:
            for object_id, points in [('object_000', [[-3, 0]]), ('object_001', [[1, 4]]), ('object_002', [[4, 0]])]:
                c.point(points, id=object_id, filled=True)
            c.line([[-3, 0], [1, 4], [4, 0]], id='object_003', solid_capstyle='butt')
            for object_id, text, anchor in [(None, 'A', [-2.78, 0.43]), (None, 'B', [1.22, 4.25]), (None, 'C', [4.22, 0.43])]:
                c.text(text, anchor, id=object_id, ha='left', va='bottom')
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Ana310().draw(sys.argv[1] if len(sys.argv) > 1 else None))
