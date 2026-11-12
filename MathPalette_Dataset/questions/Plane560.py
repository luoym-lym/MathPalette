"""Collected question Plane560; construction on the shared drawing protocol."""
from pathlib import Path
import sys
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from MathPalette_Dataset.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane560:
    variants = ('C01',)

    def __init__(self):
        self.id = 'Plane560'
        self.source_dataset = 'Author Designed'
        self.source_key = 'author-extensions95-v1:Plane243/extension_01'
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
         [10.5, 9.0],
         [11.5, 9.0],
         [11.5, 8.0],
         [12.5, 8.0],
         [12.5, 7.0],
         [12.5, 6.0],
         [13.5, 6.0],
         [13.5, 7.0],
         [13.5, 8.0],
         [13.5, 9.0],
         [14.5, 9.0],
         [14.5, 10.0],
         [14.5, 11.0],
         [13.5, 11.0],
         [12.5, 11.0],
         [12.5, 10.0],
         [11.5, 10.0],
         [10.5, 10.0],
         [9.5, 10.0],
         [8.5, 10.0],
         [8.5, 9.0],
         [8.5, 8.0],
         [8.5, 7.0],
         [8.5, 6.0]]
        self._geometry_02 = [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 79]

    def draw(self, output_path=None, *, variant=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if variant not in self.variants:
                raise ValueError('Unknown Special variant: ' + str(variant))
            return getattr(self, 'draw_' + variant)(output_path)
        with Canvas(PLANE, xlim=[-0.5749999999999993, 23.575000000000006], ylim=[-7.215245790834782, 16.934754209165224], axes_position=[0.05, 0.05, 0.9, 0.9], coordinate_axes=False) as c:
            c.path(self._geometry_01, self._geometry_02, id='target_outline', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            for object_id, points in [('target_grid_00', [[8.5, 7.0], [9.5, 7.0]]), ('target_grid_01', [[8.5, 8.0], [9.5, 8.0]]), ('target_grid_02', [[8.5, 9.0], [9.5, 9.0]]), ('target_grid_03', [[9.5, 6.0], [9.5, 7.0]]), ('target_grid_04', [[9.5, 7.0], [9.5, 8.0]]), ('target_grid_05', [[9.5, 7.0], [10.5, 7.0]]), ('target_grid_06', [[9.5, 8.0], [9.5, 9.0]]), ('target_grid_07', [[9.5, 8.0], [10.5, 8.0]]), ('target_grid_08', [[9.5, 9.0], [9.5, 10.0]]), ('target_grid_09', [[9.5, 9.0], [10.5, 9.0]]), ('target_grid_10', [[10.5, 9.0], [10.5, 10.0]]), ('target_grid_11', [[11.5, 9.0], [11.5, 10.0]]), ('target_grid_12', [[11.5, 9.0], [12.5, 9.0]]), ('target_grid_13', [[12.5, 7.0], [13.5, 7.0]]), ('target_grid_14', [[12.5, 8.0], [12.5, 9.0]]), ('target_grid_15', [[12.5, 8.0], [13.5, 8.0]]), ('target_grid_16', [[12.5, 9.0], [12.5, 10.0]]), ('target_grid_17', [[12.5, 9.0], [13.5, 9.0]]), ('target_grid_18', [[12.5, 10.0], [13.5, 10.0]]), ('target_grid_19', [[13.5, 9.0], [13.5, 10.0]]), ('target_grid_20', [[13.5, 10.0], [13.5, 11.0]]), ('target_grid_21', [[13.5, 10.0], [14.5, 10.0]])]:
                c.line(points, id=object_id, solid_capstyle='butt')
            c.path([[0.0, 0.0], [1.0, 0.0], [2.0, 0.0], [3.0, 0.0], [3.0, 1.0], [2.0, 1.0], [1.0, 1.0], [0.0, 1.0], [0.0, 0.0]], [1, 2, 2, 2, 2, 2, 2, 2, 79], id='piece_A_outline', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.line([[1.0, 0.0], [1.0, 1.0]], id='piece_A_grid_00', solid_capstyle='butt')
            c.line([[2.0, 0.0], [2.0, 1.0]], id='piece_A_grid_01', solid_capstyle='butt')
            c.path([[5.5, 0.0], [6.5, 0.0], [7.5, 0.0], [7.5, 1.0], [6.5, 1.0], [6.5, 2.0], [5.5, 2.0], [5.5, 1.0], [5.5, 0.0]], [1, 2, 2, 2, 2, 2, 2, 2, 79], id='piece_B_outline', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.line([[5.5, 1.0], [6.5, 1.0]], id='piece_B_grid_00', solid_capstyle='butt')
            c.line([[6.5, 0.0], [6.5, 1.0]], id='piece_B_grid_01', solid_capstyle='butt')
            c.path([[10.5, 0.0], [11.5, 0.0], [12.5, 0.0], [12.5, 1.0], [12.5, 2.0], [11.5, 2.0], [10.5, 2.0], [10.5, 1.0], [10.5, 0.0]], [1, 2, 2, 2, 2, 2, 2, 2, 79], id='piece_C_outline', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            for object_id, points in [('piece_C_grid_00', [[10.5, 1.0], [11.5, 1.0]]), ('piece_C_grid_01', [[11.5, 0.0], [11.5, 1.0]]), ('piece_C_grid_02', [[11.5, 1.0], [11.5, 2.0]]), ('piece_C_grid_03', [[11.5, 1.0], [12.5, 1.0]])]:
                c.line(points, id=object_id, solid_capstyle='butt')
            c.path([[15.0, 0.0], [16.0, 0.0], [17.0, 0.0], [18.0, 0.0], [18.0, 1.0], [17.0, 1.0], [17.0, 2.0], [16.0, 2.0], [16.0, 1.0], [15.0, 1.0], [15.0, 0.0]], [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 79], id='piece_D_outline', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            for object_id, points in [('piece_D_grid_00', [[16.0, 0.0], [16.0, 1.0]]), ('piece_D_grid_01', [[16.0, 1.0], [17.0, 1.0]]), ('piece_D_grid_02', [[17.0, 0.0], [17.0, 1.0]])]:
                c.line(points, id=object_id, solid_capstyle='butt')
            c.path([[20.0, 0.0], [21.0, 0.0], [22.0, 0.0], [23.0, 0.0], [23.0, 1.0], [22.0, 1.0], [21.0, 1.0], [21.0, 2.0], [20.0, 2.0], [20.0, 1.0], [20.0, 0.0]], [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 79], id='piece_E_outline', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            for object_id, points in [('piece_E_grid_00', [[20.0, 1.0], [21.0, 1.0]]), ('piece_E_grid_01', [[21.0, 0.0], [21.0, 1.0]]), ('piece_E_grid_02', [[22.0, 0.0], [22.0, 1.0]])]:
                c.line(points, id=object_id, solid_capstyle='butt')
            c.circle([13.0, 9.5], 0.075, id='target_dot', zorder=4, facecolor=[0.0, 0.0, 0.0, 1.0])
            for object_id, text, anchor in [('piece_A_label', '(A)', [1.5, -0.5]), ('piece_B_label', '(B)', [6.5, -0.5]), ('piece_C_label', '(C)', [11.5, -0.5]), ('piece_D_label', '(D)', [16.5, -0.5]), ('piece_E_label', '(E)', [21.5, -0.5])]:
                c.text(text, anchor, id=object_id, va='top', rotation_mode='default')
            return c.save(output_path)

    def draw_C01(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane560_C01.png'
        with Canvas(PLANE, xlim=(-0.5749999999999993, 23.575000000000006), ylim=(-7.215245790834782, 16.934754209165224), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
            c.path([[8.500000000000002, 6.000000000000002], [9.500000000000002, 6.000000000000002], [10.500000000000002, 6.000000000000002], [10.500000000000002, 7.000000000000002], [10.500000000000002, 8.000000000000002], [10.500000000000002, 9.000000000000002], [11.500000000000002, 9.000000000000002], [11.500000000000002, 8.000000000000002], [12.500000000000004, 8.000000000000002], [12.500000000000004, 7.000000000000002], [12.500000000000004, 6.000000000000002], [13.500000000000004, 6.000000000000002], [13.500000000000004, 7.000000000000002], [13.500000000000004, 8.000000000000002], [13.500000000000004, 9.000000000000002]], [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2], id='target_outline', capstyle='butt', fill=False)
            c.path([[13.500000000000004, 9.000000000000002], [14.500000000000004, 9.000000000000002], [14.500000000000004, 10.000000000000002], [14.500000000000004, 11.000000000000002], [13.500000000000004, 11.000000000000002], [12.500000000000004, 11.000000000000002], [12.500000000000004, 10.000000000000002], [11.500000000000002, 10.000000000000002]], [1, 2, 2, 2, 2, 2, 2, 2], id='target_outline', edgecolor=(0.08627450980392157, 0.6392156862745098, 0.2901960784313726, 1.0), capstyle='butt', fill=False)
            c.path([[11.500000000000002, 10.000000000000002], [10.500000000000002, 10.000000000000002], [9.500000000000002, 10.000000000000002], [8.500000000000002, 10.000000000000002], [8.500000000000002, 9.000000000000002], [8.500000000000002, 8.000000000000002], [8.500000000000002, 7.000000000000002], [8.500000000000002, 6.000000000000002]], [1, 2, 2, 2, 2, 2, 2, 2], id='target_outline', capstyle='butt', fill=False)
            for object_id, points in [('target_grid_00', [[8.5, 7.0], [9.5, 7.0]]), ('target_grid_01', [[8.5, 8.0], [9.5, 8.0]]), ('target_grid_02', [[8.5, 9.0], [9.5, 9.0]]), ('target_grid_03', [[9.5, 6.0], [9.5, 7.0]]), ('target_grid_04', [[9.5, 7.0], [9.5, 8.0]]), ('target_grid_05', [[9.5, 7.0], [10.5, 7.0]]), ('target_grid_06', [[9.5, 8.0], [9.5, 9.0]]), ('target_grid_07', [[9.5, 8.0], [10.5, 8.0]]), ('target_grid_08', [[9.5, 9.0], [9.5, 10.0]]), ('target_grid_09', [[9.5, 9.0], [10.5, 9.0]]), ('target_grid_10', [[10.5, 9.0], [10.5, 10.0]]), ('target_grid_11', [[11.5, 9.0], [11.5, 10.0]]), ('target_grid_12', [[11.5, 9.0], [12.5, 9.0]]), ('target_grid_13', [[12.5, 7.0], [13.5, 7.0]]), ('target_grid_14', [[12.5, 8.0], [12.5, 9.0]]), ('target_grid_15', [[12.5, 8.0], [13.5, 8.0]]), ('target_grid_16', [[12.5, 9.0], [12.5, 10.0]]), ('target_grid_17', [[12.5, 9.0], [13.5, 9.0]]), ('target_grid_18', [[12.5, 10.0], [13.5, 10.0]]), ('target_grid_19', [[13.5, 9.0], [13.5, 10.0]]), ('target_grid_20', [[13.5, 10.0], [13.5, 11.0]]), ('target_grid_21', [[13.5, 10.0], [14.5, 10.0]])]:
                c.line(points, id=object_id, solid_capstyle='butt')
            c.path([[0.0, 0.0], [1.0, 0.0], [2.0, 0.0], [3.0, 0.0], [3.0, 1.0], [2.0, 1.0], [1.0, 1.0], [0.0, 1.0], [0.0, 0.0]], [1, 2, 2, 2, 2, 2, 2, 2, 79], id='piece_A_outline', capstyle='butt', fill=False)
            c.line([[1.0, 0.0], [1.0, 1.0]], id='piece_A_grid_00', solid_capstyle='butt')
            c.line([[2.0, 0.0], [2.0, 1.0]], id='piece_A_grid_01', solid_capstyle='butt')
            c.path([[5.5, 0.0], [6.5, 0.0], [7.5, 0.0], [7.5, 1.0], [6.5, 1.0], [6.5, 2.0], [5.5, 2.0], [5.5, 1.0], [5.5, 0.0]], [1, 2, 2, 2, 2, 2, 2, 2, 79], id='piece_B_outline', capstyle='butt', fill=False)
            c.line([[5.5, 1.0], [6.5, 1.0]], id='piece_B_grid_00', solid_capstyle='butt')
            c.line([[6.5, 0.0], [6.5, 1.0]], id='piece_B_grid_01', solid_capstyle='butt')
            c.path([[10.5, 0.0], [11.5, 0.0], [12.5, 0.0], [12.5, 1.0], [12.5, 2.0], [11.5, 2.0], [10.5, 2.0], [10.5, 1.0], [10.5, 0.0]], [1, 2, 2, 2, 2, 2, 2, 2, 79], id='piece_C_outline', capstyle='butt', fill=False)
            for object_id, points in [('piece_C_grid_00', [[10.5, 1.0], [11.5, 1.0]]), ('piece_C_grid_01', [[11.5, 0.0], [11.5, 1.0]]), ('piece_C_grid_02', [[11.5, 1.0], [11.5, 2.0]]), ('piece_C_grid_03', [[11.5, 1.0], [12.5, 1.0]])]:
                c.line(points, id=object_id, solid_capstyle='butt')
            c.path([[15.0, 0.0], [16.0, 0.0], [17.0, 0.0], [18.0, 0.0], [18.0, 1.0], [17.0, 1.0], [17.0, 2.0], [16.0, 2.0], [16.0, 1.0], [15.0, 1.0], [15.0, 0.0]], [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 79], id='piece_D_outline', edgecolor=(0.08627450980392157, 0.6392156862745098, 0.2901960784313726, 1.0), linewidth=3.0, capstyle='butt', fill=False)
            for object_id, points in [('piece_D_grid_00', [[16.0, 0.0], [16.0, 1.0]]), ('piece_D_grid_01', [[16.0, 1.0], [17.0, 1.0]]), ('piece_D_grid_02', [[17.0, 0.0], [17.0, 1.0]])]:
                c.line(points, id=object_id, solid_capstyle='butt')
            c.path([[20.0, 0.0], [21.0, 0.0], [22.0, 0.0], [23.0, 0.0], [23.0, 1.0], [22.0, 1.0], [21.0, 1.0], [21.0, 2.0], [20.0, 2.0], [20.0, 1.0], [20.0, 0.0]], [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 79], id='piece_E_outline', capstyle='butt', fill=False)
            for object_id, points in [('piece_E_grid_00', [[20.0, 1.0], [21.0, 1.0]]), ('piece_E_grid_01', [[21.0, 0.0], [21.0, 1.0]]), ('piece_E_grid_02', [[22.0, 0.0], [22.0, 1.0]])]:
                c.line(points, id=object_id, solid_capstyle='butt')
            c.circle([13.0, 9.5], 0.075, id='target_dot', zorder=4, facecolor=(0.0, 0.0, 0.0, 1.0))
            for object_id, text, anchor in [('piece_A_label', '(A)', (1.5, -0.5)), ('piece_B_label', '(B)', (6.5, -0.5)), ('piece_C_label', '(C)', (11.5, -0.5)), ('piece_D_label', '(D)', (16.5, -0.5)), ('piece_E_label', '(E)', (21.5, -0.5))]:
                c.text(text, anchor, id=object_id, va='top', rotation_mode='default')
            for object_id, points in [(None, [[11.5, 9.0], [14.5, 9.0]]), (None, [[11.5, 9.0], [11.5, 10.0]]), (None, [[13.5, 10.0], [14.5, 10.0]])]:
                c.line(points, id=object_id, zorder=9, color='#16A34A', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            return c.save(output_path)
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Plane560')
    parser.add_argument('output', nargs='?')
    parser.add_argument('--variant', choices=('C01',))
    args = parser.parse_args()
    print(Plane560().draw(args.output, variant=args.variant))
