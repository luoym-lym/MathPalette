"""Collected question Ana21; construction on the shared drawing protocol."""
from pathlib import Path
import sys
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from MathPalette_Dataset.drawing import Canvas, ANALYTICS

class Ana21:
    variants = ('C01', 'C02', 'C03', 'C04', 'C05')

    def _draw_base(self, c):
        c.line([[-2, 6], [6, 6], [6, -2], [-2, -2], [-2, 6]], id='curve_001', solid_capstyle='projecting')

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
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Ana21_C01.png'
        with Canvas(ANALYTICS) as c:
            self._draw_base(c)
            c.point([[2.0, 3.0]], zorder=10, s=50, facecolors='#DC2626', edgecolors='#DC2626')
            return c.save(output_path)

    def draw_C02(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Ana21_C02.png'
        with Canvas(ANALYTICS) as c:
            self._draw_base(c)
            for object_id, points in [(None, [[-1.0, 6.0]]), (None, [[-1.0, -2.0]]), (None, [[6.0, -2.0]]), (None, [[6.0, 6.0]])]:
                c.point(points, id=object_id, zorder=10, s=50, facecolors='#DC2626', edgecolors='#DC2626')
            return c.save(output_path)

    def draw_C03(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Ana21_C03.png'
        with Canvas(ANALYTICS) as c:
            self._draw_base(c)
            for object_id, points in [(None, [[-2.0, 5.0]]), (None, [[6.0, 5.0]]), (None, [[6.0, -2.0]]), (None, [[-2.0, -2.0]])]:
                c.point(points, id=object_id, zorder=10, s=50, facecolors='#DC2626', edgecolors='#DC2626')
            return c.save(output_path)

    def draw_C04(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Ana21_C04.png'
        with Canvas(ANALYTICS) as c:
            self._draw_base(c)
            for object_id, points in [(None, [[-2.0, 6.0]]), (None, [[-2.0, -2.0]]), (None, [[5.0, -2.0]]), (None, [[5.0, 6.0]])]:
                c.point(points, id=object_id, zorder=10, s=50, facecolors='#DC2626', edgecolors='#DC2626')
            return c.save(output_path)

    def draw_C05(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Ana21_C05.png'
        with Canvas(ANALYTICS) as c:
            self._draw_base(c)
            for object_id, points in [(None, [[-2.0, 6.0]]), (None, [[6.0, 6.0]]), (None, [[6.0, -1.0]]), (None, [[-2.0, -1.0]])]:
                c.point(points, id=object_id, zorder=10, s=50, facecolors='#DC2626', edgecolors='#DC2626')
            return c.save(output_path)

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Ana21')
    parser.add_argument('output', nargs='?')
    parser.add_argument('--variant', choices=('C01', 'C02', 'C03', 'C04', 'C05'))
    args = parser.parse_args()
    print(Ana21().draw(args.output, variant=args.variant))
