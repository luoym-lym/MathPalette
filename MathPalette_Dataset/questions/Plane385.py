"""Collected question Plane385; construction on the shared drawing protocol."""
from pathlib import Path
import sys
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from MathPalette_Dataset.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane385:
    variants = ('C01', 'C02', 'C03')

    def __init__(self):
        self.id = 'Plane385'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:1552'
        self.question = 'How many different squares can be drawn in total by joining the dots with line segments in the part of the square lattice as shown on the right?'
        self.answer = '4'
        self.answer_type = 'number'
        self.query = self.question
        self.points = {'P01': [0, 1], 'P02': [0, 2], 'P10': [1, 0], 'P11': [1, 1], 'P12': [1, 2], 'P20': [2, 0], 'P21': [2, 1], 'P22': [2, 2]}

    def draw(self, output_path=None, *, variant=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if variant not in self.variants:
                raise ValueError('Unknown Special variant: ' + str(variant))
            return getattr(self, 'draw_' + variant)(output_path)
        with Canvas(PLANE, xlim=[-0.06345872833283672, 2.066791119596469], ylim=[-0.06679111959646866, 2.063458728332837]) as c:
            for object_id, points in [('dotP01', [self.points['P01']]), ('dotP02', [self.points['P02']]), ('dotP10', [self.points['P10']]), ('dotP11', [self.points['P11']]), ('dotP12', [self.points['P12']]), ('dotP20', [self.points['P20']]), ('dotP21', [self.points['P21']]), ('dotP22', [self.points['P22']])]:
                c.point(points, id=object_id, filled=True)
            return c.save(output_path)

    def draw_C01(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane385_C01.png'
        with Canvas(PLANE, xlim=(-0.06345872833283672, 2.066791119596469), ylim=(-0.06679111959646866, 2.063458728332837), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
            for object_id, points in [('dotP01', [[0.0, 1.0]]), ('dotP02', [[0.0, 2.0]]), ('dotP10', [[1.0, 0.0]]), ('dotP11', [[1.0, 1.0]]), ('dotP12', [[1.0, 2.0]]), ('dotP20', [[2.0, 0.0]]), ('dotP21', [[2.0, 1.0]]), ('dotP22', [[2.0, 2.0]])]:
                c.point(points, id=object_id)
            for object_id, points in [(None, [[0, 2], [0, 1]]), (None, [[0, 1], [1, 1]]), (None, [[1, 1], [1, 2]]), (None, [[1, 2], [0, 2]]), (None, [[1, 1], [1, 0]]), (None, [[1, 0], [2, 0]]), (None, [[2, 0], [2, 1]]), (None, [[2, 1], [1, 1]])]:
                c.line(points, id=object_id, zorder=9, color='#2563EB', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            c.line([[1, 2], [2, 2]], zorder=9, color='#DC2626', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            c.line([[2, 2], [2, 1]], zorder=9, color='#DC2626', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            return c.save(output_path)

    def draw_C02(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane385_C02.png'
        with Canvas(PLANE, xlim=(-0.06345872833283672, 2.066791119596469), ylim=(-0.06679111959646866, 2.063458728332837), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
            for object_id, points in [('dotP01', [[0.0, 1.0]]), ('dotP02', [[0.0, 2.0]]), ('dotP10', [[1.0, 0.0]]), ('dotP11', [[1.0, 1.0]]), ('dotP12', [[1.0, 2.0]]), ('dotP20', [[2.0, 0.0]]), ('dotP21', [[2.0, 1.0]]), ('dotP22', [[2.0, 2.0]])]:
                c.point(points, id=object_id)
            for object_id, points in [(None, [[0, 2], [2, 2]]), (None, [[2, 2], [2, 0]]), (None, [[2, 0], [1, 0]]), (None, [[1, 0], [1, 1]]), (None, [[1, 1], [0, 1]]), (None, [[0, 1], [0, 2]]), (None, [[1, 2], [1, 1]]), (None, [[1, 1], [2, 1]])]:
                c.line(points, id=object_id, zorder=9, color='#EA580C', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            return c.save(output_path)

    def draw_C03(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane385_C03.png'
        with Canvas(PLANE, xlim=(-0.06345872833283672, 2.066791119596469), ylim=(-0.06679111959646866, 2.063458728332837), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
            for object_id, points in [('dotP01', [[0.0, 1.0]]), ('dotP02', [[0.0, 2.0]]), ('dotP10', [[1.0, 0.0]]), ('dotP11', [[1.0, 1.0]]), ('dotP12', [[1.0, 2.0]]), ('dotP20', [[2.0, 0.0]]), ('dotP21', [[2.0, 1.0]]), ('dotP22', [[2.0, 2.0]])]:
                c.point(points, id=object_id)
            for object_id, points in [(None, [[0, 2], [2, 2]]), (None, [[2, 2], [2, 0]]), (None, [[2, 0], [1, 0]]), (None, [[1, 0], [1, 1]]), (None, [[1, 1], [0, 1]]), (None, [[0, 1], [0, 2]]), (None, [[1, 2], [1, 1]]), (None, [[2, 1], [1, 1]])]:
                c.line(points, id=object_id, zorder=9, color='#16A34A', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            return c.save(output_path)
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Plane385')
    parser.add_argument('output', nargs='?')
    parser.add_argument('--variant', choices=('C01', 'C02', 'C03'))
    args = parser.parse_args()
    print(Plane385().draw(args.output, variant=args.variant))
