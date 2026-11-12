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
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / 'Plane558_C01.png'
    with Canvas(PLANE, xlim=(-0.6444517387143618, 5.121170086019016), ylim=(-0.3635226508063538, 5.402099173927024), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        for object_id, points in [('boundary_1', [[0.0, 0.0], [4.0, 0.0]]), ('boundary_2', [[4.0, 0.0], [4.0, 5.0]]), ('boundary_3', [[4.0, 5.0], [0.0, 5.0]]), ('boundary_4', [[0.0, 5.0], [0.0, 0.0]])]:
            c.line(points, id=object_id, zorder=3, simplify=False)
        c.line([[1.0, 0.0], [1.0, 5.0]], id='grid_column_1', zorder=1, color='#999999', linestyle=(0.0, [4.0, 3.0]), simplify=False)
        c.line([[2.0, 0.0], [2.0, 5.0]], id='grid_column_2', zorder=1, color='#999999', linestyle=(0.0, [4.0, 3.0]), simplify=False)
        c.line([[3.0, 0.0], [3.0, 5.0]], id='grid_column_3', zorder=1, color='#2563EB', linewidth=1.5, linestyle=(0.0, [4.0, 3.0]), simplify=False)
        c.line([[0.0, 1.0], [4.0, 1.0]], id='grid_row_1', zorder=1, color='#999999', linestyle=(0.0, [4.0, 3.0]), simplify=False)
        c.line([[0.0, 2.0], [4.0, 2.0]], id='grid_row_2', zorder=1, color='#2563EB', linewidth=2.0, linestyle=(0.0, [4.0, 3.0]), simplify=False)
        c.line([[0.0, 3.0], [4.0, 3.0]], id='grid_row_3', zorder=1, color='#999999', linestyle=(0.0, [4.0, 3.0]), simplify=False)
        c.line([[0.0, 4.0], [4.0, 4.0]], id='grid_row_4', zorder=1, color='#999999', linestyle=(0.0, [4.0, 3.0]), simplify=False)
        for object_id, points in [('mirror_c1_r3', [[0.66, 2.66], [1.34, 3.34]]), ('mirror_c1_r4', [[0.66, 4.34], [1.34, 3.66]]), ('mirror_c2_r1', [[1.66, 1.34], [2.34, 0.66]]), ('mirror_c2_r2', [[1.66, 1.66], [2.34, 2.34]]), ('mirror_c2_r3', [[1.66, 3.34], [2.34, 2.66]]), ('mirror_c2_r4', [[1.66, 4.34], [2.34, 3.66]]), ('mirror_c3_r1', [[2.66, 0.66], [3.34, 1.34]]), ('mirror_c3_r2', [[2.66, 1.66], [3.34, 2.34]]), ('mirror_c3_r3', [[2.66, 3.34], [3.34, 2.66]]), ('mirror_c3_r4', [[2.66, 3.66], [3.34, 4.34]])]:
            c.line(points, id=object_id, zorder=3, simplify=False)
        c.path([[681.5065294454746, 321.74616905140124], [607.1790738774332, 321.74616905140124], [534.4044432937667, 321.74616905140124]], [1, 3, 3], coordinates='pixels', id='incident_arrow', zorder=4, joinstyle='round', simplify=False)
        c.path([[541.0711099604333, 318.4128357180679], [534.4044432937667, 321.74616905140124], [541.0711099604333, 325.07950238473455], [0.0, 0.0]], [1, 2, 2, 79], coordinates='pixels', id='incident_arrow', zorder=4, facecolor=(0.0, 0.0, 0.0, 1.0), joinstyle='round', simplify=False)
        c.text('A', (0, 2), id='exit_label_A', fontsize=18.0, rotation_mode='default', offset_pt=(-15, 0), annotation_clip=None)
        c.text('B', (2, 0), id='exit_label_B', fontsize=18.0, rotation_mode='default', offset_pt=(0, -15), annotation_clip=None)
        c.text('C', (3, 5), id='exit_label_C', fontsize=18.0, rotation_mode='default', offset_pt=(0, 15), annotation_clip=None)
        c.text('D', (0, 4), id='exit_label_D', fontsize=18.0, rotation_mode='default', offset_pt=(-15, 0), annotation_clip=None)
        c.text('E', (1, 5), id='exit_label_E', fontsize=18.0, rotation_mode='default', offset_pt=(0, 15), annotation_clip=None)
        c.point([[3.0, 5.0]], zorder=10, s=[50], facecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]], edgecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]])
        return c.save(output_path)

