"""Collected question Plane260; construction on the shared drawing protocol."""
from pathlib import Path
import sys
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from MathPalette_Dataset.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane260:
    variants = ('C01', 'C02')

    def __init__(self):
        self.id = 'Plane260'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:782'
        self.question = 'In the box are seven blocks. It is possible to slide the blocks around so that another block can be added to the box. What is the minimum number of blocks that must be moved?'
        self.answer = '2'
        self.answer_type = 'number'
        self.query = self.question

    def draw(self, output_path=None, *, variant=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if variant not in self.variants:
                raise ValueError('Unknown Special variant: ' + str(variant))
            return getattr(self, 'draw_' + variant)(output_path)
        with Canvas(PLANE, xlim=[-0.12667099149054195, 5.130592591748275], ylim=[-0.12979189053362905, 5.127471692705188], axes_position=[0.05, 0.05, 0.9, 0.9], coordinate_axes=False) as c:
            c.path([[0.0, 0.0], [5.0, 0.0], [5.0, 5.0], [0.0, 5.0], [0.0, 0.0]], [1, 2, 2, 2, 79], id='box', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[0.0, 0.0], [5.0, 0.0], [5.0, 5.0], [0.0, 5.0], [0.0, 0.0]], [1, 2, 2, 2, 79], id='box', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[1.045, 4.045], [3.955, 4.045], [3.955, 4.955], [1.045, 4.955], [1.045, 4.045]], [1, 2, 2, 2, 79], id='block0', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[1.045, 4.045], [3.955, 4.045], [3.955, 4.955], [1.045, 4.955], [1.045, 4.045]], [1, 2, 2, 2, 79], id='block0', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[4.045, 2.045], [4.955, 2.045], [4.955, 4.955], [4.045, 4.955], [4.045, 2.045]], [1, 2, 2, 2, 79], id='block1', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[4.045, 2.045], [4.955, 2.045], [4.955, 4.955], [4.045, 4.955], [4.045, 2.045]], [1, 2, 2, 2, 79], id='block1', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[0.045, 3.045], [2.955, 3.045], [2.955, 3.955], [0.045, 3.955], [0.045, 3.045]], [1, 2, 2, 2, 79], id='block2', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[0.045, 3.045], [2.955, 3.045], [2.955, 3.955], [0.045, 3.955], [0.045, 3.045]], [1, 2, 2, 2, 79], id='block2', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[3.045, 1.045], [3.955, 1.045], [3.955, 3.955], [3.045, 3.955], [3.045, 1.045]], [1, 2, 2, 2, 79], id='block3', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[3.045, 1.045], [3.955, 1.045], [3.955, 3.955], [3.045, 3.955], [3.045, 1.045]], [1, 2, 2, 2, 79], id='block3', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[0.045, 0.045], [0.955, 0.045], [0.955, 2.955], [0.045, 2.955], [0.045, 0.045]], [1, 2, 2, 2, 79], id='block4', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[0.045, 0.045], [0.955, 0.045], [0.955, 2.955], [0.045, 2.955], [0.045, 0.045]], [1, 2, 2, 2, 79], id='block4', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[1.045, 0.045], [1.955, 0.045], [1.955, 2.955], [1.045, 2.955], [1.045, 0.045]], [1, 2, 2, 2, 79], id='block5', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[1.045, 0.045], [1.955, 0.045], [1.955, 2.955], [1.045, 2.955], [1.045, 0.045]], [1, 2, 2, 2, 79], id='block5', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[2.045, 0.045], [4.955, 0.045], [4.955, 0.955], [2.045, 0.955], [2.045, 0.045]], [1, 2, 2, 2, 79], id='block6', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[2.045, 0.045], [4.955, 0.045], [4.955, 0.955], [2.045, 0.955], [2.045, 0.045]], [1, 2, 2, 2, 79], id='block6', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            return c.save(output_path)

    def draw_C01(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane260_C01.png'
        with Canvas(PLANE, xlim=(-0.12667099149054195, 5.130592591748275), ylim=(-0.12979189053362905, 5.127471692705188), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
            c.path([[0.0, 0.0], [5.0, 0.0], [5.0, 5.0], [0.0, 5.0], [0.0, 0.0]], [1, 2, 2, 2, 79], id='box', zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 1.0), linewidth=0.0, capstyle='butt')
            c.path([[0.0, 0.0], [5.0, 0.0], [5.0, 5.0], [0.0, 5.0], [0.0, 0.0]], [1, 2, 2, 2, 79], id='box', capstyle='butt', fill=False)
            c.path([[1.045, 4.045], [3.955, 4.045], [3.955, 4.955], [1.045, 4.955], [1.045, 4.045]], [1, 2, 2, 2, 79], id='block0', zorder=1, edgecolor='none', facecolor=(1.0, 1.0, 1.0, 1.0), linewidth=0.0, capstyle='butt')
            c.path([[1.045, 4.045], [3.955, 4.045], [3.955, 4.955], [1.045, 4.955], [1.045, 4.045]], [1, 2, 2, 2, 79], id='block0', capstyle='butt', fill=False)
            c.path([[4.045, 2.045], [4.955, 2.045], [4.955, 4.955], [4.045, 4.955], [4.045, 2.045]], [1, 2, 2, 2, 79], id='block1', zorder=1, edgecolor='none', facecolor=(1.0, 1.0, 1.0, 1.0), linewidth=0.0, capstyle='butt')
            c.path([[4.045, 2.045], [4.955, 2.045], [4.955, 4.955], [4.045, 4.955], [4.045, 2.045]], [1, 2, 2, 2, 79], id='block1', capstyle='butt', fill=False)
            c.path([[0.045, 3.045], [2.955, 3.045], [2.955, 3.955], [0.045, 3.955], [0.045, 3.045]], [1, 2, 2, 2, 79], id='block2', zorder=1, edgecolor='none', facecolor=(1.0, 1.0, 1.0, 1.0), linewidth=0.0, capstyle='butt')
            c.path([[0.045, 3.045], [2.955, 3.045], [2.955, 3.955], [0.045, 3.955], [0.045, 3.045]], [1, 2, 2, 2, 79], id='block2', capstyle='butt', fill=False)
            c.path([[3.045, 1.045], [3.955, 1.045], [3.955, 3.955], [3.045, 3.955], [3.045, 1.045]], [1, 2, 2, 2, 79], id='block3', zorder=1, edgecolor='none', facecolor=(1.0, 1.0, 1.0, 1.0), linewidth=0.0, capstyle='butt')
            c.path([[3.045, 1.045], [3.955, 1.045], [3.955, 3.955], [3.045, 3.955], [3.045, 1.045]], [1, 2, 2, 2, 79], id='block3', capstyle='butt', fill=False)
            c.path([[0.045, 0.045], [0.955, 0.045], [0.955, 2.955], [0.045, 2.955], [0.045, 0.045]], [1, 2, 2, 2, 79], id='block4', zorder=1, edgecolor='none', facecolor=(1.0, 1.0, 1.0, 1.0), linewidth=0.0, capstyle='butt')
            c.path([[0.045, 0.045], [0.955, 0.045], [0.955, 2.955], [0.045, 2.955], [0.045, 0.045]], [1, 2, 2, 2, 79], id='block4', capstyle='butt', fill=False)
            c.path([[1.045, 0.045], [1.955, 0.045], [1.955, 2.955], [1.045, 2.955], [1.045, 0.045]], [1, 2, 2, 2, 79], id='block5', zorder=1, edgecolor='none', facecolor=(1.0, 1.0, 1.0, 1.0), linewidth=0.0, capstyle='butt')
            c.path([[1.045, 0.045], [1.955, 0.045], [1.955, 2.955], [1.045, 2.955], [1.045, 0.045]], [1, 2, 2, 2, 79], id='block5', capstyle='butt', fill=False)
            c.path([[2.045, 0.045], [4.955, 0.045], [4.955, 0.955], [2.045, 0.955], [2.045, 0.045]], [1, 2, 2, 2, 79], id='block6', zorder=1, edgecolor='none', facecolor=(1.0, 1.0, 1.0, 1.0), linewidth=0.0, capstyle='butt')
            c.path([[2.045, 0.045], [4.955, 0.045], [4.955, 0.955], [2.045, 0.955], [2.045, 0.045]], [1, 2, 2, 2, 79], id='block6', capstyle='butt', fill=False)
            for object_id, points in [(None, [[2.50732973761175, 4.528298269615471]]), (None, [[4.558263856072971, 3.4598797105217973]]), (None, [[3.527427859359478, 2.5256845885001935]])]:
                c.point(points, id=object_id, zorder=10, s=[50], facecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]], edgecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]])
            return c.save(output_path)

    def draw_C02(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane260_C02.png'
        with Canvas(PLANE, xlim=(-0.12667099149054195, 5.130592591748275), ylim=(-0.12979189053362905, 5.127471692705188), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
            c.path([[0.0, 0.0], [5.0, 0.0], [5.0, 5.0], [0.0, 5.0], [0.0, 0.0]], [1, 2, 2, 2, 79], id='box', zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 1.0), linewidth=0.0, capstyle='butt')
            c.path([[0.0, 0.0], [5.0, 0.0], [5.0, 5.0], [0.0, 5.0], [0.0, 0.0]], [1, 2, 2, 2, 79], id='box', capstyle='butt', fill=False)
            c.path([[1.045, 4.045], [3.955, 4.045], [3.955, 4.955], [1.045, 4.955], [1.045, 4.045]], [1, 2, 2, 2, 79], id='block0', zorder=1, edgecolor='none', facecolor=(1.0, 1.0, 1.0, 1.0), linewidth=0.0, capstyle='butt')
            c.path([[1.045, 4.045], [3.955, 4.045], [3.955, 4.955], [1.045, 4.955], [1.045, 4.045]], [1, 2, 2, 2, 79], id='block0', capstyle='butt', fill=False)
            c.path([[4.045, 2.045], [4.955, 2.045], [4.955, 4.955], [4.045, 4.955], [4.045, 2.045]], [1, 2, 2, 2, 79], id='block1', zorder=1, edgecolor='none', facecolor=(1.0, 1.0, 1.0, 1.0), linewidth=0.0, capstyle='butt')
            c.path([[4.045, 2.045], [4.955, 2.045], [4.955, 4.955], [4.045, 4.955], [4.045, 2.045]], [1, 2, 2, 2, 79], id='block1', capstyle='butt', fill=False)
            c.path([[0.045, 3.045], [2.955, 3.045], [2.955, 3.955], [0.045, 3.955], [0.045, 3.045]], [1, 2, 2, 2, 79], id='block2', zorder=1, edgecolor='none', facecolor=(1.0, 1.0, 1.0, 1.0), linewidth=0.0, capstyle='butt')
            c.path([[0.045, 3.045], [2.955, 3.045], [2.955, 3.955], [0.045, 3.955], [0.045, 3.045]], [1, 2, 2, 2, 79], id='block2', capstyle='butt', fill=False)
            c.path([[3.045, 1.045], [3.955, 1.045], [3.955, 3.955], [3.045, 3.955], [3.045, 1.045]], [1, 2, 2, 2, 79], id='block3', zorder=1, edgecolor='none', facecolor=(1.0, 1.0, 1.0, 1.0), linewidth=0.0, capstyle='butt')
            c.path([[3.045, 1.045], [3.955, 1.045], [3.955, 3.955], [3.045, 3.955], [3.045, 1.045]], [1, 2, 2, 2, 79], id='block3', capstyle='butt', fill=False)
            c.path([[0.045, 0.045], [0.955, 0.045], [0.955, 2.955], [0.045, 2.955], [0.045, 0.045]], [1, 2, 2, 2, 79], id='block4', zorder=1, edgecolor='none', facecolor=(1.0, 1.0, 1.0, 1.0), linewidth=0.0, capstyle='butt')
            c.path([[0.045, 0.045], [0.955, 0.045], [0.955, 2.955], [0.045, 2.955], [0.045, 0.045]], [1, 2, 2, 2, 79], id='block4', capstyle='butt', fill=False)
            c.path([[1.045, 0.045], [1.955, 0.045], [1.955, 2.955], [1.045, 2.955], [1.045, 0.045]], [1, 2, 2, 2, 79], id='block5', zorder=1, edgecolor='none', facecolor=(1.0, 1.0, 1.0, 1.0), linewidth=0.0, capstyle='butt')
            c.path([[1.045, 0.045], [1.955, 0.045], [1.955, 2.955], [1.045, 2.955], [1.045, 0.045]], [1, 2, 2, 2, 79], id='block5', capstyle='butt', fill=False)
            c.path([[2.045, 0.045], [4.955, 0.045], [4.955, 0.955], [2.045, 0.955], [2.045, 0.045]], [1, 2, 2, 2, 79], id='block6', zorder=1, edgecolor='none', facecolor=(1.0, 1.0, 1.0, 1.0), linewidth=0.0, capstyle='butt')
            c.path([[2.045, 0.045], [4.955, 0.045], [4.955, 0.955], [2.045, 0.955], [2.045, 0.045]], [1, 2, 2, 2, 79], id='block6', capstyle='butt', fill=False)
            for object_id, points in [(None, [[3.575748296705422, 0.4854883450047369]]), (None, [[3.548903609291009, 2.4451505262569517]]), (None, [[2.6683978620982325, 4.528298269615471]])]:
                c.point(points, id=object_id, zorder=10, s=[50], facecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]], edgecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]])
            return c.save(output_path)
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Plane260')
    parser.add_argument('output', nargs='?')
    parser.add_argument('--variant', choices=('C01', 'C02'))
    args = parser.parse_args()
    print(Plane260().draw(args.output, variant=args.variant))
