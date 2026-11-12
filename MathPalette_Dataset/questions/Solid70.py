"""Collected question Solid70; construction on the shared drawing protocol."""
from pathlib import Path
import sys
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from MathPalette_Dataset.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Solid70:
    variants = ('C01', 'C02', 'C03', 'C04')

    def __init__(self):
        self.id = 'Solid70'
        self.source_dataset = 'Author Designed'
        self.source_key = 'midpoint-cut:square_pyramid_corner'
        self.question = 'The pyramid shown has a square base and volume 480. Each marked point is the midpoint of the edge on which it lies. Find the volume of the part containing vertex A after the pyramid is cut along the shaded plane.'
        self.answer = 60
        self.answer_type = 'number'
        self.query = self.question
        self.points = {'A': [0, 0, 0], 'B': [12, 0, 0], 'C': [12, 12, 0], 'D': [0, 12, 0], 'S': [6, 6, 10], 'M': [6, 0, 0], 'N': [0, 6, 0]}

    def draw(self, output_path=None, *, variant=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if variant not in self.variants:
                raise ValueError('Unknown Special variant: ' + str(variant))
            return getattr(self, 'draw_' + variant)(output_path)
        with Canvas(SOLID, xlim=[-6.983477957515103, 8.7834779575151], ylim=[-2.6261220524907607, 13.140833862539441], projection=[[-0.55, 0.7, 0.14], [0.25, 0.2, 0.85]], origin=[0, 0, 0], offset=[0, 0]) as c:
            c.fill(c.project([self.points['S'], self.points['M'], self.points['N']]), facecolor='#E6E6E6', alpha=1, id='cut_fill')
            c.line(c.project([self.points['C'], self.points['D']]), id='edge_CD', linestyle=(0, [4, 3]), clip_on=False)
            c.line(c.project([self.points['B'], self.points['C']]), id='edge_BC', linestyle=(0, [4, 3]), clip_on=False)
            for object_id, points in [('edge_AB', c.project([self.points['A'], self.points['B']])), ('edge_AD', c.project([self.points['A'], self.points['D']])), ('edge_AS', c.project([self.points['A'], self.points['S']])), ('edge_BS', c.project([self.points['B'], self.points['S']]))]:
                c.line(points, id=object_id, clip_on=False, zorder=3)
            c.line(c.project([self.points['C'], self.points['S']]), id='edge_CS', linestyle=(0, [4, 3]), clip_on=False)
            c.line(c.project([self.points['D'], self.points['S']]), id='edge_DS', clip_on=False, zorder=3)
            c.line(c.project([self.points['S'], self.points['M']]), id='section_SM', clip_on=False, zorder=3)
            c.line(c.project([self.points['M'], self.points['N']]), id='section_MN', linestyle=(0, [4, 3]), clip_on=False)
            c.line(c.project([self.points['N'], self.points['S']]), id='section_NS', clip_on=False, zorder=3)
            c.point(c.project([self.points['M']]), filled=True, id='midpoint_M')
            c.point(c.project([self.points['N']]), filled=True, id='midpoint_N')
            c.text('A', c.project(self.points['A']), offset_pt=[0, -8], vertex=True, va='top', id='label_A')
            return c.save(output_path)

    def draw_C01(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Solid70_C01.png'
        with Canvas(SOLID, xlim=(-6.983477957515103, 8.7834779575151), ylim=(-2.6261220524907607, 13.140833862539441), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
            c.path([[2.3, 11.2], [-3.3000000000000003, 1.5], [4.199999999999999, 1.2000000000000002], [2.3, 11.2]], [1, 2, 2, 79], id='cut_fill', alpha=1.0, zorder=1, edgecolor='none', facecolor=(0.9019607843137255, 0.9019607843137255, 0.9019607843137255, 1.0), capstyle='butt')
            c.line([[1.799999999999999, 5.4], [8.399999999999999, 2.4000000000000004]], id='edge_CD', clip_on=False, linestyle=(0, [4, 3]))
            c.line([[-6.6000000000000005, 3.0], [1.799999999999999, 5.4]], id='edge_BC', clip_on=False, linestyle=(0, [4, 3]))
            for object_id, points in [('edge_AB', [[0.0, 0.0], [-6.6000000000000005, 3.0]]), ('edge_AD', [[0.0, 0.0], [8.399999999999999, 2.4000000000000004]]), ('edge_AS', [[0.0, 0.0], [2.3, 11.2]]), ('edge_BS', [[-6.6000000000000005, 3.0], [2.3, 11.2]])]:
                c.line(points, id=object_id, zorder=3, clip_on=False)
            c.line([[1.799999999999999, 5.4], [2.3, 11.2]], id='edge_CS', clip_on=False, linestyle=(0, [4, 3]))
            c.line([[8.399999999999999, 2.4000000000000004], [2.3, 11.2]], id='edge_DS', zorder=3, clip_on=False)
            c.line([[2.3, 11.2], [-3.3000000000000003, 1.5]], id='section_SM', zorder=3, clip_on=False)
            c.line([[-3.3000000000000003, 1.5], [4.199999999999999, 1.2000000000000002]], id='section_MN', clip_on=False, linestyle=(0, [4, 3]))
            c.line([[4.199999999999999, 1.2000000000000002], [2.3, 11.2]], id='section_NS', zorder=3, clip_on=False)
            c.line([[-3.3000000000000003, 1.5]], id='midpoint_M', zorder=4, color=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765), linewidth=1.5, linestyle='None', solid_capstyle='projecting', marker='o', markersize=6.0, markeredgewidth=1.0, markeredgecolor='#000000', markerfacecolor='#000000')
            c.line([[4.199999999999999, 1.2000000000000002]], id='midpoint_N', zorder=4, color=(1.0, 0.4980392156862745, 0.054901960784313725), linewidth=1.5, linestyle='None', solid_capstyle='projecting', marker='o', markersize=6.0, markeredgewidth=1.0, markeredgecolor='#000000', markerfacecolor='#000000')
            c.text('A', (0.0, 0.0), fontsize=18.0, fontstyle='italic', va='top', rotation_mode='default', offset_pt=(0, -8), annotation_clip=None)
            c.point([[-2.4000000000000012, 4.2]], zorder=10, s=[50], facecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]], edgecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]])
            return c.save(output_path)

    def draw_C02(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Solid70_C02.png'
        with Canvas(SOLID, xlim=(-6.983477957515103, 8.7834779575151), ylim=(-2.6261220524907607, 13.140833862539441), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
            c.path([[2.3, 11.2], [-3.3000000000000003, 1.5], [4.199999999999999, 1.2000000000000002], [2.3, 11.2]], [1, 2, 2, 79], id='cut_fill', alpha=1.0, zorder=1, edgecolor='none', facecolor=(0.9019607843137255, 0.9019607843137255, 0.9019607843137255, 1.0), capstyle='butt')
            c.line([[1.799999999999999, 5.4], [8.399999999999999, 2.4000000000000004]], id='edge_CD', clip_on=False, linestyle=(0, [4, 3]))
            c.line([[-6.6000000000000005, 3.0], [1.799999999999999, 5.4]], id='edge_BC', clip_on=False, linestyle=(0, [4, 3]))
            for object_id, points in [('edge_AB', [[0.0, 0.0], [-6.6000000000000005, 3.0]]), ('edge_AD', [[0.0, 0.0], [8.399999999999999, 2.4000000000000004]]), ('edge_AS', [[0.0, 0.0], [2.3, 11.2]]), ('edge_BS', [[-6.6000000000000005, 3.0], [2.3, 11.2]])]:
                c.line(points, id=object_id, zorder=3, clip_on=False)
            c.line([[1.799999999999999, 5.4], [2.3, 11.2]], id='edge_CS', clip_on=False, linestyle=(0, [4, 3]))
            c.line([[8.399999999999999, 2.4000000000000004], [2.3, 11.2]], id='edge_DS', zorder=3, clip_on=False)
            c.line([[2.3, 11.2], [-3.3000000000000003, 1.5]], id='section_SM', zorder=3, clip_on=False)
            c.line([[-3.3000000000000003, 1.5], [4.199999999999999, 1.2000000000000002]], id='section_MN', clip_on=False, linestyle=(0, [4, 3]))
            c.line([[4.199999999999999, 1.2000000000000002], [2.3, 11.2]], id='section_NS', zorder=3, clip_on=False)
            c.line([[-3.3000000000000003, 1.5]], id='midpoint_M', zorder=4, color=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765), linewidth=1.5, linestyle='None', solid_capstyle='projecting', marker='o', markersize=6.0, markeredgewidth=1.0, markeredgecolor='#000000', markerfacecolor='#000000')
            c.line([[4.199999999999999, 1.2000000000000002]], id='midpoint_N', zorder=4, color=(1.0, 0.4980392156862745, 0.054901960784313725), linewidth=1.5, linestyle='None', solid_capstyle='projecting', marker='o', markersize=6.0, markeredgewidth=1.0, markeredgecolor='#000000', markerfacecolor='#000000')
            c.text('A', (0.0, 0.0), fontsize=18.0, fontstyle='italic', va='top', rotation_mode='default', offset_pt=(0, -8), annotation_clip=None)
            c.point([[5.35, 6.8]], zorder=10, s=[50], facecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]], edgecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]])
            return c.save(output_path)

    def draw_C03(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Solid70_C03.png'
        with Canvas(SOLID, xlim=(-6.983477957515103, 8.7834779575151), ylim=(-2.6261220524907607, 13.140833862539441), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
            c.path([[2.3, 11.2], [-3.3000000000000003, 1.5], [4.199999999999999, 1.2000000000000002], [2.3, 11.2]], [1, 2, 2, 79], id='cut_fill', alpha=1.0, zorder=1, edgecolor='none', facecolor=(0.9019607843137255, 0.9019607843137255, 0.9019607843137255, 1.0), capstyle='butt')
            c.line([[1.799999999999999, 5.4], [8.399999999999999, 2.4000000000000004]], id='edge_CD', clip_on=False, linestyle=(0, [4, 3]))
            c.line([[-6.6000000000000005, 3.0], [1.799999999999999, 5.4]], id='edge_BC', clip_on=False, linestyle=(0, [4, 3]))
            for object_id, points in [('edge_AB', [[0.0, 0.0], [-6.6000000000000005, 3.0]]), ('edge_AD', [[0.0, 0.0], [8.399999999999999, 2.4000000000000004]]), ('edge_AS', [[0.0, 0.0], [2.3, 11.2]]), ('edge_BS', [[-6.6000000000000005, 3.0], [2.3, 11.2]])]:
                c.line(points, id=object_id, zorder=3, clip_on=False)
            c.line([[1.799999999999999, 5.4], [2.3, 11.2]], id='edge_CS', clip_on=False, linestyle=(0, [4, 3]))
            c.line([[8.399999999999999, 2.4000000000000004], [2.3, 11.2]], id='edge_DS', zorder=3, clip_on=False)
            c.line([[2.3, 11.2], [-3.3000000000000003, 1.5]], id='section_SM', zorder=3, clip_on=False)
            c.line([[-3.3000000000000003, 1.5], [4.199999999999999, 1.2000000000000002]], id='section_MN', clip_on=False, linestyle=(0, [4, 3]))
            c.line([[4.199999999999999, 1.2000000000000002], [2.3, 11.2]], id='section_NS', zorder=3, clip_on=False)
            c.line([[-3.3000000000000003, 1.5]], id='midpoint_M', zorder=4, color=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765), linewidth=1.5, linestyle='None', solid_capstyle='projecting', marker='o', markersize=6.0, markeredgewidth=1.0, markeredgecolor='#000000', markerfacecolor='#000000')
            c.line([[4.199999999999999, 1.2000000000000002]], id='midpoint_N', zorder=4, color=(1.0, 0.4980392156862745, 0.054901960784313725), linewidth=1.5, linestyle='None', solid_capstyle='projecting', marker='o', markersize=6.0, markeredgewidth=1.0, markeredgecolor='#000000', markerfacecolor='#000000')
            c.text('A', (0.0, 0.0), fontsize=18.0, fontstyle='italic', va='top', rotation_mode='default', offset_pt=(0, -8), annotation_clip=None)
            c.point([[-2.1500000000000004, 7.1]], zorder=10, s=[50], facecolors=[[0.9176470588235294, 0.34509803921568627, 0.047058823529411764, 1.0]], edgecolors=[[0.9176470588235294, 0.34509803921568627, 0.047058823529411764, 1.0]])
            c.point([[2.05, 8.3]], zorder=10, s=[50], facecolors=[[0.9176470588235294, 0.34509803921568627, 0.047058823529411764, 1.0]], edgecolors=[[0.9176470588235294, 0.34509803921568627, 0.047058823529411764, 1.0]])
            return c.save(output_path)

    def draw_C04(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Solid70_C04.png'
        with Canvas(SOLID, xlim=(-6.983477957515103, 8.7834779575151), ylim=(-2.6261220524907607, 13.140833862539441), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
            c.path([[2.3, 11.2], [-3.3000000000000003, 1.5], [4.199999999999999, 1.2000000000000002], [2.3, 11.2]], [1, 2, 2, 79], id='cut_fill', alpha=1.0, zorder=1, edgecolor='none', facecolor=(0.9019607843137255, 0.9019607843137255, 0.9019607843137255, 1.0), capstyle='butt')
            c.line([[1.799999999999999, 5.4], [8.399999999999999, 2.4000000000000004]], id='edge_CD', clip_on=False, linestyle=(0, [4, 3]))
            c.line([[-6.6000000000000005, 3.0], [1.799999999999999, 5.4]], id='edge_BC', clip_on=False, linestyle=(0, [4, 3]))
            for object_id, points in [('edge_AB', [[0.0, 0.0], [-6.6000000000000005, 3.0]]), ('edge_AD', [[0.0, 0.0], [8.399999999999999, 2.4000000000000004]]), ('edge_AS', [[0.0, 0.0], [2.3, 11.2]]), ('edge_BS', [[-6.6000000000000005, 3.0], [2.3, 11.2]])]:
                c.line(points, id=object_id, zorder=3, clip_on=False)
            c.line([[1.799999999999999, 5.4], [2.3, 11.2]], id='edge_CS', clip_on=False, linestyle=(0, [4, 3]))
            c.line([[8.399999999999999, 2.4000000000000004], [2.3, 11.2]], id='edge_DS', zorder=3, clip_on=False)
            c.line([[2.3, 11.2], [-3.3000000000000003, 1.5]], id='section_SM', zorder=3, clip_on=False)
            c.line([[-3.3000000000000003, 1.5], [4.199999999999999, 1.2000000000000002]], id='section_MN', clip_on=False, linestyle=(0, [4, 3]))
            c.line([[4.199999999999999, 1.2000000000000002], [2.3, 11.2]], id='section_NS', zorder=3, clip_on=False)
            c.line([[-3.3000000000000003, 1.5]], id='midpoint_M', zorder=4, color=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765), linewidth=1.5, linestyle='None', solid_capstyle='projecting', marker='o', markersize=6.0, markeredgewidth=1.0, markeredgecolor='#000000', markerfacecolor='#000000')
            c.line([[4.199999999999999, 1.2000000000000002]], id='midpoint_N', zorder=4, color=(1.0, 0.4980392156862745, 0.054901960784313725), linewidth=1.5, linestyle='None', solid_capstyle='projecting', marker='o', markersize=6.0, markeredgewidth=1.0, markeredgecolor='#000000', markerfacecolor='#000000')
            c.text('A', (0.0, 0.0), fontsize=18.0, fontstyle='italic', va='top', rotation_mode='default', offset_pt=(0, -8), annotation_clip=None)
            c.point([[5.099999999999998, 3.9000000000000004]], zorder=10, s=[50], facecolors=[[0.1450980392156863, 0.38823529411764707, 0.9215686274509803, 1.0]], edgecolors=[[0.1450980392156863, 0.38823529411764707, 0.9215686274509803, 1.0]])
            c.point([[-2.4000000000000012, 4.2]], zorder=10, s=[50], facecolors=[[0.1450980392156863, 0.38823529411764707, 0.9215686274509803, 1.0]], edgecolors=[[0.1450980392156863, 0.38823529411764707, 0.9215686274509803, 1.0]])
            c.line([[5.099999999999998, 3.9000000000000004], [-2.4000000000000012, 4.2]], zorder=9, color='#2563EB', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            return c.save(output_path)
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Solid70')
    parser.add_argument('output', nargs='?')
    parser.add_argument('--variant', choices=('C01', 'C02', 'C03', 'C04'))
    args = parser.parse_args()
    print(Solid70().draw(args.output, variant=args.variant))
