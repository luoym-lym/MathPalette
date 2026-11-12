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
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / 'Plane585_C01.png'
    with Canvas(PLANE, xlim=(-0.1860465116279073, 8.186046511627907), ylim=(-1.1860465116279073, 7.186046511627907), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        for object_id, points in [('grid_vertical_0', [[0, 0], [0, 6]]), ('grid_vertical_1', [[1, 0], [1, 6]]), ('grid_vertical_2', [[2, 0], [2, 6]]), ('grid_vertical_3', [[3, 0], [3, 6]]), ('grid_vertical_4', [[4, 0], [4, 6]]), ('grid_vertical_5', [[5, 0], [5, 6]]), ('grid_vertical_6', [[6, 0], [6, 6]]), ('grid_vertical_7', [[7, 0], [7, 6]]), ('grid_vertical_8', [[8, 0], [8, 6]]), ('grid_horizontal_0', [[0, 0], [8, 0]]), ('grid_horizontal_1', [[0, 1], [8, 1]]), ('grid_horizontal_2', [[0, 2], [8, 2]]), ('grid_horizontal_3', [[0, 3], [8, 3]]), ('grid_horizontal_4', [[0, 4], [8, 4]]), ('grid_horizontal_5', [[0, 5], [8, 5]]), ('grid_horizontal_6', [[0, 6], [8, 6]])]:
            c.line(points, id=object_id, zorder=1, color='#AAAAAA')
        c.line([[1, 5], [4, 5]], id='given_segment_AB', zorder=3)
        c.line([[4, 1], [7, 1]], id='given_segment_CD', zorder=3)
        for object_id, center, radius in [('point_marker_X', [3, 3], 0.05046834625322997), ('point_marker_Y', [5, 3], 0.05046834625322997), ('point_marker_Z', [4, 4], 0.05046834625322997), ('point_marker_T', [4, 3], 0.05046834625322997)]:
            c.circle(center, radius, id=object_id, zorder=4, fill=False)
        c.text('X', (3, 3), id='label_X', clip_on=True, fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(-16, 16), annotation_clip=False)
        c.text('Y', (5, 3), id='label_Y', clip_on=True, fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(16, 16), annotation_clip=False)
        c.text('Z', (4, 4), id='label_Z', clip_on=True, fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(16, 16), annotation_clip=False)
        c.text('T', (4, 3), id='label_T', clip_on=True, fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(16, -16), annotation_clip=False)
        c.point([[3.0, 3.0]], zorder=10, s=[50], facecolors=[[0.9176470588235294, 0.34509803921568627, 0.047058823529411764, 1.0]], edgecolors=[[0.9176470588235294, 0.34509803921568627, 0.047058823529411764, 1.0]])
        c.line([[3.0, 3.0], [4.0, 5.0]], zorder=9, color='#16A34A', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
        c.line([[3.0, 3.0], [4.0, 1.0]], zorder=9, color='#16A34A', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
        return c.save(output_path)

def C02(output_path=None):
    if output_path is None:
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / 'Plane585_C02.png'
    with Canvas(PLANE, xlim=(-0.1860465116279073, 8.186046511627907), ylim=(-1.1860465116279073, 7.186046511627907), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        for object_id, points in [('grid_vertical_0', [[0, 0], [0, 6]]), ('grid_vertical_1', [[1, 0], [1, 6]]), ('grid_vertical_2', [[2, 0], [2, 6]]), ('grid_vertical_3', [[3, 0], [3, 6]]), ('grid_vertical_4', [[4, 0], [4, 6]]), ('grid_vertical_5', [[5, 0], [5, 6]]), ('grid_vertical_6', [[6, 0], [6, 6]]), ('grid_vertical_7', [[7, 0], [7, 6]]), ('grid_vertical_8', [[8, 0], [8, 6]]), ('grid_horizontal_0', [[0, 0], [8, 0]]), ('grid_horizontal_1', [[0, 1], [8, 1]]), ('grid_horizontal_2', [[0, 2], [8, 2]]), ('grid_horizontal_3', [[0, 3], [8, 3]]), ('grid_horizontal_4', [[0, 4], [8, 4]]), ('grid_horizontal_5', [[0, 5], [8, 5]]), ('grid_horizontal_6', [[0, 6], [8, 6]])]:
            c.line(points, id=object_id, zorder=1, color='#AAAAAA')
        c.line([[1, 5], [4, 5]], id='given_segment_AB', zorder=3)
        c.line([[4, 1], [7, 1]], id='given_segment_CD', zorder=3)
        for object_id, center, radius in [('point_marker_X', [3, 3], 0.05046834625322997), ('point_marker_Y', [5, 3], 0.05046834625322997), ('point_marker_Z', [4, 4], 0.05046834625322997), ('point_marker_T', [4, 3], 0.05046834625322997)]:
            c.circle(center, radius, id=object_id, zorder=4, fill=False)
        c.text('X', (3, 3), id='label_X', clip_on=True, fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(-16, 16), annotation_clip=False)
        c.text('Y', (5, 3), id='label_Y', clip_on=True, fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(16, 16), annotation_clip=False)
        c.text('Z', (4, 4), id='label_Z', clip_on=True, fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(16, 16), annotation_clip=False)
        c.text('T', (4, 3), id='label_T', clip_on=True, fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(16, -16), annotation_clip=False)
        c.point([[3.0, 3.0]], zorder=10, s=[50], facecolors=[[0.9176470588235294, 0.34509803921568627, 0.047058823529411764, 1.0]], edgecolors=[[0.9176470588235294, 0.34509803921568627, 0.047058823529411764, 1.0]])
        c.line([[3.0, 3.0], [4.0, 5.0]], zorder=9, color='#EA580C', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
        c.line([[3.0, 3.0], [4.0, 1.0]], zorder=9, color='#EA580C', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
        return c.save(output_path)

def C03(output_path=None):
    if output_path is None:
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / 'Plane585_C03.png'
    with Canvas(PLANE, xlim=(-0.1860465116279073, 8.186046511627907), ylim=(-1.1860465116279073, 7.186046511627907), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        for object_id, points in [('grid_vertical_0', [[0, 0], [0, 6]]), ('grid_vertical_1', [[1, 0], [1, 6]]), ('grid_vertical_2', [[2, 0], [2, 6]]), ('grid_vertical_3', [[3, 0], [3, 6]]), ('grid_vertical_4', [[4, 0], [4, 6]]), ('grid_vertical_5', [[5, 0], [5, 6]]), ('grid_vertical_6', [[6, 0], [6, 6]]), ('grid_vertical_7', [[7, 0], [7, 6]]), ('grid_vertical_8', [[8, 0], [8, 6]]), ('grid_horizontal_0', [[0, 0], [8, 0]]), ('grid_horizontal_1', [[0, 1], [8, 1]]), ('grid_horizontal_2', [[0, 2], [8, 2]]), ('grid_horizontal_3', [[0, 3], [8, 3]]), ('grid_horizontal_4', [[0, 4], [8, 4]]), ('grid_horizontal_5', [[0, 5], [8, 5]]), ('grid_horizontal_6', [[0, 6], [8, 6]])]:
            c.line(points, id=object_id, zorder=1, color='#AAAAAA')
        c.line([[1, 5], [4, 5]], id='given_segment_AB', zorder=3)
        c.line([[4, 1], [7, 1]], id='given_segment_CD', zorder=3)
        for object_id, center, radius in [('point_marker_X', [3, 3], 0.05046834625322997), ('point_marker_Y', [5, 3], 0.05046834625322997), ('point_marker_Z', [4, 4], 0.05046834625322997), ('point_marker_T', [4, 3], 0.05046834625322997)]:
            c.circle(center, radius, id=object_id, zorder=4, fill=False)
        c.text('X', (3, 3), id='label_X', clip_on=True, fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(-16, 16), annotation_clip=False)
        c.text('Y', (5, 3), id='label_Y', clip_on=True, fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(16, 16), annotation_clip=False)
        c.text('Z', (4, 4), id='label_Z', clip_on=True, fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(16, 16), annotation_clip=False)
        c.text('T', (4, 3), id='label_T', clip_on=True, fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(16, -16), annotation_clip=False)
        c.point([[3.0, 3.0]], zorder=10, s=[50], facecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]], edgecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]])
        c.line([[3.0, 3.0], [4.0, 5.0]], zorder=9, color='#EA580C', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
        c.line([[3.0, 3.0], [4.0, 1.0]], zorder=9, color='#EA580C', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
        return c.save(output_path)

def C04(output_path=None):
    if output_path is None:
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / 'Plane585_C04.png'
    with Canvas(PLANE, xlim=(-0.1860465116279073, 8.186046511627907), ylim=(-1.1860465116279073, 7.186046511627907), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        for object_id, points in [('grid_vertical_0', [[0, 0], [0, 6]]), ('grid_vertical_1', [[1, 0], [1, 6]]), ('grid_vertical_2', [[2, 0], [2, 6]]), ('grid_vertical_3', [[3, 0], [3, 6]]), ('grid_vertical_4', [[4, 0], [4, 6]]), ('grid_vertical_5', [[5, 0], [5, 6]]), ('grid_vertical_6', [[6, 0], [6, 6]]), ('grid_vertical_7', [[7, 0], [7, 6]]), ('grid_vertical_8', [[8, 0], [8, 6]]), ('grid_horizontal_0', [[0, 0], [8, 0]]), ('grid_horizontal_1', [[0, 1], [8, 1]]), ('grid_horizontal_2', [[0, 2], [8, 2]]), ('grid_horizontal_3', [[0, 3], [8, 3]]), ('grid_horizontal_4', [[0, 4], [8, 4]]), ('grid_horizontal_5', [[0, 5], [8, 5]]), ('grid_horizontal_6', [[0, 6], [8, 6]])]:
            c.line(points, id=object_id, zorder=1, color='#AAAAAA')
        c.line([[1, 5], [4, 5]], id='given_segment_AB', zorder=3)
        c.line([[4, 1], [7, 1]], id='given_segment_CD', zorder=3)
        for object_id, center, radius in [('point_marker_X', [3, 3], 0.05046834625322997), ('point_marker_Y', [5, 3], 0.05046834625322997), ('point_marker_Z', [4, 4], 0.05046834625322997), ('point_marker_T', [4, 3], 0.05046834625322997)]:
            c.circle(center, radius, id=object_id, zorder=4, fill=False)
        c.text('X', (3, 3), id='label_X', clip_on=True, fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(-16, 16), annotation_clip=False)
        c.text('Y', (5, 3), id='label_Y', clip_on=True, fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(16, 16), annotation_clip=False)
        c.text('Z', (4, 4), id='label_Z', clip_on=True, fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(16, 16), annotation_clip=False)
        c.text('T', (4, 3), id='label_T', clip_on=True, fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(16, -16), annotation_clip=False)
        c.point([[3.0, 3.0]], zorder=10, s=[50], facecolors=[[0.9176470588235294, 0.34509803921568627, 0.047058823529411764, 1.0]], edgecolors=[[0.9176470588235294, 0.34509803921568627, 0.047058823529411764, 1.0]])
        c.line([[3.0, 3.0], [4.0, 5.0]], zorder=9, color='#2563EB', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
        c.line([[3.0, 3.0], [4.0, 1.0]], zorder=9, color='#2563EB', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
        return c.save(output_path)
