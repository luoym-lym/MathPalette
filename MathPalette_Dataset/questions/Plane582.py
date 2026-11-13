"""Collected question Plane582; construction on the shared drawing protocol."""
from pathlib import Path
import sys
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from MathPalette_Dataset.drawing import Canvas, PLANE

class Plane582:
    variants = ('C01', 'C02', 'C03', 'C04', 'C05', 'C06')

    def _draw_base(self, c, hi=None):
        _hi = hi or {}
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
        _ov = {j: s for idxs, s in _hi.get(5, ()) for j in idxs}
        for i, (object_id, points) in enumerate([('C_edge_00', [[13.5, 1.0], [12.5, 1.0]]), ('C_edge_01', [[12.5, 1.0], [12.5, 0.0]]), ('C_edge_02', [[12.5, 0.0], [12.5, -1.0]]), ('C_edge_03', [[12.5, -1.0], [13.5, -1.0]]), ('C_edge_04', [[13.5, -1.0], [13.5, 0.0]]), ('C_edge_05', [[13.5, 0.0], [14.5, 0.0]]), ('C_edge_06', [[14.5, 0.0], [15.5, 0.0]]), ('C_edge_07', [[15.5, 0.0], [15.5, 1.0]]), ('C_edge_08', [[15.5, 1.0], [14.5, 1.0]])]):
            c.line(points, id=object_id, **_ov[i]) if i in _ov else c.line(points, id=object_id)
        for object_id, points in [('D_dot_00', [[20.5, -1.0]]), ('D_dot_01', [[20.5, 0.0]]), ('D_dot_02', [[19.5, 0.0]]), ('D_dot_03', [[19.5, 1.0]]), ('D_dot_04', [[20.5, 1.0]]), ('D_dot_05', [[21.5, 1.0]]), ('D_dot_06', [[22.5, 1.0]]), ('D_dot_07', [[22.5, 0.0]]), ('D_dot_08', [[21.5, 0.0]]), ('D_dot_09', [[21.5, -1.0]])]:
            c.point(points, id=object_id)
        for object_id, points in [('D_edge_00', [[20.5, -1.0], [20.5, 0.0]]), ('D_edge_01', [[20.5, 0.0], [19.5, 0.0]]), ('D_edge_02', [[19.5, 0.0], [19.5, 1.0]]), ('D_edge_03', [[19.5, 1.0], [20.5, 1.0]]), ('D_edge_04', [[20.5, 1.0], [21.5, 1.0]]), ('D_edge_05', [[21.5, 1.0], [22.5, 1.0]]), ('D_edge_06', [[22.5, 1.0], [22.5, 0.0]]), ('D_edge_07', [[22.5, 0.0], [21.5, 0.0]]), ('D_edge_08', [[21.5, 0.0], [21.5, -1.0]])]:
            c.line(points, id=object_id)
        for object_id, points in [('E_dot_00', [[28.5, 1.5]]), ('E_dot_01', [[29.5, 1.5]]), ('E_dot_02', [[29.5, 0.5]]), ('E_dot_03', [[29.5, -0.5]]), ('E_dot_04', [[28.5, -0.5]]), ('E_dot_05', [[28.5, 0.5]]), ('E_dot_06', [[27.5, 0.5]]), ('E_dot_07', [[27.5, -0.5]]), ('E_dot_08', [[27.5, -1.5]]), ('E_dot_09', [[26.5, -1.5]]), ('E_dot_10', [[26.5, -0.5]])]:
            c.point(points, id=object_id)
        _ov = {j: s for idxs, s in _hi.get(9, ()) for j in idxs}
        for i, (object_id, points) in enumerate([('E_edge_00', [[28.5, 1.5], [29.5, 1.5]]), ('E_edge_01', [[29.5, 1.5], [29.5, 0.5]]), ('E_edge_02', [[29.5, 0.5], [29.5, -0.5]]), ('E_edge_03', [[29.5, -0.5], [28.5, -0.5]]), ('E_edge_04', [[28.5, -0.5], [28.5, 0.5]]), ('E_edge_05', [[28.5, 0.5], [27.5, 0.5]]), ('E_edge_06', [[27.5, 0.5], [27.5, -0.5]]), ('E_edge_07', [[27.5, -0.5], [27.5, -1.5]]), ('E_edge_08', [[27.5, -1.5], [26.5, -1.5]]), ('E_edge_09', [[26.5, -1.5], [26.5, -0.5]])]):
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
        with Canvas(PLANE, xlim=(-2.463268463090891, 30.46326846309089), ylim=(-17.26351864685102, 15.663018279330762)) as c:
            self._draw_base(c)
            return c.save(output_path)

    def draw_C01(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane582_C01.png'
        with Canvas(PLANE, xlim=(-2.463268463090891, 30.46326846309089), ylim=(-17.26351864685102, 15.663018279330762)) as c:
            self._draw_base(c, hi={9: [({0, 1, 2, 3, 4}, {'color': '#EA580C'}), ({6, 7, 8, 9}, {'color': '#2563EB'})]})
            return c.save(output_path)

    def draw_C02(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane582_C02.png'
        with Canvas(PLANE, xlim=(-2.463268463090891, 30.46326846309089), ylim=(-17.26351864685102, 15.663018279330762)) as c:
            self._draw_base(c, hi={5: [({0, 1, 2, 3, 4, 5, 6, 7, 8}, {'color': '#16A34A'})]})
            return c.save(output_path)

    def draw_C03(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane582_C03.png'
        with Canvas(PLANE, xlim=(-2.463268463090891, 30.46326846309089), ylim=(-17.26351864685102, 15.663018279330762)) as c:
            self._draw_base(c, hi={5: [({0, 1, 2, 3, 4, 5, 6, 7, 8}, {'color': '#DC2626'})]})
            return c.save(output_path)

    def draw_C04(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane582_C04.png'
        with Canvas(PLANE, xlim=(-2.463268463090891, 30.46326846309089), ylim=(-17.26351864685102, 15.663018279330762)) as c:
            self._draw_base(c, hi={9: [({0, 1, 2, 3, 4, 5, 6, 7, 8, 9}, {'color': '#2563EB'})]})
            return c.save(output_path)

    def draw_C05(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane582_C05.png'
        with Canvas(PLANE, xlim=(-2.463268463090891, 30.46326846309089), ylim=(-17.26351864685102, 15.663018279330762)) as c:
            self._draw_base(c, hi={5: [({0, 1, 2, 3, 4, 5, 6, 7, 8}, {'color': '#DC2626', 'linewidth': 1.5})]})
            return c.save(output_path)

    def draw_C06(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane582_C06.png'
        with Canvas(PLANE, xlim=(-2.463268463090891, 30.46326846309089), ylim=(-17.26351864685102, 15.663018279330762)) as c:
            self._draw_base(c, hi={5: [({0, 1, 2, 3, 4, 5, 6, 7, 8}, {'color': '#2563EB', 'linewidth': 1.5})]})
            return c.save(output_path)
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Plane582')
    parser.add_argument('output', nargs='?')
    parser.add_argument('--variant', choices=('C01', 'C02', 'C03', 'C04', 'C05', 'C06'))
    args = parser.parse_args()
    print(Plane582().draw(args.output, variant=args.variant))
