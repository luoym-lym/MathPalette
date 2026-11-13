"""Collected question Ana90; construction on the shared drawing protocol."""
from pathlib import Path
import sys
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from MathPalette_Dataset.drawing import Canvas, ANALYTICS

class Ana90:
    variants = ('C01', 'C02')

    def _draw_base(self, c):
        segs = [(0, 1, lambda x: 2 * x ** 3 - 3 * x ** 2), (1, 2, lambda x: -2 * x ** 3 + 10 * x ** 2 - 14 * x + 5), (2, 3, lambda x: -x ** 3 + 7 * x ** 2 - 14 * x + 9), (3, 5, lambda x: -0.25 * x ** 2 + 2.5 * x - 2.25), (5, 6, lambda x: -2 * x ** 2 + 20 * x - 46)]
        c.line(np.vstack([np.column_stack(((x := np.linspace(a, b, 301)), fn(x))) for a, b, fn in segs]), id='object_000', solid_capstyle='butt')

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
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Ana90_C01.png'
        with Canvas(ANALYTICS) as c:
            self._draw_base(c)
            c.line([[1, 1], [3, 4]], zorder=9, color='#2563EB', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            c.point([[1.0, 1.0]], zorder=10, s=50, facecolors='#DC2626', edgecolors='#DC2626')
            c.point([[3.0, 4.0]], zorder=10, s=50, facecolors='#DC2626', edgecolors='#DC2626')
            return c.save(output_path)

    def draw_C02(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Ana90_C02.png'
        with Canvas(ANALYTICS) as c:
            self._draw_base(c)
            c.line([[1, -1], [3, 4]], zorder=9, color='#2563EB', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            c.point([[3.0, 4.0]], zorder=10, s=50, facecolors='#DC2626', edgecolors='#DC2626')
            c.point([[1.0, -1.0]], zorder=10, s=50, facecolors='#DC2626', edgecolors='#DC2626')
            return c.save(output_path)

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Ana90')
    parser.add_argument('output', nargs='?')
    parser.add_argument('--variant', choices=('C01', 'C02'))
    args = parser.parse_args()
    print(Ana90().draw(args.output, variant=args.variant))
