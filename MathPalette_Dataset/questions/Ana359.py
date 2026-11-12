"""Collected question Ana359; construction on the shared drawing protocol."""
from pathlib import Path
import sys
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from MathPalette_Dataset.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Ana359:
    variants = ('C01',)

    def __init__(self):
        self.id = 'Ana359'
        self.source_dataset = 'We-Math2.0-Standard'
        self.source_key = 'standard/5402'
        self.question = 'P moves along the plotted line l. Find the minimum of MP+NP. Read positions from the unit grid.'
        self.answer = '5*sqrt(2)'
        self.answer_type = 'number'
        self.query = self.question

    def draw(self, output_path=None, *, variant=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if variant not in self.variants:
                raise ValueError('Unknown Special variant: ' + str(variant))
            return getattr(self, 'draw_' + variant)(output_path)
        with Canvas(ANALYTICS, xlim=[-8, 8], ylim=[-8, 8], xlabel='x', ylabel='y') as c:
            c.point([[-2, 3]], filled=True, id='object_000')
            c.point([[3, 2]], filled=True, id='object_001')
            for object_id, text, anchor in [(None, 'M', [-1.78, 3.25]), (None, 'N', [3.22, 2.25]), (None, 'l', [6.5, 0.35])]:
                c.text(text, anchor, id=object_id, ha='left', va='bottom')
            return c.save(output_path)

    def draw_C01(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Ana359_C01.png'
        with Canvas(ANALYTICS, xlim=(-8.0, 8.0), ylim=(-8.0, 8.0), axes_position=(0.12, 0.12, 0.8, 0.8), coordinate_axes=True) as c:
            c.point([[-2.0, 3.0]], id='point_001')
            c.point([[3.0, 2.0]], id='point_002')
            for object_id, text, anchor in [('text_001', 'M', (-1.78, 3.25)), ('text_002', 'N', (3.22, 2.25)), ('text_003', 'l', (6.5, 0.35))]:
                c.text(text, anchor, id=object_id, ha='left', va='bottom', rotation_mode='default')
            for object_id, points in [(None, [[-2, 3], [-2, -3]]), (None, [[-2, -3], [3, 1]]), (None, [[-2.0, 3.0], [1.640082, -0.008016]])]:
                c.line(points, id=object_id, zorder=9, color='#2563EB', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            c.point([[-2.0, -3.0]], zorder=10, s=[50], facecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]], edgecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]])
            return c.save(output_path)
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Ana359')
    parser.add_argument('output', nargs='?')
    parser.add_argument('--variant', choices=('C01',))
    args = parser.parse_args()
    print(Ana359().draw(args.output, variant=args.variant))
