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
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / 'Solid68_C01.png'
    with Canvas(SOLID, xlim=(-5.256004818401922, 5.271177227585009), ylim=(-1.2711772275850106, 9.256004818401921), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        c.path([[-5.0, 0.0], [5.0, 0.0], [0.0, 5.0], [-5.0, 0.0]], [1, 2, 2, 79], id='cut_fill', alpha=1.0, zorder=1, edgecolor='none', facecolor=(0.9019607843137255, 0.9019607843137255, 0.9019607843137255, 1.0), capstyle='butt')
        for object_id, points in [('edge_BC', [[-5.0, 0.0], [5.0, 0.0]]), ('edge_AB', [[0.0, 2.0], [-5.0, 0.0]]), ('edge_AC', [[0.0, 2.0], [5.0, 0.0]]), ('edge_BD', [[-5.0, 0.0], [0.0, 8.0]]), ('edge_AD', [[0.0, 2.0], [0.0, 8.0]]), ('edge_CD', [[5.0, 0.0], [0.0, 8.0]]), ('section_CP', [[5.0, 0.0], [0.0, 5.0]]), ('section_PB', [[0.0, 5.0], [-5.0, 0.0]])]:
            c.line(points, id=object_id, zorder=3, clip_on=False)
        c.line([[0.0, 5.0]], id='midpoint_P', zorder=4, color=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765), linewidth=1.5, linestyle='None', solid_capstyle='projecting', marker='o', markersize=6.0, markeredgewidth=1.0, markeredgecolor='#000000', markerfacecolor='#000000')
        c.text('A', (0.0, 2.0), fontsize=18.0, fontstyle='italic', ha='left', va='bottom', rotation_mode='default', offset_pt=(8, 6), annotation_clip=None)
        c.point([[2.5, 4.0]], zorder=10, s=[50], facecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]], edgecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]])
        return c.save(output_path)

def C02(output_path=None):
    if output_path is None:
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / 'Solid68_C02.png'
    with Canvas(SOLID, xlim=(-5.256004818401922, 5.271177227585009), ylim=(-1.2711772275850106, 9.256004818401921), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        c.path([[-5.0, 0.0], [5.0, 0.0], [0.0, 5.0], [-5.0, 0.0]], [1, 2, 2, 79], id='cut_fill', alpha=1.0, zorder=1, edgecolor='none', facecolor=(0.9019607843137255, 0.9019607843137255, 0.9019607843137255, 1.0), capstyle='butt')
        for object_id, points in [('edge_BC', [[-5.0, 0.0], [5.0, 0.0]]), ('edge_AB', [[0.0, 2.0], [-5.0, 0.0]]), ('edge_AC', [[0.0, 2.0], [5.0, 0.0]]), ('edge_BD', [[-5.0, 0.0], [0.0, 8.0]]), ('edge_AD', [[0.0, 2.0], [0.0, 8.0]]), ('edge_CD', [[5.0, 0.0], [0.0, 8.0]]), ('section_CP', [[5.0, 0.0], [0.0, 5.0]]), ('section_PB', [[0.0, 5.0], [-5.0, 0.0]])]:
            c.line(points, id=object_id, zorder=3, clip_on=False)
        c.line([[0.0, 5.0]], id='midpoint_P', zorder=4, color=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765), linewidth=1.5, linestyle='None', solid_capstyle='projecting', marker='o', markersize=6.0, markeredgewidth=1.0, markeredgecolor='#000000', markerfacecolor='#000000')
        c.text('A', (0.0, 2.0), fontsize=18.0, fontstyle='italic', ha='left', va='bottom', rotation_mode='default', offset_pt=(8, 6), annotation_clip=None)
        c.point([[-2.5, 1.0]], zorder=10, s=[50], facecolors=[[0.9176470588235294, 0.34509803921568627, 0.047058823529411764, 1.0]], edgecolors=[[0.9176470588235294, 0.34509803921568627, 0.047058823529411764, 1.0]])
        c.point([[2.5, 1.0]], zorder=10, s=[50], facecolors=[[0.9176470588235294, 0.34509803921568627, 0.047058823529411764, 1.0]], edgecolors=[[0.9176470588235294, 0.34509803921568627, 0.047058823529411764, 1.0]])
        return c.save(output_path)

def C03(output_path=None):
    if output_path is None:
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / 'Solid68_C03.png'
    with Canvas(SOLID, xlim=(-5.256004818401922, 5.271177227585009), ylim=(-1.2711772275850106, 9.256004818401921), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        c.path([[-5.0, 0.0], [5.0, 0.0], [0.0, 5.0], [-5.0, 0.0]], [1, 2, 2, 79], id='cut_fill', alpha=1.0, zorder=1, edgecolor='none', facecolor=(0.9019607843137255, 0.9019607843137255, 0.9019607843137255, 1.0), capstyle='butt')
        for object_id, points in [('edge_BC', [[-5.0, 0.0], [5.0, 0.0]]), ('edge_AB', [[0.0, 2.0], [-5.0, 0.0]]), ('edge_AC', [[0.0, 2.0], [5.0, 0.0]]), ('edge_BD', [[-5.0, 0.0], [0.0, 8.0]]), ('edge_AD', [[0.0, 2.0], [0.0, 8.0]]), ('edge_CD', [[5.0, 0.0], [0.0, 8.0]]), ('section_CP', [[5.0, 0.0], [0.0, 5.0]]), ('section_PB', [[0.0, 5.0], [-5.0, 0.0]])]:
            c.line(points, id=object_id, zorder=3, clip_on=False)
        c.line([[0.0, 5.0]], id='midpoint_P', zorder=4, color=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765), linewidth=1.5, linestyle='None', solid_capstyle='projecting', marker='o', markersize=6.0, markeredgewidth=1.0, markeredgecolor='#000000', markerfacecolor='#000000')
        c.text('A', (0.0, 2.0), fontsize=18.0, fontstyle='italic', ha='left', va='bottom', rotation_mode='default', offset_pt=(8, 6), annotation_clip=None)
        c.point([[-2.5, 4.0]], zorder=10, s=[50], facecolors=[[0.9176470588235294, 0.34509803921568627, 0.047058823529411764, 1.0]], edgecolors=[[0.9176470588235294, 0.34509803921568627, 0.047058823529411764, 1.0]])
        c.point([[2.5, 4.0]], zorder=10, s=[50], facecolors=[[0.9176470588235294, 0.34509803921568627, 0.047058823529411764, 1.0]], edgecolors=[[0.9176470588235294, 0.34509803921568627, 0.047058823529411764, 1.0]])
        return c.save(output_path)

