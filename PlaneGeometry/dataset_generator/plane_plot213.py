"""Frozen question Plane213; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane213:

    def __init__(self):
        self.id = 'Plane213'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:543'
        self.question = 'The shape in the picture is to be split into three identical pieces. What does one of these pieces look like?\nChoices:\nA:A\nB:B\nC:C\nD:D\nE:E'
        self.answer = 'A'
        self.answer_type = 'choice'
        self.choices = {'A': 'A', 'B': 'B', 'C': 'C', 'D': 'D', 'E': 'E'}
        self.query = self.question
        self._geometry_01 = [('given_0', [[11, 7], [11, 8]]),
         ('given_1', [[11, 7], [12, 7]]),
         ('given_2', [[11, 8], [11, 9]]),
         ('given_3', [[11, 8], [12, 8]]),
         ('given_4', [[11, 9], [11, 10]]),
         ('given_5', [[11, 9], [12, 9]]),
         ('given_6', [[11, 10], [11, 11]]),
         ('given_7', [[11, 10], [12, 10]]),
         ('given_8', [[11, 11], [12, 11]]),
         ('given_9', [[12, 7], [12, 8]]),
         ('given_10', [[12, 7], [13, 7]]),
         ('given_11', [[12, 8], [12, 9]]),
         ('given_12', [[12, 8], [13, 8]]),
         ('given_13', [[12, 9], [12, 10]]),
         ('given_14', [[12, 9], [13, 9]]),
         ('given_15', [[12, 10], [12, 11]]),
         ('given_16', [[12, 10], [13, 10]]),
         ('given_17', [[12, 11], [13, 11]]),
         ('given_18', [[13, 7], [13, 8]]),
         ('given_19', [[13, 7], [14, 7]]),
         ('given_20', [[13, 8], [13, 9]]),
         ('given_21', [[13, 8], [14, 8]]),
         ('given_22', [[13, 9], [13, 10]]),
         ('given_23', [[13, 9], [14, 9]]),
         ('given_24', [[13, 10], [13, 11]]),
         ('given_25', [[13, 10], [14, 10]]),
         ('given_26', [[13, 11], [14, 11]]),
         ('given_27', [[14, 7], [14, 8]]),
         ('given_28', [[14, 8], [14, 9]]),
         ('given_29', [[14, 8], [15, 8]]),
         ('given_30', [[14, 9], [14, 10]]),
         ('given_31', [[14, 9], [15, 9]]),
         ('given_32', [[14, 10], [14, 11]]),
         ('given_33', [[14, 10], [15, 10]]),
         ('given_34', [[14, 11], [15, 11]]),
         ('given_35', [[15, 8], [15, 9]]),
         ('given_36', [[15, 9], [15, 10]]),
         ('given_37', [[15, 10], [15, 11]]),
         ('A_0', [[0, 0], [0, 1]]),
         ('A_1', [[0, 0], [1, 0]]),
         ('A_2', [[0, 1], [1, 1]]),
         ('A_3', [[1, 0], [1, 1]]),
         ('A_4', [[1, 0], [2, 0]]),
         ('A_5', [[1, 1], [1, 2]]),
         ('A_6', [[1, 1], [2, 1]]),
         ('A_7', [[1, 2], [2, 2]]),
         ('A_8', [[2, 0], [2, 1]]),
         ('A_9', [[2, 0], [3, 0]]),
         ('A_10', [[2, 1], [2, 2]]),
         ('A_11', [[2, 1], [3, 1]]),
         ('A_12', [[2, 2], [3, 2]]),
         ('A_13', [[3, 0], [3, 1]]),
         ('A_14', [[3, 1], [3, 2]]),
         ('B_0', [[6, 0], [6, 1]]),
         ('B_1', [[6, 0], [7, 0]]),
         ('B_2', [[6, 1], [6, 2]]),
         ('B_3', [[6, 1], [7, 1]]),
         ('B_4', [[6, 2], [7, 2]]),
         ('B_5', [[7, 0], [7, 1]]),
         ('B_6', [[7, 0], [8, 0]]),
         ('B_7', [[7, 1], [7, 2]]),
         ('B_8', [[7, 1], [8, 1]]),
         ('B_9', [[8, 0], [8, 1]]),
         ('B_10', [[8, 0], [9, 0]]),
         ('B_11', [[8, 1], [8, 2]]),
         ('B_12', [[8, 1], [9, 1]]),
         ('B_13', [[8, 2], [9, 2]]),
         ('B_14', [[9, 0], [9, 1]]),
         ('B_15', [[9, 1], [9, 2]]),
         ('C_0', [[12, 0], [12, 1]]),
         ('C_1', [[12, 0], [13, 0]]),
         ('C_2', [[12, 1], [12, 2]]),
         ('C_3', [[12, 1], [13, 1]]),
         ('C_4', [[12, 2], [12, 3]]),
         ('C_5', [[12, 2], [13, 2]]),
         ('C_6', [[12, 3], [12, 4]]),
         ('C_7', [[12, 3], [13, 3]]),
         ('C_8', [[12, 4], [13, 4]]),
         ('C_9', [[13, 0], [13, 1]]),
         ('C_10', [[13, 0], [14, 0]]),
         ('C_11', [[13, 1], [13, 2]]),
         ('C_12', [[13, 1], [14, 1]]),
         ('C_13', [[13, 2], [13, 3]]),
         ('C_14', [[13, 3], [13, 4]]),
         ('C_15', [[14, 0], [14, 1]]),
         ('D_0', [[18, 0], [18, 1]]),
         ('D_1', [[18, 0], [19, 0]]),
         ('D_2', [[18, 1], [19, 1]]),
         ('D_3', [[19, 0], [19, 1]]),
         ('D_4', [[19, 0], [20, 0]]),
         ('D_5', [[19, 1], [20, 1]]),
         ('D_6', [[20, 0], [20, 1]]),
         ('D_7', [[20, 0], [21, 0]]),
         ('D_8', [[20, 1], [20, 2]]),
         ('D_9', [[20, 1], [21, 1]]),
         ('D_10', [[20, 2], [21, 2]]),
         ('D_11', [[21, 0], [21, 1]]),
         ('D_12', [[21, 0], [22, 0]]),
         ('D_13', [[21, 1], [21, 2]]),
         ('D_14', [[21, 1], [22, 1]]),
         ('D_15', [[22, 0], [22, 1]]),
         ('E_0', [[24, 1], [24, 2]]),
         ('E_1', [[24, 1], [25, 1]]),
         ('E_2', [[24, 2], [25, 2]]),
         ('E_3', [[25, 0], [25, 1]]),
         ('E_4', [[25, 0], [26, 0]]),
         ('E_5', [[25, 1], [25, 2]]),
         ('E_6', [[25, 1], [26, 1]]),
         ('E_7', [[25, 2], [25, 3]]),
         ('E_8', [[25, 2], [26, 2]]),
         ('E_9', [[25, 3], [26, 3]]),
         ('E_10', [[26, 0], [26, 1]]),
         ('E_11', [[26, 1], [26, 2]]),
         ('E_12', [[26, 1], [27, 1]]),
         ('E_13', [[26, 2], [26, 3]]),
         ('E_14', [[26, 2], [27, 2]]),
         ('E_15', [[27, 1], [27, 2]])]
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane213.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-2.2843662692294355, 27.769071120907512], ylim=[-9.604988370994402, 20.448449019142544]) as c:
            for object_id, points in self._geometry_01:
                c.line(points, id=object_id)
            for object_id, text, anchor in [('label0', '(A)', [-1, 0.2]), ('label1', '(B)', [5, 0.2]), ('label2', '(C)', [11, 0.2]), ('label3', '(D)', [17, 0.2]), ('label4', '(E)', [23, 0.2])]:
                c.text(text, anchor, id=object_id, offset_pt=[0, 0], vertex=False)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane213().draw(sys.argv[1] if len(sys.argv) > 1 else None))
