"""Collected question Plane307; construction on the shared drawing protocol."""
from pathlib import Path
import sys
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from MathPalette_Dataset.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane307:
    variants = ('C01', 'C02', 'C03', 'C04')

    def __init__(self):
        self.id = 'Plane307'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:956'
        self.question = 'What is the smallest number of shaded squares that can be added to the diagram to create a design, including the grid, with 4 axes of symmetry?'
        self.answer = '21'
        self.answer_type = 'number'
        self.query = self.question

    def draw(self, output_path=None, *, variant=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if variant not in self.variants:
                raise ValueError('Unknown Special variant: ' + str(variant))
            return getattr(self, 'draw_' + variant)(output_path)
        with Canvas(PLANE, xlim=[-0.14824620141445033, 6.15721078160753], ylim=[-0.15797195779922157, 6.147485025222759], axes_position=[0.05, 0.05, 0.9, 0.9], coordinate_axes=False) as c:
            c.path([[2.0, 4.0], [3.0, 4.0], [3.0, 5.0], [2.0, 5.0], [2.0, 4.0]], [1, 2, 2, 2, 79], id='green24', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45], linewidth=0.0, capstyle='butt')
            c.path([[2.0, 4.0], [3.0, 4.0], [3.0, 5.0], [2.0, 5.0], [2.0, 4.0]], [1, 2, 2, 2, 79], id='green24', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[2.0, 5.0], [3.0, 5.0], [3.0, 6.0], [2.0, 6.0], [2.0, 5.0]], [1, 2, 2, 2, 79], id='green25', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45], linewidth=0.0, capstyle='butt')
            c.path([[2.0, 5.0], [3.0, 5.0], [3.0, 6.0], [2.0, 6.0], [2.0, 5.0]], [1, 2, 2, 2, 79], id='green25', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[1.0, 5.0], [2.0, 5.0], [2.0, 6.0], [1.0, 6.0], [1.0, 5.0]], [1, 2, 2, 2, 79], id='green15', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45], linewidth=0.0, capstyle='butt')
            c.path([[1.0, 5.0], [2.0, 5.0], [2.0, 6.0], [1.0, 6.0], [1.0, 5.0]], [1, 2, 2, 2, 79], id='green15', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            for object_id, points in [('v1', [[1.0, 0.0], [1.0, 6.0]]), ('v2', [[2.0, 0.0], [2.0, 6.0]]), ('v3', [[3.0, 0.0], [3.0, 6.0]]), ('v4', [[4.0, 0.0], [4.0, 6.0]]), ('v5', [[5.0, 0.0], [5.0, 6.0]]), ('h1', [[0.0, 1.0], [6.0, 1.0]]), ('h2', [[0.0, 2.0], [6.0, 2.0]]), ('h3', [[0.0, 3.0], [6.0, 3.0]]), ('h4', [[0.0, 4.0], [6.0, 4.0]]), ('h5', [[0.0, 5.0], [6.0, 5.0]])]:
                c.line(points, id=object_id)
            c.path([[0.0, 0.0], [6.0, 0.0], [6.0, 6.0], [0.0, 6.0], [0.0, 0.0]], [1, 2, 2, 2, 79], id='outer', facecolor=[0.0, 0.0, 0.0, 0.0], capstyle='butt')
            return c.save(output_path)

    def draw_C01(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane307_C01.png'
        with Canvas(PLANE, xlim=(-0.14824620141445033, 6.15721078160753), ylim=(-0.15797195779922157, 6.147485025222759), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
            c.path([[2.0, 4.0], [3.0, 4.0], [3.0, 5.0], [2.0, 5.0], [2.0, 4.0]], [1, 2, 2, 2, 79], id='green24', zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), linewidth=0.0, capstyle='butt')
            c.path([[2.0, 4.0], [3.0, 4.0], [3.0, 5.0], [2.0, 5.0], [2.0, 4.0]], [1, 2, 2, 2, 79], id='green24', capstyle='butt', fill=False)
            c.path([[2.0, 5.0], [3.0, 5.0], [3.0, 6.0], [2.0, 6.0], [2.0, 5.0]], [1, 2, 2, 2, 79], id='green25', zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), linewidth=0.0, capstyle='butt')
            c.path([[2.0, 5.0], [3.0, 5.0], [3.0, 6.0], [2.0, 6.0], [2.0, 5.0]], [1, 2, 2, 2, 79], id='green25', capstyle='butt', fill=False)
            c.path([[1.0, 5.0], [2.0, 5.0], [2.0, 6.0], [1.0, 6.0], [1.0, 5.0]], [1, 2, 2, 2, 79], id='green15', zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), linewidth=0.0, capstyle='butt')
            c.path([[1.0, 5.0], [2.0, 5.0], [2.0, 6.0], [1.0, 6.0], [1.0, 5.0]], [1, 2, 2, 2, 79], id='green15', capstyle='butt', fill=False)
            c.line([[1.0, 0.0], [1.0, 6.0]], id='v1')
            c.line([[2.0, 0.0], [2.0, 6.0]], id='v2')
            c.line([[3.0, 0.0], [3.0, 6.0]], id='v3', color='#DC2626')
            for object_id, points in [('v4', [[4.0, 0.0], [4.0, 6.0]]), ('v5', [[5.0, 0.0], [5.0, 6.0]]), ('h1', [[0.0, 1.0], [6.0, 1.0]]), ('h2', [[0.0, 2.0], [6.0, 2.0]])]:
                c.line(points, id=object_id)
            c.line([[0.0, 3.0], [6.0, 3.0]], id='h3', color='#DC2626')
            c.line([[0.0, 4.0], [6.0, 4.0]], id='h4')
            c.line([[0.0, 5.0], [6.0, 5.0]], id='h5')
            c.path([[0.0, 0.0], [6.0, 0.0], [6.0, 6.0], [0.0, 6.0], [0.0, 0.0]], [1, 2, 2, 2, 79], id='outer', capstyle='butt')
            return c.save(output_path)

    def draw_C02(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane307_C02.png'
        with Canvas(PLANE, xlim=(-0.14824620141445033, 6.15721078160753), ylim=(-0.15797195779922157, 6.147485025222759), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
            c.path([[2.0, 4.0], [3.0, 4.0], [3.0, 5.0], [2.0, 5.0], [2.0, 4.0]], [1, 2, 2, 2, 79], id='green24', zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), linewidth=0.0, capstyle='butt')
            c.path([[2.0, 4.0], [3.0, 4.0], [3.0, 5.0], [2.0, 5.0], [2.0, 4.0]], [1, 2, 2, 2, 79], id='green24', capstyle='butt', fill=False)
            c.path([[2.0, 5.0], [3.0, 5.0], [3.0, 6.0], [2.0, 6.0], [2.0, 5.0]], [1, 2, 2, 2, 79], id='green25', zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), linewidth=0.0, capstyle='butt')
            c.path([[2.0, 5.0], [3.0, 5.0], [3.0, 6.0], [2.0, 6.0], [2.0, 5.0]], [1, 2, 2, 2, 79], id='green25', capstyle='butt', fill=False)
            c.path([[1.0, 5.0], [2.0, 5.0], [2.0, 6.0], [1.0, 6.0], [1.0, 5.0]], [1, 2, 2, 2, 79], id='green15', zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), linewidth=0.0, capstyle='butt')
            c.path([[1.0, 5.0], [2.0, 5.0], [2.0, 6.0], [1.0, 6.0], [1.0, 5.0]], [1, 2, 2, 2, 79], id='green15', capstyle='butt', fill=False)
            for object_id, points in [('v1', [[1.0, 0.0], [1.0, 6.0]]), ('v2', [[2.0, 0.0], [2.0, 6.0]]), ('v3', [[3.0, 0.0], [3.0, 6.0]]), ('v4', [[4.0, 0.0], [4.0, 6.0]]), ('v5', [[5.0, 0.0], [5.0, 6.0]]), ('h1', [[0.0, 1.0], [6.0, 1.0]]), ('h2', [[0.0, 2.0], [6.0, 2.0]]), ('h3', [[0.0, 3.0], [6.0, 3.0]]), ('h4', [[0.0, 4.0], [6.0, 4.0]]), ('h5', [[0.0, 5.0], [6.0, 5.0]])]:
                c.line(points, id=object_id)
            c.path([[0.0, 0.0], [6.0, 0.0], [6.0, 6.0], [0.0, 6.0], [0.0, 0.0]], [1, 2, 2, 2, 79], id='outer', capstyle='butt')
            c.line([[0, 6], [6, 0]], zorder=9, color='#EA580C', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            c.line([[6, 6], [0, 0]], zorder=9, color='#EA580C', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            return c.save(output_path)

    def draw_C03(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane307_C03.png'
        with Canvas(PLANE, xlim=(-0.14824620141445033, 6.15721078160753), ylim=(-0.15797195779922157, 6.147485025222759), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
            c.path([[2.0, 4.0], [3.0, 4.0], [3.0, 5.0], [2.0, 5.0], [2.0, 4.0]], [1, 2, 2, 2, 79], id='green24', zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), linewidth=0.0, capstyle='butt')
            c.path([[2.0, 4.0], [3.0, 4.0], [3.0, 5.0], [2.0, 5.0], [2.0, 4.0]], [1, 2, 2, 2, 79], id='green24', capstyle='butt', fill=False)
            c.path([[2.0, 5.0], [3.0, 5.0], [3.0, 6.0], [2.0, 6.0], [2.0, 5.0]], [1, 2, 2, 2, 79], id='green25', zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), linewidth=0.0, capstyle='butt')
            c.path([[2.0, 5.0], [3.0, 5.0], [3.0, 6.0], [2.0, 6.0], [2.0, 5.0]], [1, 2, 2, 2, 79], id='green25', capstyle='butt', fill=False)
            c.path([[1.0, 5.0], [2.0, 5.0], [2.0, 6.0], [1.0, 6.0], [1.0, 5.0]], [1, 2, 2, 2, 79], id='green15', zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), linewidth=0.0, capstyle='butt')
            c.path([[1.0, 5.0], [2.0, 5.0], [2.0, 6.0], [1.0, 6.0], [1.0, 5.0]], [1, 2, 2, 2, 79], id='green15', capstyle='butt', fill=False)
            for object_id, points in [('v1', [[1.0, 0.0], [1.0, 6.0]]), ('v2', [[2.0, 0.0], [2.0, 6.0]]), ('v3', [[3.0, 0.0], [3.0, 6.0]]), ('v4', [[4.0, 0.0], [4.0, 6.0]]), ('v5', [[5.0, 0.0], [5.0, 6.0]]), ('h1', [[0.0, 1.0], [6.0, 1.0]]), ('h2', [[0.0, 2.0], [6.0, 2.0]]), ('h3', [[0.0, 3.0], [6.0, 3.0]]), ('h4', [[0.0, 4.0], [6.0, 4.0]]), ('h5', [[0.0, 5.0], [6.0, 5.0]])]:
                c.line(points, id=object_id)
            c.path([[0.0, 0.0], [6.0, 0.0], [6.0, 6.0], [0.0, 6.0], [0.0, 0.0]], [1, 2, 2, 2, 79], id='outer', capstyle='butt')
            c.line([[6, 6], [0, 0]], zorder=9, color='#2563EB', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            c.line([[0, 6], [6, 0]], zorder=9, color='#2563EB', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            return c.save(output_path)

    def draw_C04(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane307_C04.png'
        with Canvas(PLANE, xlim=(-0.14824620141445033, 6.15721078160753), ylim=(-0.15797195779922157, 6.147485025222759), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
            c.path([[2.0, 4.0], [3.0, 4.0], [3.0, 5.0], [2.0, 5.0], [2.0, 4.0]], [1, 2, 2, 2, 79], id='green24', zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), linewidth=0.0, capstyle='butt')
            c.path([[2.0, 4.0], [3.0, 4.0], [3.0, 5.0], [2.0, 5.0], [2.0, 4.0]], [1, 2, 2, 2, 79], id='green24', capstyle='butt', fill=False)
            c.path([[2.0, 5.0], [3.0, 5.0], [3.0, 6.0], [2.0, 6.0], [2.0, 5.0]], [1, 2, 2, 2, 79], id='green25', zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), linewidth=0.0, capstyle='butt')
            c.path([[2.0, 5.0], [3.0, 5.0], [3.0, 6.0], [2.0, 6.0], [2.0, 5.0]], [1, 2, 2, 2, 79], id='green25', capstyle='butt', fill=False)
            c.path([[1.0, 5.0], [2.0, 5.0], [2.0, 6.0], [1.0, 6.0], [1.0, 5.0]], [1, 2, 2, 2, 79], id='green15', zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), linewidth=0.0, capstyle='butt')
            c.path([[1.0, 5.0], [2.0, 5.0], [2.0, 6.0], [1.0, 6.0], [1.0, 5.0]], [1, 2, 2, 2, 79], id='green15', capstyle='butt', fill=False)
            for object_id, points in [('v1', [[1.0, 0.0], [1.0, 6.0]]), ('v2', [[2.0, 0.0], [2.0, 6.0]]), ('v3', [[3.0, 0.0], [3.0, 6.0]]), ('v4', [[4.0, 0.0], [4.0, 6.0]]), ('v5', [[5.0, 0.0], [5.0, 6.0]]), ('h1', [[0.0, 1.0], [6.0, 1.0]]), ('h2', [[0.0, 2.0], [6.0, 2.0]]), ('h3', [[0.0, 3.0], [6.0, 3.0]]), ('h4', [[0.0, 4.0], [6.0, 4.0]]), ('h5', [[0.0, 5.0], [6.0, 5.0]])]:
                c.line(points, id=object_id)
            c.path([[0.0, 0.0], [6.0, 0.0], [6.0, 6.0], [0.0, 6.0], [0.0, 0.0]], [1, 2, 2, 2, 79], id='outer', capstyle='butt')
            c.line([[0, 3], [6, 3]], zorder=9, color='#16A34A', solid_capstyle='butt')
            c.line([[3, 6], [3, 0]], zorder=9, color='#16A34A', solid_capstyle='butt')
            return c.save(output_path)
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Plane307')
    parser.add_argument('output', nargs='?')
    parser.add_argument('--variant', choices=('C01', 'C02', 'C03', 'C04'))
    args = parser.parse_args()
    print(Plane307().draw(args.output, variant=args.variant))
