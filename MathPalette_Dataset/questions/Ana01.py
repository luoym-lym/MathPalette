"""Collected question Ana01; construction on the shared drawing protocol."""
from pathlib import Path
import sys
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from MathPalette_Dataset.drawing import Canvas, ANALYTICS

class Ana01:
    variants = ('C01', 'C02')

    def _draw_base(self, c):
        x = np.linspace(-8, 1, 200)
        c.line(np.column_stack((x, x * x + x - 2)), id='curve_001', solid_capstyle='butt')
        x = np.linspace(1, 8, 200)
        c.line(np.column_stack((x, -4 * x + 2)), id='curve_002', solid_capstyle='butt')
        c.point([[1, 0]], filled=False, id='point_001')
        c.point([[1, -2]], id='point_002')

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
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Ana01_C01.png'
        with Canvas(ANALYTICS) as c:
            self._draw_base(c)
            c.point([[0.647794, -1.025]], zorder=10, s=50, facecolors='#DC2626', edgecolors='#DC2626')
            return c.save(output_path)

    def draw_C02(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Ana01_C02.png'
        with Canvas(ANALYTICS) as c:
            self._draw_base(c)
            c.point([[1.0, -1.0]], zorder=10, s=50, facecolors='#DC2626', edgecolors='#DC2626')
            return c.save(output_path)

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Ana01')
    parser.add_argument('output', nargs='?')
    parser.add_argument('--variant', choices=('C01', 'C02'))
    args = parser.parse_args()
    print(Ana01().draw(args.output, variant=args.variant))
