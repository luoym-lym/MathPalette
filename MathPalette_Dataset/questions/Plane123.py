"""Collected question Plane123; construction on the shared drawing protocol."""
from pathlib import Path
import sys
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from MathPalette_Dataset.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane123:
    variants = ('C01', 'C02', 'C03', 'C04', 'C05')

    def __init__(self):
        self.id = 'Plane123'
        self.source_dataset = 'Author Designed'
        self.source_key = 'unit-grid-area:reference_arrow'
        self.question = 'The grid is composed of congruent unit squares, each with area 1. What is the area of the shaded polygon?'
        self.answer = '10'
        self.answer_type = 'number'
        self.query = self.question

    def draw(self, output_path=None, *, variant=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if variant not in self.variants:
                raise ValueError('Unknown Special variant: ' + str(variant))
            return getattr(self, 'draw_' + variant)(output_path)
        with Canvas(PLANE, xlim=(-0.09302325581395365, 4.093023255813954), ylim=(-0.09302325581395365, 4.093023255813954), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
            c.path([[0.0, 0.0], [2.0, 0.0], [4.0, 2.0], [2.0, 4.0], [0.0, 4.0], [1.0, 2.0], [0.0, 0.0]], [1, 2, 2, 2, 2, 2, 79], alpha=0.45, zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), capstyle='butt')
            c.path([[0.0, 0.0], [2.0, 0.0], [4.0, 2.0], [2.0, 4.0], [0.0, 4.0], [1.0, 2.0], [0.0, 0.0]], [1, 2, 2, 2, 2, 2, 79], id='shade', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            for object_id, points in [('grid_v0', [[0.0, 0.0], [0.0, 4.0]]), ('grid_v1', [[1.0, 0.0], [1.0, 4.0]]), ('grid_v2', [[2.0, 0.0], [2.0, 4.0]]), ('grid_v3', [[3.0, 0.0], [3.0, 4.0]]), ('grid_v4', [[4.0, 0.0], [4.0, 4.0]]), ('grid_h0', [[0.0, 0.0], [4.0, 0.0]]), ('grid_h1', [[0.0, 1.0], [4.0, 1.0]]), ('grid_h2', [[0.0, 2.0], [4.0, 2.0]]), ('grid_h3', [[0.0, 3.0], [4.0, 3.0]]), ('grid_h4', [[0.0, 4.0], [4.0, 4.0]])]:
                c.line(points, id=object_id)
            return c.save(output_path)

    def draw_C01(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane123_C01.png'
        with Canvas(PLANE, xlim=(-0.09302325581395365, 4.093023255813954), ylim=(-0.09302325581395365, 4.093023255813954), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
            c.path([[0.0, 0.0], [2.0, 0.0], [4.0, 2.0], [2.0, 4.0], [0.0, 4.0], [1.0, 2.0], [0.0, 0.0]], [1, 2, 2, 2, 2, 2, 79], alpha=0.45, zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), capstyle='butt')
            c.path([[5.551115123125783e-17, 5.551115123125783e-17], [2.0, 5.551115123125783e-17], [4.0, 2.0], [2.0, 4.0], [5.551115123125783e-17, 4.0]], [1, 2, 2, 2, 2], id='shade', edgecolor=(0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0), capstyle='butt', fill=False)
            c.path([[5.551115123125783e-17, 4.0], [1.0, 2.0], [5.551115123125783e-17, 5.551115123125783e-17]], [1, 2, 2], id='shade', capstyle='butt', fill=False)
            c.line([[0.0, 0.0], [0.0, 4.0]], id='grid_v0', color='#DC2626')
            for object_id, points in [('grid_v1', [[1.0, 0.0], [1.0, 4.0]]), ('grid_v2', [[2.0, 0.0], [2.0, 4.0]]), ('grid_v3', [[3.0, 0.0], [3.0, 4.0]]), ('grid_v4', [[4.0, 0.0], [4.0, 4.0]]), ('grid_h0', [[0.0, 0.0], [4.0, 0.0]]), ('grid_h1', [[0.0, 1.0], [4.0, 1.0]]), ('grid_h2', [[0.0, 2.0], [4.0, 2.0]]), ('grid_h3', [[0.0, 3.0], [4.0, 3.0]]), ('grid_h4', [[0.0, 4.0], [4.0, 4.0]])]:
                c.line(points, id=object_id)
            return c.save(output_path)

    def draw_C02(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane123_C02.png'
        with Canvas(PLANE, xlim=(-0.09302325581395365, 4.093023255813954), ylim=(-0.09302325581395365, 4.093023255813954), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
            c.path([[0.0, 0.0], [2.0, 0.0], [4.0, 2.0], [2.0, 4.0], [0.0, 4.0], [1.0, 2.0], [0.0, 0.0]], [1, 2, 2, 2, 2, 2, 79], alpha=0.45, zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), capstyle='butt')
            c.path([[5.551115123125783e-17, 5.551115123125783e-17], [2.0, 5.551115123125783e-17], [4.0, 2.0], [2.0, 4.0], [5.551115123125783e-17, 4.0]], [1, 2, 2, 2, 2], id='shade', edgecolor=(0.1450980392156863, 0.38823529411764707, 0.9215686274509803, 1.0), linewidth=2.0, capstyle='butt', fill=False)
            c.path([[5.551115123125783e-17, 4.0], [1.0, 2.0], [5.551115123125783e-17, 5.551115123125783e-17]], [1, 2, 2], id='shade', capstyle='butt', fill=False)
            c.line([[0.0, 0.0], [0.0, 4.0]], id='grid_v0', color='#2563EB', linewidth=2.0)
            for object_id, points in [('grid_v1', [[1.0, 0.0], [1.0, 4.0]]), ('grid_v2', [[2.0, 0.0], [2.0, 4.0]]), ('grid_v3', [[3.0, 0.0], [3.0, 4.0]]), ('grid_v4', [[4.0, 0.0], [4.0, 4.0]]), ('grid_h0', [[0.0, 0.0], [4.0, 0.0]]), ('grid_h1', [[0.0, 1.0], [4.0, 1.0]]), ('grid_h2', [[0.0, 2.0], [4.0, 2.0]]), ('grid_h3', [[0.0, 3.0], [4.0, 3.0]]), ('grid_h4', [[0.0, 4.0], [4.0, 4.0]])]:
                c.line(points, id=object_id)
            return c.save(output_path)

    def draw_C03(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane123_C03.png'
        with Canvas(PLANE, xlim=(-0.09302325581395365, 4.093023255813954), ylim=(-0.09302325581395365, 4.093023255813954), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
            c.path([[0.0, 0.0], [2.0, 0.0], [4.0, 2.0], [2.0, 4.0], [0.0, 4.0], [1.0, 2.0], [0.0, 0.0]], [1, 2, 2, 2, 2, 2, 79], alpha=0.45, zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), capstyle='butt')
            c.path([[5.551115123125783e-17, 5.551115123125783e-17], [2.0, 5.551115123125783e-17], [4.0, 2.0], [2.0, 4.0], [5.551115123125783e-17, 4.0]], [1, 2, 2, 2, 2], id='shade', edgecolor=(0.08627450980392157, 0.6392156862745098, 0.2901960784313726, 1.0), linewidth=3.0, capstyle='butt', fill=False)
            c.path([[5.551115123125783e-17, 4.0], [1.0, 2.0], [5.551115123125783e-17, 5.551115123125783e-17]], [1, 2, 2], id='shade', capstyle='butt', fill=False)
            c.line([[0.0, 0.0], [0.0, 4.0]], id='grid_v0', color='#16A34A', linewidth=3.0)
            for object_id, points in [('grid_v1', [[1.0, 0.0], [1.0, 4.0]]), ('grid_v2', [[2.0, 0.0], [2.0, 4.0]]), ('grid_v3', [[3.0, 0.0], [3.0, 4.0]]), ('grid_v4', [[4.0, 0.0], [4.0, 4.0]]), ('grid_h0', [[0.0, 0.0], [4.0, 0.0]]), ('grid_h1', [[0.0, 1.0], [4.0, 1.0]]), ('grid_h2', [[0.0, 2.0], [4.0, 2.0]]), ('grid_h3', [[0.0, 3.0], [4.0, 3.0]]), ('grid_h4', [[0.0, 4.0], [4.0, 4.0]])]:
                c.line(points, id=object_id)
            return c.save(output_path)

    def draw_C04(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane123_C04.png'
        with Canvas(PLANE, xlim=(-0.09302325581395365, 4.093023255813954), ylim=(-0.09302325581395365, 4.093023255813954), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
            c.path([[0.0, 0.0], [2.0, 0.0], [4.0, 2.0], [2.0, 4.0], [0.0, 4.0], [1.0, 2.0], [0.0, 0.0]], [1, 2, 2, 2, 2, 2, 79], alpha=0.45, zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), capstyle='butt')
            c.path([[5.551115123125783e-17, 5.551115123125783e-17], [2.0, 5.551115123125783e-17], [4.0, 2.0], [2.0, 4.0], [5.551115123125783e-17, 4.0]], [1, 2, 2, 2, 2], id='shade', edgecolor=(0.9176470588235294, 0.34509803921568627, 0.047058823529411764, 1.0), linewidth=2.0, capstyle='butt', fill=False)
            c.path([[5.551115123125783e-17, 4.0], [1.0, 2.0], [5.551115123125783e-17, 5.551115123125783e-17]], [1, 2, 2], id='shade', capstyle='butt', fill=False)
            c.line([[0.0, 0.0], [0.0, 4.0]], id='grid_v0', color='#EA580C', linewidth=2.0)
            for object_id, points in [('grid_v1', [[1.0, 0.0], [1.0, 4.0]]), ('grid_v2', [[2.0, 0.0], [2.0, 4.0]]), ('grid_v3', [[3.0, 0.0], [3.0, 4.0]]), ('grid_v4', [[4.0, 0.0], [4.0, 4.0]]), ('grid_h0', [[0.0, 0.0], [4.0, 0.0]]), ('grid_h1', [[0.0, 1.0], [4.0, 1.0]]), ('grid_h2', [[0.0, 2.0], [4.0, 2.0]]), ('grid_h3', [[0.0, 3.0], [4.0, 3.0]]), ('grid_h4', [[0.0, 4.0], [4.0, 4.0]])]:
                c.line(points, id=object_id)
            return c.save(output_path)

    def draw_C05(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane123_C05.png'
        with Canvas(PLANE, xlim=(-0.09302325581395365, 4.093023255813954), ylim=(-0.09302325581395365, 4.093023255813954), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
            c.path([[0.0, 0.0], [2.0, 0.0], [4.0, 2.0], [2.0, 4.0], [0.0, 4.0], [1.0, 2.0], [0.0, 0.0]], [1, 2, 2, 2, 2, 2, 79], alpha=0.45, zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), capstyle='butt')
            c.path([[5.551115123125783e-17, 5.551115123125783e-17], [2.0, 5.551115123125783e-17], [4.0, 2.0], [2.0, 4.0], [5.551115123125783e-17, 4.0]], [1, 2, 2, 2, 2], id='shade', edgecolor=(0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0), linewidth=3.0, capstyle='butt', fill=False)
            c.path([[5.551115123125783e-17, 4.0], [1.0, 2.0], [5.551115123125783e-17, 5.551115123125783e-17]], [1, 2, 2], id='shade', capstyle='butt', fill=False)
            c.line([[0.0, 0.0], [0.0, 4.0]], id='grid_v0', color='#DC2626', linewidth=3.0)
            for object_id, points in [('grid_v1', [[1.0, 0.0], [1.0, 4.0]]), ('grid_v2', [[2.0, 0.0], [2.0, 4.0]]), ('grid_v3', [[3.0, 0.0], [3.0, 4.0]]), ('grid_v4', [[4.0, 0.0], [4.0, 4.0]]), ('grid_h0', [[0.0, 0.0], [4.0, 0.0]]), ('grid_h1', [[0.0, 1.0], [4.0, 1.0]]), ('grid_h2', [[0.0, 2.0], [4.0, 2.0]]), ('grid_h3', [[0.0, 3.0], [4.0, 3.0]]), ('grid_h4', [[0.0, 4.0], [4.0, 4.0]])]:
                c.line(points, id=object_id)
            return c.save(output_path)
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Plane123')
    parser.add_argument('output', nargs='?')
    parser.add_argument('--variant', choices=('C01', 'C02', 'C03', 'C04', 'C05'))
    args = parser.parse_args()
    print(Plane123().draw(args.output, variant=args.variant))
