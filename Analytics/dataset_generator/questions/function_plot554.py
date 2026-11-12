"""Frozen question Ana554; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[3]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Ana554:

    def __init__(self):
        self.id = 'Ana554'
        self.source_dataset = 'Author Designed'
        self.source_key = 'author_special20_20261111/Ana554'
        self.question = 'Read the unit grid. Let u=OU and v=OV, where O is the origin. Find the ordered pair (a,b) such that OP=a*u+b*v.'
        self.answer = '(2, 1)'
        self.answer_type = 'expression'
        self.query = self.question
        self.subject = 'Analytics'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'Analytics' / 'dataset_generator/scenes/Ana554.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Analytics' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('Analytics', self.id, variant, output_path)
        with Canvas(ANALYTICS, xlim=[-8, 8], ylim=[-8, 8], xlabel='x', ylabel='y') as c:
            for object_id, points in [('object_000', [[0, 0], [2, 1]]), ('object_001', [[0, 0], [-1, 2]]), ('object_002', [[0, 0], [3, 4]])]:
                c.line(points, id=object_id, solid_capstyle='butt')
            for object_id, points in [('object_003', [[2, 1]]), ('object_004', [[-1, 2]]), ('object_005', [[3, 4]])]:
                c.point(points, id=object_id, filled=True)
            for object_id, text, anchor in [(None, 'U', [2.45, 0.8]), (None, 'V', [-1.45, 2.2]), (None, 'P', [3.4, 4.3])]:
                c.text(text, anchor, id=object_id)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Ana554().draw(sys.argv[1] if len(sys.argv) > 1 else None))
