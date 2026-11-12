"""Collected question Ana21; construction on the shared drawing protocol."""
from pathlib import Path
import sys
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from MathPalette_Dataset.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Ana21:
    variants = ('C01', 'C02', 'C03', 'C04', 'C05')

    def __init__(self):
        self.id = 'Ana21'
        self.source_dataset = 'MathVerse'
        self.source_key = 's2164'
        self.question = 'Find the coordinates of the midpoint of the rectangle diagonals.'
        self.answer = '(2,2)'
        self.answer_type = 'expression'
        self.query = self.question

    def draw(self, output_path=None, *, variant=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if variant not in self.variants:
                raise ValueError('Unknown Special variant: ' + str(variant))
            return getattr(self, 'draw_' + variant)(output_path)
        with Canvas(ANALYTICS, xlim=[-8.0, 8.0], ylim=[-8.0, 8.0], axes_position=[0.12, 0.12, 0.8, 0.8], coordinate_axes=True) as c:
            c.line([[-2, 6], [6, 6], [6, -2], [-2, -2], [-2, 6]], id='curve_001', solid_capstyle='projecting')
            return c.save(output_path)

    def draw_C01(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Ana21_C01.png'
        with Canvas(ANALYTICS, xlim=(-8.0, 8.0), ylim=(-8.0, 8.0), axes_position=(0.12, 0.12, 0.8, 0.8), coordinate_axes=True) as c:
            c.line([[-2, 6], [6, 6], [6, -2], [-2, -2], [-2, 6]], id='curve_001', solid_capstyle='projecting')
            c.point([[2.0, 3.0]], zorder=10, s=[50], facecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]], edgecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]])
            return c.save(output_path)

    def draw_C02(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Ana21_C02.png'
        with Canvas(ANALYTICS, xlim=(-8.0, 8.0), ylim=(-8.0, 8.0), axes_position=(0.12, 0.12, 0.8, 0.8), coordinate_axes=True) as c:
            c.line([[-2, 6], [6, 6], [6, -2], [-2, -2], [-2, 6]], id='curve_001', solid_capstyle='projecting')
            for object_id, points in [(None, [[-1.0, 6.0]]), (None, [[-1.0, -2.0]]), (None, [[6.0, -2.0]]), (None, [[6.0, 6.0]])]:
                c.point(points, id=object_id, zorder=10, s=[50], facecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]], edgecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]])
            return c.save(output_path)

    def draw_C03(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Ana21_C03.png'
        with Canvas(ANALYTICS, xlim=(-8.0, 8.0), ylim=(-8.0, 8.0), axes_position=(0.12, 0.12, 0.8, 0.8), coordinate_axes=True) as c:
            c.line([[-2, 6], [6, 6], [6, -2], [-2, -2], [-2, 6]], id='curve_001', solid_capstyle='projecting')
            for object_id, points in [(None, [[-2.0, 5.0]]), (None, [[6.0, 5.0]]), (None, [[6.0, -2.0]]), (None, [[-2.0, -2.0]])]:
                c.point(points, id=object_id, zorder=10, s=[50], facecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]], edgecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]])
            return c.save(output_path)

    def draw_C04(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Ana21_C04.png'
        with Canvas(ANALYTICS, xlim=(-8.0, 8.0), ylim=(-8.0, 8.0), axes_position=(0.12, 0.12, 0.8, 0.8), coordinate_axes=True) as c:
            c.line([[-2, 6], [6, 6], [6, -2], [-2, -2], [-2, 6]], id='curve_001', solid_capstyle='projecting')
            for object_id, points in [(None, [[-2.0, 6.0]]), (None, [[-2.0, -2.0]]), (None, [[5.0, -2.0]]), (None, [[5.0, 6.0]])]:
                c.point(points, id=object_id, zorder=10, s=[50], facecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]], edgecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]])
            return c.save(output_path)

    def draw_C05(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Ana21_C05.png'
        with Canvas(ANALYTICS, xlim=(-8.0, 8.0), ylim=(-8.0, 8.0), axes_position=(0.12, 0.12, 0.8, 0.8), coordinate_axes=True) as c:
            c.line([[-2, 6], [6, 6], [6, -2], [-2, -2], [-2, 6]], id='curve_001', solid_capstyle='projecting')
            for object_id, points in [(None, [[-2.0, 6.0]]), (None, [[6.0, 6.0]]), (None, [[6.0, -1.0]]), (None, [[-2.0, -1.0]])]:
                c.point(points, id=object_id, zorder=10, s=[50], facecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]], edgecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]])
            return c.save(output_path)
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Ana21')
    parser.add_argument('output', nargs='?')
    parser.add_argument('--variant', choices=('C01', 'C02', 'C03', 'C04', 'C05'))
    args = parser.parse_args()
    print(Ana21().draw(args.output, variant=args.variant))
