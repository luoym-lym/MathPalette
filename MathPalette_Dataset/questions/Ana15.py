"""Collected question Ana15; construction on the shared drawing protocol."""
from pathlib import Path
import sys
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from MathPalette_Dataset.drawing import Canvas, ANALYTICS

class Ana15:
    variants = ('C01', 'C02', 'C03', 'C04')

    def _draw_base(self, c):
        x = np.linspace(-8, 8, 382)
        c.line(np.column_stack((x, 4.0 * np.cos(x))), id='curve_001', solid_capstyle='butt')
        x = np.linspace(-8, 8, 382)
        c.line(np.column_stack((x, 2.0 * np.sin(x))), id='curve_002', solid_capstyle='butt')
        c.text('y1', [0.4, 4.4], id='text_001', ha='left', va='bottom')
        c.text('y2', [1.9707963267948965, 2.4], id='text_002', ha='left', va='bottom')

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
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Ana15_C01.png'
        with Canvas(ANALYTICS) as c:
            self._draw_base(c)
            c.line([[-8, 4], [8, 4]], zorder=9, color='#2563EB', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            c.line([[-8, 3], [8, 3]], zorder=9, color='#2563EB', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            return c.save(output_path)

    def draw_C02(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Ana15_C02.png'
        with Canvas(ANALYTICS) as c:
            self._draw_base(c)
            c.line([[-8, -2], [8, -2]], zorder=9, color='#2563EB', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            c.line([[-8, -5], [8, -5]], zorder=9, color='#2563EB', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            return c.save(output_path)

    def draw_C03(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Ana15_C03.png'
        with Canvas(ANALYTICS) as c:
            self._draw_base(c)
            c.line([[-8, -2], [8, -2]], zorder=9, color='#2563EB', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            c.line([[-8, -3], [8, -3]], zorder=9, color='#2563EB', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            return c.save(output_path)

    def draw_C04(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Ana15_C04.png'
        with Canvas(ANALYTICS) as c:
            self._draw_base(c)
            c.point([[0.0, 4.0]], zorder=10, s=50, facecolors='#DC2626', edgecolors='#DC2626')
            c.point([[2.651471, 0.997059]], zorder=10, s=50, facecolors='#DC2626', edgecolors='#DC2626')
            return c.save(output_path)

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Ana15')
    parser.add_argument('output', nargs='?')
    parser.add_argument('--variant', choices=('C01', 'C02', 'C03', 'C04'))
    args = parser.parse_args()
    print(Ana15().draw(args.output, variant=args.variant))
