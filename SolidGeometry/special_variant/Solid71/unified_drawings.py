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
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / 'Solid71_C01.png'
    with Canvas(SOLID, xlim=(-7.49184549297819, 4.509142039446911), ylim=(-0.9722550051596937, 11.028732527265408), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        c.path([[0.0, 8.399999999999999], [-3.5999999999999996, 1.08], [2.1, 1.05], [0.0, 8.399999999999999]], [1, 2, 2, 79], id='cut_fill', alpha=1.0, zorder=1, edgecolor='none', facecolor=(0.9019607843137255, 0.9019607843137255, 0.9019607843137255, 1.0), capstyle='butt')
        c.line([[-7.199999999999999, 2.16], [4.2, 2.1]], id='edge_BC', clip_on=False, linestyle=(0, [4, 3]))
        for object_id, points in [('edge_AB', [[0.0, 0.0], [-7.199999999999999, 2.16]]), ('edge_AC', [[0.0, 0.0], [4.2, 2.1]]), ('edge_TU', [[0.0, 8.399999999999999], [-7.199999999999999, 10.559999999999999]]), ('edge_UV', [[-7.199999999999999, 10.559999999999999], [4.2, 10.5]]), ('edge_TV', [[0.0, 8.399999999999999], [4.2, 10.5]]), ('edge_BU', [[-7.199999999999999, 2.16], [-7.199999999999999, 10.559999999999999]]), ('edge_AT', [[0.0, 0.0], [0.0, 8.399999999999999]]), ('edge_CV', [[4.2, 2.1], [4.2, 10.5]]), ('section_TM', [[0.0, 8.399999999999999], [-3.5999999999999996, 1.08]])]:
            c.line(points, id=object_id, zorder=3, clip_on=False)
        c.line([[-3.5999999999999996, 1.08], [2.1, 1.05]], id='section_MN', clip_on=False, linestyle=(0, [4, 3]))
        c.line([[2.1, 1.05], [0.0, 8.399999999999999]], id='section_NT', zorder=3, clip_on=False)
        c.line([[-3.5999999999999996, 1.08]], id='midpoint_M', zorder=4, color=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765), linewidth=1.5, linestyle='None', solid_capstyle='projecting', marker='o', markersize=6.0, markeredgewidth=1.0, markeredgecolor='#000000', markerfacecolor='#000000')
        c.line([[2.1, 1.05]], id='midpoint_N', zorder=4, color=(1.0, 0.4980392156862745, 0.054901960784313725), linewidth=1.5, linestyle='None', solid_capstyle='projecting', marker='o', markersize=6.0, markeredgewidth=1.0, markeredgecolor='#000000', markerfacecolor='#000000')
        c.text('A', (0.0, 0.0), fontsize=18.0, fontstyle='italic', va='top', rotation_mode='default', offset_pt=(0, -8), annotation_clip=None)
        c.point([[-1.4999999999999996, 10.53]], zorder=10, s=[50], facecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]], edgecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]])
        return c.save(output_path)

def C02(output_path=None):
    if output_path is None:
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / 'Solid71_C02.png'
    with Canvas(SOLID, xlim=(-7.49184549297819, 4.509142039446911), ylim=(-0.9722550051596937, 11.028732527265408), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        c.path([[0.0, 8.399999999999999], [-3.5999999999999996, 1.08], [2.1, 1.05], [0.0, 8.399999999999999]], [1, 2, 2, 79], id='cut_fill', alpha=1.0, zorder=1, edgecolor='none', facecolor=(0.9019607843137255, 0.9019607843137255, 0.9019607843137255, 1.0), capstyle='butt')
        c.line([[-7.199999999999999, 2.16], [4.2, 2.1]], id='edge_BC', clip_on=False, linestyle=(0, [4, 3]))
        for object_id, points in [('edge_AB', [[0.0, 0.0], [-7.199999999999999, 2.16]]), ('edge_AC', [[0.0, 0.0], [4.2, 2.1]]), ('edge_TU', [[0.0, 8.399999999999999], [-7.199999999999999, 10.559999999999999]]), ('edge_UV', [[-7.199999999999999, 10.559999999999999], [4.2, 10.5]]), ('edge_TV', [[0.0, 8.399999999999999], [4.2, 10.5]]), ('edge_BU', [[-7.199999999999999, 2.16], [-7.199999999999999, 10.559999999999999]]), ('edge_AT', [[0.0, 0.0], [0.0, 8.399999999999999]]), ('edge_CV', [[4.2, 2.1], [4.2, 10.5]]), ('section_TM', [[0.0, 8.399999999999999], [-3.5999999999999996, 1.08]])]:
            c.line(points, id=object_id, zorder=3, clip_on=False)
        c.line([[-3.5999999999999996, 1.08], [2.1, 1.05]], id='section_MN', clip_on=False, linestyle=(0, [4, 3]))
        c.line([[2.1, 1.05], [0.0, 8.399999999999999]], id='section_NT', zorder=3, clip_on=False)
        c.line([[-3.5999999999999996, 1.08]], id='midpoint_M', zorder=4, color=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765), linewidth=1.5, linestyle='None', solid_capstyle='projecting', marker='o', markersize=6.0, markeredgewidth=1.0, markeredgecolor='#000000', markerfacecolor='#000000')
        c.line([[2.1, 1.05]], id='midpoint_N', zorder=4, color=(1.0, 0.4980392156862745, 0.054901960784313725), linewidth=1.5, linestyle='None', solid_capstyle='projecting', marker='o', markersize=6.0, markeredgewidth=1.0, markeredgecolor='#000000', markerfacecolor='#000000')
        c.text('A', (0.0, 0.0), fontsize=18.0, fontstyle='italic', va='top', rotation_mode='default', offset_pt=(0, -8), annotation_clip=None)
        c.point([[2.1, 9.45]], zorder=10, s=[50], facecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]], edgecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]])
        return c.save(output_path)

