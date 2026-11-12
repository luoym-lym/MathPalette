"""Frozen question Plane584; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane584:

    def __init__(self):
        self.id = 'Plane584'
        self.source_dataset = 'Author Designed'
        self.source_key = 'author-extensions95-v1:Plane301/extension_05'
        self.question = 'Which of the following rigid pieces of wire can be combined with an identical copy, joining their ends, to form a closed shape without crossings or other contacts? The pieces may be rotated but not turned over.\nChoices:\nA: Wire A\nB: Wire B\nC: Wire C\nD: Wire D\nE: Wire E'
        self.answer = 'E'
        self.answer_type = 'choice'
        self.choices = {'A': 'Wire A', 'B': 'Wire B', 'C': 'Wire C', 'D': 'Wire D', 'E': 'Wire E'}
        self.query = self.question
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane584.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-2.4788050512052635, 30.978805051205264], ylim=[-17.53147862502604, 15.926131477384487], axes_position=[0.05, 0.05, 0.9, 0.9], coordinate_axes=False) as c:
            for object_id, points in [('A_dot_00', [[-1.5, 0.5]]), ('A_dot_01', [[-1.5, 1.5]]), ('A_dot_02', [[-0.5, 1.5]]), ('A_dot_03', [[-0.5, 0.5]]), ('A_dot_04', [[0.5, 0.5]]), ('A_dot_05', [[0.5, -0.5]]), ('A_dot_06', [[-0.5, -0.5]]), ('A_dot_07', [[-1.5, -0.5]]), ('A_dot_08', [[-1.5, -1.5]]), ('A_dot_09', [[-0.5, -1.5]]), ('A_dot_10', [[0.5, -1.5]]), ('A_dot_11', [[1.5, -1.5]]), ('A_dot_12', [[1.5, -0.5]])]:
                c.point(points, id=object_id)
            for object_id, points in [('A_edge_00', [[-1.5, 0.5], [-1.5, 1.5]]), ('A_edge_01', [[-1.5, 1.5], [-0.5, 1.5]]), ('A_edge_02', [[-0.5, 1.5], [-0.5, 0.5]]), ('A_edge_03', [[-0.5, 0.5], [0.5, 0.5]]), ('A_edge_04', [[0.5, 0.5], [0.5, -0.5]]), ('A_edge_05', [[0.5, -0.5], [-0.5, -0.5]]), ('A_edge_06', [[-0.5, -0.5], [-1.5, -0.5]]), ('A_edge_07', [[-1.5, -0.5], [-1.5, -1.5]]), ('A_edge_08', [[-1.5, -1.5], [-0.5, -1.5]]), ('A_edge_09', [[-0.5, -1.5], [0.5, -1.5]]), ('A_edge_10', [[0.5, -1.5], [1.5, -1.5]]), ('A_edge_11', [[1.5, -1.5], [1.5, -0.5]])]:
                c.line(points, id=object_id)
            for object_id, points in [('B_dot_00', [[8.0, -1.0]]), ('B_dot_01', [[8.0, -2.0]]), ('B_dot_02', [[7.0, -2.0]]), ('B_dot_03', [[6.0, -2.0]]), ('B_dot_04', [[5.0, -2.0]]), ('B_dot_05', [[5.0, -1.0]]), ('B_dot_06', [[6.0, -1.0]]), ('B_dot_07', [[7.0, -1.0]]), ('B_dot_08', [[7.0, 0.0]]), ('B_dot_09', [[8.0, 0.0]]), ('B_dot_10', [[8.0, 1.0]]), ('B_dot_11', [[8.0, 2.0]]), ('B_dot_12', [[9.0, 2.0]]), ('B_dot_13', [[9.0, 1.0]])]:
                c.point(points, id=object_id)
            for object_id, points in [('B_edge_00', [[8.0, -1.0], [8.0, -2.0]]), ('B_edge_01', [[8.0, -2.0], [7.0, -2.0]]), ('B_edge_02', [[7.0, -2.0], [6.0, -2.0]]), ('B_edge_03', [[6.0, -2.0], [5.0, -2.0]]), ('B_edge_04', [[5.0, -2.0], [5.0, -1.0]]), ('B_edge_05', [[5.0, -1.0], [6.0, -1.0]]), ('B_edge_06', [[6.0, -1.0], [7.0, -1.0]]), ('B_edge_07', [[7.0, -1.0], [7.0, 0.0]]), ('B_edge_08', [[7.0, 0.0], [8.0, 0.0]]), ('B_edge_09', [[8.0, 0.0], [8.0, 1.0]]), ('B_edge_10', [[8.0, 1.0], [8.0, 2.0]]), ('B_edge_11', [[8.0, 2.0], [9.0, 2.0]]), ('B_edge_12', [[9.0, 2.0], [9.0, 1.0]])]:
                c.line(points, id=object_id)
            for object_id, points in [('C_dot_00', [[14.5, 2.0]]), ('C_dot_01', [[13.5, 2.0]]), ('C_dot_02', [[13.5, 1.0]]), ('C_dot_03', [[13.5, 0.0]]), ('C_dot_04', [[14.5, 0.0]]), ('C_dot_05', [[15.5, 0.0]]), ('C_dot_06', [[15.5, -1.0]]), ('C_dot_07', [[15.5, -2.0]]), ('C_dot_08', [[14.5, -2.0]]), ('C_dot_09', [[13.5, -2.0]]), ('C_dot_10', [[13.5, -1.0]]), ('C_dot_11', [[12.5, -1.0]]), ('C_dot_12', [[12.5, 0.0]])]:
                c.point(points, id=object_id)
            for object_id, points in [('C_edge_00', [[14.5, 2.0], [13.5, 2.0]]), ('C_edge_01', [[13.5, 2.0], [13.5, 1.0]]), ('C_edge_02', [[13.5, 1.0], [13.5, 0.0]]), ('C_edge_03', [[13.5, 0.0], [14.5, 0.0]]), ('C_edge_04', [[14.5, 0.0], [15.5, 0.0]]), ('C_edge_05', [[15.5, 0.0], [15.5, -1.0]]), ('C_edge_06', [[15.5, -1.0], [15.5, -2.0]]), ('C_edge_07', [[15.5, -2.0], [14.5, -2.0]]), ('C_edge_08', [[14.5, -2.0], [13.5, -2.0]]), ('C_edge_09', [[13.5, -2.0], [13.5, -1.0]]), ('C_edge_10', [[13.5, -1.0], [12.5, -1.0]]), ('C_edge_11', [[12.5, -1.0], [12.5, 0.0]])]:
                c.line(points, id=object_id)
            for object_id, points in [('D_dot_00', [[21.0, -1.5]]), ('D_dot_01', [[22.0, -1.5]]), ('D_dot_02', [[23.0, -1.5]]), ('D_dot_03', [[23.0, -0.5]]), ('D_dot_04', [[22.0, -0.5]]), ('D_dot_05', [[22.0, 0.5]]), ('D_dot_06', [[22.0, 1.5]]), ('D_dot_07', [[21.0, 1.5]]), ('D_dot_08', [[21.0, 0.5]]), ('D_dot_09', [[21.0, -0.5]]), ('D_dot_10', [[20.0, -0.5]]), ('D_dot_11', [[19.0, -0.5]]), ('D_dot_12', [[19.0, 0.5]])]:
                c.point(points, id=object_id)
            for object_id, points in [('D_edge_00', [[21.0, -1.5], [22.0, -1.5]]), ('D_edge_01', [[22.0, -1.5], [23.0, -1.5]]), ('D_edge_02', [[23.0, -1.5], [23.0, -0.5]]), ('D_edge_03', [[23.0, -0.5], [22.0, -0.5]]), ('D_edge_04', [[22.0, -0.5], [22.0, 0.5]]), ('D_edge_05', [[22.0, 0.5], [22.0, 1.5]]), ('D_edge_06', [[22.0, 1.5], [21.0, 1.5]]), ('D_edge_07', [[21.0, 1.5], [21.0, 0.5]]), ('D_edge_08', [[21.0, 0.5], [21.0, -0.5]]), ('D_edge_09', [[21.0, -0.5], [20.0, -0.5]]), ('D_edge_10', [[20.0, -0.5], [19.0, -0.5]]), ('D_edge_11', [[19.0, -0.5], [19.0, 0.5]])]:
                c.line(points, id=object_id)
            for object_id, points in [('E_dot_00', [[30.0, 1.5]]), ('E_dot_01', [[29.0, 1.5]]), ('E_dot_02', [[28.0, 1.5]]), ('E_dot_03', [[28.0, 0.5]]), ('E_dot_04', [[27.0, 0.5]]), ('E_dot_05', [[27.0, -0.5]]), ('E_dot_06', [[26.0, -0.5]]), ('E_dot_07', [[26.0, -1.5]]), ('E_dot_08', [[27.0, -1.5]]), ('E_dot_09', [[28.0, -1.5]]), ('E_dot_10', [[29.0, -1.5]]), ('E_dot_11', [[30.0, -1.5]]), ('E_dot_12', [[30.0, -0.5]])]:
                c.point(points, id=object_id)
            for object_id, points in [('E_edge_00', [[30.0, 1.5], [29.0, 1.5]]), ('E_edge_01', [[29.0, 1.5], [28.0, 1.5]]), ('E_edge_02', [[28.0, 1.5], [28.0, 0.5]]), ('E_edge_03', [[28.0, 0.5], [27.0, 0.5]]), ('E_edge_04', [[27.0, 0.5], [27.0, -0.5]]), ('E_edge_05', [[27.0, -0.5], [26.0, -0.5]]), ('E_edge_06', [[26.0, -0.5], [26.0, -1.5]]), ('E_edge_07', [[26.0, -1.5], [27.0, -1.5]]), ('E_edge_08', [[27.0, -1.5], [28.0, -1.5]]), ('E_edge_09', [[28.0, -1.5], [29.0, -1.5]]), ('E_edge_10', [[29.0, -1.5], [30.0, -1.5]]), ('E_edge_11', [[30.0, -1.5], [30.0, -0.5]])]:
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
    print(Plane584().draw(sys.argv[1] if len(sys.argv) > 1 else None))
