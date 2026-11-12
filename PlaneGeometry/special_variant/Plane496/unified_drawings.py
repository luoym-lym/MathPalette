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
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / 'Plane496_C01.png'
    _geometry_01 = [('grid_v_0', [[-1.0, -0.5], [-1.0, 5.5]]),
     ('grid_v_1', [[0.0, -0.5], [0.0, 5.5]]),
     ('grid_v_2', [[1.0, -0.5], [1.0, 5.5]]),
     ('grid_v_3', [[2.0, -0.5], [2.0, 5.5]]),
     ('grid_v_4', [[3.0, -0.5], [3.0, 5.5]]),
     ('grid_v_5', [[4.0, -0.5], [4.0, 5.5]]),
     ('grid_v_6', [[5.0, -0.5], [5.0, 5.5]]),
     ('grid_v_7', [[6.0, -0.5], [6.0, 5.5]]),
     ('grid_v_8', [[7.0, -0.5], [7.0, 5.5]]),
     ('grid_v_9', [[8.0, -0.5], [8.0, 5.5]]),
     ('grid_v_10', [[9.0, -0.5], [9.0, 5.5]]),
     ('grid_v_11', [[10.0, -0.5], [10.0, 5.5]]),
     ('grid_v_12', [[11.0, -0.5], [11.0, 5.5]]),
     ('grid_v_13', [[12.0, -0.5], [12.0, 5.5]]),
     ('grid_v_14', [[13.0, -0.5], [13.0, 5.5]]),
     ('grid_v_15', [[14.0, -0.5], [14.0, 5.5]]),
     ('grid_v_16', [[15.0, -0.5], [15.0, 5.5]]),
     ('grid_v_17', [[16.0, -0.5], [16.0, 5.5]]),
     ('grid_v_18', [[17.0, -0.5], [17.0, 5.5]]),
     ('grid_v_19', [[18.0, -0.5], [18.0, 5.5]]),
     ('grid_v_20', [[19.0, -0.5], [19.0, 5.5]]),
     ('grid_v_21', [[20.0, -0.5], [20.0, 5.5]]),
     ('grid_v_22', [[21.0, -0.5], [21.0, 5.5]]),
     ('grid_v_23', [[22.0, -0.5], [22.0, 5.5]]),
     ('grid_v_24', [[23.0, -0.5], [23.0, 5.5]]),
     ('grid_v_25', [[24.0, -0.5], [24.0, 5.5]]),
     ('grid_v_26', [[25.0, -0.5], [25.0, 5.5]]),
     ('grid_v_27', [[26.0, -0.5], [26.0, 5.5]]),
     ('grid_v_28', [[27.0, -0.5], [27.0, 5.5]]),
     ('grid_v_29', [[28.0, -0.5], [28.0, 5.5]]),
     ('grid_v_30', [[29.0, -0.5], [29.0, 5.5]]),
     ('grid_v_31', [[30.0, -0.5], [30.0, 5.5]]),
     ('grid_v_32', [[31.0, -0.5], [31.0, 5.5]]),
     ('grid_v_33', [[32.0, -0.5], [32.0, 5.5]]),
     ('grid_v_34', [[33.0, -0.5], [33.0, 5.5]]),
     ('grid_v_35', [[34.0, -0.5], [34.0, 5.5]]),
     ('grid_v_36', [[35.0, -0.5], [35.0, 5.5]]),
     ('grid_v_37', [[36.0, -0.5], [36.0, 5.5]]),
     ('grid_v_38', [[37.0, -0.5], [37.0, 5.5]]),
     ('grid_v_39', [[38.0, -0.5], [38.0, 5.5]]),
     ('grid_v_40', [[39.0, -0.5], [39.0, 5.5]]),
     ('grid_v_41', [[40.0, -0.5], [40.0, 5.5]]),
     ('grid_h_0', [[-0.5, 0.0], [40.0, 0.0]]),
     ('grid_h_1', [[-0.5, 1.0], [40.0, 1.0]]),
     ('grid_h_2', [[-0.5, 2.0], [40.0, 2.0]]),
     ('grid_h_3', [[-0.5, 3.0], [40.0, 3.0]]),
     ('grid_h_4', [[-0.5, 4.0], [40.0, 4.0]]),
     ('grid_h_5', [[-0.5, 5.0], [40.0, 5.0]])]
    with Canvas(PLANE, xlim=(-1.9525462962962976, 41.0162037037037), ylim=(-19.111689814814817, 23.857060185185183), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        for object_id, points in _geometry_01:
            c.line(points, id=object_id, zorder=1, color='#A8A8A8', linewidth=0.5)
        c.line([[0, 0], [0, 5]], id='pattern_1', color='#EA580C', linewidth=1.5)
        c.line([[0, 5], [5, 5]], id='pattern_2', color='#2563EB', linewidth=1.5)
        c.line([[5, 5], [5, 0]], id='pattern_3', color='#EA580C', linewidth=1.5)
        c.line([[5, 0], [6, 0]], id='pattern_4')
        for object_id, points in [('corner_52', [[0.0, 0.0]]), ('corner_53', [[0.0, 5.0]]), ('corner_54', [[5.0, 5.0]]), ('corner_55', [[5.0, 0.0]]), ('corner_56', [[6.0, 0.0]])]:
            c.point(points, id=object_id, s=[24])
        for object_id, points in [('pattern_5', [[6, 0], [6, 3]]), ('pattern_6', [[6, 3], [9, 3]]), ('pattern_7', [[9, 3], [9, 0]]), ('pattern_8', [[9, 0], [10, 0]])]:
            c.line(points, id=object_id)
        for object_id, points in [('corner_61', [[6.0, 0.0]]), ('corner_62', [[6.0, 3.0]]), ('corner_63', [[9.0, 3.0]]), ('corner_64', [[9.0, 0.0]]), ('corner_65', [[10.0, 0.0]])]:
            c.point(points, id=object_id, s=[24])
        for object_id, points in [('pattern_9', [[10, 0], [10, 2]]), ('pattern_10', [[10, 2], [12, 2]]), ('pattern_11', [[12, 2], [12, 0]]), ('pattern_12', [[12, 0], [13, 0]])]:
            c.line(points, id=object_id)
        for object_id, points in [('corner_70', [[10.0, 0.0]]), ('corner_71', [[10.0, 2.0]]), ('corner_72', [[12.0, 2.0]]), ('corner_73', [[12.0, 0.0]]), ('corner_74', [[13.0, 0.0]])]:
            c.point(points, id=object_id, s=[24])
        c.line([[13, 0], [13, 5]], id='pattern_13', color='#EA580C', linewidth=1.5)
        c.line([[13, 5], [18, 5]], id='pattern_14', color='#2563EB', linewidth=1.5)
        c.line([[18, 5], [18, 0]], id='pattern_15', color='#EA580C', linewidth=1.5)
        c.line([[18, 0], [19, 0]], id='pattern_16')
        for object_id, points in [('corner_79', [[13.0, 0.0]]), ('corner_80', [[13.0, 5.0]]), ('corner_81', [[18.0, 5.0]]), ('corner_82', [[18.0, 0.0]]), ('corner_83', [[19.0, 0.0]])]:
            c.point(points, id=object_id, s=[24])
        for object_id, points in [('pattern_17', [[19, 0], [19, 3]]), ('pattern_18', [[19, 3], [22, 3]]), ('pattern_19', [[22, 3], [22, 0]]), ('pattern_20', [[22, 0], [23, 0]])]:
            c.line(points, id=object_id)
        for object_id, points in [('corner_88', [[19.0, 0.0]]), ('corner_89', [[19.0, 3.0]]), ('corner_90', [[22.0, 3.0]]), ('corner_91', [[22.0, 0.0]]), ('corner_92', [[23.0, 0.0]])]:
            c.point(points, id=object_id, s=[24])
        for object_id, points in [('pattern_21', [[23, 0], [23, 2]]), ('pattern_22', [[23, 2], [25, 2]]), ('pattern_23', [[25, 2], [25, 0]]), ('pattern_24', [[25, 0], [26, 0]])]:
            c.line(points, id=object_id)
        for object_id, points in [('corner_97', [[23.0, 0.0]]), ('corner_98', [[23.0, 2.0]]), ('corner_99', [[25.0, 2.0]]), ('corner_100', [[25.0, 0.0]]), ('corner_101', [[26.0, 0.0]]), ('choice_A', [[28.0, 2.0]]), ('choice_D', [[30.0, 4.0]]), ('choice_C', [[33.0, 1.0]]), ('choice_B', [[35.0, 2.0]]), ('choice_E', [[38.0, 4.0]])]:
            c.point(points, id=object_id, s=[24])
        for object_id, text, anchor in [(None, 'A', (28, 2)), (None, 'D', (30, 4)), (None, 'C', (33, 1)), (None, 'B', (35, 2)), (None, 'E', (38, 4))]:
            c.text(text, anchor, id=object_id, clip_on=True, fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(0, -15), annotation_clip=None)
        c.point([[28.0, 2.0]], zorder=10, s=[50], facecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]], edgecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]])
        return c.save(output_path)