def C02(output_path=None):
    if output_path is None:
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / 'Plane558_C02.png'
    with Canvas(PLANE, xlim=(-0.6444517387143618, 5.121170086019016), ylim=(-0.3635226508063538, 5.402099173927024), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        for object_id, points in [('boundary_1', [[0.0, 0.0], [4.0, 0.0]]), ('boundary_2', [[4.0, 0.0], [4.0, 5.0]]), ('boundary_3', [[4.0, 5.0], [0.0, 5.0]]), ('boundary_4', [[0.0, 5.0], [0.0, 0.0]])]:
            c.line(points, id=object_id, zorder=3, simplify=False)
        c.line([[1.0, 0.0], [1.0, 5.0]], id='grid_column_1', zorder=1, color='#2563EB', linewidth=3.0, linestyle=(0.0, [4.0, 3.0]), simplify=False)
        for object_id, points in [('grid_column_2', [[2.0, 0.0], [2.0, 5.0]]), ('grid_column_3', [[3.0, 0.0], [3.0, 5.0]]), ('grid_row_1', [[0.0, 1.0], [4.0, 1.0]])]:
            c.line(points, id=object_id, zorder=1, color='#999999', linestyle=(0.0, [4.0, 3.0]), simplify=False)
        c.line([[0.0, 2.0], [4.0, 2.0]], id='grid_row_2', zorder=1, color='#2563EB', linewidth=1.5, linestyle=(0.0, [4.0, 3.0]), simplify=False)
        c.line([[0.0, 3.0], [4.0, 3.0]], id='grid_row_3', zorder=1, color='#999999', linestyle=(0.0, [4.0, 3.0]), simplify=False)
        c.line([[0.0, 4.0], [4.0, 4.0]], id='grid_row_4', zorder=1, color='#999999', linestyle=(0.0, [4.0, 3.0]), simplify=False)
        for object_id, points in [('mirror_c1_r3', [[0.66, 2.66], [1.34, 3.34]]), ('mirror_c1_r4', [[0.66, 4.34], [1.34, 3.66]]), ('mirror_c2_r1', [[1.66, 1.34], [2.34, 0.66]]), ('mirror_c2_r2', [[1.66, 1.66], [2.34, 2.34]]), ('mirror_c2_r3', [[1.66, 3.34], [2.34, 2.66]]), ('mirror_c2_r4', [[1.66, 4.34], [2.34, 3.66]]), ('mirror_c3_r1', [[2.66, 0.66], [3.34, 1.34]]), ('mirror_c3_r2', [[2.66, 1.66], [3.34, 2.34]]), ('mirror_c3_r3', [[2.66, 3.34], [3.34, 2.66]]), ('mirror_c3_r4', [[2.66, 3.66], [3.34, 4.34]])]:
            c.line(points, id=object_id, zorder=3, simplify=False)
        c.path([[681.5065294454746, 321.74616905140124], [607.1790738774332, 321.74616905140124], [534.4044432937667, 321.74616905140124]], [1, 3, 3], coordinates='pixels', id='incident_arrow', zorder=4, joinstyle='round', simplify=False)
        c.path([[541.0711099604333, 318.4128357180679], [534.4044432937667, 321.74616905140124], [541.0711099604333, 325.07950238473455], [0.0, 0.0]], [1, 2, 2, 79], coordinates='pixels', id='incident_arrow', zorder=4, facecolor=(0.0, 0.0, 0.0, 1.0), joinstyle='round', simplify=False)
        c.text('A', (0, 2), id='exit_label_A', fontsize=18.0, rotation_mode='default', offset_pt=(-15, 0), annotation_clip=None)
        c.text('B', (2, 0), id='exit_label_B', fontsize=18.0, rotation_mode='default', offset_pt=(0, -15), annotation_clip=None)
        c.text('C', (3, 5), id='exit_label_C', fontsize=18.0, rotation_mode='default', offset_pt=(0, 15), annotation_clip=None)
        c.text('D', (0, 4), id='exit_label_D', fontsize=18.0, rotation_mode='default', offset_pt=(-15, 0), annotation_clip=None)
        c.text('E', (1, 5), id='exit_label_E', fontsize=18.0, rotation_mode='default', offset_pt=(0, 15), annotation_clip=None)
        c.point([[3.0, 5.0]], zorder=10, s=[50], facecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]], edgecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]])
        return c.save(output_path)

