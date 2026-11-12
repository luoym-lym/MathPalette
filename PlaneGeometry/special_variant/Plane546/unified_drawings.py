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
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / 'Plane546_C01.png'
    with Canvas(PLANE, xlim=(1.6559000861326467, 98.49456287683032), ylim=(-0.6010443583117961, 96.23761843238587), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        for object_id, points in [('original_border_0', [[14, 74], [34, 74]]), ('original_border_1', [[34, 74], [34, 94]]), ('original_border_2', [[34, 94], [14, 94]]), ('original_border_3', [[14, 94], [14, 74]])]:
            c.line(points, id=object_id)
        c.line([[24.0, 74.0], [24.0, 94.0]], id='original_fold_0_0', linestyle=(0.0, [4.0, 3.0]))
        c.path([[70.0, 74.0], [80.0, 74.0], [80.0, 94.0], [70.0, 94.0], [70.0, 74.0]], [1, 2, 2, 2, 79], id='folded_paper_fill', zorder=1, edgecolor='none', facecolor=(1.0, 1.0, 1.0, 1.0), capstyle='butt')
        c.path([[70.0, 86.75], [73.5, 89.25], [70.0, 91.75], [70.0, 86.75]], [1, 2, 2, 79], id='cut_1_fill', zorder=1, edgecolor='none', facecolor=(0.7529411764705882, 0.7529411764705882, 0.7529411764705882, 1.0), capstyle='butt')
        c.path([[70.0, 77.25], [72.5, 77.25], [72.5, 80.25], [70.0, 80.25], [70.0, 77.25]], [1, 2, 2, 2, 79], id='cut_2_fill', zorder=1, edgecolor='none', facecolor=(0.7529411764705882, 0.7529411764705882, 0.7529411764705882, 1.0), capstyle='butt')
        for object_id, points in [('folded_border_0', [[70, 74], [80, 74]]), ('folded_border_1', [[80, 74], [80, 94]]), ('folded_border_2', [[80, 94], [70, 94]])]:
            c.line(points, id=object_id)
        c.line([[70, 94], [70, 74]], id='folded_border_3', linestyle=(0.0, [4.0, 3.0]))
        for object_id, points in [('cut_1_path_0', [[70.0, 86.75], [73.5, 89.25]]), ('cut_1_path_1', [[73.5, 89.25], [70.0, 91.75]]), ('cut_2_path_0', [[70.0, 77.25], [72.5, 77.25]]), ('cut_2_path_1', [[72.5, 77.25], [72.5, 80.25]]), ('cut_2_path_2', [[72.5, 80.25], [70.0, 80.25]]), ('fold_process_arrow', [[41, 84], [59, 84]]), ('fold_process_arrow_head_1', [[59.0, 84.0], [57.0, 85.1]]), ('fold_process_arrow_head_2', [[59.0, 84.0], [57.0, 82.9]]), ('option_A_boundary_0', [[4.0, 38.0], [28.0, 38.0]]), ('option_A_boundary_1', [[28.0, 38.0], [28.0, 62.0]]), ('option_A_boundary_2', [[28.0, 62.0], [4.0, 62.0]]), ('option_A_boundary_3', [[4.0, 62.0], [4.0, 38.0]]), ('option_A_boundary_4', [[16.0, 53.3], [20.2, 56.3]]), ('option_A_boundary_5', [[20.2, 56.3], [16.0, 59.3]]), ('option_A_boundary_6', [[16.0, 41.9], [19.0, 43.7]]), ('option_A_boundary_7', [[19.0, 43.7], [16.0, 45.5]]), ('option_A_boundary_8', [[16.0, 53.3], [11.8, 56.3]]), ('option_A_boundary_9', [[11.8, 56.3], [16.0, 59.3]]), ('option_A_boundary_10', [[16.0, 41.9], [13.0, 43.7]]), ('option_A_boundary_11', [[13.0, 43.7], [16.0, 45.5]])]:
            c.line(points, id=object_id)
        for object_id, points in [('A_fold_0_0', [[16.0, 38.0], [16.0, 41.9]]), ('A_fold_0_2', [[16.0, 45.5], [16.0, 53.3]]), ('A_fold_0_4', [[16.0, 59.3], [16.0, 62.0]])]:
            c.line(points, id=object_id, linestyle=(0.0, [4.0, 3.0]))
        for object_id, points in [('option_B_boundary_0', [[38.0, 38.0], [62.0, 38.0]]), ('option_B_boundary_1', [[62.0, 38.0], [62.0, 62.0]]), ('option_B_boundary_2', [[62.0, 62.0], [38.0, 62.0]]), ('option_B_boundary_3', [[38.0, 62.0], [38.0, 38.0]]), ('option_B_boundary_4', [[50.0, 54.5], [53.0, 54.5]]), ('option_B_boundary_5', [[53.0, 54.5], [53.0, 58.1]]), ('option_B_boundary_6', [[53.0, 58.1], [50.0, 58.1]]), ('option_B_boundary_7', [[50.0, 40.7], [54.2, 43.7]]), ('option_B_boundary_8', [[54.2, 43.7], [50.0, 46.7]]), ('option_B_boundary_9', [[50.0, 54.5], [47.0, 54.5]]), ('option_B_boundary_10', [[47.0, 54.5], [47.0, 58.1]]), ('option_B_boundary_11', [[47.0, 58.1], [50.0, 58.1]]), ('option_B_boundary_12', [[50.0, 40.7], [45.8, 43.7]]), ('option_B_boundary_13', [[45.8, 43.7], [50.0, 46.7]])]:
            c.line(points, id=object_id)
        for object_id, points in [('B_fold_0_0', [[50.0, 38.0], [50.0, 40.7]]), ('B_fold_0_2', [[50.0, 46.7], [50.0, 54.5]]), ('B_fold_0_4', [[50.0, 58.1], [50.0, 62.0]])]:
            c.line(points, id=object_id, linestyle=(0.0, [4.0, 3.0]))
        for object_id, points in [('option_C_boundary_0', [[72.0, 38.0], [96.0, 38.0]]), ('option_C_boundary_1', [[96.0, 38.0], [96.0, 62.0]]), ('option_C_boundary_2', [[96.0, 62.0], [72.0, 62.0]]), ('option_C_boundary_3', [[72.0, 62.0], [72.0, 38.0]]), ('option_C_boundary_4', [[85.8, 53.3], [90.0, 56.3]]), ('option_C_boundary_5', [[90.0, 56.3], [85.8, 59.3]]), ('option_C_boundary_6', [[85.8, 59.3], [85.8, 53.3]]), ('option_C_boundary_7', [[85.8, 41.9], [88.8, 41.9]]), ('option_C_boundary_8', [[88.8, 41.9], [88.8, 45.5]]), ('option_C_boundary_9', [[88.8, 45.5], [85.8, 45.5]]), ('option_C_boundary_10', [[85.8, 45.5], [85.8, 41.9]]), ('option_C_boundary_11', [[82.2, 53.3], [78.0, 56.3]]), ('option_C_boundary_12', [[78.0, 56.3], [82.2, 59.3]]), ('option_C_boundary_13', [[82.2, 59.3], [82.2, 53.3]]), ('option_C_boundary_14', [[82.2, 41.9], [79.2, 41.9]]), ('option_C_boundary_15', [[79.2, 41.9], [79.2, 45.5]]), ('option_C_boundary_16', [[79.2, 45.5], [82.2, 45.5]]), ('option_C_boundary_17', [[82.2, 45.5], [82.2, 41.9]])]:
            c.line(points, id=object_id, color='#2563EB')
        c.line([[84.0, 38.0], [84.0, 62.0]], id='C_fold_0_0', color='#2563EB', linestyle=(0.0, [4.0, 3.0]))
        for object_id, points in [('option_D_boundary_0', [[21.0, 6.0], [45.0, 6.0]]), ('option_D_boundary_1', [[45.0, 6.0], [45.0, 30.0]]), ('option_D_boundary_2', [[45.0, 30.0], [21.0, 30.0]]), ('option_D_boundary_3', [[21.0, 30.0], [21.0, 6.0]]), ('option_D_boundary_4', [[33.0, 21.3], [37.2, 24.3]]), ('option_D_boundary_5', [[37.2, 24.3], [33.0, 27.3]]), ('option_D_boundary_6', [[33.0, 9.9], [36.0, 9.9]]), ('option_D_boundary_7', [[36.0, 9.9], [36.0, 13.5]]), ('option_D_boundary_8', [[36.0, 13.5], [33.0, 13.5]]), ('option_D_boundary_9', [[33.0, 21.3], [28.8, 24.3]]), ('option_D_boundary_10', [[28.8, 24.3], [33.0, 27.3]]), ('option_D_boundary_11', [[33.0, 9.9], [30.0, 9.9]]), ('option_D_boundary_12', [[30.0, 9.9], [30.0, 13.5]]), ('option_D_boundary_13', [[30.0, 13.5], [33.0, 13.5]])]:
            c.line(points, id=object_id)
        for object_id, points in [('D_fold_0_0', [[33.0, 6.0], [33.0, 9.9]]), ('D_fold_0_2', [[33.0, 13.5], [33.0, 21.3]]), ('D_fold_0_4', [[33.0, 27.3], [33.0, 30.0]])]:
            c.line(points, id=object_id, linestyle=(0.0, [4.0, 3.0]))
        for object_id, points in [('option_E_boundary_0', [[55.0, 6.0], [79.0, 6.0]]), ('option_E_boundary_1', [[79.0, 6.0], [79.0, 30.0]]), ('option_E_boundary_2', [[79.0, 30.0], [55.0, 30.0]]), ('option_E_boundary_3', [[55.0, 30.0], [55.0, 6.0]]), ('option_E_boundary_4', [[67.0, 21.3], [71.2, 24.3]]), ('option_E_boundary_5', [[71.2, 24.3], [67.0, 27.3]]), ('option_E_boundary_6', [[67.0, 27.3], [67.0, 21.3]]), ('option_E_boundary_7', [[67.0, 9.9], [70.0, 9.9]]), ('option_E_boundary_8', [[70.0, 9.9], [70.0, 13.5]]), ('option_E_boundary_9', [[70.0, 13.5], [67.0, 13.5]]), ('option_E_boundary_10', [[67.0, 13.5], [67.0, 9.9]])]:
            c.line(points, id=object_id)
        for object_id, points in [('E_fold_0_0', [[67.0, 6.0], [67.0, 9.9]]), ('E_fold_0_2', [[67.0, 13.5], [67.0, 21.3]]), ('E_fold_0_4', [[67.0, 27.3], [67.0, 30.0]])]:
            c.line(points, id=object_id, linestyle=(0.0, [4.0, 3.0]))
        for object_id, text, anchor in [('option_label_A', '(A)', (16, 35)), ('option_label_B', '(B)', (50, 35)), ('option_label_C', '(C)', (84, 35)), ('option_label_D', '(D)', (33, 3)), ('option_label_E', '(E)', (67, 3))]:
            c.text(text, anchor, id=object_id, rotation_mode='default')
        return c.save(output_path)