def C02(output_path=None):
    if output_path is None:
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / 'Plane496_C02.png'
    _geometry_01 = [('grid_v_0', [[-1.0, -0.5], [-1.0, 5.5]]),
     ('grid_v_1', [[0.0, -0.5], [0.0, 5.5]]),
     ('grid_v_2', [[1.0, -0.5], [1.0, 5.5]]),
     ('grid_v_3', [[2.0, -0.5], [2.0, 5.5]]),
     ('grid_v_4', [[3.0, -0.5], [3.0, 5.5]]),
     ('grid_v_5', [[4.0, -0.5], [4.0, 5.5]]),
     ('grid_v_6', [[5.0, -0.5], [5.0, 5.5]]),
     ('grid_v_7', [[6.0, -0.5], [6.0, 5.5]]),
     ('grid_v_8', [[7.0, -0.5], [7.0, 5.5]]),
     ('grid_v_9', [[8.0, -0.5], [8.0, 5.5]]),
     ('grid_v_10', [[9.0, -0.5], [9.0, 5.5]]),
     ('grid_v_11', [[10.0, -0.5], [10.0, 5.5]]),
     ('grid_v_12', [[11.0, -0.5], [11.0, 5.5]]),
     ('grid_v_13', [[12.0, -0.5], [12.0, 5.5]]),
     ('grid_v_14', [[13.0, -0.5], [13.0, 5.5]]),
     ('grid_v_15', [[14.0, -0.5], [14.0, 5.5]]),
     ('grid_v_16', [[15.0, -0.5], [15.0, 5.5]]),
     ('grid_v_17', [[16.0, -0.5], [16.0, 5.5]]),
     ('grid_v_18', [[17.0, -0.5], [17.0, 5.5]]),
     ('grid_v_19', [[18.0, -0.5], [18.0, 5.5]]),
     ('grid_v_20', [[19.0, -0.5], [19.0, 5.5]]),
     ('grid_v_21', [[20.0, -0.5], [20.0, 5.5]]),
     ('grid_v_22', [[21.0, -0.5], [21.0, 5.5]]),
     ('grid_v_23', [[22.0, -0.5], [22.0, 5.5]]),
     ('grid_v_24', [[23.0, -0.5], [23.0, 5.5]]),
     ('grid_v_25', [[24.0, -0.5], [24.0, 5.5]]),
     ('grid_v_26', [[25.0, -0.5], [25.0, 5.5]]),
     ('grid_v_27', [[26.0, -0.5], [26.0, 5.5]]),
     ('grid_v_28', [[27.0, -0.5], [27.0, 5.5]]),
     ('grid_v_29', [[28.0, -0.5], [28.0, 5.5]]),
     ('grid_v_30', [[29.0, -0.5], [29.0, 5.5]]),
     ('grid_v_31', [[30.0, -0.5], [30.0, 5.5]]),
     ('grid_v_32', [[31.0, -0.5], [31.0, 5.5]]),
     ('grid_v_33', [[32.0, -0.5], [32.0, 5.5]]),
     ('grid_v_34', [[33.0, -0.5], [33.0, 5.5]]),
     ('grid_v_35', [[34.0, -0.5], [34.0, 5.5]]),
     ('grid_v_36', [[35.0, -0.5], [35.0, 5.5]]),
     ('grid_v_37', [[36.0, -0.5], [36.0, 5.5]]),
     ('grid_v_38', [[37.0, -0.5], [37.0, 5.5]]),
     ('grid_v_39', [[38.0, -0.5], [38.0, 5.5]]),
     ('grid_v_40', [[39.0, -0.5], [39.0, 5.5]]),
     ('grid_v_41', [[40.0, -0.5], [40.0, 5.5]]),
     ('grid_h_0', [[-0.5, 0.0], [40.0, 0.0]]),
     ('grid_h_1', [[-0.5, 1.0], [40.0, 1.0]]),
     ('grid_h_2', [[-0.5, 2.0], [40.0, 2.0]]),
     ('grid_h_3', [[-0.5, 3.0], [40.0, 3.0]]),
     ('grid_h_4', [[-0.5, 4.0], [40.0, 4.0]]),
     ('grid_h_5', [[-0.5, 5.0], [40.0, 5.0]])]
    with Canvas(PLANE, xlim=(-1.9525462962962976, 41.0162037037037), ylim=(-19.111689814814817, 23.857060185185183), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        for object_id, points in _geometry_01:
            c.line(points, id=object_id, zorder=1, color='#A8A8A8', linewidth=0.5)
        for object_id, points in [('pattern_1', [[0, 0], [0, 5]]), ('pattern_2', [[0, 5], [5, 5]]), ('pattern_3', [[5, 5], [5, 0]]), ('pattern_4', [[5, 0], [6, 0]])]:
            c.line(points, id=object_id)
        for object_id, points in [('corner_52', [[0.0, 0.0]]), ('corner_53', [[0.0, 5.0]]), ('corner_54', [[5.0, 5.0]]), ('corner_55', [[5.0, 0.0]]), ('corner_56', [[6.0, 0.0]])]:
            c.point(points, id=object_id, s=[24])
        for object_id, points in [('pattern_5', [[6, 0], [6, 3]]), ('pattern_6', [[6, 3], [9, 3]]), ('pattern_7', [[9, 3], [9, 0]]), ('pattern_8', [[9, 0], [10, 0]])]:
            c.line(points, id=object_id)
        for object_id, points in [('corner_61', [[6.0, 0.0]]), ('corner_62', [[6.0, 3.0]]), ('corner_63', [[9.0, 3.0]]), ('corner_64', [[9.0, 0.0]]), ('corner_65', [[10.0, 0.0]])]:
            c.point(points, id=object_id, s=[24])
        for object_id, points in [('pattern_9', [[10, 0], [10, 2]]), ('pattern_10', [[10, 2], [12, 2]]), ('pattern_11', [[12, 2], [12, 0]]), ('pattern_12', [[12, 0], [13, 0]])]:
            c.line(points, id=object_id)
        for object_id, points in [('corner_70', [[10.0, 0.0]]), ('corner_71', [[10.0, 2.0]]), ('corner_72', [[12.0, 2.0]]), ('corner_73', [[12.0, 0.0]]), ('corner_74', [[13.0, 0.0]])]:
            c.point(points, id=object_id, s=[24])
        for object_id, points in [('pattern_13', [[13, 0], [13, 5]]), ('pattern_14', [[13, 5], [18, 5]]), ('pattern_15', [[18, 5], [18, 0]]), ('pattern_16', [[18, 0], [19, 0]])]:
            c.line(points, id=object_id)
        for object_id, points in [('corner_79', [[13.0, 0.0]]), ('corner_80', [[13.0, 5.0]]), ('corner_81', [[18.0, 5.0]]), ('corner_82', [[18.0, 0.0]]), ('corner_83', [[19.0, 0.0]])]:
            c.point(points, id=object_id, s=[24])
        for object_id, points in [('pattern_17', [[19, 0], [19, 3]]), ('pattern_18', [[19, 3], [22, 3]]), ('pattern_19', [[22, 3], [22, 0]]), ('pattern_20', [[22, 0], [23, 0]])]:
            c.line(points, id=object_id)
        for object_id, points in [('corner_88', [[19.0, 0.0]]), ('corner_89', [[19.0, 3.0]]), ('corner_90', [[22.0, 3.0]]), ('corner_91', [[22.0, 0.0]]), ('corner_92', [[23.0, 0.0]])]:
            c.point(points, id=object_id, s=[24])
        for object_id, points in [('pattern_21', [[23, 0], [23, 2]]), ('pattern_22', [[23, 2], [25, 2]]), ('pattern_23', [[25, 2], [25, 0]]), ('pattern_24', [[25, 0], [26, 0]])]:
            c.line(points, id=object_id)
        for object_id, points in [('corner_97', [[23.0, 0.0]]), ('corner_98', [[23.0, 2.0]]), ('corner_99', [[25.0, 2.0]]), ('corner_100', [[25.0, 0.0]]), ('corner_101', [[26.0, 0.0]]), ('choice_A', [[28.0, 2.0]]), ('choice_D', [[30.0, 4.0]]), ('choice_C', [[33.0, 1.0]]), ('choice_B', [[35.0, 2.0]]), ('choice_E', [[38.0, 4.0]])]:
            c.point(points, id=object_id, s=[24])
        for object_id, text, anchor in [(None, 'A', (28, 2)), (None, 'D', (30, 4)), (None, 'C', (33, 1)), (None, 'B', (35, 2)), (None, 'E', (38, 4))]:
            c.text(text, anchor, id=object_id, clip_on=True, fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(0, -15), annotation_clip=None)
        c.point([[30.0, 4.0]], zorder=10, s=[50], facecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]], edgecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]])
        return c.save(output_path)

