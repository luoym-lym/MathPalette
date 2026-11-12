"""Frozen question Plane191; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane191:

    def __init__(self):
        self.id = 'Plane191'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:426'
        self.question = 'Three different figures repeat in the same order. Which figure comes next?\nChoices:\nA:A\nB:B\nC:C\nD:D\nE:E'
        self.answer = 'D'
        self.answer_type = 'choice'
        self.choices = {'A': 'A', 'B': 'B', 'C': 'C', 'D': 'D', 'E': 'E'}
        self.query = self.question
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane191.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-1.582432821603053, 16.21749620984595], ylim=[-5.638026057036251, 12.161902974412753]) as c:
            c.circle([1.0, 7.8], 0.2, id='o0')
            for object_id, points in [('o1', [[1.0, 7.6], [1.0, 6.6]]), ('o2', [[1.0, 6.6], [0.7, 5.6]]), ('o3', [[1.0, 6.6], [1.3, 5.6]]), ('o4', [[1.0, 7.35], [0.4, 7.9]]), ('o5', [[1.0, 7.35], [1.6, 7.9]])]:
                c.line(points, id=object_id)
            c.circle([3.7, 7.8], 0.2, id='o6')
            for object_id, points in [('o7', [[3.7, 7.6], [3.7, 6.6]]), ('o8', [[3.7, 6.6], [3.4000000000000004, 5.6]]), ('o9', [[3.7, 6.6], [4.0, 5.6]]), ('o10', [[3.7, 7.35], [3.1, 7.35]]), ('o11', [[3.7, 7.35], [4.3, 7.35]])]:
                c.line(points, id=object_id)
            c.circle([6.4, 7.8], 0.2, id='o12')
            for object_id, points in [('o13', [[6.4, 7.6], [6.4, 6.6]]), ('o14', [[6.4, 6.6], [6.1000000000000005, 5.6]]), ('o15', [[6.4, 6.6], [6.7, 5.6]]), ('o16', [[6.4, 7.35], [5.800000000000001, 6.85]]), ('o17', [[6.4, 7.35], [7.0, 6.85]])]:
                c.line(points, id=object_id)
            c.circle([9.100000000000001, 7.8], 0.2, id='o18')
            for object_id, points in [('o19', [[9.100000000000001, 7.6], [9.100000000000001, 6.6]]), ('o20', [[9.100000000000001, 6.6], [8.8, 5.6]]), ('o21', [[9.100000000000001, 6.6], [9.400000000000002, 5.6]]), ('o22', [[9.100000000000001, 7.35], [8.500000000000002, 7.9]]), ('o23', [[9.100000000000001, 7.35], [9.700000000000001, 7.9]])]:
                c.line(points, id=object_id)
            c.circle([11.8, 7.8], 0.2, id='o24')
            for object_id, points in [('o25', [[11.8, 7.6], [11.8, 6.6]]), ('o26', [[11.8, 6.6], [11.5, 5.6]]), ('o27', [[11.8, 6.6], [12.100000000000001, 5.6]]), ('o28', [[11.8, 7.35], [11.200000000000001, 7.35]]), ('o29', [[11.8, 7.35], [12.4, 7.35]])]:
                c.line(points, id=object_id)
            c.circle([0.0, 2.3], 0.2, id='o30')
            for object_id, points in [('o31', [[0.0, 2.1], [0.0, 1.1]]), ('o32', [[0.0, 1.1], [-0.3, 0.09999999999999998]]), ('o33', [[0.0, 1.1], [0.3, 0.09999999999999998]]), ('o34', [[0.0, 1.85], [-0.6, 2.4000000000000004]]), ('o35', [[0.0, 1.85], [0.6, 2.4000000000000004]])]:
                c.line(points, id=object_id)
            c.circle([5.6, 0.5000000000000001], 0.2, id='o36')
            for object_id, points in [('o37', [[5.4, 0.5000000000000001], [4.3999999999999995, 0.5]]), ('o38', [[4.3999999999999995, 0.5], [3.4, 0.8]]), ('o39', [[4.3999999999999995, 0.5], [3.4, 0.19999999999999998]]), ('o40', [[5.15, 0.5000000000000001], [5.7, 1.1000000000000003]]), ('o41', [[5.15, 0.5000000000000001], [5.7, -0.09999999999999987]])]:
                c.line(points, id=object_id)
            c.circle([7.6, 2.3], 0.2, id='o42')
            for object_id, points in [('o43', [[7.6, 2.1], [7.6, 1.1]]), ('o44', [[7.6, 1.1], [7.3, 0.09999999999999998]]), ('o45', [[7.6, 1.1], [7.8999999999999995, 0.09999999999999998]]), ('o46', [[7.6, 1.85], [7.0, 1.85]]), ('o47', [[7.6, 1.85], [8.2, 1.85]])]:
                c.line(points, id=object_id)
            c.circle([11.399999999999999, 2.3], 0.2, id='o48')
            for object_id, points in [('o49', [[11.399999999999999, 2.1], [11.399999999999999, 1.1]]), ('o50', [[11.399999999999999, 1.1], [11.099999999999998, 0.09999999999999998]]), ('o51', [[11.399999999999999, 1.1], [11.7, 0.09999999999999998]]), ('o52', [[11.399999999999999, 1.85], [10.799999999999999, 1.35]]), ('o53', [[11.399999999999999, 1.85], [11.999999999999998, 1.35]])]:
                c.line(points, id=object_id)
            c.circle([15.2, -1.3], 0.2, id='o54')
            for object_id, points in [('o55', [[15.2, -1.1], [15.2, -0.09999999999999998]]), ('o56', [[15.2, -0.09999999999999998], [15.5, 0.8999999999999999]]), ('o57', [[15.2, -0.09999999999999998], [14.899999999999999, 0.9]]), ('o58', [[15.2, -0.8500000000000001], [15.799999999999999, -1.4000000000000001]]), ('o59', [[15.2, -0.8500000000000001], [14.6, -1.4]])]:
                c.line(points, id=object_id)
            for object_id, text, anchor in [('t0', '?', [14.5, 7]), ('t1', 'A', [-1.0, 2.6]), ('t2', 'B', [2.8, 2.6]), ('t3', 'C', [6.6, 2.6]), ('t4', 'D', [10.399999999999999, 2.6]), ('t5', 'E', [14.2, 2.6])]:
                c.text(text, anchor, id=object_id, offset_pt=[0, 0], vertex=False)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane191().draw(sys.argv[1] if len(sys.argv) > 1 else None))