def C03(output_path=None):
    if output_path is None:
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / 'Solid71_C03.png'
    with Canvas(SOLID, xlim=(-7.49184549297819, 4.509142039446911), ylim=(-0.9722550051596937, 11.028732527265408), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        c.path([[0.0, 8.399999999999999], [-3.5999999999999996, 1.08], [2.1, 1.05], [0.0, 8.399999999999999]], [1, 2, 2, 79], id='cut_fill', alpha=1.0, zorder=1, edgecolor='none', facecolor=(0.9019607843137255, 0.9019607843137255, 0.9019607843137255, 1.0), capstyle='butt')
        c.line([[-7.199999999999999, 2.16], [4.2, 2.1]], id='edge_BC', clip_on=False, linestyle=(0, [4, 3]))
        for object_id, points in [('edge_AB', [[0.0, 0.0], [-7.199999999999999, 2.16]]), ('edge_AC', [[0.0, 0.0], [4.2, 2.1]]), ('edge_TU', [[0.0, 8.399999999999999], [-7.199999999999999, 10.559999999999999]]), ('edge_UV', [[-7.199999999999999, 10.559999999999999], [4.2, 10.5]]), ('edge_TV', [[0.0, 8.399999999999999], [4.2, 10.5]]), ('edge_BU', [[-7.199999999999999, 2.16], [-7.199999999999999, 10.559999999999999]]), ('edge_AT', [[0.0, 0.0], [0.0, 8.399999999999999]]), ('edge_CV', [[4.2, 2.1], [4.2, 10.5]]), ('section_TM', [[0.0, 8.399999999999999], [-3.5999999999999996, 1.08]])]:
            c.line(points, id=object_id, zorder=3, clip_on=False)
        c.line([[-3.5999999999999996, 1.08], [2.1, 1.05]], id='section_MN', clip_on=False, linestyle=(0, [4, 3]))
        c.line([[2.1, 1.05], [0.0, 8.399999999999999]], id='section_NT', zorder=3, clip_on=False)
        c.line([[-3.5999999999999996, 1.08]], id='midpoint_M', zorder=4, color=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765), linewidth=1.5, linestyle='None', solid_capstyle='projecting', marker='o', markersize=6.0, markeredgewidth=1.0, markeredgecolor='#000000', markerfacecolor='#000000')
        c.line([[2.1, 1.05]], id='midpoint_N', zorder=4, color=(1.0, 0.4980392156862745, 0.054901960784313725), linewidth=1.5, linestyle='None', solid_capstyle='projecting', marker='o', markersize=6.0, markeredgewidth=1.0, markeredgecolor='#000000', markerfacecolor='#000000')
        c.text('A', (0.0, 0.0), fontsize=18.0, fontstyle='italic', va='top', rotation_mode='default', offset_pt=(0, -8), annotation_clip=None)
        c.point([[-7.199999999999999, 6.359999999999999]], zorder=10, s=[50], facecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]], edgecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]])
        return c.save(output_path)

