"""Collected question Plane564; construction on the shared drawing protocol."""
from pathlib import Path
import sys
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from MathPalette_Dataset.drawing import Canvas, PLANE

class Plane564:
    variants = ('C01', 'C02', 'C03', 'C04', 'C05')

    def __init__(self):
        self._samples_001 = [
            [8.5, 5.999999999999998], [9.5, 5.999999999999998], [10.5, 5.999999999999998],
            [11.5, 5.999999999999998], [12.5, 5.999999999999998], [12.5, 6.999999999999998],
            [13.5, 6.999999999999998], [13.5, 5.999999999999998], [14.5, 5.999999999999998],
            [14.5, 6.999999999999998], [14.5, 7.999999999999998], [14.5, 8.999999999999998]
        ]
        self._samples_002 = [
            [12.5, 10.999999999999998], [11.5, 10.999999999999998], [10.5, 10.999999999999998],
            [9.5, 10.999999999999998], [8.5, 10.999999999999998], [8.5, 9.999999999999998],
            [9.5, 9.999999999999998], [10.5, 9.999999999999998], [10.5, 8.999999999999998],
            [10.5, 7.999999999999998], [11.5, 7.999999999999998], [11.5, 6.999999999999998],
            [10.5, 6.999999999999998], [9.5, 6.999999999999998], [8.5, 6.999999999999998],
            [8.5, 5.999999999999998]
        ]
        self._samples_003 = [
            [13.5, 10.999999999999998], [12.5, 10.999999999999998], [11.5, 10.999999999999998],
            [10.5, 10.999999999999998], [9.5, 10.999999999999998], [8.5, 10.999999999999998],
            [8.5, 9.999999999999998], [9.5, 9.999999999999998], [10.5, 9.999999999999998],
            [10.5, 8.999999999999998], [10.5, 7.999999999999998], [11.5, 7.999999999999998],
            [11.5, 6.999999999999998], [10.5, 6.999999999999998], [9.5, 6.999999999999998],
            [8.5, 6.999999999999998], [8.5, 5.999999999999998]
        ]
        self._geometry_01 = [
            [8.5, 6.0], [9.5, 6.0], [10.5, 6.0], [11.5, 6.0], [12.5, 6.0], [12.5, 7.0], [13.5, 7.0],
            [13.5, 6.0], [14.5, 6.0], [14.5, 7.0], [14.5, 8.0], [14.5, 9.0], [14.5, 10.0], [14.5, 11.0],
            [13.5, 11.0], [12.5, 11.0], [11.5, 11.0], [10.5, 11.0], [9.5, 11.0], [8.5, 11.0], [8.5, 10.0],
            [9.5, 10.0], [10.5, 10.0], [10.5, 9.0], [10.5, 8.0], [11.5, 8.0], [11.5, 7.0], [10.5, 7.0],
            [9.5, 7.0], [8.5, 7.0], [8.5, 6.0]
        ]
        self._geometry_02 = [1] + [2] * 29 + [79]
        self._geometry_03 = [
            ('target_grid_00', [[9.5, 6.0], [9.5, 7.0]]), ('target_grid_01', [[9.5, 10.0], [9.5, 11.0]]),
            ('target_grid_02', [[10.5, 6.0], [10.5, 7.0]]), ('target_grid_03', [[10.5, 9.0], [11.5, 9.0]]),
            ('target_grid_04', [[10.5, 10.0], [10.5, 11.0]]),
            ('target_grid_05', [[10.5, 10.0], [11.5, 10.0]]), ('target_grid_06', [[11.5, 6.0], [11.5, 7.0]]),
            ('target_grid_07', [[11.5, 7.0], [12.5, 7.0]]), ('target_grid_08', [[11.5, 8.0], [11.5, 9.0]]),
            ('target_grid_09', [[11.5, 8.0], [12.5, 8.0]]), ('target_grid_10', [[11.5, 9.0], [11.5, 10.0]]),
            ('target_grid_11', [[11.5, 9.0], [12.5, 9.0]]), ('target_grid_12', [[11.5, 10.0], [11.5, 11.0]]),
            ('target_grid_13', [[11.5, 10.0], [12.5, 10.0]]), ('target_grid_14', [[12.5, 7.0], [12.5, 8.0]]),
            ('target_grid_15', [[12.5, 8.0], [12.5, 9.0]]), ('target_grid_16', [[12.5, 8.0], [13.5, 8.0]]),
            ('target_grid_17', [[12.5, 9.0], [12.5, 10.0]]), ('target_grid_18', [[12.5, 9.0], [13.5, 9.0]]),
            ('target_grid_19', [[12.5, 10.0], [12.5, 11.0]]),
            ('target_grid_20', [[12.5, 10.0], [13.5, 10.0]]), ('target_grid_21', [[13.5, 7.0], [13.5, 8.0]]),
            ('target_grid_22', [[13.5, 7.0], [14.5, 7.0]]), ('target_grid_23', [[13.5, 8.0], [13.5, 9.0]]),
            ('target_grid_24', [[13.5, 8.0], [14.5, 8.0]]), ('target_grid_25', [[13.5, 9.0], [13.5, 10.0]]),
            ('target_grid_26', [[13.5, 9.0], [14.5, 9.0]]), ('target_grid_27', [[13.5, 10.0], [13.5, 11.0]]),
            ('target_grid_28', [[13.5, 10.0], [14.5, 10.0]])
        ]

    def _draw_base(self, c, kw=None, custom=None):
        _kw = kw or {}
        if custom and 0 in custom:
            custom[0](c)
        else:
            c.path(self._samples_001, [1] + [2] * 11, id='target_outline', capstyle='butt', fill=False)
            c.path([[14.5, 8.999999999999998], [14.5, 9.999999999999998], [14.5, 10.999999999999998], [13.5, 10.999999999999998], [12.5, 10.999999999999998]], [1, 2, 2, 2, 2], id='target_outline', edgecolor='#DC2626', linewidth=1.5, capstyle='butt', fill=False)
            c.path(self._samples_002, [1] + [2] * 15, id='target_outline', capstyle='butt', fill=False)
        for object_id, points in self._geometry_03:
            c.line(points, id=object_id, solid_capstyle='butt')
        c.path([[-0.5, 0.0], [0.5, 0.0], [1.5, 0.0], [2.5, 0.0], [3.5, 0.0], [3.5, 1.0], [2.5, 1.0], [1.5, 1.0], [0.5, 1.0], [-0.5, 1.0], [-0.5, 0.0]], [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 79], id='piece_A_outline', capstyle='butt', fill=False)
        for object_id, points in [('piece_A_grid_00', [[0.5, 0.0], [0.5, 1.0]]), ('piece_A_grid_01', [[1.5, 0.0], [1.5, 1.0]]), ('piece_A_grid_02', [[2.5, 0.0], [2.5, 1.0]])]:
            c.line(points, id=object_id, solid_capstyle='butt')
        c.path([[5.0, 0.0], [6.0, 0.0], [7.0, 0.0], [8.0, 0.0], [8.0, 1.0], [7.0, 1.0], [6.0, 1.0], [6.0, 2.0], [5.0, 2.0], [5.0, 1.0], [5.0, 0.0]], [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 79], id='piece_B_outline', capstyle='butt', fill=False, **_kw.get(6, {}))
        for object_id, points in [('piece_B_grid_00', [[5.0, 1.0], [6.0, 1.0]]), ('piece_B_grid_01', [[6.0, 0.0], [6.0, 1.0]]), ('piece_B_grid_02', [[7.0, 0.0], [7.0, 1.0]])]:
            c.line(points, id=object_id, solid_capstyle='butt')
        c.path([[10.0, 0.0], [11.0, 0.0], [12.0, 0.0], [13.0, 0.0], [13.0, 1.0], [12.0, 1.0], [12.0, 2.0], [11.0, 2.0], [11.0, 1.0], [10.0, 1.0], [10.0, 0.0]], [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 79], id='piece_C_outline', capstyle='butt', fill=False, **_kw.get(8, {}))
        for object_id, points in [('piece_C_grid_00', [[11.0, 0.0], [11.0, 1.0]]), ('piece_C_grid_01', [[11.0, 1.0], [12.0, 1.0]]), ('piece_C_grid_02', [[12.0, 0.0], [12.0, 1.0]])]:
            c.line(points, id=object_id, solid_capstyle='butt')
        c.path([[15.5, 0.0], [16.5, 0.0], [17.5, 0.0], [17.5, 1.0], [17.5, 2.0], [16.5, 2.0], [16.5, 3.0], [15.5, 3.0], [15.5, 2.0], [15.5, 1.0], [15.5, 0.0]], [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 79], id='piece_D_outline', capstyle='butt', fill=False)
        for object_id, points in [('piece_D_grid_00', [[15.5, 1.0], [16.5, 1.0]]), ('piece_D_grid_01', [[15.5, 2.0], [16.5, 2.0]]), ('piece_D_grid_02', [[16.5, 0.0], [16.5, 1.0]]), ('piece_D_grid_03', [[16.5, 1.0], [16.5, 2.0]]), ('piece_D_grid_04', [[16.5, 1.0], [17.5, 1.0]])]:
            c.line(points, id=object_id, solid_capstyle='butt')
        c.path([[19.5, 0.0], [20.5, 0.0], [21.5, 0.0], [22.5, 0.0], [23.5, 0.0], [23.5, 1.0], [22.5, 1.0], [21.5, 1.0], [21.5, 2.0], [20.5, 2.0], [20.5, 1.0], [19.5, 1.0], [19.5, 0.0]], [1] + [2] * 11 + [79], id='piece_E_outline', capstyle='butt', fill=False)
        for object_id, points in [('piece_E_grid_00', [[20.5, 0.0], [20.5, 1.0]]), ('piece_E_grid_01', [[20.5, 1.0], [21.5, 1.0]]), ('piece_E_grid_02', [[21.5, 0.0], [21.5, 1.0]]), ('piece_E_grid_03', [[22.5, 0.0], [22.5, 1.0]])]:
            c.line(points, id=object_id, solid_capstyle='butt')
        c.circle([13.0, 9.5], 0.075, id='target_dot', zorder=4, facecolor='black')
        for object_id, text, anchor in [('piece_A_label', '(A)', (1.5, -0.5)), ('piece_B_label', '(B)', (6.5, -0.5)), ('piece_C_label', '(C)', (11.5, -0.5)), ('piece_D_label', '(D)', (16.5, -0.5)), ('piece_E_label', '(E)', (21.5, -0.5))]:
            c.text(text, anchor, id=object_id, va='top')

    def draw(self, output_path=None, *, variant=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / (self.__class__.__name__ + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if variant not in self.variants:
                raise ValueError('Unknown Special variant: ' + str(variant))
            return getattr(self, 'draw_' + variant)(output_path)
        with Canvas(PLANE, xlim=(-1.099999999999996, 24.099999999999994), ylim=(-7.757212999131939, 17.44278700086805)) as c:

            def _slot_0(c):
                c.path(self._geometry_01, self._geometry_02, id='target_outline', capstyle='butt', fill=False)
            self._draw_base(c, custom={0: _slot_0})
            return c.save(output_path)

    def draw_C01(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane564_C01.png'
        with Canvas(PLANE, xlim=(-1.099999999999996, 24.099999999999994), ylim=(-7.757212999131939, 17.44278700086805)) as c:
            self._draw_base(c, kw={8: {'edgecolor': '#DC2626', 'linewidth': 1.5}})
            for object_id, points in [(None, [[11.0, 0.0], [11.0, 1.0]]), (None, [[12.0, 0.0], [12.0, 1.0]]), (None, [[11.0, 1.0], [12.0, 1.0]]), (None, [[11.5, 9.0], [14.5, 9.0]]), (None, [[11.5, 9.0], [11.5, 10.0]]), (None, [[11.5, 10.0], [12.5, 10.0]]), (None, [[12.5, 10.0], [12.5, 11.0]]), (None, [[13.5, 10.0], [13.5, 11.0]]), (None, [[13.5, 10.0], [14.5, 10.0]]), (None, [[12.5, 9.0], [12.5, 10.0]]), (None, [[13.5, 9.0], [13.5, 10.0]]), (None, [[12.5, 10.0], [13.5, 10.0]])]:
                c.line(points, id=object_id, zorder=9, color='#DC2626', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            return c.save(output_path)

    def draw_C02(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane564_C02.png'
        with Canvas(PLANE, xlim=(-1.099999999999996, 24.099999999999994), ylim=(-7.757212999131939, 17.44278700086805)) as c:

            def _slot_0(c):
                c.path(self._samples_001, [1] + [2] * 11, id='target_outline', capstyle='butt', fill=False)
                c.path([[14.5, 8.999999999999998], [14.5, 9.999999999999998], [14.5, 10.999999999999998], [13.5, 10.999999999999998], [12.5, 10.999999999999998]], [1, 2, 2, 2, 2], id='target_outline', edgecolor='#16A34A', linewidth=1.5, capstyle='butt', fill=False)
                c.path(self._samples_002, [1] + [2] * 15, id='target_outline', capstyle='butt', fill=False)
            self._draw_base(c, custom={0: _slot_0}, kw={8: {'edgecolor': '#16A34A', 'linewidth': 3.0}})
            for object_id, points in [(None, [[11.0, 0.0], [11.0, 1.0]]), (None, [[12.0, 0.0], [12.0, 1.0]]), (None, [[11.0, 1.0], [12.0, 1.0]]), (None, [[11.5, 9.0], [14.5, 9.0]]), (None, [[11.5, 9.0], [11.5, 10.0]]), (None, [[11.5, 10.0], [12.5, 10.0]]), (None, [[12.5, 10.0], [12.5, 11.0]]), (None, [[13.5, 10.0], [13.5, 11.0]]), (None, [[13.5, 10.0], [14.5, 10.0]]), (None, [[12.5, 9.0], [12.5, 10.0]]), (None, [[13.5, 9.0], [13.5, 10.0]]), (None, [[12.5, 10.0], [13.5, 10.0]])]:
                c.line(points, id=object_id, zorder=9, color='#16A34A', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            return c.save(output_path)

    def draw_C03(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane564_C03.png'
        with Canvas(PLANE, xlim=(-1.099999999999996, 24.099999999999994), ylim=(-7.757212999131939, 17.44278700086805)) as c:

            def _slot_0(c):
                c.path(self._samples_001, [1] + [2] * 11, id='target_outline', capstyle='butt', fill=False)
                c.path([[14.5, 8.999999999999998], [14.5, 9.999999999999998], [14.5, 10.999999999999998], [13.5, 10.999999999999998], [12.5, 10.999999999999998]], [1, 2, 2, 2, 2], id='target_outline', edgecolor='#2563EB', linewidth=1.5, capstyle='butt', fill=False)
                c.path(self._samples_002, [1] + [2] * 15, id='target_outline', capstyle='butt', fill=False)
            self._draw_base(c, custom={0: _slot_0}, kw={8: {'edgecolor': '#2563EB', 'linewidth': 1.5}})
            for object_id, points in [(None, [[11.0, 0.0], [11.0, 1.0]]), (None, [[12.0, 0.0], [12.0, 1.0]]), (None, [[11.0, 1.0], [12.0, 1.0]]), (None, [[11.5, 9.0], [14.5, 9.0]]), (None, [[11.5, 9.0], [11.5, 10.0]]), (None, [[11.5, 10.0], [12.5, 10.0]]), (None, [[12.5, 10.0], [12.5, 11.0]]), (None, [[13.5, 10.0], [13.5, 11.0]]), (None, [[13.5, 10.0], [14.5, 10.0]]), (None, [[12.5, 9.0], [12.5, 10.0]]), (None, [[13.5, 9.0], [13.5, 10.0]]), (None, [[12.5, 10.0], [13.5, 10.0]])]:
                c.line(points, id=object_id, zorder=9, color='#2563EB', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            return c.save(output_path)

    def draw_C04(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane564_C04.png'
        with Canvas(PLANE, xlim=(-1.099999999999996, 24.099999999999994), ylim=(-7.757212999131939, 17.44278700086805)) as c:

            def _slot_0(c):
                c.path(self._samples_001, [1] + [2] * 11, id='target_outline', capstyle='butt', fill=False)
                c.path([[14.5, 8.999999999999998], [14.5, 9.999999999999998], [14.5, 10.999999999999998], [13.5, 10.999999999999998]], [1, 2, 2, 2], id='target_outline', edgecolor='#16A34A', linewidth=1.5, capstyle='butt', fill=False)
                c.path(self._samples_003, [1] + [2] * 16, id='target_outline', capstyle='butt', fill=False)
            self._draw_base(c, custom={0: _slot_0}, kw={6: {'edgecolor': '#16A34A', 'linewidth': 1.5}})
            for object_id, points in [(None, [[5.0, 1.0], [6.0, 1.0]]), (None, [[6.0, 0.0], [6.0, 1.0]]), (None, [[7.0, 0.0], [7.0, 1.0]]), (None, [[11.5, 9.0], [14.5, 9.0]]), (None, [[11.5, 9.0], [11.5, 10.0]]), (None, [[11.5, 10.0], [13.5, 10.0]]), (None, [[13.5, 10.0], [13.5, 11.0]]), (None, [[12.5, 9.0], [12.5, 10.0]]), (None, [[13.5, 9.0], [13.5, 10.0]]), (None, [[13.5, 10.0], [14.5, 10.0]])]:
                c.line(points, id=object_id, zorder=9, color='#16A34A', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            return c.save(output_path)

    def draw_C05(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane564_C05.png'
        with Canvas(PLANE, xlim=(-1.099999999999996, 24.099999999999994), ylim=(-7.757212999131939, 17.44278700086805)) as c:

            def _slot_0(c):
                c.path(self._samples_001, [1] + [2] * 11, id='target_outline', capstyle='butt', fill=False)
                c.path([[14.5, 8.999999999999998], [14.5, 9.999999999999998], [14.5, 10.999999999999998], [13.5, 10.999999999999998]], [1, 2, 2, 2], id='target_outline', edgecolor='#DC2626', linewidth=1.5, capstyle='butt', fill=False)
                c.path(self._samples_003, [1] + [2] * 16, id='target_outline', capstyle='butt', fill=False)
            self._draw_base(c, custom={0: _slot_0}, kw={6: {'edgecolor': '#DC2626', 'linewidth': 1.5}})
            for object_id, points in [(None, [[5.0, 1.0], [6.0, 1.0]]), (None, [[6.0, 0.0], [6.0, 1.0]]), (None, [[7.0, 0.0], [7.0, 1.0]]), (None, [[11.5, 9.0], [14.5, 9.0]]), (None, [[11.5, 9.0], [11.5, 10.0]]), (None, [[11.5, 10.0], [13.5, 10.0]]), (None, [[13.5, 10.0], [13.5, 11.0]]), (None, [[12.5, 9.0], [12.5, 10.0]]), (None, [[13.5, 9.0], [13.5, 10.0]]), (None, [[13.5, 10.0], [14.5, 10.0]])]:
                c.line(points, id=object_id, zorder=9, color='#DC2626', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            return c.save(output_path)
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Plane564')
    parser.add_argument('output', nargs='?')
    parser.add_argument('--variant', choices=('C01', 'C02', 'C03', 'C04', 'C05'))
    args = parser.parse_args()
    print(Plane564().draw(args.output, variant=args.variant))
