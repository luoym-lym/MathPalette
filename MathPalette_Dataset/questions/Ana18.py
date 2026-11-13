"""Collected question Ana18; construction on the shared drawing protocol."""
from pathlib import Path
import sys
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from MathPalette_Dataset.drawing import Canvas, ANALYTICS

class Ana18:
    variants = ('C01', 'C02', 'C03', 'C04', 'C05')

    def _samples_001(self):
        x = np.linspace(-7, 5, 300)
        return np.column_stack((x, x ** 2))

    def _samples_002(self):
        x = np.linspace(-7, 5, 300)
        return np.column_stack((x, (x + 3.0) ** 2 - 2.0))

    def _draw_base(self, c):
        c.line(self._samples_001(), id='curve_001', solid_capstyle='butt')
        c.line(self._samples_002(), id='curve_002', solid_capstyle='butt')

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
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Ana18_C01.png'
        with Canvas(ANALYTICS) as c:
            c.line(self._samples_001(), id='curve_001', solid_capstyle='butt')
            c.line(self._samples_002(), id='curve_002', color='#DC2626', solid_capstyle='butt')
            return c.save(output_path)

    def draw_C02(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Ana18_C02.png'
        with Canvas(ANALYTICS) as c:
            c.line(self._samples_001(), id='curve_001', color='#2563EB', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            c.line(self._samples_002(), id='curve_002', color='#DC2626', solid_capstyle='butt')
            return c.save(output_path)

    def draw_C03(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Ana18_C03.png'
        with Canvas(ANALYTICS) as c:
            c.line(self._samples_001(), id='curve_001', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            c.line(self._samples_002(), id='curve_002', solid_capstyle='butt')
            return c.save(output_path)

    def draw_C04(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Ana18_C04.png'
        with Canvas(ANALYTICS) as c:
            self._draw_base(c)
            c.point([[-4.0, -1.0]], zorder=10, s=50, facecolors='#DC2626', edgecolors='#DC2626')
            return c.save(output_path)

    def draw_C05(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Ana18_C05.png'
        with Canvas(ANALYTICS) as c:
            c.line(self._samples_001(), id='curve_001', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            c.line(self._samples_002(), id='curve_002', solid_capstyle='butt')
            c.point([[0.0, 0.0]], zorder=10, s=50, facecolors='#DC2626', edgecolors='#DC2626')
            return c.save(output_path)

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Ana18')
    parser.add_argument('output', nargs='?')
    parser.add_argument('--variant', choices=('C01', 'C02', 'C03', 'C04', 'C05'))
    args = parser.parse_args()
    print(Ana18().draw(args.output, variant=args.variant))
