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
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / 'Solid73_C01.png'
    with Canvas(SOLID, xlim=(-0.3194144470766229, 3.4524195679314893), ylim=(-1.1292619149114638, 2.6425721000966487), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        for object_id, points in [('net_edge_B0_B1', [[0.0, 0.0], [1.0, 0.0]]), ('net_edge_B1_T1', [[1.0, 0.0], [1.0, 1.5]]), ('net_edge_T0_T1', [[0.0, 1.5], [1.0, 1.5]]), ('net_edge_B0_T0', [[0.0, 0.0], [0.0, 1.5]]), ('net_edge_B1_B2', [[1.0, 0.0], [2.0, 0.0]]), ('net_edge_B2_T2', [[2.0, 0.0], [2.0, 1.5]]), ('net_edge_T1_T2', [[1.0, 1.5], [2.0, 1.5]]), ('net_edge_B2_B3', [[2.0, 0.0], [3.0, 0.0]]), ('net_edge_B3_T3', [[3.0, 0.0], [3.0, 1.5]]), ('net_edge_T2_T3', [[2.0, 1.5], [3.0, 1.5]]), ('net_edge_P_T1', [[0.5, 2.3660254037844384], [1.0, 1.5]]), ('net_edge_P_T0', [[0.5, 2.3660254037844384], [0.0, 1.5]]), ('net_edge_B2_Q', [[2.0, 0.0], [2.5, -0.8660254037844386]]), ('net_edge_B3_Q', [[3.0, 0.0], [2.5, -0.8660254037844386]])]:
            c.line(points, id=object_id, zorder=3, clip_on=False)
        c.text('P', (0.5, 2.3660254037844384), fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(0, 16), annotation_clip=None)
        c.text('Q', (2.5, -0.8660254037844386), fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(0, -16), annotation_clip=None)
        c.text('R', (2.0, 0.0), fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(-15, -12), annotation_clip=None)
        c.text('S', (3.0, 0.0), fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(13, 0), annotation_clip=None)
        c.line([[0.5, 2.3660254037844384], [3.0, 0.0]], zorder=9, color='#DC2626', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
        c.point([[3.0, 0.0]], zorder=10, s=[50], facecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]], edgecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]])
        return c.save(output_path)

