"""Frozen question Plane583; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane583:

    def __init__(self):
        self.id = 'Plane583'
        self.source_dataset = 'Author Designed'
        self.source_key = 'author-extensions95-v1:Plane301/extension_04'
        self.question = 'Which of the following rigid pieces of wire can be combined with an identical copy, joining their ends, to form a closed shape without crossings or other contacts? The pieces may be rotated but not turned over.\nChoices:\nA: Wire A\nB: Wire B\nC: Wire C\nD: Wire D\nE: Wire E'
        self.answer = 'C'
        self.answer_type = 'choice'
        self.choices = {'A': 'Wire A', 'B': 'Wire B', 'C': 'Wire C', 'D': 'Wire D', 'E': 'Wire E'}
        self.query = self.question
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane583.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-2.9943416393196287, 30.99434163931963], ylim=[-17.79943860320105, 16.189244675438207], axes_position=[0.05, 0.05, 0.9, 0.9], coordinate_axes=False) as c:
            for object_id, points in [('A_dot_00', [[2.0, -1.5]]), ('A_dot_01', [[2.0, -0.5]]), ('A_dot_02', [[2.0, 0.5]]), ('A_dot_03', [[1.0, 0.5]]), ('A_dot_04', [[1.0, -0.5]]), ('A_dot_05', [[0.0, -0.5]]), ('A_dot_06', [[-1.0, -0.5]]), ('A_dot_07', [[-2.0, -0.5]]), ('A_dot_08', [[-2.0, 0.5]]), ('A_dot_09', [[-1.0, 0.5]]), ('A_dot_10', [[0.0, 0.5]]), ('A_dot_11', [[0.0, 1.5]])]:
                c.point(points, id=object_id)
            for object_id, points in [('A_edge_00', [[2.0, -1.5], [2.0, -0.5]]), ('A_edge_01', [[2.0, -0.5], [2.0, 0.5]]), ('A_edge_02', [[2.0, 0.5], [1.0, 0.5]]), ('A_edge_03', [[1.0, 0.5], [1.0, -0.5]]), ('A_edge_04', [[1.0, -0.5], [0.0, -0.5]]), ('A_edge_05', [[0.0, -0.5], [-1.0, -0.5]]), ('A_edge_06', [[-1.0, -0.5], [-2.0, -0.5]]), ('A_edge_07', [[-2.0, -0.5], [-2.0, 0.5]]), ('A_edge_08', [[-2.0, 0.5], [-1.0, 0.5]]), ('A_edge_09', [[-1.0, 0.5], [0.0, 0.5]]), ('A_edge_10', [[0.0, 0.5], [0.0, 1.5]])]:
                c.line(points, id=object_id)
            for object_id, points in [('B_dot_00', [[9.0, -1.0]]), ('B_dot_01', [[9.0, -2.0]]), ('B_dot_02', [[8.0, -2.0]]), ('B_dot_03', [[8.0, -1.0]]), ('B_dot_04', [[8.0, 0.0]]), ('B_dot_05', [[7.0, 0.0]]), ('B_dot_06', [[6.0, 0.0]]), ('B_dot_07', [[6.0, 1.0]]), ('B_dot_08', [[5.0, 1.0]]), ('B_dot_09', [[5.0, 2.0]]), ('B_dot_10', [[6.0, 2.0]]), ('B_dot_11', [[7.0, 2.0]]), ('B_dot_12', [[7.0, 1.0]])]:
                c.point(points, id=object_id)
            for object_id, points in [('B_edge_00', [[9.0, -1.0], [9.0, -2.0]]), ('B_edge_01', [[9.0, -2.0], [8.0, -2.0]]), ('B_edge_02', [[8.0, -2.0], [8.0, -1.0]]), ('B_edge_03', [[8.0, -1.0], [8.0, 0.0]]), ('B_edge_04', [[8.0, 0.0], [7.0, 0.0]]), ('B_edge_05', [[7.0, 0.0], [6.0, 0.0]]), ('B_edge_06', [[6.0, 0.0], [6.0, 1.0]]), ('B_edge_07', [[6.0, 1.0], [5.0, 1.0]]), ('B_edge_08', [[5.0, 1.0], [5.0, 2.0]]), ('B_edge_09', [[5.0, 2.0], [6.0, 2.0]]), ('B_edge_10', [[6.0, 2.0], [7.0, 2.0]]), ('B_edge_11', [[7.0, 2.0], [7.0, 1.0]])]:
                c.line(points, id=object_id)
            for object_id, points in [('C_dot_00', [[16.0, -1.5]]), ('C_dot_01', [[15.0, -1.5]]), ('C_dot_02', [[14.0, -1.5]]), ('C_dot_03', [[13.0, -1.5]]), ('C_dot_04', [[13.0, -0.5]]), ('C_dot_05', [[13.0, 0.5]]), ('C_dot_06', [[12.0, 0.5]]), ('C_dot_07', [[12.0, 1.5]]), ('C_dot_08', [[13.0, 1.5]]), ('C_dot_09', [[14.0, 1.5]]), ('C_dot_10', [[14.0, 0.5]]), ('C_dot_11', [[14.0, -0.5]]), ('C_dot_12', [[15.0, -0.5]])]:
                c.point(points, id=object_id)
            for object_id, points in [('C_edge_00', [[16.0, -1.5], [15.0, -1.5]]), ('C_edge_01', [[15.0, -1.5], [14.0, -1.5]]), ('C_edge_02', [[14.0, -1.5], [13.0, -1.5]]), ('C_edge_03', [[13.0, -1.5], [13.0, -0.5]]), ('C_edge_04', [[13.0, -0.5], [13.0, 0.5]]), ('C_edge_05', [[13.0, 0.5], [12.0, 0.5]]), ('C_edge_06', [[12.0, 0.5], [12.0, 1.5]]), ('C_edge_07', [[12.0, 1.5], [13.0, 1.5]]), ('C_edge_08', [[13.0, 1.5], [14.0, 1.5]]), ('C_edge_09', [[14.0, 1.5], [14.0, 0.5]]), ('C_edge_10', [[14.0, 0.5], [14.0, -0.5]]), ('C_edge_11', [[14.0, -0.5], [15.0, -0.5]])]:
                c.line(points, id=object_id)
            for object_id, points in [('D_dot_00', [[23.0, -2.0]]), ('D_dot_01', [[22.0, -2.0]]), ('D_dot_02', [[22.0, -1.0]]), ('D_dot_03', [[21.0, -1.0]]), ('D_dot_04', [[20.0, -1.0]]), ('D_dot_05', [[19.0, -1.0]]), ('D_dot_06', [[19.0, 0.0]]), ('D_dot_07', [[20.0, 0.0]]), ('D_dot_08', [[21.0, 0.0]]), ('D_dot_09', [[21.0, 1.0]]), ('D_dot_10', [[20.0, 1.0]]), ('D_dot_11', [[19.0, 1.0]]), ('D_dot_12', [[19.0, 2.0]]), ('D_dot_13', [[20.0, 2.0]])]:
                c.point(points, id=object_id)
            for object_id, points in [('D_edge_00', [[23.0, -2.0], [22.0, -2.0]]), ('D_edge_01', [[22.0, -2.0], [22.0, -1.0]]), ('D_edge_02', [[22.0, -1.0], [21.0, -1.0]]), ('D_edge_03', [[21.0, -1.0], [20.0, -1.0]]), ('D_edge_04', [[20.0, -1.0], [19.0, -1.0]]), ('D_edge_05', [[19.0, -1.0], [19.0, 0.0]]), ('D_edge_06', [[19.0, 0.0], [20.0, 0.0]]), ('D_edge_07', [[20.0, 0.0], [21.0, 0.0]]), ('D_edge_08', [[21.0, 0.0], [21.0, 1.0]]), ('D_edge_09', [[21.0, 1.0], [20.0, 1.0]]), ('D_edge_10', [[20.0, 1.0], [19.0, 1.0]]), ('D_edge_11', [[19.0, 1.0], [19.0, 2.0]]), ('D_edge_12', [[19.0, 2.0], [20.0, 2.0]])]:
                c.line(points, id=object_id)
            for object_id, points in [('E_dot_00', [[30.0, -2.0]]), ('E_dot_01', [[29.0, -2.0]]), ('E_dot_02', [[29.0, -1.0]]), ('E_dot_03', [[29.0, 0.0]]), ('E_dot_04', [[29.0, 1.0]]), ('E_dot_05', [[28.0, 1.0]]), ('E_dot_06', [[28.0, 2.0]]), ('E_dot_07', [[27.0, 2.0]]), ('E_dot_08', [[27.0, 1.0]]), ('E_dot_09', [[26.0, 1.0]]), ('E_dot_10', [[26.0, 0.0]]), ('E_dot_11', [[27.0, 0.0]]), ('E_dot_12', [[28.0, 0.0]])]:
                c.point(points, id=object_id)
            for object_id, points in [('E_edge_00', [[30.0, -2.0], [29.0, -2.0]]), ('E_edge_01', [[29.0, -2.0], [29.0, -1.0]]), ('E_edge_02', [[29.0, -1.0], [29.0, 0.0]]), ('E_edge_03', [[29.0, 0.0], [29.0, 1.0]]), ('E_edge_04', [[29.0, 1.0], [28.0, 1.0]]), ('E_edge_05', [[28.0, 1.0], [28.0, 2.0]]), ('E_edge_06', [[28.0, 2.0], [27.0, 2.0]]), ('E_edge_07', [[27.0, 2.0], [27.0, 1.0]]), ('E_edge_08', [[27.0, 1.0], [26.0, 1.0]]), ('E_edge_09', [[26.0, 1.0], [26.0, 0.0]]), ('E_edge_10', [[26.0, 0.0], [27.0, 0.0]]), ('E_edge_11', [[27.0, 0.0], [28.0, 0.0]])]:
                c.line(points, id=object_id)
            for object_id, text, anchor in [('choice_A', '(A)', [0, -3.3]), ('choice_B', '(B)', [7, -3.3]), ('choice_C', '(C)', [14, -3.3]), ('choice_D', '(D)', [21, -3.3]), ('choice_E', '(E)', [28, -3.3])]:
                c.text(text, anchor, id=object_id, rotation_mode='default')
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane583().draw(sys.argv[1] if len(sys.argv) > 1 else None))
