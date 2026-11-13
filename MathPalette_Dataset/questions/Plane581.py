"""Collected question Plane581; construction on the shared drawing protocol."""
from pathlib import Path
import sys
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from MathPalette_Dataset.drawing import Canvas, PLANE

class Plane581:
    variants = ('C01', 'C02', 'C03', 'C04')

    def _draw_base(self, c, hi=None):
        _hi = hi or {}
        for object_id, points in [('A_dot_00', [[1.0, -0.5]]), ('A_dot_01', [[1.0, -1.5]]), ('A_dot_02', [[2.0, -1.5]]), ('A_dot_03', [[2.0, -0.5]]), ('A_dot_04', [[2.0, 0.5]]), ('A_dot_05', [[1.0, 0.5]]), ('A_dot_06', [[0.0, 0.5]]), ('A_dot_07', [[0.0, 1.5]]), ('A_dot_08', [[-1.0, 1.5]]), ('A_dot_09', [[-1.0, 0.5]]), ('A_dot_10', [[-2.0, 0.5]])]:
            c.point(points, id=object_id)
        for object_id, points in [('A_edge_00', [[1.0, -0.5], [1.0, -1.5]]), ('A_edge_01', [[1.0, -1.5], [2.0, -1.5]]), ('A_edge_02', [[2.0, -1.5], [2.0, -0.5]]), ('A_edge_03', [[2.0, -0.5], [2.0, 0.5]]), ('A_edge_04', [[2.0, 0.5], [1.0, 0.5]]), ('A_edge_05', [[1.0, 0.5], [0.0, 0.5]]), ('A_edge_06', [[0.0, 0.5], [0.0, 1.5]]), ('A_edge_07', [[0.0, 1.5], [-1.0, 1.5]]), ('A_edge_08', [[-1.0, 1.5], [-1.0, 0.5]]), ('A_edge_09', [[-1.0, 0.5], [-2.0, 0.5]])]:
            c.line(points, id=object_id)
        for object_id, points in [('B_dot_00', [[7.0, 0.0]]), ('B_dot_01', [[7.0, -1.0]]), ('B_dot_02', [[7.0, -2.0]]), ('B_dot_03', [[8.0, -2.0]]), ('B_dot_04', [[8.0, -1.0]]), ('B_dot_05', [[8.0, 0.0]]), ('B_dot_06', [[8.0, 1.0]]), ('B_dot_07', [[8.0, 2.0]]), ('B_dot_08', [[7.0, 2.0]]), ('B_dot_09', [[7.0, 1.0]]), ('B_dot_10', [[6.0, 1.0]]), ('B_dot_11', [[6.0, 0.0]])]:
            c.point(points, id=object_id)
        for object_id, points in [('B_edge_00', [[7.0, 0.0], [7.0, -1.0]]), ('B_edge_01', [[7.0, -1.0], [7.0, -2.0]]), ('B_edge_02', [[7.0, -2.0], [8.0, -2.0]]), ('B_edge_03', [[8.0, -2.0], [8.0, -1.0]]), ('B_edge_04', [[8.0, -1.0], [8.0, 0.0]]), ('B_edge_05', [[8.0, 0.0], [8.0, 1.0]]), ('B_edge_06', [[8.0, 1.0], [8.0, 2.0]]), ('B_edge_07', [[8.0, 2.0], [7.0, 2.0]]), ('B_edge_08', [[7.0, 2.0], [7.0, 1.0]]), ('B_edge_09', [[7.0, 1.0], [6.0, 1.0]]), ('B_edge_10', [[6.0, 1.0], [6.0, 0.0]])]:
            c.line(points, id=object_id)
        for object_id, points in [('C_dot_00', [[16.0, 0.5]]), ('C_dot_01', [[15.0, 0.5]]), ('C_dot_02', [[15.0, -0.5]]), ('C_dot_03', [[14.0, -0.5]]), ('C_dot_04', [[14.0, 0.5]]), ('C_dot_05', [[13.0, 0.5]]), ('C_dot_06', [[13.0, 1.5]]), ('C_dot_07', [[12.0, 1.5]]), ('C_dot_08', [[12.0, 0.5]]), ('C_dot_09', [[12.0, -0.5]]), ('C_dot_10', [[12.0, -1.5]])]:
            c.point(points, id=object_id)
        for object_id, points in [('C_edge_00', [[16.0, 0.5], [15.0, 0.5]]), ('C_edge_01', [[15.0, 0.5], [15.0, -0.5]]), ('C_edge_02', [[15.0, -0.5], [14.0, -0.5]]), ('C_edge_03', [[14.0, -0.5], [14.0, 0.5]]), ('C_edge_04', [[14.0, 0.5], [13.0, 0.5]]), ('C_edge_05', [[13.0, 0.5], [13.0, 1.5]]), ('C_edge_06', [[13.0, 1.5], [12.0, 1.5]]), ('C_edge_07', [[12.0, 1.5], [12.0, 0.5]]), ('C_edge_08', [[12.0, 0.5], [12.0, -0.5]]), ('C_edge_09', [[12.0, -0.5], [12.0, -1.5]])]:
            c.line(points, id=object_id)
        for object_id, points in [('D_dot_00', [[19.0, 1.0]]), ('D_dot_01', [[20.0, 1.0]]), ('D_dot_02', [[20.0, 0.0]]), ('D_dot_03', [[21.0, 0.0]]), ('D_dot_04', [[21.0, 1.0]]), ('D_dot_05', [[22.0, 1.0]]), ('D_dot_06', [[23.0, 1.0]]), ('D_dot_07', [[23.0, 0.0]]), ('D_dot_08', [[22.0, 0.0]]), ('D_dot_09', [[22.0, -1.0]])]:
            c.point(points, id=object_id)
        for object_id, points in [('D_edge_00', [[19.0, 1.0], [20.0, 1.0]]), ('D_edge_01', [[20.0, 1.0], [20.0, 0.0]]), ('D_edge_02', [[20.0, 0.0], [21.0, 0.0]]), ('D_edge_03', [[21.0, 0.0], [21.0, 1.0]]), ('D_edge_04', [[21.0, 1.0], [22.0, 1.0]]), ('D_edge_05', [[22.0, 1.0], [23.0, 1.0]]), ('D_edge_06', [[23.0, 1.0], [23.0, 0.0]]), ('D_edge_07', [[23.0, 0.0], [22.0, 0.0]]), ('D_edge_08', [[22.0, 0.0], [22.0, -1.0]])]:
            c.line(points, id=object_id)
        for object_id, points in [('E_dot_00', [[29.0, 2.0]]), ('E_dot_01', [[29.0, 1.0]]), ('E_dot_02', [[28.0, 1.0]]), ('E_dot_03', [[27.0, 1.0]]), ('E_dot_04', [[27.0, 0.0]]), ('E_dot_05', [[28.0, 0.0]]), ('E_dot_06', [[28.0, -1.0]]), ('E_dot_07', [[29.0, -1.0]]), ('E_dot_08', [[29.0, -2.0]]), ('E_dot_09', [[28.0, -2.0]]), ('E_dot_10', [[27.0, -2.0]])]:
            c.point(points, id=object_id)
        _defs = [
            {'color': '#2563EB'}, {'color': '#2563EB'}, {'color': '#2563EB'}, {'color': '#2563EB'},
            {'color': '#2563EB'}, {}, {}, {}, {}, {}
        ]
        _ov = {j: s for idxs, s in _hi.get(9, ()) for j in idxs}
        for i, (object_id, points) in enumerate([('E_edge_00', [[29.0, 2.0], [29.0, 1.0]]), ('E_edge_01', [[29.0, 1.0], [28.0, 1.0]]), ('E_edge_02', [[28.0, 1.0], [27.0, 1.0]]), ('E_edge_03', [[27.0, 1.0], [27.0, 0.0]]), ('E_edge_04', [[27.0, 0.0], [28.0, 0.0]]), ('E_edge_05', [[28.0, 0.0], [28.0, -1.0]]), ('E_edge_06', [[28.0, -1.0], [29.0, -1.0]]), ('E_edge_07', [[29.0, -1.0], [29.0, -2.0]]), ('E_edge_08', [[29.0, -2.0], [28.0, -2.0]]), ('E_edge_09', [[28.0, -2.0], [27.0, -2.0]])]):
            c.line(points, id=object_id, **_ov.get(i, _defs[i]))
        for object_id, text, anchor in [('choice_A', '(A)', (0, -3.3)), ('choice_B', '(B)', (7, -3.3)), ('choice_C', '(C)', (14, -3.3)), ('choice_D', '(D)', (21, -3.3)), ('choice_E', '(E)', (28, -3.3))]:
            c.text(text, anchor, id=object_id)

    def draw(self, output_path=None, *, variant=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / (self.__class__.__name__ + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if variant not in self.variants:
                raise ValueError('Unknown Special variant: ' + str(variant))
            return getattr(self, 'draw_' + variant)(output_path)
        with Canvas(PLANE, xlim=(-2.963268463090891, 29.96326846309089), ylim=(-17.26351864685102, 15.663018279330762)) as c:
            self._draw_base(c, hi={9: [({0, 1, 2, 3, 4}, {})]})
            return c.save(output_path)

    def draw_C01(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane581_C01.png'
        with Canvas(PLANE, xlim=(-2.963268463090891, 29.96326846309089), ylim=(-17.26351864685102, 15.663018279330762)) as c:
            self._draw_base(c, hi={9: [({0, 1, 2, 3, 4}, {'color': '#EA580C'}), ({6, 7, 8, 9}, {'color': '#2563EB'})]})
            return c.save(output_path)

    def draw_C02(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane581_C02.png'
        with Canvas(PLANE, xlim=(-2.963268463090891, 29.96326846309089), ylim=(-17.26351864685102, 15.663018279330762)) as c:
            self._draw_base(c, hi={9: [({5, 6, 7, 8, 9}, {'color': '#2563EB'})]})
            return c.save(output_path)

    def draw_C03(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane581_C03.png'
        with Canvas(PLANE, xlim=(-2.963268463090891, 29.96326846309089), ylim=(-17.26351864685102, 15.663018279330762)) as c:
            self._draw_base(c)
            return c.save(output_path)

    def draw_C04(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane581_C04.png'
        with Canvas(PLANE, xlim=(-2.963268463090891, 29.96326846309089), ylim=(-17.26351864685102, 15.663018279330762)) as c:
            self._draw_base(c, hi={9: [({0, 1, 2, 3, 4, 5}, {'color': '#DC2626'})]})
            return c.save(output_path)
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Plane581')
    parser.add_argument('output', nargs='?')
    parser.add_argument('--variant', choices=('C01', 'C02', 'C03', 'C04'))
    args = parser.parse_args()
    print(Plane581().draw(args.output, variant=args.variant))
