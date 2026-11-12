"""Frozen question Ana72; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[3]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Ana72:

    def __init__(self):
        self.id = 'Ana72'
        self.source_dataset = 'MathVista'
        self.source_key = 'testmini/34'
        self.question = 'Is the plotted function continuous at x=0?\nChoices:\nA: Yes\nB: No'
        self.answer = 'B'
        self.answer_type = 'choice'
        self.choices = {'A': 'Yes', 'B': 'No'}
        self.query = self.question
        self.subject = 'Analytics'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'Analytics' / 'dataset_generator/scenes/Ana72.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Analytics' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('Analytics', self.id, variant, output_path)
        with Canvas(ANALYTICS, xlim=[-8, 8], ylim=[-8, 8], xlabel='x', ylabel='y') as c:
            for object_id, points in [('object_000', [[-7, 6], [-6, 6]]), ('object_001', [[-6, 5], [-5, 5]]), ('object_002', [[-5, 4], [-4, 4]]), ('object_003', [[-4, 3], [-3, 3]]), ('object_004', [[-3, 2], [-2, 2]]), ('object_005', [[-2, 1], [-1, 1]]), ('object_006', [[-1, 0], [0, 0]]), ('object_007', [[0, -1], [1, -1]]), ('object_008', [[1, -2], [2, -2]]), ('object_009', [[2, -3], [3, -3]]), ('object_010', [[3, -4], [4, -4]]), ('object_011', [[4, -5], [5, -5]]), ('object_012', [[5, -6], [6, -6]]), ('object_013', [[6, -7], [7, -7]])]:
                c.line(points, id=object_id, solid_capstyle='butt')
            c.point([[-6, 6]], filled=True, id='object_014')
            c.point([[-5, 5]], filled=True, id='object_015')
            c.point([[-6, 5]], filled=False, id='object_016')
            c.point([[-4, 4]], filled=True, id='object_017')
            c.point([[-5, 4]], filled=False, id='object_018')
            c.point([[-3, 3]], filled=True, id='object_019')
            c.point([[-4, 3]], filled=False, id='object_020')
            c.point([[-2, 2]], filled=True, id='object_021')
            c.point([[-3, 2]], filled=False, id='object_022')
            c.point([[-1, 1]], filled=True, id='object_023')
            c.point([[-2, 1]], filled=False, id='object_024')
            c.point([[0, 0]], filled=True, id='object_025')
            c.point([[-1, 0]], filled=False, id='object_026')
            c.point([[1, -1]], filled=True, id='object_027')
            c.point([[0, -1]], filled=False, id='object_028')
            c.point([[2, -2]], filled=True, id='object_029')
            c.point([[1, -2]], filled=False, id='object_030')
            c.point([[3, -3]], filled=True, id='object_031')
            c.point([[2, -3]], filled=False, id='object_032')
            c.point([[4, -4]], filled=True, id='object_033')
            c.point([[3, -4]], filled=False, id='object_034')
            c.point([[5, -5]], filled=True, id='object_035')
            c.point([[4, -5]], filled=False, id='object_036')
            c.point([[6, -6]], filled=True, id='object_037')
            c.point([[5, -6]], filled=False, id='object_038')
            c.point([[6, -7]], filled=False, id='object_039')
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Ana72().draw(sys.argv[1] if len(sys.argv) > 1 else None))
