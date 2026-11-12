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
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / 'Plane536_C01.png'
    with Canvas(PLANE, xlim=(-0.79232376, 10.775252), ylim=(-2.69842908, 8.86914668), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        for object_id, points in [('rail_left_0', [[0.0, 0.21], [0.0, 5.79]]), ('rail_right_0', [[10.0, 0.21], [10.0, 5.79]]), ('rail_bottom_0', [[0.21, 0.0], [9.79, 0.0]]), ('rail_top_0', [[0.21, 6.0], [9.79, 6.0]]), ('grid_v_1', [[1.0, 0.0], [1.0, 6.0]]), ('grid_v_2', [[2.0, 0.0], [2.0, 6.0]]), ('grid_v_3', [[3.0, 0.0], [3.0, 6.0]]), ('grid_v_4', [[4.0, 0.0], [4.0, 6.0]]), ('grid_v_5', [[5.0, 0.0], [5.0, 6.0]]), ('grid_v_6', [[6.0, 0.0], [6.0, 6.0]]), ('grid_v_7', [[7.0, 0.0], [7.0, 6.0]]), ('grid_v_8', [[8.0, 0.0], [8.0, 6.0]]), ('grid_v_9', [[9.0, 0.0], [9.0, 6.0]]), ('grid_h_1', [[0.0, 1.0], [10.0, 1.0]]), ('grid_h_2', [[0.0, 2.0], [10.0, 2.0]]), ('grid_h_3', [[0.0, 3.0], [10.0, 3.0]]), ('grid_h_4', [[0.0, 4.0], [10.0, 4.0]]), ('grid_h_5', [[0.0, 5.0], [10.0, 5.0]])]:
            c.line(points, id=object_id)
        for object_id, center, radius in [('pocket_A', [10, 0], 0.21), ('pocket_B', [10, 6], 0.21), ('pocket_C', [0, 6], 0.21), ('pocket_D', [0, 0], 0.21)]:
            c.circle(center, radius, id=object_id, zorder=3)
        c.line([[0.7, 4.7], [2.0, 6.0]], id='incoming_path')
        c.line([[2.0, 6.0], [4.5, 3.5]], id='outgoing_path')
        c.circle([0.7, 4.7], 0.09, id='ball_symbol', zorder=4, facecolor=(0.0, 0.0, 0.0, 1.0))
        c.path([[4.5, 3.5], [4.351507576, 3.775771645], [4.224228355, 3.648492424], [4.5, 3.5]], [1, 2, 2, 79], id='outgoing_arrowhead', zorder=4, facecolor=(0.0, 0.0, 0.0, 1.0), capstyle='butt')
        c.path([[2.361587833878426, 5.638412166121574], [2.4090711131635296, 5.685895445406678], [2.446739506724172, 5.742270180279887], [2.472437272295423, 5.804310074444685], [2.4981350378666733, 5.866349968609483], [2.5113624186599797, 5.9328485024490565], [2.5113624186599797, 6.0]], [1, 4, 4, 4, 4, 4, 4], id='incidence_arc', zorder=4, capstyle='butt', fill=False)
        c.text('A', (10, 0), id='label_A', clip_on=True, fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(16, -15), annotation_clip=False)
        c.text('B', (10, 6), id='label_B', clip_on=True, fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(16, 15), annotation_clip=False)
        c.text('C', (0, 6), id='label_C', clip_on=True, fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(-16, 15), annotation_clip=False)
        c.text('D', (0, 0), id='label_D', clip_on=True, fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(-16, -15), annotation_clip=False)
        c.text('45°', (2, 6), id='angle_label', clip_on=True, rotation_mode='default', offset_pt=(65, -17), annotation_clip=False)
        c.text('P', (2, 6), id='label_P', clip_on=True, fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(0, 19), annotation_clip=False)
        c.line([[2, 6], [8, 0]], zorder=9, color='#16A34A', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
        c.line([[8, 0], [10, 6]], zorder=9, color='#16A34A', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
        c.point([[8.0, 0.0]], zorder=10, s=[50], facecolors=[[0.9176470588235294, 0.34509803921568627, 0.047058823529411764, 1.0]], edgecolors=[[0.9176470588235294, 0.34509803921568627, 0.047058823529411764, 1.0]])
        return c.save(output_path)

def C02(output_path=None):
    if output_path is None:
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / 'Plane536_C02.png'
    with Canvas(PLANE, xlim=(-0.79232376, 10.775252), ylim=(-2.69842908, 8.86914668), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        for object_id, points in [('rail_left_0', [[0.0, 0.21], [0.0, 5.79]]), ('rail_right_0', [[10.0, 0.21], [10.0, 5.79]]), ('rail_bottom_0', [[0.21, 0.0], [9.79, 0.0]]), ('rail_top_0', [[0.21, 6.0], [9.79, 6.0]]), ('grid_v_1', [[1.0, 0.0], [1.0, 6.0]]), ('grid_v_2', [[2.0, 0.0], [2.0, 6.0]]), ('grid_v_3', [[3.0, 0.0], [3.0, 6.0]]), ('grid_v_4', [[4.0, 0.0], [4.0, 6.0]]), ('grid_v_5', [[5.0, 0.0], [5.0, 6.0]]), ('grid_v_6', [[6.0, 0.0], [6.0, 6.0]]), ('grid_v_7', [[7.0, 0.0], [7.0, 6.0]]), ('grid_v_8', [[8.0, 0.0], [8.0, 6.0]]), ('grid_v_9', [[9.0, 0.0], [9.0, 6.0]]), ('grid_h_1', [[0.0, 1.0], [10.0, 1.0]]), ('grid_h_2', [[0.0, 2.0], [10.0, 2.0]]), ('grid_h_3', [[0.0, 3.0], [10.0, 3.0]]), ('grid_h_4', [[0.0, 4.0], [10.0, 4.0]]), ('grid_h_5', [[0.0, 5.0], [10.0, 5.0]])]:
            c.line(points, id=object_id)
        for object_id, center, radius in [('pocket_A', [10, 0], 0.21), ('pocket_B', [10, 6], 0.21), ('pocket_C', [0, 6], 0.21), ('pocket_D', [0, 0], 0.21)]:
            c.circle(center, radius, id=object_id, zorder=3)
        c.line([[0.7, 4.7], [2.0, 6.0]], id='incoming_path')
        c.line([[2.0, 6.0], [4.5, 3.5]], id='outgoing_path')
        c.circle([0.7, 4.7], 0.09, id='ball_symbol', zorder=4, facecolor=(0.0, 0.0, 0.0, 1.0))
        c.path([[4.5, 3.5], [4.351507576, 3.775771645], [4.224228355, 3.648492424], [4.5, 3.5]], [1, 2, 2, 79], id='outgoing_arrowhead', zorder=4, facecolor=(0.0, 0.0, 0.0, 1.0), capstyle='butt')
        c.path([[2.361587833878426, 5.638412166121574], [2.4090711131635296, 5.685895445406678], [2.446739506724172, 5.742270180279887], [2.472437272295423, 5.804310074444685], [2.4981350378666733, 5.866349968609483], [2.5113624186599797, 5.9328485024490565], [2.5113624186599797, 6.0]], [1, 4, 4, 4, 4, 4, 4], id='incidence_arc', zorder=4, capstyle='butt', fill=False)
        c.text('A', (10, 0), id='label_A', clip_on=True, fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(16, -15), annotation_clip=False)
        c.text('B', (10, 6), id='label_B', clip_on=True, fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(16, 15), annotation_clip=False)
        c.text('C', (0, 6), id='label_C', clip_on=True, fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(-16, 15), annotation_clip=False)
        c.text('D', (0, 0), id='label_D', clip_on=True, fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(-16, -15), annotation_clip=False)
        c.text('45°', (2, 6), id='angle_label', clip_on=True, rotation_mode='default', offset_pt=(65, -17), annotation_clip=False)
        c.text('P', (2, 6), id='label_P', clip_on=True, fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(0, 19), annotation_clip=False)
        c.line([[8, 0], [10, 6]], zorder=9, color='#EA580C', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
        return c.save(output_path)

def C03(output_path=None):
    if output_path is None:
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / 'Plane536_C03.png'
    with Canvas(PLANE, xlim=(-0.79232376, 10.775252), ylim=(-2.69842908, 8.86914668), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        for object_id, points in [('rail_left_0', [[0.0, 0.21], [0.0, 5.79]]), ('rail_right_0', [[10.0, 0.21], [10.0, 5.79]]), ('rail_bottom_0', [[0.21, 0.0], [9.79, 0.0]]), ('rail_top_0', [[0.21, 6.0], [9.79, 6.0]]), ('grid_v_1', [[1.0, 0.0], [1.0, 6.0]]), ('grid_v_2', [[2.0, 0.0], [2.0, 6.0]]), ('grid_v_3', [[3.0, 0.0], [3.0, 6.0]]), ('grid_v_4', [[4.0, 0.0], [4.0, 6.0]]), ('grid_v_5', [[5.0, 0.0], [5.0, 6.0]]), ('grid_v_6', [[6.0, 0.0], [6.0, 6.0]]), ('grid_v_7', [[7.0, 0.0], [7.0, 6.0]]), ('grid_v_8', [[8.0, 0.0], [8.0, 6.0]]), ('grid_v_9', [[9.0, 0.0], [9.0, 6.0]]), ('grid_h_1', [[0.0, 1.0], [10.0, 1.0]]), ('grid_h_2', [[0.0, 2.0], [10.0, 2.0]]), ('grid_h_3', [[0.0, 3.0], [10.0, 3.0]]), ('grid_h_4', [[0.0, 4.0], [10.0, 4.0]]), ('grid_h_5', [[0.0, 5.0], [10.0, 5.0]])]:
            c.line(points, id=object_id)
        for object_id, center, radius in [('pocket_A', [10, 0], 0.21), ('pocket_B', [10, 6], 0.21), ('pocket_C', [0, 6], 0.21), ('pocket_D', [0, 0], 0.21)]:
            c.circle(center, radius, id=object_id, zorder=3)
        c.line([[0.7, 4.7], [2.0, 6.0]], id='incoming_path')
        c.line([[2.0, 6.0], [4.5, 3.5]], id='outgoing_path')
        c.circle([0.7, 4.7], 0.09, id='ball_symbol', zorder=4, facecolor=(0.0, 0.0, 0.0, 1.0))
        c.path([[4.5, 3.5], [4.351507576, 3.775771645], [4.224228355, 3.648492424], [4.5, 3.5]], [1, 2, 2, 79], id='outgoing_arrowhead', zorder=4, facecolor=(0.0, 0.0, 0.0, 1.0), capstyle='butt')
        c.path([[2.361587833878426, 5.638412166121574], [2.4090711131635296, 5.685895445406678], [2.446739506724172, 5.742270180279887], [2.472437272295423, 5.804310074444685], [2.4981350378666733, 5.866349968609483], [2.5113624186599797, 5.9328485024490565], [2.5113624186599797, 6.0]], [1, 4, 4, 4, 4, 4, 4], id='incidence_arc', zorder=4, capstyle='butt', fill=False)
        c.text('A', (10, 0), id='label_A', clip_on=True, fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(16, -15), annotation_clip=False)
        c.text('B', (10, 6), id='label_B', clip_on=True, fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(16, 15), annotation_clip=False)
        c.text('C', (0, 6), id='label_C', clip_on=True, fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(-16, 15), annotation_clip=False)
        c.text('D', (0, 0), id='label_D', clip_on=True, fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(-16, -15), annotation_clip=False)
        c.text('45°', (2, 6), id='angle_label', clip_on=True, rotation_mode='default', offset_pt=(65, -17), annotation_clip=False)
        c.text('P', (2, 6), id='label_P', clip_on=True, fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(0, 19), annotation_clip=False)
        c.line([[2, 6], [8, 0]], zorder=9, color='#DC2626', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
        c.line([[8, 0], [10, 6]], zorder=9, color='#DC2626', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
        c.point([[8.0, 0.0]], zorder=10, s=[50], facecolors=[[0.1450980392156863, 0.38823529411764707, 0.9215686274509803, 1.0]], edgecolors=[[0.1450980392156863, 0.38823529411764707, 0.9215686274509803, 1.0]])
        return c.save(output_path)

def C04(output_path=None):
    if output_path is None:
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / 'Plane536_C04.png'
    with Canvas(PLANE, xlim=(-0.79232376, 10.775252), ylim=(-2.69842908, 8.86914668), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        for object_id, points in [('rail_left_0', [[0.0, 0.21], [0.0, 5.79]]), ('rail_right_0', [[10.0, 0.21], [10.0, 5.79]]), ('rail_bottom_0', [[0.21, 0.0], [9.79, 0.0]]), ('rail_top_0', [[0.21, 6.0], [9.79, 6.0]]), ('grid_v_1', [[1.0, 0.0], [1.0, 6.0]]), ('grid_v_2', [[2.0, 0.0], [2.0, 6.0]]), ('grid_v_3', [[3.0, 0.0], [3.0, 6.0]]), ('grid_v_4', [[4.0, 0.0], [4.0, 6.0]]), ('grid_v_5', [[5.0, 0.0], [5.0, 6.0]]), ('grid_v_6', [[6.0, 0.0], [6.0, 6.0]]), ('grid_v_7', [[7.0, 0.0], [7.0, 6.0]]), ('grid_v_8', [[8.0, 0.0], [8.0, 6.0]]), ('grid_v_9', [[9.0, 0.0], [9.0, 6.0]]), ('grid_h_1', [[0.0, 1.0], [10.0, 1.0]]), ('grid_h_2', [[0.0, 2.0], [10.0, 2.0]]), ('grid_h_3', [[0.0, 3.0], [10.0, 3.0]]), ('grid_h_4', [[0.0, 4.0], [10.0, 4.0]]), ('grid_h_5', [[0.0, 5.0], [10.0, 5.0]])]:
            c.line(points, id=object_id)
        for object_id, center, radius in [('pocket_A', [10, 0], 0.21), ('pocket_B', [10, 6], 0.21), ('pocket_C', [0, 6], 0.21), ('pocket_D', [0, 0], 0.21)]:
            c.circle(center, radius, id=object_id, zorder=3)
        c.line([[0.7, 4.7], [2.0, 6.0]], id='incoming_path')
        c.line([[2.0, 6.0], [4.5, 3.5]], id='outgoing_path')
        c.circle([0.7, 4.7], 0.09, id='ball_symbol', zorder=4, facecolor=(0.0, 0.0, 0.0, 1.0))
        c.path([[4.5, 3.5], [4.351507576, 3.775771645], [4.224228355, 3.648492424], [4.5, 3.5]], [1, 2, 2, 79], id='outgoing_arrowhead', zorder=4, facecolor=(0.0, 0.0, 0.0, 1.0), capstyle='butt')
        c.path([[2.361587833878426, 5.638412166121574], [2.4090711131635296, 5.685895445406678], [2.446739506724172, 5.742270180279887], [2.472437272295423, 5.804310074444685], [2.4981350378666733, 5.866349968609483], [2.5113624186599797, 5.9328485024490565], [2.5113624186599797, 6.0]], [1, 4, 4, 4, 4, 4, 4], id='incidence_arc', zorder=4, capstyle='butt', fill=False)
        c.text('A', (10, 0), id='label_A', clip_on=True, fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(16, -15), annotation_clip=False)
        c.text('B', (10, 6), id='label_B', clip_on=True, fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(16, 15), annotation_clip=False)
        c.text('C', (0, 6), id='label_C', clip_on=True, fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(-16, 15), annotation_clip=False)
        c.text('D', (0, 0), id='label_D', clip_on=True, fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(-16, -15), annotation_clip=False)
        c.text('45°', (2, 6), id='angle_label', clip_on=True, rotation_mode='default', offset_pt=(65, -17), annotation_clip=False)
        c.text('P', (2, 6), id='label_P', clip_on=True, fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(0, 19), annotation_clip=False)
        for object_id, points in [(None, [[2, 6], [8, 0]]), (None, [[8, 0], [10, 2]]), (None, [[10, 2], [0, 6]])]:
            c.line(points, id=object_id, zorder=9, color='#EA580C', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
        c.point([[10.0, 2.0]], zorder=10, s=[50], facecolors=[[0.1450980392156863, 0.38823529411764707, 0.9215686274509803, 1.0]], edgecolors=[[0.1450980392156863, 0.38823529411764707, 0.9215686274509803, 1.0]])
        return c.save(output_path)

def C05(output_path=None):
    if output_path is None:
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / 'Plane536_C05.png'
    with Canvas(PLANE, xlim=(-0.79232376, 10.775252), ylim=(-2.69842908, 8.86914668), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        for object_id, points in [('rail_left_0', [[0.0, 0.21], [0.0, 5.79]]), ('rail_right_0', [[10.0, 0.21], [10.0, 5.79]]), ('rail_bottom_0', [[0.21, 0.0], [9.79, 0.0]]), ('rail_top_0', [[0.21, 6.0], [9.79, 6.0]]), ('grid_v_1', [[1.0, 0.0], [1.0, 6.0]]), ('grid_v_2', [[2.0, 0.0], [2.0, 6.0]]), ('grid_v_3', [[3.0, 0.0], [3.0, 6.0]]), ('grid_v_4', [[4.0, 0.0], [4.0, 6.0]]), ('grid_v_5', [[5.0, 0.0], [5.0, 6.0]]), ('grid_v_6', [[6.0, 0.0], [6.0, 6.0]]), ('grid_v_7', [[7.0, 0.0], [7.0, 6.0]]), ('grid_v_8', [[8.0, 0.0], [8.0, 6.0]]), ('grid_v_9', [[9.0, 0.0], [9.0, 6.0]]), ('grid_h_1', [[0.0, 1.0], [10.0, 1.0]]), ('grid_h_2', [[0.0, 2.0], [10.0, 2.0]]), ('grid_h_3', [[0.0, 3.0], [10.0, 3.0]]), ('grid_h_4', [[0.0, 4.0], [10.0, 4.0]]), ('grid_h_5', [[0.0, 5.0], [10.0, 5.0]])]:
            c.line(points, id=object_id)
        for object_id, center, radius in [('pocket_A', [10, 0], 0.21), ('pocket_B', [10, 6], 0.21), ('pocket_C', [0, 6], 0.21), ('pocket_D', [0, 0], 0.21)]:
            c.circle(center, radius, id=object_id, zorder=3)
        c.line([[0.7, 4.7], [2.0, 6.0]], id='incoming_path')
        c.line([[2.0, 6.0], [4.5, 3.5]], id='outgoing_path')
        c.circle([0.7, 4.7], 0.09, id='ball_symbol', zorder=4, facecolor=(0.0, 0.0, 0.0, 1.0))
        c.path([[4.5, 3.5], [4.351507576, 3.775771645], [4.224228355, 3.648492424], [4.5, 3.5]], [1, 2, 2, 79], id='outgoing_arrowhead', zorder=4, facecolor=(0.0, 0.0, 0.0, 1.0), capstyle='butt')
        c.path([[2.361587833878426, 5.638412166121574], [2.4090711131635296, 5.685895445406678], [2.446739506724172, 5.742270180279887], [2.472437272295423, 5.804310074444685], [2.4981350378666733, 5.866349968609483], [2.5113624186599797, 5.9328485024490565], [2.5113624186599797, 6.0]], [1, 4, 4, 4, 4, 4, 4], id='incidence_arc', zorder=4, capstyle='butt', fill=False)
        c.text('A', (10, 0), id='label_A', clip_on=True, fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(16, -15), annotation_clip=False)
        c.text('B', (10, 6), id='label_B', clip_on=True, fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(16, 15), annotation_clip=False)
        c.text('C', (0, 6), id='label_C', clip_on=True, fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(-16, 15), annotation_clip=False)
        c.text('D', (0, 0), id='label_D', clip_on=True, fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(-16, -15), annotation_clip=False)
        c.text('45°', (2, 6), id='angle_label', clip_on=True, rotation_mode='default', offset_pt=(65, -17), annotation_clip=False)
        c.text('P', (2, 6), id='label_P', clip_on=True, fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(0, 19), annotation_clip=False)
        c.line([[8, 0], [10, 6]], zorder=9, color='#16A34A', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
        return c.save(output_path)

def C06(output_path=None):
    if output_path is None:
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / 'Plane536_C06.png'
    with Canvas(PLANE, xlim=(-0.79232376, 10.775252), ylim=(-2.69842908, 8.86914668), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        for object_id, points in [('rail_left_0', [[0.0, 0.21], [0.0, 5.79]]), ('rail_right_0', [[10.0, 0.21], [10.0, 5.79]]), ('rail_bottom_0', [[0.21, 0.0], [9.79, 0.0]]), ('rail_top_0', [[0.21, 6.0], [9.79, 6.0]]), ('grid_v_1', [[1.0, 0.0], [1.0, 6.0]]), ('grid_v_2', [[2.0, 0.0], [2.0, 6.0]]), ('grid_v_3', [[3.0, 0.0], [3.0, 6.0]]), ('grid_v_4', [[4.0, 0.0], [4.0, 6.0]]), ('grid_v_5', [[5.0, 0.0], [5.0, 6.0]]), ('grid_v_6', [[6.0, 0.0], [6.0, 6.0]]), ('grid_v_7', [[7.0, 0.0], [7.0, 6.0]]), ('grid_v_8', [[8.0, 0.0], [8.0, 6.0]]), ('grid_v_9', [[9.0, 0.0], [9.0, 6.0]]), ('grid_h_1', [[0.0, 1.0], [10.0, 1.0]]), ('grid_h_2', [[0.0, 2.0], [10.0, 2.0]]), ('grid_h_3', [[0.0, 3.0], [10.0, 3.0]]), ('grid_h_4', [[0.0, 4.0], [10.0, 4.0]]), ('grid_h_5', [[0.0, 5.0], [10.0, 5.0]])]:
            c.line(points, id=object_id)
        for object_id, center, radius in [('pocket_A', [10, 0], 0.21), ('pocket_B', [10, 6], 0.21), ('pocket_C', [0, 6], 0.21), ('pocket_D', [0, 0], 0.21)]:
            c.circle(center, radius, id=object_id, zorder=3)
        c.line([[0.7, 4.7], [2.0, 6.0]], id='incoming_path')
        c.line([[2.0, 6.0], [4.5, 3.5]], id='outgoing_path')
        c.circle([0.7, 4.7], 0.09, id='ball_symbol', zorder=4, facecolor=(0.0, 0.0, 0.0, 1.0))
        c.path([[4.5, 3.5], [4.351507576, 3.775771645], [4.224228355, 3.648492424], [4.5, 3.5]], [1, 2, 2, 79], id='outgoing_arrowhead', zorder=4, facecolor=(0.0, 0.0, 0.0, 1.0), capstyle='butt')
        c.path([[2.361587833878426, 5.638412166121574], [2.4090711131635296, 5.685895445406678], [2.446739506724172, 5.742270180279887], [2.472437272295423, 5.804310074444685], [2.4981350378666733, 5.866349968609483], [2.5113624186599797, 5.9328485024490565], [2.5113624186599797, 6.0]], [1, 4, 4, 4, 4, 4, 4], id='incidence_arc', zorder=4, capstyle='butt', fill=False)
        c.text('A', (10, 0), id='label_A', clip_on=True, fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(16, -15), annotation_clip=False)
        c.text('B', (10, 6), id='label_B', clip_on=True, fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(16, 15), annotation_clip=False)
        c.text('C', (0, 6), id='label_C', clip_on=True, fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(-16, 15), annotation_clip=False)
        c.text('D', (0, 0), id='label_D', clip_on=True, fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(-16, -15), annotation_clip=False)
        c.text('45°', (2, 6), id='angle_label', clip_on=True, rotation_mode='default', offset_pt=(65, -17), annotation_clip=False)
        c.text('P', (2, 6), id='label_P', clip_on=True, fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(0, 19), annotation_clip=False)
        for object_id, points in [(None, [[2, 6], [8, 0]]), (None, [[8, 0], [10, 2]]), (None, [[10, 2], [0, 6]])]:
            c.line(points, id=object_id, zorder=9, color='#16A34A', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
        c.point([[10.0, 2.0]], zorder=10, s=[50], facecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]], edgecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]])
        return c.save(output_path)