def C03(output_path=None):
    if output_path is None:
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / 'Plane558_C03.png'
    with Canvas(PLANE, xlim=(-0.6444517387143618, 5.121170086019016), ylim=(-0.3635226508063538, 5.402099173927024), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        for object_id, points in [('boundary_1', [[0.0, 0.0], [4.0, 0.0]]), ('boundary_2', [[4.0, 0.0], [4.0, 5.0]]), ('boundary_3', [[4.0, 5.0], [0.0, 5.0]]), ('boundary_4', [[0.0, 5.0], [0.0, 0.0]])]:
            c.line(points, id=object_id, zorder=3, simplify=False)
        c.line([[1.0, 0.0], [1.0, 5.0]], id='grid_column_1', zorder=1, color='#999999', linestyle=(0.0, [4.0, 3.0]), simplify=False)
        c.line([[2.0, 0.0], [2.0, 5.0]], id='grid_column_2', zorder=1, color='#999999', linestyle=(0.0, [4.0, 3.0]), simplify=False)
        c.line([[3.0, 0.0], [3.0, 5.0]], id='grid_column_3', zorder=1, color='#EA580C', linewidth=1.5, linestyle=(0.0, [4.0, 3.0]), simplify=False)
        c.line([[0.0, 1.0], [4.0, 1.0]], id='grid_row_1', zorder=1, color='#999999', linestyle=(0.0, [4.0, 3.0]), simplify=False)
        c.line([[0.0, 2.0], [4.0, 2.0]], id='grid_row_2', zorder=1, color='#EA580C', linewidth=2.0, linestyle=(0.0, [4.0, 3.0]), simplify=False)
        c.line([[0.0, 3.0], [4.0, 3.0]], id='grid_row_3', zorder=1, color='#999999', linestyle=(0.0, [4.0, 3.0]), simplify=False)
        c.line([[0.0, 4.0], [4.0, 4.0]], id='grid_row_4', zorder=1, color='#999999', linestyle=(0.0, [4.0, 3.0]), simplify=False)
        for object_id, points in [('mirror_c1_r3', [[0.66, 2.66], [1.34, 3.34]]), ('mirror_c1_r4', [[0.66, 4.34], [1.34, 3.66]]), ('mirror_c2_r1', [[1.66, 1.34], [2.34, 0.66]]), ('mirror_c2_r2', [[1.66, 1.66], [2.34, 2.34]]), ('mirror_c2_r3', [[1.66, 3.34], [2.34, 2.66]]), ('mirror_c2_r4', [[1.66, 4.34], [2.34, 3.66]]), ('mirror_c3_r1', [[2.66, 0.66], [3.34, 1.34]]), ('mirror_c3_r2', [[2.66, 1.66], [3.34, 2.34]]), ('mirror_c3_r3', [[2.66, 3.34], [3.34, 2.66]]), ('mirror_c3_r4', [[2.66, 3.66], [3.34, 4.34]])]:
            c.line(points, id=object_id, zorder=3, simplify=False)
        c.path([[681.5065294454746, 321.74616905140124], [607.1790738774332, 321.74616905140124], [534.4044432937667, 321.74616905140124]], [1, 3, 3], coordinates='pixels', id='incident_arrow', zorder=4, joinstyle='round', simplify=False)
        c.path([[541.0711099604333, 318.4128357180679], [534.4044432937667, 321.74616905140124], [541.0711099604333, 325.07950238473455], [0.0, 0.0]], [1, 2, 2, 79], coordinates='pixels', id='incident_arrow', zorder=4, facecolor=(0.0, 0.0, 0.0, 1.0), joinstyle='round', simplify=False)
        c.text('A', (0, 2), id='exit_label_A', fontsize=18.0, rotation_mode='default', offset_pt=(-15, 0), annotation_clip=None)
        c.text('B', (2, 0), id='exit_label_B', fontsize=18.0, rotation_mode='default', offset_pt=(0, -15), annotation_clip=None)
        c.text('C', (3, 5), id='exit_label_C', fontsize=18.0, rotation_mode='default', offset_pt=(0, 15), annotation_clip=None)
        c.text('D', (0, 4), id='exit_label_D', fontsize=18.0, rotation_mode='default', offset_pt=(-15, 0), annotation_clip=None)
        c.text('E', (1, 5), id='exit_label_E', fontsize=18.0, rotation_mode='default', offset_pt=(0, 15), annotation_clip=None)
        c.point([[3.0, 5.0]], zorder=10, s=[50], facecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]], edgecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]])
        return c.save(output_path)

