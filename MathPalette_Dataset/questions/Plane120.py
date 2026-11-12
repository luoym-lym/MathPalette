"""Collected question Plane120; construction on the shared drawing protocol."""
from pathlib import Path
import sys
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from MathPalette_Dataset.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane120:
    variants = ('C01',)

    def __init__(self):
        self.id = 'Plane120'
        self.source_dataset = 'Author Designed'
        self.source_key = 'structure-count:open-path-turns'
        self.question = 'How many times does the direction change along the polygonal path from P to Q?'
        self.answer = 5
        self.answer_type = 'number'
        self.query = self.question
        self.points = {'P': [-4.0, -2.0], 'T1': [-2.8, -0.3], 'T2': [-0.8, -0.3], 'T3': [0.2, 1.6], 'T4': [2.1, 1.6], 'T5': [2.1, -0.9], 'Q': [4.0, -0.9]}

    def draw(self, output_path=None, *, variant=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if variant not in self.variants:
                raise ValueError('Unknown Special variant: ' + str(variant))
            return getattr(self, 'draw_' + variant)(output_path)
        with Canvas(PLANE, xlim=[-4.6457628047975135, 4.61567021220492], ylim=[-5.00564200460506, 4.255791012397373]) as c:
            for object_id, points in [('edge_00', [self.points['P'], self.points['T1']]), ('edge_01', [self.points['T1'], self.points['T2']]), ('edge_02', [self.points['T2'], self.points['T3']]), ('edge_03', [self.points['T3'], self.points['T4']]), ('edge_04', [self.points['T4'], self.points['T5']]), ('edge_05', [self.points['T5'], self.points['Q']])]:
                c.line(points, id=object_id)
            c.text('P', self.points['P'], offset_pt=[-18.0, -16.0], vertex=True, id='label_P')
            c.text('Q', self.points['Q'], offset_pt=[15.0, 13.0], vertex=True, id='label_Q')
            return c.save(output_path)

    def draw_C01(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane120_C01.png'
        with Canvas(PLANE, xlim=(-4.6457628047975135, 4.61567021220492), ylim=(-5.00564200460506, 4.255791012397373), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
            for object_id, points in [('edge_00', [[-4.0, -2.0], [-2.8, -0.3]]), ('edge_01', [[-2.8, -0.3], [-0.8, -0.3]]), ('edge_02', [[-0.8, -0.3], [0.2, 1.6]]), ('edge_03', [[0.2, 1.6], [2.1, 1.6]]), ('edge_04', [[2.1, 1.6], [2.1, -0.9]]), ('edge_05', [[2.1, -0.9], [4.0, -0.9]])]:
                c.line(points, id=object_id)
            c.text('P', (-4.0, -2.0), id='label_P', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(-18.0, -16.0), annotation_clip=None)
            c.text('Q', (4.0, -0.9), id='label_Q', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(15.0, 13.0), annotation_clip=None)
            for object_id, points in [(None, [[-2.8, -0.3]]), (None, [[-0.8, -0.3]]), (None, [[0.2, 1.6]]), (None, [[2.1, 1.6]]), (None, [[2.1, -0.9]]), (None, [[1.1500000000000001, 1.6]])]:
                c.point(points, id=object_id, zorder=10, s=[50], facecolors=[[0.08627450980392157, 0.6392156862745098, 0.2901960784313726, 1.0]], edgecolors=[[0.08627450980392157, 0.6392156862745098, 0.2901960784313726, 1.0]])
            return c.save(output_path)
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Plane120')
    parser.add_argument('output', nargs='?')
    parser.add_argument('--variant', choices=('C01',))
    args = parser.parse_args()
    print(Plane120().draw(args.output, variant=args.variant))
