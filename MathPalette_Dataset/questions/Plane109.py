"""Collected question Plane109; construction on the shared drawing protocol."""
from pathlib import Path
import sys
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from MathPalette_Dataset.drawing import Canvas, PLANE

class Plane109:
    variants = ('C01', 'C02', 'C03', 'C04', 'C05', 'C06', 'C07', 'C08')

    def __init__(self):
        self.points = {
            'top_center': [0, 1.3279056191361391], 'left_center': [-1.15, -0.6639528095680696],
            'right_center': [1.15, -0.6639528095680696],
            'crossing_1': [-1.5996950765959597, 0.9235843830939964],
            'crossing_2': [-0.44969507659595975, -0.2596315735259268],
            'crossing_3': [0.0, -1.8471687661879928], 'crossing_4': [0.0, 0.5192631470518536],
            'crossing_5': [0.44969507659595975, -0.2596315735259268],
            'crossing_6': [1.5996950765959597, 0.9235843830939964]
        }

    def draw(self, output_path=None, *, variant=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / (self.__class__.__name__ + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if variant not in self.variants:
                raise ValueError('Unknown Special variant: ' + str(variant))
            return getattr(self, 'draw_' + variant)(output_path)
        with Canvas(PLANE, xlim=(-2.9302325581395348, 2.9302325581395348), ylim=(-2.5982561533555, 3.2622089629235695)) as c:
            for object_id, center, radius in [('top', self.points['top_center'], 1.65), ('left', self.points['left_center'], 1.65), ('right', self.points['right_center'], 1.65)]:
                c.circle(center, radius, id=object_id)
            return c.save(output_path)

    def draw_C01(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane109_C01.png'
        with Canvas(PLANE, xlim=(-2.9302325581395348, 2.9302325581395348), ylim=(-2.5982561533555, 3.2622089629235695)) as c:
            for object_id, center, radius in [('top', [0.0, 1.3279056191361391], 1.65), ('left', [-1.15, -0.6639528095680696], 1.65), ('right', [1.15, -0.6639528095680696], 1.65)]:
                c.circle(center, radius, id=object_id, fill=False)
            for object_id, points in [(None, [[-0.44969507659595975, -0.2596315735259268]]), (None, [[0.0, -1.8471687661879928]]), (None, [[0.0, 0.5192631470518536]]), (None, [[0.44969507659595975, -0.2596315735259268]]), (None, [[1.5996950765959597, 0.9235843830939964]])]:
                c.point(points, id=object_id, zorder=10, s=50, facecolors='#DC2626', edgecolors='#DC2626')
            return c.save(output_path)

    def draw_C02(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane109_C02.png'
        with Canvas(PLANE, xlim=(-2.9302325581395348, 2.9302325581395348), ylim=(-2.5982561533555, 3.2622089629235695)) as c:
            for object_id, center, radius in [('top', [0.0, 1.3279056191361391], 1.65), ('left', [-1.15, -0.6639528095680696], 1.65), ('right', [1.15, -0.6639528095680696], 1.65)]:
                c.circle(center, radius, id=object_id, fill=False)
            for object_id, points in [(None, [[-1.5996950765959597, 0.9235843830939964]]), (None, [[0.0, -1.8471687661879928]]), (None, [[0.0, 0.5192631470518536]]), (None, [[0.44969507659595975, -0.2596315735259268]]), (None, [[1.5996950765959597, 0.9235843830939964]])]:
                c.point(points, id=object_id, zorder=10, s=50, facecolors='#EA580C', edgecolors='#EA580C')
            return c.save(output_path)

    def draw_C03(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane109_C03.png'
        with Canvas(PLANE, xlim=(-2.9302325581395348, 2.9302325581395348), ylim=(-2.5982561533555, 3.2622089629235695)) as c:
            for object_id, center, radius in [('top', [0.0, 1.3279056191361391], 1.65), ('left', [-1.15, -0.6639528095680696], 1.65), ('right', [1.15, -0.6639528095680696], 1.65)]:
                c.circle(center, radius, id=object_id, fill=False)
            for object_id, points in [(None, [[-1.5996950765959597, 0.9235843830939964]]), (None, [[-0.44969507659595975, -0.2596315735259268]]), (None, [[0.0, -1.8471687661879928]]), (None, [[0.0, 0.5192631470518536]]), (None, [[0.44969507659595975, -0.2596315735259268]])]:
                c.point(points, id=object_id, zorder=10, s=50, facecolors='#EA580C', edgecolors='#EA580C')
            return c.save(output_path)

    def draw_C04(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane109_C04.png'
        with Canvas(PLANE, xlim=(-2.9302325581395348, 2.9302325581395348), ylim=(-2.5982561533555, 3.2622089629235695)) as c:
            for object_id, center, radius in [('top', [0.0, 1.3279056191361391], 1.65), ('left', [-1.15, -0.6639528095680696], 1.65), ('right', [1.15, -0.6639528095680696], 1.65)]:
                c.circle(center, radius, id=object_id, fill=False)
            for object_id, points in [(None, [[0.0, -1.8471687661879928]]), (None, [[0.0, 0.5192631470518536]]), (None, [[0.44969507659595975, -0.2596315735259268]]), (None, [[1.5996950765959597, 0.9235843830939964]])]:
                c.point(points, id=object_id, zorder=10, s=50, facecolors='#DC2626', edgecolors='#DC2626')
            return c.save(output_path)

    def draw_C05(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane109_C05.png'
        with Canvas(PLANE, xlim=(-2.9302325581395348, 2.9302325581395348), ylim=(-2.5982561533555, 3.2622089629235695)) as c:
            for object_id, center, radius in [('top', [0.0, 1.3279056191361391], 1.65), ('left', [-1.15, -0.6639528095680696], 1.65), ('right', [1.15, -0.6639528095680696], 1.65)]:
                c.circle(center, radius, id=object_id, fill=False)
            for object_id, points in [(None, [[-0.44969507659595975, -0.2596315735259268]]), (None, [[0.0, -1.8471687661879928]]), (None, [[0.0, 0.5192631470518536]]), (None, [[1.5996950765959597, 0.9235843830939964]])]:
                c.point(points, id=object_id, zorder=10, s=50, facecolors='#DC2626', edgecolors='#DC2626')
            return c.save(output_path)

    def draw_C06(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane109_C06.png'
        with Canvas(PLANE, xlim=(-2.9302325581395348, 2.9302325581395348), ylim=(-2.5982561533555, 3.2622089629235695)) as c:
            for object_id, center, radius in [('top', [0.0, 1.3279056191361391], 1.65), ('left', [-1.15, -0.6639528095680696], 1.65), ('right', [1.15, -0.6639528095680696], 1.65)]:
                c.circle(center, radius, id=object_id, fill=False)
            for object_id, points in [(None, [[-1.5996950765959597, 0.9235843830939964]]), (None, [[-0.44969507659595975, -0.2596315735259268]]), (None, [[0.0, -1.8471687661879928]]), (None, [[0.0, 0.5192631470518536]]), (None, [[0.44969507659595975, -0.2596315735259268]]), (None, [[1.5996950765959597, 0.9235843830939964]]), (None, [[1.65, 1.3279056191361391]])]:
                c.point(points, id=object_id, zorder=10, s=50, facecolors='#DC2626', edgecolors='#DC2626')
            return c.save(output_path)

    def draw_C07(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane109_C07.png'
        with Canvas(PLANE, xlim=(-2.9302325581395348, 2.9302325581395348), ylim=(-2.5982561533555, 3.2622089629235695)) as c:
            for object_id, center, radius in [('top', [0.0, 1.3279056191361391], 1.65), ('left', [-1.15, -0.6639528095680696], 1.65), ('right', [1.15, -0.6639528095680696], 1.65)]:
                c.circle(center, radius, id=object_id, fill=False)
            for object_id, points in [(None, [[-1.5996950765959597, 0.9235843830939964]]), (None, [[-0.44969507659595975, -0.2596315735259268]]), (None, [[0.0, -1.8471687661879928]]), (None, [[0.0, 0.5192631470518536]]), (None, [[0.44969507659595975, -0.2596315735259268]]), (None, [[1.5996950765959597, 0.9235843830939964]]), (None, [[-3.031000827889699e-16, -0.3220943808638608]])]:
                c.point(points, id=object_id, zorder=10, s=50, facecolors='#16A34A', edgecolors='#16A34A')
            return c.save(output_path)

    def draw_C08(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane109_C08.png'
        with Canvas(PLANE, xlim=(-2.9302325581395348, 2.9302325581395348), ylim=(-2.5982561533555, 3.2622089629235695)) as c:
            for object_id, center, radius in [('top', [0.0, 1.3279056191361391], 1.65), ('left', [-1.15, -0.6639528095680696], 1.65), ('right', [1.15, -0.6639528095680696], 1.65)]:
                c.circle(center, radius, id=object_id, fill=False)
            for object_id, points in [(None, [[-1.5996950765959597, 0.9235843830939964]]), (None, [[-0.44969507659595975, -0.2596315735259268]]), (None, [[0.0, -1.8471687661879928]]), (None, [[0.0, 0.5192631470518536]]), (None, [[0.44969507659595975, -0.2596315735259268]]), (None, [[1.5996950765959597, 0.9235843830939964]]), (None, [[0.5, -0.6639528095680696]])]:
                c.point(points, id=object_id, zorder=10, s=50, facecolors='#DC2626', edgecolors='#DC2626')
            return c.save(output_path)

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Plane109')
    parser.add_argument('output', nargs='?')
    parser.add_argument('--variant', choices=('C01', 'C02', 'C03', 'C04', 'C05', 'C06', 'C07', 'C08'))
    args = parser.parse_args()
    print(Plane109().draw(args.output, variant=args.variant))
