"""Frozen question Plane144; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane144:

    def __init__(self):
        self.id = 'Plane144'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:37'
        self.question = 'A square is cut into four pieces. Which shape cannot be made with these four pieces?\nChoices:\nA:A\nB:B\nC:C\nD:D\nE:E'
        self.answer = 'D'
        self.answer_type = 'choice'
        self.choices = {'A': 'A', 'B': 'B', 'C': 'C', 'D': 'D', 'E': 'E'}
        self.query = self.question
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane144.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-2.251900242291754, 26.66367801808414], ylim=[-10.969447189487397, 17.946131070888498]) as c:
            c.path([[9, 10], [13, 10], [13, 14], [9, 14], [9, 10]], [1, 2, 2, 2, 79], id='source')
            for object_id, points in [('source_grid0_10_0', [[10, 10.0], [10, 14.0]]), ('source_grid0_11_0', [[11, 10.0], [11, 14.0]]), ('source_grid0_12_0', [[12, 10.0], [12, 14.0]]), ('source_grid1_11_0', [[9.0, 11], [13.0, 11]]), ('source_grid1_12_0', [[9.0, 12], [13.0, 12]]), ('source_grid1_13_0', [[9.0, 13], [13.0, 13]])]:
                c.line(points, id=object_id, linestyle=(0, [4, 3]))
            for object_id, points in [('source_cut0', [[9, 12], [11, 14]]), ('source_cut1', [[9, 12], [11, 10]]), ('source_cut2', [[11, 10], [11, 14]])]:
                c.line(points, id=object_id)
            c.path([[0, 3], [2, 1], [4, 3], [4, 5], [2, 7], [0, 5], [0, 3]], [1, 2, 2, 2, 2, 2, 79], id='A')
            for object_id, points in [('A_grid0_1_0', [[1, 2.0], [1, 6.0]]), ('A_grid0_2_0', [[2, 1.0], [2, 7.0]]), ('A_grid0_3_0', [[3, 2.0], [3, 6.0]]), ('A_grid1_2_0', [[1.0, 2], [3.0, 2]]), ('A_grid1_3_0', [[0.0, 3], [4.0, 3]]), ('A_grid1_4_0', [[0.0, 4], [4.0, 4]]), ('A_grid1_5_0', [[0.0, 5], [4.0, 5]]), ('A_grid1_6_0', [[1.0, 6], [3.0, 6]])]:
                c.line(points, id=object_id, linestyle=(0, [4, 3]))
            c.path([[7, 3], [15, 3], [11, 7], [7, 3]], [1, 2, 2, 79], id='B')
            for object_id, points in [('B_grid0_8_0', [[8, 3.0], [8, 4.0]]), ('B_grid0_9_0', [[9, 3.0], [9, 5.0]]), ('B_grid0_10_0', [[10, 3.0], [10, 6.0]]), ('B_grid0_11_0', [[11, 3.0], [11, 7.0]]), ('B_grid0_12_0', [[12, 3.0], [12, 6.0]]), ('B_grid0_13_0', [[13, 3.0], [13, 5.0]]), ('B_grid0_14_0', [[14, 3.0], [14, 4.0]]), ('B_grid1_4_0', [[8.0, 4], [14.0, 4]]), ('B_grid1_5_0', [[9.0, 5], [13.0, 5]]), ('B_grid1_6_0', [[10.0, 6], [12.0, 6]])]:
                c.line(points, id=object_id, linestyle=(0, [4, 3]))
            c.path([[0, -7], [2, -5], [4, -7], [4, -3], [2, -1], [0, -3], [0, -7]], [1, 2, 2, 2, 2, 2, 79], id='C')
            for object_id, points in [('C_grid0_1_0', [[1, -6.0], [1, -2.0]]), ('C_grid0_2_0', [[2, -5.0], [2, -1.0]]), ('C_grid0_3_0', [[3, -6.0], [3, -2.0]]), ('C_grid1_-6_0', [[0.0, -6], [1.0, -6]]), ('C_grid1_-6_2', [[3.0, -6], [4.0, -6]]), ('C_grid1_-5_0', [[0.0, -5], [4.0, -5]]), ('C_grid1_-4_0', [[0.0, -4], [4.0, -4]]), ('C_grid1_-3_0', [[0.0, -3], [4.0, -3]]), ('C_grid1_-2_0', [[1.0, -2], [3.0, -2]])]:
                c.line(points, id=object_id, linestyle=(0, [4, 3]))
            c.path([[10, -7], [12, -5], [14, -7], [14, -5], [16, -5], [14, -3], [12, -3], [12, -1], [10, -3], [10, -7]], [1, 2, 2, 2, 2, 2, 2, 2, 2, 79], id='D')
            for object_id, points in [('D_grid0_11_0', [[11, -6.0], [11, -2.0]]), ('D_grid0_12_0', [[12, -5.0], [12, -3.0]]), ('D_grid0_13_0', [[13, -6.0], [13, -3.0]]), ('D_grid0_14_0', [[14, -5.0], [14, -3.0]]), ('D_grid0_15_0', [[15, -5.0], [15, -4.0]]), ('D_grid1_-6_0', [[10.0, -6], [11.0, -6]]), ('D_grid1_-6_2', [[13.0, -6], [14.0, -6]]), ('D_grid1_-5_0', [[10.0, -5], [16.0, -5]]), ('D_grid1_-4_0', [[10.0, -4], [15.0, -4]]), ('D_grid1_-3_0', [[10.0, -3], [12.0, -3]]), ('D_grid1_-2_0', [[11.0, -2], [12.0, -2]])]:
                c.line(points, id=object_id, linestyle=(0, [4, 3]))
            c.path([[20, -5], [22, -5], [24, -7], [24, -5], [26, -5], [22, -1], [20, -3], [20, -5]], [1, 2, 2, 2, 2, 2, 2, 79], id='E')
            for object_id, points in [('E_grid0_21_0', [[21, -5.0], [21, -2.0]]), ('E_grid0_22_0', [[22, -5.0], [22, -1.0]]), ('E_grid0_23_0', [[23, -6.0], [23, -2.0]]), ('E_grid0_24_0', [[24, -5.0], [24, -3.0]]), ('E_grid0_25_0', [[25, -5.0], [25, -4.0]]), ('E_grid1_-6_0', [[23.0, -6], [24.0, -6]]), ('E_grid1_-5_0', [[20.0, -5], [26.0, -5]]), ('E_grid1_-4_0', [[20.0, -4], [25.0, -4]]), ('E_grid1_-3_0', [[20.0, -3], [24.0, -3]]), ('E_grid1_-2_0', [[21.0, -2], [23.0, -2]])]:
                c.line(points, id=object_id, linestyle=(0, [4, 3]))
            for object_id, text, anchor in [('label0', '(A)', [-1, 1.3]), ('label1', '(B)', [6, 3.3]), ('label2', '(C)', [-1, -6.7]), ('label3', '(D)', [9, -6.7]), ('label4', '(E)', [19, -6.7])]:
                c.text(text, anchor, id=object_id, offset_pt=[0, 0], vertex=False)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane144().draw(sys.argv[1] if len(sys.argv) > 1 else None))
