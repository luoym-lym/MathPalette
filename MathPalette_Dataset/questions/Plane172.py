"""Collected question Plane172; construction on the shared drawing protocol."""
from pathlib import Path
import sys
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from MathPalette_Dataset.drawing import Canvas, PLANE

class Plane172:
    variants = ('C01', 'C02', 'C03')

    def _draw_base(self, c, kw=None):
        _kw = kw or {}
        c.path([[0.0, 6.0], [0.0, 10.0], [2.0, 8.0], [0.0, 6.0]], [1, 2, 2, 79], id='squarepiece0', alpha=1, edgecolor='none', linewidth=0.0, capstyle='butt')
        c.path([[0.0, 6.0], [0.0, 10.0], [2.0, 8.0], [0.0, 6.0]], [1, 2, 2, 79], id='squarepiece0', capstyle='butt', fill=False)
        c.path([[0.0, 6.0], [4.0, 6.0], [2.0, 8.0], [0.0, 6.0]], [1, 2, 2, 79], id='squarepiece1', alpha=1, edgecolor='none', linewidth=0.0, capstyle='butt')
        c.path([[0.0, 6.0], [4.0, 6.0], [2.0, 8.0], [0.0, 6.0]], [1, 2, 2, 79], id='squarepiece1', capstyle='butt', fill=False)
        c.path([[2.0, 10.0], [4.0, 10.0], [4.0, 8.0], [2.0, 10.0]], [1, 2, 2, 79], id='squarepiece2', alpha=1, edgecolor='none', linewidth=0.0, capstyle='butt')
        c.path([[2.0, 10.0], [4.0, 10.0], [4.0, 8.0], [2.0, 10.0]], [1, 2, 2, 79], id='squarepiece2', capstyle='butt', fill=False)
        c.path([[1.0, 9.0], [3.0, 9.0], [2.0, 8.0], [1.0, 9.0]], [1, 2, 2, 79], id='squarepiece3', alpha=1, edgecolor='none', linewidth=0.0, capstyle='butt')
        c.path([[1.0, 9.0], [3.0, 9.0], [2.0, 8.0], [1.0, 9.0]], [1, 2, 2, 79], id='squarepiece3', capstyle='butt', fill=False)
        c.path([[3.0, 7.0], [4.0, 8.0], [4.0, 6.0], [3.0, 7.0]], [1, 2, 2, 79], id='squarepiece4', alpha=1, edgecolor='none', linewidth=0.0, capstyle='butt')
        c.path([[3.0, 7.0], [4.0, 8.0], [4.0, 6.0], [3.0, 7.0]], [1, 2, 2, 79], id='squarepiece4', capstyle='butt', fill=False)
        c.path([[2.0, 8.0], [3.0, 9.0], [4.0, 8.0], [3.0, 7.0], [2.0, 8.0]], [1, 2, 2, 2, 79], id='squarepiece5', alpha=1, edgecolor='none', linewidth=0.0, capstyle='butt')
        c.path([[2.0, 8.0], [3.0, 9.0], [4.0, 8.0], [3.0, 7.0], [2.0, 8.0]], [1, 2, 2, 2, 79], id='squarepiece5', capstyle='butt', fill=False)
        c.path([[0.0, 10.0], [2.0, 10.0], [3.0, 9.0], [1.0, 9.0], [0.0, 10.0]], [1, 2, 2, 2, 79], id='squarepiece6', alpha=1, edgecolor='none', linewidth=0.0, capstyle='butt')
        c.path([[0.0, 10.0], [2.0, 10.0], [3.0, 9.0], [1.0, 9.0], [0.0, 10.0]], [1, 2, 2, 2, 79], id='squarepiece6', capstyle='butt', fill=False)
        c.path([[7.585786437626905, 10.121320343559642], [9.0, 10.121320343559642], [9.0, 11.535533905932738], [7.585786437626905, 10.121320343559642]], [1, 2, 2, 79], id='kangaroopiece0', alpha=1, edgecolor='none', linewidth=0.0, capstyle='butt')
        c.path([[7.585786437626905, 10.121320343559642], [9.0, 10.121320343559642], [9.0, 11.535533905932738], [7.585786437626905, 10.121320343559642]], [1, 2, 2, 79], id='kangaroopiece0', capstyle='butt', fill=False)
        c.path([[9.0, 8.0], [9.0, 10.82842712474619], [11.82842712474619, 8.0], [9.0, 8.0]], [1, 2, 2, 79], id='kangaroopiece1', alpha=1, edgecolor='none', linewidth=0.0, capstyle='butt')
        c.path([[9.0, 8.0], [9.0, 10.82842712474619], [11.82842712474619, 8.0], [9.0, 8.0]], [1, 2, 2, 79], id='kangaroopiece1', capstyle='butt', fill=False)
        c.path([[8.0, 8.0], [9.0, 9.0], [9.0, 7.0], [8.0, 8.0]], [1, 2, 2, 79], id='kangaroopiece2', alpha=1, edgecolor='none', linewidth=0.0, capstyle='butt')
        c.path([[8.0, 8.0], [9.0, 9.0], [9.0, 7.0], [8.0, 8.0]], [1, 2, 2, 79], id='kangaroopiece2', capstyle='butt', fill=False, **_kw.get(19, {}))
        c.path([[9.707106781186548, 8.0], [12.535533905932738, 8.0], [12.535533905932738, 5.17157287525381], [9.707106781186548, 8.0]], [1, 2, 2, 79], id='kangaroopiece3', alpha=1, edgecolor='none', linewidth=0.0, capstyle='butt')
        c.path([[9.707106781186548, 8.0], [12.535533905932738, 8.0], [12.535533905932738, 5.17157287525381], [9.707106781186548, 8.0]], [1, 2, 2, 79], id='kangaroopiece3', capstyle='butt', fill=False)
        c.path([[10.535533905932738, 5.17157287525381], [11.535533905932738, 6.17157287525381], [12.535533905932738, 5.17157287525381], [11.535533905932738, 4.17157287525381], [10.535533905932738, 5.17157287525381]], [1, 2, 2, 2, 79], id='kangaroopiece4', alpha=1, edgecolor='none', linewidth=0.0, capstyle='butt')
        c.path([[10.535533905932738, 5.17157287525381], [11.535533905932738, 6.17157287525381], [12.535533905932738, 5.17157287525381], [11.535533905932738, 4.17157287525381], [10.535533905932738, 5.17157287525381]], [1, 2, 2, 2, 79], id='kangaroopiece4', capstyle='butt', fill=False)
        c.path([[11.121320343559642, 3.7573593128807143], [13.949747468305834, 3.7573593128807143], [12.535533905932738, 5.17157287525381], [11.121320343559642, 3.7573593128807143]], [1, 2, 2, 79], id='kangaroopiece5', alpha=1, edgecolor='none', linewidth=0.0, capstyle='butt')
        c.path([[11.121320343559642, 3.7573593128807143], [13.949747468305834, 3.7573593128807143], [12.535533905932738, 5.17157287525381], [11.121320343559642, 3.7573593128807143]], [1, 2, 2, 79], id='kangaroopiece5', capstyle='butt', fill=False)
        c.path([[5.4, 7.9], [5.75, 7.9], [5.75, 7.75], [6.5, 8.0], [5.75, 8.25], [5.75, 8.1], [5.4, 8.1], [5.4, 7.9]], [1, 2, 2, 2, 2, 2, 2, 79], id='rearrangement_arrow', edgecolor='none', facecolor='black', linewidth=0.0, capstyle='butt')
        c.path([[5.4, 7.9], [5.75, 7.9], [5.75, 7.75], [6.5, 8.0], [5.75, 8.25], [5.75, 8.1], [5.4, 8.1], [5.4, 7.9]], [1, 2, 2, 2, 2, 2, 2, 79], id='rearrangement_arrow', capstyle='butt', fill=False)
        c.path([[0.0, 1.0], [2.0, 1.0], [3.0, 0.0], [1.0, 0.0], [0.0, 1.0]], [1, 2, 2, 2, 79], id='option0', alpha=1, edgecolor='none', linewidth=0.0, capstyle='butt')
        c.path([[0.0, 1.0], [2.0, 1.0], [3.0, 0.0], [1.0, 0.0], [0.0, 1.0]], [1, 2, 2, 2, 79], id='option0', capstyle='butt', fill=False)
        c.path([[4.0, 1.0], [6.0, 1.0], [5.0, 0.0], [4.0, 1.0]], [1, 2, 2, 79], id='option1', alpha=1, edgecolor='none', linewidth=0.0, capstyle='butt')
        c.path([[4.0, 1.0], [6.0, 1.0], [5.0, 0.0], [4.0, 1.0]], [1, 2, 2, 79], id='option1', capstyle='butt', fill=False)
        c.path([[8.0, 1.0], [9.0, 2.0], [10.0, 1.0], [9.0, 0.0], [8.0, 1.0]], [1, 2, 2, 2, 79], id='option2', alpha=1, edgecolor='none', linewidth=0.0, capstyle='butt')
        c.path([[8.0, 1.0], [9.0, 2.0], [10.0, 1.0], [9.0, 0.0], [8.0, 1.0]], [1, 2, 2, 2, 79], id='option2', capstyle='butt', fill=False)
        c.path([[12.0, 1.0], [13.0, 2.0], [13.0, 0.0], [12.0, 1.0]], [1, 2, 2, 79], id='option3', alpha=1, edgecolor='none', linewidth=0.0, capstyle='butt')
        c.path([[12.0, 1.0], [13.0, 2.0], [13.0, 0.0], [12.0, 1.0]], [1, 2, 2, 79], id='option3', capstyle='butt', fill=False)
        c.path([[16.0, 2.0], [18.0, 2.0], [18.0, 0.0], [16.0, 2.0]], [1, 2, 2, 79], id='option4', alpha=1, edgecolor='none', linewidth=0.0, capstyle='butt')
        c.path([[16.0, 2.0], [18.0, 2.0], [18.0, 0.0], [16.0, 2.0]], [1, 2, 2, 79], id='option4', capstyle='butt', fill=False)
        for object_id, text, anchor in [('label0', '(A)', (-0.6, -0.3)), ('label1', '(B)', (3.4, -0.3)), ('label2', '(C)', (7.4, -0.3)), ('label3', '(D)', (11.4, -0.3)), ('label4', '(E)', (15.4, -0.3))]:
            c.text(text, anchor, id=object_id)

    def draw(self, output_path=None, *, variant=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / (self.__class__.__name__ + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if variant not in self.variants:
                raise ValueError('Unknown Special variant: ' + str(variant))
            return getattr(self, 'draw_' + variant)(output_path)
        with Canvas(PLANE, xlim=(-1.4521597015863072, 18.485111318252773), ylim=(-4.462575492302271, 15.47469552753681)) as c:
            self._draw_base(c)
            return c.save(output_path)

    def draw_C01(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane172_C01.png'
        with Canvas(PLANE, xlim=(-1.4521597015863072, 18.485111318252773), ylim=(-4.462575492302271, 15.47469552753681)) as c:
            self._draw_base(c)
            for object_id, points in [(None, [[8.53683658347604, 7.990074585040029], [12.568270061752326, 0.8434425099138885]]), (None, [[12.425744635752658, 4.223331183620267], [1.5327299343495668, 0.5583916579145551]]), (None, [[8.57755813376166, 10.51481070274841], [4.994061708627186, 0.5991132082001744]]), (None, [[12.161054558896135, 6.992396603042362], [17.59738152202628, 1.3524618884841253]])]:
                c.line(points, id=object_id, zorder=9, color='#EA580C', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            return c.save(output_path)

    def draw_C02(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane172_C02.png'
        with Canvas(PLANE, xlim=(-1.4521597015863072, 18.485111318252773), ylim=(-4.462575492302271, 15.47469552753681)) as c:
            self._draw_base(c)
            for object_id, points in [(None, [[8.0, 8.0]]), (None, [[9.0, 9.0]]), (None, [[9.0, 7.0]])]:
                c.point(points, id=object_id, zorder=10, s=50, facecolors='#DC2626', edgecolors='#DC2626')
            return c.save(output_path)

    def draw_C03(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane172_C03.png'
        with Canvas(PLANE, xlim=(-1.4521597015863072, 18.485111318252773), ylim=(-4.462575492302271, 15.47469552753681)) as c:
            self._draw_base(c, kw={19: {'edgecolor': '#DC2626', 'linewidth': 1.5}})
            return c.save(output_path)
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Plane172')
    parser.add_argument('output', nargs='?')
    parser.add_argument('--variant', choices=('C01', 'C02', 'C03'))
    args = parser.parse_args()
    print(Plane172().draw(args.output, variant=args.variant))
