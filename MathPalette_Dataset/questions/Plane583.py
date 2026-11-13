"""Collected question Plane583; construction on the shared drawing protocol."""
from pathlib import Path
import sys
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from MathPalette_Dataset.drawing import Canvas, PLANE

class Plane583:
    variants = ('C01', 'C02', 'C03', 'C04', 'C05', 'C06')

    def _draw_base(self, c, hi=None):
        _hi = hi or {}
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
        _ov = {j: s for idxs, s in _hi.get(9, ()) for j in idxs}
        for i, (object_id, points) in enumerate([('E_edge_00', [[30.0, -2.0], [29.0, -2.0]]), ('E_edge_01', [[29.0, -2.0], [29.0, -1.0]]), ('E_edge_02', [[29.0, -1.0], [29.0, 0.0]]), ('E_edge_03', [[29.0, 0.0], [29.0, 1.0]]), ('E_edge_04', [[29.0, 1.0], [28.0, 1.0]]), ('E_edge_05', [[28.0, 1.0], [28.0, 2.0]]), ('E_edge_06', [[28.0, 2.0], [27.0, 2.0]]), ('E_edge_07', [[27.0, 2.0], [27.0, 1.0]]), ('E_edge_08', [[27.0, 1.0], [26.0, 1.0]]), ('E_edge_09', [[26.0, 1.0], [26.0, 0.0]]), ('E_edge_10', [[26.0, 0.0], [27.0, 0.0]]), ('E_edge_11', [[27.0, 0.0], [28.0, 0.0]])]):
            c.line(points, id=object_id, **_ov[i]) if i in _ov else c.line(points, id=object_id)
        for object_id, text, anchor in [('choice_A', '(A)', (0, -3.3)), ('choice_B', '(B)', (7, -3.3)), ('choice_C', '(C)', (14, -3.3)), ('choice_D', '(D)', (21, -3.3)), ('choice_E', '(E)', (28, -3.3))]:
            c.text(text, anchor, id=object_id)

    def draw(self, output_path=None, *, variant=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / (self.__class__.__name__ + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if variant not in self.variants:
                raise ValueError('Unknown Special variant: ' + str(variant))
            return getattr(self, 'draw_' + variant)(output_path)
        with Canvas(PLANE, xlim=(-2.9943416393196287, 30.99434163931963), ylim=(-17.79943860320105, 16.189244675438207)) as c:
            self._draw_base(c)
            return c.save(output_path)

    def draw_C01(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane583_C01.png'
        with Canvas(PLANE, xlim=(-2.9943416393196287, 30.99434163931963), ylim=(-17.79943860320105, 16.189244675438207)) as c:
            self._draw_base(c, hi={9: [({0, 1, 2, 3, 4, 7, 8, 9, 10, 11}, {'color': '#EA580C'})]})
            return c.save(output_path)

    def draw_C02(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane583_C02.png'
        with Canvas(PLANE, xlim=(-2.9943416393196287, 30.99434163931963), ylim=(-17.79943860320105, 16.189244675438207)) as c:
            self._draw_base(c, hi={9: [({0, 1, 2, 3, 4, 7, 8, 9, 10, 11}, {'color': '#2563EB'})]})
            return c.save(output_path)

    def draw_C03(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane583_C03.png'
        with Canvas(PLANE, xlim=(-2.9943416393196287, 30.99434163931963), ylim=(-17.79943860320105, 16.189244675438207)) as c:
            self._draw_base(c, hi={9: [({0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}, {'color': '#EA580C', 'linewidth': 2.0})]})
            return c.save(output_path)

    def draw_C04(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane583_C04.png'
        with Canvas(PLANE, xlim=(-2.9943416393196287, 30.99434163931963), ylim=(-17.79943860320105, 16.189244675438207)) as c:
            self._draw_base(c, hi={9: [({0, 1, 2, 3, 4, 7, 8, 9, 10, 11}, {'color': '#16A34A', 'linewidth': 1.5})]})
            return c.save(output_path)

    def draw_C05(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane583_C05.png'
        with Canvas(PLANE, xlim=(-2.9943416393196287, 30.99434163931963), ylim=(-17.79943860320105, 16.189244675438207)) as c:
            self._draw_base(c, hi={9: [({0, 1, 2, 3, 4, 7, 8, 9, 10, 11}, {'color': '#DC2626', 'linewidth': 1.5})]})
            return c.save(output_path)

    def draw_C06(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane583_C06.png'
        with Canvas(PLANE, xlim=(-2.9943416393196287, 30.99434163931963), ylim=(-17.79943860320105, 16.189244675438207)) as c:
            self._draw_base(c, hi={9: [({0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}, {'color': '#2563EB', 'linewidth': 1.5})]})
            return c.save(output_path)
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Plane583')
    parser.add_argument('output', nargs='?')
    parser.add_argument('--variant', choices=('C01', 'C02', 'C03', 'C04', 'C05', 'C06'))
    args = parser.parse_args()
    print(Plane583().draw(args.output, variant=args.variant))
