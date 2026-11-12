"""Collected question Plane462; construction on the shared drawing protocol."""
from pathlib import Path
import sys
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from MathPalette_Dataset.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane462:
    variants = ('C01', 'C02')

    def __init__(self):
        self.id = 'Plane462'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:2620'
        self.question = 'Consider these two geoboard quadrilaterals. Which of the following statements is true?\n\nChoices:\nA:$\\text{The area of quadrilateral I is more than the area of quadrilateral II.}$\nB:$\\text{The area of quadrilateral I is less than the area of quadrilateral II.}$\nC:$\\text{The quadrilaterals have the same area and the same perimeter.}$\nD:$\\text{The quadrilaterals have the same area, but the perimeter of I is more than the perimeter of II.}$\nE:$\\text{The quadrilaterals have the same area, but the perimeter of I is less than the perimeter of II.}$'
        self.answer = 'E'
        self.answer_type = 'choice'
        self.choices = {'A': '$\\text{The area of quadrilateral I is more than the area of quadrilateral II.}$',
         'B': '$\\text{The area of quadrilateral I is less than the area of quadrilateral II.}$',
         'C': '$\\text{The quadrilaterals have the same area and the same perimeter.}$',
         'D': '$\\text{The quadrilaterals have the same area, but the perimeter of I is more than the '
              'perimeter of II.}$',
         'E': '$\\text{The quadrilaterals have the same area, but the perimeter of I is less than the '
              'perimeter of II.}$'}
        self.query = self.question
        self.points = {'p00': [0, 0],
         'p01': [0, 1],
         'p02': [0, 2],
         'p03': [0, 3],
         'p04': [0, 4],
         'p10': [1, 0],
         'p11': [1, 1],
         'p12': [1, 2],
         'p13': [1, 3],
         'p14': [1, 4],
         'p20': [2, 0],
         'p21': [2, 1],
         'p22': [2, 2],
         'p23': [2, 3],
         'p24': [2, 4],
         'p30': [3, 0],
         'p31': [3, 1],
         'p32': [3, 2],
         'p33': [3, 3],
         'p34': [3, 4],
         'p40': [4, 0],
         'p41': [4, 1],
         'p42': [4, 2],
         'p43': [4, 3],
         'p44': [4, 4],
         'labI': [0.55, 2.95],
         'labII': [2.65, 0.95]}

    def draw(self, output_path=None, *, variant=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if variant not in self.variants:
                raise ValueError('Unknown Special variant: ' + str(variant))
            return getattr(self, 'draw_' + variant)(output_path)
        with Canvas(PLANE, xlim=[-0.12691745666567344, 4.133582239192938], ylim=[-0.13358223919293732, 4.126917456665674]) as c:
            for object_id, points in [('p00', [self.points['p00']]), ('p01', [self.points['p01']]), ('p02', [self.points['p02']]), ('p03', [self.points['p03']]), ('p04', [self.points['p04']]), ('p10', [self.points['p10']]), ('p11', [self.points['p11']]), ('p12', [self.points['p12']]), ('p13', [self.points['p13']]), ('p14', [self.points['p14']]), ('p20', [self.points['p20']]), ('p21', [self.points['p21']]), ('p22', [self.points['p22']]), ('p23', [self.points['p23']]), ('p24', [self.points['p24']]), ('p30', [self.points['p30']]), ('p31', [self.points['p31']]), ('p32', [self.points['p32']]), ('p33', [self.points['p33']]), ('p34', [self.points['p34']]), ('p40', [self.points['p40']]), ('p41', [self.points['p41']]), ('p42', [self.points['p42']]), ('p43', [self.points['p43']]), ('p44', [self.points['p44']])]:
                c.point(points, id=object_id, filled=True)
            c.path([self.points['p04'], self.points['p13'], self.points['p12'], self.points['p03'], self.points['p04']], [1, 2, 2, 2, 79], id='I')
            c.path([self.points['p21'], self.points['p42'], self.points['p31'], self.points['p30'], self.points['p21']], [1, 2, 2, 2, 79], id='II')
            c.text('I', self.points['labI'], offset_pt=[0, 0], vertex=False, id='nameI')
            c.text('II', self.points['labII'], offset_pt=[0, 0], vertex=False, id='nameII')
            return c.save(output_path)

    def draw_C01(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane462_C01.png'
        _geometry_01 = [('p00', [[0.0, 0.0]]),
         ('p01', [[0.0, 1.0]]),
         ('p02', [[0.0, 2.0]]),
         ('p03', [[0.0, 3.0]]),
         ('p04', [[0.0, 4.0]]),
         ('p10', [[1.0, 0.0]]),
         ('p11', [[1.0, 1.0]]),
         ('p12', [[1.0, 2.0]]),
         ('p13', [[1.0, 3.0]]),
         ('p14', [[1.0, 4.0]]),
         ('p20', [[2.0, 0.0]]),
         ('p21', [[2.0, 1.0]]),
         ('p22', [[2.0, 2.0]]),
         ('p23', [[2.0, 3.0]]),
         ('p24', [[2.0, 4.0]]),
         ('p30', [[3.0, 0.0]]),
         ('p31', [[3.0, 1.0]]),
         ('p32', [[3.0, 2.0]]),
         ('p33', [[3.0, 3.0]]),
         ('p34', [[3.0, 4.0]]),
         ('p40', [[4.0, 0.0]]),
         ('p41', [[4.0, 1.0]]),
         ('p42', [[4.0, 2.0]]),
         ('p43', [[4.0, 3.0]]),
         ('p44', [[4.0, 4.0]])]
        with Canvas(PLANE, xlim=(-0.12691745666567344, 4.133582239192938), ylim=(-0.13358223919293732, 4.126917456665674), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
            for object_id, points in _geometry_01:
                c.point(points, id=object_id)
            c.path([[0.0, 4.0], [1.0, 3.0], [1.0, 2.0], [0.0, 3.0], [0.0, 4.0]], [1, 2, 2, 2, 79], id='I', capstyle='butt')
            c.path([[2.0, 1.0], [4.0, 2.0], [3.0, 1.0], [3.0, 0.0], [2.0, 1.0]], [1, 2, 2, 2, 79], id='II', capstyle='butt')
            c.text('I', (0.55, 2.95), id='nameI', rotation_mode='default', offset_pt=(0, 0), annotation_clip=None)
            c.text('II', (2.65, 0.95), id='nameII', rotation_mode='default', offset_pt=(0, 0), annotation_clip=None)
            for object_id, points in [(None, [[2, 2], [4, 2]]), (None, [[4, 2], [4, 0]]), (None, [[4, 0], [2, 0]]), (None, [[2, 0], [2, 2]])]:
                c.line(points, id=object_id, zorder=9, color='#2563EB', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            return c.save(output_path)

    def draw_C02(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane462_C02.png'
        _geometry_01 = [('p00', [[0.0, 0.0]]),
         ('p01', [[0.0, 1.0]]),
         ('p02', [[0.0, 2.0]]),
         ('p03', [[0.0, 3.0]]),
         ('p04', [[0.0, 4.0]]),
         ('p10', [[1.0, 0.0]]),
         ('p11', [[1.0, 1.0]]),
         ('p12', [[1.0, 2.0]]),
         ('p13', [[1.0, 3.0]]),
         ('p14', [[1.0, 4.0]]),
         ('p20', [[2.0, 0.0]]),
         ('p21', [[2.0, 1.0]]),
         ('p22', [[2.0, 2.0]]),
         ('p23', [[2.0, 3.0]]),
         ('p24', [[2.0, 4.0]]),
         ('p30', [[3.0, 0.0]]),
         ('p31', [[3.0, 1.0]]),
         ('p32', [[3.0, 2.0]]),
         ('p33', [[3.0, 3.0]]),
         ('p34', [[3.0, 4.0]]),
         ('p40', [[4.0, 0.0]]),
         ('p41', [[4.0, 1.0]]),
         ('p42', [[4.0, 2.0]]),
         ('p43', [[4.0, 3.0]]),
         ('p44', [[4.0, 4.0]])]
        with Canvas(PLANE, xlim=(-0.12691745666567344, 4.133582239192938), ylim=(-0.13358223919293732, 4.126917456665674), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
            for object_id, points in _geometry_01:
                c.point(points, id=object_id)
            c.path([[0.0, 4.0], [1.0, 3.0], [1.0, 2.0], [0.0, 3.0], [0.0, 4.0]], [1, 2, 2, 2, 79], id='I', capstyle='butt')
            c.path([[2.0, 1.0], [4.0, 2.0], [3.0, 1.0], [3.0, 0.0], [2.0, 1.0]], [1, 2, 2, 2, 79], id='II', capstyle='butt')
            c.text('I', (0.55, 2.95), id='nameI', rotation_mode='default', offset_pt=(0, 0), annotation_clip=None)
            c.text('II', (2.65, 0.95), id='nameII', rotation_mode='default', offset_pt=(0, 0), annotation_clip=None)
            c.line([[2, 2], [4, 2]], zorder=9, color='#2563EB', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            c.line([[2, 2], [2, 1]], zorder=9, color='#2563EB', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            return c.save(output_path)
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Plane462')
    parser.add_argument('output', nargs='?')
    parser.add_argument('--variant', choices=('C01', 'C02'))
    args = parser.parse_args()
    print(Plane462().draw(args.output, variant=args.variant))
