"""Collected question Plane563; construction on the shared drawing protocol."""
from pathlib import Path
import sys
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from MathPalette_Dataset.drawing import Canvas, PLANE

class Plane563:
    variants = ('C01', 'C02', 'C03', 'C04', 'C05', 'C06')

    def __init__(self):
        self._samples_001 = [
            [8.5, 7.0], [9.5, 7.0], [10.5, 7.0], [10.5, 6.0], [11.5, 6.0], [12.5, 6.0], [13.5, 6.0],
            [14.5, 6.0], [14.5, 7.0], [14.5, 8.0], [14.5, 9.0], [13.5, 9.0], [12.5, 9.0], [12.5, 10.0],
            [13.5, 10.0], [14.5, 10.0], [14.5, 11.0], [13.5, 11.0], [12.5, 11.0], [11.5, 11.0], [10.5, 11.0],
            [10.5, 10.0], [10.5, 9.0], [9.5, 9.0], [9.5, 8.0], [8.5, 8.0], [8.5, 7.0]
        ]
        self._geometry_02 = [1] + [2] * 25 + [79]
        self._geometry_03 = [
            ('target_grid_00', [[9.5, 7.0], [9.5, 8.0]]), ('target_grid_01', [[9.5, 8.0], [10.5, 8.0]]),
            ('target_grid_02', [[10.5, 7.0], [10.5, 8.0]]), ('target_grid_03', [[10.5, 7.0], [11.5, 7.0]]),
            ('target_grid_04', [[10.5, 8.0], [10.5, 9.0]]), ('target_grid_05', [[10.5, 8.0], [11.5, 8.0]]),
            ('target_grid_06', [[10.5, 9.0], [11.5, 9.0]]), ('target_grid_07', [[10.5, 10.0], [11.5, 10.0]]),
            ('target_grid_08', [[11.5, 6.0], [11.5, 7.0]]), ('target_grid_09', [[11.5, 7.0], [11.5, 8.0]]),
            ('target_grid_10', [[11.5, 7.0], [12.5, 7.0]]), ('target_grid_11', [[11.5, 8.0], [11.5, 9.0]]),
            ('target_grid_12', [[11.5, 8.0], [12.5, 8.0]]), ('target_grid_13', [[11.5, 9.0], [11.5, 10.0]]),
            ('target_grid_14', [[11.5, 9.0], [12.5, 9.0]]), ('target_grid_15', [[11.5, 10.0], [11.5, 11.0]]),
            ('target_grid_16', [[11.5, 10.0], [12.5, 10.0]]), ('target_grid_17', [[12.5, 6.0], [12.5, 7.0]]),
            ('target_grid_18', [[12.5, 7.0], [12.5, 8.0]]), ('target_grid_19', [[12.5, 7.0], [13.5, 7.0]]),
            ('target_grid_20', [[12.5, 8.0], [12.5, 9.0]]), ('target_grid_21', [[12.5, 8.0], [13.5, 8.0]]),
            ('target_grid_22', [[12.5, 10.0], [12.5, 11.0]]), ('target_grid_23', [[13.5, 6.0], [13.5, 7.0]]),
            ('target_grid_24', [[13.5, 7.0], [13.5, 8.0]]), ('target_grid_25', [[13.5, 7.0], [14.5, 7.0]]),
            ('target_grid_26', [[13.5, 8.0], [13.5, 9.0]]), ('target_grid_27', [[13.5, 8.0], [14.5, 8.0]]),
            ('target_grid_28', [[13.5, 10.0], [13.5, 11.0]])
        ]

    def draw(self, output_path=None, *, variant=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / (self.__class__.__name__ + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if variant not in self.variants:
                raise ValueError('Unknown Special variant: ' + str(variant))
            return getattr(self, 'draw_' + variant)(output_path)
        with Canvas(PLANE, xlim=(-0.0625, 23.562499999999993), ylim=(-6.9442621866861955, 16.680737813313797)) as c:
            c.path(self._samples_001, self._geometry_02, id='target_outline', capstyle='butt', fill=False)
            for object_id, points in self._geometry_03:
                c.line(points, id=object_id, solid_capstyle='butt')
            c.path([[0.5, 0.0], [1.5, 0.0], [2.5, 0.0], [2.5, 1.0], [1.5, 1.0], [1.5, 2.0], [0.5, 2.0], [0.5, 1.0], [0.5, 0.0]], [1, 2, 2, 2, 2, 2, 2, 2, 79], id='piece_A_outline', capstyle='butt', fill=False)
            c.line([[0.5, 1.0], [1.5, 1.0]], id='piece_A_grid_00', solid_capstyle='butt')
            c.line([[1.5, 0.0], [1.5, 1.0]], id='piece_A_grid_01', solid_capstyle='butt')
            c.path([[4.5, 0.0], [5.5, 0.0], [6.5, 0.0], [7.5, 0.0], [8.5, 0.0], [8.5, 1.0], [7.5, 1.0], [6.5, 1.0], [5.5, 1.0], [4.5, 1.0], [4.5, 0.0]], [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 79], id='piece_B_outline', capstyle='butt', fill=False)
            for object_id, points in [('piece_B_grid_00', [[5.5, 0.0], [5.5, 1.0]]), ('piece_B_grid_01', [[6.5, 0.0], [6.5, 1.0]]), ('piece_B_grid_02', [[7.5, 0.0], [7.5, 1.0]])]:
                c.line(points, id=object_id, solid_capstyle='butt')
            c.path([[10.0, 0.0], [11.0, 0.0], [12.0, 0.0], [12.0, 1.0], [13.0, 1.0], [13.0, 2.0], [12.0, 2.0], [11.0, 2.0], [11.0, 1.0], [10.0, 1.0], [10.0, 0.0]], [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 79], id='piece_C_outline', capstyle='butt', fill=False)
            for object_id, points in [('piece_C_grid_00', [[11.0, 0.0], [11.0, 1.0]]), ('piece_C_grid_01', [[11.0, 1.0], [12.0, 1.0]]), ('piece_C_grid_02', [[12.0, 1.0], [12.0, 2.0]])]:
                c.line(points, id=object_id, solid_capstyle='butt')
            c.path([[15.0, 0.0], [16.0, 0.0], [17.0, 0.0], [18.0, 0.0], [18.0, 1.0], [17.0, 1.0], [16.0, 1.0], [16.0, 2.0], [16.0, 3.0], [15.0, 3.0], [15.0, 2.0], [15.0, 1.0], [15.0, 0.0]], [1] + [2] * 11 + [79], id='piece_D_outline', capstyle='butt', fill=False)
            for object_id, points in [('piece_D_grid_00', [[15.0, 1.0], [16.0, 1.0]]), ('piece_D_grid_01', [[15.0, 2.0], [16.0, 2.0]]), ('piece_D_grid_02', [[16.0, 0.0], [16.0, 1.0]]), ('piece_D_grid_03', [[17.0, 0.0], [17.0, 1.0]])]:
                c.line(points, id=object_id, solid_capstyle='butt')
            c.path([[20.0, 0.0], [21.0, 0.0], [22.0, 0.0], [22.0, 1.0], [23.0, 1.0], [23.0, 2.0], [23.0, 3.0], [22.0, 3.0], [22.0, 2.0], [21.0, 2.0], [21.0, 1.0], [20.0, 1.0], [20.0, 0.0]], [1] + [2] * 11 + [79], id='piece_E_outline', capstyle='butt', fill=False)
            for object_id, points in [('piece_E_grid_00', [[21.0, 0.0], [21.0, 1.0]]), ('piece_E_grid_01', [[21.0, 1.0], [22.0, 1.0]]), ('piece_E_grid_02', [[22.0, 1.0], [22.0, 2.0]]), ('piece_E_grid_03', [[22.0, 2.0], [23.0, 2.0]])]:
                c.line(points, id=object_id, solid_capstyle='butt')
            c.circle([12.0, 7.5], 0.075, id='target_dot', zorder=4, facecolor='black')
            for object_id, text, anchor in [('piece_A_label', '(A)', (1.5, -0.5)), ('piece_B_label', '(B)', (6.5, -0.5)), ('piece_C_label', '(C)', (11.5, -0.5)), ('piece_D_label', '(D)', (16.5, -0.5)), ('piece_E_label', '(E)', (21.5, -0.5))]:
                c.text(text, anchor, id=object_id, va='top')
            return c.save(output_path)

    def _draw_choices(self, c, kw=None, custom=None):
        _kw = kw or {}
        c.path(self._samples_001, self._geometry_02, id='target_outline', capstyle='butt', fill=False)
        for object_id, points in self._geometry_03:
            c.line(points, id=object_id, solid_capstyle='butt')
        c.path([[0.5, 0.0], [1.5, 0.0], [2.5, 0.0], [2.5, 1.0], [1.5, 1.0], [1.5, 2.0], [0.5, 2.0], [0.5, 1.0], [0.5, 0.0]], [1, 2, 2, 2, 2, 2, 2, 2, 79], id='piece_A_outline', capstyle='butt', fill=False)
        c.line([[0.5, 1.0], [1.5, 1.0]], id='piece_A_grid_00', solid_capstyle='butt')
        c.line([[1.5, 0.0], [1.5, 1.0]], id='piece_A_grid_01', solid_capstyle='butt')
        c.path([[4.5, 0.0], [5.5, 0.0], [6.5, 0.0], [7.5, 0.0], [8.5, 0.0], [8.5, 1.0], [7.5, 1.0], [6.5, 1.0], [5.5, 1.0], [4.5, 1.0], [4.5, 0.0]], [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 79], id='piece_B_outline', capstyle='butt', fill=False)
        for object_id, points in [('piece_B_grid_00', [[5.5, 0.0], [5.5, 1.0]]), ('piece_B_grid_01', [[6.5, 0.0], [6.5, 1.0]]), ('piece_B_grid_02', [[7.5, 0.0], [7.5, 1.0]])]:
            c.line(points, id=object_id, solid_capstyle='butt')
        c.path([[10.0, 0.0], [11.0, 0.0], [12.0, 0.0], [12.0, 1.0], [13.0, 1.0], [13.0, 2.0], [12.0, 2.0], [11.0, 2.0], [11.0, 1.0], [10.0, 1.0], [10.0, 0.0]], [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 79], id='piece_C_outline', capstyle='butt', fill=False, **_kw.get(7, {}))
        for object_id, points in [('piece_C_grid_00', [[11.0, 0.0], [11.0, 1.0]]), ('piece_C_grid_01', [[11.0, 1.0], [12.0, 1.0]]), ('piece_C_grid_02', [[12.0, 1.0], [12.0, 2.0]])]:
            c.line(points, id=object_id, solid_capstyle='butt')
        c.path([[15.0, 0.0], [16.0, 0.0], [17.0, 0.0], [18.0, 0.0], [18.0, 1.0], [17.0, 1.0], [16.0, 1.0], [16.0, 2.0], [16.0, 3.0], [15.0, 3.0], [15.0, 2.0], [15.0, 1.0], [15.0, 0.0]], [1] + [2] * 11 + [79], id='piece_D_outline', capstyle='butt', fill=False, **_kw.get(9, {}))
        for object_id, points in [('piece_D_grid_00', [[15.0, 1.0], [16.0, 1.0]]), ('piece_D_grid_01', [[15.0, 2.0], [16.0, 2.0]]), ('piece_D_grid_02', [[16.0, 0.0], [16.0, 1.0]]), ('piece_D_grid_03', [[17.0, 0.0], [17.0, 1.0]])]:
            c.line(points, id=object_id, solid_capstyle='butt')
        c.path([[20.0, 0.0], [21.0, 0.0], [22.0, 0.0], [22.0, 1.0], [23.0, 1.0], [23.0, 2.0], [23.0, 3.0], [22.0, 3.0], [22.0, 2.0], [21.0, 2.0], [21.0, 1.0], [20.0, 1.0], [20.0, 0.0]], [1] + [2] * 11 + [79], id='piece_E_outline', capstyle='butt', fill=False, **_kw.get(11, {}))
        for object_id, points in [('piece_E_grid_00', [[21.0, 0.0], [21.0, 1.0]]), ('piece_E_grid_01', [[21.0, 1.0], [22.0, 1.0]]), ('piece_E_grid_02', [[22.0, 1.0], [22.0, 2.0]]), ('piece_E_grid_03', [[22.0, 2.0], [23.0, 2.0]])]:
            c.line(points, id=object_id, solid_capstyle='butt')
        c.circle([12.0, 7.5], 0.075, id='target_dot', zorder=4, facecolor='black')
        for object_id, text, anchor in [('piece_A_label', '(A)', (1.5, -0.5)), ('piece_B_label', '(B)', (6.5, -0.5)), ('piece_C_label', '(C)', (11.5, -0.5)), ('piece_D_label', '(D)', (16.5, -0.5)), ('piece_E_label', '(E)', (21.5, -0.5))]:
            c.text(text, anchor, id=object_id, va='top')
        if custom and 15 in custom:
            custom[15](c)
        else:
            for object_id, points in [(None, [[21.0, 0.0], [21.0, 1.0]]), (None, [[21.0, 1.0], [22.0, 1.0]]), (None, [[22.0, 1.0], [22.0, 2.0]]), (None, [[22.0, 2.0], [23.0, 2.0]]), (None, [[11.5, 7.0], [12.5, 7.0]]), (None, [[12.5, 7.0], [12.5, 8.0]]), (None, [[11.5, 8.0], [12.5, 8.0]]), (None, [[11.5, 7.0], [11.5, 8.0]])]:
                c.line(points, id=object_id, zorder=9, color='#16A34A', solid_capstyle='butt')
        c.line([[12.5, 7.0], [13.5, 8.0]], zorder=9, linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt', **_kw.get(16, {'color': '#16A34A'}))

    def draw_C01(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane563_C01.png'
        with Canvas(PLANE, xlim=(-0.0625, 23.562499999999993), ylim=(-6.9442621866861955, 16.680737813313797)) as c:

            def _slot_15(c):
                for object_id, points in [(None, [[11.5, 7.0], [12.5, 7.0]]), (None, [[12.5, 7.0], [12.5, 8.0]]), (None, [[11.5, 8.0], [12.5, 8.0]]), (None, [[11.5, 7.0], [11.5, 8.0]])]:
                    c.line(points, id=object_id, zorder=9, color='#16A34A', solid_capstyle='butt')
            self._draw_choices(c, custom={15: _slot_15}, kw={9: {'edgecolor': '#16A34A', 'linewidth': 1.5}})
            return c.save(output_path)

    def draw_C02(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane563_C02.png'
        with Canvas(PLANE, xlim=(-0.0625, 23.562499999999993), ylim=(-6.9442621866861955, 16.680737813313797)) as c:
            self._draw_choices(c, kw={11: {'edgecolor': '#16A34A', 'linewidth': 1.5}})
            return c.save(output_path)

    def draw_C03(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane563_C03.png'
        with Canvas(PLANE, xlim=(-0.0625, 23.562499999999993), ylim=(-6.9442621866861955, 16.680737813313797)) as c:

            def _slot_15(c):
                for object_id, points in [(None, [[11.0, 0.0], [11.0, 1.0]]), (None, [[11.0, 1.0], [12.0, 1.0]]), (None, [[12.0, 1.0], [12.0, 2.0]]), (None, [[11.5, 7.0], [12.5, 7.0]]), (None, [[12.5, 7.0], [12.5, 8.0]]), (None, [[11.5, 8.0], [12.5, 8.0]]), (None, [[11.5, 7.0], [11.5, 8.0]])]:
                    c.line(points, id=object_id, zorder=9, color='#16A34A', solid_capstyle='butt')
            self._draw_choices(c, custom={15: _slot_15}, kw={7: {'edgecolor': '#16A34A', 'linewidth': 1.5}})
            return c.save(output_path)

    def draw_C04(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane563_C04.png'
        with Canvas(PLANE, xlim=(-0.0625, 23.562499999999993), ylim=(-6.9442621866861955, 16.680737813313797)) as c:

            def _slot_15(c):
                for object_id, points in [(None, [[21.0, 0.0], [21.0, 1.0]]), (None, [[21.0, 1.0], [22.0, 1.0]]), (None, [[22.0, 1.0], [22.0, 2.0]]), (None, [[22.0, 2.0], [23.0, 2.0]]), (None, [[11.5, 7.0], [12.5, 7.0]]), (None, [[12.5, 7.0], [12.5, 8.0]]), (None, [[11.5, 8.0], [12.5, 8.0]]), (None, [[11.5, 7.0], [11.5, 8.0]])]:
                    c.line(points, id=object_id, zorder=9, color='#DC2626', solid_capstyle='butt')
            self._draw_choices(c, custom={15: _slot_15}, kw={11: {'edgecolor': '#DC2626', 'linewidth': 1.5}, 16: {'color': '#DC2626'}})
            return c.save(output_path)

    def draw_C05(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane563_C05.png'
        with Canvas(PLANE, xlim=(-0.0625, 23.562499999999993), ylim=(-6.9442621866861955, 16.680737813313797)) as c:

            def _slot_15(c):
                for object_id, points in [(None, [[15.0, 1.0], [16.0, 1.0]]), (None, [[15.0, 2.0], [16.0, 2.0]]), (None, [[16.0, 0.0], [16.0, 1.0]]), (None, [[17.0, 0.0], [17.0, 1.0]]), (None, [[11.5, 7.0], [12.5, 7.0]]), (None, [[12.5, 7.0], [12.5, 8.0]]), (None, [[11.5, 8.0], [12.5, 8.0]]), (None, [[11.5, 7.0], [11.5, 8.0]]), (None, [[11.5, 7.0], [14.5, 7.0]]), (None, [[11.5, 7.0], [11.5, 10.0]]), (None, [[11.5, 10.0], [12.5, 10.0]]), (None, [[12.5, 8.0], [12.5, 10.0]]), (None, [[12.5, 8.0], [14.5, 8.0]]), (None, [[14.5, 7.0], [14.5, 8.0]])]:
                    c.line(points, id=object_id, zorder=9, color='#16A34A', solid_capstyle='butt')
            self._draw_choices(c, custom={15: _slot_15}, kw={9: {'edgecolor': '#16A34A', 'linewidth': 1.5}})
            return c.save(output_path)

    def draw_C06(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane563_C06.png'
        with Canvas(PLANE, xlim=(-0.0625, 23.562499999999993), ylim=(-6.9442621866861955, 16.680737813313797)) as c:

            def _slot_15(c):
                for object_id, points in [(None, [[15.0, 1.0], [16.0, 1.0]]), (None, [[15.0, 2.0], [16.0, 2.0]]), (None, [[16.0, 0.0], [16.0, 1.0]]), (None, [[17.0, 0.0], [17.0, 1.0]]), (None, [[11.5, 7.0], [12.5, 7.0]]), (None, [[12.5, 7.0], [12.5, 8.0]]), (None, [[11.5, 8.0], [12.5, 8.0]]), (None, [[11.5, 7.0], [11.5, 8.0]])]:
                    c.line(points, id=object_id, zorder=9, color='#16A34A', solid_capstyle='butt')
            self._draw_choices(c, custom={15: _slot_15}, kw={9: {'edgecolor': '#16A34A', 'linewidth': 1.5}})
            return c.save(output_path)
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Plane563')
    parser.add_argument('output', nargs='?')
    parser.add_argument('--variant', choices=('C01', 'C02', 'C03', 'C04', 'C05', 'C06'))
    args = parser.parse_args()
    print(Plane563().draw(args.output, variant=args.variant))