def C04(output_path=None):
    if output_path is None:
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / 'Plane558_C04.png'
    with Canvas(PLANE, xlim=(-0.6444517387143618, 5.121170086019016), ylim=(-0.3635226508063538, 5.402099173927024), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        for object_id, points in [('boundary_1', [[0.0, 0.0], [4.0, 0.0]]), ('boundary_2', [[4.0, 0.0], [4.0, 5.0]]), ('boundary_3', [[4.0, 5.0], [0.0, 5.0]]), ('boundary_4', [[0.0, 5.0], [0.0, 0.0]])]:
            c.line(points, id=object_id, zorder=3, simplify=False)
        c.line([[1.0, 0.0], [1.0, 5.0]], id='grid_column_1', zorder=1, color='#16A34A', linewidth=3.0, linestyle=(0.0, [4.0, 3.0]), simplify=False)
        for object_id, points in [('grid_column_2', [[2.0, 0.0], [2.0, 5.0]]), ('grid_column_3', [[3.0, 0.0], [3.0, 5.0]]), ('grid_row_1', [[0.0, 1.0], [4.0, 1.0]])]:
            c.line(points, id=object_id, zorder=1, color='#999999', linestyle=(0.0, [4.0, 3.0]), simplify=False)
        c.line([[0.0, 2.0], [4.0, 2.0]], id='grid_row_2', zorder=1, color='#16A34A', linewidth=1.5, linestyle=(0.0, [4.0, 3.0]), simplify=False)
        c.line([[0.0, 3.0], [4.0, 3.0]], id='grid_row_3', zorder=1, color='#999999', linestyle=(0.0, [4.0, 3.0]), simplify=False)
        c.line([[0.0, 4.0], [4.0, 4.0]], id='grid_row_4', zorder=1, color='#999999', linestyle=(0.0, [4.0, 3.0]), simplify=False)
        for object_id, points in [('mirror_c1_r3', [[0.66, 2.66], [1.34, 3.34]]), ('mirror_c1_r4', [[0.66, 4.34], [1.34, 3.66]]), ('mirror_c2_r1', [[1.66, 1.34], [2.34, 0.66]]), ('mirror_c2_r2', [[1.66, 1.66], [2.34, 2.34]]), ('mirror_c2_r3', [[1.66, 3.34], [2.34, 2.66]]), ('mirror_c2_r4', [[1.66, 4.34], [2.34, 3.66]]), ('mirror_c3_r1', [[2.66, 0.66], [3.34, 1.34]]), ('mirror_c3_r2', [[2.66, 1.66], [3.34, 2.34]]), ('mirror_c3_r3', [[2.66, 3.34], [3.34, 2.66]]), ('mirror_c3_r4', [[2.66, 3.66], [3.34, 4.34]])]:
            c.line(points, id=object_id, zorder=3, simplify=False)
        c.path([[681.5065294454746, 321.74616905140124], [607.1790738774332, 321.74616905140124], [534.4044432937667, 321.74616905140124]], [1, 3, 3], coordinates='pixels', id='incident_arrow', zorder=4, joinstyle='round', simplify=False)
        c.path([[541.0711099604333, 318.4128357180679], [534.4044432937667, 321.74616905140124], [541.0711099604333, 325.07950238473455], [0.0, 0.0]], [1, 2, 2, 79], coordinates='pixels', id='incident_arrow', zorder=4, facecolor=(0.0, 0.0, 0.0, 1.0), joinstyle='round', simplify=False)
        c.text('A', (0, 2), id='exit_label_A', fontsize=18.0, rotation_mode='default', offset_pt=(-15, 0), annotation_clip=None)
        c.text('B', (2, 0), id='exit_label_B', fontsize=18.0, rotation_mode='default', offset_pt=(0, -15), annotation_clip=None)
        c.text('C', (3, 5), id='exit_label_C', fontsize=18.0, rotation_mode='default', offset_pt=(0, 15), annotation_clip=None)
        c.text('D', (0, 4), id='exit_label_D', fontsize=18.0, rotation_mode='default', offset_pt=(-15, 0), annotation_clip=None)
        c.text('E', (1, 5), id='exit_label_E', fontsize=18.0, rotation_mode='default', offset_pt=(0, 15), annotation_clip=None)
        c.point([[3.0, 5.0]], zorder=10, s=[50], facecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]], edgecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]])
        return c.save(output_path)

