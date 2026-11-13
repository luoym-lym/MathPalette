"""Collected question Ana14; construction on the shared drawing protocol."""
from pathlib import Path
import sys
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from MathPalette_Dataset.drawing import Canvas, ANALYTICS

class Ana14:
    variants = ('C01', 'C02', 'C03', 'C04')

    def _draw_base(self, c):
        x = np.linspace(-5, 5.5, 300)
        c.line(np.column_stack((x, 0.15 * (x + 3.0) * (x - 1.0) * (x - 4.0))), id='curve_001', solid_capstyle='butt')

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
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Ana14_C01.png'
        with Canvas(ANALYTICS) as c:
            self._draw_base(c)
            for object_id, points in [(None, [[-3.0, 0.0]]), (None, [[1.0, 0.0]]), (None, [[5.0, 0.0]])]:
                c.point(points, id=object_id, zorder=10, s=50, facecolors='#DC2626', edgecolors='#DC2626')
            return c.save(output_path)

    def draw_C02(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Ana14_C02.png'
        with Canvas(ANALYTICS) as c:
            self._draw_base(c)
            for object_id, points in [(None, [[3.0, 0.0]]), (None, [[1.0, 0.0]]), (None, [[-3.0, 0.0]])]:
                c.point(points, id=object_id, zorder=10, s=50, facecolors='#DC2626', edgecolors='#DC2626')
            return c.save(output_path)

    def draw_C03(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Ana14_C03.png'
        with Canvas(ANALYTICS) as c:
            self._draw_base(c)
            for object_id, points in [(None, [[1.0, 0.0]]), (None, [[4.0, 0.0]]), (None, [[-2.0, 0.0]])]:
                c.point(points, id=object_id, zorder=10, s=50, facecolors='#DC2626', edgecolors='#DC2626')
            return c.save(output_path)

    def draw_C04(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Ana14_C04.png'
        with Canvas(ANALYTICS) as c:
            self._draw_base(c)
            for object_id, points in [(None, [[-4.0, 0.0]]), (None, [[1.0, 0.0]]), (None, [[4.0, 0.0]])]:
                c.point(points, id=object_id, zorder=10, s=50, facecolors='#DC2626', edgecolors='#DC2626')
            return c.save(output_path)

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Ana14')
    parser.add_argument('output', nargs='?')
    parser.add_argument('--variant', choices=('C01', 'C02', 'C03', 'C04'))
    args = parser.parse_args()
    print(Ana14().draw(args.output, variant=args.variant))
