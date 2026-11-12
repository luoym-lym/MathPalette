"""Frozen question Plane562; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane562:

    def __init__(self):
        self.id = 'Plane562'
        self.source_dataset = 'Author Designed'
        self.source_key = 'author-extensions95-v1:Plane243/extension_03'
        self.question = 'Using the pieces $A, B, C, D$ and $E$ one can fill this shape completely. Pieces may be turned or flipped. Which of the pieces lies on the dot?\nChoices:\nA:A\nB:B\nC:C\nD:D\nE:E'
        self.answer = 'C'
        self.answer_type = 'choice'
        self.choices = {'A': 'A', 'B': 'B', 'C': 'C', 'D': 'D', 'E': 'E'}
        self.query = self.question
        self._geometry_01 = [[8.5, 6.0],
         [9.5, 6.0],
         [10.5, 6.0],
         [10.5, 7.0],
         [10.5, 8.0],
         [11.5, 8.0],
         [11.5, 7.0],
         [12.5, 7.0],
         [12.5, 6.0],
         [13.5, 6.0],
         [13.5, 7.0],
         [14.5, 7.0],
         [14.5, 8.0],
         [13.5, 8.0],
         [13.5, 9.0],
         [14.5, 9.0],
         [14.5, 10.0],
         [14.5, 11.0],
         [13.5, 11.0],
         [13.5, 10.0],
         [12.5, 10.0],
         [11.5, 10.0],
         [11.5, 11.0],
         [10.5, 11.0],
         [9.5, 11.0],
         [8.5, 11.0],
         [8.5, 10.0],
         [9.5, 10.0],
         [10.5, 10.0],
         [10.5, 9.0],
         [9.5, 9.0],
         [9.5, 8.0],
         [8.5, 8.0],
         [8.5, 7.0],
         [8.5, 6.0]]
        self._geometry_02 = [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 79]
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane562.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-0.5749999999999993, 23.575000000000006], ylim=[-7.215245790834782, 16.934754209165224], axes_position=[0.05, 0.05, 0.9, 0.9], coordinate_axes=False) as c:
            c.path(self._geometry_01, self._geometry_02, id='target_outline', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            for object_id, points in [('target_grid_00', [[8.5, 7.0], [9.5, 7.0]]), ('target_grid_01', [[9.5, 6.0], [9.5, 7.0]]), ('target_grid_02', [[9.5, 7.0], [9.5, 8.0]]), ('target_grid_03', [[9.5, 7.0], [10.5, 7.0]]), ('target_grid_04', [[9.5, 8.0], [10.5, 8.0]]), ('target_grid_05', [[9.5, 10.0], [9.5, 11.0]]), ('target_grid_06', [[10.5, 8.0], [10.5, 9.0]]), ('target_grid_07', [[10.5, 9.0], [11.5, 9.0]]), ('target_grid_08', [[10.5, 10.0], [10.5, 11.0]]), ('target_grid_09', [[10.5, 10.0], [11.5, 10.0]]), ('target_grid_10', [[11.5, 8.0], [11.5, 9.0]]), ('target_grid_11', [[11.5, 8.0], [12.5, 8.0]]), ('target_grid_12', [[11.5, 9.0], [11.5, 10.0]]), ('target_grid_13', [[11.5, 9.0], [12.5, 9.0]]), ('target_grid_14', [[12.5, 7.0], [12.5, 8.0]]), ('target_grid_15', [[12.5, 7.0], [13.5, 7.0]]), ('target_grid_16', [[12.5, 8.0], [12.5, 9.0]]), ('target_grid_17', [[12.5, 8.0], [13.5, 8.0]]), ('target_grid_18', [[12.5, 9.0], [12.5, 10.0]]), ('target_grid_19', [[12.5, 9.0], [13.5, 9.0]]), ('target_grid_20', [[13.5, 7.0], [13.5, 8.0]]), ('target_grid_21', [[13.5, 9.0], [13.5, 10.0]]), ('target_grid_22', [[13.5, 10.0], [14.5, 10.0]])]:
                c.line(points, id=object_id, solid_capstyle='butt')
            c.path([[0.0, 0.0], [1.0, 0.0], [2.0, 0.0], [3.0, 0.0], [3.0, 1.0], [2.0, 1.0], [1.0, 1.0], [0.0, 1.0], [0.0, 0.0]], [1, 2, 2, 2, 2, 2, 2, 2, 79], id='piece_A_outline', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.line([[1.0, 0.0], [1.0, 1.0]], id='piece_A_grid_00', solid_capstyle='butt')
            c.line([[2.0, 0.0], [2.0, 1.0]], id='piece_A_grid_01', solid_capstyle='butt')
            c.path([[5.0, 0.0], [6.0, 0.0], [7.0, 0.0], [8.0, 0.0], [8.0, 1.0], [7.0, 1.0], [6.0, 1.0], [6.0, 2.0], [5.0, 2.0], [5.0, 1.0], [5.0, 0.0]], [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 79], id='piece_B_outline', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            for object_id, points in [('piece_B_grid_00', [[5.0, 1.0], [6.0, 1.0]]), ('piece_B_grid_01', [[6.0, 0.0], [6.0, 1.0]]), ('piece_B_grid_02', [[7.0, 0.0], [7.0, 1.0]])]:
                c.line(points, id=object_id, solid_capstyle='butt')
            c.path([[10.0, 0.0], [11.0, 0.0], [12.0, 0.0], [13.0, 0.0], [13.0, 1.0], [12.0, 1.0], [12.0, 2.0], [11.0, 2.0], [11.0, 1.0], [10.0, 1.0], [10.0, 0.0]], [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 79], id='piece_C_outline', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            for object_id, points in [('piece_C_grid_00', [[11.0, 0.0], [11.0, 1.0]]), ('piece_C_grid_01', [[11.0, 1.0], [12.0, 1.0]]), ('piece_C_grid_02', [[12.0, 0.0], [12.0, 1.0]])]:
                c.line(points, id=object_id, solid_capstyle='butt')
            c.path([[15.5, 0.0], [16.5, 0.0], [17.5, 0.0], [17.5, 1.0], [17.5, 2.0], [16.5, 2.0], [15.5, 2.0], [15.5, 1.0], [15.5, 0.0]], [1, 2, 2, 2, 2, 2, 2, 2, 79], id='piece_D_outline', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            for object_id, points in [('piece_D_grid_00', [[15.5, 1.0], [16.5, 1.0]]), ('piece_D_grid_01', [[16.5, 0.0], [16.5, 1.0]]), ('piece_D_grid_02', [[16.5, 1.0], [16.5, 2.0]]), ('piece_D_grid_03', [[16.5, 1.0], [17.5, 1.0]])]:
                c.line(points, id=object_id, solid_capstyle='butt')
            c.path([[20.0, 1.0], [21.0, 1.0], [21.0, 0.0], [22.0, 0.0], [22.0, 1.0], [22.0, 2.0], [23.0, 2.0], [23.0, 3.0], [22.0, 3.0], [21.0, 3.0], [21.0, 2.0], [20.0, 2.0], [20.0, 1.0]], [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 79], id='piece_E_outline', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            for object_id, points in [('piece_E_grid_00', [[21.0, 1.0], [21.0, 2.0]]), ('piece_E_grid_01', [[21.0, 1.0], [22.0, 1.0]]), ('piece_E_grid_02', [[21.0, 2.0], [22.0, 2.0]]), ('piece_E_grid_03', [[22.0, 2.0], [22.0, 3.0]])]:
                c.line(points, id=object_id, solid_capstyle='butt')
            c.circle([13.0, 7.5], 0.075, id='target_dot', zorder=4, facecolor=[0.0, 0.0, 0.0, 1.0])
            for object_id, text, anchor in [('piece_A_label', '(A)', [1.5, -0.5]), ('piece_B_label', '(B)', [6.5, -0.5]), ('piece_C_label', '(C)', [11.5, -0.5]), ('piece_D_label', '(D)', [16.5, -0.5]), ('piece_E_label', '(E)', [21.5, -0.5])]:
                c.text(text, anchor, id=object_id, va='top', rotation_mode='default')
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane562().draw(sys.argv[1] if len(sys.argv) > 1 else None))
