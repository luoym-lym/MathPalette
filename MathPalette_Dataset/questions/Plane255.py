"""Collected question Plane255; construction on the shared drawing protocol."""
from pathlib import Path
import sys
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from MathPalette_Dataset.drawing import Canvas, PLANE

class Plane255:
    variants = ('C01',)

    def draw(self, output_path=None, *, variant=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / (self.__class__.__name__ + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if variant not in self.variants:
                raise ValueError('Unknown Special variant: ' + str(variant))
            return getattr(self, 'draw_' + variant)(output_path)
        with Canvas(PLANE, xlim=(-0.3090991525872955, 12.309099152587295), ylim=(-3.815876804671571, 8.80232150050302)) as c:
            c.path([[0, 5], [8, 5], [12, 0], [4, 0], [0, 5]], [1, 2, 2, 2, 79], id='o0')
            for object_id, points in [('o1', [[0, 5], [1.5, 3.9]]), ('o2', [[1.5, 3.9], [2.6, 4.5]]), ('o3', [[2.6, 4.5], [2.7, 3.2]]), ('o4', [[2.7, 3.2], [5.5, 2.95]]), ('o5', [[5.5, 2.95], [5.5, 1.2]]), ('o6', [[5.5, 1.2], [7, 1.95]]), ('o7', [[7, 1.95], [8.4, 0.85]]), ('o8', [[8.4, 0.85], [9.25, 1.45]]), ('o9', [[9.25, 1.45], [9.35, 0.7]]), ('o10', [[9.35, 0.7], [12, 0]])]:
                c.line(points, id=object_id)
            c.text('$P_1$', [4.5, 1.4], id='t0')
            c.text('$P_2$', [7.3, 3.5], id='t1')
            return c.save(output_path)

    def draw_C01(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane255_C01.png'
        with Canvas(PLANE, xlim=(-0.3090991525872955, 12.309099152587295), ylim=(-3.815876804671571, 8.80232150050302)) as c:
            c.path([[0.0, 5.0], [8.0, 5.0], [12.0, 0.0], [4.0, 0.0], [0.0, 5.0]], [1, 2, 2, 2, 79], id='o0', capstyle='butt')
            for object_id, points in [('o1', [[0.0, 5.0], [1.5, 3.9]]), ('o2', [[1.5, 3.9], [2.6, 4.5]]), ('o3', [[2.6, 4.5], [2.7, 3.2]]), ('o4', [[2.7, 3.2], [5.5, 2.95]]), ('o5', [[5.5, 2.95], [5.5, 1.2]]), ('o6', [[5.5, 1.2], [7.0, 1.95]]), ('o7', [[7.0, 1.95], [8.4, 0.85]]), ('o8', [[8.4, 0.85], [9.25, 1.45]]), ('o9', [[9.25, 1.45], [9.35, 0.7]]), ('o10', [[9.35, 0.7], [12.0, 0.0]])]:
                c.line(points, id=object_id)
            c.text('$P_1$', (4.5, 1.4), id='t0')
            c.text('$P_2$', (7.3, 3.5), id='t1')
            c.line([[0, 5], [12, 0]], zorder=9, color='#2563EB', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            return c.save(output_path)
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Plane255')
    parser.add_argument('output', nargs='?')
    parser.add_argument('--variant', choices=('C01',))
    args = parser.parse_args()
    print(Plane255().draw(args.output, variant=args.variant))
