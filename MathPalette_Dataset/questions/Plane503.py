"""Collected question Plane503; construction on the shared drawing protocol."""
from pathlib import Path
import sys
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from MathPalette_Dataset.drawing import Canvas, PLANE

class Plane503:
    variants = ('C01', 'C02', 'C03', 'C04', 'C05')

    def __init__(self):
        self._geometry_01 = [
            ('piece2_0', [[2, 22], [2, 23]]), ('piece2_1', [[2, 22], [3, 22]]),
            ('piece2_2', [[2, 23], [2, 24]]), ('piece2_3', [[2, 24], [2, 25]]),
            ('piece2_4', [[2, 25], [2, 26]]), ('piece2_5', [[2, 26], [2, 27]]),
            ('piece2_6', [[2, 27], [3, 27]]), ('piece2_7', [[3, 22], [4, 22]]),
            ('piece2_8', [[3, 27], [4, 27]]), ('piece2_9', [[4, 22], [5, 22]]),
            ('piece2_10', [[4, 23], [4, 24]]), ('piece2_11', [[4, 23], [5, 23]]),
            ('piece2_12', [[4, 24], [5, 24]]), ('piece2_13', [[4, 25], [4, 26]]),
            ('piece2_14', [[4, 25], [5, 25]]), ('piece2_15', [[4, 26], [5, 26]]),
            ('piece2_16', [[4, 27], [5, 27]]), ('piece2_17', [[5, 22], [5, 23]]),
            ('piece2_18', [[5, 24], [5, 25]]), ('piece2_19', [[5, 26], [5, 27]]),
            ('piece3_0', [[2, 13], [2, 14]]), ('piece3_1', [[2, 13], [3, 13]]),
            ('piece3_2', [[2, 14], [3, 14]]), ('piece3_3', [[2, 15], [2, 16]]),
            ('piece3_4', [[2, 15], [3, 15]]), ('piece3_5', [[2, 16], [3, 16]]),
            ('piece3_6', [[3, 12], [3, 13]]), ('piece3_7', [[3, 12], [4, 12]]),
            ('piece3_8', [[3, 14], [3, 15]]), ('piece3_9', [[3, 16], [3, 17]]),
            ('piece3_10', [[3, 17], [4, 17]]), ('piece3_11', [[4, 12], [5, 12]]),
            ('piece3_12', [[4, 17], [5, 17]]), ('piece3_13', [[5, 12], [6, 12]]),
            ('piece3_14', [[5, 15], [5, 16]]), ('piece3_15', [[5, 15], [6, 15]]),
            ('piece3_16', [[5, 16], [5, 17]]), ('piece3_17', [[6, 12], [7, 12]]),
            ('piece3_18', [[6, 15], [7, 15]]), ('piece3_19', [[7, 12], [8, 12]]),
            ('piece3_20', [[7, 15], [8, 15]]), ('piece3_21', [[8, 12], [8, 13]]),
            ('piece3_22', [[8, 13], [8, 14]]), ('piece3_23', [[8, 14], [8, 15]]),
            ('piece4_0', [[21, 13], [21, 14]]), ('piece4_1', [[21, 13], [22, 13]]),
            ('piece4_2', [[21, 14], [22, 14]]), ('piece4_3', [[21, 15], [21, 16]]),
            ('piece4_4', [[21, 15], [22, 15]]), ('piece4_5', [[21, 16], [22, 16]]),
            ('piece4_6', [[22, 12], [22, 13]]), ('piece4_7', [[22, 12], [23, 12]]),
            ('piece4_8', [[22, 14], [22, 15]]), ('piece4_9', [[22, 16], [22, 17]]),
            ('piece4_10', [[22, 17], [23, 17]]), ('piece4_11', [[23, 12], [24, 12]]),
            ('piece4_12', [[23, 16], [23, 17]]), ('piece4_13', [[23, 16], [24, 16]]),
            ('piece4_14', [[24, 12], [25, 12]]), ('piece4_15', [[24, 15], [24, 16]]),
            ('piece4_16', [[24, 15], [25, 15]]), ('piece4_17', [[25, 12], [26, 12]]),
            ('piece4_18', [[25, 15], [25, 16]]), ('piece4_19', [[25, 16], [26, 16]]),
            ('piece4_20', [[26, 12], [27, 12]]), ('piece4_21', [[26, 15], [26, 16]]),
            ('piece4_22', [[26, 15], [27, 15]]), ('piece4_23', [[27, 12], [27, 13]]),
            ('piece4_24', [[27, 13], [27, 14]]), ('piece4_25', [[27, 14], [27, 15]]),
            ('target_0', [[12, 2], [12, 3]]), ('target_1', [[12, 2], [13, 2]]),
            ('target_2', [[12, 3], [12, 4]]), ('target_3', [[12, 4], [12, 5]]),
            ('target_4', [[12, 5], [12, 6]]), ('target_5', [[12, 6], [12, 7]]),
            ('target_6', [[12, 7], [13, 7]]), ('target_7', [[13, 2], [14, 2]]),
            ('target_8', [[13, 7], [14, 7]]), ('target_9', [[14, 2], [15, 2]]),
            ('target_10', [[14, 7], [15, 7]]), ('target_11', [[15, 2], [16, 2]]),
            ('target_12', [[15, 7], [16, 7]]), ('target_13', [[16, 2], [17, 2]]),
            ('target_14', [[16, 7], [17, 7]]), ('target_15', [[17, 2], [18, 2]]),
            ('target_16', [[17, 5], [17, 6]]), ('target_17', [[17, 5], [18, 5]]),
            ('target_18', [[17, 6], [17, 7]]), ('target_19', [[18, 2], [19, 2]]),
            ('target_20', [[18, 5], [19, 5]]), ('target_21', [[19, 2], [20, 2]]),
            ('target_22', [[19, 5], [20, 5]]), ('target_23', [[20, 2], [20, 3]]),
            ('target_24', [[20, 3], [20, 4]]), ('target_25', [[20, 4], [20, 5]]),
            ('piece1_0', [[21.0, 22.0], [24.0, 22.0]]), ('piece1_1', [[23.0, 23.0], [24.0, 23.0]]),
            ('piece1_2', [[23.0, 24.5], [24.0, 24.5]]), ('piece1_3', [[23.0, 25.5], [24.0, 25.5]]),
            ('piece1_4', [[23.0, 26.0], [24.0, 26.0]]), ('piece1_5', [[21.0, 27.0], [24.0, 27.0]]),
            ('piece1_6', [[21.0, 22.0], [21.0, 27.0]]), ('piece1_7', [[23.0, 23.0], [23.0, 24.5]]),
            ('piece1_8', [[23.0, 25.5], [23.0, 26.0]]), ('piece1_9', [[24.0, 22.0], [24.0, 23.0]]),
            ('piece1_10', [[24.0, 24.5], [24.0, 25.5]]), ('piece1_11', [[24.0, 26.0], [24.0, 27.0]])
        ]

    def _draw_base(self, c, hi=None):
        _hi = hi or {}
        _ov = {j: s for idxs, s in _hi.get(0, ()) for j in idxs}
        for i, (object_id, points) in enumerate(self._geometry_01):
            c.line(points, id=object_id, **_ov[i]) if i in _ov else c.line(points, id=object_id)
        for object_id, text, anchor in [(None, '1', (22.5, 21)), (None, '2', (3.5, 21)), (None, '3', (5.0, 11)), (None, '4', (24.0, 11))]:
            c.text(text, anchor, id=None, zorder=3, fontsize=18.0)
        c.text('Target hexagon', (16.0, 0.6), zorder=3)

    def draw(self, output_path=None, *, variant=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / (self.__class__.__name__ + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if variant not in self.variants:
                raise ValueError('Unknown Special variant: ' + str(variant))
            return getattr(self, 'draw_' + variant)(output_path)
        with Canvas(PLANE, xlim=(0.44673162148224144, 28.60187948962887), ylim=(-0.4715825212624303, 27.6835653468842)) as c:
            self._draw_base(c)
            return c.save(output_path)

    def draw_C01(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane503_C01.png'
        with Canvas(PLANE, xlim=(0.44673162148224144, 28.60187948962887), ylim=(-0.4715825212624303, 27.6835653468842)) as c:
            self._draw_base(c, hi={0: [({30, 32, 34, 35, 36, 38, 40, 82, 84, 86, 87, 88, 90, 92}, {'color': '#EA580C', 'linewidth': 1.5}), ({70, 72, 73, 74, 75, 102}, {'color': '#2563EB', 'linewidth': 1.5})]})
            return c.save(output_path)

    def draw_C02(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane503_C02.png'
        with Canvas(PLANE, xlim=(0.44673162148224144, 28.60187948962887), ylim=(-0.4715825212624303, 27.6835653468842)) as c:
            self._draw_base(c, hi={0: [({27, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95}, {'color': '#EA580C', 'linewidth': 1.5}), ({70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 96, 101, 102}, {'color': '#2563EB', 'linewidth': 1.5})]})
            return c.save(output_path)

    def draw_C03(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane503_C03.png'
        with Canvas(PLANE, xlim=(0.44673162148224144, 28.60187948962887), ylim=(-0.4715825212624303, 27.6835653468842)) as c:
            self._draw_base(c, hi={0: [({20, 21, 22, 97, 98, 103}, {'color': '#2563EB', 'linewidth': 1.5}), ({23, 24, 25, 99, 100, 104}, {'color': '#EA580C', 'linewidth': 1.5})]})
            return c.save(output_path)

    def draw_C04(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane503_C04.png'
        with Canvas(PLANE, xlim=(0.44673162148224144, 28.60187948962887), ylim=(-0.4715825212624303, 27.6835653468842)) as c:
            self._draw_base(c, hi={0: [({51, 55, 58, 61, 64, 81, 83, 85, 89, 91}, {'color': '#EA580C', 'linewidth': 1.5}), ({71, 77, 79, 96}, {'color': '#2563EB', 'linewidth': 1.5})]})
            return c.save(output_path)

    def draw_C05(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane503_C05.png'
        with Canvas(PLANE, xlim=(0.44673162148224144, 28.60187948962887), ylim=(-0.4715825212624303, 27.6835653468842)) as c:
            self._draw_base(c)
            c.point([[21.0, 27.0]], zorder=10, s=50, facecolors='#2563EB', edgecolors='#2563EB')
            c.point([[12.0, 7.0]], zorder=10, s=50, facecolors='#2563EB', edgecolors='#2563EB')
            c.point([[27.0, 12.0]], zorder=10, s=50, facecolors='#EA580C', edgecolors='#EA580C')
            c.point([[20.0, 2.0]], zorder=10, s=50, facecolors='#EA580C', edgecolors='#EA580C')
            return c.save(output_path)
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Plane503')
    parser.add_argument('output', nargs='?')
    parser.add_argument('--variant', choices=('C01', 'C02', 'C03', 'C04', 'C05'))
    args = parser.parse_args()
    print(Plane503().draw(args.output, variant=args.variant))
