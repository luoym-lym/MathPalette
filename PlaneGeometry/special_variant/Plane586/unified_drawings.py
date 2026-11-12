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
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / 'Plane586_C01.png'
    with Canvas(PLANE, xlim=(-0.7093023255813948, 8.709302325581394), ylim=(-0.20930232558139483, 9.209302325581394), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        for object_id, points in [('grid_vertical_0', [[0, 0], [0, 9]]), ('grid_vertical_1', [[1, 0], [1, 9]]), ('grid_vertical_2', [[2, 0], [2, 9]]), ('grid_vertical_3', [[3, 0], [3, 9]]), ('grid_vertical_4', [[4, 0], [4, 9]]), ('grid_vertical_5', [[5, 0], [5, 9]]), ('grid_vertical_6', [[6, 0], [6, 9]]), ('grid_vertical_7', [[7, 0], [7, 9]]), ('grid_vertical_8', [[8, 0], [8, 9]]), ('grid_horizontal_0', [[0, 0], [8, 0]]), ('grid_horizontal_1', [[0, 1], [8, 1]]), ('grid_horizontal_2', [[0, 2], [8, 2]]), ('grid_horizontal_3', [[0, 3], [8, 3]]), ('grid_horizontal_4', [[0, 4], [8, 4]]), ('grid_horizontal_5', [[0, 5], [8, 5]]), ('grid_horizontal_6', [[0, 6], [8, 6]]), ('grid_horizontal_7', [[0, 7], [8, 7]]), ('grid_horizontal_8', [[0, 8], [8, 8]]), ('grid_horizontal_9', [[0, 9], [8, 9]])]:
            c.line(points, id=object_id, zorder=1, color='#AAAAAA')
        c.line([[1, 3], [7, 3]], id='given_segment_AB', zorder=3)
        c.line([[4, 2], [4, 8]], id='given_segment_CD', zorder=3)
        for object_id, center, radius in [('point_marker_X', [3, 4], 0.05677688953488369), ('point_marker_Y', [5, 4], 0.05677688953488369), ('point_marker_Z', [4, 4], 0.05677688953488369), ('point_marker_T', [2, 6], 0.05677688953488369)]:
            c.circle(center, radius, id=object_id, zorder=4, fill=False)
        c.text('X', (3, 4), id='label_X', clip_on=True, fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(-14, 14), annotation_clip=False)
        c.text('Y', (5, 4), id='label_Y', clip_on=True, fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(14, 14), annotation_clip=False)
        c.text('Z', (4, 4), id='label_Z', clip_on=True, fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(14, -14), annotation_clip=False)
        c.text('T', (2, 6), id='label_T', clip_on=True, fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(-14, 14), annotation_clip=False)
        c.point([[3.0, 4.0]], zorder=10, s=[50], facecolors=[[0.9176470588235294, 0.34509803921568627, 0.047058823529411764, 1.0]], edgecolors=[[0.9176470588235294, 0.34509803921568627, 0.047058823529411764, 1.0]])
        c.line([[3, 4], [1, 3]], zorder=9, color='#16A34A', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
        c.line([[3, 4], [4, 2]], zorder=9, color='#16A34A', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
        return c.save(output_path)

def C02(output_path=None):
    if output_path is None:
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / 'Plane586_C02.png'
    with Canvas(PLANE, xlim=(-0.7093023255813948, 8.709302325581394), ylim=(-0.20930232558139483, 9.209302325581394), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        for object_id, points in [('grid_vertical_0', [[0, 0], [0, 9]]), ('grid_vertical_1', [[1, 0], [1, 9]]), ('grid_vertical_2', [[2, 0], [2, 9]]), ('grid_vertical_3', [[3, 0], [3, 9]]), ('grid_vertical_4', [[4, 0], [4, 9]]), ('grid_vertical_5', [[5, 0], [5, 9]]), ('grid_vertical_6', [[6, 0], [6, 9]]), ('grid_vertical_7', [[7, 0], [7, 9]]), ('grid_vertical_8', [[8, 0], [8, 9]]), ('grid_horizontal_0', [[0, 0], [8, 0]]), ('grid_horizontal_1', [[0, 1], [8, 1]]), ('grid_horizontal_2', [[0, 2], [8, 2]]), ('grid_horizontal_3', [[0, 3], [8, 3]]), ('grid_horizontal_4', [[0, 4], [8, 4]]), ('grid_horizontal_5', [[0, 5], [8, 5]]), ('grid_horizontal_6', [[0, 6], [8, 6]]), ('grid_horizontal_7', [[0, 7], [8, 7]]), ('grid_horizontal_8', [[0, 8], [8, 8]]), ('grid_horizontal_9', [[0, 9], [8, 9]])]:
            c.line(points, id=object_id, zorder=1, color='#AAAAAA')
        c.line([[1, 3], [7, 3]], id='given_segment_AB', zorder=3)
        c.line([[4, 2], [4, 8]], id='given_segment_CD', zorder=3)
        for object_id, center, radius in [('point_marker_X', [3, 4], 0.05677688953488369), ('point_marker_Y', [5, 4], 0.05677688953488369), ('point_marker_Z', [4, 4], 0.05677688953488369), ('point_marker_T', [2, 6], 0.05677688953488369)]:
            c.circle(center, radius, id=object_id, zorder=4, fill=False)
        c.text('X', (3, 4), id='label_X', clip_on=True, fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(-14, 14), annotation_clip=False)
        c.text('Y', (5, 4), id='label_Y', clip_on=True, fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(14, 14), annotation_clip=False)
        c.text('Z', (4, 4), id='label_Z', clip_on=True, fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(14, -14), annotation_clip=False)
        c.text('T', (2, 6), id='label_T', clip_on=True, fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(-14, 14), annotation_clip=False)
        c.point([[4.0, 4.0]], zorder=10, s=[50], facecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]], edgecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]])
        c.line([[4, 4], [1, 3]], zorder=9, color='#2563EB', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
        c.line([[4, 4], [4, 2]], zorder=9, color='#2563EB', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
        return c.save(output_path)

def C03(output_path=None):
    if output_path is None:
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / 'Plane586_C03.png'
    with Canvas(PLANE, xlim=(-0.7093023255813948, 8.709302325581394), ylim=(-0.20930232558139483, 9.209302325581394), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        for object_id, points in [('grid_vertical_0', [[0, 0], [0, 9]]), ('grid_vertical_1', [[1, 0], [1, 9]]), ('grid_vertical_2', [[2, 0], [2, 9]]), ('grid_vertical_3', [[3, 0], [3, 9]]), ('grid_vertical_4', [[4, 0], [4, 9]]), ('grid_vertical_5', [[5, 0], [5, 9]]), ('grid_vertical_6', [[6, 0], [6, 9]]), ('grid_vertical_7', [[7, 0], [7, 9]]), ('grid_vertical_8', [[8, 0], [8, 9]]), ('grid_horizontal_0', [[0, 0], [8, 0]]), ('grid_horizontal_1', [[0, 1], [8, 1]]), ('grid_horizontal_2', [[0, 2], [8, 2]]), ('grid_horizontal_3', [[0, 3], [8, 3]]), ('grid_horizontal_4', [[0, 4], [8, 4]]), ('grid_horizontal_5', [[0, 5], [8, 5]]), ('grid_horizontal_6', [[0, 6], [8, 6]]), ('grid_horizontal_7', [[0, 7], [8, 7]]), ('grid_horizontal_8', [[0, 8], [8, 8]]), ('grid_horizontal_9', [[0, 9], [8, 9]])]:
            c.line(points, id=object_id, zorder=1, color='#AAAAAA')
        c.line([[1, 3], [7, 3]], id='given_segment_AB', zorder=3)
        c.line([[4, 2], [4, 8]], id='given_segment_CD', zorder=3)
        for object_id, center, radius in [('point_marker_X', [3, 4], 0.05677688953488369), ('point_marker_Y', [5, 4], 0.05677688953488369), ('point_marker_Z', [4, 4], 0.05677688953488369), ('point_marker_T', [2, 6], 0.05677688953488369)]:
            c.circle(center, radius, id=object_id, zorder=4, fill=False)
        c.text('X', (3, 4), id='label_X', clip_on=True, fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(-14, 14), annotation_clip=False)
        c.text('Y', (5, 4), id='label_Y', clip_on=True, fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(14, 14), annotation_clip=False)
        c.text('Z', (4, 4), id='label_Z', clip_on=True, fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(14, -14), annotation_clip=False)
        c.text('T', (2, 6), id='label_T', clip_on=True, fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(-14, 14), annotation_clip=False)
        c.point([[4.0, 4.0]], zorder=10, s=[50], facecolors=[[0.9176470588235294, 0.34509803921568627, 0.047058823529411764, 1.0]], edgecolors=[[0.9176470588235294, 0.34509803921568627, 0.047058823529411764, 1.0]])
        c.line([[4, 4], [1, 3]], zorder=9, color='#16A34A', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
        c.line([[4, 4], [4, 2]], zorder=9, color='#16A34A', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
        return c.save(output_path)

def C04(output_path=None):
    if output_path is None:
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / 'Plane586_C04.png'
    with Canvas(PLANE, xlim=(-0.7093023255813948, 8.709302325581394), ylim=(-0.20930232558139483, 9.209302325581394), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        for object_id, points in [('grid_vertical_0', [[0, 0], [0, 9]]), ('grid_vertical_1', [[1, 0], [1, 9]]), ('grid_vertical_2', [[2, 0], [2, 9]]), ('grid_vertical_3', [[3, 0], [3, 9]]), ('grid_vertical_4', [[4, 0], [4, 9]]), ('grid_vertical_5', [[5, 0], [5, 9]]), ('grid_vertical_6', [[6, 0], [6, 9]]), ('grid_vertical_7', [[7, 0], [7, 9]]), ('grid_vertical_8', [[8, 0], [8, 9]]), ('grid_horizontal_0', [[0, 0], [8, 0]]), ('grid_horizontal_1', [[0, 1], [8, 1]]), ('grid_horizontal_2', [[0, 2], [8, 2]]), ('grid_horizontal_3', [[0, 3], [8, 3]]), ('grid_horizontal_4', [[0, 4], [8, 4]]), ('grid_horizontal_5', [[0, 5], [8, 5]]), ('grid_horizontal_6', [[0, 6], [8, 6]]), ('grid_horizontal_7', [[0, 7], [8, 7]]), ('grid_horizontal_8', [[0, 8], [8, 8]]), ('grid_horizontal_9', [[0, 9], [8, 9]])]:
            c.line(points, id=object_id, zorder=1, color='#AAAAAA')
        c.line([[1, 3], [7, 3]], id='given_segment_AB', zorder=3)
        c.line([[4, 2], [4, 8]], id='given_segment_CD', zorder=3)
        for object_id, center, radius in [('point_marker_X', [3, 4], 0.05677688953488369), ('point_marker_Y', [5, 4], 0.05677688953488369), ('point_marker_Z', [4, 4], 0.05677688953488369), ('point_marker_T', [2, 6], 0.05677688953488369)]:
            c.circle(center, radius, id=object_id, zorder=4, fill=False)
        c.text('X', (3, 4), id='label_X', clip_on=True, fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(-14, 14), annotation_clip=False)
        c.text('Y', (5, 4), id='label_Y', clip_on=True, fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(14, 14), annotation_clip=False)
        c.text('Z', (4, 4), id='label_Z', clip_on=True, fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(14, -14), annotation_clip=False)
        c.text('T', (2, 6), id='label_T', clip_on=True, fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(-14, 14), annotation_clip=False)
        c.line([[4, 4], [1, 3]], zorder=9, color='#16A34A', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
        c.line([[4, 4], [4, 2]], zorder=9, color='#16A34A', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
        return c.save(output_path)

def C05(output_path=None):
    if output_path is None:
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / 'Plane586_C05.png'
    with Canvas(PLANE, xlim=(-0.7093023255813948, 8.709302325581394), ylim=(-0.20930232558139483, 9.209302325581394), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        for object_id, points in [('grid_vertical_0', [[0, 0], [0, 9]]), ('grid_vertical_1', [[1, 0], [1, 9]]), ('grid_vertical_2', [[2, 0], [2, 9]]), ('grid_vertical_3', [[3, 0], [3, 9]]), ('grid_vertical_4', [[4, 0], [4, 9]]), ('grid_vertical_5', [[5, 0], [5, 9]]), ('grid_vertical_6', [[6, 0], [6, 9]]), ('grid_vertical_7', [[7, 0], [7, 9]]), ('grid_vertical_8', [[8, 0], [8, 9]]), ('grid_horizontal_0', [[0, 0], [8, 0]]), ('grid_horizontal_1', [[0, 1], [8, 1]]), ('grid_horizontal_2', [[0, 2], [8, 2]]), ('grid_horizontal_3', [[0, 3], [8, 3]]), ('grid_horizontal_4', [[0, 4], [8, 4]]), ('grid_horizontal_5', [[0, 5], [8, 5]]), ('grid_horizontal_6', [[0, 6], [8, 6]]), ('grid_horizontal_7', [[0, 7], [8, 7]]), ('grid_horizontal_8', [[0, 8], [8, 8]]), ('grid_horizontal_9', [[0, 9], [8, 9]])]:
            c.line(points, id=object_id, zorder=1, color='#AAAAAA')
        c.line([[1, 3], [7, 3]], id='given_segment_AB', zorder=3)
        c.line([[4, 2], [4, 8]], id='given_segment_CD', zorder=3)
        for object_id, center, radius in [('point_marker_X', [3, 4], 0.05677688953488369), ('point_marker_Y', [5, 4], 0.05677688953488369), ('point_marker_Z', [4, 4], 0.05677688953488369), ('point_marker_T', [2, 6], 0.05677688953488369)]:
            c.circle(center, radius, id=object_id, zorder=4, fill=False)
        c.text('X', (3, 4), id='label_X', clip_on=True, fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(-14, 14), annotation_clip=False)
        c.text('Y', (5, 4), id='label_Y', clip_on=True, fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(14, 14), annotation_clip=False)
        c.text('Z', (4, 4), id='label_Z', clip_on=True, fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(14, -14), annotation_clip=False)
        c.text('T', (2, 6), id='label_T', clip_on=True, fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(-14, 14), annotation_clip=False)
        c.point([[4.0, 4.0]], zorder=10, s=[50], facecolors=[[0.08627450980392157, 0.6392156862745098, 0.2901960784313726, 1.0]], edgecolors=[[0.08627450980392157, 0.6392156862745098, 0.2901960784313726, 1.0]])
        c.line([[4, 4], [1, 3]], zorder=9, color='#16A34A', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
        c.line([[4, 4], [4, 2]], zorder=9, color='#16A34A', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
        return c.save(output_path)
