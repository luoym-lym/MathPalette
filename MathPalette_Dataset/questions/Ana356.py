"""Collected question Ana356; construction on the shared drawing protocol."""
from pathlib import Path
import sys
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from MathPalette_Dataset.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Ana356:
    variants = ('C01', 'C02')

    def __init__(self):
        self.id = 'Ana356'
        self.source_dataset = 'We-Math2.0-Standard'
        self.source_key = 'standard/5399'
        self.question = 'Find the distance from L to the plotted oblique line. Read positions from the unit grid.'
        self.answer = '10/sqrt(5)'
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
            c.line([[-7, 2.5], [7, -4.5]], id='object_000', solid_capstyle='butt')
            c.point([[2, 3]], filled=True, id='object_001')
            c.text('L', [2.22, 3.25], ha='left', va='bottom')
            return c.save(output_path)

    def draw_C01(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Ana356_C01.png'
        with Canvas(ANALYTICS, xlim=(-8.0, 8.0), ylim=(-8.0, 8.0), axes_position=(0.12, 0.12, 0.8, 0.8), coordinate_axes=True) as c:
            c.line([[-7.0, 2.5], [7.0, -4.5]], id='curve_001', solid_capstyle='butt')
            c.point([[2.0, 3.0]], id='point_001')
            c.text('L', (2.22, 3.25), id='text_001', ha='left', va='bottom', rotation_mode='default')
            c.line([[2, 3], [0, -1]], zorder=9, color='#2563EB', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            c.point([[0.0, -1.0]], zorder=10, s=[50], facecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]], edgecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]])
            return c.save(output_path)

    def draw_C02(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Ana356_C02.png'
        with Canvas(ANALYTICS, xlim=(-8.0, 8.0), ylim=(-8.0, 8.0), axes_position=(0.12, 0.12, 0.8, 0.8), coordinate_axes=True) as c:
            c.line([[-7.0, 2.5], [7.0, -4.5]], id='curve_001', solid_capstyle='butt')
            c.point([[2.0, 3.0]], id='point_001')
            c.text('L', (2.22, 3.25), id='text_001', ha='left', va='bottom', rotation_mode='default')
            c.line([[2, 3], [-1, 0]], zorder=9, color='#2563EB', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            c.point([[-1.0, 0.0]], zorder=10, s=[50], facecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]], edgecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]])
            return c.save(output_path)
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Ana356')
    parser.add_argument('output', nargs='?')
    parser.add_argument('--variant', choices=('C01', 'C02'))
    args = parser.parse_args()
    print(Ana356().draw(args.output, variant=args.variant))
