"""Collected question Plane217; construction on the shared drawing protocol."""
from pathlib import Path
import sys
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from MathPalette_Dataset.drawing import Canvas, PLANE

class Plane217:
    variants = ('C01', 'C02', 'C03')

    def _draw_base(self, c, hi=None, kw=None):
        _hi = hi or {}
        _kw = kw or {}
        c.path([[8.0, 6.0], [12.0, 6.0], [12.0, 10.0], [8.0, 10.0], [8.0, 6.0]], [1, 2, 2, 2, 79], id='o0', capstyle='butt')
        _ov = {j: s for idxs, s in _hi.get(1, ()) for j in idxs}
        for i, (object_id, center, radius) in enumerate([('o1', [9.0, 7.45], 0.09), ('o2', [9.0, 8.55], 0.09), ('o3', [11.0, 7.45], 0.09), ('o4', [11.0, 8.55], 0.09)]):
            c.circle(center, radius, id=object_id, fill=False, **_ov[i]) if i in _ov else c.circle(center, radius, id=object_id, fill=False)
        c.path([[0.0, 0.0], [3.0, 0.0], [3.0, 3.0], [0.0, 3.0], [0.0, 0.0]], [1, 2, 2, 2, 79], id='o5', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
        c.path([[0.0, 0.0], [3.0, 0.0], [3.0, 3.0], [0.0, 3.0], [0.0, 0.0]], [1, 2, 2, 2, 79], id='o5', capstyle='butt', fill=False)
        c.line([[0.0, 0.0], [3.0, 3.0]], id='o6', linestyle=(0.0, [4.0, 3.0]), **_kw.get(4, {}))
        c.line([[0.0, 3.0], [3.0, 0.0]], id='o7', linestyle=(0.0, [4.0, 3.0]), **_kw.get(5, {}))
        c.path([[4.2, 0.0], [7.2, 0.0], [7.2, 3.0], [4.2, 3.0], [4.2, 0.0]], [1, 2, 2, 2, 79], id='o8', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
        c.path([[4.2, 0.0], [7.2, 0.0], [7.2, 3.0], [4.2, 3.0], [4.2, 0.0]], [1, 2, 2, 2, 79], id='o8', capstyle='butt', fill=False)
        for object_id, points in [('o9', [[4.95, 0.0], [4.95, 3.0]]), ('o10', [[5.7, 0.0], [5.7, 3.0]]), ('o11', [[6.45, 0.0], [6.45, 3.0]])]:
            c.line(points, id=object_id, linestyle=(0.0, [4.0, 3.0]))
        c.path([[8.4, 0.0], [11.4, 0.0], [11.4, 3.0], [8.4, 3.0], [8.4, 0.0]], [1, 2, 2, 2, 79], id='o12', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
        c.path([[8.4, 0.0], [11.4, 0.0], [11.4, 3.0], [8.4, 3.0], [8.4, 0.0]], [1, 2, 2, 2, 79], id='o12', capstyle='butt', fill=False)
        c.line([[9.9, 0.0], [9.9, 3.0]], id='o13', linestyle=(0.0, [4.0, 3.0]))
        c.line([[8.4, 1.5], [11.4, 1.5]], id='o14', linestyle=(0.0, [4.0, 3.0]))
        c.path([[12.600000000000001, 0.0], [15.600000000000001, 0.0], [15.600000000000001, 3.0], [12.600000000000001, 3.0], [12.600000000000001, 0.0]], [1, 2, 2, 2, 79], id='o15', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
        c.path([[12.600000000000001, 0.0], [15.600000000000001, 0.0], [15.600000000000001, 3.0], [12.600000000000001, 3.0], [12.600000000000001, 0.0]], [1, 2, 2, 2, 79], id='o15', capstyle='butt', fill=False)
        _ov = {j: s for idxs, s in _hi.get(15, ()) for j in idxs}
        for i, (object_id, points) in enumerate([('o16', [[12.600000000000001, 0.0], [15.600000000000001, 3.0]]), ('o17', [[12.600000000000001, 1.5], [14.100000000000001, 3.0]]), ('o18', [[14.100000000000001, 0.0], [15.600000000000001, 1.5]])]):
            c.line(points, id=object_id, linestyle=(0.0, [4.0, 3.0]), **_ov[i]) if i in _ov else c.line(points, id=object_id, linestyle=(0.0, [4.0, 3.0]))
        c.path([[16.8, 0.0], [19.8, 0.0], [19.8, 3.0], [16.8, 3.0], [16.8, 0.0]], [1, 2, 2, 2, 79], id='o19', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
        c.path([[16.8, 0.0], [19.8, 0.0], [19.8, 3.0], [16.8, 3.0], [16.8, 0.0]], [1, 2, 2, 2, 79], id='o19', capstyle='butt', fill=False)
        c.line([[17.8, 0.0], [17.8, 3.0]], id='o20', linestyle=(0.0, [4.0, 3.0]))
        c.line([[18.8, 0.0], [18.8, 3.0]], id='o21', linestyle=(0.0, [4.0, 3.0]))
        for object_id, text, anchor in [('t0', '(A)', (-0.5, 0.2)), ('t1', '(B)', (3.7, 0.2)), ('t2', '(C)', (7.9, 0.2)), ('t3', '(D)', (12.100000000000001, 0.2)), ('t4', '(E)', (16.3, 0.2))]:
            c.text(text, anchor, id=object_id)

    def draw(self, output_path=None, *, variant=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / (self.__class__.__name__ + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if variant not in self.variants:
                raise ValueError('Unknown Special variant: ' + str(variant))
            return getattr(self, 'draw_' + variant)(output_path)
        with Canvas(PLANE, xlim=(-1.4453489548654161, 20.3311548245613), ylim=(-5.916018220009818, 15.860485559416897)) as c:
            self._draw_base(c)
            return c.save(output_path)

    def draw_C01(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane217_C01.png'
        with Canvas(PLANE, xlim=(-1.4453489548654161, 20.3311548245613), ylim=(-5.916018220009818, 15.860485559416897)) as c:
            self._draw_base(c, hi={1: [({0, 3}, {'edgecolor': '#2563EB'}), ({1, 2}, {'edgecolor': '#DC2626'})]}, kw={4: {'color': '#2563EB'}, 5: {'color': '#DC2626'}})
            return c.save(output_path)

    def draw_C02(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane217_C02.png'
        with Canvas(PLANE, xlim=(-1.4453489548654161, 20.3311548245613), ylim=(-5.916018220009818, 15.860485559416897)) as c:
            self._draw_base(c, hi={1: [({0, 3}, {'edgecolor': '#DC2626', 'linewidth': 1.5})]}, kw={4: {'color': '#DC2626', 'linewidth': 1.5}})
            return c.save(output_path)

    def draw_C03(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane217_C03.png'
        with Canvas(PLANE, xlim=(-1.4453489548654161, 20.3311548245613), ylim=(-5.916018220009818, 15.860485559416897)) as c:
            self._draw_base(c, hi={1: [({0, 3}, {'edgecolor': '#DC2626'})], 15: [({0}, {'color': '#DC2626'})]})
            return c.save(output_path)
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Plane217')
    parser.add_argument('output', nargs='?')
    parser.add_argument('--variant', choices=('C01', 'C02', 'C03'))
    args = parser.parse_args()
    print(Plane217().draw(args.output, variant=args.variant))
