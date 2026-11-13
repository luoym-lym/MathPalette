"""Collected question Plane143; construction on the shared drawing protocol."""
from pathlib import Path
import sys
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from MathPalette_Dataset.drawing import Canvas, PLANE

class Plane143:
    variants = ('C01', 'C02', 'C03', 'C04')

    def _draw_base(self, c, kw=None, custom=None):
        _kw = kw or {}
        c.path([[16.0, 16.0], [16.0, 20.0], [19.0, 17.0], [21.0, 19.0], [22.0, 18.0], [23.0, 19.0], [25.0, 17.0], [28.0, 20.0], [28.0, 16.0], [16.0, 16.0]], [1, 2, 2, 2, 2, 2, 2, 2, 2, 79], id='source', alpha=0.45, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
        if custom and 1 in custom:
            custom[1](c)
        else:
            c.path([[16.0, 16.0], [16.0, 20.0], [19.0, 17.0], [21.0, 19.0], [22.0, 18.0], [23.0, 19.0], [25.0, 17.0], [28.0, 20.0], [28.0, 16.0], [16.0, 16.0]], [1, 2, 2, 2, 2, 2, 2, 2, 2, 79], id='source', capstyle='butt', fill=False)
        c.path([[0.0, 8.0], [0.0, 9.0], [3.0, 12.0], [6.0, 9.0], [9.0, 12.0], [12.0, 9.0], [12.0, 8.0], [0.0, 8.0]], [1, 2, 2, 2, 2, 2, 2, 79], id='A', alpha=0.45, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
        c.path([[0.0, 8.0], [0.0, 9.0], [3.0, 12.0], [6.0, 9.0], [9.0, 12.0], [12.0, 9.0], [12.0, 8.0], [0.0, 8.0]], [1, 2, 2, 2, 2, 2, 2, 79], id='A', capstyle='butt', fill=False, **_kw.get(3, {}))
        c.path([[18.0, 8.0], [18.0, 9.3], [20.8, 12.0], [22.2, 10.7], [23.6, 12.0], [26.4, 9.3], [29.2, 12.0], [30.6, 10.7], [32.0, 12.0], [34.8, 9.3], [34.8, 8.0], [18.0, 8.0]], [1] + [2] * 10 + [79], id='B', alpha=0.45, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
        c.path([[18.0, 8.0], [18.0, 9.3], [20.8, 12.0], [22.2, 10.7], [23.6, 12.0], [26.4, 9.3], [29.2, 12.0], [30.6, 10.7], [32.0, 12.0], [34.8, 9.3], [34.8, 8.0], [18.0, 8.0]], [1] + [2] * 10 + [79], id='B', capstyle='butt', fill=False, **_kw.get(5, {}))
        c.path([[0.0, 0.0], [0.0, 1.0], [3.0, 4.0], [4.0, 3.0], [5.0, 4.0], [6.0, 3.0], [7.0, 4.0], [8.0, 3.0], [9.0, 4.0], [12.0, 1.0], [12.0, 0.0], [0.0, 0.0]], [1] + [2] * 10 + [79], id='C', alpha=0.45, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
        c.path([[0.0, 0.0], [0.0, 1.0], [3.0, 4.0], [4.0, 3.0], [5.0, 4.0], [6.0, 3.0], [7.0, 4.0], [8.0, 3.0], [9.0, 4.0], [12.0, 1.0], [12.0, 0.0], [0.0, 0.0]], [1] + [2] * 10 + [79], id='C', capstyle='butt', fill=False, **_kw.get(7, {}))
        c.path([[18.0, 0.0], [18.0, 1.0], [20.0, 2.3], [21.0, 1.4], [24.0, 4.0], [27.0, 1.4], [28.0, 2.2], [30.0, 1.0], [30.0, 0.0], [18.0, 0.0]], [1, 2, 2, 2, 2, 2, 2, 2, 2, 79], id='D', alpha=0.45, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
        if custom and 9 in custom:
            custom[9](c)
        else:
            c.path([[18.0, 0.0], [18.0, 1.0], [20.0, 2.3], [21.0, 1.4], [24.0, 4.0], [27.0, 1.4], [28.0, 2.2], [30.0, 1.0], [30.0, 0.0], [18.0, 0.0]], [1, 2, 2, 2, 2, 2, 2, 2, 2, 79], id='D', capstyle='butt', fill=False)
        c.path([[36.0, 0.0], [36.0, 1.0], [39.0, 4.0], [41.0, 2.0], [42.0, 3.0], [43.0, 2.0], [45.0, 4.0], [48.0, 1.0], [48.0, 0.0], [36.0, 0.0]], [1, 2, 2, 2, 2, 2, 2, 2, 2, 79], id='E', alpha=0.45, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
        c.path([[36.0, 0.0], [36.0, 1.0], [39.0, 4.0], [41.0, 2.0], [42.0, 3.0], [43.0, 2.0], [45.0, 4.0], [48.0, 1.0], [48.0, 0.0], [36.0, 0.0]], [1, 2, 2, 2, 2, 2, 2, 2, 2, 79], id='E', capstyle='butt', fill=False, **_kw.get(11, {}))
        for object_id, text, anchor in [('label0', '(A)', (-1.6, 8.5)), ('label1', '(B)', (16.4, 8.5)), ('label2', '(C)', (-1.6, 0.5)), ('label3', '(D)', (16.4, 0.5)), ('label4', '(E)', (34.4, 0.5))]:
            c.text(text, anchor, id=object_id)

    def draw(self, output_path=None, *, variant=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / (self.__class__.__name__ + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if variant not in self.variants:
                raise ValueError('Unknown Special variant: ' + str(variant))
            return getattr(self, 'draw_' + variant)(output_path)
        with Canvas(PLANE, xlim=(-3.9021095661614638, 49.24300703085192), ylim=(-16.633964504742366, 36.51115209227102)) as c:
            self._draw_base(c)
            return c.save(output_path)

    def draw_C01(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane143_C01.png'
        with Canvas(PLANE, xlim=(-3.9021095661614638, 49.24300703085192), ylim=(-16.633964504742366, 36.51115209227102)) as c:

            def _slot_1(c):
                c.path([[16.0, 16.0], [16.0, 20.0], [19.0, 17.0], [21.0, 19.0], [22.0, 18.0], [23.0, 19.0], [25.0, 17.0], [28.0, 20.0], [28.0, 16.0], [16.0, 16.0]], [1, 2, 2, 2, 2, 2, 2, 2, 2, 79], id='source', edgecolor='#DC2626', capstyle='butt', fill=False)

            def _slot_9(c):
                c.path([[18.0, 0.0], [18.0, 1.0], [20.0, 2.3], [21.0, 1.4], [24.0, 4.0], [27.0, 1.4], [28.0, 2.2], [30.0, 1.0], [30.0, 0.0], [18.0, 0.0]], [1, 2, 2, 2, 2, 2, 2, 2, 2, 79], id='D', edgecolor='#DC2626', linewidth=2.0, capstyle='butt', fill=False)
            self._draw_base(c, custom={1: _slot_1, 9: _slot_9}, kw={3: {'linestyle': (0, [3.7, 1.6])}, 5: {'linestyle': (0, [3.7, 1.6])}, 7: {'linestyle': (0, [3.7, 1.6])}, 11: {'linestyle': (0, [3.7, 1.6])}})
            return c.save(output_path)

    def draw_C02(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane143_C02.png'
        with Canvas(PLANE, xlim=(-3.9021095661614638, 49.24300703085192), ylim=(-16.633964504742366, 36.51115209227102)) as c:
            self._draw_base(c)
            c.line([[0, 1], [3, 4]], zorder=9, color='#2563EB', solid_capstyle='butt')
            c.line([[9, 4], [12, 1]], zorder=9, color='#2563EB', solid_capstyle='butt')
            for object_id, points in [(None, [[3, 4], [4, 3]]), (None, [[4, 3], [5, 4]]), (None, [[5, 4], [6, 3]]), (None, [[6, 3], [7, 4]]), (None, [[7, 4], [8, 3]]), (None, [[8, 3], [9, 4]])]:
                c.line(points, id=object_id, zorder=9, color='#EA580C', solid_capstyle='butt')
            c.line([[16, 20], [19, 17]], zorder=9, color='#2563EB', solid_capstyle='butt')
            c.line([[25, 17], [28, 20]], zorder=9, color='#2563EB', solid_capstyle='butt')
            for object_id, points in [(None, [[19, 17], [21, 19]]), (None, [[21, 19], [22, 18]]), (None, [[22, 18], [23, 19]]), (None, [[23, 19], [25, 17]])]:
                c.line(points, id=object_id, zorder=9, color='#EA580C', solid_capstyle='butt')
            return c.save(output_path)

    def draw_C03(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane143_C03.png'
        with Canvas(PLANE, xlim=(-3.9021095661614638, 49.24300703085192), ylim=(-16.633964504742366, 36.51115209227102)) as c:

            def _slot_1(c):
                c.path([[15.999999999999998, 15.999999999999995], [15.999999999999998, 19.999999999999993]], [1, 2], id='source', capstyle='butt', fill=False)
                c.path([[15.999999999999998, 19.999999999999993], [18.999999999999996, 16.999999999999993], [19.0, 17.0]], [1, 2, 2], id='source', edgecolor='#16A34A', capstyle='butt', fill=False)
                c.path([[19.0, 17.0], [20.999999999999996, 18.999999999999993], [21.999999999999996, 17.999999999999993], [22.999999999999996, 18.999999999999993], [24.99999999999999, 16.999999999999996]], [1, 2, 2, 2, 2], id='source', edgecolor='#DC2626', linewidth=1.5, capstyle='butt', fill=False)
                c.path([[24.99999999999999, 16.999999999999996], [24.999999999999996, 16.999999999999993], [27.999999999999996, 19.999999999999993]], [1, 2, 2], id='source', edgecolor='#16A34A', linewidth=1.5, capstyle='butt', fill=False)
                c.path([[27.999999999999996, 19.999999999999993], [27.999999999999996, 15.999999999999995], [15.999999999999998, 15.999999999999995]], [1, 2, 2], id='source', capstyle='butt', fill=False)

            def _slot_9(c):
                c.path([[17.999999999999996, -3.552713678800501e-15], [17.999999999999996, 0.9999999999999963], [18.000000000000004, 0.9999999999999996]], [1, 2, 2], id='D', capstyle='butt', fill=False)
                c.path([[18.000000000000004, 0.9999999999999996], [19.999999999999996, 2.299999999999996]], [1, 2], id='D', edgecolor='#16A34A', linewidth=1.5, capstyle='butt', fill=False)
                c.path([[19.999999999999996, 2.299999999999996], [20.999999999999996, 1.3999999999999961], [23.999999999999996, 3.999999999999996], [26.999999999999996, 1.3999999999999961], [27.999999999999996, 2.199999999999996]], [1, 2, 2, 2, 2], id='D', edgecolor='#DC2626', linewidth=1.5, capstyle='butt', fill=False)
                c.path([[27.999999999999996, 2.199999999999996], [29.999999999999996, 0.9999999999999963]], [1, 2], id='D', edgecolor='#16A34A', linewidth=1.5, capstyle='butt', fill=False)
                c.path([[29.999999999999996, 0.9999999999999963], [29.999999999999996, -3.552713678800501e-15], [17.999999999999996, -3.552713678800501e-15]], [1, 2, 2], id='D', capstyle='butt', fill=False)
            self._draw_base(c, custom={1: _slot_1, 9: _slot_9})
            return c.save(output_path)

    def draw_C04(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane143_C04.png'
        with Canvas(PLANE, xlim=(-3.9021095661614638, 49.24300703085192), ylim=(-16.633964504742366, 36.51115209227102)) as c:

            def _slot_1(c):
                c.path([[15.999999999999998, 15.999999999999995], [15.999999999999998, 19.999999999999993]], [1, 2], id='source', capstyle='butt', fill=False)
                c.path([[15.999999999999998, 19.999999999999993], [18.999999999999996, 16.999999999999993], [20.999999999999996, 18.999999999999993]], [1, 2, 2], id='source', edgecolor='#EA580C', capstyle='butt', fill=False)
                c.path([[20.999999999999996, 18.999999999999993], [21.999999999999996, 17.999999999999993], [22.999999999999996, 18.999999999999993]], [1, 2, 2], id='source', edgecolor='#2563EB', capstyle='butt', fill=False)
                c.path([[22.999999999999996, 18.999999999999993], [24.999999999999996, 16.999999999999993], [27.999999999999996, 19.999999999999993]], [1, 2, 2], id='source', edgecolor='#EA580C', capstyle='butt', fill=False)
                c.path([[27.999999999999996, 19.999999999999993], [27.999999999999996, 15.999999999999995], [15.999999999999998, 15.999999999999995]], [1, 2, 2], id='source', capstyle='butt', fill=False)

            def _slot_9(c):
                c.path([[17.999999999999996, -3.552713678800501e-15], [17.999999999999996, 0.9999999999999963], [18.000000000000004, 0.9999999999999996]], [1, 2, 2], id='D', capstyle='butt', fill=False)
                c.path([[18.000000000000004, 0.9999999999999996], [19.999999999999996, 2.299999999999996], [20.999999999999996, 1.3999999999999961], [22.483333836660357, 2.6855559917723095]], [1, 2, 2, 2], id='D', edgecolor='#EA580C', capstyle='butt', fill=False)
                c.path([[22.483333836660357, 2.685555991772309], [22.514327881406114, 2.712417497218631]], [1, 2], id='D', capstyle='butt', fill=False)
                c.path([[22.514327881406114, 2.712417497218631], [23.999999999999996, 3.999999999999996], [25.370146189318724, 2.8125399692571]], [1, 2, 2], id='D', edgecolor='#2563EB', capstyle='butt', fill=False)
                c.path([[25.370146189318724, 2.8125399692571], [25.458995784256558, 2.7355369869776434]], [1, 2], id='D', capstyle='butt', fill=False)
                c.path([[25.458995784256558, 2.7355369869776434], [26.999999999999996, 1.3999999999999961], [27.999999999999996, 2.199999999999996], [29.999999999999996, 0.9999999999999963]], [1, 2, 2, 2], id='D', edgecolor='#EA580C', capstyle='butt', fill=False)
                c.path([[29.999999999999996, 0.9999999999999963], [29.999999999999996, -3.552713678800501e-15], [17.999999999999996, -3.552713678800501e-15]], [1, 2, 2], id='D', capstyle='butt', fill=False)
            self._draw_base(c, custom={1: _slot_1, 9: _slot_9})
            return c.save(output_path)
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Plane143')
    parser.add_argument('output', nargs='?')
    parser.add_argument('--variant', choices=('C01', 'C02', 'C03', 'C04'))
    args = parser.parse_args()
    print(Plane143().draw(args.output, variant=args.variant))
