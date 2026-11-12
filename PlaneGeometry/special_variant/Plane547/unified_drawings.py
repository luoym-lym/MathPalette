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
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / 'Plane547_C01.png'
    _geometry_01 = [('fold_process_arrow', [[41, 84], [59, 84]]),
     ('fold_process_arrow_head_1', [[59.0, 84.0], [57.0, 85.1]]),
     ('fold_process_arrow_head_2', [[59.0, 84.0], [57.0, 82.9]]),
     ('option_A_boundary_0', [[4.0, 38.0], [28.0, 38.0]]),
     ('option_A_boundary_1', [[28.0, 38.0], [28.0, 41.3]]),
     ('option_A_boundary_2', [[28.0, 46.7], [28.0, 62.0]]),
     ('option_A_boundary_3', [[28.0, 62.0], [4.0, 62.0]]),
     ('option_A_boundary_4', [[4.0, 62.0], [4.0, 46.7]]),
     ('option_A_boundary_5', [[4.0, 41.3], [4.0, 38.0]]),
     ('option_A_boundary_6', [[16.0, 47.6], [19.6, 50.0]]),
     ('option_A_boundary_7', [[19.6, 50.0], [16.0, 52.4]]),
     ('option_A_boundary_8', [[21.4, 54.8], [23.8, 54.8]]),
     ('option_A_boundary_9', [[23.8, 54.8], [23.8, 57.2]]),
     ('option_A_boundary_10', [[23.8, 57.2], [21.4, 57.2]]),
     ('option_A_boundary_11', [[21.4, 57.2], [21.4, 54.8]]),
     ('option_A_boundary_12', [[28.0, 41.3], [25.0, 44.0]]),
     ('option_A_boundary_13', [[25.0, 44.0], [28.0, 46.7]]),
     ('option_A_boundary_14', [[16.0, 47.6], [12.4, 50.0]]),
     ('option_A_boundary_15', [[12.4, 50.0], [16.0, 52.4]]),
     ('option_A_boundary_16', [[10.6, 54.8], [8.2, 54.8]]),
     ('option_A_boundary_17', [[8.2, 54.8], [8.2, 57.2]]),
     ('option_A_boundary_18', [[8.2, 57.2], [10.6, 57.2]]),
     ('option_A_boundary_19', [[10.6, 57.2], [10.6, 54.8]]),
     ('option_A_boundary_20', [[4.0, 41.3], [7.0, 44.0]]),
     ('option_A_boundary_21', [[7.0, 44.0], [4.0, 46.7]])]
    _geometry_02 = [('option_D_boundary_0', [[21.0, 6.0], [45.0, 6.0]]),
     ('option_D_boundary_1', [[45.0, 6.0], [45.0, 9.3]]),
     ('option_D_boundary_2', [[45.0, 14.7], [45.0, 30.0]]),
     ('option_D_boundary_3', [[45.0, 30.0], [21.0, 30.0]]),
     ('option_D_boundary_4', [[21.0, 30.0], [21.0, 14.7]]),
     ('option_D_boundary_5', [[21.0, 9.3], [21.0, 6.0]]),
     ('option_D_boundary_6', [[34.5, 15.6], [38.1, 18.0]]),
     ('option_D_boundary_7', [[38.1, 18.0], [34.5, 20.4]]),
     ('option_D_boundary_8', [[34.5, 20.4], [34.5, 15.6]]),
     ('option_D_boundary_9', [[38.4, 22.8], [40.8, 22.8]]),
     ('option_D_boundary_10', [[40.8, 22.8], [40.8, 25.2]]),
     ('option_D_boundary_11', [[40.8, 25.2], [38.4, 25.2]]),
     ('option_D_boundary_12', [[38.4, 25.2], [38.4, 22.8]]),
     ('option_D_boundary_13', [[45.0, 9.3], [42.0, 12.0]]),
     ('option_D_boundary_14', [[42.0, 12.0], [45.0, 14.7]]),
     ('option_D_boundary_15', [[31.5, 15.6], [27.9, 18.0]]),
     ('option_D_boundary_16', [[27.9, 18.0], [31.5, 20.4]]),
     ('option_D_boundary_17', [[31.5, 20.4], [31.5, 15.6]]),
     ('option_D_boundary_18', [[27.6, 22.8], [25.2, 22.8]]),
     ('option_D_boundary_19', [[25.2, 22.8], [25.2, 25.2]]),
     ('option_D_boundary_20', [[25.2, 25.2], [27.6, 25.2]]),
     ('option_D_boundary_21', [[27.6, 25.2], [27.6, 22.8]]),
     ('option_D_boundary_22', [[21.0, 9.3], [24.0, 12.0]]),
     ('option_D_boundary_23', [[24.0, 12.0], [21.0, 14.7]])]
    _geometry_03 = [('option_E_boundary_0', [[55.0, 6.0], [79.0, 6.0]]),
     ('option_E_boundary_1', [[79.0, 6.0], [79.0, 9.3]]),
     ('option_E_boundary_2', [[79.0, 14.7], [79.0, 30.0]]),
     ('option_E_boundary_3', [[79.0, 30.0], [55.0, 30.0]]),
     ('option_E_boundary_4', [[55.0, 30.0], [55.0, 14.7]]),
     ('option_E_boundary_5', [[55.0, 9.3], [55.0, 6.0]]),
     ('option_E_boundary_6', [[67.0, 15.6], [70.6, 18.0]]),
     ('option_E_boundary_7', [[70.6, 18.0], [67.0, 20.4]]),
     ('option_E_boundary_8', [[72.4, 22.8], [74.8, 22.8]]),
     ('option_E_boundary_9', [[74.8, 22.8], [74.8, 25.2]]),
     ('option_E_boundary_10', [[74.8, 25.2], [72.4, 25.2]]),
     ('option_E_boundary_11', [[72.4, 25.2], [72.4, 22.8]]),
     ('option_E_boundary_12', [[76.0, 9.3], [79.0, 9.3]]),
     ('option_E_boundary_13', [[79.0, 14.7], [76.0, 14.7]]),
     ('option_E_boundary_14', [[76.0, 14.7], [76.0, 9.3]]),
     ('option_E_boundary_15', [[67.0, 15.6], [63.4, 18.0]]),
     ('option_E_boundary_16', [[63.4, 18.0], [67.0, 20.4]]),
     ('option_E_boundary_17', [[61.6, 22.8], [59.2, 22.8]]),
     ('option_E_boundary_18', [[59.2, 22.8], [59.2, 25.2]]),
     ('option_E_boundary_19', [[59.2, 25.2], [61.6, 25.2]]),
     ('option_E_boundary_20', [[61.6, 25.2], [61.6, 22.8]]),
     ('option_E_boundary_21', [[58.0, 9.3], [55.0, 9.3]]),
     ('option_E_boundary_22', [[55.0, 14.7], [58.0, 14.7]]),
     ('option_E_boundary_23', [[58.0, 14.7], [58.0, 9.3]])]
    with Canvas(PLANE, xlim=(1.6559000861326467, 98.49456287683032), ylim=(-0.6010443583117961, 96.23761843238587), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        for object_id, points in [('original_border_0', [[14, 74], [34, 74]]), ('original_border_1', [[34, 74], [34, 94]]), ('original_border_2', [[34, 94], [14, 94]]), ('original_border_3', [[14, 94], [14, 74]])]:
            c.line(points, id=object_id)
        c.line([[24.0, 74.0], [24.0, 94.0]], id='original_fold_0_0', linestyle=(0.0, [4.0, 3.0]))
        c.path([[70.0, 74.0], [80.0, 74.0], [80.0, 94.0], [70.0, 94.0], [70.0, 74.0]], [1, 2, 2, 2, 79], id='folded_paper_fill', zorder=1, edgecolor='none', facecolor=(1.0, 1.0, 1.0, 1.0), capstyle='butt')
        for object_id, vertices, codes in [('cut_1_fill', [[70.0, 82.0], [73.0, 84.0], [70.0, 86.0], [70.0, 82.0]], [1, 2, 2, 79]), ('cut_2_fill', [[74.5, 88.0], [76.5, 88.0], [76.5, 90.0], [74.5, 90.0], [74.5, 88.0]], [1, 2, 2, 2, 79]), ('cut_3_fill', [[80.0, 76.75], [77.5, 79.0], [80.0, 81.25], [80.0, 76.75]], [1, 2, 2, 79])]:
            c.path(vertices, codes, id=object_id, zorder=1, edgecolor='none', facecolor=(0.7529411764705882, 0.7529411764705882, 0.7529411764705882, 1.0), capstyle='butt')
        for object_id, points in [('folded_border_0', [[70, 74], [80, 74]]), ('folded_border_1', [[80, 74], [80, 94]]), ('folded_border_2', [[80, 94], [70, 94]])]:
            c.line(points, id=object_id, color='#2563EB')
        c.line([[70, 94], [70, 74]], id='folded_border_3', color='#2563EB', linestyle=(0.0, [4.0, 3.0]))
        for object_id, points in [('cut_1_path_0', [[70.0, 82.0], [73.0, 84.0]]), ('cut_1_path_1', [[73.0, 84.0], [70.0, 86.0]]), ('cut_2_path_0', [[74.5, 88.0], [76.5, 88.0]]), ('cut_2_path_1', [[76.5, 88.0], [76.5, 90.0]]), ('cut_2_path_2', [[76.5, 90.0], [74.5, 90.0]]), ('cut_2_path_3', [[74.5, 90.0], [74.5, 88.0]]), ('cut_3_path_0', [[80.0, 76.75], [77.5, 79.0]]), ('cut_3_path_1', [[77.5, 79.0], [80.0, 81.25]])]:
            c.line(points, id=object_id, color='#2563EB')
        for object_id, points in _geometry_01:
            c.line(points, id=object_id)
        c.line([[16.0, 38.0], [16.0, 47.6]], id='A_fold_0_0', linestyle=(0.0, [4.0, 3.0]))
        c.line([[16.0, 52.4], [16.0, 62.0]], id='A_fold_0_2', linestyle=(0.0, [4.0, 3.0]))
        for object_id, points in [('option_B_boundary_0', [[38.0, 38.0], [62.0, 38.0]]), ('option_B_boundary_1', [[62.0, 38.0], [62.0, 41.3]]), ('option_B_boundary_2', [[62.0, 46.7], [62.0, 62.0]]), ('option_B_boundary_3', [[62.0, 62.0], [38.0, 62.0]]), ('option_B_boundary_4', [[38.0, 62.0], [38.0, 46.7]]), ('option_B_boundary_5', [[38.0, 41.3], [38.0, 38.0]]), ('option_B_boundary_6', [[50.0, 47.6], [53.6, 50.0]]), ('option_B_boundary_7', [[53.6, 50.0], [50.0, 52.4]]), ('option_B_boundary_8', [[62.0, 41.3], [59.0, 44.0]]), ('option_B_boundary_9', [[59.0, 44.0], [62.0, 46.7]]), ('option_B_boundary_10', [[50.0, 47.6], [46.4, 50.0]]), ('option_B_boundary_11', [[46.4, 50.0], [50.0, 52.4]]), ('option_B_boundary_12', [[38.0, 41.3], [41.0, 44.0]]), ('option_B_boundary_13', [[41.0, 44.0], [38.0, 46.7]]), ('option_B_boundary_14', [[55.4, 54.8], [57.8, 54.8]]), ('option_B_boundary_15', [[57.8, 54.8], [57.8, 57.2]]), ('option_B_boundary_16', [[57.8, 57.2], [55.4, 57.2]]), ('option_B_boundary_17', [[55.4, 57.2], [55.4, 54.8]])]:
            c.line(points, id=object_id, color='#2563EB')
        c.line([[50.0, 38.0], [50.0, 47.6]], id='B_fold_0_0', linestyle=(0.0, [4.0, 3.0]))
        c.line([[50.0, 52.4], [50.0, 62.0]], id='B_fold_0_2', linestyle=(0.0, [4.0, 3.0]))
        for object_id, points in [('option_C_boundary_0', [[72.0, 38.0], [96.0, 38.0]]), ('option_C_boundary_1', [[96.0, 38.0], [96.0, 53.3]]), ('option_C_boundary_2', [[96.0, 58.7], [96.0, 62.0]]), ('option_C_boundary_3', [[96.0, 62.0], [72.0, 62.0]]), ('option_C_boundary_4', [[72.0, 62.0], [72.0, 58.7]]), ('option_C_boundary_5', [[72.0, 53.3], [72.0, 38.0]]), ('option_C_boundary_6', [[84.0, 47.6], [87.6, 50.0]]), ('option_C_boundary_7', [[87.6, 50.0], [84.0, 52.4]]), ('option_C_boundary_8', [[89.4, 54.8], [91.8, 54.8]]), ('option_C_boundary_9', [[91.8, 54.8], [91.8, 57.2]]), ('option_C_boundary_10', [[91.8, 57.2], [89.4, 57.2]]), ('option_C_boundary_11', [[89.4, 57.2], [89.4, 54.8]]), ('option_C_boundary_12', [[96.0, 58.7], [93.0, 56.0]]), ('option_C_boundary_13', [[93.0, 56.0], [96.0, 53.3]]), ('option_C_boundary_14', [[84.0, 47.6], [80.4, 50.0]]), ('option_C_boundary_15', [[80.4, 50.0], [84.0, 52.4]]), ('option_C_boundary_16', [[78.6, 54.8], [76.2, 54.8]]), ('option_C_boundary_17', [[76.2, 54.8], [76.2, 57.2]]), ('option_C_boundary_18', [[76.2, 57.2], [78.6, 57.2]]), ('option_C_boundary_19', [[78.6, 57.2], [78.6, 54.8]]), ('option_C_boundary_20', [[72.0, 58.7], [75.0, 56.0]]), ('option_C_boundary_21', [[75.0, 56.0], [72.0, 53.3]])]:
            c.line(points, id=object_id)
        c.line([[84.0, 38.0], [84.0, 47.6]], id='C_fold_0_0', linestyle=(0.0, [4.0, 3.0]))
        c.line([[84.0, 52.4], [84.0, 62.0]], id='C_fold_0_2', linestyle=(0.0, [4.0, 3.0]))
        for object_id, points in _geometry_02:
            c.line(points, id=object_id)
        c.line([[33.0, 6.0], [33.0, 30.0]], id='D_fold_0_0', linestyle=(0.0, [4.0, 3.0]))
        for object_id, points in _geometry_03:
            c.line(points, id=object_id)
        c.line([[67.0, 6.0], [67.0, 15.6]], id='E_fold_0_0', linestyle=(0.0, [4.0, 3.0]))
        c.line([[67.0, 20.4], [67.0, 30.0]], id='E_fold_0_2', linestyle=(0.0, [4.0, 3.0]))
        for object_id, text, anchor in [('option_label_A', '(A)', (16, 35)), ('option_label_B', '(B)', (50, 35)), ('option_label_C', '(C)', (84, 35)), ('option_label_D', '(D)', (33, 3)), ('option_label_E', '(E)', (67, 3))]:
            c.text(text, anchor, id=object_id, rotation_mode='default')
        return c.save(output_path)

def C02(output_path=None):
    if output_path is None:
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / 'Plane547_C02.png'
    _geometry_01 = [('cut_1_path_0', [[70.0, 82.0], [73.0, 84.0]]),
     ('cut_1_path_1', [[73.0, 84.0], [70.0, 86.0]]),
     ('cut_2_path_0', [[74.5, 88.0], [76.5, 88.0]]),
     ('cut_2_path_1', [[76.5, 88.0], [76.5, 90.0]]),
     ('cut_2_path_2', [[76.5, 90.0], [74.5, 90.0]]),
     ('cut_2_path_3', [[74.5, 90.0], [74.5, 88.0]]),
     ('cut_3_path_0', [[80.0, 76.75], [77.5, 79.0]]),
     ('cut_3_path_1', [[77.5, 79.0], [80.0, 81.25]]),
     ('fold_process_arrow', [[41, 84], [59, 84]]),
     ('fold_process_arrow_head_1', [[59.0, 84.0], [57.0, 85.1]]),
     ('fold_process_arrow_head_2', [[59.0, 84.0], [57.0, 82.9]]),
     ('option_A_boundary_0', [[4.0, 38.0], [28.0, 38.0]]),
     ('option_A_boundary_1', [[28.0, 38.0], [28.0, 41.3]]),
     ('option_A_boundary_2', [[28.0, 46.7], [28.0, 62.0]]),
     ('option_A_boundary_3', [[28.0, 62.0], [4.0, 62.0]]),
     ('option_A_boundary_4', [[4.0, 62.0], [4.0, 46.7]]),
     ('option_A_boundary_5', [[4.0, 41.3], [4.0, 38.0]]),
     ('option_A_boundary_6', [[16.0, 47.6], [19.6, 50.0]]),
     ('option_A_boundary_7', [[19.6, 50.0], [16.0, 52.4]]),
     ('option_A_boundary_8', [[21.4, 54.8], [23.8, 54.8]]),
     ('option_A_boundary_9', [[23.8, 54.8], [23.8, 57.2]]),
     ('option_A_boundary_10', [[23.8, 57.2], [21.4, 57.2]]),
     ('option_A_boundary_11', [[21.4, 57.2], [21.4, 54.8]]),
     ('option_A_boundary_12', [[28.0, 41.3], [25.0, 44.0]]),
     ('option_A_boundary_13', [[25.0, 44.0], [28.0, 46.7]]),
     ('option_A_boundary_14', [[16.0, 47.6], [12.4, 50.0]]),
     ('option_A_boundary_15', [[12.4, 50.0], [16.0, 52.4]]),
     ('option_A_boundary_16', [[10.6, 54.8], [8.2, 54.8]]),
     ('option_A_boundary_17', [[8.2, 54.8], [8.2, 57.2]]),
     ('option_A_boundary_18', [[8.2, 57.2], [10.6, 57.2]]),
     ('option_A_boundary_19', [[10.6, 57.2], [10.6, 54.8]]),
     ('option_A_boundary_20', [[4.0, 41.3], [7.0, 44.0]]),
     ('option_A_boundary_21', [[7.0, 44.0], [4.0, 46.7]])]
    _geometry_02 = [('option_D_boundary_0', [[21.0, 6.0], [45.0, 6.0]]),
     ('option_D_boundary_1', [[45.0, 6.0], [45.0, 9.3]]),
     ('option_D_boundary_2', [[45.0, 14.7], [45.0, 30.0]]),
     ('option_D_boundary_3', [[45.0, 30.0], [21.0, 30.0]]),
     ('option_D_boundary_4', [[21.0, 30.0], [21.0, 14.7]]),
     ('option_D_boundary_5', [[21.0, 9.3], [21.0, 6.0]]),
     ('option_D_boundary_6', [[34.5, 15.6], [38.1, 18.0]]),
     ('option_D_boundary_7', [[38.1, 18.0], [34.5, 20.4]]),
     ('option_D_boundary_8', [[34.5, 20.4], [34.5, 15.6]]),
     ('option_D_boundary_9', [[38.4, 22.8], [40.8, 22.8]]),
     ('option_D_boundary_10', [[40.8, 22.8], [40.8, 25.2]]),
     ('option_D_boundary_11', [[40.8, 25.2], [38.4, 25.2]]),
     ('option_D_boundary_12', [[38.4, 25.2], [38.4, 22.8]]),
     ('option_D_boundary_13', [[45.0, 9.3], [42.0, 12.0]]),
     ('option_D_boundary_14', [[42.0, 12.0], [45.0, 14.7]]),
     ('option_D_boundary_15', [[31.5, 15.6], [27.9, 18.0]]),
     ('option_D_boundary_16', [[27.9, 18.0], [31.5, 20.4]]),
     ('option_D_boundary_17', [[31.5, 20.4], [31.5, 15.6]]),
     ('option_D_boundary_18', [[27.6, 22.8], [25.2, 22.8]]),
     ('option_D_boundary_19', [[25.2, 22.8], [25.2, 25.2]]),
     ('option_D_boundary_20', [[25.2, 25.2], [27.6, 25.2]]),
     ('option_D_boundary_21', [[27.6, 25.2], [27.6, 22.8]]),
     ('option_D_boundary_22', [[21.0, 9.3], [24.0, 12.0]]),
     ('option_D_boundary_23', [[24.0, 12.0], [21.0, 14.7]])]
    _geometry_03 = [('option_E_boundary_0', [[55.0, 6.0], [79.0, 6.0]]),
     ('option_E_boundary_1', [[79.0, 6.0], [79.0, 9.3]]),
     ('option_E_boundary_2', [[79.0, 14.7], [79.0, 30.0]]),
     ('option_E_boundary_3', [[79.0, 30.0], [55.0, 30.0]]),
     ('option_E_boundary_4', [[55.0, 30.0], [55.0, 14.7]]),
     ('option_E_boundary_5', [[55.0, 9.3], [55.0, 6.0]]),
     ('option_E_boundary_6', [[67.0, 15.6], [70.6, 18.0]]),
     ('option_E_boundary_7', [[70.6, 18.0], [67.0, 20.4]]),
     ('option_E_boundary_8', [[72.4, 22.8], [74.8, 22.8]]),
     ('option_E_boundary_9', [[74.8, 22.8], [74.8, 25.2]]),
     ('option_E_boundary_10', [[74.8, 25.2], [72.4, 25.2]]),
     ('option_E_boundary_11', [[72.4, 25.2], [72.4, 22.8]]),
     ('option_E_boundary_12', [[76.0, 9.3], [79.0, 9.3]]),
     ('option_E_boundary_13', [[79.0, 14.7], [76.0, 14.7]]),
     ('option_E_boundary_14', [[76.0, 14.7], [76.0, 9.3]]),
     ('option_E_boundary_15', [[67.0, 15.6], [63.4, 18.0]]),
     ('option_E_boundary_16', [[63.4, 18.0], [67.0, 20.4]]),
     ('option_E_boundary_17', [[61.6, 22.8], [59.2, 22.8]]),
     ('option_E_boundary_18', [[59.2, 22.8], [59.2, 25.2]]),
     ('option_E_boundary_19', [[59.2, 25.2], [61.6, 25.2]]),
     ('option_E_boundary_20', [[61.6, 25.2], [61.6, 22.8]]),
     ('option_E_boundary_21', [[58.0, 9.3], [55.0, 9.3]]),
     ('option_E_boundary_22', [[55.0, 14.7], [58.0, 14.7]]),
     ('option_E_boundary_23', [[58.0, 14.7], [58.0, 9.3]])]
    with Canvas(PLANE, xlim=(1.6559000861326467, 98.49456287683032), ylim=(-0.6010443583117961, 96.23761843238587), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        for object_id, points in [('original_border_0', [[14, 74], [34, 74]]), ('original_border_1', [[34, 74], [34, 94]]), ('original_border_2', [[34, 94], [14, 94]]), ('original_border_3', [[14, 94], [14, 74]])]:
            c.line(points, id=object_id)
        c.line([[24.0, 74.0], [24.0, 94.0]], id='original_fold_0_0', linestyle=(0.0, [4.0, 3.0]))
        c.path([[70.0, 74.0], [80.0, 74.0], [80.0, 94.0], [70.0, 94.0], [70.0, 74.0]], [1, 2, 2, 2, 79], id='folded_paper_fill', zorder=1, edgecolor='none', facecolor=(1.0, 1.0, 1.0, 1.0), capstyle='butt')
        for object_id, vertices, codes in [('cut_1_fill', [[70.0, 82.0], [73.0, 84.0], [70.0, 86.0], [70.0, 82.0]], [1, 2, 2, 79]), ('cut_2_fill', [[74.5, 88.0], [76.5, 88.0], [76.5, 90.0], [74.5, 90.0], [74.5, 88.0]], [1, 2, 2, 2, 79]), ('cut_3_fill', [[80.0, 76.75], [77.5, 79.0], [80.0, 81.25], [80.0, 76.75]], [1, 2, 2, 79])]:
            c.path(vertices, codes, id=object_id, zorder=1, edgecolor='none', facecolor=(0.7529411764705882, 0.7529411764705882, 0.7529411764705882, 1.0), capstyle='butt')
        for object_id, points in [('folded_border_0', [[70, 74], [80, 74]]), ('folded_border_1', [[80, 74], [80, 94]]), ('folded_border_2', [[80, 94], [70, 94]])]:
            c.line(points, id=object_id)
        c.line([[70, 94], [70, 74]], id='folded_border_3', linestyle=(0.0, [4.0, 3.0]))
        for object_id, points in _geometry_01:
            c.line(points, id=object_id)
        c.line([[16.0, 38.0], [16.0, 47.6]], id='A_fold_0_0', linestyle=(0.0, [4.0, 3.0]))
        c.line([[16.0, 52.4], [16.0, 62.0]], id='A_fold_0_2', linestyle=(0.0, [4.0, 3.0]))
        for object_id, points in [('option_B_boundary_0', [[38.0, 38.0], [62.0, 38.0]]), ('option_B_boundary_1', [[62.0, 38.0], [62.0, 41.3]]), ('option_B_boundary_2', [[62.0, 46.7], [62.0, 62.0]]), ('option_B_boundary_3', [[62.0, 62.0], [38.0, 62.0]]), ('option_B_boundary_4', [[38.0, 62.0], [38.0, 46.7]]), ('option_B_boundary_5', [[38.0, 41.3], [38.0, 38.0]]), ('option_B_boundary_6', [[50.0, 47.6], [53.6, 50.0]]), ('option_B_boundary_7', [[53.6, 50.0], [50.0, 52.4]]), ('option_B_boundary_8', [[62.0, 41.3], [59.0, 44.0]]), ('option_B_boundary_9', [[59.0, 44.0], [62.0, 46.7]]), ('option_B_boundary_10', [[50.0, 47.6], [46.4, 50.0]]), ('option_B_boundary_11', [[46.4, 50.0], [50.0, 52.4]]), ('option_B_boundary_12', [[38.0, 41.3], [41.0, 44.0]]), ('option_B_boundary_13', [[41.0, 44.0], [38.0, 46.7]]), ('option_B_boundary_14', [[55.4, 54.8], [57.8, 54.8]]), ('option_B_boundary_15', [[57.8, 54.8], [57.8, 57.2]]), ('option_B_boundary_16', [[57.8, 57.2], [55.4, 57.2]]), ('option_B_boundary_17', [[55.4, 57.2], [55.4, 54.8]])]:
            c.line(points, id=object_id)
        c.line([[50.0, 38.0], [50.0, 47.6]], id='B_fold_0_0', linestyle=(0.0, [4.0, 3.0]))
        c.line([[50.0, 52.4], [50.0, 62.0]], id='B_fold_0_2', linestyle=(0.0, [4.0, 3.0]))
        for object_id, points in [('option_C_boundary_0', [[72.0, 38.0], [96.0, 38.0]]), ('option_C_boundary_1', [[96.0, 38.0], [96.0, 53.3]]), ('option_C_boundary_2', [[96.0, 58.7], [96.0, 62.0]]), ('option_C_boundary_3', [[96.0, 62.0], [72.0, 62.0]]), ('option_C_boundary_4', [[72.0, 62.0], [72.0, 58.7]]), ('option_C_boundary_5', [[72.0, 53.3], [72.0, 38.0]]), ('option_C_boundary_6', [[84.0, 47.6], [87.6, 50.0]]), ('option_C_boundary_7', [[87.6, 50.0], [84.0, 52.4]]), ('option_C_boundary_8', [[89.4, 54.8], [91.8, 54.8]]), ('option_C_boundary_9', [[91.8, 54.8], [91.8, 57.2]]), ('option_C_boundary_10', [[91.8, 57.2], [89.4, 57.2]]), ('option_C_boundary_11', [[89.4, 57.2], [89.4, 54.8]]), ('option_C_boundary_12', [[96.0, 58.7], [93.0, 56.0]]), ('option_C_boundary_13', [[93.0, 56.0], [96.0, 53.3]]), ('option_C_boundary_14', [[84.0, 47.6], [80.4, 50.0]]), ('option_C_boundary_15', [[80.4, 50.0], [84.0, 52.4]]), ('option_C_boundary_16', [[78.6, 54.8], [76.2, 54.8]]), ('option_C_boundary_17', [[76.2, 54.8], [76.2, 57.2]]), ('option_C_boundary_18', [[76.2, 57.2], [78.6, 57.2]]), ('option_C_boundary_19', [[78.6, 57.2], [78.6, 54.8]]), ('option_C_boundary_20', [[72.0, 58.7], [75.0, 56.0]]), ('option_C_boundary_21', [[75.0, 56.0], [72.0, 53.3]])]:
            c.line(points, id=object_id)
        c.line([[84.0, 38.0], [84.0, 47.6]], id='C_fold_0_0', linestyle=(0.0, [4.0, 3.0]))
        c.line([[84.0, 52.4], [84.0, 62.0]], id='C_fold_0_2', linestyle=(0.0, [4.0, 3.0]))
        for object_id, points in _geometry_02:
            c.line(points, id=object_id, color='#EA580C')
        c.line([[33.0, 6.0], [33.0, 30.0]], id='D_fold_0_0', linestyle=(0.0, [4.0, 3.0]))
        for object_id, points in _geometry_03:
            c.line(points, id=object_id)
        c.line([[67.0, 6.0], [67.0, 15.6]], id='E_fold_0_0', linestyle=(0.0, [4.0, 3.0]))
        c.line([[67.0, 20.4], [67.0, 30.0]], id='E_fold_0_2', linestyle=(0.0, [4.0, 3.0]))
        for object_id, text, anchor in [('option_label_A', '(A)', (16, 35)), ('option_label_B', '(B)', (50, 35)), ('option_label_C', '(C)', (84, 35)), ('option_label_D', '(D)', (33, 3)), ('option_label_E', '(E)', (67, 3))]:
            c.text(text, anchor, id=object_id, rotation_mode='default')
        return c.save(output_path)

def C03(output_path=None):
    if output_path is None:
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / 'Plane547_C03.png'
    _geometry_01 = [('cut_1_path_0', [[70.0, 82.0], [73.0, 84.0]]),
     ('cut_1_path_1', [[73.0, 84.0], [70.0, 86.0]]),
     ('cut_2_path_0', [[74.5, 88.0], [76.5, 88.0]]),
     ('cut_2_path_1', [[76.5, 88.0], [76.5, 90.0]]),
     ('cut_2_path_2', [[76.5, 90.0], [74.5, 90.0]]),
     ('cut_2_path_3', [[74.5, 90.0], [74.5, 88.0]]),
     ('cut_3_path_0', [[80.0, 76.75], [77.5, 79.0]]),
     ('cut_3_path_1', [[77.5, 79.0], [80.0, 81.25]]),
     ('fold_process_arrow', [[41, 84], [59, 84]]),
     ('fold_process_arrow_head_1', [[59.0, 84.0], [57.0, 85.1]]),
     ('fold_process_arrow_head_2', [[59.0, 84.0], [57.0, 82.9]]),
     ('option_A_boundary_0', [[4.0, 38.0], [28.0, 38.0]]),
     ('option_A_boundary_1', [[28.0, 38.0], [28.0, 41.3]]),
     ('option_A_boundary_2', [[28.0, 46.7], [28.0, 62.0]]),
     ('option_A_boundary_3', [[28.0, 62.0], [4.0, 62.0]]),
     ('option_A_boundary_4', [[4.0, 62.0], [4.0, 46.7]]),
     ('option_A_boundary_5', [[4.0, 41.3], [4.0, 38.0]]),
     ('option_A_boundary_6', [[16.0, 47.6], [19.6, 50.0]]),
     ('option_A_boundary_7', [[19.6, 50.0], [16.0, 52.4]]),
     ('option_A_boundary_8', [[21.4, 54.8], [23.8, 54.8]]),
     ('option_A_boundary_9', [[23.8, 54.8], [23.8, 57.2]]),
     ('option_A_boundary_10', [[23.8, 57.2], [21.4, 57.2]]),
     ('option_A_boundary_11', [[21.4, 57.2], [21.4, 54.8]]),
     ('option_A_boundary_12', [[28.0, 41.3], [25.0, 44.0]]),
     ('option_A_boundary_13', [[25.0, 44.0], [28.0, 46.7]]),
     ('option_A_boundary_14', [[16.0, 47.6], [12.4, 50.0]]),
     ('option_A_boundary_15', [[12.4, 50.0], [16.0, 52.4]]),
     ('option_A_boundary_16', [[10.6, 54.8], [8.2, 54.8]]),
     ('option_A_boundary_17', [[8.2, 54.8], [8.2, 57.2]]),
     ('option_A_boundary_18', [[8.2, 57.2], [10.6, 57.2]]),
     ('option_A_boundary_19', [[10.6, 57.2], [10.6, 54.8]]),
     ('option_A_boundary_20', [[4.0, 41.3], [7.0, 44.0]]),
     ('option_A_boundary_21', [[7.0, 44.0], [4.0, 46.7]])]
    _geometry_02 = [('option_D_boundary_0', [[21.0, 6.0], [45.0, 6.0]]),
     ('option_D_boundary_1', [[45.0, 6.0], [45.0, 9.3]]),
     ('option_D_boundary_2', [[45.0, 14.7], [45.0, 30.0]]),
     ('option_D_boundary_3', [[45.0, 30.0], [21.0, 30.0]]),
     ('option_D_boundary_4', [[21.0, 30.0], [21.0, 14.7]]),
     ('option_D_boundary_5', [[21.0, 9.3], [21.0, 6.0]]),
     ('option_D_boundary_6', [[34.5, 15.6], [38.1, 18.0]]),
     ('option_D_boundary_7', [[38.1, 18.0], [34.5, 20.4]]),
     ('option_D_boundary_8', [[34.5, 20.4], [34.5, 15.6]]),
     ('option_D_boundary_9', [[38.4, 22.8], [40.8, 22.8]]),
     ('option_D_boundary_10', [[40.8, 22.8], [40.8, 25.2]]),
     ('option_D_boundary_11', [[40.8, 25.2], [38.4, 25.2]]),
     ('option_D_boundary_12', [[38.4, 25.2], [38.4, 22.8]]),
     ('option_D_boundary_13', [[45.0, 9.3], [42.0, 12.0]]),
     ('option_D_boundary_14', [[42.0, 12.0], [45.0, 14.7]]),
     ('option_D_boundary_15', [[31.5, 15.6], [27.9, 18.0]]),
     ('option_D_boundary_16', [[27.9, 18.0], [31.5, 20.4]]),
     ('option_D_boundary_17', [[31.5, 20.4], [31.5, 15.6]]),
     ('option_D_boundary_18', [[27.6, 22.8], [25.2, 22.8]]),
     ('option_D_boundary_19', [[25.2, 22.8], [25.2, 25.2]]),
     ('option_D_boundary_20', [[25.2, 25.2], [27.6, 25.2]]),
     ('option_D_boundary_21', [[27.6, 25.2], [27.6, 22.8]]),
     ('option_D_boundary_22', [[21.0, 9.3], [24.0, 12.0]]),
     ('option_D_boundary_23', [[24.0, 12.0], [21.0, 14.7]])]
    _geometry_03 = [('option_E_boundary_0', [[55.0, 6.0], [79.0, 6.0]]),
     ('option_E_boundary_1', [[79.0, 6.0], [79.0, 9.3]]),
     ('option_E_boundary_2', [[79.0, 14.7], [79.0, 30.0]]),
     ('option_E_boundary_3', [[79.0, 30.0], [55.0, 30.0]]),
     ('option_E_boundary_4', [[55.0, 30.0], [55.0, 14.7]]),
     ('option_E_boundary_5', [[55.0, 9.3], [55.0, 6.0]]),
     ('option_E_boundary_6', [[67.0, 15.6], [70.6, 18.0]]),
     ('option_E_boundary_7', [[70.6, 18.0], [67.0, 20.4]]),
     ('option_E_boundary_8', [[72.4, 22.8], [74.8, 22.8]]),
     ('option_E_boundary_9', [[74.8, 22.8], [74.8, 25.2]]),
     ('option_E_boundary_10', [[74.8, 25.2], [72.4, 25.2]]),
     ('option_E_boundary_11', [[72.4, 25.2], [72.4, 22.8]]),
     ('option_E_boundary_12', [[76.0, 9.3], [79.0, 9.3]]),
     ('option_E_boundary_13', [[79.0, 14.7], [76.0, 14.7]]),
     ('option_E_boundary_14', [[76.0, 14.7], [76.0, 9.3]]),
     ('option_E_boundary_15', [[67.0, 15.6], [63.4, 18.0]]),
     ('option_E_boundary_16', [[63.4, 18.0], [67.0, 20.4]]),
     ('option_E_boundary_17', [[61.6, 22.8], [59.2, 22.8]]),
     ('option_E_boundary_18', [[59.2, 22.8], [59.2, 25.2]]),
     ('option_E_boundary_19', [[59.2, 25.2], [61.6, 25.2]]),
     ('option_E_boundary_20', [[61.6, 25.2], [61.6, 22.8]]),
     ('option_E_boundary_21', [[58.0, 9.3], [55.0, 9.3]]),
     ('option_E_boundary_22', [[55.0, 14.7], [58.0, 14.7]]),
     ('option_E_boundary_23', [[58.0, 14.7], [58.0, 9.3]])]
    with Canvas(PLANE, xlim=(1.6559000861326467, 98.49456287683032), ylim=(-0.6010443583117961, 96.23761843238587), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        for object_id, points in [('original_border_0', [[14, 74], [34, 74]]), ('original_border_1', [[34, 74], [34, 94]]), ('original_border_2', [[34, 94], [14, 94]]), ('original_border_3', [[14, 94], [14, 74]])]:
            c.line(points, id=object_id)
        c.line([[24.0, 74.0], [24.0, 94.0]], id='original_fold_0_0', linestyle=(0.0, [4.0, 3.0]))
        c.path([[70.0, 74.0], [80.0, 74.0], [80.0, 94.0], [70.0, 94.0], [70.0, 74.0]], [1, 2, 2, 2, 79], id='folded_paper_fill', zorder=1, edgecolor='none', facecolor=(1.0, 1.0, 1.0, 1.0), capstyle='butt')
        for object_id, vertices, codes in [('cut_1_fill', [[70.0, 82.0], [73.0, 84.0], [70.0, 86.0], [70.0, 82.0]], [1, 2, 2, 79]), ('cut_2_fill', [[74.5, 88.0], [76.5, 88.0], [76.5, 90.0], [74.5, 90.0], [74.5, 88.0]], [1, 2, 2, 2, 79]), ('cut_3_fill', [[80.0, 76.75], [77.5, 79.0], [80.0, 81.25], [80.0, 76.75]], [1, 2, 2, 79])]:
            c.path(vertices, codes, id=object_id, zorder=1, edgecolor='none', facecolor=(0.7529411764705882, 0.7529411764705882, 0.7529411764705882, 1.0), capstyle='butt')
        for object_id, points in [('folded_border_0', [[70, 74], [80, 74]]), ('folded_border_1', [[80, 74], [80, 94]]), ('folded_border_2', [[80, 94], [70, 94]])]:
            c.line(points, id=object_id)
        c.line([[70, 94], [70, 74]], id='folded_border_3', linestyle=(0.0, [4.0, 3.0]))
        for object_id, points in _geometry_01:
            c.line(points, id=object_id)
        c.line([[16.0, 38.0], [16.0, 47.6]], id='A_fold_0_0', linestyle=(0.0, [4.0, 3.0]))
        c.line([[16.0, 52.4], [16.0, 62.0]], id='A_fold_0_2', linestyle=(0.0, [4.0, 3.0]))
        for object_id, points in [('option_B_boundary_0', [[38.0, 38.0], [62.0, 38.0]]), ('option_B_boundary_1', [[62.0, 38.0], [62.0, 41.3]]), ('option_B_boundary_2', [[62.0, 46.7], [62.0, 62.0]]), ('option_B_boundary_3', [[62.0, 62.0], [38.0, 62.0]]), ('option_B_boundary_4', [[38.0, 62.0], [38.0, 46.7]]), ('option_B_boundary_5', [[38.0, 41.3], [38.0, 38.0]]), ('option_B_boundary_6', [[50.0, 47.6], [53.6, 50.0]]), ('option_B_boundary_7', [[53.6, 50.0], [50.0, 52.4]]), ('option_B_boundary_8', [[62.0, 41.3], [59.0, 44.0]]), ('option_B_boundary_9', [[59.0, 44.0], [62.0, 46.7]]), ('option_B_boundary_10', [[50.0, 47.6], [46.4, 50.0]]), ('option_B_boundary_11', [[46.4, 50.0], [50.0, 52.4]]), ('option_B_boundary_12', [[38.0, 41.3], [41.0, 44.0]]), ('option_B_boundary_13', [[41.0, 44.0], [38.0, 46.7]]), ('option_B_boundary_14', [[55.4, 54.8], [57.8, 54.8]]), ('option_B_boundary_15', [[57.8, 54.8], [57.8, 57.2]]), ('option_B_boundary_16', [[57.8, 57.2], [55.4, 57.2]]), ('option_B_boundary_17', [[55.4, 57.2], [55.4, 54.8]])]:
            c.line(points, id=object_id, color='#16A34A')
        c.line([[50.0, 38.0], [50.0, 47.6]], id='B_fold_0_0', linestyle=(0.0, [4.0, 3.0]))
        c.line([[50.0, 52.4], [50.0, 62.0]], id='B_fold_0_2', linestyle=(0.0, [4.0, 3.0]))
        for object_id, points in [('option_C_boundary_0', [[72.0, 38.0], [96.0, 38.0]]), ('option_C_boundary_1', [[96.0, 38.0], [96.0, 53.3]]), ('option_C_boundary_2', [[96.0, 58.7], [96.0, 62.0]]), ('option_C_boundary_3', [[96.0, 62.0], [72.0, 62.0]]), ('option_C_boundary_4', [[72.0, 62.0], [72.0, 58.7]]), ('option_C_boundary_5', [[72.0, 53.3], [72.0, 38.0]]), ('option_C_boundary_6', [[84.0, 47.6], [87.6, 50.0]]), ('option_C_boundary_7', [[87.6, 50.0], [84.0, 52.4]]), ('option_C_boundary_8', [[89.4, 54.8], [91.8, 54.8]]), ('option_C_boundary_9', [[91.8, 54.8], [91.8, 57.2]]), ('option_C_boundary_10', [[91.8, 57.2], [89.4, 57.2]]), ('option_C_boundary_11', [[89.4, 57.2], [89.4, 54.8]]), ('option_C_boundary_12', [[96.0, 58.7], [93.0, 56.0]]), ('option_C_boundary_13', [[93.0, 56.0], [96.0, 53.3]]), ('option_C_boundary_14', [[84.0, 47.6], [80.4, 50.0]]), ('option_C_boundary_15', [[80.4, 50.0], [84.0, 52.4]]), ('option_C_boundary_16', [[78.6, 54.8], [76.2, 54.8]]), ('option_C_boundary_17', [[76.2, 54.8], [76.2, 57.2]]), ('option_C_boundary_18', [[76.2, 57.2], [78.6, 57.2]]), ('option_C_boundary_19', [[78.6, 57.2], [78.6, 54.8]]), ('option_C_boundary_20', [[72.0, 58.7], [75.0, 56.0]]), ('option_C_boundary_21', [[75.0, 56.0], [72.0, 53.3]])]:
            c.line(points, id=object_id)
        c.line([[84.0, 38.0], [84.0, 47.6]], id='C_fold_0_0', linestyle=(0.0, [4.0, 3.0]))
        c.line([[84.0, 52.4], [84.0, 62.0]], id='C_fold_0_2', linestyle=(0.0, [4.0, 3.0]))
        for object_id, points in _geometry_02:
            c.line(points, id=object_id)
        c.line([[33.0, 6.0], [33.0, 30.0]], id='D_fold_0_0', linestyle=(0.0, [4.0, 3.0]))
        for object_id, points in _geometry_03:
            c.line(points, id=object_id)
        c.line([[67.0, 6.0], [67.0, 15.6]], id='E_fold_0_0', linestyle=(0.0, [4.0, 3.0]))
        c.line([[67.0, 20.4], [67.0, 30.0]], id='E_fold_0_2', linestyle=(0.0, [4.0, 3.0]))
        for object_id, text, anchor in [('option_label_A', '(A)', (16, 35)), ('option_label_B', '(B)', (50, 35)), ('option_label_C', '(C)', (84, 35)), ('option_label_D', '(D)', (33, 3)), ('option_label_E', '(E)', (67, 3))]:
            c.text(text, anchor, id=object_id, rotation_mode='default')
        return c.save(output_path)

def C04(output_path=None):
    if output_path is None:
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / 'Plane547_C04.png'
    _geometry_01 = [('fold_process_arrow', [[41, 84], [59, 84]]),
     ('fold_process_arrow_head_1', [[59.0, 84.0], [57.0, 85.1]]),
     ('fold_process_arrow_head_2', [[59.0, 84.0], [57.0, 82.9]]),
     ('option_A_boundary_0', [[4.0, 38.0], [28.0, 38.0]]),
     ('option_A_boundary_1', [[28.0, 38.0], [28.0, 41.3]]),
     ('option_A_boundary_2', [[28.0, 46.7], [28.0, 62.0]]),
     ('option_A_boundary_3', [[28.0, 62.0], [4.0, 62.0]]),
     ('option_A_boundary_4', [[4.0, 62.0], [4.0, 46.7]]),
     ('option_A_boundary_5', [[4.0, 41.3], [4.0, 38.0]]),
     ('option_A_boundary_6', [[16.0, 47.6], [19.6, 50.0]]),
     ('option_A_boundary_7', [[19.6, 50.0], [16.0, 52.4]]),
     ('option_A_boundary_8', [[21.4, 54.8], [23.8, 54.8]]),
     ('option_A_boundary_9', [[23.8, 54.8], [23.8, 57.2]]),
     ('option_A_boundary_10', [[23.8, 57.2], [21.4, 57.2]]),
     ('option_A_boundary_11', [[21.4, 57.2], [21.4, 54.8]]),
     ('option_A_boundary_12', [[28.0, 41.3], [25.0, 44.0]]),
     ('option_A_boundary_13', [[25.0, 44.0], [28.0, 46.7]]),
     ('option_A_boundary_14', [[16.0, 47.6], [12.4, 50.0]]),
     ('option_A_boundary_15', [[12.4, 50.0], [16.0, 52.4]]),
     ('option_A_boundary_16', [[10.6, 54.8], [8.2, 54.8]]),
     ('option_A_boundary_17', [[8.2, 54.8], [8.2, 57.2]]),
     ('option_A_boundary_18', [[8.2, 57.2], [10.6, 57.2]]),
     ('option_A_boundary_19', [[10.6, 57.2], [10.6, 54.8]]),
     ('option_A_boundary_20', [[4.0, 41.3], [7.0, 44.0]]),
     ('option_A_boundary_21', [[7.0, 44.0], [4.0, 46.7]])]
    _geometry_02 = [('option_D_boundary_0', [[21.0, 6.0], [45.0, 6.0]]),
     ('option_D_boundary_1', [[45.0, 6.0], [45.0, 9.3]]),
     ('option_D_boundary_2', [[45.0, 14.7], [45.0, 30.0]]),
     ('option_D_boundary_3', [[45.0, 30.0], [21.0, 30.0]]),
     ('option_D_boundary_4', [[21.0, 30.0], [21.0, 14.7]]),
     ('option_D_boundary_5', [[21.0, 9.3], [21.0, 6.0]]),
     ('option_D_boundary_6', [[34.5, 15.6], [38.1, 18.0]]),
     ('option_D_boundary_7', [[38.1, 18.0], [34.5, 20.4]]),
     ('option_D_boundary_8', [[34.5, 20.4], [34.5, 15.6]]),
     ('option_D_boundary_9', [[38.4, 22.8], [40.8, 22.8]]),
     ('option_D_boundary_10', [[40.8, 22.8], [40.8, 25.2]]),
     ('option_D_boundary_11', [[40.8, 25.2], [38.4, 25.2]]),
     ('option_D_boundary_12', [[38.4, 25.2], [38.4, 22.8]]),
     ('option_D_boundary_13', [[45.0, 9.3], [42.0, 12.0]]),
     ('option_D_boundary_14', [[42.0, 12.0], [45.0, 14.7]]),
     ('option_D_boundary_15', [[31.5, 15.6], [27.9, 18.0]]),
     ('option_D_boundary_16', [[27.9, 18.0], [31.5, 20.4]]),
     ('option_D_boundary_17', [[31.5, 20.4], [31.5, 15.6]]),
     ('option_D_boundary_18', [[27.6, 22.8], [25.2, 22.8]]),
     ('option_D_boundary_19', [[25.2, 22.8], [25.2, 25.2]]),
     ('option_D_boundary_20', [[25.2, 25.2], [27.6, 25.2]]),
     ('option_D_boundary_21', [[27.6, 25.2], [27.6, 22.8]]),
     ('option_D_boundary_22', [[21.0, 9.3], [24.0, 12.0]]),
     ('option_D_boundary_23', [[24.0, 12.0], [21.0, 14.7]])]
    _geometry_03 = [('option_E_boundary_0', [[55.0, 6.0], [79.0, 6.0]]),
     ('option_E_boundary_1', [[79.0, 6.0], [79.0, 9.3]]),
     ('option_E_boundary_2', [[79.0, 14.7], [79.0, 30.0]]),
     ('option_E_boundary_3', [[79.0, 30.0], [55.0, 30.0]]),
     ('option_E_boundary_4', [[55.0, 30.0], [55.0, 14.7]]),
     ('option_E_boundary_5', [[55.0, 9.3], [55.0, 6.0]]),
     ('option_E_boundary_6', [[67.0, 15.6], [70.6, 18.0]]),
     ('option_E_boundary_7', [[70.6, 18.0], [67.0, 20.4]]),
     ('option_E_boundary_8', [[72.4, 22.8], [74.8, 22.8]]),
     ('option_E_boundary_9', [[74.8, 22.8], [74.8, 25.2]]),
     ('option_E_boundary_10', [[74.8, 25.2], [72.4, 25.2]]),
     ('option_E_boundary_11', [[72.4, 25.2], [72.4, 22.8]]),
     ('option_E_boundary_12', [[76.0, 9.3], [79.0, 9.3]]),
     ('option_E_boundary_13', [[79.0, 14.7], [76.0, 14.7]]),
     ('option_E_boundary_14', [[76.0, 14.7], [76.0, 9.3]]),
     ('option_E_boundary_15', [[67.0, 15.6], [63.4, 18.0]]),
     ('option_E_boundary_16', [[63.4, 18.0], [67.0, 20.4]]),
     ('option_E_boundary_17', [[61.6, 22.8], [59.2, 22.8]]),
     ('option_E_boundary_18', [[59.2, 22.8], [59.2, 25.2]]),
     ('option_E_boundary_19', [[59.2, 25.2], [61.6, 25.2]]),
     ('option_E_boundary_20', [[61.6, 25.2], [61.6, 22.8]]),
     ('option_E_boundary_21', [[58.0, 9.3], [55.0, 9.3]]),
     ('option_E_boundary_22', [[55.0, 14.7], [58.0, 14.7]]),
     ('option_E_boundary_23', [[58.0, 14.7], [58.0, 9.3]])]
    with Canvas(PLANE, xlim=(1.6559000861326467, 98.49456287683032), ylim=(-0.6010443583117961, 96.23761843238587), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        for object_id, points in [('original_border_0', [[14, 74], [34, 74]]), ('original_border_1', [[34, 74], [34, 94]]), ('original_border_2', [[34, 94], [14, 94]]), ('original_border_3', [[14, 94], [14, 74]])]:
            c.line(points, id=object_id)
        c.line([[24.0, 74.0], [24.0, 94.0]], id='original_fold_0_0', linestyle=(0.0, [4.0, 3.0]))
        c.path([[70.0, 74.0], [80.0, 74.0], [80.0, 94.0], [70.0, 94.0], [70.0, 74.0]], [1, 2, 2, 2, 79], id='folded_paper_fill', zorder=1, edgecolor='none', facecolor=(1.0, 1.0, 1.0, 1.0), capstyle='butt')
        for object_id, vertices, codes in [('cut_1_fill', [[70.0, 82.0], [73.0, 84.0], [70.0, 86.0], [70.0, 82.0]], [1, 2, 2, 79]), ('cut_2_fill', [[74.5, 88.0], [76.5, 88.0], [76.5, 90.0], [74.5, 90.0], [74.5, 88.0]], [1, 2, 2, 2, 79]), ('cut_3_fill', [[80.0, 76.75], [77.5, 79.0], [80.0, 81.25], [80.0, 76.75]], [1, 2, 2, 79])]:
            c.path(vertices, codes, id=object_id, zorder=1, edgecolor='none', facecolor=(0.7529411764705882, 0.7529411764705882, 0.7529411764705882, 1.0), capstyle='butt')
        for object_id, points in [('folded_border_0', [[70, 74], [80, 74]]), ('folded_border_1', [[80, 74], [80, 94]]), ('folded_border_2', [[80, 94], [70, 94]])]:
            c.line(points, id=object_id)
        c.line([[70, 94], [70, 74]], id='folded_border_3', linestyle=(0.0, [4.0, 3.0]))
        for object_id, points in [('cut_1_path_0', [[70.0, 82.0], [73.0, 84.0]]), ('cut_1_path_1', [[73.0, 84.0], [70.0, 86.0]]), ('cut_2_path_0', [[74.5, 88.0], [76.5, 88.0]]), ('cut_2_path_1', [[76.5, 88.0], [76.5, 90.0]]), ('cut_2_path_2', [[76.5, 90.0], [74.5, 90.0]]), ('cut_2_path_3', [[74.5, 90.0], [74.5, 88.0]]), ('cut_3_path_0', [[80.0, 76.75], [77.5, 79.0]]), ('cut_3_path_1', [[77.5, 79.0], [80.0, 81.25]])]:
            c.line(points, id=object_id, color='#EA580C')
        for object_id, points in _geometry_01:
            c.line(points, id=object_id)
        c.line([[16.0, 38.0], [16.0, 47.6]], id='A_fold_0_0', linestyle=(0.0, [4.0, 3.0]))
        c.line([[16.0, 52.4], [16.0, 62.0]], id='A_fold_0_2', linestyle=(0.0, [4.0, 3.0]))
        for object_id, points in [('option_B_boundary_0', [[38.0, 38.0], [62.0, 38.0]]), ('option_B_boundary_1', [[62.0, 38.0], [62.0, 41.3]]), ('option_B_boundary_2', [[62.0, 46.7], [62.0, 62.0]]), ('option_B_boundary_3', [[62.0, 62.0], [38.0, 62.0]]), ('option_B_boundary_4', [[38.0, 62.0], [38.0, 46.7]]), ('option_B_boundary_5', [[38.0, 41.3], [38.0, 38.0]]), ('option_B_boundary_6', [[50.0, 47.6], [53.6, 50.0]]), ('option_B_boundary_7', [[53.6, 50.0], [50.0, 52.4]]), ('option_B_boundary_8', [[62.0, 41.3], [59.0, 44.0]]), ('option_B_boundary_9', [[59.0, 44.0], [62.0, 46.7]]), ('option_B_boundary_10', [[50.0, 47.6], [46.4, 50.0]]), ('option_B_boundary_11', [[46.4, 50.0], [50.0, 52.4]]), ('option_B_boundary_12', [[38.0, 41.3], [41.0, 44.0]]), ('option_B_boundary_13', [[41.0, 44.0], [38.0, 46.7]]), ('option_B_boundary_14', [[55.4, 54.8], [57.8, 54.8]]), ('option_B_boundary_15', [[57.8, 54.8], [57.8, 57.2]]), ('option_B_boundary_16', [[57.8, 57.2], [55.4, 57.2]]), ('option_B_boundary_17', [[55.4, 57.2], [55.4, 54.8]])]:
            c.line(points, id=object_id)
        c.line([[50.0, 38.0], [50.0, 47.6]], id='B_fold_0_0', linestyle=(0.0, [4.0, 3.0]))
        c.line([[50.0, 52.4], [50.0, 62.0]], id='B_fold_0_2', linestyle=(0.0, [4.0, 3.0]))
        for object_id, points in [('option_C_boundary_0', [[72.0, 38.0], [96.0, 38.0]]), ('option_C_boundary_1', [[96.0, 38.0], [96.0, 53.3]]), ('option_C_boundary_2', [[96.0, 58.7], [96.0, 62.0]]), ('option_C_boundary_3', [[96.0, 62.0], [72.0, 62.0]]), ('option_C_boundary_4', [[72.0, 62.0], [72.0, 58.7]]), ('option_C_boundary_5', [[72.0, 53.3], [72.0, 38.0]]), ('option_C_boundary_6', [[84.0, 47.6], [87.6, 50.0]]), ('option_C_boundary_7', [[87.6, 50.0], [84.0, 52.4]]), ('option_C_boundary_8', [[89.4, 54.8], [91.8, 54.8]]), ('option_C_boundary_9', [[91.8, 54.8], [91.8, 57.2]]), ('option_C_boundary_10', [[91.8, 57.2], [89.4, 57.2]]), ('option_C_boundary_11', [[89.4, 57.2], [89.4, 54.8]]), ('option_C_boundary_12', [[96.0, 58.7], [93.0, 56.0]]), ('option_C_boundary_13', [[93.0, 56.0], [96.0, 53.3]]), ('option_C_boundary_14', [[84.0, 47.6], [80.4, 50.0]]), ('option_C_boundary_15', [[80.4, 50.0], [84.0, 52.4]]), ('option_C_boundary_16', [[78.6, 54.8], [76.2, 54.8]]), ('option_C_boundary_17', [[76.2, 54.8], [76.2, 57.2]]), ('option_C_boundary_18', [[76.2, 57.2], [78.6, 57.2]]), ('option_C_boundary_19', [[78.6, 57.2], [78.6, 54.8]]), ('option_C_boundary_20', [[72.0, 58.7], [75.0, 56.0]]), ('option_C_boundary_21', [[75.0, 56.0], [72.0, 53.3]])]:
            c.line(points, id=object_id)
        c.line([[84.0, 38.0], [84.0, 47.6]], id='C_fold_0_0', linestyle=(0.0, [4.0, 3.0]))
        c.line([[84.0, 52.4], [84.0, 62.0]], id='C_fold_0_2', linestyle=(0.0, [4.0, 3.0]))
        for object_id, points in _geometry_02:
            c.line(points, id=object_id, color='#EA580C')
        c.line([[33.0, 6.0], [33.0, 30.0]], id='D_fold_0_0', linestyle=(0.0, [4.0, 3.0]))
        for object_id, points in _geometry_03:
            c.line(points, id=object_id)
        c.line([[67.0, 6.0], [67.0, 15.6]], id='E_fold_0_0', linestyle=(0.0, [4.0, 3.0]))
        c.line([[67.0, 20.4], [67.0, 30.0]], id='E_fold_0_2', linestyle=(0.0, [4.0, 3.0]))
        for object_id, text, anchor in [('option_label_A', '(A)', (16, 35)), ('option_label_B', '(B)', (50, 35)), ('option_label_C', '(C)', (84, 35)), ('option_label_D', '(D)', (33, 3)), ('option_label_E', '(E)', (67, 3))]:
            c.text(text, anchor, id=object_id, rotation_mode='default')
        return c.save(output_path)
