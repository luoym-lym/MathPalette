"""Frozen question Plane582; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane582:

    def __init__(self):
        self.id = 'Plane582'
        self.source_dataset = 'Author Designed'
        self.source_key = 'author-extensions95-v1:Plane301/extension_03'
        self.question = 'Which of the following rigid pieces of wire can be combined with an identical copy, joining their ends, to form a closed shape without crossings or other contacts? The pieces may be rotated but not turned over.\nChoices:\nA: Wire A\nB: Wire B\nC: Wire C\nD: Wire D\nE: Wire E'
        self.answer = 'D'
        self.answer_type = 'choice'
        self.choices = {'A': 'Wire A', 'B': 'Wire B', 'C': 'Wire C', 'D': 'Wire D', 'E': 'Wire E'}
        self.query = self.question
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane582.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-2.463268463090891, 30.46326846309089], ylim=[-17.26351864685102, 15.663018279330762], axes_position=[0.05, 0.05, 0.9, 0.9], coordinate_axes=False) as c:
            for object_id, points in [('A_dot_00', [[1.5, -2.0]]), ('A_dot_01', [[1.5, -1.0]]), ('A_dot_02', [[1.5, 0.0]]), ('A_dot_03', [[0.5, 0.0]]), ('A_dot_04', [[-0.5, 0.0]]), ('A_dot_05', [[-1.5, 0.0]]), ('A_dot_06', [[-1.5, 1.0]]), ('A_dot_07', [[-1.5, 2.0]]), ('A_dot_08', [[-0.5, 2.0]]), ('A_dot_09', [[0.5, 2.0]]), ('A_dot_10', [[1.5, 2.0]]), ('A_dot_11', [[1.5, 1.0]]), ('A_dot_12', [[0.5, 1.0]])]:
                c.point(points, id=object_id)
            for object_id, points in [('A_edge_00', [[1.5, -2.0], [1.5, -1.0]]), ('A_edge_01', [[1.5, -1.0], [1.5, 0.0]]), ('A_edge_02', [[1.5, 0.0], [0.5, 0.0]]), ('A_edge_03', [[0.5, 0.0], [-0.5, 0.0]]), ('A_edge_04', [[-0.5, 0.0], [-1.5, 0.0]]), ('A_edge_05', [[-1.5, 0.0], [-1.5, 1.0]]), ('A_edge_06', [[-1.5, 1.0], [-1.5, 2.0]]), ('A_edge_07', [[-1.5, 2.0], [-0.5, 2.0]]), ('A_edge_08', [[-0.5, 2.0], [0.5, 2.0]]), ('A_edge_09', [[0.5, 2.0], [1.5, 2.0]]), ('A_edge_10', [[1.5, 2.0], [1.5, 1.0]]), ('A_edge_11', [[1.5, 1.0], [0.5, 1.0]])]:
                c.line(points, id=object_id)
            for object_id, points in [('B_dot_00', [[8.5, 2.0]]), ('B_dot_01', [[7.5, 2.0]]), ('B_dot_02', [[6.5, 2.0]]), ('B_dot_03', [[5.5, 2.0]]), ('B_dot_04', [[5.5, 1.0]]), ('B_dot_05', [[6.5, 1.0]]), ('B_dot_06', [[7.5, 1.0]]), ('B_dot_07', [[8.5, 1.0]]), ('B_dot_08', [[8.5, 0.0]]), ('B_dot_09', [[7.5, 0.0]]), ('B_dot_10', [[7.5, -1.0]]), ('B_dot_11', [[7.5, -2.0]]), ('B_dot_12', [[8.5, -2.0]])]:
                c.point(points, id=object_id)
            for object_id, points in [('B_edge_00', [[8.5, 2.0], [7.5, 2.0]]), ('B_edge_01', [[7.5, 2.0], [6.5, 2.0]]), ('B_edge_02', [[6.5, 2.0], [5.5, 2.0]]), ('B_edge_03', [[5.5, 2.0], [5.5, 1.0]]), ('B_edge_04', [[5.5, 1.0], [6.5, 1.0]]), ('B_edge_05', [[6.5, 1.0], [7.5, 1.0]]), ('B_edge_06', [[7.5, 1.0], [8.5, 1.0]]), ('B_edge_07', [[8.5, 1.0], [8.5, 0.0]]), ('B_edge_08', [[8.5, 0.0], [7.5, 0.0]]), ('B_edge_09', [[7.5, 0.0], [7.5, -1.0]]), ('B_edge_10', [[7.5, -1.0], [7.5, -2.0]]), ('B_edge_11', [[7.5, -2.0], [8.5, -2.0]])]:
                c.line(points, id=object_id)
            for object_id, points in [('C_dot_00', [[13.5, 1.0]]), ('C_dot_01', [[12.5, 1.0]]), ('C_dot_02', [[12.5, 0.0]]), ('C_dot_03', [[12.5, -1.0]]), ('C_dot_04', [[13.5, -1.0]]), ('C_dot_05', [[13.5, 0.0]]), ('C_dot_06', [[14.5, 0.0]]), ('C_dot_07', [[15.5, 0.0]]), ('C_dot_08', [[15.5, 1.0]]), ('C_dot_09', [[14.5, 1.0]])]:
                c.point(points, id=object_id)
            for object_id, points in [('C_edge_00', [[13.5, 1.0], [12.5, 1.0]]), ('C_edge_01', [[12.5, 1.0], [12.5, 0.0]]), ('C_edge_02', [[12.5, 0.0], [12.5, -1.0]]), ('C_edge_03', [[12.5, -1.0], [13.5, -1.0]]), ('C_edge_04', [[13.5, -1.0], [13.5, 0.0]]), ('C_edge_05', [[13.5, 0.0], [14.5, 0.0]]), ('C_edge_06', [[14.5, 0.0], [15.5, 0.0]]), ('C_edge_07', [[15.5, 0.0], [15.5, 1.0]]), ('C_edge_08', [[15.5, 1.0], [14.5, 1.0]])]:
                c.line(points, id=object_id)
            for object_id, points in [('D_dot_00', [[20.5, -1.0]]), ('D_dot_01', [[20.5, 0.0]]), ('D_dot_02', [[19.5, 0.0]]), ('D_dot_03', [[19.5, 1.0]]), ('D_dot_04', [[20.5, 1.0]]), ('D_dot_05', [[21.5, 1.0]]), ('D_dot_06', [[22.5, 1.0]]), ('D_dot_07', [[22.5, 0.0]]), ('D_dot_08', [[21.5, 0.0]]), ('D_dot_09', [[21.5, -1.0]])]:
                c.point(points, id=object_id)
            for object_id, points in [('D_edge_00', [[20.5, -1.0], [20.5, 0.0]]), ('D_edge_01', [[20.5, 0.0], [19.5, 0.0]]), ('D_edge_02', [[19.5, 0.0], [19.5, 1.0]]), ('D_edge_03', [[19.5, 1.0], [20.5, 1.0]]), ('D_edge_04', [[20.5, 1.0], [21.5, 1.0]]), ('D_edge_05', [[21.5, 1.0], [22.5, 1.0]]), ('D_edge_06', [[22.5, 1.0], [22.5, 0.0]]), ('D_edge_07', [[22.5, 0.0], [21.5, 0.0]]), ('D_edge_08', [[21.5, 0.0], [21.5, -1.0]])]:
                c.line(points, id=object_id)
            for object_id, points in [('E_dot_00', [[28.5, 1.5]]), ('E_dot_01', [[29.5, 1.5]]), ('E_dot_02', [[29.5, 0.5]]), ('E_dot_03', [[29.5, -0.5]]), ('E_dot_04', [[28.5, -0.5]]), ('E_dot_05', [[28.5, 0.5]]), ('E_dot_06', [[27.5, 0.5]]), ('E_dot_07', [[27.5, -0.5]]), ('E_dot_08', [[27.5, -1.5]]), ('E_dot_09', [[26.5, -1.5]]), ('E_dot_10', [[26.5, -0.5]])]:
                c.point(points, id=object_id)
            for object_id, points in [('E_edge_00', [[28.5, 1.5], [29.5, 1.5]]), ('E_edge_01', [[29.5, 1.5], [29.5, 0.5]]), ('E_edge_02', [[29.5, 0.5], [29.5, -0.5]]), ('E_edge_03', [[29.5, -0.5], [28.5, -0.5]]), ('E_edge_04', [[28.5, -0.5], [28.5, 0.5]]), ('E_edge_05', [[28.5, 0.5], [27.5, 0.5]]), ('E_edge_06', [[27.5, 0.5], [27.5, -0.5]]), ('E_edge_07', [[27.5, -0.5], [27.5, -1.5]]), ('E_edge_08', [[27.5, -1.5], [26.5, -1.5]]), ('E_edge_09', [[26.5, -1.5], [26.5, -0.5]])]:
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
    print(Plane582().draw(sys.argv[1] if len(sys.argv) > 1 else None))
