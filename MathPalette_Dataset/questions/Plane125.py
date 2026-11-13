"""Collected question Plane125; construction on the shared drawing protocol."""
from pathlib import Path
import sys
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from MathPalette_Dataset.drawing import Canvas, PLANE

class Plane125:
    variants = ('C01', 'C02', 'C03', 'C04', 'C05', 'C06')

    def draw(self, output_path=None, *, variant=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / (self.__class__.__name__ + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if variant not in self.variants:
                raise ValueError('Unknown Special variant: ' + str(variant))
            return getattr(self, 'draw_' + variant)(output_path)
        with Canvas(PLANE, xlim=(-0.13953488372093048, 6.1395348837209305), ylim=(-1.1395348837209305, 5.1395348837209305)) as c:
            c.path([[0.0, 2.0], [2.0, 0.0], [3.0, 1.0], [4.0, 0.0], [6.0, 2.0], [4.0, 4.0], [3.0, 3.0], [2.0, 4.0], [0.0, 2.0]], [1, 2, 2, 2, 2, 2, 2, 2, 79], alpha=0.45, zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), capstyle='butt')
            c.path([[0.0, 2.0], [2.0, 0.0], [3.0, 1.0], [4.0, 0.0], [6.0, 2.0], [4.0, 4.0], [3.0, 3.0], [2.0, 4.0], [0.0, 2.0]], [1, 2, 2, 2, 2, 2, 2, 2, 79], id='shade', capstyle='butt', fill=False)
            for object_id, points in [('grid_v0', [[0.0, 0.0], [0.0, 4.0]]), ('grid_v1', [[1.0, 0.0], [1.0, 4.0]]), ('grid_v2', [[2.0, 0.0], [2.0, 4.0]]), ('grid_v3', [[3.0, 0.0], [3.0, 4.0]]), ('grid_v4', [[4.0, 0.0], [4.0, 4.0]]), ('grid_v5', [[5.0, 0.0], [5.0, 4.0]]), ('grid_v6', [[6.0, 0.0], [6.0, 4.0]]), ('grid_h0', [[0.0, 0.0], [6.0, 0.0]]), ('grid_h1', [[0.0, 1.0], [6.0, 1.0]]), ('grid_h2', [[0.0, 2.0], [6.0, 2.0]]), ('grid_h3', [[0.0, 3.0], [6.0, 3.0]]), ('grid_h4', [[0.0, 4.0], [6.0, 4.0]])]:
                c.line(points, id=object_id)
            return c.save(output_path)

    def _draw_choices(self, c, kw=None, custom=None):
        _kw = kw or {}
        c.path([[0.0, 2.0], [2.0, 0.0], [3.0, 1.0], [4.0, 0.0], [6.0, 2.0], [4.0, 4.0], [3.0, 3.0], [2.0, 4.0], [0.0, 2.0]], [1, 2, 2, 2, 2, 2, 2, 2, 79], alpha=0.45, zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), capstyle='butt')
        c.path([[0.0, 2.0], [2.0, 0.0]], [1, 2], id='shade', capstyle='butt', fill=False, **_kw.get(1, {}))
        c.path([[2.0, 0.0], [3.0, 1.0], [4.0, 0.0]], [1, 2, 2], id='shade', capstyle='butt', fill=False, **_kw.get(2, {}))
        c.path([[4.0, 0.0], [6.0, 2.0], [4.0, 4.0]], [1, 2, 2], id='shade', capstyle='butt', fill=False, **_kw.get(3, {}))
        c.path([[4.0, 4.0], [3.0, 3.0], [2.0, 4.0]], [1, 2, 2], id='shade', capstyle='butt', fill=False, **_kw.get(4, {}))
        c.path([[2.0, 4.0], [0.0, 2.0]], [1, 2], id='shade', capstyle='butt', fill=False, **_kw.get(5, {}))
        if custom and 6 in custom:
            custom[6](c)
        else:
            for object_id, points in [('grid_v0', [[0.0, 0.0], [0.0, 4.0]]), ('grid_v1', [[1.0, 0.0], [1.0, 4.0]]), ('grid_v2', [[2.0, 0.0], [2.0, 4.0]]), ('grid_v3', [[3.0, 0.0], [3.0, 4.0]]), ('grid_v4', [[4.0, 0.0], [4.0, 4.0]]), ('grid_v5', [[5.0, 0.0], [5.0, 4.0]]), ('grid_v6', [[6.0, 0.0], [6.0, 4.0]])]:
                c.line(points, id=object_id)
        c.path([[0.0, 0.0], [2.0, 0.0]], [1, 2], id='grid_h0', joinstyle='round', fill=False, **_kw.get(7, {}))
        c.path([[2.0, 0.0], [4.0, 0.0]], [1, 2], id='grid_h0', joinstyle='round', fill=False, **_kw.get(8, {}))
        c.path([[4.0, 0.0], [6.0, 0.0]], [1, 2], id='grid_h0', joinstyle='round', fill=False, **_kw.get(9, {}))
        for object_id, points in [('grid_h1', [[0.0, 1.0], [6.0, 1.0]]), ('grid_h2', [[0.0, 2.0], [6.0, 2.0]]), ('grid_h3', [[0.0, 3.0], [6.0, 3.0]])]:
            c.line(points, id=object_id)
        c.path([[0.0, 4.0], [2.0, 4.0]], [1, 2], id='grid_h4', joinstyle='round', fill=False, **_kw.get(11, {}))
        c.path([[2.0, 4.0], [4.0, 4.0]], [1, 2], id='grid_h4', joinstyle='round', fill=False, **_kw.get(12, {}))
        c.path([[4.0, 4.0], [6.0, 4.0]], [1, 2], id='grid_h4', joinstyle='round', fill=False, **_kw.get(13, {}))

    def draw_C01(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane125_C01.png'
        with Canvas(PLANE, xlim=(-0.13953488372093048, 6.1395348837209305), ylim=(-1.1395348837209305, 5.1395348837209305)) as c:
            self._draw_choices(c, kw={1: {'edgecolor': '#DC2626', 'linewidth': 1.5}, 3: {'edgecolor': '#DC2626', 'linewidth': 1.5}, 5: {'edgecolor': '#DC2626', 'linewidth': 1.5}, 8: {'edgecolor': '#DC2626', 'linewidth': 1.5}, 12: {'edgecolor': '#DC2626', 'linewidth': 2.0}})
            return c.save(output_path)

    def draw_C02(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane125_C02.png'
        with Canvas(PLANE, xlim=(-0.13953488372093048, 6.1395348837209305), ylim=(-1.1395348837209305, 5.1395348837209305)) as c:

            def _slot_6(c):
                c.path([[0.0, 0.0], [0.0, 4.0]], [1, 2], id='grid_v0', edgecolor='#DC2626', linewidth=1.5, joinstyle='round', fill=False)
                for object_id, points in [('grid_v1', [[1.0, 0.0], [1.0, 4.0]]), ('grid_v2', [[2.0, 0.0], [2.0, 4.0]]), ('grid_v3', [[3.0, 0.0], [3.0, 4.0]]), ('grid_v4', [[4.0, 0.0], [4.0, 4.0]]), ('grid_v5', [[5.0, 0.0], [5.0, 4.0]])]:
                    c.line(points, id=object_id)
                c.path([[6.0, 0.0], [6.0, 4.0]], [1, 2], id='grid_v6', edgecolor='#DC2626', linewidth=1.5, joinstyle='round', fill=False)
            self._draw_choices(c, custom={6: _slot_6}, kw={2: {'edgecolor': '#DC2626', 'linewidth': 1.5}, 4: {'edgecolor': '#DC2626', 'linewidth': 1.5}, 7: {'edgecolor': '#DC2626', 'linewidth': 1.5}, 9: {'edgecolor': '#DC2626', 'linewidth': 1.5}, 11: {'edgecolor': '#DC2626', 'linewidth': 1.5}, 13: {'edgecolor': '#DC2626', 'linewidth': 1.5}})
            return c.save(output_path)

    def draw_C03(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane125_C03.png'
        with Canvas(PLANE, xlim=(-0.13953488372093048, 6.1395348837209305), ylim=(-1.1395348837209305, 5.1395348837209305)) as c:
            self._draw_choices(c, kw={1: {'edgecolor': '#DC2626', 'linewidth': 3.0}, 3: {'edgecolor': '#DC2626', 'linewidth': 3.0}, 5: {'edgecolor': '#DC2626', 'linewidth': 3.0}, 8: {'edgecolor': '#DC2626', 'linewidth': 3.0}, 12: {'edgecolor': '#DC2626', 'linewidth': 3.0}})
            return c.save(output_path)

    def draw_C04(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane125_C04.png'
        with Canvas(PLANE, xlim=(-0.13953488372093048, 6.1395348837209305), ylim=(-1.1395348837209305, 5.1395348837209305)) as c:
            self._draw_choices(c, kw={1: {'edgecolor': '#2563EB', 'linewidth': 3.0}, 3: {'edgecolor': '#2563EB', 'linewidth': 3.0}, 5: {'edgecolor': '#2563EB', 'linewidth': 3.0}, 8: {'edgecolor': '#2563EB', 'linewidth': 3.0}, 12: {'edgecolor': '#2563EB', 'linewidth': 3.0}})
            return c.save(output_path)

    def draw_C05(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane125_C05.png'
        with Canvas(PLANE, xlim=(-0.13953488372093048, 6.1395348837209305), ylim=(-1.1395348837209305, 5.1395348837209305)) as c:

            def _slot_6(c):
                c.path([[0.0, 0.0], [0.0, 4.0]], [1, 2], id='grid_v0', edgecolor='#DC2626', linewidth=3.0, joinstyle='round', fill=False)
                for object_id, points in [('grid_v1', [[1.0, 0.0], [1.0, 4.0]]), ('grid_v2', [[2.0, 0.0], [2.0, 4.0]]), ('grid_v3', [[3.0, 0.0], [3.0, 4.0]]), ('grid_v4', [[4.0, 0.0], [4.0, 4.0]]), ('grid_v5', [[5.0, 0.0], [5.0, 4.0]])]:
                    c.line(points, id=object_id)
                c.path([[6.0, 0.0], [6.0, 4.0]], [1, 2], id='grid_v6', edgecolor='#DC2626', linewidth=3.0, joinstyle='round', fill=False)
            self._draw_choices(c, custom={6: _slot_6}, kw={2: {'edgecolor': '#DC2626', 'linewidth': 3.0}, 4: {'edgecolor': '#DC2626', 'linewidth': 3.0}, 7: {'edgecolor': '#DC2626', 'linewidth': 3.0}, 9: {'edgecolor': '#DC2626', 'linewidth': 3.0}, 11: {'edgecolor': '#DC2626', 'linewidth': 3.0}, 13: {'edgecolor': '#DC2626', 'linewidth': 3.0}})
            return c.save(output_path)

    def draw_C06(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane125_C06.png'
        with Canvas(PLANE, xlim=(-0.13953488372093048, 6.1395348837209305), ylim=(-1.1395348837209305, 5.1395348837209305)) as c:

            def _slot_6(c):
                c.path([[0.0, 0.0], [0.0, 4.0]], [1, 2], id='grid_v0', edgecolor='#2563EB', linewidth=3.0, joinstyle='round', fill=False)
                for object_id, points in [('grid_v1', [[1.0, 0.0], [1.0, 4.0]]), ('grid_v2', [[2.0, 0.0], [2.0, 4.0]]), ('grid_v3', [[3.0, 0.0], [3.0, 4.0]]), ('grid_v4', [[4.0, 0.0], [4.0, 4.0]]), ('grid_v5', [[5.0, 0.0], [5.0, 4.0]])]:
                    c.line(points, id=object_id)
                c.path([[6.0, 0.0], [6.0, 4.0]], [1, 2], id='grid_v6', edgecolor='#2563EB', linewidth=3.0, joinstyle='round', fill=False)
            self._draw_choices(c, custom={6: _slot_6}, kw={2: {'edgecolor': '#2563EB', 'linewidth': 3.0}, 4: {'edgecolor': '#2563EB', 'linewidth': 3.0}, 7: {'edgecolor': '#2563EB', 'linewidth': 3.0}, 9: {'edgecolor': '#2563EB', 'linewidth': 3.0}, 11: {'edgecolor': '#2563EB', 'linewidth': 3.0}, 13: {'edgecolor': '#2563EB', 'linewidth': 3.0}})
            return c.save(output_path)
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Plane125')
    parser.add_argument('output', nargs='?')
    parser.add_argument('--variant', choices=('C01', 'C02', 'C03', 'C04', 'C05', 'C06'))
    args = parser.parse_args()
    print(Plane125().draw(args.output, variant=args.variant))
