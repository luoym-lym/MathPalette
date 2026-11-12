"""Collected question Ana550; construction on the shared drawing protocol."""
from pathlib import Path
import sys
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from MathPalette_Dataset.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Ana550:
    variants = ('C01', 'C02')

    def __init__(self):
        self.id = 'Ana550'
        self.source_dataset = 'Author Designed'
        self.source_key = 'author_special20_20261111/Ana550'
        self.question = 'The graph defines f on its displayed closed domain. Find all real solutions of |f(x)|=2.'
        self.answer = '{-5,-3,-1,1,3,5}'
        self.answer_type = 'expression'
        self.query = self.question

    def draw(self, output_path=None, *, variant=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if variant not in self.variants:
                raise ValueError('Unknown Special variant: ' + str(variant))
            return getattr(self, 'draw_' + variant)(output_path)
        with Canvas(ANALYTICS, xlim=[-8, 8], ylim=[-8, 8]) as c:
            c.line([[-6, 4], [-4, 0], [-2, -4], [0, 0], [2, 4], [4, 0], [6, -4]], id='object_000', solid_capstyle='butt')
            c.point([[-6, 4], [6, -4]], filled=True, id='object_001')
            c.text('$f$', [6.5, -4.2])
            return c.save(output_path)

    def draw_C01(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Ana550_C01.png'
        with Canvas(ANALYTICS, xlim=(-8.0, 8.0), ylim=(-8.0, 8.0), axes_position=(0.12, 0.12, 0.8, 0.8), coordinate_axes=True) as c:
            c.line([[-6.0, 4.0], [-4.0, 0.0], [-2.0, -4.0], [0.0, 0.0], [2.0, 4.0], [4.0, 0.0], [6.0, -4.0]], id='curve_001', solid_capstyle='butt')
            c.point([[-6.0, 4.0], [6.0, -4.0]], id='point_001')
            c.text('$f$', (6.5, -4.2), id='text_001', rotation_mode='default')
            c.line([[-8, 2], [8, 2]], zorder=9, color='#2563EB', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            for object_id, points in [(None, [[-5.0, 2.0]]), (None, [[1.0, 2.0]]), (None, [[3.0, 2.0]])]:
                c.point(points, id=object_id, zorder=10, s=[50], facecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]], edgecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]])
            c.line([[-8, -2], [2, -2]], zorder=9, color='#2563EB', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            c.point([[-3.0, -2.0]], zorder=10, s=[50], facecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]], edgecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]])
            c.point([[-1.0, -2.0]], zorder=10, s=[50], facecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]], edgecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]])
            return c.save(output_path)

    def draw_C02(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Ana550_C02.png'
        with Canvas(ANALYTICS, xlim=(-8.0, 8.0), ylim=(-8.0, 8.0), axes_position=(0.12, 0.12, 0.8, 0.8), coordinate_axes=True) as c:
            c.line([[-6.0, 4.0], [-4.0, 0.0], [-2.0, -4.0], [0.0, 0.0], [2.0, 4.0], [4.0, 0.0], [6.0, -4.0]], id='curve_001', solid_capstyle='butt')
            c.point([[-6.0, 4.0], [6.0, -4.0]], id='point_001')
            c.text('$f$', (6.5, -4.2), id='text_001', rotation_mode='default')
            c.line([[-8, 2], [2, 2]], zorder=9, color='#2563EB', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            c.line([[-8, -3], [8, -3]], zorder=9, color='#2563EB', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            for object_id, points in [(None, [[-5.0, 2.0]]), (None, [[1.0, 2.0]]), (None, [[-2.502582, -2.988995]]), (None, [[-1.489674, -2.989504]]), (None, [[5.513383, -2.968274]])]:
                c.point(points, id=object_id, zorder=10, s=[50], facecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]], edgecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]])
            return c.save(output_path)
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Ana550')
    parser.add_argument('output', nargs='?')
    parser.add_argument('--variant', choices=('C01', 'C02'))
    args = parser.parse_args()
    print(Ana550().draw(args.output, variant=args.variant))
