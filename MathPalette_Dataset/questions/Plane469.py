"""Collected question Plane469; construction on the shared drawing protocol."""
from pathlib import Path
import sys
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from MathPalette_Dataset.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane469:
    variants = ('C01',)

    def __init__(self):
        self.id = 'Plane469'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:2662'
        self.question = 'What is the minimum number of small squares that must be colored black so that a line of symmetry lies on the diagonal $ \\overline{BD}$ of square $ ABCD$?'
        self.answer = '4'
        self.answer_type = 'number'
        self.query = self.question

    def draw(self, output_path=None, *, variant=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if variant not in self.variants:
                raise ValueError('Unknown Special variant: ' + str(variant))
            return getattr(self, 'draw_' + variant)(output_path)
        with Canvas(PLANE, xlim=[-0.3073701959163735, 4.300694539430536], ylim=[-0.29072218248826953, 4.31734255285864], axes_position=[0.05, 0.05, 0.9, 0.9], coordinate_axes=False) as c:
            for object_id, vertices, codes in [('c00', [[0.0, 0.0], [1.0, 0.0], [1.0, 1.0], [0.0, 1.0], [0.0, 0.0]], [1, 2, 2, 2, 79]), ('c01', [[0.0, 1.0], [1.0, 1.0], [1.0, 2.0], [0.0, 2.0], [0.0, 1.0]], [1, 2, 2, 2, 79]), ('c02', [[0.0, 2.0], [1.0, 2.0], [1.0, 3.0], [0.0, 3.0], [0.0, 2.0]], [1, 2, 2, 2, 79])]:
                c.path(vertices, codes, id=object_id, facecolor=[0.0, 0.0, 0.0, 0.0], capstyle='butt')
            c.path([[0.0, 3.0], [1.0, 3.0], [1.0, 4.0], [0.0, 4.0], [0.0, 3.0]], [1, 2, 2, 2, 79], id='c03', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.0, 0.0, 0.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[0.0, 3.0], [1.0, 3.0], [1.0, 4.0], [0.0, 4.0], [0.0, 3.0]], [1, 2, 2, 2, 79], id='c03', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[1.0, 0.0], [2.0, 0.0], [2.0, 1.0], [1.0, 1.0], [1.0, 0.0]], [1, 2, 2, 2, 79], id='c10', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.0, 0.0, 0.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[1.0, 0.0], [2.0, 0.0], [2.0, 1.0], [1.0, 1.0], [1.0, 0.0]], [1, 2, 2, 2, 79], id='c10', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            for object_id, vertices, codes in [('c11', [[1.0, 1.0], [2.0, 1.0], [2.0, 2.0], [1.0, 2.0], [1.0, 1.0]], [1, 2, 2, 2, 79]), ('c12', [[1.0, 2.0], [2.0, 2.0], [2.0, 3.0], [1.0, 3.0], [1.0, 2.0]], [1, 2, 2, 2, 79]), ('c13', [[1.0, 3.0], [2.0, 3.0], [2.0, 4.0], [1.0, 4.0], [1.0, 3.0]], [1, 2, 2, 2, 79]), ('c20', [[2.0, 0.0], [3.0, 0.0], [3.0, 1.0], [2.0, 1.0], [2.0, 0.0]], [1, 2, 2, 2, 79]), ('c21', [[2.0, 1.0], [3.0, 1.0], [3.0, 2.0], [2.0, 2.0], [2.0, 1.0]], [1, 2, 2, 2, 79]), ('c22', [[2.0, 2.0], [3.0, 2.0], [3.0, 3.0], [2.0, 3.0], [2.0, 2.0]], [1, 2, 2, 2, 79])]:
                c.path(vertices, codes, id=object_id, facecolor=[0.0, 0.0, 0.0, 0.0], capstyle='butt')
            c.path([[2.0, 3.0], [3.0, 3.0], [3.0, 4.0], [2.0, 4.0], [2.0, 3.0]], [1, 2, 2, 2, 79], id='c23', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.0, 0.0, 0.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[2.0, 3.0], [3.0, 3.0], [3.0, 4.0], [2.0, 4.0], [2.0, 3.0]], [1, 2, 2, 2, 79], id='c23', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[3.0, 0.0], [4.0, 0.0], [4.0, 1.0], [3.0, 1.0], [3.0, 0.0]], [1, 2, 2, 2, 79], id='c30', facecolor=[0.0, 0.0, 0.0, 0.0], capstyle='butt')
            c.path([[3.0, 1.0], [4.0, 1.0], [4.0, 2.0], [3.0, 2.0], [3.0, 1.0]], [1, 2, 2, 2, 79], id='c31', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.0, 0.0, 0.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[3.0, 1.0], [4.0, 1.0], [4.0, 2.0], [3.0, 2.0], [3.0, 1.0]], [1, 2, 2, 2, 79], id='c31', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[3.0, 2.0], [4.0, 2.0], [4.0, 3.0], [3.0, 3.0], [3.0, 2.0]], [1, 2, 2, 2, 79], id='c32', facecolor=[0.0, 0.0, 0.0, 0.0], capstyle='butt')
            c.path([[3.0, 3.0], [4.0, 3.0], [4.0, 4.0], [3.0, 4.0], [3.0, 3.0]], [1, 2, 2, 2, 79], id='c33', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.0, 0.0, 0.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[3.0, 3.0], [4.0, 3.0], [4.0, 4.0], [3.0, 4.0], [3.0, 3.0]], [1, 2, 2, 2, 79], id='c33', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.text('A', [0.0, 4.0], id='nameA', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[-15, 15], annotation_clip=None)
            c.text('B', [4.0, 4.0], id='nameB', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[15, 15], annotation_clip=None)
            c.text('C', [4.0, 0.0], id='nameC', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[15, -15], annotation_clip=None)
            c.text('D', [0.0, 0.0], id='nameD', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[-15, -15], annotation_clip=None)
            return c.save(output_path)

    def draw_C01(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane469_C01.png'
        with Canvas(PLANE, xlim=(-0.3073701959163735, 4.300694539430536), ylim=(-0.29072218248826953, 4.31734255285864), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
            for object_id, vertices, codes in [('c00', [[0.0, 0.0], [1.0, 0.0], [1.0, 1.0], [0.0, 1.0], [0.0, 0.0]], [1, 2, 2, 2, 79]), ('c01', [[0.0, 1.0], [1.0, 1.0], [1.0, 2.0], [0.0, 2.0], [0.0, 1.0]], [1, 2, 2, 2, 79]), ('c02', [[0.0, 2.0], [1.0, 2.0], [1.0, 3.0], [0.0, 3.0], [0.0, 2.0]], [1, 2, 2, 2, 79])]:
                c.path(vertices, codes, id=object_id, capstyle='butt')
            c.path([[0.0, 3.0], [1.0, 3.0], [1.0, 4.0], [0.0, 4.0], [0.0, 3.0]], [1, 2, 2, 2, 79], id='c03', zorder=1, edgecolor='none', facecolor=(0.0, 0.0, 0.0, 1.0), linewidth=0.0, capstyle='butt')
            c.path([[0.0, 3.0], [1.0, 3.0], [1.0, 4.0], [0.0, 4.0], [0.0, 3.0]], [1, 2, 2, 2, 79], id='c03', capstyle='butt', fill=False)
            c.path([[1.0, 0.0], [2.0, 0.0], [2.0, 1.0], [1.0, 1.0], [1.0, 0.0]], [1, 2, 2, 2, 79], id='c10', zorder=1, edgecolor='none', facecolor=(0.0, 0.0, 0.0, 1.0), linewidth=0.0, capstyle='butt')
            c.path([[1.0, 0.0], [2.0, 0.0], [2.0, 1.0], [1.0, 1.0], [1.0, 0.0]], [1, 2, 2, 2, 79], id='c10', capstyle='butt', fill=False)
            for object_id, vertices, codes in [('c11', [[1.0, 1.0], [2.0, 1.0], [2.0, 2.0], [1.0, 2.0], [1.0, 1.0]], [1, 2, 2, 2, 79]), ('c12', [[1.0, 2.0], [2.0, 2.0], [2.0, 3.0], [1.0, 3.0], [1.0, 2.0]], [1, 2, 2, 2, 79]), ('c13', [[1.0, 3.0], [2.0, 3.0], [2.0, 4.0], [1.0, 4.0], [1.0, 3.0]], [1, 2, 2, 2, 79]), ('c20', [[2.0, 0.0], [3.0, 0.0], [3.0, 1.0], [2.0, 1.0], [2.0, 0.0]], [1, 2, 2, 2, 79]), ('c21', [[2.0, 1.0], [3.0, 1.0], [3.0, 2.0], [2.0, 2.0], [2.0, 1.0]], [1, 2, 2, 2, 79]), ('c22', [[2.0, 2.0], [3.0, 2.0], [3.0, 3.0], [2.0, 3.0], [2.0, 2.0]], [1, 2, 2, 2, 79])]:
                c.path(vertices, codes, id=object_id, capstyle='butt')
            c.path([[2.0, 3.0], [3.0, 3.0], [3.0, 4.0], [2.0, 4.0], [2.0, 3.0]], [1, 2, 2, 2, 79], id='c23', zorder=1, edgecolor='none', facecolor=(0.0, 0.0, 0.0, 1.0), linewidth=0.0, capstyle='butt')
            c.path([[2.0, 3.0], [3.0, 3.0], [3.0, 4.0], [2.0, 4.0], [2.0, 3.0]], [1, 2, 2, 2, 79], id='c23', capstyle='butt', fill=False)
            c.path([[3.0, 0.0], [4.0, 0.0], [4.0, 1.0], [3.0, 1.0], [3.0, 0.0]], [1, 2, 2, 2, 79], id='c30', capstyle='butt')
            c.path([[3.0, 1.0], [4.0, 1.0], [4.0, 2.0], [3.0, 2.0], [3.0, 1.0]], [1, 2, 2, 2, 79], id='c31', zorder=1, edgecolor='none', facecolor=(0.0, 0.0, 0.0, 1.0), linewidth=0.0, capstyle='butt')
            c.path([[3.0, 1.0], [4.0, 1.0], [4.0, 2.0], [3.0, 2.0], [3.0, 1.0]], [1, 2, 2, 2, 79], id='c31', capstyle='butt', fill=False)
            c.path([[3.0, 2.0], [4.0, 2.0], [4.0, 3.0], [3.0, 3.0], [3.0, 2.0]], [1, 2, 2, 2, 79], id='c32', capstyle='butt')
            c.path([[3.0, 3.0], [4.0, 3.0], [4.0, 4.0], [3.0, 4.0], [3.0, 3.0]], [1, 2, 2, 2, 79], id='c33', zorder=1, edgecolor='none', facecolor=(0.0, 0.0, 0.0, 1.0), linewidth=0.0, capstyle='butt')
            c.path([[3.0, 3.0], [4.0, 3.0], [4.0, 4.0], [3.0, 4.0], [3.0, 3.0]], [1, 2, 2, 2, 79], id='c33', capstyle='butt', fill=False)
            c.text('A', (0.0, 4.0), id='nameA', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(-15, 15), annotation_clip=None)
            c.text('B', (4.0, 4.0), id='nameB', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(15, 15), annotation_clip=None)
            c.text('C', (4.0, 0.0), id='nameC', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(15, -15), annotation_clip=None)
            c.text('D', (0.0, 0.0), id='nameD', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(-15, -15), annotation_clip=None)
            c.line([[4, 4], [0, 0]], zorder=9, color='#2563EB', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            for object_id, points in [(None, [[3.497859731576999, 1.500361802676185]]), (None, [[2.5472581419731637, 3.4956839511515625]]), (None, [[1.535479222345319, 0.5074066769018817]])]:
                c.point(points, id=object_id, zorder=10, s=[50], facecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]], edgecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]])
            for object_id, points in [(None, [[3.568448958527779, 2.4509633922800202]]), (None, [[1.5448911192720902, 3.4815661057614067]]), (None, [[0.5142884057907041, 1.4956558542127998]])]:
                c.point(points, id=object_id, zorder=10, s=[50], facecolors=[[0.1450980392156863, 0.38823529411764707, 0.9215686274509803, 1.0]], edgecolors=[[0.1450980392156863, 0.38823529411764707, 0.9215686274509803, 1.0]])
            return c.save(output_path)
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Plane469')
    parser.add_argument('output', nargs='?')
    parser.add_argument('--variant', choices=('C01',))
    args = parser.parse_args()
    print(Plane469().draw(args.output, variant=args.variant))
