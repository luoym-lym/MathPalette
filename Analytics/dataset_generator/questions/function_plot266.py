"""Frozen question Ana266; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[3]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Ana266:

    def __init__(self):
        self.id = 'Ana266'
        self.source_dataset = 'We-Math2.0-Standard'
        self.source_key = 'standard/3895'
        self.question = 'Read the unit grid. Find the area of quadrilateral ABCD in square units.'
        self.answer = '55/2'
        self.answer_type = 'number'
        self.query = self.question
        self.subject = 'Analytics'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'Analytics' / 'dataset_generator/scenes/Ana266.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Analytics' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('Analytics', self.id, variant, output_path)
        with Canvas(ANALYTICS, xlim=[-8, 8], ylim=[-8, 8], xlabel='x', ylabel='y') as c:
            c.line([[-4, -2], [3, -2], [2, 3], [-2, 3], [-4, -2]], id='object_000', solid_capstyle='butt')
            for object_id, points in [('object_001', [[-4, -2]]), ('object_002', [[3, -2]]), ('object_003', [[2, 3]]), ('object_004', [[-2, 3]])]:
                c.point(points, id=object_id, filled=True)
            c.text('A', [-4.25, -1.63], ha='right', va='bottom')
            c.text('B', [3.23, -1.63], ha='left', va='bottom')
            c.text('C', [1.75, 3.37], ha='right', va='bottom')
            c.text('D', [-2.25, 3.37], ha='right', va='bottom')
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Ana266().draw(sys.argv[1] if len(sys.argv) > 1 else None))