def C04(output_path=None):
    if output_path is None:
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / 'Solid71_C04.png'
    with Canvas(SOLID, xlim=(-7.49184549297819, 4.509142039446911), ylim=(-0.9722550051596937, 11.028732527265408), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        c.path([[0.0, 8.399999999999999], [-3.5999999999999996, 1.08], [2.1, 1.05], [0.0, 8.399999999999999]], [1, 2, 2, 79], id='cut_fill', alpha=1.0, zorder=1, edgecolor='none', facecolor=(0.9019607843137255, 0.9019607843137255, 0.9019607843137255, 1.0), capstyle='butt')
        c.line([[-7.199999999999999, 2.16], [4.2, 2.1]], id='edge_BC', clip_on=False, linestyle=(0, [4, 3]))
        for object_id, points in [('edge_AB', [[0.0, 0.0], [-7.199999999999999, 2.16]]), ('edge_AC', [[0.0, 0.0], [4.2, 2.1]]), ('edge_TU', [[0.0, 8.399999999999999], [-7.199999999999999, 10.559999999999999]]), ('edge_UV', [[-7.199999999999999, 10.559999999999999], [4.2, 10.5]]), ('edge_TV', [[0.0, 8.399999999999999], [4.2, 10.5]]), ('edge_BU', [[-7.199999999999999, 2.16], [-7.199999999999999, 10.559999999999999]]), ('edge_AT', [[0.0, 0.0], [0.0, 8.399999999999999]]), ('edge_CV', [[4.2, 2.1], [4.2, 10.5]]), ('section_TM', [[0.0, 8.399999999999999], [-3.5999999999999996, 1.08]])]:
            c.line(points, id=object_id, zorder=3, clip_on=False)
        c.line([[-3.5999999999999996, 1.08], [2.1, 1.05]], id='section_MN', clip_on=False, linestyle=(0, [4, 3]))
        c.line([[2.1, 1.05], [0.0, 8.399999999999999]], id='section_NT', zorder=3, clip_on=False)
        c.line([[-3.5999999999999996, 1.08]], id='midpoint_M', zorder=4, color=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765), linewidth=1.5, linestyle='None', solid_capstyle='projecting', marker='o', markersize=6.0, markeredgewidth=1.0, markeredgecolor='#000000', markerfacecolor='#000000')
        c.line([[2.1, 1.05]], id='midpoint_N', zorder=4, color=(1.0, 0.4980392156862745, 0.054901960784313725), linewidth=1.5, linestyle='None', solid_capstyle='projecting', marker='o', markersize=6.0, markeredgewidth=1.0, markeredgecolor='#000000', markerfacecolor='#000000')
        c.text('A', (0.0, 0.0), fontsize=18.0, fontstyle='italic', va='top', rotation_mode='default', offset_pt=(0, -8), annotation_clip=None)
        c.point([[0.0, 4.199999999999999]], zorder=10, s=[50], facecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]], edgecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]])
        return c.save(output_path)

def C05(output_path=None):
    if output_path is None:
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / 'Solid71_C05.png'
    with Canvas(SOLID, xlim=(-7.49184549297819, 4.509142039446911), ylim=(-0.9722550051596937, 11.028732527265408), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        c.path([[0.0, 8.399999999999999], [-3.5999999999999996, 1.08], [2.1, 1.05], [0.0, 8.399999999999999]], [1, 2, 2, 79], id='cut_fill', alpha=1.0, zorder=1, edgecolor='none', facecolor=(0.9019607843137255, 0.9019607843137255, 0.9019607843137255, 1.0), capstyle='butt')
        c.line([[-7.199999999999999, 2.16], [4.2, 2.1]], id='edge_BC', clip_on=False, linestyle=(0, [4, 3]))
        for object_id, points in [('edge_AB', [[0.0, 0.0], [-7.199999999999999, 2.16]]), ('edge_AC', [[0.0, 0.0], [4.2, 2.1]]), ('edge_TU', [[0.0, 8.399999999999999], [-7.199999999999999, 10.559999999999999]]), ('edge_UV', [[-7.199999999999999, 10.559999999999999], [4.2, 10.5]]), ('edge_TV', [[0.0, 8.399999999999999], [4.2, 10.5]]), ('edge_BU', [[-7.199999999999999, 2.16], [-7.199999999999999, 10.559999999999999]]), ('edge_AT', [[0.0, 0.0], [0.0, 8.399999999999999]]), ('edge_CV', [[4.2, 2.1], [4.2, 10.5]]), ('section_TM', [[0.0, 8.399999999999999], [-3.5999999999999996, 1.08]])]:
            c.line(points, id=object_id, zorder=3, clip_on=False)
        c.line([[-3.5999999999999996, 1.08], [2.1, 1.05]], id='section_MN', clip_on=False, linestyle=(0, [4, 3]))
        c.line([[2.1, 1.05], [0.0, 8.399999999999999]], id='section_NT', zorder=3, clip_on=False)
        c.line([[-3.5999999999999996, 1.08]], id='midpoint_M', zorder=4, color=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765), linewidth=1.5, linestyle='None', solid_capstyle='projecting', marker='o', markersize=6.0, markeredgewidth=1.0, markeredgecolor='#000000', markerfacecolor='#000000')
        c.line([[2.1, 1.05]], id='midpoint_N', zorder=4, color=(1.0, 0.4980392156862745, 0.054901960784313725), linewidth=1.5, linestyle='None', solid_capstyle='projecting', marker='o', markersize=6.0, markeredgewidth=1.0, markeredgecolor='#000000', markerfacecolor='#000000')
        c.text('A', (0.0, 0.0), fontsize=18.0, fontstyle='italic', va='top', rotation_mode='default', offset_pt=(0, -8), annotation_clip=None)
        c.point([[-3.5999999999999996, 9.479999999999999]], zorder=10, s=[50], facecolors=[[0.9176470588235294, 0.34509803921568627, 0.047058823529411764, 1.0]], edgecolors=[[0.9176470588235294, 0.34509803921568627, 0.047058823529411764, 1.0]])
        c.point([[-1.4999999999999996, 10.53]], zorder=10, s=[50], facecolors=[[0.9176470588235294, 0.34509803921568627, 0.047058823529411764, 1.0]], edgecolors=[[0.9176470588235294, 0.34509803921568627, 0.047058823529411764, 1.0]])
        return c.save(output_path)
