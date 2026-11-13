"""Collected question Ana20; construction on the shared drawing protocol."""
from pathlib import Path
import sys
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from MathPalette_Dataset.drawing import Canvas, ANALYTICS

class Ana20:
    variants = ('C01', 'C02', 'C03', 'C04')

    def _draw_base(self, c):
        x = np.linspace(-6, 4, 300)
        c.line(np.column_stack((x, 0.5 * (x + 4) * (x - 2))), id='curve_001', solid_capstyle='butt')

    def draw(self, output_path=None, *, variant=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / (self.__class__.__name__ + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if variant not in self.variants:
                raise ValueError('Unknown Special variant: ' + str(variant))
            return getattr(self, 'draw_' + variant)(output_path)
        with Canvas(ANALYTICS) as c:
            self._draw_base(c)
            return c.save(output_path)

    def draw_C01(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Ana20_C01.png'
        with Canvas(ANALYTICS) as c:
            self._draw_base(c)
            c.point([[-4.0, 0.0]], zorder=10, s=50, facecolors='#DC2626', edgecolors='#DC2626')
            c.point([[3.0, 0.0]], zorder=10, s=50, facecolors='#DC2626', edgecolors='#DC2626')
            return c.save(output_path)

    def draw_C02(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Ana20_C02.png'
        with Canvas(ANALYTICS) as c:
            self._draw_base(c)
            c.point([[-4.0, 0.0]], zorder=10, s=50, facecolors='#DC2626', edgecolors='#DC2626')
            c.point([[1.0, 0.0]], zorder=10, s=50, facecolors='#DC2626', edgecolors='#DC2626')
            return c.save(output_path)

    def draw_C03(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Ana20_C03.png'
        with Canvas(ANALYTICS) as c:
            self._draw_base(c)
            c.point([[-4.0, 0.0]], zorder=10, s=50, facecolors='#DC2626', edgecolors='#DC2626')
            return c.save(output_path)

    def draw_C04(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Ana20_C04.png'
        with Canvas(ANALYTICS) as c:
            self._draw_base(c)
            c.line([[-8, 1], [8, 1]], zorder=9, color='#2563EB', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            c.point([[2.320588, 0.997059]], zorder=10, s=50, facecolors='#DC2626', edgecolors='#DC2626')
            c.point([[-4.333824, 0.923529]], zorder=10, s=50, facecolors='#DC2626', edgecolors='#DC2626')
            return c.save(output_path)

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Ana20')
    parser.add_argument('output', nargs='?')
    parser.add_argument('--variant', choices=('C01', 'C02', 'C03', 'C04'))
    args = parser.parse_args()
    print(Ana20().draw(args.output, variant=args.variant))