def C05(output_path=None):
    if output_path is None:
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / 'Plane558_C05.png'
    with Canvas(PLANE, xlim=(-0.6444517387143618, 5.121170086019016), ylim=(-0.3635226508063538, 5.402099173927024), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        for object_id, points in [('boundary_1', [[0.0, 0.0], [4.0, 0.0]]), ('boundary_2', [[4.0, 0.0], [4.0, 5.0]]), ('boundary_3', [[4.0, 5.0], [0.0, 5.0]]), ('boundary_4', [[0.0, 5.0], [0.0, 0.0]])]:
            c.line(points, id=object_id, zorder=3, simplify=False)
        c.line([[1.0, 0.0], [1.0, 5.0]], id='grid_column_1', zorder=1, color='#999999', linestyle=(0.0, [4.0, 3.0]), simplify=False)
        c.line([[2.0, 0.0], [2.0, 5.0]], id='grid_column_2', zorder=1, color='#999999', linestyle=(0.0, [4.0, 3.0]), simplify=False)
        c.line([[3.0, 0.0], [3.0, 5.0]], id='grid_column_3', zorder=1, color='#2563EB', linewidth=2.0, linestyle=(0.0, [4.0, 3.0]), simplify=False)
        c.line([[0.0, 1.0], [4.0, 1.0]], id='grid_row_1', zorder=1, color='#999999', linestyle=(0.0, [4.0, 3.0]), simplify=False)
        c.line([[0.0, 2.0], [4.0, 2.0]], id='grid_row_2', zorder=1, color='#2563EB', linewidth=1.5, linestyle=(0.0, [4.0, 3.0]), simplify=False)
        c.line([[0.0, 3.0], [4.0, 3.0]], id='grid_row_3', zorder=1, color='#999999', linestyle=(0.0, [4.0, 3.0]), simplify=False)
        c.line([[0.0, 4.0], [4.0, 4.0]], id='grid_row_4', zorder=1, color='#999999', linestyle=(0.0, [4.0, 3.0]), simplify=False)
        for object_id, points in [('mirror_c1_r3', [[0.66, 2.66], [1.34, 3.34]]), ('mirror_c1_r4', [[0.66, 4.34], [1.34, 3.66]]), ('mirror_c2_r1', [[1.66, 1.34], [2.34, 0.66]]), ('mirror_c2_r2', [[1.66, 1.66], [2.34, 2.34]]), ('mirror_c2_r3', [[1.66, 3.34], [2.34, 2.66]]), ('mirror_c2_r4', [[1.66, 4.34], [2.34, 3.66]]), ('mirror_c3_r1', [[2.66, 0.66], [3.34, 1.34]]), ('mirror_c3_r2', [[2.66, 1.66], [3.34, 2.34]]), ('mirror_c3_r3', [[2.66, 3.34], [3.34, 2.66]]), ('mirror_c3_r4', [[2.66, 3.66], [3.34, 4.34]])]:
            c.line(points, id=object_id, zorder=3, simplify=False)
        c.path([[681.5065294454746, 321.74616905140124], [607.1790738774332, 321.74616905140124], [534.4044432937667, 321.74616905140124]], [1, 3, 3], coordinates='pixels', id='incident_arrow', zorder=4, joinstyle='round', simplify=False)
        c.path([[541.0711099604333, 318.4128357180679], [534.4044432937667, 321.74616905140124], [541.0711099604333, 325.07950238473455], [0.0, 0.0]], [1, 2, 2, 79], coordinates='pixels', id='incident_arrow', zorder=4, facecolor=(0.0, 0.0, 0.0, 1.0), joinstyle='round', simplify=False)
        c.text('A', (0, 2), id='exit_label_A', fontsize=18.0, rotation_mode='default', offset_pt=(-15, 0), annotation_clip=None)
        c.text('B', (2, 0), id='exit_label_B', fontsize=18.0, rotation_mode='default', offset_pt=(0, -15), annotation_clip=None)
        c.text('C', (3, 5), id='exit_label_C', fontsize=18.0, rotation_mode='default', offset_pt=(0, 15), annotation_clip=None)
        c.text('D', (0, 4), id='exit_label_D', fontsize=18.0, rotation_mode='default', offset_pt=(-15, 0), annotation_clip=None)
        c.text('E', (1, 5), id='exit_label_E', fontsize=18.0, rotation_mode='default', offset_pt=(0, 15), annotation_clip=None)
        c.point([[3.0, 5.0]], zorder=10, s=[50], facecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]], edgecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]])
        return c.save(output_path)

