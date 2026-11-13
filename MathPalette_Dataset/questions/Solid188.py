"""Collected question Solid188; construction on the shared drawing protocol."""
from pathlib import Path
import sys
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from MathPalette_Dataset.drawing import Canvas, SOLID

class Solid188:
    variants = ('C01', 'C02', 'C03', 'C04', 'C05')

    def _draw_base(self, c, hi=None):
        _hi = hi or {}
        for object_id, vertices, codes in [('givenfront_fill', [[15.0, 6.0], [18.0, 6.0], [18.0, 9.0], [15.0, 9.0], [15.0, 6.0]], [1, 2, 2, 2, 79]), ('giventop_fill', [[15.0, 9.0], [18.0, 9.0], [19.05, 10.05], [16.05, 10.05], [15.0, 9.0]], [1, 2, 2, 2, 79]), ('givenright_fill', [[18.0, 6.0], [19.05, 7.05], [19.05, 10.05], [18.0, 9.0], [18.0, 6.0]], [1, 2, 2, 2, 79])]:
            c.path(vertices, codes, id=object_id, alpha=1.0, zorder=1, edgecolor='none', facecolor='white', linewidth=0.0, capstyle='butt')
        _defs = [
            {}, {}, {}, {}, {}, {}, {}, {}, {}, {'color': '#2563EB'}, {},
            {'color': '#2563EB', 'linewidth': 2.0, 'solid_capstyle': 'butt'}
        ]
        _ov = {j: s for idxs, s in _hi.get(1, ()) for j in idxs}
        for i, (object_id, points) in enumerate([('givenedge0', [[15.0, 6.0], [15.0, 9.0]]), ('givenedge1', [[15.0, 6.0], [18.0, 6.0]]), ('givenedge2', [[15.0, 9.0], [16.05, 10.05]]), ('givenedge3', [[15.0, 9.0], [18.0, 9.0]]), ('givenedge4', [[16.05, 10.05], [19.05, 10.05]]), ('givenedge5', [[18.0, 6.0], [18.0, 9.0]]), ('givenedge6', [[18.0, 6.0], [19.05, 7.05]]), ('givenedge7', [[18.0, 9.0], [19.05, 10.05]]), ('givenedge8', [[19.05, 7.05], [19.05, 10.05]]), ('given_diagonal0', [[15.0, 9.0], [18.0, 6.0]]), ('given_diagonal1', [[15.0, 9.0], [19.05, 10.05]]), ('given_diagonal2', [[18.0, 6.0], [19.05, 10.05]])]):
            c.line(points, id=object_id, zorder=3, clip_on=False, **_ov.get(i, _defs[i]))
        for object_id, vertices, codes in [('A_cell0_0_fill', [[0.0, 0.0], [1.0, 0.0], [1.0, 1.0], [0.0, 1.0], [0.0, 0.0]], [1, 2, 2, 2, 79]), ('A_cell1_0_fill', [[1.0, 0.0], [2.0, 0.0], [2.0, 1.0], [1.0, 1.0], [1.0, 0.0]], [1, 2, 2, 2, 79]), ('A_cell2_0_fill', [[2.0, 0.0], [3.0, 0.0], [3.0, 1.0], [2.0, 1.0], [2.0, 0.0]], [1, 2, 2, 2, 79]), ('A_cell3_0_fill', [[3.0, 0.0], [4.0, 0.0], [4.0, 1.0], [3.0, 1.0], [3.0, 0.0]], [1, 2, 2, 2, 79]), ('A_cell1_1_fill', [[1.0, 1.0], [2.0, 1.0], [2.0, 2.0], [1.0, 2.0], [1.0, 1.0]], [1, 2, 2, 2, 79]), ('A_cell1_-1_fill', [[1.0, -1.0], [2.0, -1.0], [2.0, 0.0], [1.0, 0.0], [1.0, -1.0]], [1, 2, 2, 2, 79])]:
            c.path(vertices, codes, id=object_id, alpha=1.0, zorder=1, edgecolor='none', facecolor='white', linewidth=0.0, capstyle='butt')
        _defs = [
            {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {'color': '#2563EB'},
            {'color': '#2563EB'}, {'color': '#2563EB'}
        ]
        _ov = {j: s for idxs, s in _hi.get(3, ()) for j in idxs}
        for i, (object_id, points) in enumerate([('A_netedge0', [[0.0, 0.0], [0.0, 1.0]]), ('A_netedge1', [[0.0, 0.0], [1.0, 0.0]]), ('A_netedge2', [[0.0, 1.0], [1.0, 1.0]]), ('A_netedge3', [[1.0, -1.0], [1.0, 0.0]]), ('A_netedge4', [[1.0, -1.0], [2.0, -1.0]]), ('A_netedge5', [[1.0, 0.0], [1.0, 1.0]]), ('A_netedge6', [[1.0, 0.0], [2.0, 0.0]]), ('A_netedge7', [[1.0, 1.0], [1.0, 2.0]]), ('A_netedge8', [[1.0, 1.0], [2.0, 1.0]]), ('A_netedge9', [[1.0, 2.0], [2.0, 2.0]]), ('A_netedge10', [[2.0, -1.0], [2.0, 0.0]]), ('A_netedge11', [[2.0, 0.0], [2.0, 1.0]]), ('A_netedge12', [[2.0, 0.0], [3.0, 0.0]]), ('A_netedge13', [[2.0, 1.0], [2.0, 2.0]]), ('A_netedge14', [[2.0, 1.0], [3.0, 1.0]]), ('A_netedge15', [[3.0, 0.0], [3.0, 1.0]]), ('A_netedge16', [[3.0, 0.0], [4.0, 0.0]]), ('A_netedge17', [[3.0, 1.0], [4.0, 1.0]]), ('A_netedge18', [[4.0, 0.0], [4.0, 1.0]]), ('Adiagonal0', [[0.0, 1.0], [1.0, 0.0]]), ('Adiagonal1', [[3.0, 1.0], [4.0, 0.0]]), ('Adiagonal2', [[1.0, 0.0], [2.0, -1.0]])]):
            c.line(points, id=object_id, zorder=3, clip_on=False, **_ov.get(i, _defs[i]))
        for object_id, vertices, codes in [('B_cell0_0_fill', [[7.0, 0.0], [8.0, 0.0], [8.0, 1.0], [7.0, 1.0], [7.0, 0.0]], [1, 2, 2, 2, 79]), ('B_cell1_0_fill', [[8.0, 0.0], [9.0, 0.0], [9.0, 1.0], [8.0, 1.0], [8.0, 0.0]], [1, 2, 2, 2, 79]), ('B_cell2_0_fill', [[9.0, 0.0], [10.0, 0.0], [10.0, 1.0], [9.0, 1.0], [9.0, 0.0]], [1, 2, 2, 2, 79]), ('B_cell3_0_fill', [[10.0, 0.0], [11.0, 0.0], [11.0, 1.0], [10.0, 1.0], [10.0, 0.0]], [1, 2, 2, 2, 79]), ('B_cell1_1_fill', [[8.0, 1.0], [9.0, 1.0], [9.0, 2.0], [8.0, 2.0], [8.0, 1.0]], [1, 2, 2, 2, 79]), ('B_cell1_-1_fill', [[8.0, -1.0], [9.0, -1.0], [9.0, 0.0], [8.0, 0.0], [8.0, -1.0]], [1, 2, 2, 2, 79])]:
            c.path(vertices, codes, id=object_id, alpha=1.0, zorder=1, edgecolor='none', facecolor='white', linewidth=0.0, capstyle='butt')
        for object_id, points in [('B_netedge0', [[7.0, 0.0], [7.0, 1.0]]), ('B_netedge1', [[7.0, 0.0], [8.0, 0.0]]), ('B_netedge2', [[7.0, 1.0], [8.0, 1.0]]), ('B_netedge3', [[8.0, -1.0], [8.0, 0.0]]), ('B_netedge4', [[8.0, -1.0], [9.0, -1.0]]), ('B_netedge5', [[8.0, 0.0], [8.0, 1.0]]), ('B_netedge6', [[8.0, 0.0], [9.0, 0.0]]), ('B_netedge7', [[8.0, 1.0], [8.0, 2.0]]), ('B_netedge8', [[8.0, 1.0], [9.0, 1.0]]), ('B_netedge9', [[8.0, 2.0], [9.0, 2.0]]), ('B_netedge10', [[9.0, -1.0], [9.0, 0.0]]), ('B_netedge11', [[9.0, 0.0], [9.0, 1.0]]), ('B_netedge12', [[9.0, 0.0], [10.0, 0.0]]), ('B_netedge13', [[9.0, 1.0], [9.0, 2.0]]), ('B_netedge14', [[9.0, 1.0], [10.0, 1.0]]), ('B_netedge15', [[10.0, 0.0], [10.0, 1.0]]), ('B_netedge16', [[10.0, 0.0], [11.0, 0.0]]), ('B_netedge17', [[10.0, 1.0], [11.0, 1.0]]), ('B_netedge18', [[11.0, 0.0], [11.0, 1.0]]), ('Bdiagonal0', [[7.0, 0.0], [8.0, 1.0]]), ('Bdiagonal1', [[10.0, 1.0], [11.0, 0.0]]), ('Bdiagonal2', [[8.0, -1.0], [9.0, 0.0]])]:
            c.line(points, id=object_id, zorder=3, clip_on=False)
        for object_id, vertices, codes in [('C_cell0_0_fill', [[14.0, 0.0], [15.0, 0.0], [15.0, 1.0], [14.0, 1.0], [14.0, 0.0]], [1, 2, 2, 2, 79]), ('C_cell1_0_fill', [[15.0, 0.0], [16.0, 0.0], [16.0, 1.0], [15.0, 1.0], [15.0, 0.0]], [1, 2, 2, 2, 79]), ('C_cell2_0_fill', [[16.0, 0.0], [17.0, 0.0], [17.0, 1.0], [16.0, 1.0], [16.0, 0.0]], [1, 2, 2, 2, 79]), ('C_cell3_0_fill', [[17.0, 0.0], [18.0, 0.0], [18.0, 1.0], [17.0, 1.0], [17.0, 0.0]], [1, 2, 2, 2, 79]), ('C_cell1_1_fill', [[15.0, 1.0], [16.0, 1.0], [16.0, 2.0], [15.0, 2.0], [15.0, 1.0]], [1, 2, 2, 2, 79]), ('C_cell1_-1_fill', [[15.0, -1.0], [16.0, -1.0], [16.0, 0.0], [15.0, 0.0], [15.0, -1.0]], [1, 2, 2, 2, 79])]:
            c.path(vertices, codes, id=object_id, alpha=1.0, zorder=1, edgecolor='none', facecolor='white', linewidth=0.0, capstyle='butt')
        for object_id, points in [('C_netedge0', [[14.0, 0.0], [14.0, 1.0]]), ('C_netedge1', [[14.0, 0.0], [15.0, 0.0]]), ('C_netedge2', [[14.0, 1.0], [15.0, 1.0]]), ('C_netedge3', [[15.0, -1.0], [15.0, 0.0]]), ('C_netedge4', [[15.0, -1.0], [16.0, -1.0]]), ('C_netedge5', [[15.0, 0.0], [15.0, 1.0]]), ('C_netedge6', [[15.0, 0.0], [16.0, 0.0]]), ('C_netedge7', [[15.0, 1.0], [15.0, 2.0]]), ('C_netedge8', [[15.0, 1.0], [16.0, 1.0]]), ('C_netedge9', [[15.0, 2.0], [16.0, 2.0]]), ('C_netedge10', [[16.0, -1.0], [16.0, 0.0]]), ('C_netedge11', [[16.0, 0.0], [16.0, 1.0]]), ('C_netedge12', [[16.0, 0.0], [17.0, 0.0]]), ('C_netedge13', [[16.0, 1.0], [16.0, 2.0]]), ('C_netedge14', [[16.0, 1.0], [17.0, 1.0]]), ('C_netedge15', [[17.0, 0.0], [17.0, 1.0]]), ('C_netedge16', [[17.0, 0.0], [18.0, 0.0]]), ('C_netedge17', [[17.0, 1.0], [18.0, 1.0]]), ('C_netedge18', [[18.0, 0.0], [18.0, 1.0]]), ('Cdiagonal0', [[14.0, 0.0], [15.0, 1.0]]), ('Cdiagonal1', [[17.0, 0.0], [18.0, 1.0]]), ('Cdiagonal2', [[15.0, -1.0], [16.0, 0.0]])]:
            c.line(points, id=object_id, zorder=3, clip_on=False)
        for object_id, vertices, codes in [('D_cell0_0_fill', [[21.0, 0.0], [22.0, 0.0], [22.0, 1.0], [21.0, 1.0], [21.0, 0.0]], [1, 2, 2, 2, 79]), ('D_cell1_0_fill', [[22.0, 0.0], [23.0, 0.0], [23.0, 1.0], [22.0, 1.0], [22.0, 0.0]], [1, 2, 2, 2, 79]), ('D_cell2_0_fill', [[23.0, 0.0], [24.0, 0.0], [24.0, 1.0], [23.0, 1.0], [23.0, 0.0]], [1, 2, 2, 2, 79]), ('D_cell3_0_fill', [[24.0, 0.0], [25.0, 0.0], [25.0, 1.0], [24.0, 1.0], [24.0, 0.0]], [1, 2, 2, 2, 79]), ('D_cell1_1_fill', [[22.0, 1.0], [23.0, 1.0], [23.0, 2.0], [22.0, 2.0], [22.0, 1.0]], [1, 2, 2, 2, 79]), ('D_cell1_-1_fill', [[22.0, -1.0], [23.0, -1.0], [23.0, 0.0], [22.0, 0.0], [22.0, -1.0]], [1, 2, 2, 2, 79])]:
            c.path(vertices, codes, id=object_id, alpha=1.0, zorder=1, edgecolor='none', facecolor='white', linewidth=0.0, capstyle='butt')
        for object_id, points in [('D_netedge0', [[21.0, 0.0], [21.0, 1.0]]), ('D_netedge1', [[21.0, 0.0], [22.0, 0.0]]), ('D_netedge2', [[21.0, 1.0], [22.0, 1.0]]), ('D_netedge3', [[22.0, -1.0], [22.0, 0.0]]), ('D_netedge4', [[22.0, -1.0], [23.0, -1.0]]), ('D_netedge5', [[22.0, 0.0], [22.0, 1.0]]), ('D_netedge6', [[22.0, 0.0], [23.0, 0.0]]), ('D_netedge7', [[22.0, 1.0], [22.0, 2.0]]), ('D_netedge8', [[22.0, 1.0], [23.0, 1.0]]), ('D_netedge9', [[22.0, 2.0], [23.0, 2.0]]), ('D_netedge10', [[23.0, -1.0], [23.0, 0.0]]), ('D_netedge11', [[23.0, 0.0], [23.0, 1.0]]), ('D_netedge12', [[23.0, 0.0], [24.0, 0.0]]), ('D_netedge13', [[23.0, 1.0], [23.0, 2.0]]), ('D_netedge14', [[23.0, 1.0], [24.0, 1.0]]), ('D_netedge15', [[24.0, 0.0], [24.0, 1.0]]), ('D_netedge16', [[24.0, 0.0], [25.0, 0.0]]), ('D_netedge17', [[24.0, 1.0], [25.0, 1.0]]), ('D_netedge18', [[25.0, 0.0], [25.0, 1.0]]), ('Ddiagonal0', [[21.0, 1.0], [22.0, 0.0]]), ('Ddiagonal1', [[24.0, 0.0], [25.0, 1.0]]), ('Ddiagonal2', [[22.0, 0.0], [23.0, -1.0]])]:
            c.line(points, id=object_id, zorder=3, clip_on=False)
        for object_id, text, anchor in [('label0', 'A', (2.0, -2.0)), ('label1', 'B', (9.0, -2.0)), ('label2', 'C', (16.0, -2.0)), ('label3', 'D', (23.0, -2.0)), ('label4', 'E', (30.0, -2.0)), ('label5', 'none of those\nshown', (32.5, 0.5))]:
            c.text(text, anchor, id=object_id)

    def draw(self, output_path=None, *, variant=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / (self.__class__.__name__ + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if variant not in self.variants:
                raise ValueError('Unknown Special variant: ' + str(variant))
            return getattr(self, 'draw_' + variant)(output_path)
        with Canvas(SOLID, xlim=(-0.9362328796080384, 37.59962469240455), ylim=(-15.37506254347186, 23.160795028540722)) as c:
            self._draw_base(c, hi={1: [({9, 11}, {})], 3: [({19, 20, 21}, {})]})
            return c.save(output_path)

    def draw_C01(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Solid188_C01.png'
        with Canvas(SOLID, xlim=(-0.9362328796080384, 37.59962469240455), ylim=(-15.37506254347186, 23.160795028540722)) as c:
            self._draw_base(c, hi={1: [({11}, {})]})
            return c.save(output_path)

    def draw_C02(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Solid188_C02.png'
        with Canvas(SOLID, xlim=(-0.9362328796080384, 37.59962469240455), ylim=(-15.37506254347186, 23.160795028540722)) as c:
            self._draw_base(c)
            return c.save(output_path)

    def draw_C03(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Solid188_C03.png'
        with Canvas(SOLID, xlim=(-0.9362328796080384, 37.59962469240455), ylim=(-15.37506254347186, 23.160795028540722)) as c:
            self._draw_base(c, hi={1: [({3}, {'color': '#2563EB'})], 3: [({21}, {})]})
            return c.save(output_path)

    def draw_C04(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Solid188_C04.png'
        with Canvas(SOLID, xlim=(-0.9362328796080384, 37.59962469240455), ylim=(-15.37506254347186, 23.160795028540722)) as c:
            self._draw_base(c, hi={1: [({5}, {'color': '#2563EB'}), ({9}, {})]})
            return c.save(output_path)

    def draw_C05(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Solid188_C05.png'
        with Canvas(SOLID, xlim=(-0.9362328796080384, 37.59962469240455), ylim=(-15.37506254347186, 23.160795028540722)) as c:
            self._draw_base(c, hi={1: [({9, 10, 11}, {'color': '#DC2626'})], 3: [({19, 20, 21}, {'color': '#DC2626'})]})
            return c.save(output_path)
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Solid188')
    parser.add_argument('output', nargs='?')
    parser.add_argument('--variant', choices=('C01', 'C02', 'C03', 'C04', 'C05'))
    args = parser.parse_args()
    print(Solid188().draw(args.output, variant=args.variant))
