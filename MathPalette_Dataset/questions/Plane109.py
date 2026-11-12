"""Collected question Plane109; construction on the shared drawing protocol."""
from pathlib import Path
import sys
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from MathPalette_Dataset.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane109:
    variants = ('C01', 'C02', 'C03', 'C04', 'C05', 'C06', 'C07', 'C08')

    def __init__(self):
        self.id = 'Plane109'
        self.source_dataset = 'Author Designed'
        self.source_key = 'intersection-counting:equal_circles_small_center'
        self.question = 'How many intersection points are there in the diagram?'
        self.answer = 6
        self.answer_type = 'number'
        self.query = self.question
        self.points = {'top_center': [0, 1.3279056191361391],
         'left_center': [-1.15, -0.6639528095680696],
         'right_center': [1.15, -0.6639528095680696],
         'crossing_1': [-1.5996950765959597, 0.9235843830939964],
         'crossing_2': [-0.44969507659595975, -0.2596315735259268],
         'crossing_3': [0.0, -1.8471687661879928],
         'crossing_4': [0.0, 0.5192631470518536],
         'crossing_5': [0.44969507659595975, -0.2596315735259268],
         'crossing_6': [1.5996950765959597, 0.9235843830939964]}

    def draw(self, output_path=None, *, variant=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if variant not in self.variants:
                raise ValueError('Unknown Special variant: ' + str(variant))
            return getattr(self, 'draw_' + variant)(output_path)
        with Canvas(PLANE, xlim=[-2.9302325581395348, 2.9302325581395348], ylim=[-2.5982561533555, 3.2622089629235695]) as c:
            for object_id, center, radius in [('top', self.points['top_center'], 1.65), ('left', self.points['left_center'], 1.65), ('right', self.points['right_center'], 1.65)]:
                c.circle(center, radius, id=object_id)
            return c.save(output_path)

    def draw_C01(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane109_C01.png'
        with Canvas(PLANE, xlim=(-2.9302325581395348, 2.9302325581395348), ylim=(-2.5982561533555, 3.2622089629235695), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
            for object_id, center, radius in [('top', [0.0, 1.3279056191361391], 1.65), ('left', [-1.15, -0.6639528095680696], 1.65), ('right', [1.15, -0.6639528095680696], 1.65)]:
                c.circle(center, radius, id=object_id, fill=False)
            for object_id, points in [(None, [[-0.44969507659595975, -0.2596315735259268]]), (None, [[0.0, -1.8471687661879928]]), (None, [[0.0, 0.5192631470518536]]), (None, [[0.44969507659595975, -0.2596315735259268]]), (None, [[1.5996950765959597, 0.9235843830939964]])]:
                c.point(points, id=object_id, zorder=10, s=[50], facecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]], edgecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]])
            return c.save(output_path)

    def draw_C02(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane109_C02.png'
        with Canvas(PLANE, xlim=(-2.9302325581395348, 2.9302325581395348), ylim=(-2.5982561533555, 3.2622089629235695), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
            for object_id, center, radius in [('top', [0.0, 1.3279056191361391], 1.65), ('left', [-1.15, -0.6639528095680696], 1.65), ('right', [1.15, -0.6639528095680696], 1.65)]:
                c.circle(center, radius, id=object_id, fill=False)
            for object_id, points in [(None, [[-1.5996950765959597, 0.9235843830939964]]), (None, [[0.0, -1.8471687661879928]]), (None, [[0.0, 0.5192631470518536]]), (None, [[0.44969507659595975, -0.2596315735259268]]), (None, [[1.5996950765959597, 0.9235843830939964]])]:
                c.point(points, id=object_id, zorder=10, s=[50], facecolors=[[0.9176470588235294, 0.34509803921568627, 0.047058823529411764, 1.0]], edgecolors=[[0.9176470588235294, 0.34509803921568627, 0.047058823529411764, 1.0]])
            return c.save(output_path)

    def draw_C03(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane109_C03.png'
        with Canvas(PLANE, xlim=(-2.9302325581395348, 2.9302325581395348), ylim=(-2.5982561533555, 3.2622089629235695), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
            for object_id, center, radius in [('top', [0.0, 1.3279056191361391], 1.65), ('left', [-1.15, -0.6639528095680696], 1.65), ('right', [1.15, -0.6639528095680696], 1.65)]:
                c.circle(center, radius, id=object_id, fill=False)
            for object_id, points in [(None, [[-1.5996950765959597, 0.9235843830939964]]), (None, [[-0.44969507659595975, -0.2596315735259268]]), (None, [[0.0, -1.8471687661879928]]), (None, [[0.0, 0.5192631470518536]]), (None, [[0.44969507659595975, -0.2596315735259268]])]:
                c.point(points, id=object_id, zorder=10, s=[50], facecolors=[[0.9176470588235294, 0.34509803921568627, 0.047058823529411764, 1.0]], edgecolors=[[0.9176470588235294, 0.34509803921568627, 0.047058823529411764, 1.0]])
            return c.save(output_path)

    def draw_C04(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane109_C04.png'
        with Canvas(PLANE, xlim=(-2.9302325581395348, 2.9302325581395348), ylim=(-2.5982561533555, 3.2622089629235695), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
            for object_id, center, radius in [('top', [0.0, 1.3279056191361391], 1.65), ('left', [-1.15, -0.6639528095680696], 1.65), ('right', [1.15, -0.6639528095680696], 1.65)]:
                c.circle(center, radius, id=object_id, fill=False)
            for object_id, points in [(None, [[0.0, -1.8471687661879928]]), (None, [[0.0, 0.5192631470518536]]), (None, [[0.44969507659595975, -0.2596315735259268]]), (None, [[1.5996950765959597, 0.9235843830939964]])]:
                c.point(points, id=object_id, zorder=10, s=[50], facecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]], edgecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]])
            return c.save(output_path)

    def draw_C05(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane109_C05.png'
        with Canvas(PLANE, xlim=(-2.9302325581395348, 2.9302325581395348), ylim=(-2.5982561533555, 3.2622089629235695), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
            for object_id, center, radius in [('top', [0.0, 1.3279056191361391], 1.65), ('left', [-1.15, -0.6639528095680696], 1.65), ('right', [1.15, -0.6639528095680696], 1.65)]:
                c.circle(center, radius, id=object_id, fill=False)
            for object_id, points in [(None, [[-0.44969507659595975, -0.2596315735259268]]), (None, [[0.0, -1.8471687661879928]]), (None, [[0.0, 0.5192631470518536]]), (None, [[1.5996950765959597, 0.9235843830939964]])]:
                c.point(points, id=object_id, zorder=10, s=[50], facecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]], edgecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]])
            return c.save(output_path)

    def draw_C06(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane109_C06.png'
        with Canvas(PLANE, xlim=(-2.9302325581395348, 2.9302325581395348), ylim=(-2.5982561533555, 3.2622089629235695), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
            for object_id, center, radius in [('top', [0.0, 1.3279056191361391], 1.65), ('left', [-1.15, -0.6639528095680696], 1.65), ('right', [1.15, -0.6639528095680696], 1.65)]:
                c.circle(center, radius, id=object_id, fill=False)
            for object_id, points in [(None, [[-1.5996950765959597, 0.9235843830939964]]), (None, [[-0.44969507659595975, -0.2596315735259268]]), (None, [[0.0, -1.8471687661879928]]), (None, [[0.0, 0.5192631470518536]]), (None, [[0.44969507659595975, -0.2596315735259268]]), (None, [[1.5996950765959597, 0.9235843830939964]]), (None, [[1.65, 1.3279056191361391]])]:
                c.point(points, id=object_id, zorder=10, s=[50], facecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]], edgecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]])
            return c.save(output_path)

    def draw_C07(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane109_C07.png'
        with Canvas(PLANE, xlim=(-2.9302325581395348, 2.9302325581395348), ylim=(-2.5982561533555, 3.2622089629235695), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
            for object_id, center, radius in [('top', [0.0, 1.3279056191361391], 1.65), ('left', [-1.15, -0.6639528095680696], 1.65), ('right', [1.15, -0.6639528095680696], 1.65)]:
                c.circle(center, radius, id=object_id, fill=False)
            for object_id, points in [(None, [[-1.5996950765959597, 0.9235843830939964]]), (None, [[-0.44969507659595975, -0.2596315735259268]]), (None, [[0.0, -1.8471687661879928]]), (None, [[0.0, 0.5192631470518536]]), (None, [[0.44969507659595975, -0.2596315735259268]]), (None, [[1.5996950765959597, 0.9235843830939964]]), (None, [[-3.031000827889699e-16, -0.3220943808638608]])]:
                c.point(points, id=object_id, zorder=10, s=[50], facecolors=[[0.08627450980392157, 0.6392156862745098, 0.2901960784313726, 1.0]], edgecolors=[[0.08627450980392157, 0.6392156862745098, 0.2901960784313726, 1.0]])
            return c.save(output_path)

    def draw_C08(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane109_C08.png'
        with Canvas(PLANE, xlim=(-2.9302325581395348, 2.9302325581395348), ylim=(-2.5982561533555, 3.2622089629235695), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
            for object_id, center, radius in [('top', [0.0, 1.3279056191361391], 1.65), ('left', [-1.15, -0.6639528095680696], 1.65), ('right', [1.15, -0.6639528095680696], 1.65)]:
                c.circle(center, radius, id=object_id, fill=False)
            for object_id, points in [(None, [[-1.5996950765959597, 0.9235843830939964]]), (None, [[-0.44969507659595975, -0.2596315735259268]]), (None, [[0.0, -1.8471687661879928]]), (None, [[0.0, 0.5192631470518536]]), (None, [[0.44969507659595975, -0.2596315735259268]]), (None, [[1.5996950765959597, 0.9235843830939964]]), (None, [[0.5, -0.6639528095680696]])]:
                c.point(points, id=object_id, zorder=10, s=[50], facecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]], edgecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]])
            return c.save(output_path)
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Plane109')
    parser.add_argument('output', nargs='?')
    parser.add_argument('--variant', choices=('C01', 'C02', 'C03', 'C04', 'C05', 'C06', 'C07', 'C08'))
    args = parser.parse_args()
    print(Plane109().draw(args.output, variant=args.variant))