def C06(output_path=None):
    if output_path is None:
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / 'Plane558_C06.png'
    with Canvas(PLANE, xlim=(-0.6444517387143618, 5.121170086019016), ylim=(-0.3635226508063538, 5.402099173927024), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        for object_id, points in [('boundary_1', [[0.0, 0.0], [4.0, 0.0]]), ('boundary_2', [[4.0, 0.0], [4.0, 5.0]]), ('boundary_3', [[4.0, 5.0], [0.0, 5.0]]), ('boundary_4', [[0.0, 5.0], [0.0, 0.0]])]:
            c.line(points, id=object_id, zorder=3, simplify=False)
        c.line([[1.0, 0.0], [1.0, 5.0]], id='grid_column_1', zorder=1, color='#999999', linestyle=(0.0, [4.0, 3.0]), simplify=False)
        c.line([[2.0, 0.0], [2.0, 5.0]], id='grid_column_2', zorder=1, color='#999999', linestyle=(0.0, [4.0, 3.0]), simplify=False)
        c.line([[3.0, 0.0], [3.0, 5.0]], id='grid_column_3', zorder=1, color='#EA580C', linewidth=2.0, linestyle=(0.0, [4.0, 3.0]), simplify=False)
        c.line([[0.0, 1.0], [4.0, 1.0]], id='grid_row_1', zorder=1, color='#999999', linestyle=(0.0, [4.0, 3.0]), simplify=False)
        c.line([[0.0, 2.0], [4.0, 2.0]], id='grid_row_2', zorder=1, color='#EA580C', linewidth=1.5, linestyle=(0.0, [4.0, 3.0]), simplify=False)
        c.line([[0.0, 3.0], [4.0, 3.0]], id='grid_row_3', zorder=1, color='#999999', linestyle=(0.0, [4.0, 3.0]), simplify=False)
        c.line([[0.0, 4.0], [4.0, 4.0]], id='grid_row_4', zorder=1, color='#999999', linestyle=(0.0, [4.0, 3.0]), simplify=False)
        for object_id, points in [('mirror_c1_r3', [[0.66, 2.66], [1.34, 3.34]]), ('mirror_c1_r4', [[0.66, 4.34], [1.34, 3.66]]), ('mirror_c2_r1', [[1.66, 1.34], [2.34, 0.66]]), ('mirror_c2_r2', [[1.66, 1.66], [2.34, 2.34]]), ('mirror_c2_r3', [[1.66, 3.34], [2.34, 2.66]]), ('mirror_c2_r4', [[1.66, 4.34], [2.34, 3.66]]), ('mirror_c3_r1', [[2.66, 0.66], [3.34, 1.34]]), ('mirror_c3_r2', [[2.66, 1.66], [3.34, 2.34]]), ('mirror_c3_r3', [[2.66, 3.34], [3.34, 2.66]]), ('mirror_c3_r4', [[2.66, 3.66], [3.34, 4.34]])]:
            c.line(points, id=object_id, zorder=3, simplify=False)
        c.path([[681.5065294454746, 321.74616905140124], [607.1790738774332, 321.74616905140124], [534.4044432937667, 321.74616905140124]], [1, 3, 3], coordinates='pixels', id='incident_arrow', zorder=4, joinstyle='round', simplify=False)
        c.path([[541.0711099604333, 318.4128357180679], [534.4044432937667, 321.74616905140124], [541.0711099604333, 325.07950238473455], [0.0, 0.0]], [1, 2, 2, 79], coordinates='pixels', id='incident_arrow', zorder=4, facecolor=(0.0, 0.0, 0.0, 1.0), joinstyle='round', simplify=False)
        c.text('A', (0, 2), id='exit_label_A', fontsize=18.0, rotation_mode='default', offset_pt=(-15, 0), annotation_clip=None)
        c.text('B', (2, 0), id='exit_label_B', fontsize=18.0, rotation_mode='default', offset_pt=(0, -15), annotation_clip=None)
        c.text('C', (3, 5), id='exit_label_C', fontsize=18.0, rotation_mode='default', offset_pt=(0, 15), annotation_clip=None)
        c.text('D', (0, 4), id='exit_label_D', fontsize=18.0, rotation_mode='default', offset_pt=(-15, 0), annotation_clip=None)
        c.text('E', (1, 5), id='exit_label_E', fontsize=18.0, rotation_mode='default', offset_pt=(0, 15), annotation_clip=None)
        c.point([[3.0, 5.0]], zorder=10, s=[50], facecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]], edgecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]])
        return c.save(output_path)