def C02(output_path=None):
    if output_path is None:
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / 'Solid73_C02.png'
    with Canvas(SOLID, xlim=(-0.3194144470766229, 3.4524195679314893), ylim=(-1.1292619149114638, 2.6425721000966487), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        for object_id, points in [('net_edge_B0_B1', [[0.0, 0.0], [1.0, 0.0]]), ('net_edge_B1_T1', [[1.0, 0.0], [1.0, 1.5]]), ('net_edge_T0_T1', [[0.0, 1.5], [1.0, 1.5]]), ('net_edge_B0_T0', [[0.0, 0.0], [0.0, 1.5]]), ('net_edge_B1_B2', [[1.0, 0.0], [2.0, 0.0]]), ('net_edge_B2_T2', [[2.0, 0.0], [2.0, 1.5]]), ('net_edge_T1_T2', [[1.0, 1.5], [2.0, 1.5]]), ('net_edge_B2_B3', [[2.0, 0.0], [3.0, 0.0]]), ('net_edge_B3_T3', [[3.0, 0.0], [3.0, 1.5]]), ('net_edge_T2_T3', [[2.0, 1.5], [3.0, 1.5]]), ('net_edge_P_T1', [[0.5, 2.3660254037844384], [1.0, 1.5]]), ('net_edge_P_T0', [[0.5, 2.3660254037844384], [0.0, 1.5]]), ('net_edge_B2_Q', [[2.0, 0.0], [2.5, -0.8660254037844386]]), ('net_edge_B3_Q', [[3.0, 0.0], [2.5, -0.8660254037844386]])]:
            c.line(points, id=object_id, zorder=3, clip_on=False)
        c.text('P', (0.5, 2.3660254037844384), fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(0, 16), annotation_clip=None)
        c.text('Q', (2.5, -0.8660254037844386), fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(0, -16), annotation_clip=None)
        c.text('R', (2.0, 0.0), fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(-15, -12), annotation_clip=None)
        c.text('S', (3.0, 0.0), fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(13, 0), annotation_clip=None)
        c.point([[0.0, 1.5]], zorder=10, s=[50], facecolors=[[0.08627450980392157, 0.6392156862745098, 0.2901960784313726, 1.0]], edgecolors=[[0.08627450980392157, 0.6392156862745098, 0.2901960784313726, 1.0]])
        c.point([[2.0, 0.0]], zorder=10, s=[50], facecolors=[[0.08627450980392157, 0.6392156862745098, 0.2901960784313726, 1.0]], edgecolors=[[0.08627450980392157, 0.6392156862745098, 0.2901960784313726, 1.0]])
        c.point([[1.0, 1.5]], zorder=10, s=[50], facecolors=[[0.9176470588235294, 0.34509803921568627, 0.047058823529411764, 1.0]], edgecolors=[[0.9176470588235294, 0.34509803921568627, 0.047058823529411764, 1.0]])
        c.point([[2.5, -0.8660254037844386]], zorder=10, s=[50], facecolors=[[0.9176470588235294, 0.34509803921568627, 0.047058823529411764, 1.0]], edgecolors=[[0.9176470588235294, 0.34509803921568627, 0.047058823529411764, 1.0]])
        c.point([[0.5, 2.3660254037844384]], zorder=10, s=[50], facecolors=[[0.1450980392156863, 0.38823529411764707, 0.9215686274509803, 1.0]], edgecolors=[[0.1450980392156863, 0.38823529411764707, 0.9215686274509803, 1.0]])
        c.point([[3.0, 0.0]], zorder=10, s=[50], facecolors=[[0.1450980392156863, 0.38823529411764707, 0.9215686274509803, 1.0]], edgecolors=[[0.1450980392156863, 0.38823529411764707, 0.9215686274509803, 1.0]])
        return c.save(output_path)

def C03(output_path=None):
    if output_path is None:
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / 'Solid73_C03.png'
    with Canvas(SOLID, xlim=(-0.3194144470766229, 3.4524195679314893), ylim=(-1.1292619149114638, 2.6425721000966487), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        for object_id, points in [('net_edge_B0_B1', [[0.0, 0.0], [1.0, 0.0]]), ('net_edge_B1_T1', [[1.0, 0.0], [1.0, 1.5]]), ('net_edge_T0_T1', [[0.0, 1.5], [1.0, 1.5]]), ('net_edge_B0_T0', [[0.0, 0.0], [0.0, 1.5]]), ('net_edge_B1_B2', [[1.0, 0.0], [2.0, 0.0]]), ('net_edge_B2_T2', [[2.0, 0.0], [2.0, 1.5]]), ('net_edge_T1_T2', [[1.0, 1.5], [2.0, 1.5]]), ('net_edge_B2_B3', [[2.0, 0.0], [3.0, 0.0]]), ('net_edge_B3_T3', [[3.0, 0.0], [3.0, 1.5]]), ('net_edge_T2_T3', [[2.0, 1.5], [3.0, 1.5]]), ('net_edge_P_T1', [[0.5, 2.3660254037844384], [1.0, 1.5]]), ('net_edge_P_T0', [[0.5, 2.3660254037844384], [0.0, 1.5]]), ('net_edge_B2_Q', [[2.0, 0.0], [2.5, -0.8660254037844386]]), ('net_edge_B3_Q', [[3.0, 0.0], [2.5, -0.8660254037844386]])]:
            c.line(points, id=object_id, zorder=3, clip_on=False)
        c.text('P', (0.5, 2.3660254037844384), fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(0, 16), annotation_clip=None)
        c.text('Q', (2.5, -0.8660254037844386), fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(0, -16), annotation_clip=None)
        c.text('R', (2.0, 0.0), fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(-15, -12), annotation_clip=None)
        c.text('S', (3.0, 0.0), fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(13, 0), annotation_clip=None)
        c.point([[0.5, 2.3660254037844384]], zorder=10, s=[50], facecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]], edgecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]])
        c.point([[2.5, -0.8660254037844386]], zorder=10, s=[50], facecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]], edgecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]])
        c.point([[0.0, 1.5]], zorder=10, s=[50], facecolors=[[0.1450980392156863, 0.38823529411764707, 0.9215686274509803, 1.0]], edgecolors=[[0.1450980392156863, 0.38823529411764707, 0.9215686274509803, 1.0]])
        c.point([[3.0, 0.0]], zorder=10, s=[50], facecolors=[[0.1450980392156863, 0.38823529411764707, 0.9215686274509803, 1.0]], edgecolors=[[0.1450980392156863, 0.38823529411764707, 0.9215686274509803, 1.0]])
        c.point([[1.0, 1.5]], zorder=10, s=[50], facecolors=[[0.08627450980392157, 0.6392156862745098, 0.2901960784313726, 1.0]], edgecolors=[[0.08627450980392157, 0.6392156862745098, 0.2901960784313726, 1.0]])
        c.point([[2.0, 0.0]], zorder=10, s=[50], facecolors=[[0.08627450980392157, 0.6392156862745098, 0.2901960784313726, 1.0]], edgecolors=[[0.08627450980392157, 0.6392156862745098, 0.2901960784313726, 1.0]])
        return c.save(output_path)

