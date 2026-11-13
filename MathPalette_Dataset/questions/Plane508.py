"""Collected question Plane508; construction on the shared drawing protocol."""
from pathlib import Path
import sys
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from MathPalette_Dataset.drawing import Canvas, PLANE

class Plane508:
    variants = ('C01', 'C02')

    def _draw_base(self, c, kw=None):
        _kw = kw or {}
        for object_id, points in [('source_dot4', [[2.873, 6.9705]]), ('source_dot1', [[3.793, 7.603]]), ('source_dot6', [[4.897, 7.258]]), ('source_dot3', [[5.173, 6.1195]]), ('source_dot2', [[4.2645, 5.28]]), ('source_dot5', [[3.057, 5.5905]])]:
            c.point(points, id=object_id, zorder=3, linewidths=0)
        c.line([[0.5366, 4.1101], [1.2006, 4.5666], [0.6694, 3.1141], [0.5366, 4.1101]], id='option0_0', solid_capstyle='projecting')
        c.line([[1.9974, 4.3176], [2.1966, 3.4959], [1.5409, 2.89], [1.9974, 4.3176]], id='option0_1', solid_capstyle='projecting')
        for object_id, points in [('option0_dot0', [[0.5366, 4.1101]]), ('option0_dot1', [[1.2006, 4.5666]]), ('option0_dot2', [[1.9974, 4.3176]]), ('option0_dot3', [[2.1966, 3.4959]]), ('option0_dot4', [[1.5409, 2.89]]), ('option0_dot5', [[0.6694, 3.1141]])]:
            c.point(points, id=object_id, zorder=3, s=12, linewidths=0)
        c.line([[3.1866, 4.1101], [3.8506, 4.5666], [4.6474, 4.3176], [3.1866, 4.1101]], id='option1_0', solid_capstyle='projecting')
        c.line([[4.8466, 3.4959], [4.1909, 2.89], [3.3194, 3.1141], [4.8466, 3.4959]], id='option1_1', solid_capstyle='projecting')
        for object_id, points in [('option1_dot0', [[3.1866, 4.1101]]), ('option1_dot1', [[3.8506, 4.5666]]), ('option1_dot2', [[4.6474, 4.3176]]), ('option1_dot3', [[4.8466, 3.4959]]), ('option1_dot4', [[4.1909, 2.89]]), ('option1_dot5', [[3.3194, 3.1141]])]:
            c.point(points, id=object_id, zorder=3, s=12, linewidths=0)
        c.line([[5.8366, 4.1101], [7.2974, 4.3176], [7.4966, 3.4959], [5.8366, 4.1101]], id='option2_0', solid_capstyle='projecting', **_kw.get(7, {}))
        c.line([[6.5006, 4.5666], [6.8409, 2.89], [5.9694, 3.1141], [6.5006, 4.5666]], id='option2_1', solid_capstyle='projecting', **_kw.get(8, {}))
        for object_id, points in [('option2_dot0', [[5.8366, 4.1101]]), ('option2_dot1', [[6.5006, 4.5666]]), ('option2_dot2', [[7.2974, 4.3176]]), ('option2_dot3', [[7.4966, 3.4959]]), ('option2_dot4', [[6.8409, 2.89]]), ('option2_dot5', [[5.9694, 3.1141]])]:
            c.point(points, id=object_id, zorder=3, s=12, linewidths=0)
        c.line([[1.8366, 1.8301], [3.2974, 2.0376], [1.9694, 0.8341], [1.8366, 1.8301]], id='option3_0', solid_capstyle='projecting', **_kw.get(10, {}))
        c.line([[2.5006, 2.2866], [3.4966, 1.2159], [2.8409, 0.61], [2.5006, 2.2866]], id='option3_1', solid_capstyle='projecting', **_kw.get(11, {}))
        for object_id, points in [('option3_dot0', [[1.8366, 1.8301]]), ('option3_dot1', [[2.5006, 2.2866]]), ('option3_dot2', [[3.2974, 2.0376]]), ('option3_dot3', [[3.4966, 1.2159]]), ('option3_dot4', [[2.8409, 0.61]]), ('option3_dot5', [[1.9694, 0.8341]])]:
            c.point(points, id=object_id, zorder=3, s=12, linewidths=0)
        c.line([[4.5366, 1.8301], [5.9974, 2.0376], [5.5409, 0.61], [4.5366, 1.8301]], id='option4_0', solid_capstyle='projecting')
        c.line([[5.2006, 2.2866], [6.1966, 1.2159], [4.6694, 0.8341], [5.2006, 2.2866]], id='option4_1', solid_capstyle='projecting')
        for object_id, points in [('option4_dot0', [[4.5366, 1.8301]]), ('option4_dot1', [[5.2006, 2.2866]]), ('option4_dot2', [[5.9974, 2.0376]]), ('option4_dot3', [[6.1966, 1.2159]]), ('option4_dot4', [[5.5409, 0.61]]), ('option4_dot5', [[4.6694, 0.8341]])]:
            c.point(points, id=object_id, zorder=3, s=12, linewidths=0)
        for object_id, text, anchor in [(None, '4', (2.59348, 7.10455)), (None, '1', (3.73913, 7.90828)), (None, '6', (5.12479, 7.46827)), (None, '3', (5.47268, 6.04017)), (None, '2', (4.33399, 4.97789)), (None, '5', (2.82546, 5.38437)), (None, '(A)', (1.35, 2.6)), (None, '(B)', (4, 2.6)), (None, '(C)', (6.65, 2.6)), (None, '(D)', (2.65, 0.31999999999999984)), (None, '(E)', (5.35, 0.31999999999999984))]:
            c.text(text, anchor, id=None, zorder=3)

    def draw(self, output_path=None, *, variant=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / (self.__class__.__name__ + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if variant not in self.variants:
                raise ValueError('Unknown Special variant: ' + str(variant))
            return getattr(self, 'draw_' + variant)(output_path)
        with Canvas(PLANE, xlim=(0.0, 8.0), ylim=(0.0, 8.0)) as c:
            self._draw_base(c)
            return c.save(output_path)

    def draw_C01(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane508_C01.png'
        with Canvas(PLANE, xlim=(0.0, 8.0), ylim=(0.0, 8.0)) as c:
            self._draw_base(c, kw={10: {'color': '#DC2626', 'linewidth': 1.5}, 11: {'color': '#2563EB', 'linewidth': 1.5}})
            for object_id, points in [(None, [[2.873, 6.9705], [4.897, 7.258]]), (None, [[2.873, 6.9705], [3.057, 5.5905]]), (None, [[4.897, 7.258], [3.057, 5.5905]])]:
                c.line(points, id=object_id, zorder=9, color='#DC2626', solid_capstyle='butt')
            for object_id, points in [(None, [[3.793, 7.603], [5.173, 6.1195]]), (None, [[3.793, 7.603], [4.2645, 5.28]]), (None, [[5.173, 6.1195], [4.2645, 5.28]])]:
                c.line(points, id=object_id, zorder=9, color='#2563EB', solid_capstyle='butt')
            return c.save(output_path)

    def draw_C02(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane508_C02.png'
        with Canvas(PLANE, xlim=(0.0, 8.0), ylim=(0.0, 8.0)) as c:
            self._draw_base(c, kw={7: {'color': '#2563EB', 'linewidth': 1.5}, 8: {'color': '#DC2626', 'linewidth': 1.5}})
            for object_id, points in [(None, [[2.873, 6.9705], [4.897, 7.258]]), (None, [[4.897, 7.258], [5.173, 6.1195]]), (None, [[5.173, 6.1195], [2.873, 6.9705]])]:
                c.line(points, id=object_id, zorder=9, color='#2563EB', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            for object_id, points in [(None, [[3.793, 7.603], [4.2645, 5.28]]), (None, [[4.2645, 5.28], [3.057, 5.5905]]), (None, [[3.057, 5.5905], [3.793, 7.603]])]:
                c.line(points, id=object_id, zorder=9, color='#DC2626', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            return c.save(output_path)
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Plane508')
    parser.add_argument('output', nargs='?')
    parser.add_argument('--variant', choices=('C01', 'C02'))
    args = parser.parse_args()
    print(Plane508().draw(args.output, variant=args.variant))
