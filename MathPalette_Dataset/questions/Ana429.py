"""Collected question Ana429; construction on the shared drawing protocol."""
from pathlib import Path
import sys
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from MathPalette_Dataset.drawing import Canvas, ANALYTICS

class Ana429:
    variants = ('C01', 'C02', 'C03', 'C04')

    def _draw_base(self, c):
        t = np.linspace(0, 2 * np.pi, 1601)
        c.line(np.column_stack((5 * np.cos(t), 3 * np.sin(t))), id='object_000', solid_capstyle='butt')
        c.point([[1, 1]], id='object_001')
        c.text('M', [1.22, 1.26], ha='left', va='bottom')

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
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Ana429_C01.png'
        with Canvas(ANALYTICS) as c:
            self._draw_base(c)
            c.point([[-2.0, 4.0]], zorder=10, s=50, facecolors='#DC2626', edgecolors='#DC2626')
            c.point([[4.0, -2.0]], zorder=10, s=50, facecolors='#DC2626', edgecolors='#DC2626')
            c.line([[-2, 4], [4, -2]], zorder=9, color='#2563EB', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            return c.save(output_path)

    def draw_C02(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Ana429_C02.png'
        with Canvas(ANALYTICS) as c:
            self._draw_base(c)
            c.point([[-1.0, -1.0]], zorder=10, s=50, facecolors='#DC2626', edgecolors='#DC2626')
            c.point([[3.0, 3.0]], zorder=10, s=50, facecolors='#DC2626', edgecolors='#DC2626')
            c.line([[-1, -1], [3, 3]], zorder=9, color='#2563EB', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            return c.save(output_path)

    def draw_C03(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Ana429_C03.png'
        with Canvas(ANALYTICS) as c:
            self._draw_base(c)
            c.line([[-3, 2], [5, 0]], zorder=9, color='#2563EB', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            c.point([[-3.0, 2.0]], zorder=10, s=50, facecolors='#DC2626', edgecolors='#DC2626')
            c.point([[5.0, 0.0]], zorder=10, s=50, facecolors='#DC2626', edgecolors='#DC2626')
            return c.save(output_path)

    def draw_C04(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Ana429_C04.png'
        with Canvas(ANALYTICS) as c:
            self._draw_base(c)
            c.line([[5, 1], [-3, 1]], zorder=9, color='#2563EB', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            c.point([[-3.0, 1.0]], zorder=10, s=50, facecolors='#DC2626', edgecolors='#DC2626')
            c.point([[5.0, 1.0]], zorder=10, s=50, facecolors='#DC2626', edgecolors='#DC2626')
            return c.save(output_path)

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Ana429')
    parser.add_argument('output', nargs='?')
    parser.add_argument('--variant', choices=('C01', 'C02', 'C03', 'C04'))
    args = parser.parse_args()
    print(Ana429().draw(args.output, variant=args.variant))