def C04(output_path=None):
    if output_path is None:
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / 'Solid73_C04.png'
    with Canvas(SOLID, xlim=(-0.3194144470766229, 3.4524195679314893), ylim=(-1.1292619149114638, 2.6425721000966487), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        for object_id, points in [('net_edge_B0_B1', [[0.0, 0.0], [1.0, 0.0]]), ('net_edge_B1_T1', [[1.0, 0.0], [1.0, 1.5]]), ('net_edge_T0_T1', [[0.0, 1.5], [1.0, 1.5]]), ('net_edge_B0_T0', [[0.0, 0.0], [0.0, 1.5]]), ('net_edge_B1_B2', [[1.0, 0.0], [2.0, 0.0]]), ('net_edge_B2_T2', [[2.0, 0.0], [2.0, 1.5]]), ('net_edge_T1_T2', [[1.0, 1.5], [2.0, 1.5]]), ('net_edge_B2_B3', [[2.0, 0.0], [3.0, 0.0]]), ('net_edge_B3_T3', [[3.0, 0.0], [3.0, 1.5]]), ('net_edge_T2_T3', [[2.0, 1.5], [3.0, 1.5]]), ('net_edge_P_T1', [[0.5, 2.3660254037844384], [1.0, 1.5]]), ('net_edge_P_T0', [[0.5, 2.3660254037844384], [0.0, 1.5]]), ('net_edge_B2_Q', [[2.0, 0.0], [2.5, -0.8660254037844386]]), ('net_edge_B3_Q', [[3.0, 0.0], [2.5, -0.8660254037844386]])]:
            c.line(points, id=object_id, zorder=3, clip_on=False)
        c.text('P', (0.5, 2.3660254037844384), fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(0, 16), annotation_clip=None)
        c.text('Q', (2.5, -0.8660254037844386), fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(0, -16), annotation_clip=None)
        c.text('R', (2.0, 0.0), fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(-15, -12), annotation_clip=None)
        c.text('S', (3.0, 0.0), fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(13, 0), annotation_clip=None)
        c.point([[0.5, 2.3660254037844384]], zorder=10, s=[50], facecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]], edgecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]])
        c.point([[3.0, 0.0]], zorder=10, s=[50], facecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]], edgecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]])
        return c.save(output_path)
