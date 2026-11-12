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
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / 'Solid74_C01.png'
    with Canvas(SOLID, xlim=(-0.2784482720289403, 4.09723746072793), ylim=(-1.6698298632670028, 2.7058558694898682), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        for object_id, points in [('edge_v0_0_v1_0', [[0.0, 0.0], [1.0, 0.0]]), ('edge_v1_0_v1_1', [[1.0, 0.0], [1.0, 1.0]]), ('edge_v0_1_v1_1', [[0.0, 1.0], [1.0, 1.0]]), ('edge_v0_0_v0_1', [[0.0, 0.0], [0.0, 1.0]]), ('edge_v1_0_v2_0', [[1.0, 0.0], [2.0, 0.0]]), ('edge_v2_0_v2_1', [[2.0, 0.0], [2.0, 1.0]]), ('edge_v1_1_v2_1', [[1.0, 1.0], [2.0, 1.0]]), ('edge_v2_1_v2_2', [[2.0, 1.0], [2.0, 2.0]]), ('edge_v1_2_v2_2', [[1.0, 2.0], [2.0, 2.0]]), ('edge_v1_1_v1_2', [[1.0, 1.0], [1.0, 2.0]]), ('edge_v2_-1_v3_-1', [[2.0, -1.0], [3.0, -1.0]]), ('edge_v3_-1_v3_0', [[3.0, -1.0], [3.0, 0.0]]), ('edge_v2_0_v3_0', [[2.0, 0.0], [3.0, 0.0]]), ('edge_v2_-1_v2_0', [[2.0, -1.0], [2.0, 0.0]]), ('edge_v3_0_v3_1', [[3.0, 0.0], [3.0, 1.0]]), ('edge_v2_1_v3_1', [[2.0, 1.0], [3.0, 1.0]]), ('edge_v3_0_v4_0', [[3.0, 0.0], [4.0, 0.0]]), ('edge_v4_0_v4_1', [[4.0, 0.0], [4.0, 1.0]]), ('edge_v3_1_v4_1', [[3.0, 1.0], [4.0, 1.0]])]:
            c.line(points, id=object_id, zorder=3, clip_on=False)
        c.text('P', (1.0, 2.0), fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(0, 16), annotation_clip=None)
        c.text('Q', (3.0, -1.0), fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(12, -12), annotation_clip=None)
        c.text('R', (0.0, 1.0), fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(-14, 0), annotation_clip=None)
        c.text('S', (1.0, 1.0), fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(22, 17), annotation_clip=None)
        c.point([[1.0, 2.0]], zorder=10, s=[50], facecolors=[[0.1450980392156863, 0.38823529411764707, 0.9215686274509803, 1.0]], edgecolors=[[0.1450980392156863, 0.38823529411764707, 0.9215686274509803, 1.0]])
        c.point([[3.0, -1.0]], zorder=10, s=[50], facecolors=[[0.1450980392156863, 0.38823529411764707, 0.9215686274509803, 1.0]], edgecolors=[[0.1450980392156863, 0.38823529411764707, 0.9215686274509803, 1.0]])
        c.point([[0.0, 1.0]], zorder=10, s=[50], facecolors=[[0.08627450980392157, 0.6392156862745098, 0.2901960784313726, 1.0]], edgecolors=[[0.08627450980392157, 0.6392156862745098, 0.2901960784313726, 1.0]])
        return c.save(output_path)

def C02(output_path=None):
    if output_path is None:
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / 'Solid74_C02.png'
    with Canvas(SOLID, xlim=(-0.2784482720289403, 4.09723746072793), ylim=(-1.6698298632670028, 2.7058558694898682), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        for object_id, points in [('edge_v0_0_v1_0', [[0.0, 0.0], [1.0, 0.0]]), ('edge_v1_0_v1_1', [[1.0, 0.0], [1.0, 1.0]]), ('edge_v0_1_v1_1', [[0.0, 1.0], [1.0, 1.0]]), ('edge_v0_0_v0_1', [[0.0, 0.0], [0.0, 1.0]]), ('edge_v1_0_v2_0', [[1.0, 0.0], [2.0, 0.0]]), ('edge_v2_0_v2_1', [[2.0, 0.0], [2.0, 1.0]]), ('edge_v1_1_v2_1', [[1.0, 1.0], [2.0, 1.0]]), ('edge_v2_1_v2_2', [[2.0, 1.0], [2.0, 2.0]]), ('edge_v1_2_v2_2', [[1.0, 2.0], [2.0, 2.0]]), ('edge_v1_1_v1_2', [[1.0, 1.0], [1.0, 2.0]]), ('edge_v2_-1_v3_-1', [[2.0, -1.0], [3.0, -1.0]]), ('edge_v3_-1_v3_0', [[3.0, -1.0], [3.0, 0.0]]), ('edge_v2_0_v3_0', [[2.0, 0.0], [3.0, 0.0]]), ('edge_v2_-1_v2_0', [[2.0, -1.0], [2.0, 0.0]]), ('edge_v3_0_v3_1', [[3.0, 0.0], [3.0, 1.0]]), ('edge_v2_1_v3_1', [[2.0, 1.0], [3.0, 1.0]]), ('edge_v3_0_v4_0', [[3.0, 0.0], [4.0, 0.0]]), ('edge_v4_0_v4_1', [[4.0, 0.0], [4.0, 1.0]]), ('edge_v3_1_v4_1', [[3.0, 1.0], [4.0, 1.0]])]:
            c.line(points, id=object_id, zorder=3, clip_on=False)
        c.text('P', (1.0, 2.0), fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(0, 16), annotation_clip=None)
        c.text('Q', (3.0, -1.0), fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(12, -12), annotation_clip=None)
        c.text('R', (0.0, 1.0), fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(-14, 0), annotation_clip=None)
        c.text('S', (1.0, 1.0), fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(22, 17), annotation_clip=None)
        c.point([[1.0, 2.0]], zorder=10, s=[50], facecolors=[[0.08627450980392157, 0.6392156862745098, 0.2901960784313726, 1.0]], edgecolors=[[0.08627450980392157, 0.6392156862745098, 0.2901960784313726, 1.0]])
        c.point([[3.0, -1.0]], zorder=10, s=[50], facecolors=[[0.08627450980392157, 0.6392156862745098, 0.2901960784313726, 1.0]], edgecolors=[[0.08627450980392157, 0.6392156862745098, 0.2901960784313726, 1.0]])
        c.line([[1.0, 2.0], [3.0, -1.0]], zorder=9, color='#16A34A', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
        return c.save(output_path)

def C03(output_path=None):
    if output_path is None:
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / 'Solid74_C03.png'
    with Canvas(SOLID, xlim=(-0.2784482720289403, 4.09723746072793), ylim=(-1.6698298632670028, 2.7058558694898682), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        for object_id, points in [('edge_v0_0_v1_0', [[0.0, 0.0], [1.0, 0.0]]), ('edge_v1_0_v1_1', [[1.0, 0.0], [1.0, 1.0]]), ('edge_v0_1_v1_1', [[0.0, 1.0], [1.0, 1.0]]), ('edge_v0_0_v0_1', [[0.0, 0.0], [0.0, 1.0]]), ('edge_v1_0_v2_0', [[1.0, 0.0], [2.0, 0.0]]), ('edge_v2_0_v2_1', [[2.0, 0.0], [2.0, 1.0]]), ('edge_v1_1_v2_1', [[1.0, 1.0], [2.0, 1.0]]), ('edge_v2_1_v2_2', [[2.0, 1.0], [2.0, 2.0]]), ('edge_v1_2_v2_2', [[1.0, 2.0], [2.0, 2.0]]), ('edge_v1_1_v1_2', [[1.0, 1.0], [1.0, 2.0]]), ('edge_v2_-1_v3_-1', [[2.0, -1.0], [3.0, -1.0]]), ('edge_v3_-1_v3_0', [[3.0, -1.0], [3.0, 0.0]]), ('edge_v2_0_v3_0', [[2.0, 0.0], [3.0, 0.0]]), ('edge_v2_-1_v2_0', [[2.0, -1.0], [2.0, 0.0]]), ('edge_v3_0_v3_1', [[3.0, 0.0], [3.0, 1.0]]), ('edge_v2_1_v3_1', [[2.0, 1.0], [3.0, 1.0]]), ('edge_v3_0_v4_0', [[3.0, 0.0], [4.0, 0.0]]), ('edge_v4_0_v4_1', [[4.0, 0.0], [4.0, 1.0]]), ('edge_v3_1_v4_1', [[3.0, 1.0], [4.0, 1.0]])]:
            c.line(points, id=object_id, zorder=3, clip_on=False)
        c.text('P', (1.0, 2.0), fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(0, 16), annotation_clip=None)
        c.text('Q', (3.0, -1.0), fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(12, -12), annotation_clip=None)
        c.text('R', (0.0, 1.0), fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(-14, 0), annotation_clip=None)
        c.text('S', (1.0, 1.0), fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(22, 17), annotation_clip=None)
        c.point([[1.0, 2.0]], zorder=10, s=[50], facecolors=[[0.9176470588235294, 0.34509803921568627, 0.047058823529411764, 1.0]], edgecolors=[[0.9176470588235294, 0.34509803921568627, 0.047058823529411764, 1.0]])
        c.point([[3.0, -1.0]], zorder=10, s=[50], facecolors=[[0.9176470588235294, 0.34509803921568627, 0.047058823529411764, 1.0]], edgecolors=[[0.9176470588235294, 0.34509803921568627, 0.047058823529411764, 1.0]])
        c.line([[1.0, 2.0], [3.0, -1.0]], zorder=9, color='#EA580C', solid_capstyle='butt')
        return c.save(output_path)

def C04(output_path=None):
    if output_path is None:
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / 'Solid74_C04.png'
    with Canvas(SOLID, xlim=(-0.2784482720289403, 4.09723746072793), ylim=(-1.6698298632670028, 2.7058558694898682), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        for object_id, points in [('edge_v0_0_v1_0', [[0.0, 0.0], [1.0, 0.0]]), ('edge_v1_0_v1_1', [[1.0, 0.0], [1.0, 1.0]]), ('edge_v0_1_v1_1', [[0.0, 1.0], [1.0, 1.0]]), ('edge_v0_0_v0_1', [[0.0, 0.0], [0.0, 1.0]]), ('edge_v1_0_v2_0', [[1.0, 0.0], [2.0, 0.0]]), ('edge_v2_0_v2_1', [[2.0, 0.0], [2.0, 1.0]]), ('edge_v1_1_v2_1', [[1.0, 1.0], [2.0, 1.0]]), ('edge_v2_1_v2_2', [[2.0, 1.0], [2.0, 2.0]]), ('edge_v1_2_v2_2', [[1.0, 2.0], [2.0, 2.0]]), ('edge_v1_1_v1_2', [[1.0, 1.0], [1.0, 2.0]]), ('edge_v2_-1_v3_-1', [[2.0, -1.0], [3.0, -1.0]]), ('edge_v3_-1_v3_0', [[3.0, -1.0], [3.0, 0.0]]), ('edge_v2_0_v3_0', [[2.0, 0.0], [3.0, 0.0]]), ('edge_v2_-1_v2_0', [[2.0, -1.0], [2.0, 0.0]]), ('edge_v3_0_v3_1', [[3.0, 0.0], [3.0, 1.0]]), ('edge_v2_1_v3_1', [[2.0, 1.0], [3.0, 1.0]]), ('edge_v3_0_v4_0', [[3.0, 0.0], [4.0, 0.0]]), ('edge_v4_0_v4_1', [[4.0, 0.0], [4.0, 1.0]]), ('edge_v3_1_v4_1', [[3.0, 1.0], [4.0, 1.0]])]:
            c.line(points, id=object_id, zorder=3, clip_on=False)
        c.text('P', (1.0, 2.0), fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(0, 16), annotation_clip=None)
        c.text('Q', (3.0, -1.0), fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(12, -12), annotation_clip=None)
        c.text('R', (0.0, 1.0), fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(-14, 0), annotation_clip=None)
        c.text('S', (1.0, 1.0), fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(22, 17), annotation_clip=None)
        c.point([[1.0, 2.0]], zorder=10, s=[50], facecolors=[[0.1450980392156863, 0.38823529411764707, 0.9215686274509803, 1.0]], edgecolors=[[0.1450980392156863, 0.38823529411764707, 0.9215686274509803, 1.0]])
        c.point([[1.0, 1.0]], zorder=10, s=[50], facecolors=[[0.1450980392156863, 0.38823529411764707, 0.9215686274509803, 1.0]], edgecolors=[[0.1450980392156863, 0.38823529411764707, 0.9215686274509803, 1.0]])
        c.point([[0.0, 1.0]], zorder=10, s=[50], facecolors=[[0.08627450980392157, 0.6392156862745098, 0.2901960784313726, 1.0]], edgecolors=[[0.08627450980392157, 0.6392156862745098, 0.2901960784313726, 1.0]])
        return c.save(output_path)

def C05(output_path=None):
    if output_path is None:
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / 'Solid74_C05.png'
    with Canvas(SOLID, xlim=(-0.2784482720289403, 4.09723746072793), ylim=(-1.6698298632670028, 2.7058558694898682), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        for object_id, points in [('edge_v0_0_v1_0', [[0.0, 0.0], [1.0, 0.0]]), ('edge_v1_0_v1_1', [[1.0, 0.0], [1.0, 1.0]]), ('edge_v0_1_v1_1', [[0.0, 1.0], [1.0, 1.0]]), ('edge_v0_0_v0_1', [[0.0, 0.0], [0.0, 1.0]]), ('edge_v1_0_v2_0', [[1.0, 0.0], [2.0, 0.0]]), ('edge_v2_0_v2_1', [[2.0, 0.0], [2.0, 1.0]]), ('edge_v1_1_v2_1', [[1.0, 1.0], [2.0, 1.0]]), ('edge_v2_1_v2_2', [[2.0, 1.0], [2.0, 2.0]]), ('edge_v1_2_v2_2', [[1.0, 2.0], [2.0, 2.0]]), ('edge_v1_1_v1_2', [[1.0, 1.0], [1.0, 2.0]]), ('edge_v2_-1_v3_-1', [[2.0, -1.0], [3.0, -1.0]]), ('edge_v3_-1_v3_0', [[3.0, -1.0], [3.0, 0.0]]), ('edge_v2_0_v3_0', [[2.0, 0.0], [3.0, 0.0]]), ('edge_v2_-1_v2_0', [[2.0, -1.0], [2.0, 0.0]]), ('edge_v3_0_v3_1', [[3.0, 0.0], [3.0, 1.0]]), ('edge_v2_1_v3_1', [[2.0, 1.0], [3.0, 1.0]]), ('edge_v3_0_v4_0', [[3.0, 0.0], [4.0, 0.0]]), ('edge_v4_0_v4_1', [[4.0, 0.0], [4.0, 1.0]]), ('edge_v3_1_v4_1', [[3.0, 1.0], [4.0, 1.0]])]:
            c.line(points, id=object_id, zorder=3, clip_on=False)
        c.text('P', (1.0, 2.0), fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(0, 16), annotation_clip=None)
        c.text('Q', (3.0, -1.0), fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(12, -12), annotation_clip=None)
        c.text('R', (0.0, 1.0), fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(-14, 0), annotation_clip=None)
        c.text('S', (1.0, 1.0), fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(22, 17), annotation_clip=None)
        c.point([[1.0, 2.0]], zorder=10, s=[50], facecolors=[[0.08627450980392157, 0.6392156862745098, 0.2901960784313726, 1.0]], edgecolors=[[0.08627450980392157, 0.6392156862745098, 0.2901960784313726, 1.0]])
        c.point([[1.0, 1.0]], zorder=10, s=[50], facecolors=[[0.08627450980392157, 0.6392156862745098, 0.2901960784313726, 1.0]], edgecolors=[[0.08627450980392157, 0.6392156862745098, 0.2901960784313726, 1.0]])
        c.line([[1.0, 2.0], [1.0, 1.0]], zorder=9, color='#16A34A', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
        return c.save(output_path)
