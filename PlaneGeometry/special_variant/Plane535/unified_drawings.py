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
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / 'Plane535_C01.png'
    with Canvas(PLANE, xlim=(-0.71963068, 9.70400568), ylim=(-2.17275568, 8.25088068), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        for object_id, points in [('rail_left_0', [[0.0, 0.21], [0.0, 5.79]]), ('rail_right_0', [[9.0, 0.21], [9.0, 5.79]]), ('rail_bottom_0', [[0.21, 0.0], [8.79, 0.0]]), ('rail_top_0', [[0.21, 6.0], [8.79, 6.0]]), ('grid_v_1', [[1.0, 0.0], [1.0, 6.0]]), ('grid_v_2', [[2.0, 0.0], [2.0, 6.0]]), ('grid_v_3', [[3.0, 0.0], [3.0, 6.0]]), ('grid_v_4', [[4.0, 0.0], [4.0, 6.0]]), ('grid_v_5', [[5.0, 0.0], [5.0, 6.0]]), ('grid_v_6', [[6.0, 0.0], [6.0, 6.0]]), ('grid_v_7', [[7.0, 0.0], [7.0, 6.0]]), ('grid_v_8', [[8.0, 0.0], [8.0, 6.0]]), ('grid_h_1', [[0.0, 1.0], [9.0, 1.0]]), ('grid_h_2', [[0.0, 2.0], [9.0, 2.0]]), ('grid_h_3', [[0.0, 3.0], [9.0, 3.0]]), ('grid_h_4', [[0.0, 4.0], [9.0, 4.0]]), ('grid_h_5', [[0.0, 5.0], [9.0, 5.0]])]:
            c.line(points, id=object_id)
        for object_id, center, radius in [('pocket_A', [9, 0], 0.21), ('pocket_B', [9, 6], 0.21), ('pocket_C', [0, 6], 0.21), ('pocket_D', [0, 0], 0.21)]:
            c.circle(center, radius, id=object_id, zorder=3)
        c.line([[1.5, 1.5], [0.0, 3.0]], id='incoming_path')
        c.line([[0.0, 3.0], [2.6, 5.6]], id='outgoing_path')
        c.circle([1.5, 1.5], 0.09, id='ball_symbol', zorder=4, facecolor=(0.0, 0.0, 0.0, 1.0))
        c.path([[2.6, 5.6], [2.324228355, 5.451507576], [2.451507576, 5.324228355], [2.6, 5.6]], [1, 2, 2, 79], id='outgoing_arrowhead', zorder=4, facecolor=(0.0, 0.0, 0.0, 1.0), capstyle='butt')
        c.path([[0.32582973051120945, 3.3258297305112094], [0.2830421623364028, 3.368617298686016], [0.23224243139867845, 3.4025605937106516], [0.17633777946435292, 3.4257170587415966], [0.12043312753002736, 3.4488735237725416], [0.060510759213775106, 3.460792823913323], [2.821542284377605e-17, 3.460792823913323]], [1, 4, 4, 4, 4, 4, 4], id='incidence_arc', zorder=4, capstyle='butt', fill=False)
        c.text('A', (9, 0), id='label_A', clip_on=True, fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(16, -15), annotation_clip=False)
        c.text('B', (9, 6), id='label_B', clip_on=True, fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(16, 15), annotation_clip=False)
        c.text('C', (0, 6), id='label_C', clip_on=True, fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(-16, 15), annotation_clip=False)
        c.text('D', (0, 0), id='label_D', clip_on=True, fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(-16, -15), annotation_clip=False)
        c.text('45°', (0, 3), id='angle_label', clip_on=True, rotation_mode='default', offset_pt=(15.3073373, 36.9551813), annotation_clip=False)
        c.text('P', (0, 3), id='label_P', clip_on=True, fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(-17, 0), annotation_clip=False)
        c.line([[0, 3], [3, 6]], zorder=9, color='#16A34A', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
        c.line([[3, 6], [0, 0]], zorder=9, color='#16A34A', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
        c.point([[3.0, 6.0]], zorder=10, s=[50], facecolors=[[0.9176470588235294, 0.34509803921568627, 0.047058823529411764, 1.0]], edgecolors=[[0.9176470588235294, 0.34509803921568627, 0.047058823529411764, 1.0]])
        return c.save(output_path)

def C02(output_path=None):
    if output_path is None:
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / 'Plane535_C02.png'
    with Canvas(PLANE, xlim=(-0.71963068, 9.70400568), ylim=(-2.17275568, 8.25088068), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        for object_id, points in [('rail_left_0', [[0.0, 0.21], [0.0, 5.79]]), ('rail_right_0', [[9.0, 0.21], [9.0, 5.79]]), ('rail_bottom_0', [[0.21, 0.0], [8.79, 0.0]]), ('rail_top_0', [[0.21, 6.0], [8.79, 6.0]]), ('grid_v_1', [[1.0, 0.0], [1.0, 6.0]]), ('grid_v_2', [[2.0, 0.0], [2.0, 6.0]]), ('grid_v_3', [[3.0, 0.0], [3.0, 6.0]]), ('grid_v_4', [[4.0, 0.0], [4.0, 6.0]]), ('grid_v_5', [[5.0, 0.0], [5.0, 6.0]]), ('grid_v_6', [[6.0, 0.0], [6.0, 6.0]]), ('grid_v_7', [[7.0, 0.0], [7.0, 6.0]]), ('grid_v_8', [[8.0, 0.0], [8.0, 6.0]]), ('grid_h_1', [[0.0, 1.0], [9.0, 1.0]]), ('grid_h_2', [[0.0, 2.0], [9.0, 2.0]]), ('grid_h_3', [[0.0, 3.0], [9.0, 3.0]]), ('grid_h_4', [[0.0, 4.0], [9.0, 4.0]]), ('grid_h_5', [[0.0, 5.0], [9.0, 5.0]])]:
            c.line(points, id=object_id)
        for object_id, center, radius in [('pocket_A', [9, 0], 0.21), ('pocket_B', [9, 6], 0.21), ('pocket_C', [0, 6], 0.21), ('pocket_D', [0, 0], 0.21)]:
            c.circle(center, radius, id=object_id, zorder=3)
        c.line([[1.5, 1.5], [0.0, 3.0]], id='incoming_path')
        c.line([[0.0, 3.0], [2.6, 5.6]], id='outgoing_path')
        c.circle([1.5, 1.5], 0.09, id='ball_symbol', zorder=4, facecolor=(0.0, 0.0, 0.0, 1.0))
        c.path([[2.6, 5.6], [2.324228355, 5.451507576], [2.451507576, 5.324228355], [2.6, 5.6]], [1, 2, 2, 79], id='outgoing_arrowhead', zorder=4, facecolor=(0.0, 0.0, 0.0, 1.0), capstyle='butt')
        c.path([[0.32582973051120945, 3.3258297305112094], [0.2830421623364028, 3.368617298686016], [0.23224243139867845, 3.4025605937106516], [0.17633777946435292, 3.4257170587415966], [0.12043312753002736, 3.4488735237725416], [0.060510759213775106, 3.460792823913323], [2.821542284377605e-17, 3.460792823913323]], [1, 4, 4, 4, 4, 4, 4], id='incidence_arc', zorder=4, capstyle='butt', fill=False)
        c.text('A', (9, 0), id='label_A', clip_on=True, fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(16, -15), annotation_clip=False)
        c.text('B', (9, 6), id='label_B', clip_on=True, fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(16, 15), annotation_clip=False)
        c.text('C', (0, 6), id='label_C', clip_on=True, fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(-16, 15), annotation_clip=False)
        c.text('D', (0, 0), id='label_D', clip_on=True, fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(-16, -15), annotation_clip=False)
        c.text('45°', (0, 3), id='angle_label', clip_on=True, rotation_mode='default', offset_pt=(15.3073373, 36.9551813), annotation_clip=False)
        c.text('P', (0, 3), id='label_P', clip_on=True, fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(-17, 0), annotation_clip=False)
        c.line([[0, 3], [3, 6]], zorder=9, color='#EA580C', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
        c.line([[3, 6], [9, 4]], zorder=9, color='#EA580C', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
        c.point([[3.0, 6.0]], zorder=10, s=[50], facecolors=[[0.08627450980392157, 0.6392156862745098, 0.2901960784313726, 1.0]], edgecolors=[[0.08627450980392157, 0.6392156862745098, 0.2901960784313726, 1.0]])
        return c.save(output_path)

def C03(output_path=None):
    if output_path is None:
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / 'Plane535_C03.png'
    with Canvas(PLANE, xlim=(-0.71963068, 9.70400568), ylim=(-2.17275568, 8.25088068), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        for object_id, points in [('rail_left_0', [[0.0, 0.21], [0.0, 5.79]]), ('rail_right_0', [[9.0, 0.21], [9.0, 5.79]]), ('rail_bottom_0', [[0.21, 0.0], [8.79, 0.0]]), ('rail_top_0', [[0.21, 6.0], [8.79, 6.0]]), ('grid_v_1', [[1.0, 0.0], [1.0, 6.0]]), ('grid_v_2', [[2.0, 0.0], [2.0, 6.0]]), ('grid_v_3', [[3.0, 0.0], [3.0, 6.0]]), ('grid_v_4', [[4.0, 0.0], [4.0, 6.0]]), ('grid_v_5', [[5.0, 0.0], [5.0, 6.0]]), ('grid_v_6', [[6.0, 0.0], [6.0, 6.0]]), ('grid_v_7', [[7.0, 0.0], [7.0, 6.0]]), ('grid_v_8', [[8.0, 0.0], [8.0, 6.0]]), ('grid_h_1', [[0.0, 1.0], [9.0, 1.0]]), ('grid_h_2', [[0.0, 2.0], [9.0, 2.0]]), ('grid_h_3', [[0.0, 3.0], [9.0, 3.0]]), ('grid_h_4', [[0.0, 4.0], [9.0, 4.0]]), ('grid_h_5', [[0.0, 5.0], [9.0, 5.0]])]:
            c.line(points, id=object_id)
        for object_id, center, radius in [('pocket_A', [9, 0], 0.21), ('pocket_B', [9, 6], 0.21), ('pocket_C', [0, 6], 0.21), ('pocket_D', [0, 0], 0.21)]:
            c.circle(center, radius, id=object_id, zorder=3)
        c.line([[1.5, 1.5], [0.0, 3.0]], id='incoming_path')
        c.line([[0.0, 3.0], [2.6, 5.6]], id='outgoing_path')
        c.circle([1.5, 1.5], 0.09, id='ball_symbol', zorder=4, facecolor=(0.0, 0.0, 0.0, 1.0))
        c.path([[2.6, 5.6], [2.324228355, 5.451507576], [2.451507576, 5.324228355], [2.6, 5.6]], [1, 2, 2, 79], id='outgoing_arrowhead', zorder=4, facecolor=(0.0, 0.0, 0.0, 1.0), capstyle='butt')
        c.path([[0.32582973051120945, 3.3258297305112094], [0.2830421623364028, 3.368617298686016], [0.23224243139867845, 3.4025605937106516], [0.17633777946435292, 3.4257170587415966], [0.12043312753002736, 3.4488735237725416], [0.060510759213775106, 3.460792823913323], [2.821542284377605e-17, 3.460792823913323]], [1, 4, 4, 4, 4, 4, 4], id='incidence_arc', zorder=4, capstyle='butt', fill=False)
        c.text('A', (9, 0), id='label_A', clip_on=True, fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(16, -15), annotation_clip=False)
        c.text('B', (9, 6), id='label_B', clip_on=True, fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(16, 15), annotation_clip=False)
        c.text('C', (0, 6), id='label_C', clip_on=True, fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(-16, 15), annotation_clip=False)
        c.text('D', (0, 0), id='label_D', clip_on=True, fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(-16, -15), annotation_clip=False)
        c.text('45°', (0, 3), id='angle_label', clip_on=True, rotation_mode='default', offset_pt=(15.3073373, 36.9551813), annotation_clip=False)
        c.text('P', (0, 3), id='label_P', clip_on=True, fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(-17, 0), annotation_clip=False)
        c.line([[0, 3], [3, 6]], zorder=9, color='#DC2626', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
        c.line([[3, 6], [9, 4]], zorder=9, color='#DC2626', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
        c.point([[3.0, 6.0]], zorder=10, s=[50], facecolors=[[0.1450980392156863, 0.38823529411764707, 0.9215686274509803, 1.0]], edgecolors=[[0.1450980392156863, 0.38823529411764707, 0.9215686274509803, 1.0]])
        c.line([[9, 4], [3, 0]], zorder=9, color='#DC2626', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
        return c.save(output_path)

def C04(output_path=None):
    if output_path is None:
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / 'Plane535_C04.png'
    with Canvas(PLANE, xlim=(-0.71963068, 9.70400568), ylim=(-2.17275568, 8.25088068), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        for object_id, points in [('rail_left_0', [[0.0, 0.21], [0.0, 5.79]]), ('rail_right_0', [[9.0, 0.21], [9.0, 5.79]]), ('rail_bottom_0', [[0.21, 0.0], [8.79, 0.0]]), ('rail_top_0', [[0.21, 6.0], [8.79, 6.0]]), ('grid_v_1', [[1.0, 0.0], [1.0, 6.0]]), ('grid_v_2', [[2.0, 0.0], [2.0, 6.0]]), ('grid_v_3', [[3.0, 0.0], [3.0, 6.0]]), ('grid_v_4', [[4.0, 0.0], [4.0, 6.0]]), ('grid_v_5', [[5.0, 0.0], [5.0, 6.0]]), ('grid_v_6', [[6.0, 0.0], [6.0, 6.0]]), ('grid_v_7', [[7.0, 0.0], [7.0, 6.0]]), ('grid_v_8', [[8.0, 0.0], [8.0, 6.0]]), ('grid_h_1', [[0.0, 1.0], [9.0, 1.0]]), ('grid_h_2', [[0.0, 2.0], [9.0, 2.0]]), ('grid_h_3', [[0.0, 3.0], [9.0, 3.0]]), ('grid_h_4', [[0.0, 4.0], [9.0, 4.0]]), ('grid_h_5', [[0.0, 5.0], [9.0, 5.0]])]:
            c.line(points, id=object_id)
        for object_id, center, radius in [('pocket_A', [9, 0], 0.21), ('pocket_B', [9, 6], 0.21), ('pocket_C', [0, 6], 0.21), ('pocket_D', [0, 0], 0.21)]:
            c.circle(center, radius, id=object_id, zorder=3)
        c.line([[1.5, 1.5], [0.0, 3.0]], id='incoming_path')
        c.line([[0.0, 3.0], [2.6, 5.6]], id='outgoing_path')
        c.circle([1.5, 1.5], 0.09, id='ball_symbol', zorder=4, facecolor=(0.0, 0.0, 0.0, 1.0))
        c.path([[2.6, 5.6], [2.324228355, 5.451507576], [2.451507576, 5.324228355], [2.6, 5.6]], [1, 2, 2, 79], id='outgoing_arrowhead', zorder=4, facecolor=(0.0, 0.0, 0.0, 1.0), capstyle='butt')
        c.path([[0.32582973051120945, 3.3258297305112094], [0.2830421623364028, 3.368617298686016], [0.23224243139867845, 3.4025605937106516], [0.17633777946435292, 3.4257170587415966], [0.12043312753002736, 3.4488735237725416], [0.060510759213775106, 3.460792823913323], [2.821542284377605e-17, 3.460792823913323]], [1, 4, 4, 4, 4, 4, 4], id='incidence_arc', zorder=4, capstyle='butt', fill=False)
        c.text('A', (9, 0), id='label_A', clip_on=True, fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(16, -15), annotation_clip=False)
        c.text('B', (9, 6), id='label_B', clip_on=True, fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(16, 15), annotation_clip=False)
        c.text('C', (0, 6), id='label_C', clip_on=True, fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(-16, 15), annotation_clip=False)
        c.text('D', (0, 0), id='label_D', clip_on=True, fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(-16, -15), annotation_clip=False)
        c.text('45°', (0, 3), id='angle_label', clip_on=True, rotation_mode='default', offset_pt=(15.3073373, 36.9551813), annotation_clip=False)
        c.text('P', (0, 3), id='label_P', clip_on=True, fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(-17, 0), annotation_clip=False)
        c.line([[0, 3], [3, 6]], zorder=9, color='#16A34A', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
        c.line([[3, 6], [9, 4]], zorder=9, color='#16A34A', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
        c.point([[3.0, 6.0]], zorder=10, s=[50], facecolors=[[0.9176470588235294, 0.34509803921568627, 0.047058823529411764, 1.0]], edgecolors=[[0.9176470588235294, 0.34509803921568627, 0.047058823529411764, 1.0]])
        c.line([[9, 4], [3, 0]], zorder=9, color='#16A34A', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
        return c.save(output_path)

def C05(output_path=None):
    if output_path is None:
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / 'Plane535_C05.png'
    with Canvas(PLANE, xlim=(-0.71963068, 9.70400568), ylim=(-2.17275568, 8.25088068), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        for object_id, points in [('rail_left_0', [[0.0, 0.21], [0.0, 5.79]]), ('rail_right_0', [[9.0, 0.21], [9.0, 5.79]]), ('rail_bottom_0', [[0.21, 0.0], [8.79, 0.0]]), ('rail_top_0', [[0.21, 6.0], [8.79, 6.0]]), ('grid_v_1', [[1.0, 0.0], [1.0, 6.0]]), ('grid_v_2', [[2.0, 0.0], [2.0, 6.0]]), ('grid_v_3', [[3.0, 0.0], [3.0, 6.0]]), ('grid_v_4', [[4.0, 0.0], [4.0, 6.0]]), ('grid_v_5', [[5.0, 0.0], [5.0, 6.0]]), ('grid_v_6', [[6.0, 0.0], [6.0, 6.0]]), ('grid_v_7', [[7.0, 0.0], [7.0, 6.0]]), ('grid_v_8', [[8.0, 0.0], [8.0, 6.0]]), ('grid_h_1', [[0.0, 1.0], [9.0, 1.0]]), ('grid_h_2', [[0.0, 2.0], [9.0, 2.0]]), ('grid_h_3', [[0.0, 3.0], [9.0, 3.0]]), ('grid_h_4', [[0.0, 4.0], [9.0, 4.0]]), ('grid_h_5', [[0.0, 5.0], [9.0, 5.0]])]:
            c.line(points, id=object_id)
        for object_id, center, radius in [('pocket_A', [9, 0], 0.21), ('pocket_B', [9, 6], 0.21), ('pocket_C', [0, 6], 0.21), ('pocket_D', [0, 0], 0.21)]:
            c.circle(center, radius, id=object_id, zorder=3)
        c.line([[1.5, 1.5], [0.0, 3.0]], id='incoming_path')
        c.line([[0.0, 3.0], [2.6, 5.6]], id='outgoing_path')
        c.circle([1.5, 1.5], 0.09, id='ball_symbol', zorder=4, facecolor=(0.0, 0.0, 0.0, 1.0))
        c.path([[2.6, 5.6], [2.324228355, 5.451507576], [2.451507576, 5.324228355], [2.6, 5.6]], [1, 2, 2, 79], id='outgoing_arrowhead', zorder=4, facecolor=(0.0, 0.0, 0.0, 1.0), capstyle='butt')
        c.path([[0.32582973051120945, 3.3258297305112094], [0.2830421623364028, 3.368617298686016], [0.23224243139867845, 3.4025605937106516], [0.17633777946435292, 3.4257170587415966], [0.12043312753002736, 3.4488735237725416], [0.060510759213775106, 3.460792823913323], [2.821542284377605e-17, 3.460792823913323]], [1, 4, 4, 4, 4, 4, 4], id='incidence_arc', zorder=4, capstyle='butt', fill=False)
        c.text('A', (9, 0), id='label_A', clip_on=True, fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(16, -15), annotation_clip=False)
        c.text('B', (9, 6), id='label_B', clip_on=True, fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(16, 15), annotation_clip=False)
        c.text('C', (0, 6), id='label_C', clip_on=True, fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(-16, 15), annotation_clip=False)
        c.text('D', (0, 0), id='label_D', clip_on=True, fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(-16, -15), annotation_clip=False)
        c.text('45°', (0, 3), id='angle_label', clip_on=True, rotation_mode='default', offset_pt=(15.3073373, 36.9551813), annotation_clip=False)
        c.text('P', (0, 3), id='label_P', clip_on=True, fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(-17, 0), annotation_clip=False)
        c.line([[0, 3], [3, 6]], zorder=9, color='#EA580C', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
        c.line([[3, 6], [9, 4]], zorder=9, color='#EA580C', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
        c.point([[3.0, 6.0]], zorder=10, s=[50], facecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]], edgecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]])
        c.line([[9, 4], [3, 0]], zorder=9, color='#EA580C', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
        return c.save(output_path)

def C06(output_path=None):
    if output_path is None:
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / 'Plane535_C06.png'
    with Canvas(PLANE, xlim=(-0.71963068, 9.70400568), ylim=(-2.17275568, 8.25088068), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        for object_id, points in [('rail_left_0', [[0.0, 0.21], [0.0, 5.79]]), ('rail_right_0', [[9.0, 0.21], [9.0, 5.79]]), ('rail_bottom_0', [[0.21, 0.0], [8.79, 0.0]]), ('rail_top_0', [[0.21, 6.0], [8.79, 6.0]]), ('grid_v_1', [[1.0, 0.0], [1.0, 6.0]]), ('grid_v_2', [[2.0, 0.0], [2.0, 6.0]]), ('grid_v_3', [[3.0, 0.0], [3.0, 6.0]]), ('grid_v_4', [[4.0, 0.0], [4.0, 6.0]]), ('grid_v_5', [[5.0, 0.0], [5.0, 6.0]]), ('grid_v_6', [[6.0, 0.0], [6.0, 6.0]]), ('grid_v_7', [[7.0, 0.0], [7.0, 6.0]]), ('grid_v_8', [[8.0, 0.0], [8.0, 6.0]]), ('grid_h_1', [[0.0, 1.0], [9.0, 1.0]]), ('grid_h_2', [[0.0, 2.0], [9.0, 2.0]]), ('grid_h_3', [[0.0, 3.0], [9.0, 3.0]]), ('grid_h_4', [[0.0, 4.0], [9.0, 4.0]]), ('grid_h_5', [[0.0, 5.0], [9.0, 5.0]])]:
            c.line(points, id=object_id)
        for object_id, center, radius in [('pocket_A', [9, 0], 0.21), ('pocket_B', [9, 6], 0.21), ('pocket_C', [0, 6], 0.21), ('pocket_D', [0, 0], 0.21)]:
            c.circle(center, radius, id=object_id, zorder=3)
        c.line([[1.5, 1.5], [0.0, 3.0]], id='incoming_path')
        c.line([[0.0, 3.0], [2.6, 5.6]], id='outgoing_path')
        c.circle([1.5, 1.5], 0.09, id='ball_symbol', zorder=4, facecolor=(0.0, 0.0, 0.0, 1.0))
        c.path([[2.6, 5.6], [2.324228355, 5.451507576], [2.451507576, 5.324228355], [2.6, 5.6]], [1, 2, 2, 79], id='outgoing_arrowhead', zorder=4, facecolor=(0.0, 0.0, 0.0, 1.0), capstyle='butt')
        c.path([[0.32582973051120945, 3.3258297305112094], [0.2830421623364028, 3.368617298686016], [0.23224243139867845, 3.4025605937106516], [0.17633777946435292, 3.4257170587415966], [0.12043312753002736, 3.4488735237725416], [0.060510759213775106, 3.460792823913323], [2.821542284377605e-17, 3.460792823913323]], [1, 4, 4, 4, 4, 4, 4], id='incidence_arc', zorder=4, capstyle='butt', fill=False)
        c.text('A', (9, 0), id='label_A', clip_on=True, fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(16, -15), annotation_clip=False)
        c.text('B', (9, 6), id='label_B', clip_on=True, fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(16, 15), annotation_clip=False)
        c.text('C', (0, 6), id='label_C', clip_on=True, fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(-16, 15), annotation_clip=False)
        c.text('D', (0, 0), id='label_D', clip_on=True, fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(-16, -15), annotation_clip=False)
        c.text('45°', (0, 3), id='angle_label', clip_on=True, rotation_mode='default', offset_pt=(15.3073373, 36.9551813), annotation_clip=False)
        c.text('P', (0, 3), id='label_P', clip_on=True, fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(-17, 0), annotation_clip=False)
        c.line([[0, 3], [3, 6]], zorder=9, color='#2563EB', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
        c.line([[3, 6], [9, 4]], zorder=9, color='#2563EB', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
        c.point([[3.0, 6.0]], zorder=10, s=[50], facecolors=[[0.08627450980392157, 0.6392156862745098, 0.2901960784313726, 1.0]], edgecolors=[[0.08627450980392157, 0.6392156862745098, 0.2901960784313726, 1.0]])
        c.line([[9, 4], [3, 0]], zorder=9, color='#2563EB', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
        return c.save(output_path)
