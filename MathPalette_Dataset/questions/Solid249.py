"""Collected question Solid249; construction on the shared drawing protocol."""
from pathlib import Path
import sys
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from MathPalette_Dataset.drawing import Canvas, SOLID

class Solid249:
    variants = ('C01',)

    def draw(self, output_path=None, *, variant=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / (self.__class__.__name__ + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if variant not in self.variants:
                raise ValueError('Unknown Special variant: ' + str(variant))
            return getattr(self, 'draw_' + variant)(output_path)
        with Canvas(SOLID, xlim=(-5.0, 5.0), ylim=(-5.0, 5.0)) as c:
            for object_id, points in [('bottom', [[-4, -4], [4, -4]]), ('right', [[4, -4], [4, 4]]), ('top', [[4, 4], [-4, 4]]), ('left', [[-4, 4], [-4, -4]])]:
                c.line(points, id=object_id)
            for object_id, center, radius in [('hole0', [-2, 1], 0.14), ('hole1', [2, 1], 0.14), ('hole2', [-1, -2], 0.14), ('hole3', [1, -2], 0.14)]:
                c.circle(center, radius, id=object_id, zorder=1, fill=False)
            return c.save(output_path)

    def draw_C01(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Solid249_C01.png'
        with Canvas(SOLID, xlim=(-5.0, 5.0), ylim=(-5.0, 5.0)) as c:
            for object_id, points in [('bottom', [[-4, -4], [4, -4]]), ('right', [[4, -4], [4, 4]]), ('top', [[4, 4], [-4, 4]]), ('left', [[-4, 4], [-4, -4]])]:
                c.line(points, id=object_id)
            c.circle([-2, 1], 0.14, id='hole0', zorder=1, edgecolor='#2563EB', linewidth=1.5, fill=False)
            c.circle([2, 1], 0.14, id='hole1', zorder=1, edgecolor='#DC2626', linewidth=1.5, fill=False)
            c.circle([-1, -2], 0.14, id='hole2', zorder=1, edgecolor='#DC2626', linewidth=1.5, fill=False)
            c.circle([1, -2], 0.14, id='hole3', zorder=1, edgecolor='#2563EB', linewidth=1.5, fill=False)
            return c.save(output_path)
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Solid249')
    parser.add_argument('output', nargs='?')
    parser.add_argument('--variant', choices=('C01',))
    args = parser.parse_args()
    print(Solid249().draw(args.output, variant=args.variant))
