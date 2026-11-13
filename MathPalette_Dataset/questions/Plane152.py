"""Collected question Plane152; construction on the shared drawing protocol."""
from pathlib import Path
import sys
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from MathPalette_Dataset.drawing import Canvas, PLANE

class Plane152:
    variants = ('C01', 'C02')

    def __init__(self):
        self._geometry_01 = [
            ('gridv0', [[0.0, -0.5], [0.0, 3.5]]), ('gridv1', [[1.0, -0.5], [1.0, 3.5]]),
            ('gridv2', [[2.0, -0.5], [2.0, 3.5]]), ('gridv3', [[3.0, -0.5], [3.0, 3.5]]),
            ('gridv4', [[4.0, -0.5], [4.0, 3.5]]), ('gridv5', [[5.0, -0.5], [5.0, 3.5]]),
            ('gridv6', [[6.0, -0.5], [6.0, 3.5]]), ('gridv7', [[7.0, -0.5], [7.0, 3.5]]),
            ('gridv8', [[8.0, -0.5], [8.0, 3.5]]), ('gridv9', [[9.0, -0.5], [9.0, 3.5]]),
            ('gridv10', [[10.0, -0.5], [10.0, 3.5]]), ('gridv11', [[11.0, -0.5], [11.0, 3.5]]),
            ('gridv12', [[12.0, -0.5], [12.0, 3.5]]), ('gridv13', [[13.0, -0.5], [13.0, 3.5]]),
            ('gridv14', [[14.0, -0.5], [14.0, 3.5]]), ('gridv15', [[15.0, -0.5], [15.0, 3.5]]),
            ('gridv16', [[16.0, -0.5], [16.0, 3.5]]), ('gridv17', [[17.0, -0.5], [17.0, 3.5]]),
            ('gridv18', [[18.0, -0.5], [18.0, 3.5]]), ('gridv19', [[19.0, -0.5], [19.0, 3.5]]),
            ('gridv20', [[20.0, -0.5], [20.0, 3.5]]), ('gridv21', [[21.0, -0.5], [21.0, 3.5]]),
            ('gridv22', [[22.0, -0.5], [22.0, 3.5]]), ('gridv23', [[23.0, -0.5], [23.0, 3.5]]),
            ('gridv24', [[24.0, -0.5], [24.0, 3.5]]), ('gridv25', [[25.0, -0.5], [25.0, 3.5]]),
            ('gridv26', [[26.0, -0.5], [26.0, 3.5]]), ('gridv27', [[27.0, -0.5], [27.0, 3.5]]),
            ('gridh0', [[-0.5, 0.0], [27.5, 0.0]]), ('gridh1', [[-0.5, 1.0], [27.5, 1.0]]),
            ('gridh2', [[-0.5, 2.0], [27.5, 2.0]]), ('gridh3', [[-0.5, 3.0], [27.5, 3.0]])
        ]
        self._geometry_02 = [
            ('pattern0', [[0.0, 0.0], [0.0, 3.0]]), ('pattern1', [[0.0, 3.0], [3.0, 3.0]]),
            ('pattern2', [[3.0, 3.0], [3.0, 0.0]]), ('pattern3', [[3.0, 0.0], [4.0, 0.0]]),
            ('pattern4', [[4.0, 0.0], [4.0, 2.0]]), ('pattern5', [[4.0, 2.0], [6.0, 2.0]]),
            ('pattern6', [[6.0, 2.0], [6.0, 0.0]]), ('pattern7', [[6.0, 0.0], [7.0, 0.0]]),
            ('pattern8', [[7.0, 0.0], [7.0, 1.0]]), ('pattern9', [[7.0, 1.0], [8.0, 1.0]]),
            ('pattern10', [[8.0, 1.0], [8.0, 0.0]]), ('pattern11', [[8.0, 0.0], [9.0, 0.0]]),
            ('pattern12', [[9.0, 0.0], [9.0, 3.0]]), ('pattern13', [[9.0, 3.0], [12.0, 3.0]]),
            ('pattern14', [[12.0, 3.0], [12.0, 0.0]]), ('pattern15', [[12.0, 0.0], [13.0, 0.0]]),
            ('pattern16', [[13.0, 0.0], [13.0, 2.0]]), ('pattern17', [[13.0, 2.0], [15.0, 2.0]]),
            ('pattern18', [[15.0, 2.0], [15.0, 0.0]]), ('pattern19', [[15.0, 0.0], [16.0, 0.0]]),
            ('pattern20', [[16.0, 0.0], [16.0, 1.0]]), ('pattern21', [[16.0, 1.0], [17.0, 1.0]]),
            ('pattern22', [[17.0, 1.0], [17.0, 0.0]]), ('pattern23', [[17.0, 0.0], [18.0, 0.0]])
        ]
        self._geometry_03 = [
            ('dot0', [[0.0, 0.0]]), ('dot1', [[0.0, 3.0]]), ('dot2', [[3.0, 3.0]]), ('dot3', [[3.0, 0.0]]),
            ('dot4', [[4.0, 0.0]]), ('dot5', [[4.0, 2.0]]), ('dot6', [[6.0, 2.0]]), ('dot7', [[6.0, 0.0]]),
            ('dot8', [[7.0, 0.0]]), ('dot9', [[7.0, 1.0]]), ('dot10', [[8.0, 1.0]]), ('dot11', [[8.0, 0.0]]),
            ('dot12', [[9.0, 0.0]]), ('dot13', [[9.0, 3.0]]), ('dot14', [[12.0, 3.0]]),
            ('dot15', [[12.0, 0.0]]), ('dot16', [[13.0, 0.0]]), ('dot17', [[13.0, 2.0]]),
            ('dot18', [[15.0, 2.0]]), ('dot19', [[15.0, 0.0]]), ('dot20', [[16.0, 0.0]]),
            ('dot21', [[16.0, 1.0]]), ('dot22', [[17.0, 1.0]]), ('dot23', [[17.0, 0.0]]),
            ('dot24', [[18.0, 0.0]]), ('A_dot', [[20.0, 2.0]]), ('B_dot', [[22.0, 3.0]]),
            ('C_dot', [[23.0, 1.0]]), ('D_dot', [[24.0, 2.0]]), ('E_dot', [[26.0, 2.0]])
        ]

    def _draw_base(self, c, hi=None):
        _hi = hi or {}
        for object_id, points in self._geometry_01:
            c.line(points, id=object_id, color='#B0B0B0')
        _ov = {j: s for idxs, s in _hi.get(1, ()) for j in idxs}
        for i, (object_id, points) in enumerate(self._geometry_02):
            c.line(points, id=object_id, **_ov[i]) if i in _ov else c.line(points, id=object_id)
        for object_id, points in self._geometry_03:
            c.point(points, id=object_id)
        for object_id, text, anchor in [('A_label', 'A', (20.0, 2.0)), ('B_label', 'B', (22.0, 3.0)), ('C_label', 'C', (23.0, 1.0)), ('D_label', 'D', (24.0, 2.0)), ('E_label', 'E', (26.0, 2.0))]:
            c.text(text, anchor, id=object_id, fontsize=18.0, fontstyle='italic', offset_pt=(0, -17))

    def draw(self, output_path=None, *, variant=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / (self.__class__.__name__ + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if variant not in self.variants:
                raise ValueError('Unknown Special variant: ' + str(variant))
            return getattr(self, 'draw_' + variant)(output_path)
        with Canvas(PLANE, xlim=(-1.1830077986274325, 28.253225663548907), ylim=(-13.25275685548334, 16.183476606693)) as c:
            self._draw_base(c)
            return c.save(output_path)

    def draw_C01(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane152_C01.png'
        with Canvas(PLANE, xlim=(-1.1830077986274325, 28.253225663548907), ylim=(-13.25275685548334, 16.183476606693)) as c:
            self._draw_base(c)
            c.point([[23.0, 1.0]], zorder=10, s=50, facecolors='#DC2626', edgecolors='#DC2626')
            return c.save(output_path)

    def draw_C02(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane152_C02.png'
        with Canvas(PLANE, xlim=(-1.1830077986274325, 28.253225663548907), ylim=(-13.25275685548334, 16.183476606693)) as c:
            self._draw_base(c, hi={1: [({12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23}, {'color': '#2563EB', 'linewidth': 1.5})]})
            c.point([[20.0, 2.0]], zorder=10, s=50, facecolors='#DC2626', edgecolors='#DC2626')
            return c.save(output_path)
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Plane152')
    parser.add_argument('output', nargs='?')
    parser.add_argument('--variant', choices=('C01', 'C02'))
    args = parser.parse_args()
    print(Plane152().draw(args.output, variant=args.variant))
