"""Collected question Solid249; construction on the shared drawing protocol."""
from pathlib import Path
import sys
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from MathPalette_Dataset.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Solid249:
    variants = ('C01',)

    def __init__(self):
        self.id = 'Solid249'
        self.source_dataset = 'Author Designed'
        self.source_key = 'author-promote15:Solid249'
        self.question = 'A square sheet occupies -4 ≤ x ≤ 4, -4 ≤ y ≤ 4. It was folded once in half along one of the lines listed below, and two small circular holes were punched through both layers at distinct points away from the fold. The sheet is completely unfolded and shown. Which line was the fold?\nA: x=0\nB: y=0\nC: y=x\nD: y=-x\nE: x=1'
        self.answer = 'A'
        self.answer_type = 'choice'
        self.choices = {'A': 'x=0', 'B': 'y=0', 'C': 'y=x', 'D': 'y=-x', 'E': 'x=1'}
        self.query = self.question

    def draw(self, output_path=None, *, variant=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if variant not in self.variants:
                raise ValueError('Unknown Special variant: ' + str(variant))
            return getattr(self, 'draw_' + variant)(output_path)
        with Canvas(SOLID, xlim=[-5.0, 5.0], ylim=[-5.0, 5.0], axes_position=[0.05, 0.05, 0.9, 0.9], coordinate_axes=False) as c:
            for object_id, points in [('bottom', [[-4, -4], [4, -4]]), ('right', [[4, -4], [4, 4]]), ('top', [[4, 4], [-4, 4]]), ('left', [[-4, 4], [-4, -4]])]:
                c.line(points, id=object_id)
            for object_id, center, radius in [('hole0', [-2, 1], 0.14), ('hole1', [2, 1], 0.14), ('hole2', [-1, -2], 0.14), ('hole3', [1, -2], 0.14)]:
                c.circle(center, radius, id=object_id, zorder=1, facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], fill=False)
            return c.save(output_path)

    def draw_C01(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Solid249_C01.png'
        with Canvas(SOLID, xlim=(-5.0, 5.0), ylim=(-5.0, 5.0), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
            for object_id, points in [('bottom', [[-4, -4], [4, -4]]), ('right', [[4, -4], [4, 4]]), ('top', [[4, 4], [-4, 4]]), ('left', [[-4, 4], [-4, -4]])]:
                c.line(points, id=object_id)
            c.circle([-2, 1], 0.14, id='hole0', zorder=1, edgecolor=(0.1450980392156863, 0.38823529411764707, 0.9215686274509803, 1.0), linewidth=1.5, fill=False)
            c.circle([2, 1], 0.14, id='hole1', zorder=1, edgecolor=(0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0), linewidth=1.5, fill=False)
            c.circle([-1, -2], 0.14, id='hole2', zorder=1, edgecolor=(0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0), linewidth=1.5, fill=False)
            c.circle([1, -2], 0.14, id='hole3', zorder=1, edgecolor=(0.1450980392156863, 0.38823529411764707, 0.9215686274509803, 1.0), linewidth=1.5, fill=False)
            return c.save(output_path)
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Solid249')
    parser.add_argument('output', nargs='?')
    parser.add_argument('--variant', choices=('C01',))
    args = parser.parse_args()
    print(Solid249().draw(args.output, variant=args.variant))
