"""Collected question Plane25; construction on the shared drawing protocol."""
from pathlib import Path
import sys
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from MathPalette_Dataset.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane25:
    variants = ('C01',)

    def __init__(self):
        self.id = 'Plane25'
        self.source_dataset = 'MathVista'
        self.source_key = 'testmini/102'
        self.question = 'The shape is made of unit squares. What is the area of the shape?'
        self.answer = '6'
        self.answer_type = 'number'
        self.query = self.question
        self.points = {'p00': [0.0, 0.0],
         'p01': [0.0, 1.0],
         'p02': [0.0, 2.0],
         'p03': [0.0, 3.0],
         'p10': [1.0, 0.0],
         'p11': [1.0, 1.0],
         'p12': [1.0, 2.0],
         'p13': [1.0, 3.0],
         'p20': [2.0, 0.0],
         'p21': [2.0, 1.0],
         'p22': [2.0, 2.0],
         'p23': [2.0, 3.0]}

    def draw(self, output_path=None, *, variant=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if variant not in self.variants:
                raise ValueError('Unknown Special variant: ' + str(variant))
            return getattr(self, 'draw_' + variant)(output_path)
        with Canvas(PLANE, xlim=[-0.5734572248750054, 2.5776993434716937], ylim=[-0.0776993434716935, 3.073457224875005]) as c:
            for object_id, points in [('o1', [self.points['p00'], self.points['p03']]), ('o2', [self.points['p10'], self.points['p13']]), ('o3', [self.points['p20'], self.points['p23']]), ('o4', [self.points['p00'], self.points['p20']]), ('o5', [self.points['p01'], self.points['p21']]), ('o6', [self.points['p02'], self.points['p22']]), ('o7', [self.points['p03'], self.points['p23']])]:
                c.line(points, id=object_id)
            return c.save(output_path)

    def draw_C01(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane25_C01.png'
        with Canvas(PLANE, xlim=(-0.5734572248750054, 2.5776993434716937), ylim=(-0.0776993434716935, 3.073457224875005), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
            for object_id, points in [('o1', [[0.0, 0.0], [0.0, 3.0]]), ('o2', [[1.0, 0.0], [1.0, 3.0]]), ('o3', [[2.0, 0.0], [2.0, 3.0]]), ('o4', [[0.0, 0.0], [2.0, 0.0]]), ('o5', [[0.0, 1.0], [2.0, 1.0]]), ('o6', [[0.0, 2.0], [2.0, 2.0]]), ('o7', [[0.0, 3.0], [2.0, 3.0]])]:
                c.line(points, id=object_id)
            c.line([[0.00451226008727712, 1.4817884761982516], [1.9997298585094105, 1.4785703832975705]], zorder=9, color='#2563EB', solid_capstyle='butt')
            return c.save(output_path)
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Plane25')
    parser.add_argument('output', nargs='?')
    parser.add_argument('--variant', choices=('C01',))
    args = parser.parse_args()
    print(Plane25().draw(args.output, variant=args.variant))