def C04(output_path=None):
    if output_path is None:
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / 'Solid68_C04.png'
    with Canvas(SOLID, xlim=(-5.256004818401922, 5.271177227585009), ylim=(-1.2711772275850106, 9.256004818401921), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        c.path([[-5.0, 0.0], [5.0, 0.0], [0.0, 5.0], [-5.0, 0.0]], [1, 2, 2, 79], id='cut_fill', alpha=1.0, zorder=1, edgecolor='none', facecolor=(0.9019607843137255, 0.9019607843137255, 0.9019607843137255, 1.0), capstyle='butt')
        for object_id, points in [('edge_BC', [[-5.0, 0.0], [5.0, 0.0]]), ('edge_AB', [[0.0, 2.0], [-5.0, 0.0]]), ('edge_AC', [[0.0, 2.0], [5.0, 0.0]]), ('edge_BD', [[-5.0, 0.0], [0.0, 8.0]]), ('edge_AD', [[0.0, 2.0], [0.0, 8.0]]), ('edge_CD', [[5.0, 0.0], [0.0, 8.0]]), ('section_CP', [[5.0, 0.0], [0.0, 5.0]]), ('section_PB', [[0.0, 5.0], [-5.0, 0.0]])]:
            c.line(points, id=object_id, zorder=3, clip_on=False)
        c.line([[0.0, 5.0]], id='midpoint_P', zorder=4, color=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765), linewidth=1.5, linestyle='None', solid_capstyle='projecting', marker='o', markersize=6.0, markeredgewidth=1.0, markeredgecolor='#000000', markerfacecolor='#000000')
        c.text('A', (0.0, 2.0), fontsize=18.0, fontstyle='italic', ha='left', va='bottom', rotation_mode='default', offset_pt=(8, 6), annotation_clip=None)
        c.point([[-2.5, 1.0]], zorder=10, s=[50], facecolors=[[0.1450980392156863, 0.38823529411764707, 0.9215686274509803, 1.0]], edgecolors=[[0.1450980392156863, 0.38823529411764707, 0.9215686274509803, 1.0]])
        c.point([[2.5, 1.0]], zorder=10, s=[50], facecolors=[[0.1450980392156863, 0.38823529411764707, 0.9215686274509803, 1.0]], edgecolors=[[0.1450980392156863, 0.38823529411764707, 0.9215686274509803, 1.0]])
        c.line([[-2.5, 1.0], [2.5, 1.0]], zorder=9, color='#2563EB', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
        return c.save(output_path)

def C05(output_path=None):
    if output_path is None:
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / 'Solid68_C05.png'
    with Canvas(SOLID, xlim=(-5.256004818401922, 5.271177227585009), ylim=(-1.2711772275850106, 9.256004818401921), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        c.path([[-5.0, 0.0], [5.0, 0.0], [0.0, 5.0], [-5.0, 0.0]], [1, 2, 2, 79], id='cut_fill', alpha=1.0, zorder=1, edgecolor='none', facecolor=(0.9019607843137255, 0.9019607843137255, 0.9019607843137255, 1.0), capstyle='butt')
        for object_id, points in [('edge_BC', [[-5.0, 0.0], [5.0, 0.0]]), ('edge_AB', [[0.0, 2.0], [-5.0, 0.0]]), ('edge_AC', [[0.0, 2.0], [5.0, 0.0]]), ('edge_BD', [[-5.0, 0.0], [0.0, 8.0]]), ('edge_AD', [[0.0, 2.0], [0.0, 8.0]]), ('edge_CD', [[5.0, 0.0], [0.0, 8.0]]), ('section_CP', [[5.0, 0.0], [0.0, 5.0]]), ('section_PB', [[0.0, 5.0], [-5.0, 0.0]])]:
            c.line(points, id=object_id, zorder=3, clip_on=False)
        c.line([[0.0, 5.0]], id='midpoint_P', zorder=4, color=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765), linewidth=1.5, linestyle='None', solid_capstyle='projecting', marker='o', markersize=6.0, markeredgewidth=1.0, markeredgecolor='#000000', markerfacecolor='#000000')
        c.text('A', (0.0, 2.0), fontsize=18.0, fontstyle='italic', ha='left', va='bottom', rotation_mode='default', offset_pt=(8, 6), annotation_clip=None)
        for object_id, points in [(None, [[0.0, 0.0]]), (None, [[-2.5, 1.0]]), (None, [[2.5, 1.0]])]:
            c.point(points, id=object_id, zorder=10, s=[50], facecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]], edgecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]])
        for object_id, points in [(None, [[0.0, 0.0], [-2.5, 1.0]]), (None, [[-2.5, 1.0], [2.5, 1.0]]), (None, [[2.5, 1.0], [0.0, 0.0]])]:
            c.line(points, id=object_id, zorder=9, color='#DC2626', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
        return c.save(output_path)
