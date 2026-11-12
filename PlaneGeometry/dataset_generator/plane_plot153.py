"""Frozen question Plane153; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane153:

    def __init__(self):
        self.id = 'Plane153'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:77'
        self.question = 'The diagram shows two transparent sheets. What pattern results when the sheets are placed on top of each other?\nChoices:\nA:A\nB:B\nC:C\nD:D\nE:E'
        self.answer = 'D'
        self.answer_type = 'choice'
        self.choices = {'A': 'A', 'B': 'B', 'C': 'C', 'D': 'D', 'E': 'E'}
        self.query = self.question
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane153.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-2.1363739178869317, 28.780790225471012], ylim=[-10.052714587172364, 20.86444955618558]) as c:
            c.path([[8, 7], [12, 7], [12, 11], [8, 11], [8, 7]], [1, 2, 2, 2, 79], id='sheet1_frame')
            for object_id, points in [('sheet1_line0', [[9, 8], [9, 10]]), ('sheet1_line1', [[9, 8], [11, 8]]), ('sheet1_line2', [[9, 10], [10, 9]])]:
                c.line(points, id=object_id)
            c.point([[9, 8]], filled=True, id='sheet1_dot0')
            c.path([[15, 7], [19, 7], [19, 11], [15, 11], [15, 7]], [1, 2, 2, 2, 79], id='sheet2_frame')
            c.line([[17, 9], [18, 10]], id='sheet2_line0')
            c.line([[17, 9], [18, 9]], id='sheet2_line1')
            c.point([[17, 9]], filled=True, id='sheet2_dot0')
            c.path([[0, 0], [4, 0], [4, 4], [0, 4], [0, 0]], [1, 2, 2, 2, 79], id='A_frame')
            for object_id, points in [('A_line0', [[1, 1], [1, 3]]), ('A_line1', [[1, 3], [3, 3]]), ('A_line2', [[3, 3], [2, 2]]), ('A_line3', [[2, 2], [3, 2]]), ('A_line4', [[2, 2], [2, 1]])]:
                c.line(points, id=object_id)
            c.point([[1, 3]], filled=True, id='A_dot0')
            c.point([[2, 2]], filled=True, id='A_dot1')
            c.path([[6, 0], [10, 0], [10, 4], [6, 4], [6, 0]], [1, 2, 2, 2, 79], id='B_frame')
            for object_id, points in [('B_line0', [[7, 1], [7, 3]]), ('B_line1', [[7, 3], [9, 3]]), ('B_line2', [[9, 3], [8, 2]]), ('B_line3', [[7, 3], [9, 1]]), ('B_line4', [[8, 2], [9, 2]])]:
                c.line(points, id=object_id)
            c.point([[7, 3]], filled=True, id='B_dot0')
            c.point([[8, 2]], filled=True, id='B_dot1')
            c.path([[12, 0], [16, 0], [16, 4], [12, 4], [12, 0]], [1, 2, 2, 2, 79], id='C_frame')
            for object_id, points in [('C_line0', [[13, 1], [13, 3]]), ('C_line1', [[13, 3], [15, 3]]), ('C_line2', [[15, 3], [14, 2]]), ('C_line3', [[13, 3], [15, 1]]), ('C_line4', [[14, 2], [14, 1]])]:
                c.line(points, id=object_id)
            c.point([[13, 3]], filled=True, id='C_dot0')
            c.point([[14, 2]], filled=True, id='C_dot1')
            c.path([[18, 0], [22, 0], [22, 4], [18, 4], [18, 0]], [1, 2, 2, 2, 79], id='D_frame')
            for object_id, points in [('D_line0', [[19, 1], [19, 3]]), ('D_line1', [[19, 3], [21, 3]]), ('D_line2', [[21, 3], [20, 2]]), ('D_line3', [[20, 2], [21, 1]]), ('D_line4', [[20, 2], [20, 1]])]:
                c.line(points, id=object_id)
            c.point([[19, 3]], filled=True, id='D_dot0')
            c.point([[20, 2]], filled=True, id='D_dot1')
            c.path([[24, 0], [28, 0], [28, 4], [24, 4], [24, 0]], [1, 2, 2, 2, 79], id='E_frame')
            for object_id, points in [('E_line0', [[25, 1], [25, 3]]), ('E_line1', [[25, 3], [27, 3]]), ('E_line2', [[27, 3], [26, 2]]), ('E_line3', [[26, 2], [27, 1]])]:
                c.line(points, id=object_id)
            c.point([[25, 3]], filled=True, id='E_dot0')
            c.point([[26, 2]], filled=True, id='E_dot1')
            for object_id, text, anchor in [('label0', '(A)', [-0.8, 0.2]), ('label1', '(B)', [5.2, 0.2]), ('label2', '(C)', [11.2, 0.2]), ('label3', '(D)', [17.2, 0.2]), ('label4', '(E)', [23.2, 0.2])]:
                c.text(text, anchor, id=object_id, offset_pt=[0, 0], vertex=False)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane153().draw(sys.argv[1] if len(sys.argv) > 1 else None))
