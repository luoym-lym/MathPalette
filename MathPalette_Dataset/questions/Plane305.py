"""Collected question Plane305; construction on the shared drawing protocol."""
from pathlib import Path
import sys
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from MathPalette_Dataset.drawing import Canvas, PLANE

class Plane305:
    variants = ('C01', 'C02', 'C03', 'C04')

    def _draw_base(self, c, hi=None, kw=None):
        _hi = hi or {}
        _kw = kw or {}
        c.path([[6.0, 6.0], [7.0, 6.0], [7.0, 7.0], [6.0, 7.0], [6.0, 6.0]], [1, 2, 2, 2, 79], id='color0', zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), linewidth=0.0, capstyle='butt')
        c.path([[6.0, 6.0], [7.0, 6.0], [7.0, 7.0], [6.0, 7.0], [6.0, 6.0]], [1, 2, 2, 2, 79], id='color0', capstyle='butt', fill=False, **_kw.get(1, {}))
        for object_id, points in [('line0_0', [[4.0, 0.0], [4.0, 8.0]]), ('line0_1', [[4.0, 4.0], [8.0, 4.0]]), ('line0_2', [[0.0, 0.0], [4.0, 8.0]]), ('line0_3', [[0.0, 4.0], [2.0, 8.0]]), ('line0_4', [[4.0, 8.0], [8.0, 4.0]]), ('line0_5', [[6.0, 6.0], [6.0, 8.0]]), ('line0_6', [[7.0, 6.0], [7.0, 8.0]]), ('line0_7', [[6.0, 6.0], [8.0, 6.0]]), ('line0_8', [[6.0, 7.0], [8.0, 7.0]])]:
            c.line(points, id=object_id)
        c.path([[0.0, 0.0], [8.0, 0.0], [8.0, 8.0], [0.0, 8.0], [0.0, 0.0]], [1, 2, 2, 2, 79], id='frame0', capstyle='butt')
        c.path([[10.0, 8.0], [12.0, 8.0], [10.0, 4.0], [10.0, 8.0]], [1, 2, 2, 79], id='color1', zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), linewidth=0.0, capstyle='butt')
        c.path([[10.0, 8.0], [12.0, 8.0], [10.0, 4.0], [10.0, 8.0]], [1, 2, 2, 79], id='color1', capstyle='butt', fill=False)
        for object_id, points in [('line1_0', [[14.0, 0.0], [14.0, 8.0]]), ('line1_1', [[14.0, 4.0], [18.0, 4.0]]), ('line1_2', [[10.0, 0.0], [14.0, 8.0]]), ('line1_3', [[10.0, 4.0], [12.0, 8.0]]), ('line1_4', [[14.0, 8.0], [18.0, 4.0]]), ('line1_5', [[16.0, 6.0], [16.0, 8.0]]), ('line1_6', [[17.0, 6.0], [17.0, 8.0]]), ('line1_7', [[16.0, 6.0], [18.0, 6.0]]), ('line1_8', [[16.0, 7.0], [18.0, 7.0]])]:
            c.line(points, id=object_id)
        c.path([[10.0, 0.0], [18.0, 0.0], [18.0, 8.0], [10.0, 8.0], [10.0, 0.0]], [1, 2, 2, 2, 79], id='frame1', capstyle='butt')
        c.path([[20.0, 0.0], [24.0, 0.0], [24.0, 8.0], [20.0, 0.0]], [1, 2, 2, 79], id='color2', zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), linewidth=0.0, capstyle='butt')
        c.path([[20.0, 0.0], [24.0, 0.0], [24.0, 8.0], [20.0, 0.0]], [1, 2, 2, 79], id='color2', capstyle='butt', fill=False, **_kw.get(9, {}))
        _ov = {j: s for idxs, s in _hi.get(10, ()) for j in idxs}
        for i, (object_id, points) in enumerate([('line2_0', [[24.0, 0.0], [24.0, 8.0]]), ('line2_1', [[24.0, 4.0], [28.0, 4.0]]), ('line2_2', [[20.0, 0.0], [24.0, 8.0]]), ('line2_3', [[20.0, 4.0], [22.0, 8.0]]), ('line2_4', [[24.0, 8.0], [28.0, 4.0]]), ('line2_5', [[26.0, 6.0], [26.0, 8.0]]), ('line2_6', [[27.0, 6.0], [27.0, 8.0]]), ('line2_7', [[26.0, 6.0], [28.0, 6.0]]), ('line2_8', [[26.0, 7.0], [28.0, 7.0]])]):
            c.line(points, id=object_id, **_ov[i]) if i in _ov else c.line(points, id=object_id)
        c.path([[20.0, 0.0], [28.0, 0.0], [28.0, 8.0], [20.0, 8.0], [20.0, 0.0]], [1, 2, 2, 2, 79], id='frame2', capstyle='butt')
        c.path([[34.0, 4.0], [38.0, 4.0], [34.0, 8.0], [34.0, 4.0]], [1, 2, 2, 79], id='color3', zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), linewidth=0.0, capstyle='butt')
        c.path([[34.0, 4.0], [38.0, 4.0], [34.0, 8.0], [34.0, 4.0]], [1, 2, 2, 79], id='color3', capstyle='butt', fill=False)
        for object_id, points in [('line3_0', [[34.0, 0.0], [34.0, 8.0]]), ('line3_1', [[34.0, 4.0], [38.0, 4.0]]), ('line3_2', [[30.0, 0.0], [34.0, 8.0]]), ('line3_3', [[30.0, 4.0], [32.0, 8.0]]), ('line3_4', [[34.0, 8.0], [38.0, 4.0]]), ('line3_5', [[36.0, 6.0], [36.0, 8.0]]), ('line3_6', [[37.0, 6.0], [37.0, 8.0]]), ('line3_7', [[36.0, 6.0], [38.0, 6.0]]), ('line3_8', [[36.0, 7.0], [38.0, 7.0]])]:
            c.line(points, id=object_id)
        c.path([[30.0, 0.0], [38.0, 0.0], [38.0, 8.0], [30.0, 8.0], [30.0, 0.0]], [1, 2, 2, 2, 79], id='frame3', capstyle='butt')
        c.path([[44.0, 0.0], [48.0, 0.0], [48.0, 4.0], [44.0, 4.0], [44.0, 0.0]], [1, 2, 2, 2, 79], id='color4', zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), linewidth=0.0, capstyle='butt')
        c.path([[44.0, 0.0], [48.0, 0.0], [48.0, 4.0], [44.0, 4.0], [44.0, 0.0]], [1, 2, 2, 2, 79], id='color4', capstyle='butt', fill=False)
        for object_id, points in [('line4_0', [[44.0, 0.0], [44.0, 8.0]]), ('line4_1', [[44.0, 4.0], [48.0, 4.0]]), ('line4_2', [[40.0, 0.0], [44.0, 8.0]]), ('line4_3', [[40.0, 4.0], [42.0, 8.0]]), ('line4_4', [[44.0, 8.0], [48.0, 4.0]]), ('line4_5', [[46.0, 6.0], [46.0, 8.0]]), ('line4_6', [[47.0, 6.0], [47.0, 8.0]]), ('line4_7', [[46.0, 6.0], [48.0, 6.0]]), ('line4_8', [[46.0, 7.0], [48.0, 7.0]])]:
            c.line(points, id=object_id)
        c.path([[40.0, 0.0], [48.0, 0.0], [48.0, 8.0], [40.0, 8.0], [40.0, 0.0]], [1, 2, 2, 2, 79], id='frame4', capstyle='butt')
        for object_id, text, anchor in [('label0', '(A)', (0.5, 9.0)), ('label1', '(B)', (10.5, 9.0)), ('label2', '(C)', (20.5, 9.0)), ('label3', '(D)', (30.5, 9.0)), ('label4', '(E)', (40.5, 9.0))]:
            c.text(text, anchor, id=object_id)

    def draw(self, output_path=None, *, variant=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / (self.__class__.__name__ + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if variant not in self.variants:
                raise ValueError('Unknown Special variant: ' + str(variant))
            return getattr(self, 'draw_' + variant)(output_path)
        with Canvas(PLANE, xlim=(-1.6797080275161065, 49.298033537879654), ylim=(-20.699544585588708, 30.278196979807053)) as c:
            self._draw_base(c)
            return c.save(output_path)

    def draw_C01(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane305_C01.png'
        with Canvas(PLANE, xlim=(-1.6797080275161065, 49.298033537879654), ylim=(-20.699544585588708, 30.278196979807053)) as c:
            self._draw_base(c)
            c.line([[48, 4], [44, 0]], zorder=9, color='#DC2626', solid_capstyle='butt')
            return c.save(output_path)

    def draw_C02(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane305_C02.png'
        with Canvas(PLANE, xlim=(-1.6797080275161065, 49.298033537879654), ylim=(-20.699544585588708, 30.278196979807053)) as c:
            self._draw_base(c, kw={1: {'edgecolor': '#DC2626', 'linewidth': 2.0}})
            return c.save(output_path)

    def draw_C03(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane305_C03.png'
        with Canvas(PLANE, xlim=(-1.6797080275161065, 49.298033537879654), ylim=(-20.699544585588708, 30.278196979807053)) as c:
            self._draw_base(c, hi={10: [({2}, {'color': '#EA580C', 'linewidth': 2.0})]})
            return c.save(output_path)

    def draw_C04(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane305_C04.png'
        with Canvas(PLANE, xlim=(-1.6797080275161065, 49.298033537879654), ylim=(-20.699544585588708, 30.278196979807053)) as c:
            self._draw_base(c, hi={10: [({2}, {'color': '#DC2626', 'linewidth': 2.0})]}, kw={9: {'edgecolor': '#DC2626', 'linewidth': 2.0}})
            return c.save(output_path)
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Plane305')
    parser.add_argument('output', nargs='?')
    parser.add_argument('--variant', choices=('C01', 'C02', 'C03', 'C04'))
    args = parser.parse_args()
    print(Plane305().draw(args.output, variant=args.variant))
