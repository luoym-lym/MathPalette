"""Collected question Plane485; construction on the shared drawing protocol."""
from pathlib import Path
import sys
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from MathPalette_Dataset.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane485:
    variants = ('C01', 'C02')

    def __init__(self):
        self.id = 'Plane485'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:2845'
        self.question = 'What is the maximum number of $T$-shaped polyominos (shown below) that can be placed in a $6 \\times 6$ grid without any overlaps? The blocks can be rotated.'
        self.answer = '8'
        self.answer_type = 'number'
        self.query = self.question
        self.points = {'tile00': [0, 1],
         'tile01': [1, 1],
         'tile02': [1, 2],
         'tile03': [0, 2],
         'tile10': [1, 1],
         'tile11': [2, 1],
         'tile12': [2, 2],
         'tile13': [1, 2],
         'tile20': [2, 1],
         'tile21': [3, 1],
         'tile22': [3, 2],
         'tile23': [2, 2],
         'tile30': [1, 0],
         'tile31': [2, 0],
         'tile32': [2, 1],
         'tile33': [1, 1]}

    def draw(self, output_path=None, *, variant=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if variant not in self.variants:
                raise ValueError('Unknown Special variant: ' + str(variant))
            return getattr(self, 'draw_' + variant)(output_path)
        with Canvas(PLANE, xlim=[-0.07435006984377468, 3.079344978439784], ylim=[-0.577058547025228, 2.576636501258331]) as c:
            for object_id, vertices, codes in [('tile0', [self.points['tile00'], self.points['tile01'], self.points['tile02'], self.points['tile03'], self.points['tile00']], [1, 2, 2, 2, 79]), ('tile1', [self.points['tile10'], self.points['tile11'], self.points['tile12'], self.points['tile13'], self.points['tile10']], [1, 2, 2, 2, 79]), ('tile2', [self.points['tile20'], self.points['tile21'], self.points['tile22'], self.points['tile23'], self.points['tile20']], [1, 2, 2, 2, 79]), ('tile3', [self.points['tile30'], self.points['tile31'], self.points['tile32'], self.points['tile33'], self.points['tile30']], [1, 2, 2, 2, 79])]:
                c.path(vertices, codes, id=object_id)
            return c.save(output_path)

    def draw_C01(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane485_C01.png'
        with Canvas(PLANE, xlim=(-0.07435006984377468, 3.079344978439784), ylim=(-0.577058547025228, 2.576636501258331), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
            for object_id, vertices, codes in [('tile0', [[0.0, 1.0], [1.0, 1.0], [1.0, 2.0], [0.0, 2.0], [0.0, 1.0]], [1, 2, 2, 2, 79]), ('tile1', [[1.0, 1.0], [2.0, 1.0], [2.0, 2.0], [1.0, 2.0], [1.0, 1.0]], [1, 2, 2, 2, 79]), ('tile2', [[2.0, 1.0], [3.0, 1.0], [3.0, 2.0], [2.0, 2.0], [2.0, 1.0]], [1, 2, 2, 2, 79]), ('tile3', [[1.0, 0.0], [2.0, 0.0], [2.0, 1.0], [1.0, 1.0], [1.0, 0.0]], [1, 2, 2, 2, 79])]:
                c.path(vertices, codes, id=object_id, capstyle='butt')
            for object_id, points in [(None, [[0.48476089868362093, 1.5440847932520925]]), (None, [[1.5411456779289308, 1.5118779402263207]]), (None, [[1.5186008808108904, 0.43938973446812524]]), (None, [[2.52989606582012, 1.5054365696211662]])]:
                c.point(points, id=object_id, zorder=10, s=[50], facecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]], edgecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]])
            return c.save(output_path)

    def draw_C02(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane485_C02.png'
        with Canvas(PLANE, xlim=(-0.07435006984377468, 3.079344978439784), ylim=(-0.577058547025228, 2.576636501258331), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
            for object_id, vertices, codes in [('tile0', [[0.0, 1.0], [1.0, 1.0], [1.0, 2.0], [0.0, 2.0], [0.0, 1.0]], [1, 2, 2, 2, 79]), ('tile1', [[1.0, 1.0], [2.0, 1.0], [2.0, 2.0], [1.0, 2.0], [1.0, 1.0]], [1, 2, 2, 2, 79]), ('tile2', [[2.0, 1.0], [3.0, 1.0], [3.0, 2.0], [2.0, 2.0], [2.0, 1.0]], [1, 2, 2, 2, 79])]:
                c.path(vertices, codes, id=object_id, edgecolor=(0.1450980392156863, 0.38823529411764707, 0.9215686274509803, 1.0), capstyle='butt')
            c.path([[1.0, 0.0], [2.0, 0.0], [2.0, 1.0], [1.0, 1.0], [1.0, 0.0]], [1, 2, 2, 2, 79], id='tile3', edgecolor=(0.08627450980392157, 0.6392156862745098, 0.2901960784313726, 1.0), capstyle='butt')
            return c.save(output_path)
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Plane485')
    parser.add_argument('output', nargs='?')
    parser.add_argument('--variant', choices=('C01', 'C02'))
    args = parser.parse_args()
    print(Plane485().draw(args.output, variant=args.variant))
