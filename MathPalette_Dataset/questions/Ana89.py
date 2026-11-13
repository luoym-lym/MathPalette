"""Collected question Ana89; construction on the shared drawing protocol."""
from pathlib import Path
import sys
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from MathPalette_Dataset.drawing import Canvas, ANALYTICS

class Ana89:
    variants = ('C01',)

    def _draw_base(self, c):
        x1 = np.linspace(-8, 4.984066602343638, 1601)
        c.fill([np.vstack(([-8.0, 8.0], np.column_stack((x1, x1 ** 3 / 8 - 1.5 * x1)), [x1[-1], 8.0], [x1[-1], 8.0], np.column_stack((x1[::-1], np.full_like(x1, 8.0)))))], id='region_001', facecolors=[[0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45]], edgecolors=[], linewidths=[1.0], linestyles=[(0.0, None)], antialiaseds=[True])
        x2 = np.linspace(-8, 8, 2001)
        c.line(np.column_stack((x2, x2 ** 3 / 8 - 1.5 * x2)), id='curve_001', solid_capstyle='butt')

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
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Ana89_C01.png'
        with Canvas(ANALYTICS) as c:
            self._draw_base(c)
            c.line([[1, 8], [1, -8]], zorder=9, color='#2563EB', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            c.line([[-8, -2], [8, -2]], zorder=9, color='#2563EB', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            c.point([[1.0, -2.0]], zorder=10, s=50, facecolors='#DC2626', edgecolors='#DC2626')
            return c.save(output_path)

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Ana89')
    parser.add_argument('output', nargs='?')
    parser.add_argument('--variant', choices=('C01',))
    args = parser.parse_args()
    print(Ana89().draw(args.output, variant=args.variant))
