"""Collected question Ana13; construction on the shared drawing protocol."""
from pathlib import Path
import sys
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from MathPalette_Dataset.drawing import Canvas, ANALYTICS

class Ana13:
    variants = ('C01', 'C02', 'C03', 'C04', 'C05')

    def _draw_base(self, c):
        x1 = np.linspace(-8, 2.65, 200)
        c.line(np.column_stack((x1, 2.0 / (x1 - 3.0) + 1.0)), id='curve_001', solid_capstyle='butt')
        x2 = np.linspace(3.35, 8, 200)
        c.line(np.column_stack((x2, 2.0 / (x2 - 3.0) + 1.0)), id='curve_002', solid_capstyle='butt')

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
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Ana13_C01.png'
        with Canvas(ANALYTICS) as c:
            self._draw_base(c)
            c.line([[2, 8], [2, -8]], zorder=9, color='#2563EB', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            return c.save(output_path)

    def draw_C02(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Ana13_C02.png'
        with Canvas(ANALYTICS) as c:
            self._draw_base(c)
            c.line([[4, 8], [4, -8]], zorder=9, color='#2563EB', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            return c.save(output_path)

    def draw_C03(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Ana13_C03.png'
        with Canvas(ANALYTICS) as c:
            self._draw_base(c)
            c.line([[2, 8], [4, -8]], zorder=9, color='#2563EB', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            return c.save(output_path)

    def draw_C04(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Ana13_C04.png'
        with Canvas(ANALYTICS) as c:
            self._draw_base(c)
            c.point([[2.0, -5.0]], zorder=10, s=50, facecolors='#DC2626', edgecolors='#DC2626')
            return c.save(output_path)

    def draw_C05(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Ana13_C05.png'
        with Canvas(ANALYTICS) as c:
            self._draw_base(c)
            c.point([[4.0, 7.0]], zorder=10, s=50, facecolors='#DC2626', edgecolors='#DC2626')
            return c.save(output_path)

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Ana13')
    parser.add_argument('output', nargs='?')
    parser.add_argument('--variant', choices=('C01', 'C02', 'C03', 'C04', 'C05'))
    args = parser.parse_args()
    print(Ana13().draw(args.output, variant=args.variant))
