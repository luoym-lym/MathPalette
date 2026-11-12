"""Frozen question Ana135; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[3]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Ana135:

    def __init__(self):
        self.id = 'Ana135'
        self.source_dataset = 'We-Math2.0-Standard'
        self.source_key = 'standard/5410'
        self.question = 'As shown in the figure, the normal vectors of lines $l$ and $m$ are vectors $OA$ and $OB$. Find the cosine of the angle between lines $l$ and $m$ (express your answer as a fraction).'
        self.answer = '$\\frac{\\sqrt{2}}{2}$'
        self.answer_type = 'number'
        self.query = self.question
        self.subject = 'Analytics'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'Analytics' / 'dataset_generator/scenes/Ana135.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Analytics' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('Analytics', self.id, variant, output_path)
        with Canvas(ANALYTICS, xlim=[-8, 8], ylim=[-8, 8], xlabel='x', ylabel='y') as c:
            c.point([[-1, 1]], filled=True, id='object_000')
            c.point([[1, 0]], filled=True, id='object_001')
            for object_id, points in [('object_002', [[0, 0], [-1, 1]]), ('object_003', [[-1, 1], [-0.6535176772185918, 0.8939339828220179]]), ('object_004', [[-1, 1], [-0.8939339828220179, 0.6535176772185918]]), ('object_005', [[0, 0], [1, 0]]), ('object_006', [[1, 0], [0.6799999999999999, -0.17]]), ('object_007', [[1, 0], [0.6799999999999999, 0.17]])]:
                c.line(points, id=object_id, solid_capstyle='butt')
            c.text('A', [-1.25, 1.25], ha='right', va='bottom')
            for object_id, text, anchor in [(None, 'B', [1.22, 0.25]), (None, '', [-2, 2]), (None, '', [1, -1])]:
                c.text(text, anchor, id=object_id, ha='left', va='bottom')
            c.text('$O$', [-0.32, -0.25], ha='right', va='top')
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Ana135().draw(sys.argv[1] if len(sys.argv) > 1 else None))
