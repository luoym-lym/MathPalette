"""Collected question Ana02; construction on the shared drawing protocol."""
from pathlib import Path
import sys
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from MathPalette_Dataset.drawing import Canvas, ANALYTICS

class Ana02:
    variants = ('C01', 'C02', 'C03')

    def _draw_base(self, c):
        x = np.linspace(-8, 8, 200)
        c.line(np.column_stack((x, 1.9 * x ** 3 + 1.5 * x ** 2 - 0.4)), id='curve_001', solid_capstyle='butt')

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
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Ana02_C01.png'
        with Canvas(ANALYTICS) as c:
            self._draw_base(c)
            c.point([[-1.0, 2.0]], zorder=10, s=50, facecolors='#DC2626', edgecolors='#DC2626')
            c.point([[1.0, 1.0]], zorder=10, s=50, facecolors='#DC2626', edgecolors='#DC2626')
            return c.save(output_path)

    def draw_C02(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Ana02_C02.png'
        with Canvas(ANALYTICS) as c:
            self._draw_base(c)
            c.point([[-1.0, 1.0]], zorder=10, s=50, facecolors='#DC2626', edgecolors='#DC2626')
            c.point([[1.0, 0.0]], zorder=10, s=50, facecolors='#DC2626', edgecolors='#DC2626')
            return c.save(output_path)

    def draw_C03(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Ana02_C03.png'
        with Canvas(ANALYTICS) as c:
            self._draw_base(c)
            c.point([[-0.951471, -0.767647]], zorder=10, s=50, facecolors='#DC2626', edgecolors='#DC2626')
            c.point([[1.0, -1.0]], zorder=10, s=50, facecolors='#DC2626', edgecolors='#DC2626')
            return c.save(output_path)

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Ana02')
    parser.add_argument('output', nargs='?')
    parser.add_argument('--variant', choices=('C01', 'C02', 'C03'))
    args = parser.parse_args()
    print(Ana02().draw(args.output, variant=args.variant))
