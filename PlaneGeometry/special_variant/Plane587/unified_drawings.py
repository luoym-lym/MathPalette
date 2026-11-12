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
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / 'Plane587_C01.png'
    with Canvas(PLANE, xlim=(-0.23255813953488413, 10.232558139534884), ylim=(-0.23255813953488413, 10.232558139534884), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        for object_id, points in [('grid_vertical_0', [[0, 0], [0, 10]]), ('grid_vertical_1', [[1, 0], [1, 10]]), ('grid_vertical_2', [[2, 0], [2, 10]]), ('grid_vertical_3', [[3, 0], [3, 10]]), ('grid_vertical_4', [[4, 0], [4, 10]]), ('grid_vertical_5', [[5, 0], [5, 10]]), ('grid_vertical_6', [[6, 0], [6, 10]]), ('grid_vertical_7', [[7, 0], [7, 10]]), ('grid_vertical_8', [[8, 0], [8, 10]]), ('grid_vertical_9', [[9, 0], [9, 10]]), ('grid_vertical_10', [[10, 0], [10, 10]]), ('grid_horizontal_0', [[0, 0], [10, 0]]), ('grid_horizontal_1', [[0, 1], [10, 1]]), ('grid_horizontal_2', [[0, 2], [10, 2]]), ('grid_horizontal_3', [[0, 3], [10, 3]]), ('grid_horizontal_4', [[0, 4], [10, 4]]), ('grid_horizontal_5', [[0, 5], [10, 5]]), ('grid_horizontal_6', [[0, 6], [10, 6]]), ('grid_horizontal_7', [[0, 7], [10, 7]]), ('grid_horizontal_8', [[0, 8], [10, 8]]), ('grid_horizontal_9', [[0, 9], [10, 9]]), ('grid_horizontal_10', [[0, 10], [10, 10]])]:
            c.line(points, id=object_id, zorder=1, color='#AAAAAA')
        c.line([[5, 1], [9, 9]], id='given_segment_AB', zorder=3)
        c.line([[5, 1], [1, 9]], id='given_segment_CD', zorder=3)
        for object_id, center, radius in [('point_marker_X', [5, 1], 0.06308543281653746), ('point_marker_Y', [5, 5], 0.06308543281653746), ('point_marker_Z', [5, 9], 0.06308543281653746), ('point_marker_T', [5, 6], 0.06308543281653746)]:
            c.circle(center, radius, id=object_id, zorder=4, fill=False)
        c.text('X', (5, 1), id='label_X', clip_on=True, fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(16, -16), annotation_clip=False)
        c.text('Y', (5, 5), id='label_Y', clip_on=True, fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(-16, -16), annotation_clip=False)
        c.text('Z', (5, 9), id='label_Z', clip_on=True, fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(16, 16), annotation_clip=False)
        c.text('T', (5, 6), id='label_T', clip_on=True, fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(16, 16), annotation_clip=False)
        c.point([[5.0, 6.0]], zorder=10, s=[50], facecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]], edgecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]])
        c.line([[5.0, 6.0], [9.0, 9.0]], zorder=9, color='#2563EB', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
        return c.save(output_path)

def C02(output_path=None):
    if output_path is None:
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / 'Plane587_C02.png'
    with Canvas(PLANE, xlim=(-0.23255813953488413, 10.232558139534884), ylim=(-0.23255813953488413, 10.232558139534884), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        for object_id, points in [('grid_vertical_0', [[0, 0], [0, 10]]), ('grid_vertical_1', [[1, 0], [1, 10]]), ('grid_vertical_2', [[2, 0], [2, 10]]), ('grid_vertical_3', [[3, 0], [3, 10]]), ('grid_vertical_4', [[4, 0], [4, 10]]), ('grid_vertical_5', [[5, 0], [5, 10]]), ('grid_vertical_6', [[6, 0], [6, 10]]), ('grid_vertical_7', [[7, 0], [7, 10]]), ('grid_vertical_8', [[8, 0], [8, 10]]), ('grid_vertical_9', [[9, 0], [9, 10]]), ('grid_vertical_10', [[10, 0], [10, 10]]), ('grid_horizontal_0', [[0, 0], [10, 0]]), ('grid_horizontal_1', [[0, 1], [10, 1]]), ('grid_horizontal_2', [[0, 2], [10, 2]]), ('grid_horizontal_3', [[0, 3], [10, 3]]), ('grid_horizontal_4', [[0, 4], [10, 4]]), ('grid_horizontal_5', [[0, 5], [10, 5]]), ('grid_horizontal_6', [[0, 6], [10, 6]]), ('grid_horizontal_7', [[0, 7], [10, 7]]), ('grid_horizontal_8', [[0, 8], [10, 8]]), ('grid_horizontal_9', [[0, 9], [10, 9]]), ('grid_horizontal_10', [[0, 10], [10, 10]])]:
            c.line(points, id=object_id, zorder=1, color='#AAAAAA')
        c.line([[5, 1], [9, 9]], id='given_segment_AB', zorder=3)
        c.line([[5, 1], [1, 9]], id='given_segment_CD', zorder=3)
        for object_id, center, radius in [('point_marker_X', [5, 1], 0.06308543281653746), ('point_marker_Y', [5, 5], 0.06308543281653746), ('point_marker_Z', [5, 9], 0.06308543281653746), ('point_marker_T', [5, 6], 0.06308543281653746)]:
            c.circle(center, radius, id=object_id, zorder=4, fill=False)
        c.text('X', (5, 1), id='label_X', clip_on=True, fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(16, -16), annotation_clip=False)
        c.text('Y', (5, 5), id='label_Y', clip_on=True, fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(-16, -16), annotation_clip=False)
        c.text('Z', (5, 9), id='label_Z', clip_on=True, fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(16, 16), annotation_clip=False)
        c.text('T', (5, 6), id='label_T', clip_on=True, fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(16, 16), annotation_clip=False)
        c.point([[5.0, 6.0]], zorder=10, s=[50], facecolors=[[0.9176470588235294, 0.34509803921568627, 0.047058823529411764, 1.0]], edgecolors=[[0.9176470588235294, 0.34509803921568627, 0.047058823529411764, 1.0]])
        c.line([[5.0, 6.0], [9.0, 9.0]], zorder=9, color='#16A34A', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
        return c.save(output_path)

def C03(output_path=None):
    if output_path is None:
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / 'Plane587_C03.png'
    with Canvas(PLANE, xlim=(-0.23255813953488413, 10.232558139534884), ylim=(-0.23255813953488413, 10.232558139534884), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        for object_id, points in [('grid_vertical_0', [[0, 0], [0, 10]]), ('grid_vertical_1', [[1, 0], [1, 10]]), ('grid_vertical_2', [[2, 0], [2, 10]]), ('grid_vertical_3', [[3, 0], [3, 10]]), ('grid_vertical_4', [[4, 0], [4, 10]]), ('grid_vertical_5', [[5, 0], [5, 10]]), ('grid_vertical_6', [[6, 0], [6, 10]]), ('grid_vertical_7', [[7, 0], [7, 10]]), ('grid_vertical_8', [[8, 0], [8, 10]]), ('grid_vertical_9', [[9, 0], [9, 10]]), ('grid_vertical_10', [[10, 0], [10, 10]]), ('grid_horizontal_0', [[0, 0], [10, 0]]), ('grid_horizontal_1', [[0, 1], [10, 1]]), ('grid_horizontal_2', [[0, 2], [10, 2]]), ('grid_horizontal_3', [[0, 3], [10, 3]]), ('grid_horizontal_4', [[0, 4], [10, 4]]), ('grid_horizontal_5', [[0, 5], [10, 5]]), ('grid_horizontal_6', [[0, 6], [10, 6]]), ('grid_horizontal_7', [[0, 7], [10, 7]]), ('grid_horizontal_8', [[0, 8], [10, 8]]), ('grid_horizontal_9', [[0, 9], [10, 9]]), ('grid_horizontal_10', [[0, 10], [10, 10]])]:
            c.line(points, id=object_id, zorder=1, color='#AAAAAA')
        c.line([[5, 1], [9, 9]], id='given_segment_AB', zorder=3)
        c.line([[5, 1], [1, 9]], id='given_segment_CD', zorder=3)
        for object_id, center, radius in [('point_marker_X', [5, 1], 0.06308543281653746), ('point_marker_Y', [5, 5], 0.06308543281653746), ('point_marker_Z', [5, 9], 0.06308543281653746), ('point_marker_T', [5, 6], 0.06308543281653746)]:
            c.circle(center, radius, id=object_id, zorder=4, fill=False)
        c.text('X', (5, 1), id='label_X', clip_on=True, fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(16, -16), annotation_clip=False)
        c.text('Y', (5, 5), id='label_Y', clip_on=True, fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(-16, -16), annotation_clip=False)
        c.text('Z', (5, 9), id='label_Z', clip_on=True, fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(16, 16), annotation_clip=False)
        c.text('T', (5, 6), id='label_T', clip_on=True, fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(16, 16), annotation_clip=False)
        c.point([[5.0, 6.0]], zorder=10, s=[50], facecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]], edgecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]])
        c.line([[5.0, 6.0], [9.0, 9.0]], zorder=9, color='#EA580C', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
        return c.save(output_path)
