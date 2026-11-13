"""Collected question Plane575; construction on the shared drawing protocol."""
from pathlib import Path
import sys
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from MathPalette_Dataset.drawing import Canvas, PLANE

class Plane575:
    variants = ('C01', 'C02', 'C03', 'C04', 'C05', 'C06')

    @staticmethod
    def _grid(c, pfx, xs, ys, mask):
        n = len(xs) - 1
        codes = [1, 2, 2, 2, 79]
        for r in range(n):
            for col in range(n):
                x0, x1, y0, y1 = (xs[col], xs[col + 1], ys[r], ys[r + 1])
                fc = '#DADADA' if mask[r * n + col] == '#' else 'white'
                c.path([[x0, y0], [x1, y0], [x1, y1], [x0, y1], [x0, y0]], codes, id=f'{pfx}_cell_r{r + 1}_c{col + 1}', zorder=1, edgecolor='none', facecolor=fc, linewidth=0.0, capstyle='butt')
        for r in range(n + 1):
            for col in range(n):
                c.line([[xs[col], ys[r]], [xs[col + 1], ys[r]]], id=f'{pfx}_horizontal_r{r}_c{col}', solid_capstyle='butt')
        for r in range(n):
            for col in range(n + 1):
                c.line([[xs[col], ys[r]], [xs[col], ys[r + 1]]], id=f'{pfx}_vertical_r{r}_c{col}', solid_capstyle='butt')

    def _draw_base(self, c):
        _ys = [45.43831018518518, 40.771643518518516, 36.10497685185185, 31.438310185185188]
        self._grid(c, 'upper', [43.0, 47.666666666666664, 52.333333333333336, 57.0], [73.43831018518519, 68.77164351851852, 64.10497685185186, 59.43831018518518], '##..#..#.')
        self._grid(c, 'A', [2.25, 6.916666666666667, 11.583333333333334, 16.25], _ys, '##..#..#.')
        self._grid(c, 'B', [22.625, 27.291666666666668, 31.958333333333336, 36.625], _ys, '...####..')
        self._grid(c, 'C', [43.0, 47.666666666666664, 52.333333333333336, 57.0], _ys, '..####...')
        self._grid(c, 'D', [63.375, 68.04166666666667, 72.70833333333333, 77.375], _ys, '.##.#..#.')
        self._grid(c, 'E', [83.75, 88.41666666666667, 93.08333333333333, 97.75], _ys, '.#.###...')
        c.text('(A)', (9.25, 27.638310185185187), id='label_A', zorder=3)
        c.text('(B)', (29.625, 27.638310185185187), id='label_B', zorder=3)
        c.text('(C)', (50.0, 27.638310185185187), id='label_C', zorder=3)
        c.text('(D)', (70.375, 27.638310185185187), id='label_D', zorder=3)
        c.text('(E)', (90.75, 27.638310185185187), id='label_E', zorder=3)

    def draw(self, output_path=None, *, variant=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / (self.__class__.__name__ + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if variant not in self.variants:
                raise ValueError('Unknown Special variant: ' + str(variant))
            return getattr(self, 'draw_' + variant)(output_path)
        with Canvas(PLANE, xlim=(0.0, 100.0), ylim=(0.0, 100.0)) as c:
            self._draw_base(c)
            return c.save(output_path)

    def draw_C01(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane575_C01.png'
        with Canvas(PLANE, xlim=(0.0, 100.0), ylim=(0.0, 100.0)) as c:
            self._draw_base(c)
            c.line([[43.0, 73.43831018518519], [43.0, 59.43831018518518]], zorder=9, color='#2563EB', solid_capstyle='butt')
            c.line([[43.0, 59.43831018518518], [57.0, 59.43831018518518]], zorder=9, color='#DC2626', solid_capstyle='butt')
            c.line([[22.625, 31.438310185185188], [36.625, 31.438310185185188]], zorder=9, color='#2563EB', solid_capstyle='butt')
            c.line([[36.625, 31.438310185185188], [36.625, 45.43831018518518]], zorder=9, color='#DC2626', solid_capstyle='butt')
            return c.save(output_path)

    def draw_C02(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane575_C02.png'
        with Canvas(PLANE, xlim=(0.0, 100.0), ylim=(0.0, 100.0)) as c:
            self._draw_base(c)
            c.line([[43.0, 73.43831018518519], [43.0, 59.43831018518518]], zorder=9, color='#16A34A', solid_capstyle='butt')
            c.line([[43.0, 59.43831018518518], [57.0, 59.43831018518518]], zorder=9, color='#EA580C', solid_capstyle='butt')
            c.line([[22.625, 31.438310185185188], [36.625, 31.438310185185188]], zorder=9, color='#16A34A', solid_capstyle='butt')
            c.line([[36.625, 31.438310185185188], [36.625, 45.43831018518518]], zorder=9, color='#EA580C', solid_capstyle='butt')
            return c.save(output_path)

    def draw_C03(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane575_C03.png'
        with Canvas(PLANE, xlim=(0.0, 100.0), ylim=(0.0, 100.0)) as c:
            self._draw_base(c)
            c.line([[43.0, 73.43831018518519], [43.0, 59.43831018518518]], zorder=9, color='#16A34A', solid_capstyle='butt')
            c.line([[43.0, 59.43831018518518], [57.0, 59.43831018518518]], zorder=9, color='#EA580C', solid_capstyle='butt')
            c.line([[22.625, 31.438310185185188], [36.625, 31.438310185185188]], zorder=9, color='#16A34A', solid_capstyle='butt')
            return c.save(output_path)

    def draw_C04(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane575_C04.png'
        with Canvas(PLANE, xlim=(0.0, 100.0), ylim=(0.0, 100.0)) as c:
            self._draw_base(c)
            c.line([[43.0, 73.43831018518519], [43.0, 59.43831018518518]], zorder=9, color='#16A34A', solid_capstyle='butt')
            c.line([[43.0, 59.43831018518518], [57.0, 59.43831018518518]], zorder=9, color='#EA580C', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            c.line([[22.625, 31.438310185185188], [36.625, 31.438310185185188]], zorder=9, color='#16A34A', solid_capstyle='butt')
            c.line([[36.625, 31.438310185185188], [36.625, 45.43831018518518]], zorder=9, color='#EA580C', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            return c.save(output_path)

    def draw_C05(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane575_C05.png'
        with Canvas(PLANE, xlim=(0.0, 100.0), ylim=(0.0, 100.0)) as c:
            self._draw_base(c)
            c.line([[43.0, 73.43831018518519], [43.0, 59.43831018518518]], zorder=9, color='#16A34A', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            c.line([[43.0, 59.43831018518518], [57.0, 59.43831018518518]], zorder=9, color='#EA580C', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            c.line([[22.625, 31.438310185185188], [36.625, 31.438310185185188]], zorder=9, color='#16A34A', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            c.line([[36.625, 31.438310185185188], [36.625, 45.43831018518518]], zorder=9, color='#EA580C', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            c.point([[43.0, 59.43831018518518]], zorder=10, s=50, facecolors='#16A34A', edgecolors='#16A34A')
            c.point([[36.625, 31.438310185185188]], zorder=10, s=50, facecolors='#16A34A', edgecolors='#16A34A')
            return c.save(output_path)

    def draw_C06(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane575_C06.png'
        with Canvas(PLANE, xlim=(0.0, 100.0), ylim=(0.0, 100.0)) as c:
            self._draw_base(c)
            c.line([[43.0, 73.43831018518519], [43.0, 59.43831018518518]], zorder=9, color='#DC2626', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            c.line([[43.0, 59.43831018518518], [57.0, 59.43831018518518]], zorder=9, color='#2563EB', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            c.line([[22.625, 31.438310185185188], [36.625, 31.438310185185188]], zorder=9, color='#DC2626', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            c.line([[36.625, 31.438310185185188], [36.625, 45.43831018518518]], zorder=9, color='#2563EB', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            return c.save(output_path)
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Plane575')
    parser.add_argument('output', nargs='?')
    parser.add_argument('--variant', choices=('C01', 'C02', 'C03', 'C04', 'C05', 'C06'))
    args = parser.parse_args()
    print(Plane575().draw(args.output, variant=args.variant))
