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
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / 'Plane247_C01.png'
    _geometry_01 = [('remaining_square_0', [[0.0, 0.0], [0.0, 1.0]]),
     ('remaining_square_1', [[0.0, 0.0], [1.0, 0.0]]),
     ('remaining_square_2', [[0.0, 1.0], [0.0, 2.0]]),
     ('remaining_square_3', [[0.0, 1.0], [1.0, 1.0]]),
     ('remaining_square_4', [[0.0, 2.0], [0.0, 3.0]]),
     ('remaining_square_5', [[0.0, 2.0], [1.0, 2.0]]),
     ('remaining_square_6', [[0.0, 3.0], [0.0, 4.0]]),
     ('remaining_square_7', [[0.0, 3.0], [1.0, 3.0]]),
     ('remaining_square_8', [[0.0, 4.0], [0.0, 5.0]]),
     ('remaining_square_9', [[0.0, 4.0], [1.0, 4.0]]),
     ('remaining_square_10', [[0.0, 5.0], [0.0, 6.0]]),
     ('remaining_square_11', [[0.0, 5.0], [1.0, 5.0]]),
     ('remaining_square_12', [[0.0, 6.0], [0.0, 7.0]]),
     ('remaining_square_13', [[0.0, 6.0], [1.0, 6.0]]),
     ('remaining_square_14', [[0.0, 7.0], [1.0, 7.0]]),
     ('remaining_square_15', [[1.0, 0.0], [1.0, 1.0]]),
     ('remaining_square_16', [[1.0, 0.0], [2.0, 0.0]]),
     ('remaining_square_17', [[1.0, 1.0], [1.0, 2.0]]),
     ('remaining_square_18', [[1.0, 1.0], [2.0, 1.0]]),
     ('remaining_square_19', [[1.0, 2.0], [1.0, 3.0]]),
     ('remaining_square_20', [[1.0, 2.0], [2.0, 2.0]]),
     ('remaining_square_21', [[1.0, 3.0], [1.0, 4.0]]),
     ('remaining_square_22', [[1.0, 3.0], [2.0, 3.0]]),
     ('remaining_square_23', [[1.0, 4.0], [1.0, 5.0]]),
     ('remaining_square_24', [[1.0, 4.0], [2.0, 4.0]]),
     ('remaining_square_25', [[1.0, 5.0], [1.0, 6.0]]),
     ('remaining_square_26', [[1.0, 5.0], [2.0, 5.0]]),
     ('remaining_square_27', [[1.0, 6.0], [1.0, 7.0]]),
     ('remaining_square_28', [[1.0, 6.0], [2.0, 6.0]]),
     ('remaining_square_29', [[1.0, 7.0], [2.0, 7.0]]),
     ('remaining_square_30', [[2.0, 0.0], [2.0, 1.0]]),
     ('remaining_square_31', [[2.0, 0.0], [3.0, 0.0]]),
     ('remaining_square_32', [[2.0, 1.0], [2.0, 2.0]]),
     ('remaining_square_33', [[2.0, 1.0], [3.0, 1.0]]),
     ('remaining_square_34', [[2.0, 2.0], [2.0, 3.0]]),
     ('remaining_square_35', [[2.0, 2.0], [3.0, 2.0]]),
     ('remaining_square_36', [[2.0, 3.0], [2.0, 4.0]]),
     ('remaining_square_37', [[2.0, 4.0], [2.0, 5.0]]),
     ('remaining_square_38', [[2.0, 5.0], [2.0, 6.0]]),
     ('remaining_square_39', [[2.0, 5.0], [3.0, 5.0]]),
     ('remaining_square_40', [[2.0, 6.0], [2.0, 7.0]]),
     ('remaining_square_41', [[2.0, 6.0], [3.0, 6.0]]),
     ('remaining_square_42', [[2.0, 7.0], [3.0, 7.0]]),
     ('remaining_square_43', [[3.0, 0.0], [3.0, 1.0]]),
     ('remaining_square_44', [[3.0, 0.0], [4.0, 0.0]]),
     ('remaining_square_45', [[3.0, 1.0], [3.0, 2.0]]),
     ('remaining_square_46', [[3.0, 1.0], [4.0, 1.0]]),
     ('remaining_square_47', [[3.0, 5.0], [3.0, 6.0]]),
     ('remaining_square_48', [[3.0, 5.0], [4.0, 5.0]]),
     ('remaining_square_49', [[3.0, 6.0], [3.0, 7.0]]),
     ('remaining_square_50', [[3.0, 6.0], [4.0, 6.0]]),
     ('remaining_square_51', [[3.0, 7.0], [4.0, 7.0]]),
     ('remaining_square_52', [[4.0, 0.0], [4.0, 1.0]])]
    _geometry_02 = [('piece1_10', [[11.0, 3.0], [12.0, 3.0]]),
     ('piece1_11', [[12.0, 1.0], [12.0, 2.0]]),
     ('piece1_12', [[12.0, 1.0], [13.0, 1.0]]),
     ('piece1_13', [[12.0, 2.0], [12.0, 3.0]]),
     ('piece1_14', [[12.0, 2.0], [13.0, 2.0]]),
     ('piece1_15', [[12.0, 3.0], [13.0, 3.0]]),
     ('piece1_16', [[13.0, 0.0], [13.0, 1.0]]),
     ('piece1_17', [[13.0, 0.0], [14.0, 0.0]]),
     ('piece1_18', [[13.0, 1.0], [13.0, 2.0]]),
     ('piece1_19', [[13.0, 1.0], [14.0, 1.0]]),
     ('piece1_20', [[13.0, 2.0], [13.0, 3.0]]),
     ('piece1_21', [[13.0, 2.0], [14.0, 2.0]]),
     ('piece1_22', [[13.0, 3.0], [14.0, 3.0]]),
     ('piece1_23', [[14.0, 0.0], [14.0, 1.0]]),
     ('piece1_24', [[14.0, 1.0], [14.0, 2.0]]),
     ('piece1_25', [[14.0, 2.0], [14.0, 3.0]]),
     ('piece2_0', [[15.0, 2.0], [15.0, 3.0]]),
     ('piece2_1', [[15.0, 2.0], [16.0, 2.0]]),
     ('piece2_2', [[15.0, 3.0], [15.0, 4.0]]),
     ('piece2_3', [[15.0, 3.0], [16.0, 3.0]]),
     ('piece2_4', [[15.0, 4.0], [16.0, 4.0]]),
     ('piece2_5', [[16.0, 1.0], [16.0, 2.0]]),
     ('piece2_6', [[16.0, 1.0], [17.0, 1.0]]),
     ('piece2_7', [[16.0, 2.0], [16.0, 3.0]]),
     ('piece2_8', [[16.0, 2.0], [17.0, 2.0]]),
     ('piece2_9', [[16.0, 3.0], [16.0, 4.0]]),
     ('piece2_10', [[16.0, 3.0], [17.0, 3.0]]),
     ('piece2_11', [[17.0, 0.0], [17.0, 1.0]]),
     ('piece2_12', [[17.0, 0.0], [18.0, 0.0]]),
     ('piece2_13', [[17.0, 1.0], [17.0, 2.0]]),
     ('piece2_14', [[17.0, 1.0], [18.0, 1.0]]),
     ('piece2_15', [[17.0, 2.0], [17.0, 3.0]]),
     ('piece2_16', [[17.0, 2.0], [18.0, 2.0]]),
     ('piece2_17', [[17.0, 3.0], [18.0, 3.0]]),
     ('piece2_18', [[18.0, 0.0], [18.0, 1.0]]),
     ('piece2_19', [[18.0, 0.0], [19.0, 0.0]]),
     ('piece2_20', [[18.0, 1.0], [18.0, 2.0]]),
     ('piece2_21', [[18.0, 1.0], [19.0, 1.0]]),
     ('piece2_22', [[18.0, 2.0], [18.0, 3.0]]),
     ('piece2_23', [[18.0, 2.0], [19.0, 2.0]]),
     ('piece2_24', [[18.0, 3.0], [19.0, 3.0]]),
     ('piece2_25', [[19.0, 0.0], [19.0, 1.0]]),
     ('piece2_26', [[19.0, 1.0], [19.0, 2.0]]),
     ('piece2_27', [[19.0, 2.0], [19.0, 3.0]]),
     ('piece3_0', [[20.0, 1.0], [20.0, 2.0]]),
     ('piece3_1', [[20.0, 1.0], [21.0, 1.0]]),
     ('piece3_2', [[20.0, 2.0], [20.0, 3.0]]),
     ('piece3_3', [[20.0, 2.0], [21.0, 2.0]]),
     ('piece3_4', [[20.0, 3.0], [21.0, 3.0]]),
     ('piece3_5', [[21.0, 0.0], [21.0, 1.0]]),
     ('piece3_6', [[21.0, 0.0], [22.0, 0.0]]),
     ('piece3_7', [[21.0, 1.0], [21.0, 2.0]]),
     ('piece3_8', [[21.0, 1.0], [22.0, 1.0]]),
     ('piece3_9', [[21.0, 2.0], [21.0, 3.0]]),
     ('piece3_10', [[21.0, 2.0], [22.0, 2.0]]),
     ('piece3_11', [[21.0, 3.0], [22.0, 3.0]]),
     ('piece3_12', [[22.0, 0.0], [22.0, 1.0]]),
     ('piece3_13', [[22.0, 1.0], [22.0, 2.0]]),
     ('piece3_14', [[22.0, 2.0], [22.0, 3.0]]),
     ('piece3_15', [[22.0, 2.0], [23.0, 2.0]]),
     ('piece3_16', [[22.0, 3.0], [22.0, 4.0]]),
     ('piece3_17', [[22.0, 3.0], [23.0, 3.0]]),
     ('piece3_18', [[22.0, 4.0], [23.0, 4.0]]),
     ('piece3_19', [[23.0, 2.0], [23.0, 3.0]]),
     ('piece3_20', [[23.0, 3.0], [23.0, 4.0]]),
     ('piece4_0', [[25.0, 1.0], [25.0, 2.0]]),
     ('piece4_1', [[25.0, 1.0], [26.0, 1.0]]),
     ('piece4_2', [[25.0, 2.0], [25.0, 3.0]]),
     ('piece4_3', [[25.0, 2.0], [26.0, 2.0]]),
     ('piece4_4', [[25.0, 3.0], [25.0, 4.0]]),
     ('piece4_5', [[25.0, 3.0], [26.0, 3.0]]),
     ('piece4_6', [[25.0, 4.0], [26.0, 4.0]]),
     ('piece4_7', [[26.0, 1.0], [26.0, 2.0]]),
     ('piece4_8', [[26.0, 1.0], [27.0, 1.0]]),
     ('piece4_9', [[26.0, 2.0], [26.0, 3.0]]),
     ('piece4_10', [[26.0, 2.0], [27.0, 2.0]]),
     ('piece4_11', [[26.0, 3.0], [26.0, 4.0]]),
     ('piece4_12', [[27.0, 0.0], [27.0, 1.0]]),
     ('piece4_13', [[27.0, 0.0], [28.0, 0.0]]),
     ('piece4_14', [[27.0, 1.0], [27.0, 2.0]]),
     ('piece4_15', [[27.0, 1.0], [28.0, 1.0]]),
     ('piece4_16', [[27.0, 2.0], [27.0, 3.0]]),
     ('piece4_17', [[27.0, 2.0], [28.0, 2.0]]),
     ('piece4_18', [[27.0, 3.0], [28.0, 3.0]]),
     ('piece4_19', [[28.0, 0.0], [28.0, 1.0]]),
     ('piece4_20', [[28.0, 0.0], [29.0, 0.0]]),
     ('piece4_21', [[28.0, 1.0], [28.0, 2.0]]),
     ('piece4_22', [[28.0, 1.0], [29.0, 1.0]]),
     ('piece4_23', [[28.0, 2.0], [28.0, 3.0]]),
     ('piece4_24', [[29.0, 0.0], [29.0, 1.0]])]
    with Canvas(PLANE, xlim=(-0.7422490307749534, 29.775315456542568), ylim=(-11.777664975409404, 18.739899511908117), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        for object_id, points in _geometry_01:
            c.line(points, id=object_id)
        c.line([[4.0, 5.0], [4.0, 6.0]], id='remaining_square_53', color='#DC2626', linewidth=1.5)
        c.line([[4.0, 6.0], [4.0, 7.0]], id='remaining_square_54')
        c.line([[4.0, 6.0], [5.0, 6.0]], id='remaining_square_55', color='#DC2626', linewidth=1.5)
        for object_id, points in [('remaining_square_56', [[4.0, 7.0], [5.0, 7.0]]), ('remaining_square_57', [[5.0, 3.0], [5.0, 4.0]]), ('remaining_square_58', [[5.0, 3.0], [6.0, 3.0]]), ('remaining_square_59', [[5.0, 4.0], [5.0, 5.0]]), ('remaining_square_60', [[5.0, 4.0], [6.0, 4.0]])]:
            c.line(points, id=object_id)
        c.line([[5.0, 5.0], [6.0, 5.0]], id='remaining_square_61', color='#DC2626', linewidth=1.5)
        c.line([[5.0, 6.0], [5.0, 7.0]], id='remaining_square_62')
        c.line([[5.0, 6.0], [6.0, 6.0]], id='remaining_square_63', color='#DC2626', linewidth=1.5)
        for object_id, points in [('remaining_square_64', [[5.0, 7.0], [6.0, 7.0]]), ('remaining_square_65', [[6.0, 0.0], [6.0, 1.0]]), ('remaining_square_66', [[6.0, 0.0], [7.0, 0.0]]), ('remaining_square_67', [[6.0, 1.0], [6.0, 2.0]]), ('remaining_square_68', [[6.0, 1.0], [7.0, 1.0]]), ('remaining_square_69', [[6.0, 2.0], [6.0, 3.0]]), ('remaining_square_70', [[6.0, 2.0], [7.0, 2.0]]), ('remaining_square_71', [[6.0, 3.0], [6.0, 4.0]]), ('remaining_square_72', [[6.0, 3.0], [7.0, 3.0]]), ('remaining_square_73', [[6.0, 4.0], [6.0, 5.0]]), ('remaining_square_74', [[6.0, 4.0], [7.0, 4.0]])]:
            c.line(points, id=object_id)
        c.line([[6.0, 5.0], [6.0, 6.0]], id='remaining_square_75', color='#DC2626', linewidth=1.5)
        for object_id, points in [('remaining_square_76', [[6.0, 5.0], [7.0, 5.0]]), ('remaining_square_77', [[6.0, 6.0], [6.0, 7.0]]), ('remaining_square_78', [[6.0, 6.0], [7.0, 6.0]]), ('remaining_square_79', [[6.0, 7.0], [7.0, 7.0]]), ('remaining_square_80', [[7.0, 0.0], [7.0, 1.0]]), ('remaining_square_81', [[7.0, 1.0], [7.0, 2.0]]), ('remaining_square_82', [[7.0, 2.0], [7.0, 3.0]]), ('remaining_square_83', [[7.0, 3.0], [7.0, 4.0]]), ('remaining_square_84', [[7.0, 4.0], [7.0, 5.0]]), ('remaining_square_85', [[7.0, 5.0], [7.0, 6.0]]), ('remaining_square_86', [[7.0, 6.0], [7.0, 7.0]])]:
            c.line(points, id=object_id)
        c.line([[4.0, 0.0], [6.0, 0.0]], id='cutout_bottom_boundary', linestyle=(0.0, [4.0, 3.0]))
        for object_id, points in [('piece1_0', [[10.0, 2.0], [10.0, 3.0]]), ('piece1_1', [[10.0, 2.0], [11.0, 2.0]]), ('piece1_2', [[10.0, 3.0], [10.0, 4.0]])]:
            c.line(points, id=object_id, color='#DC2626', linewidth=1.5)
        c.line([[10.0, 3.0], [11.0, 3.0]], id='piece1_3')
        c.line([[10.0, 4.0], [11.0, 4.0]], id='piece1_4', color='#DC2626', linewidth=1.5)
        for object_id, points in [('piece1_5', [[11.0, 1.0], [11.0, 2.0]]), ('piece1_6', [[11.0, 1.0], [12.0, 1.0]]), ('piece1_7', [[11.0, 2.0], [11.0, 3.0]]), ('piece1_8', [[11.0, 2.0], [12.0, 2.0]])]:
            c.line(points, id=object_id)
        c.line([[11.0, 3.0], [11.0, 4.0]], id='piece1_9', color='#DC2626', linewidth=1.5)
        for object_id, points in _geometry_02:
            c.line(points, id=object_id)
        for object_id, text, anchor in [('label0', '1', (11.8, 4.8)), ('label1', '2', (16.8, 4.8)), ('label2', '3', (21.8, 4.8)), ('label3', '4', (26.8, 4.8))]:
            c.text(text, anchor, id=object_id, rotation_mode='default', offset_pt=(0, 0), annotation_clip=None)
        return c.save(output_path)
