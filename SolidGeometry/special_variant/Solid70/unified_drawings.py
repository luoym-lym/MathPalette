"""Frozen, previously passed Special drawings on the unified protocol. No new Pass/Collect."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[3]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

def C01(output_path=None):
    if output_path is None:
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / 'Solid70_C01.png'
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

def C02(output_path=None):
    if output_path is None:
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / 'Solid70_C02.png'
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

def C03(output_path=None):
    if output_path is None:
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / 'Solid70_C03.png'
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

def C04(output_path=None):
    if output_path is None:
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / 'Solid70_C04.png'
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
