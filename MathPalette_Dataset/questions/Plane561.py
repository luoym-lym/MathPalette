"""Collected question Plane561; construction on the shared drawing protocol."""
from pathlib import Path
import sys
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from MathPalette_Dataset.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane561:
    variants = ('C01', 'C02', 'C03')

    def __init__(self):
        self._samples_001 = [[8.999999999999998, 5.999999999999999],
         [9.999999999999998, 5.999999999999999],
         [10.999999999999998, 5.999999999999999],
         [11.999999999999998, 5.999999999999999],
         [11.999999999999998, 6.999999999999999],
         [12.999999999999998, 6.999999999999999],
         [12.999999999999998, 7.999999999999999],
         [12.999999999999998, 8.999999999999998],
         [12.999999999999998, 9.999999999999998],
         [12.999999999999998, 10.999999999999998],
         [13.999999999999998, 10.999999999999998],
         [13.999999999999998, 11.999999999999998],
         [12.999999999999998, 11.999999999999998],
         [11.999999999999998, 11.999999999999998],
         [11.999999999999998, 10.999999999999998],
         [10.999999999999998, 10.999999999999998],
         [9.999999999999998, 10.999999999999998],
         [8.999999999999998, 10.999999999999998],
         [8.999999999999998, 9.999999999999998],
         [9.999999999999998, 9.999999999999998],
         [9.999999999999998, 9.999999999199998]]
        self.id = 'Plane561'
        self.source_dataset = 'Author Designed'
        self.source_key = 'author-extensions95-v1:Plane243/extension_02'
        self.question = 'Using the pieces $A, B, C, D$ and $E$ one can fill this shape completely. Pieces may be turned but not flipped. Which of the pieces lies on the dot?\nChoices:\nA:A\nB:B\nC:C\nD:D\nE:E'
        self.answer = 'E'
        self.answer_type = 'choice'
        self.choices = {'A': 'A', 'B': 'B', 'C': 'C', 'D': 'D', 'E': 'E'}
        self.query = self.question
        self._geometry_01 = [[9.0, 6.0],
         [10.0, 6.0],
         [11.0, 6.0],
         [12.0, 6.0],
         [12.0, 7.0],
         [13.0, 7.0],
         [13.0, 8.0],
         [13.0, 9.0],
         [13.0, 10.0],
         [13.0, 11.0],
         [14.0, 11.0],
         [14.0, 12.0],
         [13.0, 12.0],
         [12.0, 12.0],
         [12.0, 11.0],
         [11.0, 11.0],
         [10.0, 11.0],
         [9.0, 11.0],
         [9.0, 10.0],
         [10.0, 10.0],
         [10.0, 9.0],
         [9.0, 9.0],
         [9.0, 8.0],
         [10.0, 8.0],
         [10.0, 7.0],
         [9.0, 7.0],
         [9.0, 6.0]]
        self._geometry_02 = [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 79]
        self._geometry_03 = [('target_grid_00', [[10.0, 6.0], [10.0, 7.0]]),
         ('target_grid_01', [[10.0, 7.0], [11.0, 7.0]]),
         ('target_grid_02', [[10.0, 8.0], [10.0, 9.0]]),
         ('target_grid_03', [[10.0, 8.0], [11.0, 8.0]]),
         ('target_grid_04', [[10.0, 9.0], [11.0, 9.0]]),
         ('target_grid_05', [[10.0, 10.0], [10.0, 11.0]]),
         ('target_grid_06', [[10.0, 10.0], [11.0, 10.0]]),
         ('target_grid_07', [[11.0, 6.0], [11.0, 7.0]]),
         ('target_grid_08', [[11.0, 7.0], [11.0, 8.0]]),
         ('target_grid_09', [[11.0, 7.0], [12.0, 7.0]]),
         ('target_grid_10', [[11.0, 8.0], [11.0, 9.0]]),
         ('target_grid_11', [[11.0, 8.0], [12.0, 8.0]]),
         ('target_grid_12', [[11.0, 9.0], [11.0, 10.0]]),
         ('target_grid_13', [[11.0, 9.0], [12.0, 9.0]]),
         ('target_grid_14', [[11.0, 10.0], [11.0, 11.0]]),
         ('target_grid_15', [[11.0, 10.0], [12.0, 10.0]]),
         ('target_grid_16', [[12.0, 7.0], [12.0, 8.0]]),
         ('target_grid_17', [[12.0, 8.0], [12.0, 9.0]]),
         ('target_grid_18', [[12.0, 8.0], [13.0, 8.0]]),
         ('target_grid_19', [[12.0, 9.0], [12.0, 10.0]]),
         ('target_grid_20', [[12.0, 9.0], [13.0, 9.0]]),
         ('target_grid_21', [[12.0, 10.0], [12.0, 11.0]]),
         ('target_grid_22', [[12.0, 10.0], [13.0, 10.0]]),
         ('target_grid_23', [[12.0, 11.0], [13.0, 11.0]]),
         ('target_grid_24', [[13.0, 11.0], [13.0, 12.0]])]

    def draw(self, output_path=None, *, variant=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if variant not in self.variants:
                raise ValueError('Unknown Special variant: ' + str(variant))
            return getattr(self, 'draw_' + variant)(output_path)
        with Canvas(PLANE, xlim=[-0.06249999999999645, 23.562499999999996], ylim=[-6.4442621866861955, 17.180737813313797], axes_position=[0.05, 0.05, 0.9, 0.9], coordinate_axes=False) as c:
            c.path(self._geometry_01, self._geometry_02, id='target_outline', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            for object_id, points in self._geometry_03:
                c.line(points, id=object_id, solid_capstyle='butt')
            c.path([[0.5, 0.0], [1.5, 0.0], [2.5, 0.0], [2.5, 1.0], [1.5, 1.0], [0.5, 1.0], [0.5, 0.0]], [1, 2, 2, 2, 2, 2, 79], id='piece_A_outline', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.line([[1.5, 0.0], [1.5, 1.0]], id='piece_A_grid_00', solid_capstyle='butt')
            c.path([[5.5, 0.0], [6.5, 0.0], [7.5, 0.0], [7.5, 1.0], [6.5, 1.0], [6.5, 2.0], [5.5, 2.0], [5.5, 1.0], [5.5, 0.0]], [1, 2, 2, 2, 2, 2, 2, 2, 79], id='piece_B_outline', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.line([[5.5, 1.0], [6.5, 1.0]], id='piece_B_grid_00', solid_capstyle='butt')
            c.line([[6.5, 0.0], [6.5, 1.0]], id='piece_B_grid_01', solid_capstyle='butt')
            c.path([[10.0, 0.0], [11.0, 0.0], [12.0, 0.0], [12.0, 1.0], [13.0, 1.0], [13.0, 2.0], [12.0, 2.0], [11.0, 2.0], [11.0, 1.0], [10.0, 1.0], [10.0, 0.0]], [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 79], id='piece_C_outline', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            for object_id, points in [('piece_C_grid_00', [[11.0, 0.0], [11.0, 1.0]]), ('piece_C_grid_01', [[11.0, 1.0], [12.0, 1.0]]), ('piece_C_grid_02', [[12.0, 1.0], [12.0, 2.0]])]:
                c.line(points, id=object_id, solid_capstyle='butt')
            c.path([[15.5, 0.0], [16.5, 0.0], [17.5, 0.0], [17.5, 1.0], [17.5, 2.0], [16.5, 2.0], [16.5, 3.0], [15.5, 3.0], [15.5, 2.0], [15.5, 1.0], [15.5, 0.0]], [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 79], id='piece_D_outline', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            for object_id, points in [('piece_D_grid_00', [[15.5, 1.0], [16.5, 1.0]]), ('piece_D_grid_01', [[15.5, 2.0], [16.5, 2.0]]), ('piece_D_grid_02', [[16.5, 0.0], [16.5, 1.0]]), ('piece_D_grid_03', [[16.5, 1.0], [16.5, 2.0]]), ('piece_D_grid_04', [[16.5, 1.0], [17.5, 1.0]])]:
                c.line(points, id=object_id, solid_capstyle='butt')
            c.path([[20.0, 0.0], [21.0, 0.0], [22.0, 0.0], [23.0, 0.0], [23.0, 1.0], [23.0, 2.0], [22.0, 2.0], [22.0, 1.0], [21.0, 1.0], [21.0, 2.0], [20.0, 2.0], [20.0, 1.0], [20.0, 0.0]], [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 79], id='piece_E_outline', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            for object_id, points in [('piece_E_grid_00', [[20.0, 1.0], [21.0, 1.0]]), ('piece_E_grid_01', [[21.0, 0.0], [21.0, 1.0]]), ('piece_E_grid_02', [[22.0, 0.0], [22.0, 1.0]]), ('piece_E_grid_03', [[22.0, 1.0], [23.0, 1.0]])]:
                c.line(points, id=object_id, solid_capstyle='butt')
            c.circle([10.5, 8.5], 0.075, id='target_dot', zorder=4, facecolor=[0.0, 0.0, 0.0, 1.0])
            for object_id, text, anchor in [('piece_A_label', '(A)', [1.5, -0.5]), ('piece_B_label', '(B)', [6.5, -0.5]), ('piece_C_label', '(C)', [11.5, -0.5]), ('piece_D_label', '(D)', [16.5, -0.5]), ('piece_E_label', '(E)', [21.5, -0.5])]:
                c.text(text, anchor, id=object_id, va='top', rotation_mode='default')
            return c.save(output_path)

    def draw_C01(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane561_C01.png'
        _geometry_01 = [('target_grid_00', [[10.0, 6.0], [10.0, 7.0]]),
         ('target_grid_01', [[10.0, 7.0], [11.0, 7.0]]),
         ('target_grid_02', [[10.0, 8.0], [10.0, 9.0]]),
         ('target_grid_03', [[10.0, 8.0], [11.0, 8.0]]),
         ('target_grid_04', [[10.0, 9.0], [11.0, 9.0]]),
         ('target_grid_05', [[10.0, 10.0], [10.0, 11.0]]),
         ('target_grid_06', [[10.0, 10.0], [11.0, 10.0]]),
         ('target_grid_07', [[11.0, 6.0], [11.0, 7.0]]),
         ('target_grid_08', [[11.0, 7.0], [11.0, 8.0]]),
         ('target_grid_09', [[11.0, 7.0], [12.0, 7.0]]),
         ('target_grid_10', [[11.0, 8.0], [11.0, 9.0]]),
         ('target_grid_11', [[11.0, 8.0], [12.0, 8.0]]),
         ('target_grid_12', [[11.0, 9.0], [11.0, 10.0]]),
         ('target_grid_13', [[11.0, 9.0], [12.0, 9.0]]),
         ('target_grid_14', [[11.0, 10.0], [11.0, 11.0]]),
         ('target_grid_15', [[11.0, 10.0], [12.0, 10.0]]),
         ('target_grid_16', [[12.0, 7.0], [12.0, 8.0]]),
         ('target_grid_17', [[12.0, 8.0], [12.0, 9.0]]),
         ('target_grid_18', [[12.0, 8.0], [13.0, 8.0]]),
         ('target_grid_19', [[12.0, 9.0], [12.0, 10.0]]),
         ('target_grid_20', [[12.0, 9.0], [13.0, 9.0]]),
         ('target_grid_21', [[12.0, 10.0], [12.0, 11.0]]),
         ('target_grid_22', [[12.0, 10.0], [13.0, 10.0]]),
         ('target_grid_23', [[12.0, 11.0], [13.0, 11.0]]),
         ('target_grid_24', [[13.0, 11.0], [13.0, 12.0]])]
        with Canvas(PLANE, xlim=(-0.06249999999999645, 23.562499999999996), ylim=(-6.4442621866861955, 17.180737813313797), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
            c.path(self._samples_001, [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2], id='target_outline', capstyle='butt', fill=False)
            c.path([[9.999999999999998, 9.999999999199998], [9.999999999999998, 8.999999999999998], [8.999999999999998, 8.999999999999998], [8.999999999999998, 7.999999999999999], [9.999999999599998, 7.999999999999999]], [1, 2, 2, 2, 2], id='target_outline', edgecolor=(0.9176470588235294, 0.34509803921568627, 0.047058823529411764, 1.0), linewidth=1.5, capstyle='butt', fill=False)
            c.path([[9.999999999599998, 7.999999999999999], [9.999999999999998, 7.999999999999999], [9.999999999999998, 6.999999999999999], [8.999999999999998, 6.999999999999999], [8.999999999999998, 5.999999999999999]], [1, 2, 2, 2, 2], id='target_outline', capstyle='butt', fill=False)
            for object_id, points in _geometry_01:
                c.line(points, id=object_id, solid_capstyle='butt')
            c.path([[0.5, 0.0], [1.5, 0.0], [2.5, 0.0], [2.5, 1.0], [1.5, 1.0], [0.5, 1.0], [0.5, 0.0]], [1, 2, 2, 2, 2, 2, 79], id='piece_A_outline', capstyle='butt', fill=False)
            c.line([[1.5, 0.0], [1.5, 1.0]], id='piece_A_grid_00', solid_capstyle='butt')
            c.path([[5.5, 0.0], [6.5, 0.0], [7.5, 0.0], [7.5, 1.0], [6.5, 1.0], [6.5, 2.0], [5.5, 2.0], [5.5, 1.0], [5.5, 0.0]], [1, 2, 2, 2, 2, 2, 2, 2, 79], id='piece_B_outline', capstyle='butt', fill=False)
            c.line([[5.5, 1.0], [6.5, 1.0]], id='piece_B_grid_00', solid_capstyle='butt')
            c.line([[6.5, 0.0], [6.5, 1.0]], id='piece_B_grid_01', solid_capstyle='butt')
            c.path([[10.0, 0.0], [11.0, 0.0], [12.0, 0.0], [12.0, 1.0], [13.0, 1.0], [13.0, 2.0], [12.0, 2.0], [11.0, 2.0], [11.0, 1.0], [10.0, 1.0], [10.0, 0.0]], [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 79], id='piece_C_outline', capstyle='butt', fill=False)
            for object_id, points in [('piece_C_grid_00', [[11.0, 0.0], [11.0, 1.0]]), ('piece_C_grid_01', [[11.0, 1.0], [12.0, 1.0]]), ('piece_C_grid_02', [[12.0, 1.0], [12.0, 2.0]])]:
                c.line(points, id=object_id, solid_capstyle='butt')
            c.path([[15.5, 0.0], [16.5, 0.0], [17.5, 0.0], [17.5, 1.0], [17.5, 2.0], [16.5, 2.0], [16.5, 3.0], [15.5, 3.0], [15.5, 2.0], [15.5, 1.0], [15.5, 0.0]], [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 79], id='piece_D_outline', edgecolor=(0.9176470588235294, 0.34509803921568627, 0.047058823529411764, 1.0), linewidth=1.5, capstyle='butt', fill=False)
            for object_id, points in [('piece_D_grid_00', [[15.5, 1.0], [16.5, 1.0]]), ('piece_D_grid_01', [[15.5, 2.0], [16.5, 2.0]]), ('piece_D_grid_02', [[16.5, 0.0], [16.5, 1.0]]), ('piece_D_grid_03', [[16.5, 1.0], [16.5, 2.0]]), ('piece_D_grid_04', [[16.5, 1.0], [17.5, 1.0]])]:
                c.line(points, id=object_id, solid_capstyle='butt')
            c.path([[20.0, 0.0], [21.0, 0.0], [22.0, 0.0], [23.0, 0.0], [23.0, 1.0], [23.0, 2.0], [22.0, 2.0], [22.0, 1.0], [21.0, 1.0], [21.0, 2.0], [20.0, 2.0], [20.0, 1.0], [20.0, 0.0]], [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 79], id='piece_E_outline', capstyle='butt', fill=False)
            for object_id, points in [('piece_E_grid_00', [[20.0, 1.0], [21.0, 1.0]]), ('piece_E_grid_01', [[21.0, 0.0], [21.0, 1.0]]), ('piece_E_grid_02', [[22.0, 0.0], [22.0, 1.0]]), ('piece_E_grid_03', [[22.0, 1.0], [23.0, 1.0]])]:
                c.line(points, id=object_id, solid_capstyle='butt')
            c.circle([10.5, 8.5], 0.075, id='target_dot', zorder=4, facecolor=(0.0, 0.0, 0.0, 1.0))
            for object_id, text, anchor in [('piece_A_label', '(A)', (1.5, -0.5)), ('piece_B_label', '(B)', (6.5, -0.5)), ('piece_C_label', '(C)', (11.5, -0.5)), ('piece_D_label', '(D)', (16.5, -0.5)), ('piece_E_label', '(E)', (21.5, -0.5))]:
                c.text(text, anchor, id=object_id, va='top', rotation_mode='default')
            for object_id, points in [(None, [[10.0, 8.0], [12.0, 8.0]]), (None, [[12.0, 8.0], [12.0, 10.0]]), (None, [[10.0, 10.0], [12.0, 10.0]])]:
                c.line(points, id=object_id, zorder=9, color='#EA580C', solid_capstyle='butt')
            for object_id, points in [(None, [[10.0, 8.0], [10.0, 9.0]]), (None, [[11.0, 8.0], [11.0, 10.0]]), (None, [[10.0, 9.0], [12.0, 9.0]]), (None, [[15.5, 2.0], [16.5, 2.0]]), (None, [[16.5, 0.0], [16.5, 2.0]]), (None, [[15.5, 1.0], [17.5, 1.0]])]:
                c.line(points, id=object_id, zorder=9, color='#EA580C', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            return c.save(output_path)

    def draw_C02(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane561_C02.png'
        _geometry_01 = [('target_grid_00', [[10.0, 6.0], [10.0, 7.0]]),
         ('target_grid_01', [[10.0, 7.0], [11.0, 7.0]]),
         ('target_grid_02', [[10.0, 8.0], [10.0, 9.0]]),
         ('target_grid_03', [[10.0, 8.0], [11.0, 8.0]]),
         ('target_grid_04', [[10.0, 9.0], [11.0, 9.0]]),
         ('target_grid_05', [[10.0, 10.0], [10.0, 11.0]]),
         ('target_grid_06', [[10.0, 10.0], [11.0, 10.0]]),
         ('target_grid_07', [[11.0, 6.0], [11.0, 7.0]]),
         ('target_grid_08', [[11.0, 7.0], [11.0, 8.0]]),
         ('target_grid_09', [[11.0, 7.0], [12.0, 7.0]]),
         ('target_grid_10', [[11.0, 8.0], [11.0, 9.0]]),
         ('target_grid_11', [[11.0, 8.0], [12.0, 8.0]]),
         ('target_grid_12', [[11.0, 9.0], [11.0, 10.0]]),
         ('target_grid_13', [[11.0, 9.0], [12.0, 9.0]]),
         ('target_grid_14', [[11.0, 10.0], [11.0, 11.0]]),
         ('target_grid_15', [[11.0, 10.0], [12.0, 10.0]]),
         ('target_grid_16', [[12.0, 7.0], [12.0, 8.0]]),
         ('target_grid_17', [[12.0, 8.0], [12.0, 9.0]]),
         ('target_grid_18', [[12.0, 8.0], [13.0, 8.0]]),
         ('target_grid_19', [[12.0, 9.0], [12.0, 10.0]]),
         ('target_grid_20', [[12.0, 9.0], [13.0, 9.0]]),
         ('target_grid_21', [[12.0, 10.0], [12.0, 11.0]]),
         ('target_grid_22', [[12.0, 10.0], [13.0, 10.0]]),
         ('target_grid_23', [[12.0, 11.0], [13.0, 11.0]]),
         ('target_grid_24', [[13.0, 11.0], [13.0, 12.0]])]
        with Canvas(PLANE, xlim=(-0.06249999999999645, 23.562499999999996), ylim=(-6.4442621866861955, 17.180737813313797), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
            c.path(self._samples_001, [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2], id='target_outline', capstyle='butt', fill=False)
            c.path([[9.999999999999998, 9.999999999199998], [9.999999999999998, 8.999999999999998], [8.999999999999998, 8.999999999999998], [8.999999999999998, 7.999999999999999], [9.999999999599998, 7.999999999999999]], [1, 2, 2, 2, 2], id='target_outline', edgecolor=(0.1450980392156863, 0.38823529411764707, 0.9215686274509803, 1.0), linewidth=2.0, capstyle='butt', fill=False)
            c.path([[9.999999999599998, 7.999999999999999], [9.999999999999998, 7.999999999999999], [9.999999999999998, 6.999999999999999], [8.999999999999998, 6.999999999999999], [8.999999999999998, 5.999999999999999]], [1, 2, 2, 2, 2], id='target_outline', capstyle='butt', fill=False)
            for object_id, points in _geometry_01:
                c.line(points, id=object_id, solid_capstyle='butt')
            c.path([[0.5, 0.0], [1.5, 0.0], [2.5, 0.0], [2.5, 1.0], [1.5, 1.0], [0.5, 1.0], [0.5, 0.0]], [1, 2, 2, 2, 2, 2, 79], id='piece_A_outline', capstyle='butt', fill=False)
            c.line([[1.5, 0.0], [1.5, 1.0]], id='piece_A_grid_00', solid_capstyle='butt')
            c.path([[5.5, 0.0], [6.5, 0.0], [7.5, 0.0], [7.5, 1.0], [6.5, 1.0], [6.5, 2.0], [5.5, 2.0], [5.5, 1.0], [5.5, 0.0]], [1, 2, 2, 2, 2, 2, 2, 2, 79], id='piece_B_outline', capstyle='butt', fill=False)
            c.line([[5.5, 1.0], [6.5, 1.0]], id='piece_B_grid_00', solid_capstyle='butt')
            c.line([[6.5, 0.0], [6.5, 1.0]], id='piece_B_grid_01', solid_capstyle='butt')
            c.path([[10.0, 0.0], [11.0, 0.0], [12.0, 0.0], [12.0, 1.0], [13.0, 1.0], [13.0, 2.0], [12.0, 2.0], [11.0, 2.0], [11.0, 1.0], [10.0, 1.0], [10.0, 0.0]], [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 79], id='piece_C_outline', capstyle='butt', fill=False)
            for object_id, points in [('piece_C_grid_00', [[11.0, 0.0], [11.0, 1.0]]), ('piece_C_grid_01', [[11.0, 1.0], [12.0, 1.0]]), ('piece_C_grid_02', [[12.0, 1.0], [12.0, 2.0]])]:
                c.line(points, id=object_id, solid_capstyle='butt')
            c.path([[15.5, 0.0], [16.5, 0.0], [17.5, 0.0], [17.5, 1.0], [17.5, 2.0], [16.5, 2.0], [16.5, 3.0], [15.5, 3.0], [15.5, 2.0], [15.5, 1.0], [15.5, 0.0]], [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 79], id='piece_D_outline', edgecolor=(0.1450980392156863, 0.38823529411764707, 0.9215686274509803, 1.0), linewidth=2.0, capstyle='butt', fill=False)
            for object_id, points in [('piece_D_grid_00', [[15.5, 1.0], [16.5, 1.0]]), ('piece_D_grid_01', [[15.5, 2.0], [16.5, 2.0]]), ('piece_D_grid_02', [[16.5, 0.0], [16.5, 1.0]]), ('piece_D_grid_03', [[16.5, 1.0], [16.5, 2.0]]), ('piece_D_grid_04', [[16.5, 1.0], [17.5, 1.0]])]:
                c.line(points, id=object_id, solid_capstyle='butt')
            c.path([[20.0, 0.0], [21.0, 0.0], [22.0, 0.0], [23.0, 0.0], [23.0, 1.0], [23.0, 2.0], [22.0, 2.0], [22.0, 1.0], [21.0, 1.0], [21.0, 2.0], [20.0, 2.0], [20.0, 1.0], [20.0, 0.0]], [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 79], id='piece_E_outline', capstyle='butt', fill=False)
            for object_id, points in [('piece_E_grid_00', [[20.0, 1.0], [21.0, 1.0]]), ('piece_E_grid_01', [[21.0, 0.0], [21.0, 1.0]]), ('piece_E_grid_02', [[22.0, 0.0], [22.0, 1.0]]), ('piece_E_grid_03', [[22.0, 1.0], [23.0, 1.0]])]:
                c.line(points, id=object_id, solid_capstyle='butt')
            c.circle([10.5, 8.5], 0.075, id='target_dot', zorder=4, facecolor=(0.0, 0.0, 0.0, 1.0))
            for object_id, text, anchor in [('piece_A_label', '(A)', (1.5, -0.5)), ('piece_B_label', '(B)', (6.5, -0.5)), ('piece_C_label', '(C)', (11.5, -0.5)), ('piece_D_label', '(D)', (16.5, -0.5)), ('piece_E_label', '(E)', (21.5, -0.5))]:
                c.text(text, anchor, id=object_id, va='top', rotation_mode='default')
            for object_id, points in [(None, [[10.0, 8.0], [12.0, 8.0]]), (None, [[12.0, 8.0], [12.0, 10.0]]), (None, [[10.0, 10.0], [12.0, 10.0]])]:
                c.line(points, id=object_id, zorder=9, color='#2563EB', solid_capstyle='butt')
            for object_id, points in [(None, [[10.0, 8.0], [10.0, 9.0]]), (None, [[11.0, 8.0], [11.0, 10.0]]), (None, [[10.0, 9.0], [12.0, 9.0]]), (None, [[15.5, 2.0], [16.5, 2.0]]), (None, [[16.5, 0.0], [16.5, 2.0]]), (None, [[15.5, 1.0], [17.5, 1.0]])]:
                c.line(points, id=object_id, zorder=9, color='#2563EB', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            return c.save(output_path)

    def draw_C03(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane561_C03.png'
        _geometry_01 = [('target_grid_00', [[10.0, 6.0], [10.0, 7.0]]),
         ('target_grid_01', [[10.0, 7.0], [11.0, 7.0]]),
         ('target_grid_02', [[10.0, 8.0], [10.0, 9.0]]),
         ('target_grid_03', [[10.0, 8.0], [11.0, 8.0]]),
         ('target_grid_04', [[10.0, 9.0], [11.0, 9.0]]),
         ('target_grid_05', [[10.0, 10.0], [10.0, 11.0]]),
         ('target_grid_06', [[10.0, 10.0], [11.0, 10.0]]),
         ('target_grid_07', [[11.0, 6.0], [11.0, 7.0]]),
         ('target_grid_08', [[11.0, 7.0], [11.0, 8.0]]),
         ('target_grid_09', [[11.0, 7.0], [12.0, 7.0]]),
         ('target_grid_10', [[11.0, 8.0], [11.0, 9.0]]),
         ('target_grid_11', [[11.0, 8.0], [12.0, 8.0]]),
         ('target_grid_12', [[11.0, 9.0], [11.0, 10.0]]),
         ('target_grid_13', [[11.0, 9.0], [12.0, 9.0]]),
         ('target_grid_14', [[11.0, 10.0], [11.0, 11.0]]),
         ('target_grid_15', [[11.0, 10.0], [12.0, 10.0]]),
         ('target_grid_16', [[12.0, 7.0], [12.0, 8.0]]),
         ('target_grid_17', [[12.0, 8.0], [12.0, 9.0]]),
         ('target_grid_18', [[12.0, 8.0], [13.0, 8.0]]),
         ('target_grid_19', [[12.0, 9.0], [12.0, 10.0]]),
         ('target_grid_20', [[12.0, 9.0], [13.0, 9.0]]),
         ('target_grid_21', [[12.0, 10.0], [12.0, 11.0]]),
         ('target_grid_22', [[12.0, 10.0], [13.0, 10.0]]),
         ('target_grid_23', [[12.0, 11.0], [13.0, 11.0]]),
         ('target_grid_24', [[13.0, 11.0], [13.0, 12.0]])]
        with Canvas(PLANE, xlim=(-0.06249999999999645, 23.562499999999996), ylim=(-6.4442621866861955, 17.180737813313797), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
            c.path(self._samples_001, [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2], id='target_outline', capstyle='butt', fill=False)
            c.path([[9.999999999999998, 9.999999999199998], [9.999999999999998, 8.999999999999998], [8.999999999999998, 8.999999999999998], [8.999999999999998, 7.999999999999999], [9.999999999599998, 7.999999999999999]], [1, 2, 2, 2, 2], id='target_outline', edgecolor=(0.08627450980392157, 0.6392156862745098, 0.2901960784313726, 1.0), linewidth=1.5, capstyle='butt', fill=False)
            c.path([[9.999999999599998, 7.999999999999999], [9.999999999999998, 7.999999999999999], [9.999999999999998, 6.999999999999999], [8.999999999999998, 6.999999999999999], [8.999999999999998, 5.999999999999999]], [1, 2, 2, 2, 2], id='target_outline', capstyle='butt', fill=False)
            for object_id, points in _geometry_01:
                c.line(points, id=object_id, solid_capstyle='butt')
            c.path([[0.5, 0.0], [1.5, 0.0], [2.5, 0.0], [2.5, 1.0], [1.5, 1.0], [0.5, 1.0], [0.5, 0.0]], [1, 2, 2, 2, 2, 2, 79], id='piece_A_outline', capstyle='butt', fill=False)
            c.line([[1.5, 0.0], [1.5, 1.0]], id='piece_A_grid_00', solid_capstyle='butt')
            c.path([[5.5, 0.0], [6.5, 0.0], [7.5, 0.0], [7.5, 1.0], [6.5, 1.0], [6.5, 2.0], [5.5, 2.0], [5.5, 1.0], [5.5, 0.0]], [1, 2, 2, 2, 2, 2, 2, 2, 79], id='piece_B_outline', capstyle='butt', fill=False)
            c.line([[5.5, 1.0], [6.5, 1.0]], id='piece_B_grid_00', solid_capstyle='butt')
            c.line([[6.5, 0.0], [6.5, 1.0]], id='piece_B_grid_01', solid_capstyle='butt')
            c.path([[10.0, 0.0], [11.0, 0.0], [12.0, 0.0], [12.0, 1.0], [13.0, 1.0], [13.0, 2.0], [12.0, 2.0], [11.0, 2.0], [11.0, 1.0], [10.0, 1.0], [10.0, 0.0]], [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 79], id='piece_C_outline', capstyle='butt', fill=False)
            for object_id, points in [('piece_C_grid_00', [[11.0, 0.0], [11.0, 1.0]]), ('piece_C_grid_01', [[11.0, 1.0], [12.0, 1.0]]), ('piece_C_grid_02', [[12.0, 1.0], [12.0, 2.0]])]:
                c.line(points, id=object_id, solid_capstyle='butt')
            c.path([[15.5, 0.0], [16.5, 0.0], [17.5, 0.0], [17.5, 1.0], [17.5, 2.0], [16.5, 2.0], [16.5, 3.0], [15.5, 3.0], [15.5, 2.0], [15.5, 1.0], [15.5, 0.0]], [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 79], id='piece_D_outline', edgecolor=(0.08627450980392157, 0.6392156862745098, 0.2901960784313726, 1.0), linewidth=1.5, capstyle='butt', fill=False)
            for object_id, points in [('piece_D_grid_00', [[15.5, 1.0], [16.5, 1.0]]), ('piece_D_grid_01', [[15.5, 2.0], [16.5, 2.0]]), ('piece_D_grid_02', [[16.5, 0.0], [16.5, 1.0]]), ('piece_D_grid_03', [[16.5, 1.0], [16.5, 2.0]]), ('piece_D_grid_04', [[16.5, 1.0], [17.5, 1.0]])]:
                c.line(points, id=object_id, solid_capstyle='butt')
            c.path([[20.0, 0.0], [21.0, 0.0], [22.0, 0.0], [23.0, 0.0], [23.0, 1.0], [23.0, 2.0], [22.0, 2.0], [22.0, 1.0], [21.0, 1.0], [21.0, 2.0], [20.0, 2.0], [20.0, 1.0], [20.0, 0.0]], [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 79], id='piece_E_outline', capstyle='butt', fill=False)
            for object_id, points in [('piece_E_grid_00', [[20.0, 1.0], [21.0, 1.0]]), ('piece_E_grid_01', [[21.0, 0.0], [21.0, 1.0]]), ('piece_E_grid_02', [[22.0, 0.0], [22.0, 1.0]]), ('piece_E_grid_03', [[22.0, 1.0], [23.0, 1.0]])]:
                c.line(points, id=object_id, solid_capstyle='butt')
            c.circle([10.5, 8.5], 0.075, id='target_dot', zorder=4, facecolor=(0.0, 0.0, 0.0, 1.0))
            for object_id, text, anchor in [('piece_A_label', '(A)', (1.5, -0.5)), ('piece_B_label', '(B)', (6.5, -0.5)), ('piece_C_label', '(C)', (11.5, -0.5)), ('piece_D_label', '(D)', (16.5, -0.5)), ('piece_E_label', '(E)', (21.5, -0.5))]:
                c.text(text, anchor, id=object_id, va='top', rotation_mode='default')
            for object_id, points in [(None, [[10.0, 8.0], [12.0, 8.0]]), (None, [[12.0, 8.0], [12.0, 10.0]]), (None, [[10.0, 10.0], [12.0, 10.0]])]:
                c.line(points, id=object_id, zorder=9, color='#16A34A', solid_capstyle='butt')
            for object_id, points in [(None, [[10.0, 8.0], [10.0, 9.0]]), (None, [[11.0, 8.0], [11.0, 10.0]]), (None, [[10.0, 9.0], [12.0, 9.0]]), (None, [[15.5, 2.0], [16.5, 2.0]]), (None, [[16.5, 0.0], [16.5, 2.0]]), (None, [[15.5, 1.0], [17.5, 1.0]])]:
                c.line(points, id=object_id, zorder=9, color='#16A34A', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            return c.save(output_path)
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Plane561')
    parser.add_argument('output', nargs='?')
    parser.add_argument('--variant', choices=('C01', 'C02', 'C03'))
    args = parser.parse_args()
    print(Plane561().draw(args.output, variant=args.variant))
