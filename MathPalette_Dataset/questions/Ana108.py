"""Collected question Ana108; construction on the shared drawing protocol."""
from pathlib import Path
import sys
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from MathPalette_Dataset.drawing import Canvas, ANALYTICS

class Ana108:
    variants = ('C01',)

    def _draw_base(self, c):
        _segs108 = [(-6.8, -6.0, 51, False, [-36.20019189415, -18.88134008588, -3.40626408565, -0.19531323354]), (-6.0, -5.0, 51, True, [-23.14999714323, -14.69999843594, -3.09999971506, -0.19999998273]), (-5.0, -4.0, 51, True, [4.34999994151, 1.29999996082, -8.73e-09, -6.5e-10]), (-4.0, -3.0, 51, True, [2.75000000101, 0.50000000087, -0.09999999975, 2e-11]), (-3.0, -2.0, 51, True, [1.39999999836, -0.850000002, -0.55000000081, -0.05000000011]), (-2.0, -1.0, 51, True, [1.79999999996, -0.45000000009, -0.45000000006, -0.05000000001]), (-1.0, 0.0, 51, True, [2.0, 0.0, -0.15, 0.0]), (0.0, 1.0, 51, True, [2.0, -0.0, -0.04, -0.04]), (1.0, 2.0, 51, True, [2.01999999997, -0.01999999993, -0.06000000005, -0.01999999999]), (2.0, 3.0, 51, True, [1.77999999901, 0.50000000121, -0.40000000049, 0.05000000006]), (3.0, 4.0, 51, True, [-0.01999995226, 2.14999995876, -0.89999998818, 0.09999999887]), (4.0, 4.5, 51, True, [-15.70016134767, 12.87011404423, -3.32002685032, 0.28000210568]), (4.5, 5.0, 51, True, [-15.69971058116, 11.24981701555, -2.5999614584, 0.19999729558]), (5.0, 6.0, 51, True, [11.80000061504, -6.00000033682, 1.00000006138, -0.05000000372]), (6.0, 7.0, 51, True, [44.19999781389, -22.1999989915, 3.69999984511, -0.19999999208]), (7.0, 7.8, 50, True, [-4.49375892987, 1.51250362334, -0.09375048976, 2.205e-08])]
        c.line(np.vstack([np.column_stack(((x := np.linspace(a, b, n)[1 if skip else 0:]), c0 + c1 * x + c2 * x ** 2 + c3 * x ** 3)) for a, b, n, skip, (c0, c1, c2, c3) in _segs108]), id='object_000', solid_capstyle='butt')

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
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Ana108_C01.png'
        with Canvas(ANALYTICS) as c:
            self._draw_base(c)
            c.point([[-2.480163, 0.969905]], zorder=10, s=50, facecolors='#DC2626', edgecolors='#DC2626')
            c.point([[6.0, 1.0]], zorder=10, s=50, facecolors='#DC2626', edgecolors='#DC2626')
            c.line([[-8, 1], [-1, 1]], zorder=9, color='#2563EB', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            c.line([[4, 1], [8, 1]], zorder=9, color='#2563EB', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            return c.save(output_path)

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Ana108')
    parser.add_argument('output', nargs='?')
    parser.add_argument('--variant', choices=('C01',))
    args = parser.parse_args()
    print(Ana108().draw(args.output, variant=args.variant))
