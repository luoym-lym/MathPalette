"""Collected question Solid67; construction on the shared drawing protocol."""
from pathlib import Path
import sys
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from MathPalette_Dataset.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Solid67:
    variants = ('C01', 'C02', 'C03')

    def __init__(self):
        self.id = 'Solid67'
        self.source_dataset = 'Author Designed'
        self.source_key = 'midpoint-cut:original'
        self.question = 'The tetrahedron shown has volume 120. Each marked point is the midpoint of the edge on which it lies. Find the volume of the part containing vertex A after the tetrahedron is cut along the shaded plane.'
        self.answer = 30
        self.answer_type = 'number'
        self.query = self.question
        self.points = {'A': [0, 0, 0], 'B': [8, 0, 0], 'C': [0, 9, 0], 'T': [0, 0, 10], 'M': [4, 0, 0], 'N': [0, 4.5, 0]}

    def draw(self, output_path=None, *, variant=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if variant not in self.variants:
                raise ValueError('Unknown Special variant: ' + str(variant))
            return getattr(self, 'draw_' + variant)(output_path)
        with Canvas(SOLID, xlim=[-5.457778918154196, 4.429207489582769], ylim=[-0.6605827211024282, 9.226403686634537], projection=[[-0.6285714285714286, 0.4444444444444444, 0.0], [0.375, 0.15079365079365079, 0.8985714285714286]], origin=[0, 0, 0], offset=[0, 0]) as c:
            c.fill(c.project([self.points['T'], self.points['M'], self.points['N']]), facecolor='#E6E6E6', alpha=1, id='cut_fill')
            c.line(c.project([self.points['B'], self.points['C']]), id='edge_BC', linestyle=(0, [4, 3]), clip_on=False)
            c.line(c.project([self.points['M'], self.points['N']]), id='section_MN', linestyle=(0, [4, 3]), clip_on=False)
            for object_id, points in [('edge_TB', c.project([self.points['T'], self.points['B']])), ('edge_TC', c.project([self.points['T'], self.points['C']])), ('edge_AB', c.project([self.points['A'], self.points['B']])), ('edge_AC', c.project([self.points['A'], self.points['C']])), ('edge_TA', c.project([self.points['T'], self.points['A']])), ('section_TM', c.project([self.points['T'], self.points['M']])), ('section_TN', c.project([self.points['T'], self.points['N']]))]:
                c.line(points, id=object_id, clip_on=False, zorder=3)
            c.point(c.project([self.points['M']]), filled=True, id='midpoint_M')
            c.point(c.project([self.points['N']]), filled=True, id='midpoint_N')
            c.text('A', c.project(self.points['A']), offset_pt=[0, -8], vertex=True, va='top', id='label_A')
            return c.save(output_path)

    def draw_C01(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Solid67_C01.png'
        with Canvas(SOLID, xlim=(-5.457778918154196, 4.429207489582769), ylim=(-0.6605827211024282, 9.226403686634537), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
            c.path([[0.0, 8.985714285714286], [-2.5142857142857142, 1.5], [2.0, 0.6785714285714285], [0.0, 8.985714285714286]], [1, 2, 2, 79], id='cut_fill', alpha=1.0, zorder=1, edgecolor='none', facecolor=(0.9019607843137255, 0.9019607843137255, 0.9019607843137255, 1.0), capstyle='butt')
            c.line([[-5.0285714285714285, 3.0], [4.0, 1.357142857142857]], id='edge_BC', clip_on=False, linestyle=(0, [4, 3]))
            c.line([[-2.5142857142857142, 1.5], [2.0, 0.6785714285714285]], id='section_MN', clip_on=False, linestyle=(0, [4, 3]))
            for object_id, points in [('edge_TB', [[0.0, 8.985714285714286], [-5.0285714285714285, 3.0]]), ('edge_TC', [[0.0, 8.985714285714286], [4.0, 1.357142857142857]]), ('edge_AB', [[0.0, 0.0], [-5.0285714285714285, 3.0]]), ('edge_AC', [[0.0, 0.0], [4.0, 1.357142857142857]]), ('edge_TA', [[0.0, 8.985714285714286], [0.0, 0.0]]), ('section_TM', [[0.0, 8.985714285714286], [-2.5142857142857142, 1.5]]), ('section_TN', [[0.0, 8.985714285714286], [2.0, 0.6785714285714285]])]:
                c.line(points, id=object_id, zorder=3, clip_on=False)
            c.line([[-2.5142857142857142, 1.5]], id='midpoint_M', zorder=4, color=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765), linewidth=1.5, linestyle='None', solid_capstyle='projecting', marker='o', markersize=6.0, markeredgewidth=1.0, markeredgecolor='#000000', markerfacecolor='#000000')
            c.line([[2.0, 0.6785714285714285]], id='midpoint_N', zorder=4, color=(1.0, 0.4980392156862745, 0.054901960784313725), linewidth=1.5, linestyle='None', solid_capstyle='projecting', marker='o', markersize=6.0, markeredgewidth=1.0, markeredgecolor='#000000', markerfacecolor='#000000')
            c.text('A', (0.0, 0.0), fontsize=18.0, fontstyle='italic', va='top', rotation_mode='default', offset_pt=(0, -8), annotation_clip=None)
            c.point([[0.010758498543455453, 4.787760687409487]], zorder=10, s=[50], facecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]], edgecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]])
            return c.save(output_path)

    def draw_C02(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Solid67_C02.png'
        with Canvas(SOLID, xlim=(-5.457778918154196, 4.429207489582769), ylim=(-0.6605827211024282, 9.226403686634537), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
            c.path([[0.0, 8.985714285714286], [-2.5142857142857142, 1.5], [2.0, 0.6785714285714285], [0.0, 8.985714285714286]], [1, 2, 2, 79], id='cut_fill', alpha=1.0, zorder=1, edgecolor='none', facecolor=(0.9019607843137255, 0.9019607843137255, 0.9019607843137255, 1.0), capstyle='butt')
            c.line([[-5.0285714285714285, 3.0], [4.0, 1.357142857142857]], id='edge_BC', clip_on=False, linestyle=(0, [4, 3]))
            c.line([[-2.5142857142857142, 1.5], [2.0, 0.6785714285714285]], id='section_MN', clip_on=False, linestyle=(0, [4, 3]))
            for object_id, points in [('edge_TB', [[0.0, 8.985714285714286], [-5.0285714285714285, 3.0]]), ('edge_TC', [[0.0, 8.985714285714286], [4.0, 1.357142857142857]]), ('edge_AB', [[0.0, 0.0], [-5.0285714285714285, 3.0]]), ('edge_AC', [[0.0, 0.0], [4.0, 1.357142857142857]]), ('edge_TA', [[0.0, 8.985714285714286], [0.0, 0.0]]), ('section_TM', [[0.0, 8.985714285714286], [-2.5142857142857142, 1.5]]), ('section_TN', [[0.0, 8.985714285714286], [2.0, 0.6785714285714285]])]:
                c.line(points, id=object_id, zorder=3, clip_on=False)
            c.line([[-2.5142857142857142, 1.5]], id='midpoint_M', zorder=4, color=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765), linewidth=1.5, linestyle='None', solid_capstyle='projecting', marker='o', markersize=6.0, markeredgewidth=1.0, markeredgecolor='#000000', markerfacecolor='#000000')
            c.line([[2.0, 0.6785714285714285]], id='midpoint_N', zorder=4, color=(1.0, 0.4980392156862745, 0.054901960784313725), linewidth=1.5, linestyle='None', solid_capstyle='projecting', marker='o', markersize=6.0, markeredgewidth=1.0, markeredgecolor='#000000', markerfacecolor='#000000')
            c.text('A', (0.0, 0.0), fontsize=18.0, fontstyle='italic', va='top', rotation_mode='default', offset_pt=(0, -8), annotation_clip=None)
            c.point([[-0.009435509642282014, 4.828148703780961]], zorder=10, s=[50], facecolors=[[0.9176470588235294, 0.34509803921568627, 0.047058823529411764, 1.0]], edgecolors=[[0.9176470588235294, 0.34509803921568627, 0.047058823529411764, 1.0]])
            return c.save(output_path)

    def draw_C03(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Solid67_C03.png'
        with Canvas(SOLID, xlim=(-5.457778918154196, 4.429207489582769), ylim=(-0.6605827211024282, 9.226403686634537), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
            c.path([[0.0, 8.985714285714286], [-2.5142857142857142, 1.5], [2.0, 0.6785714285714285], [0.0, 8.985714285714286]], [1, 2, 2, 79], id='cut_fill', alpha=1.0, zorder=1, edgecolor='none', facecolor=(0.9019607843137255, 0.9019607843137255, 0.9019607843137255, 1.0), capstyle='butt')
            c.line([[-5.0285714285714285, 3.0], [4.0, 1.357142857142857]], id='edge_BC', clip_on=False, linestyle=(0, [4, 3]))
            c.line([[-2.5142857142857142, 1.5], [2.0, 0.6785714285714285]], id='section_MN', clip_on=False, linestyle=(0, [4, 3]))
            for object_id, points in [('edge_TB', [[0.0, 8.985714285714286], [-5.0285714285714285, 3.0]]), ('edge_TC', [[0.0, 8.985714285714286], [4.0, 1.357142857142857]]), ('edge_AB', [[0.0, 0.0], [-5.0285714285714285, 3.0]]), ('edge_AC', [[0.0, 0.0], [4.0, 1.357142857142857]]), ('edge_TA', [[0.0, 8.985714285714286], [0.0, 0.0]]), ('section_TM', [[0.0, 8.985714285714286], [-2.5142857142857142, 1.5]]), ('section_TN', [[0.0, 8.985714285714286], [2.0, 0.6785714285714285]])]:
                c.line(points, id=object_id, zorder=3, clip_on=False)
            c.line([[-2.5142857142857142, 1.5]], id='midpoint_M', zorder=4, color=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765), linewidth=1.5, linestyle='None', solid_capstyle='projecting', marker='o', markersize=6.0, markeredgewidth=1.0, markeredgecolor='#000000', markerfacecolor='#000000')
            c.line([[2.0, 0.6785714285714285]], id='midpoint_N', zorder=4, color=(1.0, 0.4980392156862745, 0.054901960784313725), linewidth=1.5, linestyle='None', solid_capstyle='projecting', marker='o', markersize=6.0, markeredgewidth=1.0, markeredgecolor='#000000', markerfacecolor='#000000')
            c.text('A', (0.0, 0.0), fontsize=18.0, fontstyle='italic', va='top', rotation_mode='default', offset_pt=(0, -8), annotation_clip=None)
            c.point([[1.9998683048385768, 5.201737855217101]], zorder=10, s=[50], facecolors=[[0.9176470588235294, 0.34509803921568627, 0.047058823529411764, 1.0]], edgecolors=[[0.9176470588235294, 0.34509803921568627, 0.047058823529411764, 1.0]])
            return c.save(output_path)
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Solid67')
    parser.add_argument('output', nargs='?')
    parser.add_argument('--variant', choices=('C01', 'C02', 'C03'))
    args = parser.parse_args()
    print(Solid67().draw(args.output, variant=args.variant))
