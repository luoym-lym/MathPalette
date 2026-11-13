"""Collected question Plane114; construction on the shared drawing protocol."""
from pathlib import Path
import sys
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from MathPalette_Dataset.drawing import Canvas, PLANE

class Plane114:
    variants = ('C01', 'C02', 'C03', 'C04', 'C05')

    def __init__(self):
        self.points = {
            'circle_center': [0.0, 0.0], 'square_v0': [-1.5, -1.5], 'square_v1': [1.5, -1.5],
            'square_v2': [1.5, 1.5], 'square_v3': [-1.5, 1.5], 'crossing_1': [-1.5, -0.9013878188659974],
            'crossing_2': [-1.5, 0.9013878188659974], 'crossing_3': [-0.9013878188659974, -1.5],
            'crossing_4': [-0.9013878188659974, 1.5], 'crossing_5': [0.9013878188659974, -1.5],
            'crossing_6': [0.9013878188659974, 1.5], 'crossing_7': [1.5, -0.9013878188659974],
            'crossing_8': [1.5, 0.9013878188659974]
        }

    def draw(self, output_path=None, *, variant=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / (self.__class__.__name__ + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if variant not in self.variants:
                raise ValueError('Unknown Special variant: ' + str(variant))
            return getattr(self, 'draw_' + variant)(output_path)
        with Canvas(PLANE, xlim=(-1.8313953488372092, 1.8313953488372092), ylim=(-1.8313953488372092, 1.8313953488372092)) as c:
            c.circle(self.points['circle_center'], 1.75, id='circle')
            c.path([self.points['square_v0'], self.points['square_v1'], self.points['square_v2'], self.points['square_v3'], self.points['square_v0']], [1, 2, 2, 2, 79], id='square')
            return c.save(output_path)

    def draw_C01(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane114_C01.png'
        with Canvas(PLANE, xlim=(-1.8313953488372092, 1.8313953488372092), ylim=(-1.8313953488372092, 1.8313953488372092)) as c:
            c.circle([0.0, 0.0], 1.75, id='circle', fill=False)
            c.path([[-1.5, -1.5], [1.5, -1.5], [1.5, 1.5], [-1.5, 1.5], [-1.5, -1.5]], [1, 2, 2, 2, 79], id='square', capstyle='butt')
            for object_id, points in [(None, [[-1.5, 0.9013878188659974]]), (None, [[-0.9013878188659974, -1.5]]), (None, [[-0.9013878188659974, 1.5]]), (None, [[0.9013878188659974, -1.5]]), (None, [[0.9013878188659974, 1.5]]), (None, [[1.5, -0.9013878188659974]]), (None, [[1.5, 0.9013878188659974]])]:
                c.point(points, id=object_id, zorder=10, s=50, facecolors='#DC2626', edgecolors='#DC2626')
            return c.save(output_path)

    def draw_C02(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane114_C02.png'
        with Canvas(PLANE, xlim=(-1.8313953488372092, 1.8313953488372092), ylim=(-1.8313953488372092, 1.8313953488372092)) as c:
            c.circle([0.0, 0.0], 1.75, id='circle', fill=False)
            c.path([[-1.5, -1.5], [1.5, -1.5], [1.5, 1.5], [-1.5, 1.5], [-1.5, -1.5]], [1, 2, 2, 2, 79], id='square', capstyle='butt')
            for object_id, points in [(None, [[-1.5, -0.9013878188659974]]), (None, [[-1.5, 0.9013878188659974]]), (None, [[-0.9013878188659974, 1.5]]), (None, [[0.9013878188659974, -1.5]]), (None, [[0.9013878188659974, 1.5]]), (None, [[1.5, -0.9013878188659974]]), (None, [[1.5, 0.9013878188659974]])]:
                c.point(points, id=object_id, zorder=10, s=50, facecolors='#2563EB', edgecolors='#2563EB')
            return c.save(output_path)

    def draw_C03(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane114_C03.png'
        with Canvas(PLANE, xlim=(-1.8313953488372092, 1.8313953488372092), ylim=(-1.8313953488372092, 1.8313953488372092)) as c:
            c.circle([0.0, 0.0], 1.75, id='circle', fill=False)
            c.path([[-1.5, -1.5], [1.5, -1.5], [1.5, 1.5], [-1.5, 1.5], [-1.5, -1.5]], [1, 2, 2, 2, 79], id='square', capstyle='butt')
            for object_id, points in [(None, [[-1.5, 0.9013878188659974]]), (None, [[-0.9013878188659974, 1.5]]), (None, [[0.9013878188659974, -1.5]]), (None, [[0.9013878188659974, 1.5]]), (None, [[1.5, -0.9013878188659974]]), (None, [[1.5, 0.9013878188659974]])]:
                c.point(points, id=object_id, zorder=10, s=50, facecolors='#DC2626', edgecolors='#DC2626')
            return c.save(output_path)

    def draw_C04(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane114_C04.png'
        with Canvas(PLANE, xlim=(-1.8313953488372092, 1.8313953488372092), ylim=(-1.8313953488372092, 1.8313953488372092)) as c:
            c.circle([0.0, 0.0], 1.75, id='circle', fill=False)
            c.path([[-1.5, -1.5], [1.5, -1.5], [1.5, 1.5], [-1.5, 1.5], [-1.5, -1.5]], [1, 2, 2, 2, 79], id='square', capstyle='butt')
            for object_id, points in [(None, [[-1.5, 0.9013878188659974]]), (None, [[-0.9013878188659974, -1.5]]), (None, [[-0.9013878188659974, 1.5]]), (None, [[0.9013878188659974, 1.5]]), (None, [[1.5, -0.9013878188659974]]), (None, [[1.5, 0.9013878188659974]])]:
                c.point(points, id=object_id, zorder=10, s=50, facecolors='#DC2626', edgecolors='#DC2626')
            return c.save(output_path)

    def draw_C05(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane114_C05.png'
        with Canvas(PLANE, xlim=(-1.8313953488372092, 1.8313953488372092), ylim=(-1.8313953488372092, 1.8313953488372092)) as c:
            c.circle([0.0, 0.0], 1.75, id='circle', fill=False)
            c.path([[-1.5, -1.5], [1.5, -1.5], [1.5, 1.5], [-1.5, 1.5], [-1.5, -1.5]], [1, 2, 2, 2, 79], id='square', capstyle='butt')
            for object_id, points in [(None, [[-1.5, -0.9013878188659974]]), (None, [[-1.5, 0.9013878188659974]]), (None, [[-0.9013878188659974, -1.5]]), (None, [[-0.9013878188659974, 1.5]]), (None, [[0.9013878188659974, -1.5]]), (None, [[0.9013878188659974, 1.5]]), (None, [[1.5, -0.9013878188659974]]), (None, [[1.5, 0.9013878188659974]]), (None, [[1.75, 0.0]])]:
                c.point(points, id=object_id, zorder=10, s=50, facecolors='#DC2626', edgecolors='#DC2626')
            return c.save(output_path)

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Plane114')
    parser.add_argument('output', nargs='?')
    parser.add_argument('--variant', choices=('C01', 'C02', 'C03', 'C04', 'C05'))
    args = parser.parse_args()
    print(Plane114().draw(args.output, variant=args.variant))
