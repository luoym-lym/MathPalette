"""Collected question Plane236; construction on the shared drawing protocol."""
from pathlib import Path
import sys
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from MathPalette_Dataset.drawing import Canvas, PLANE

class Plane236:
    variants = ('C01', 'C02', 'C03', 'C04', 'C05', 'C06')

    def _draw_base(self, c, hi=None):
        _hi = hi or {}
        c.path([[0.0, 1.0], [4.0, 1.0], [4.0, 5.0], [0.0, 5.0], [0.0, 1.0]], [1, 2, 2, 2, 79], id='o0', capstyle='butt')
        for object_id, points in [('o1', [[1.0, 1.0], [1.0, 5.0]]), ('o2', [[3.0, 1.0], [3.0, 5.0]]), ('o3', [[0.0, 2.0], [4.0, 2.0]]), ('o4', [[0.0, 4.0], [4.0, 4.0]])]:
            c.line(points, id=object_id, linestyle=(0.0, [4.0, 3.0]))
        for object_id, points in [('o5', [[0.6, 4.4], [1.4, 3.6]]), ('o6', [[2.6, 3.6], [3.4, 4.4]]), ('o7', [[0.6, 2.4], [1.4, 1.6]]), ('o8', [[2.6, 1.6], [3.4, 2.4]]), ('o9', [[-1.0, 4.0], [1.0, 4.0]])]:
            c.line(points, id=object_id)
        c.path([[1.0, 4.0], [0.78, 4.08], [0.78, 3.92], [1.0, 4.0]], [1, 2, 2, 79], id='o10', zorder=1, edgecolor='none', facecolor='black', linewidth=0.0, capstyle='butt')
        c.path([[1.0, 4.0], [0.78, 4.08], [0.78, 3.92], [1.0, 4.0]], [1, 2, 2, 79], id='o10', capstyle='butt', fill=False)
        c.line([[1.0, 4.0], [1.0, 2.0]], id='o11')
        c.path([[1.0, 2.0], [1.08, 2.22], [0.92, 2.22], [1.0, 2.0]], [1, 2, 2, 79], id='o12', zorder=1, edgecolor='none', facecolor='black', linewidth=0.0, capstyle='butt')
        c.path([[1.0, 2.0], [1.08, 2.22], [0.92, 2.22], [1.0, 2.0]], [1, 2, 2, 79], id='o12', capstyle='butt', fill=False)
        c.line([[1.0, 2.0], [3.0, 2.0]], id='o13')
        c.path([[3.0, 2.0], [2.78, 2.08], [2.78, 1.92], [3.0, 2.0]], [1, 2, 2, 79], id='o14', zorder=1, edgecolor='none', facecolor='black', linewidth=0.0, capstyle='butt')
        c.path([[3.0, 2.0], [2.78, 2.08], [2.78, 1.92], [3.0, 2.0]], [1, 2, 2, 79], id='o14', capstyle='butt', fill=False)
        c.line([[3.0, 2.0], [3.0, 4.0]], id='o15')
        c.path([[3.0, 4.0], [2.92, 3.78], [3.08, 3.78], [3.0, 4.0]], [1, 2, 2, 79], id='o16', zorder=1, edgecolor='none', facecolor='black', linewidth=0.0, capstyle='butt')
        c.path([[3.0, 4.0], [2.92, 3.78], [3.08, 3.78], [3.0, 4.0]], [1, 2, 2, 79], id='o16', capstyle='butt', fill=False)
        c.line([[3.0, 4.0], [5.0, 4.0]], id='o17')
        c.path([[5.0, 4.0], [4.78, 4.08], [4.78, 3.92], [5.0, 4.0]], [1, 2, 2, 79], id='o18', zorder=1, edgecolor='none', facecolor='black', linewidth=0.0, capstyle='butt')
        c.path([[5.0, 4.0], [4.78, 4.08], [4.78, 3.92], [5.0, 4.0]], [1, 2, 2, 79], id='o18', capstyle='butt', fill=False)
        c.path([[6.0, 0.0], [15.0, 0.0], [15.0, 6.0], [6.0, 6.0], [6.0, 0.0]], [1, 2, 2, 2, 79], id='o19', capstyle='butt')
        _defs = [{}, {}, {}, {}, {'color': '#2563EB', 'linewidth': 2.0}]
        _ov = {j: s for idxs, s in _hi.get(18, ()) for j in idxs}
        for i, (object_id, points) in enumerate([('o20', [[7.5, 0.0], [7.5, 6.0]]), ('o21', [[10.5, 0.0], [10.5, 6.0]]), ('o22', [[13.5, 0.0], [13.5, 6.0]]), ('o23', [[6.0, 1.5], [15.0, 1.5]]), ('o24', [[6.0, 4.5], [15.0, 4.5]])]):
            c.line(points, id=object_id, linestyle=(0.0, [4.0, 3.0]), **_ov.get(i, _defs[i]))
        _ov = {j: s for idxs, s in _hi.get(19, ()) for j in idxs}
        for i, (object_id, points) in enumerate([('o25', [[6.9, 5.1], [8.1, 3.9]]), ('o26', [[9.9, 3.9], [11.1, 5.1]]), ('o27', [[12.9, 5.1], [14.1, 3.9]]), ('o28', [[6.9, 2.1], [8.1, 0.9]]), ('o29', [[9.9, 0.9], [11.1, 2.1]]), ('o30', [[12.9, 0.9], [14.1, 2.1]]), ('o31', [[4.8, 4.5], [7.5, 4.5]])]):
            c.line(points, id=object_id, **_ov[i]) if i in _ov else c.line(points, id=object_id)
        c.path([[7.5, 4.5], [7.28, 4.58], [7.28, 4.42], [7.5, 4.5]], [1, 2, 2, 79], id='o32', zorder=1, edgecolor='none', facecolor='black', linewidth=0.0, capstyle='butt')
        c.path([[7.5, 4.5], [7.28, 4.58], [7.28, 4.42], [7.5, 4.5]], [1, 2, 2, 79], id='o32', capstyle='butt', fill=False)
        for object_id, text, anchor in [('t0', 'A', (7.5, -0.7)), ('t1', 'B', (10.5, -0.7)), ('t2', 'C', (13.5, -0.7)), ('t3', 'D', (15.7, 1.5)), ('t4', 'E', (15.7, 4.5))]:
            c.text(text, anchor, id=object_id)

    def draw(self, output_path=None, *, variant=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / (self.__class__.__name__ + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if variant not in self.variants:
                raise ValueError('Unknown Special variant: ' + str(variant))
            return getattr(self, 'draw_' + variant)(output_path)
        with Canvas(PLANE, xlim=(-1.4150335547329664, 16.27532336824312), ylim=(-6.262004552846797, 11.42835237012929)) as c:
            self._draw_base(c, hi={18: [({4}, {})]})
            return c.save(output_path)

    def draw_C01(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane236_C01.png'
        with Canvas(PLANE, xlim=(-1.4150335547329664, 16.27532336824312), ylim=(-6.262004552846797, 11.42835237012929)) as c:
            self._draw_base(c, hi={18: [({3}, {'color': '#2563EB', 'linewidth': 2.0}), ({4}, {})]})
            return c.save(output_path)

    def draw_C02(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane236_C02.png'
        with Canvas(PLANE, xlim=(-1.4150335547329664, 16.27532336824312), ylim=(-6.262004552846797, 11.42835237012929)) as c:
            self._draw_base(c)
            return c.save(output_path)

    def draw_C03(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane236_C03.png'
        with Canvas(PLANE, xlim=(-1.4150335547329664, 16.27532336824312), ylim=(-6.262004552846797, 11.42835237012929)) as c:
            self._draw_base(c, hi={18: [({3}, {'color': '#2563EB', 'linewidth': 2.0}), ({4}, {'color': '#2563EB', 'linewidth': 1.5})]})
            c.point([[15.0, 1.5]], zorder=10, s=50, facecolors='#DC2626', edgecolors='#DC2626')
            return c.save(output_path)

    def draw_C04(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane236_C04.png'
        with Canvas(PLANE, xlim=(-1.4150335547329664, 16.27532336824312), ylim=(-6.262004552846797, 11.42835237012929)) as c:
            self._draw_base(c, hi={19: [({2}, {'color': '#2563EB', 'linewidth': 1.5})]})
            c.point([[13.5, 0.0]], zorder=10, s=50, facecolors='#DC2626', edgecolors='#DC2626')
            return c.save(output_path)

    def draw_C05(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane236_C05.png'
        with Canvas(PLANE, xlim=(-1.4150335547329664, 16.27532336824312), ylim=(-6.262004552846797, 11.42835237012929)) as c:
            self._draw_base(c, hi={18: [({0}, {'color': '#2563EB', 'linewidth': 3.0}), ({4}, {'color': '#2563EB', 'linewidth': 1.5})]})
            c.point([[13.5, 0.0]], zorder=10, s=50, facecolors='#DC2626', edgecolors='#DC2626')
            return c.save(output_path)

    def draw_C06(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane236_C06.png'
        with Canvas(PLANE, xlim=(-1.4150335547329664, 16.27532336824312), ylim=(-6.262004552846797, 11.42835237012929)) as c:
            self._draw_base(c, hi={18: [({2}, {'color': '#2563EB', 'linewidth': 1.5})]})
            c.point([[13.5, 0.0]], zorder=10, s=50, facecolors='#DC2626', edgecolors='#DC2626')
            return c.save(output_path)
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Plane236')
    parser.add_argument('output', nargs='?')
    parser.add_argument('--variant', choices=('C01', 'C02', 'C03', 'C04', 'C05', 'C06'))
    args = parser.parse_args()
    print(Plane236().draw(args.output, variant=args.variant))
