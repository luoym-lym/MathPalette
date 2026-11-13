"""Collected question Plane123; construction on the shared drawing protocol."""
from pathlib import Path
import sys
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from MathPalette_Dataset.drawing import Canvas, PLANE

class Plane123:
    variants = ('C01', 'C02', 'C03', 'C04', 'C05')

    def _draw_base(self, c, hi=None, custom=None):
        _hi = hi or {}
        c.path([[0.0, 0.0], [2.0, 0.0], [4.0, 2.0], [2.0, 4.0], [0.0, 4.0], [1.0, 2.0], [0.0, 0.0]], [1, 2, 2, 2, 2, 2, 79], alpha=0.45, zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), capstyle='butt')
        if custom and 1 in custom:
            custom[1](c)
        else:
            c.path([[5.551115123125783e-17, 5.551115123125783e-17], [2.0, 5.551115123125783e-17], [4.0, 2.0], [2.0, 4.0], [5.551115123125783e-17, 4.0]], [1, 2, 2, 2, 2], id='shade', edgecolor='#DC2626', capstyle='butt', fill=False)
            c.path([[5.551115123125783e-17, 4.0], [1.0, 2.0], [5.551115123125783e-17, 5.551115123125783e-17]], [1, 2, 2], id='shade', capstyle='butt', fill=False)
        _defs = [{'color': '#DC2626'}, {}, {}, {}, {}, {}, {}, {}, {}, {}]
        _ov = {j: s for idxs, s in _hi.get(3, ()) for j in idxs}
        for i, (object_id, points) in enumerate([('grid_v0', [[0.0, 0.0], [0.0, 4.0]]), ('grid_v1', [[1.0, 0.0], [1.0, 4.0]]), ('grid_v2', [[2.0, 0.0], [2.0, 4.0]]), ('grid_v3', [[3.0, 0.0], [3.0, 4.0]]), ('grid_v4', [[4.0, 0.0], [4.0, 4.0]]), ('grid_h0', [[0.0, 0.0], [4.0, 0.0]]), ('grid_h1', [[0.0, 1.0], [4.0, 1.0]]), ('grid_h2', [[0.0, 2.0], [4.0, 2.0]]), ('grid_h3', [[0.0, 3.0], [4.0, 3.0]]), ('grid_h4', [[0.0, 4.0], [4.0, 4.0]])]):
            c.line(points, id=object_id, **_ov.get(i, _defs[i]))

    def draw(self, output_path=None, *, variant=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / (self.__class__.__name__ + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if variant not in self.variants:
                raise ValueError('Unknown Special variant: ' + str(variant))
            return getattr(self, 'draw_' + variant)(output_path)
        with Canvas(PLANE, xlim=(-0.09302325581395365, 4.093023255813954), ylim=(-0.09302325581395365, 4.093023255813954)) as c:

            def _slot_1(c):
                c.path([[0.0, 0.0], [2.0, 0.0], [4.0, 2.0], [2.0, 4.0], [0.0, 4.0], [1.0, 2.0], [0.0, 0.0]], [1, 2, 2, 2, 2, 2, 79], id='shade', capstyle='butt', fill=False)
            self._draw_base(c, custom={1: _slot_1}, hi={3: [({0}, {})]})
            return c.save(output_path)

    def draw_C01(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane123_C01.png'
        with Canvas(PLANE, xlim=(-0.09302325581395365, 4.093023255813954), ylim=(-0.09302325581395365, 4.093023255813954)) as c:
            self._draw_base(c)
            return c.save(output_path)

    def draw_C02(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane123_C02.png'
        with Canvas(PLANE, xlim=(-0.09302325581395365, 4.093023255813954), ylim=(-0.09302325581395365, 4.093023255813954)) as c:

            def _slot_1(c):
                c.path([[5.551115123125783e-17, 5.551115123125783e-17], [2.0, 5.551115123125783e-17], [4.0, 2.0], [2.0, 4.0], [5.551115123125783e-17, 4.0]], [1, 2, 2, 2, 2], id='shade', edgecolor='#2563EB', linewidth=2.0, capstyle='butt', fill=False)
                c.path([[5.551115123125783e-17, 4.0], [1.0, 2.0], [5.551115123125783e-17, 5.551115123125783e-17]], [1, 2, 2], id='shade', capstyle='butt', fill=False)
            self._draw_base(c, custom={1: _slot_1}, hi={3: [({0}, {'color': '#2563EB', 'linewidth': 2.0})]})
            return c.save(output_path)

    def draw_C03(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane123_C03.png'
        with Canvas(PLANE, xlim=(-0.09302325581395365, 4.093023255813954), ylim=(-0.09302325581395365, 4.093023255813954)) as c:

            def _slot_1(c):
                c.path([[5.551115123125783e-17, 5.551115123125783e-17], [2.0, 5.551115123125783e-17], [4.0, 2.0], [2.0, 4.0], [5.551115123125783e-17, 4.0]], [1, 2, 2, 2, 2], id='shade', edgecolor='#16A34A', linewidth=3.0, capstyle='butt', fill=False)
                c.path([[5.551115123125783e-17, 4.0], [1.0, 2.0], [5.551115123125783e-17, 5.551115123125783e-17]], [1, 2, 2], id='shade', capstyle='butt', fill=False)
            self._draw_base(c, custom={1: _slot_1}, hi={3: [({0}, {'color': '#16A34A', 'linewidth': 3.0})]})
            return c.save(output_path)

    def draw_C04(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane123_C04.png'
        with Canvas(PLANE, xlim=(-0.09302325581395365, 4.093023255813954), ylim=(-0.09302325581395365, 4.093023255813954)) as c:

            def _slot_1(c):
                c.path([[5.551115123125783e-17, 5.551115123125783e-17], [2.0, 5.551115123125783e-17], [4.0, 2.0], [2.0, 4.0], [5.551115123125783e-17, 4.0]], [1, 2, 2, 2, 2], id='shade', edgecolor='#EA580C', linewidth=2.0, capstyle='butt', fill=False)
                c.path([[5.551115123125783e-17, 4.0], [1.0, 2.0], [5.551115123125783e-17, 5.551115123125783e-17]], [1, 2, 2], id='shade', capstyle='butt', fill=False)
            self._draw_base(c, custom={1: _slot_1}, hi={3: [({0}, {'color': '#EA580C', 'linewidth': 2.0})]})
            return c.save(output_path)

    def draw_C05(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane123_C05.png'
        with Canvas(PLANE, xlim=(-0.09302325581395365, 4.093023255813954), ylim=(-0.09302325581395365, 4.093023255813954)) as c:

            def _slot_1(c):
                c.path([[5.551115123125783e-17, 5.551115123125783e-17], [2.0, 5.551115123125783e-17], [4.0, 2.0], [2.0, 4.0], [5.551115123125783e-17, 4.0]], [1, 2, 2, 2, 2], id='shade', edgecolor='#DC2626', linewidth=3.0, capstyle='butt', fill=False)
                c.path([[5.551115123125783e-17, 4.0], [1.0, 2.0], [5.551115123125783e-17, 5.551115123125783e-17]], [1, 2, 2], id='shade', capstyle='butt', fill=False)
            self._draw_base(c, custom={1: _slot_1}, hi={3: [({0}, {'color': '#DC2626', 'linewidth': 3.0})]})
            return c.save(output_path)
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Plane123')
    parser.add_argument('output', nargs='?')
    parser.add_argument('--variant', choices=('C01', 'C02', 'C03', 'C04', 'C05'))
    args = parser.parse_args()
    print(Plane123().draw(args.output, variant=args.variant))
