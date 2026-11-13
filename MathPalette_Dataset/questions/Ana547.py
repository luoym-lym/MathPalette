"""Collected question Ana547; construction on the shared drawing protocol."""
from pathlib import Path
import sys
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from MathPalette_Dataset.drawing import Canvas, ANALYTICS

class Ana547:
    variants = ('C01', 'C02')

    def _draw_base(self, c):
        c.line([[-6, -3], [-2, 1], [1, 4], [4, 1], [6, 3]], id='object_000', solid_capstyle='butt')
        c.line([[-6, 5], [-2, 3], [0, -1], [2, 1], [4, -3], [6, -1]], id='object_001', solid_capstyle='butt')
        c.point([[-6, -3], [6, 3], [-6, 5], [6, -1]], id='object_002')
        c.text('$f$', [6.5, 3.3])
        c.text('$g$', [6.5, -1.2])

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
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Ana547_C01.png'
        with Canvas(ANALYTICS) as c:
            self._draw_base(c)
            c.point([[-2.0, 1.0]], zorder=10, s=50, facecolors='#DC2626', edgecolors='#DC2626')
            for object_id, points in [(None, [[-2, 1], [4, 1]]), (None, [[-2, 1], [-2, 0]]), (None, [[4, 1], [4, 0]])]:
                c.line(points, id=object_id, zorder=9, color='#2563EB', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            c.point([[4.0, 1.0]], zorder=10, s=50, facecolors='#DC2626', edgecolors='#DC2626')
            return c.save(output_path)

    def draw_C02(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Ana547_C02.png'
        with Canvas(ANALYTICS) as c:
            self._draw_base(c)
            c.point([[-2.0, 1.0]], zorder=10, s=50, facecolors='#DC2626', edgecolors='#DC2626')
            c.line([[8, 8], [-8, -8]], zorder=9, color='#2563EB', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            c.point([[1.0, 1.0]], zorder=10, s=50, facecolors='#DC2626', edgecolors='#DC2626')
            for object_id, points in [(None, [[-2, 1], [1, 1]]), (None, [[-2, 1], [-2, 0]]), (None, [[1, 1], [1, 0]])]:
                c.line(points, id=object_id, zorder=9, color='#2563EB', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            return c.save(output_path)

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Ana547')
    parser.add_argument('output', nargs='?')
    parser.add_argument('--variant', choices=('C01', 'C02'))
    args = parser.parse_args()
    print(Ana547().draw(args.output, variant=args.variant))
