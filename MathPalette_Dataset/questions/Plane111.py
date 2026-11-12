"""Collected question Plane111; construction on the shared drawing protocol."""
from pathlib import Path
import sys
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from MathPalette_Dataset.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane111:
    variants = ('C01', 'C02', 'C03', 'C04', 'C05', 'C06', 'C07', 'C08')

    def __init__(self):
        self.id = 'Plane111'
        self.source_dataset = 'Author Designed'
        self.source_key = 'intersection-counting:circle_nonparallel_lines'
        self.question = 'How many intersection points are shown?'
        self.answer = 5
        self.answer_type = 'number'
        self.query = self.question
        self.points = {'circle_center': [0, 0],
         'line_a_a': [-2.7, -0.32500000000000007],
         'line_a_b': [2.7, 1.025],
         'line_b_a': [-2.7, 1.7899999999999998],
         'line_b_b': [2.7, -1.99],
         'crossing_1': [-1.7478381048599623, -0.08695952621499062],
         'crossing_2': [-1.4790639505617877, 0.9353447653932512],
         'crossing_3': [-0.47368421052631593, 0.231578947368421],
         'crossing_4': [1.3851042190181628, -1.0695729533127138],
         'crossing_5': [1.5831322225070208, 0.7457830556267552]}

    def draw(self, output_path=None, *, variant=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if variant not in self.variants:
                raise ValueError('Unknown Special variant: ' + str(variant))
            return getattr(self, 'draw_' + variant)(output_path)
        with Canvas(PLANE, xlim=[-2.8255813953488373, 2.8255813953488373], ylim=[-2.9255813953488374, 2.7255813953488373]) as c:
            c.circle(self.points['circle_center'], 1.75, id='circle')
            c.line([self.points['line_a_a'], self.points['line_a_b']], id='line_a')
            c.line([self.points['line_b_a'], self.points['line_b_b']], id='line_b')
            return c.save(output_path)

    def draw_C01(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane111_C01.png'
        with Canvas(PLANE, xlim=(-2.8255813953488373, 2.8255813953488373), ylim=(-2.9255813953488374, 2.7255813953488373), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
            c.circle([0.0, 0.0], 1.75, id='circle', fill=False)
            c.line([[-2.7, -0.32500000000000007], [2.7, 1.025]], id='line_a')
            c.line([[-2.7, 1.7899999999999998], [2.7, -1.99]], id='line_b')
            for object_id, points in [(None, [[-1.4790639505617877, 0.9353447653932512]]), (None, [[-0.47368421052631593, 0.231578947368421]]), (None, [[1.3851042190181628, -1.0695729533127138]]), (None, [[1.5831322225070208, 0.7457830556267552]])]:
                c.point(points, id=object_id, zorder=10, s=[50], facecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]], edgecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]])
            return c.save(output_path)

    def draw_C02(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane111_C02.png'
        with Canvas(PLANE, xlim=(-2.8255813953488373, 2.8255813953488373), ylim=(-2.9255813953488374, 2.7255813953488373), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
            c.circle([0.0, 0.0], 1.75, id='circle', fill=False)
            c.line([[-2.7, -0.32500000000000007], [2.7, 1.025]], id='line_a')
            c.line([[-2.7, 1.7899999999999998], [2.7, -1.99]], id='line_b')
            for object_id, points in [(None, [[-1.7478381048599623, -0.08695952621499062]]), (None, [[-0.47368421052631593, 0.231578947368421]]), (None, [[1.3851042190181628, -1.0695729533127138]]), (None, [[1.5831322225070208, 0.7457830556267552]])]:
                c.point(points, id=object_id, zorder=10, s=[50], facecolors=[[0.9176470588235294, 0.34509803921568627, 0.047058823529411764, 1.0]], edgecolors=[[0.9176470588235294, 0.34509803921568627, 0.047058823529411764, 1.0]])
            return c.save(output_path)

    def draw_C03(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane111_C03.png'
        with Canvas(PLANE, xlim=(-2.8255813953488373, 2.8255813953488373), ylim=(-2.9255813953488374, 2.7255813953488373), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
            c.circle([0.0, 0.0], 1.75, id='circle', fill=False)
            c.line([[-2.7, -0.32500000000000007], [2.7, 1.025]], id='line_a')
            c.line([[-2.7, 1.7899999999999998], [2.7, -1.99]], id='line_b')
            for object_id, points in [(None, [[-1.7478381048599623, -0.08695952621499062]]), (None, [[-1.4790639505617877, 0.9353447653932512]]), (None, [[-0.47368421052631593, 0.231578947368421]]), (None, [[1.5831322225070208, 0.7457830556267552]])]:
                c.point(points, id=object_id, zorder=10, s=[50], facecolors=[[0.08627450980392157, 0.6392156862745098, 0.2901960784313726, 1.0]], edgecolors=[[0.08627450980392157, 0.6392156862745098, 0.2901960784313726, 1.0]])
            return c.save(output_path)

    def draw_C04(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane111_C04.png'
        with Canvas(PLANE, xlim=(-2.8255813953488373, 2.8255813953488373), ylim=(-2.9255813953488374, 2.7255813953488373), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
            c.circle([0.0, 0.0], 1.75, id='circle', fill=False)
            c.line([[-2.7, -0.32500000000000007], [2.7, 1.025]], id='line_a')
            c.line([[-2.7, 1.7899999999999998], [2.7, -1.99]], id='line_b')
            for object_id, points in [(None, [[-1.7478381048599623, -0.08695952621499062]]), (None, [[-1.4790639505617877, 0.9353447653932512]]), (None, [[-0.47368421052631593, 0.231578947368421]]), (None, [[1.3851042190181628, -1.0695729533127138]])]:
                c.point(points, id=object_id, zorder=10, s=[50], facecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]], edgecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]])
            return c.save(output_path)

    def draw_C05(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane111_C05.png'
        with Canvas(PLANE, xlim=(-2.8255813953488373, 2.8255813953488373), ylim=(-2.9255813953488374, 2.7255813953488373), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
            c.circle([0.0, 0.0], 1.75, id='circle', fill=False)
            c.line([[-2.7, -0.32500000000000007], [2.7, 1.025]], id='line_a')
            c.line([[-2.7, 1.7899999999999998], [2.7, -1.99]], id='line_b')
            for object_id, points in [(None, [[-0.47368421052631593, 0.231578947368421]]), (None, [[1.3851042190181628, -1.0695729533127138]]), (None, [[1.5831322225070208, 0.7457830556267552]])]:
                c.point(points, id=object_id, zorder=10, s=[50], facecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]], edgecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]])
            return c.save(output_path)

    def draw_C06(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane111_C06.png'
        with Canvas(PLANE, xlim=(-2.8255813953488373, 2.8255813953488373), ylim=(-2.9255813953488374, 2.7255813953488373), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
            c.circle([0.0, 0.0], 1.75, id='circle', fill=False)
            c.line([[-2.7, -0.32500000000000007], [2.7, 1.025]], id='line_a')
            c.line([[-2.7, 1.7899999999999998], [2.7, -1.99]], id='line_b')
            for object_id, points in [(None, [[-1.4790639505617877, 0.9353447653932512]]), (None, [[1.3851042190181628, -1.0695729533127138]]), (None, [[1.5831322225070208, 0.7457830556267552]])]:
                c.point(points, id=object_id, zorder=10, s=[50], facecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]], edgecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]])
            return c.save(output_path)

    def draw_C07(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane111_C07.png'
        with Canvas(PLANE, xlim=(-2.8255813953488373, 2.8255813953488373), ylim=(-2.9255813953488374, 2.7255813953488373), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
            c.circle([0.0, 0.0], 1.75, id='circle', fill=False)
            c.line([[-2.7, -0.32500000000000007], [2.7, 1.025]], id='line_a')
            c.line([[-2.7, 1.7899999999999998], [2.7, -1.99]], id='line_b')
            for object_id, points in [(None, [[-1.4790639505617877, 0.9353447653932512]]), (None, [[-0.47368421052631593, 0.231578947368421]]), (None, [[1.5831322225070208, 0.7457830556267552]])]:
                c.point(points, id=object_id, zorder=10, s=[50], facecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]], edgecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]])
            return c.save(output_path)

    def draw_C08(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane111_C08.png'
        with Canvas(PLANE, xlim=(-2.8255813953488373, 2.8255813953488373), ylim=(-2.9255813953488374, 2.7255813953488373), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
            c.circle([0.0, 0.0], 1.75, id='circle', fill=False)
            c.line([[-2.7, -0.32500000000000007], [2.7, 1.025]], id='line_a')
            c.line([[-2.7, 1.7899999999999998], [2.7, -1.99]], id='line_b')
            for object_id, points in [(None, [[-1.4790639505617877, 0.9353447653932512]]), (None, [[-0.47368421052631593, 0.231578947368421]]), (None, [[1.3851042190181628, -1.0695729533127138]])]:
                c.point(points, id=object_id, zorder=10, s=[50], facecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]], edgecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]])
            return c.save(output_path)
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Plane111')
    parser.add_argument('output', nargs='?')
    parser.add_argument('--variant', choices=('C01', 'C02', 'C03', 'C04', 'C05', 'C06', 'C07', 'C08'))
    args = parser.parse_args()
    print(Plane111().draw(args.output, variant=args.variant))
