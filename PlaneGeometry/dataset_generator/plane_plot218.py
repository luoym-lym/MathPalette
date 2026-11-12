"""Frozen question Plane218; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane218:

    def __init__(self):
        self.id = 'Plane218'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:572'
        self.question = 'Two identical pieces are to be cut from the $4 \\times 3$ grid. Which of the following shapes cannot be used for the two pieces?\nChoices:\nA:A\nB:B\nC:C\nD:D\nE:E'
        self.answer = 'A'
        self.answer_type = 'choice'
        self.choices = {'A': 'A', 'B': 'B', 'C': 'C', 'D': 'D', 'E': 'E'}
        self.query = self.question
        self._geometry_01 = [('given_0', [[12, 7], [12, 8]]),
         ('given_1', [[12, 7], [13, 7]]),
         ('given_2', [[12, 8], [12, 9]]),
         ('given_3', [[12, 8], [13, 8]]),
         ('given_4', [[12, 9], [12, 10]]),
         ('given_5', [[12, 9], [13, 9]]),
         ('given_6', [[12, 10], [13, 10]]),
         ('given_7', [[13, 7], [13, 8]]),
         ('given_8', [[13, 7], [14, 7]]),
         ('given_9', [[13, 8], [13, 9]]),
         ('given_10', [[13, 8], [14, 8]]),
         ('given_11', [[13, 9], [13, 10]]),
         ('given_12', [[13, 9], [14, 9]]),
         ('given_13', [[13, 10], [14, 10]]),
         ('given_14', [[14, 7], [14, 8]]),
         ('given_15', [[14, 7], [15, 7]]),
         ('given_16', [[14, 8], [14, 9]]),
         ('given_17', [[14, 8], [15, 8]]),
         ('given_18', [[14, 9], [14, 10]]),
         ('given_19', [[14, 9], [15, 9]]),
         ('given_20', [[14, 10], [15, 10]]),
         ('given_21', [[15, 7], [15, 8]]),
         ('given_22', [[15, 7], [16, 7]]),
         ('given_23', [[15, 8], [15, 9]]),
         ('given_24', [[15, 8], [16, 8]]),
         ('given_25', [[15, 9], [15, 10]]),
         ('given_26', [[15, 9], [16, 9]]),
         ('given_27', [[15, 10], [16, 10]]),
         ('given_28', [[16, 7], [16, 8]]),
         ('given_29', [[16, 8], [16, 9]]),
         ('given_30', [[16, 9], [16, 10]]),
         ('A_0', [[0, 0], [0, 1]]),
         ('A_1', [[0, 0], [1, 0]]),
         ('A_2', [[0, 1], [0, 2]]),
         ('A_3', [[0, 1], [1, 1]]),
         ('A_4', [[0, 2], [0, 3]]),
         ('A_5', [[0, 2], [1, 2]]),
         ('A_6', [[0, 3], [1, 3]]),
         ('A_7', [[1, 0], [1, 1]]),
         ('A_8', [[1, 1], [1, 2]]),
         ('A_9', [[1, 1], [2, 1]]),
         ('A_10', [[1, 2], [1, 3]]),
         ('A_11', [[1, 2], [2, 2]]),
         ('A_12', [[2, 1], [2, 2]]),
         ('A_13', [[2, 1], [3, 1]]),
         ('A_14', [[2, 2], [3, 2]]),
         ('A_15', [[3, 1], [3, 2]]),
         ('B_0', [[6, 0], [6, 1]]),
         ('B_1', [[6, 0], [7, 0]]),
         ('B_2', [[6, 1], [6, 2]]),
         ('B_3', [[6, 1], [7, 1]]),
         ('B_4', [[6, 2], [7, 2]]),
         ('B_5', [[7, 0], [7, 1]]),
         ('B_6', [[7, 1], [7, 2]]),
         ('B_7', [[7, 1], [8, 1]]),
         ('B_8', [[7, 2], [8, 2]]),
         ('B_9', [[8, 0], [8, 1]]),
         ('B_10', [[8, 0], [9, 0]]),
         ('B_11', [[8, 1], [8, 2]]),
         ('B_12', [[8, 1], [9, 1]]),
         ('B_13', [[8, 2], [9, 2]]),
         ('B_14', [[9, 0], [9, 1]]),
         ('B_15', [[9, 1], [9, 2]]),
         ('C_0', [[12, 0], [12, 1]]),
         ('C_1', [[12, 0], [13, 0]]),
         ('C_2', [[12, 1], [13, 1]]),
         ('C_3', [[13, 0], [13, 1]]),
         ('C_4', [[13, 0], [14, 0]]),
         ('C_5', [[13, 1], [14, 1]]),
         ('C_6', [[14, 0], [14, 1]]),
         ('C_7', [[14, 0], [15, 0]]),
         ('C_8', [[14, 1], [15, 1]]),
         ('C_9', [[15, 0], [15, 1]]),
         ('C_10', [[15, 0], [16, 0]]),
         ('C_11', [[15, 1], [15, 2]]),
         ('C_12', [[15, 1], [16, 1]]),
         ('C_13', [[15, 2], [16, 2]]),
         ('C_14', [[16, 0], [16, 1]]),
         ('C_15', [[16, 1], [16, 2]]),
         ('D_0', [[18, 0], [18, 1]]),
         ('D_1', [[18, 0], [19, 0]]),
         ('D_2', [[18, 1], [19, 1]]),
         ('D_3', [[19, 0], [19, 1]]),
         ('D_4', [[19, 0], [20, 0]]),
         ('D_5', [[19, 1], [19, 2]]),
         ('D_6', [[19, 1], [20, 1]]),
         ('D_7', [[19, 2], [20, 2]]),
         ('D_8', [[20, 0], [20, 1]]),
         ('D_9', [[20, 0], [21, 0]]),
         ('D_10', [[20, 1], [20, 2]]),
         ('D_11', [[20, 1], [21, 1]]),
         ('D_12', [[21, 0], [21, 1]]),
         ('D_13', [[21, 0], [22, 0]]),
         ('D_14', [[21, 1], [22, 1]]),
         ('D_15', [[22, 0], [22, 1]]),
         ('E_0', [[24, 0], [24, 1]]),
         ('E_1', [[24, 0], [25, 0]]),
         ('E_2', [[24, 1], [24, 2]]),
         ('E_3', [[24, 1], [25, 1]]),
         ('E_4', [[24, 2], [24, 3]]),
         ('E_5', [[24, 2], [25, 2]]),
         ('E_6', [[24, 3], [25, 3]]),
         ('E_7', [[25, 0], [25, 1]]),
         ('E_8', [[25, 0], [26, 0]]),
         ('E_9', [[25, 1], [25, 2]]),
         ('E_10', [[25, 1], [26, 1]]),
         ('E_11', [[25, 2], [25, 3]]),
         ('E_12', [[25, 2], [26, 2]]),
         ('E_13', [[26, 0], [26, 1]]),
         ('E_14', [[26, 1], [26, 2]])]
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane218.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-2.2492539557962967, 26.73472889830395], ylim=[-9.55569649900677, 19.428286355093476]) as c:
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
    print(Plane218().draw(sys.argv[1] if len(sys.argv) > 1 else None))
