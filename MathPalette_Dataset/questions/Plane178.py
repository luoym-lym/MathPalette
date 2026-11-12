"""Collected question Plane178; construction on the shared drawing protocol."""
from pathlib import Path
import sys
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from MathPalette_Dataset.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane178:
    variants = ('C01',)

    def __init__(self):
        self.id = 'Plane178'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:225'
        self.question = 'A box contains seven blocks. What is the minimum number of blocks that must be moved to rearrange them so that another block can be placed in the box?'
        self.answer = '3'
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
            c.path([[0.0, 0.0], [5.0, 0.0], [5.0, 5.0], [0.0, 5.0], [0.0, 0.0]], [1, 2, 2, 2, 79], id='box', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.6, 0.6, 0.6, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[0.0, 0.0], [5.0, 0.0], [5.0, 5.0], [0.0, 5.0], [0.0, 0.0]], [1, 2, 2, 2, 79], id='box', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[0.0, 2.0], [1.0, 2.0], [1.0, 5.0], [0.0, 5.0], [0.0, 2.0]], [1, 2, 2, 2, 79], id='block0', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.8666666666666667, 0.8666666666666667, 0.8666666666666667, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[0.0, 2.0], [1.0, 2.0], [1.0, 5.0], [0.0, 5.0], [0.0, 2.0]], [1, 2, 2, 2, 79], id='block0', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[1.0, 4.0], [4.0, 4.0], [4.0, 5.0], [1.0, 5.0], [1.0, 4.0]], [1, 2, 2, 2, 79], id='block1', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.8666666666666667, 0.8666666666666667, 0.8666666666666667, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[1.0, 4.0], [4.0, 4.0], [4.0, 5.0], [1.0, 5.0], [1.0, 4.0]], [1, 2, 2, 2, 79], id='block1', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[1.0, 3.0], [4.0, 3.0], [4.0, 4.0], [1.0, 4.0], [1.0, 3.0]], [1, 2, 2, 2, 79], id='block2', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.8666666666666667, 0.8666666666666667, 0.8666666666666667, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[1.0, 3.0], [4.0, 3.0], [4.0, 4.0], [1.0, 4.0], [1.0, 3.0]], [1, 2, 2, 2, 79], id='block2', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[4.0, 2.0], [5.0, 2.0], [5.0, 5.0], [4.0, 5.0], [4.0, 2.0]], [1, 2, 2, 2, 79], id='block3', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.8666666666666667, 0.8666666666666667, 0.8666666666666667, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[4.0, 2.0], [5.0, 2.0], [5.0, 5.0], [4.0, 5.0], [4.0, 2.0]], [1, 2, 2, 2, 79], id='block3', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[1.0, 0.0], [2.0, 0.0], [2.0, 3.0], [1.0, 3.0], [1.0, 0.0]], [1, 2, 2, 2, 79], id='block4', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.8666666666666667, 0.8666666666666667, 0.8666666666666667, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[1.0, 0.0], [2.0, 0.0], [2.0, 3.0], [1.0, 3.0], [1.0, 0.0]], [1, 2, 2, 2, 79], id='block4', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[2.0, 1.0], [5.0, 1.0], [5.0, 2.0], [2.0, 2.0], [2.0, 1.0]], [1, 2, 2, 2, 79], id='block5', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.8666666666666667, 0.8666666666666667, 0.8666666666666667, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[2.0, 1.0], [5.0, 1.0], [5.0, 2.0], [2.0, 2.0], [2.0, 1.0]], [1, 2, 2, 2, 79], id='block5', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[2.0, 0.0], [5.0, 0.0], [5.0, 1.0], [2.0, 1.0], [2.0, 0.0]], [1, 2, 2, 2, 79], id='block6', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.8666666666666667, 0.8666666666666667, 0.8666666666666667, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[2.0, 0.0], [5.0, 0.0], [5.0, 1.0], [2.0, 1.0], [2.0, 0.0]], [1, 2, 2, 2, 79], id='block6', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            return c.save(output_path)

    def draw_C01(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane178_C01.png'
        with Canvas(PLANE, xlim=(-0.12667099149054195, 5.130592591748275), ylim=(-0.12979189053362905, 5.127471692705188), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
            c.path([[0.0, 0.0], [5.0, 0.0], [5.0, 5.0], [0.0, 5.0], [0.0, 0.0]], [1, 2, 2, 2, 79], id='box', zorder=1, edgecolor='none', facecolor=(0.6, 0.6, 0.6, 1.0), linewidth=0.0, capstyle='butt')
            c.path([[0.0, 0.0], [5.0, 0.0], [5.0, 5.0], [0.0, 5.0], [0.0, 0.0]], [1, 2, 2, 2, 79], id='box', capstyle='butt', fill=False)
            c.path([[0.0, 2.0], [1.0, 2.0], [1.0, 5.0], [0.0, 5.0], [0.0, 2.0]], [1, 2, 2, 2, 79], id='block0', zorder=1, edgecolor='none', facecolor=(0.8666666666666667, 0.8666666666666667, 0.8666666666666667, 1.0), linewidth=0.0, capstyle='butt')
            c.path([[0.0, 2.0], [1.0, 2.0], [1.0, 5.0], [0.0, 5.0], [0.0, 2.0]], [1, 2, 2, 2, 79], id='block0', capstyle='butt', fill=False)
            c.path([[1.0, 4.0], [4.0, 4.0], [4.0, 5.0], [1.0, 5.0], [1.0, 4.0]], [1, 2, 2, 2, 79], id='block1', zorder=1, edgecolor='none', facecolor=(0.8666666666666667, 0.8666666666666667, 0.8666666666666667, 1.0), linewidth=0.0, capstyle='butt')
            c.path([[1.0, 4.0], [4.0, 4.0], [4.0, 5.0], [1.0, 5.0], [1.0, 4.0]], [1, 2, 2, 2, 79], id='block1', capstyle='butt', fill=False)
            c.path([[1.0, 3.0], [4.0, 3.0], [4.0, 4.0], [1.0, 4.0], [1.0, 3.0]], [1, 2, 2, 2, 79], id='block2', zorder=1, edgecolor='none', facecolor=(0.8666666666666667, 0.8666666666666667, 0.8666666666666667, 1.0), linewidth=0.0, capstyle='butt')
            c.path([[1.0, 3.0], [4.0, 3.0], [4.0, 4.0], [1.0, 4.0], [1.0, 3.0]], [1, 2, 2, 2, 79], id='block2', capstyle='butt', fill=False)
            c.path([[4.0, 2.0], [5.0, 2.0], [5.0, 5.0], [4.0, 5.0], [4.0, 2.0]], [1, 2, 2, 2, 79], id='block3', zorder=1, edgecolor='none', facecolor=(0.8666666666666667, 0.8666666666666667, 0.8666666666666667, 1.0), linewidth=0.0, capstyle='butt')
            c.path([[4.0, 2.0], [5.0, 2.0], [5.0, 5.0], [4.0, 5.0], [4.0, 2.0]], [1, 2, 2, 2, 79], id='block3', capstyle='butt', fill=False)
            c.path([[1.0, 0.0], [2.0, 0.0], [2.0, 3.0], [1.0, 3.0], [1.0, 0.0]], [1, 2, 2, 2, 79], id='block4', zorder=1, edgecolor='none', facecolor=(0.8666666666666667, 0.8666666666666667, 0.8666666666666667, 1.0), linewidth=0.0, capstyle='butt')
            c.path([[1.0, 0.0], [2.0, 0.0], [2.0, 3.0], [1.0, 3.0], [1.0, 0.0]], [1, 2, 2, 2, 79], id='block4', capstyle='butt', fill=False)
            c.path([[2.0, 1.0], [5.0, 1.0], [5.0, 2.0], [2.0, 2.0], [2.0, 1.0]], [1, 2, 2, 2, 79], id='block5', zorder=1, edgecolor='none', facecolor=(0.8666666666666667, 0.8666666666666667, 0.8666666666666667, 1.0), linewidth=0.0, capstyle='butt')
            c.path([[2.0, 1.0], [5.0, 1.0], [5.0, 2.0], [2.0, 2.0], [2.0, 1.0]], [1, 2, 2, 2, 79], id='block5', capstyle='butt', fill=False)
            c.path([[2.0, 0.0], [5.0, 0.0], [5.0, 1.0], [2.0, 1.0], [2.0, 0.0]], [1, 2, 2, 2, 79], id='block6', zorder=1, edgecolor='none', facecolor=(0.8666666666666667, 0.8666666666666667, 0.8666666666666667, 1.0), linewidth=0.0, capstyle='butt')
            c.path([[2.0, 0.0], [5.0, 0.0], [5.0, 1.0], [2.0, 1.0], [2.0, 0.0]], [1, 2, 2, 2, 79], id='block6', capstyle='butt', fill=False)
            c.line([[0, 5], [1, 2]], zorder=9, color='#DC2626', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            c.line([[1, 3], [2, 0]], zorder=9, color='#DC2626', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            return c.save(output_path)
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Plane178')
    parser.add_argument('output', nargs='?')
    parser.add_argument('--variant', choices=('C01',))
    args = parser.parse_args()
    print(Plane178().draw(args.output, variant=args.variant))