def C03(output_path=None):
    if output_path is None:
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / 'Plane496_C03.png'
    _geometry_01 = [('grid_v_0', [[-1.0, -0.5], [-1.0, 5.5]]),
     ('grid_v_1', [[0.0, -0.5], [0.0, 5.5]]),
     ('grid_v_2', [[1.0, -0.5], [1.0, 5.5]]),
     ('grid_v_3', [[2.0, -0.5], [2.0, 5.5]]),
     ('grid_v_4', [[3.0, -0.5], [3.0, 5.5]]),
     ('grid_v_5', [[4.0, -0.5], [4.0, 5.5]]),
     ('grid_v_6', [[5.0, -0.5], [5.0, 5.5]]),
     ('grid_v_7', [[6.0, -0.5], [6.0, 5.5]]),
     ('grid_v_8', [[7.0, -0.5], [7.0, 5.5]]),
     ('grid_v_9', [[8.0, -0.5], [8.0, 5.5]]),
     ('grid_v_10', [[9.0, -0.5], [9.0, 5.5]]),
     ('grid_v_11', [[10.0, -0.5], [10.0, 5.5]]),
     ('grid_v_12', [[11.0, -0.5], [11.0, 5.5]]),
     ('grid_v_13', [[12.0, -0.5], [12.0, 5.5]]),
     ('grid_v_14', [[13.0, -0.5], [13.0, 5.5]]),
     ('grid_v_15', [[14.0, -0.5], [14.0, 5.5]]),
     ('grid_v_16', [[15.0, -0.5], [15.0, 5.5]]),
     ('grid_v_17', [[16.0, -0.5], [16.0, 5.5]]),
     ('grid_v_18', [[17.0, -0.5], [17.0, 5.5]]),
     ('grid_v_19', [[18.0, -0.5], [18.0, 5.5]]),
     ('grid_v_20', [[19.0, -0.5], [19.0, 5.5]]),
     ('grid_v_21', [[20.0, -0.5], [20.0, 5.5]]),
     ('grid_v_22', [[21.0, -0.5], [21.0, 5.5]]),
     ('grid_v_23', [[22.0, -0.5], [22.0, 5.5]]),
     ('grid_v_24', [[23.0, -0.5], [23.0, 5.5]]),
     ('grid_v_25', [[24.0, -0.5], [24.0, 5.5]]),
     ('grid_v_26', [[25.0, -0.5], [25.0, 5.5]]),
     ('grid_v_27', [[26.0, -0.5], [26.0, 5.5]]),
     ('grid_v_28', [[27.0, -0.5], [27.0, 5.5]]),
     ('grid_v_29', [[28.0, -0.5], [28.0, 5.5]]),
     ('grid_v_30', [[29.0, -0.5], [29.0, 5.5]]),
     ('grid_v_31', [[30.0, -0.5], [30.0, 5.5]]),
     ('grid_v_32', [[31.0, -0.5], [31.0, 5.5]]),
     ('grid_v_33', [[32.0, -0.5], [32.0, 5.5]]),
     ('grid_v_34', [[33.0, -0.5], [33.0, 5.5]]),
     ('grid_v_35', [[34.0, -0.5], [34.0, 5.5]]),
     ('grid_v_36', [[35.0, -0.5], [35.0, 5.5]]),
     ('grid_v_37', [[36.0, -0.5], [36.0, 5.5]]),
     ('grid_v_38', [[37.0, -0.5], [37.0, 5.5]]),
     ('grid_v_39', [[38.0, -0.5], [38.0, 5.5]]),
     ('grid_v_40', [[39.0, -0.5], [39.0, 5.5]]),
     ('grid_v_41', [[40.0, -0.5], [40.0, 5.5]]),
     ('grid_h_0', [[-0.5, 0.0], [40.0, 0.0]]),
     ('grid_h_1', [[-0.5, 1.0], [40.0, 1.0]]),
     ('grid_h_2', [[-0.5, 2.0], [40.0, 2.0]]),
     ('grid_h_3', [[-0.5, 3.0], [40.0, 3.0]]),
     ('grid_h_4', [[-0.5, 4.0], [40.0, 4.0]]),
     ('grid_h_5', [[-0.5, 5.0], [40.0, 5.0]])]
    with Canvas(PLANE, xlim=(-1.9525462962962976, 41.0162037037037), ylim=(-19.111689814814817, 23.857060185185183), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        for object_id, points in _geometry_01:
            c.line(points, id=object_id, zorder=1, color='#A8A8A8', linewidth=0.5)
        for object_id, points in [('pattern_1', [[0, 0], [0, 5]]), ('pattern_2', [[0, 5], [5, 5]]), ('pattern_3', [[5, 5], [5, 0]]), ('pattern_4', [[5, 0], [6, 0]])]:
            c.line(points, id=object_id)
        for object_id, points in [('corner_52', [[0.0, 0.0]]), ('corner_53', [[0.0, 5.0]]), ('corner_54', [[5.0, 5.0]]), ('corner_55', [[5.0, 0.0]]), ('corner_56', [[6.0, 0.0]])]:
            c.point(points, id=object_id, s=[24])
        for object_id, points in [('pattern_5', [[6, 0], [6, 3]]), ('pattern_6', [[6, 3], [9, 3]]), ('pattern_7', [[9, 3], [9, 0]]), ('pattern_8', [[9, 0], [10, 0]])]:
            c.line(points, id=object_id)
        for object_id, points in [('corner_61', [[6.0, 0.0]]), ('corner_62', [[6.0, 3.0]]), ('corner_63', [[9.0, 3.0]]), ('corner_64', [[9.0, 0.0]]), ('corner_65', [[10.0, 0.0]])]:
            c.point(points, id=object_id, s=[24])
        for object_id, points in [('pattern_9', [[10, 0], [10, 2]]), ('pattern_10', [[10, 2], [12, 2]]), ('pattern_11', [[12, 2], [12, 0]]), ('pattern_12', [[12, 0], [13, 0]])]:
            c.line(points, id=object_id)
        for object_id, points in [('corner_70', [[10.0, 0.0]]), ('corner_71', [[10.0, 2.0]]), ('corner_72', [[12.0, 2.0]]), ('corner_73', [[12.0, 0.0]]), ('corner_74', [[13.0, 0.0]])]:
            c.point(points, id=object_id, s=[24])
        for object_id, points in [('pattern_13', [[13, 0], [13, 5]]), ('pattern_14', [[13, 5], [18, 5]]), ('pattern_15', [[18, 5], [18, 0]]), ('pattern_16', [[18, 0], [19, 0]])]:
            c.line(points, id=object_id)
        for object_id, points in [('corner_79', [[13.0, 0.0]]), ('corner_80', [[13.0, 5.0]]), ('corner_81', [[18.0, 5.0]]), ('corner_82', [[18.0, 0.0]]), ('corner_83', [[19.0, 0.0]])]:
            c.point(points, id=object_id, s=[24])
        for object_id, points in [('pattern_17', [[19, 0], [19, 3]]), ('pattern_18', [[19, 3], [22, 3]]), ('pattern_19', [[22, 3], [22, 0]]), ('pattern_20', [[22, 0], [23, 0]])]:
            c.line(points, id=object_id)
        for object_id, points in [('corner_88', [[19.0, 0.0]]), ('corner_89', [[19.0, 3.0]]), ('corner_90', [[22.0, 3.0]]), ('corner_91', [[22.0, 0.0]]), ('corner_92', [[23.0, 0.0]])]:
            c.point(points, id=object_id, s=[24])
        for object_id, points in [('pattern_21', [[23, 0], [23, 2]]), ('pattern_22', [[23, 2], [25, 2]]), ('pattern_23', [[25, 2], [25, 0]]), ('pattern_24', [[25, 0], [26, 0]])]:
            c.line(points, id=object_id)
        for object_id, points in [('corner_97', [[23.0, 0.0]]), ('corner_98', [[23.0, 2.0]]), ('corner_99', [[25.0, 2.0]]), ('corner_100', [[25.0, 0.0]]), ('corner_101', [[26.0, 0.0]]), ('choice_A', [[28.0, 2.0]]), ('choice_D', [[30.0, 4.0]]), ('choice_C', [[33.0, 1.0]]), ('choice_B', [[35.0, 2.0]]), ('choice_E', [[38.0, 4.0]])]:
            c.point(points, id=object_id, s=[24])
        for object_id, text, anchor in [(None, 'A', (28, 2)), (None, 'D', (30, 4)), (None, 'C', (33, 1)), (None, 'B', (35, 2)), (None, 'E', (38, 4))]:
            c.text(text, anchor, id=object_id, clip_on=True, fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(0, -15), annotation_clip=None)
        c.point([[38.0, 4.0]], zorder=10, s=[50], facecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]], edgecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]])
        return c.save(output_path)
