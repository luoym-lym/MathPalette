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
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / 'Solid67_C01.png'
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

def C02(output_path=None):
    if output_path is None:
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / 'Solid67_C02.png'
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

def C03(output_path=None):
    if output_path is None:
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / 'Solid67_C03.png'
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
