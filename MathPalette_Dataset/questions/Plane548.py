"""Collected question Plane548; construction on the shared drawing protocol."""
from pathlib import Path
import sys
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from MathPalette_Dataset.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane548:
    variants = ('C01', 'C02', 'C03', 'C04', 'C05', 'C06')

    def __init__(self):
        self.id = 'Plane548'
        self.source_dataset = 'Author Designed'
        self.source_key = 'author-extensions95-v1:Plane220/extension_04'
        self.question = 'A piece of paper is folded exactly in half twice, and a figure is cut out as shown.\nWhich of the five pictures can result when the paper is unfolded?\nChoices:\nA:A\nB:B\nC:C\nD:D\nE:E'
        self.answer = 'E'
        self.answer_type = 'choice'
        self.choices = {'A': 'A', 'B': 'B', 'C': 'C', 'D': 'D', 'E': 'E'}
        self.query = self.question
        self._geometry_01 = [('cut_1_path_1', [[72.75, 79.0], [70.0, 81.75]]),
         ('cut_2_path_0', [[70.0, 83.75], [71.75, 83.75]]),
         ('cut_2_path_1', [[71.75, 83.75], [71.75, 85.75]]),
         ('cut_2_path_2', [[71.75, 85.75], [70.0, 85.75]]),
         ('cut_3_path_1', [[78.0, 89.0], [80.0, 87.0]]),
         ('fold_process_arrow', [[41, 84], [59, 84]]),
         ('fold_process_arrow_head_1', [[59.0, 84.0], [57.0, 85.1]]),
         ('fold_process_arrow_head_2', [[59.0, 84.0], [57.0, 82.9]]),
         ('option_A_boundary_0', [[4.0, 38.0], [28.0, 38.0]]),
         ('option_A_boundary_1', [[28.0, 38.0], [28.0, 59.6]]),
         ('option_A_boundary_2', [[25.6, 62.0], [6.4, 62.0]]),
         ('option_A_boundary_3', [[4.0, 59.6], [4.0, 38.0]]),
         ('option_A_boundary_4', [[16.0, 50.0], [19.3, 50.0]]),
         ('option_A_boundary_5', [[19.3, 50.0], [16.0, 53.3]]),
         ('option_A_boundary_6', [[16.0, 55.7], [18.1, 55.7]]),
         ('option_A_boundary_7', [[18.1, 55.7], [18.1, 58.1]]),
         ('option_A_boundary_8', [[18.1, 58.1], [16.0, 58.1]]),
         ('option_A_boundary_9', [[25.6, 62.0], [28.0, 59.6]]),
         ('option_A_boundary_10', [[16.0, 50.0], [12.7, 50.0]]),
         ('option_A_boundary_11', [[12.7, 50.0], [16.0, 53.3]]),
         ('option_A_boundary_12', [[16.0, 55.7], [13.9, 55.7]]),
         ('option_A_boundary_13', [[13.9, 55.7], [13.9, 58.1]]),
         ('option_A_boundary_14', [[13.9, 58.1], [16.0, 58.1]]),
         ('option_A_boundary_15', [[6.4, 62.0], [4.0, 59.6]])]
        self._geometry_02 = [('option_B_boundary_0', [[40.4, 38.0], [59.6, 38.0]]),
         ('option_B_boundary_1', [[62.0, 40.4], [62.0, 59.6]]),
         ('option_B_boundary_2', [[59.6, 62.0], [40.4, 62.0]]),
         ('option_B_boundary_3', [[38.0, 59.6], [38.0, 40.4]]),
         ('option_B_boundary_4', [[53.3, 50.0], [53.3, 53.3]]),
         ('option_B_boundary_5', [[53.3, 53.3], [50.0, 53.3]]),
         ('option_B_boundary_6', [[50.0, 55.7], [52.1, 55.7]]),
         ('option_B_boundary_7', [[52.1, 55.7], [52.1, 58.1]]),
         ('option_B_boundary_8', [[52.1, 58.1], [50.0, 58.1]]),
         ('option_B_boundary_9', [[59.6, 62.0], [62.0, 59.6]]),
         ('option_B_boundary_10', [[53.3, 50.0], [53.3, 46.7]]),
         ('option_B_boundary_11', [[53.3, 46.7], [50.0, 46.7]]),
         ('option_B_boundary_12', [[50.0, 44.3], [52.1, 44.3]]),
         ('option_B_boundary_13', [[52.1, 44.3], [52.1, 41.9]]),
         ('option_B_boundary_14', [[52.1, 41.9], [50.0, 41.9]]),
         ('option_B_boundary_15', [[59.6, 38.0], [62.0, 40.4]]),
         ('option_B_boundary_16', [[46.7, 50.0], [46.7, 53.3]]),
         ('option_B_boundary_17', [[46.7, 53.3], [50.0, 53.3]]),
         ('option_B_boundary_18', [[50.0, 55.7], [47.9, 55.7]]),
         ('option_B_boundary_19', [[47.9, 55.7], [47.9, 58.1]]),
         ('option_B_boundary_20', [[47.9, 58.1], [50.0, 58.1]]),
         ('option_B_boundary_21', [[40.4, 62.0], [38.0, 59.6]]),
         ('option_B_boundary_22', [[46.7, 50.0], [46.7, 46.7]]),
         ('option_B_boundary_23', [[46.7, 46.7], [50.0, 46.7]]),
         ('option_B_boundary_24', [[50.0, 44.3], [47.9, 44.3]]),
         ('option_B_boundary_25', [[47.9, 44.3], [47.9, 41.9]]),
         ('option_B_boundary_26', [[47.9, 41.9], [50.0, 41.9]]),
         ('option_B_boundary_27', [[40.4, 38.0], [38.0, 40.4]])]
        self._geometry_03 = [('option_C_boundary_0', [[74.4, 38.0], [93.6, 38.0]]),
         ('option_C_boundary_1', [[96.0, 40.4], [96.0, 59.6]]),
         ('option_C_boundary_2', [[93.6, 62.0], [74.4, 62.0]]),
         ('option_C_boundary_3', [[72.0, 59.6], [72.0, 40.4]]),
         ('option_C_boundary_4', [[87.3, 50.0], [84.0, 53.3]]),
         ('option_C_boundary_5', [[85.5, 55.7], [87.6, 55.7]]),
         ('option_C_boundary_6', [[87.6, 55.7], [87.6, 58.1]]),
         ('option_C_boundary_7', [[87.6, 58.1], [85.5, 58.1]]),
         ('option_C_boundary_8', [[85.5, 58.1], [85.5, 55.7]]),
         ('option_C_boundary_9', [[93.6, 62.0], [96.0, 59.6]]),
         ('option_C_boundary_10', [[87.3, 50.0], [84.0, 46.7]]),
         ('option_C_boundary_11', [[85.5, 44.3], [87.6, 44.3]]),
         ('option_C_boundary_12', [[87.6, 44.3], [87.6, 41.9]]),
         ('option_C_boundary_13', [[87.6, 41.9], [85.5, 41.9]]),
         ('option_C_boundary_14', [[85.5, 41.9], [85.5, 44.3]]),
         ('option_C_boundary_15', [[93.6, 38.0], [96.0, 40.4]]),
         ('option_C_boundary_16', [[80.7, 50.0], [84.0, 53.3]]),
         ('option_C_boundary_17', [[82.5, 55.7], [80.4, 55.7]]),
         ('option_C_boundary_18', [[80.4, 55.7], [80.4, 58.1]]),
         ('option_C_boundary_19', [[80.4, 58.1], [82.5, 58.1]]),
         ('option_C_boundary_20', [[82.5, 58.1], [82.5, 55.7]]),
         ('option_C_boundary_21', [[74.4, 62.0], [72.0, 59.6]]),
         ('option_C_boundary_22', [[80.7, 50.0], [84.0, 46.7]]),
         ('option_C_boundary_23', [[82.5, 44.3], [80.4, 44.3]]),
         ('option_C_boundary_24', [[80.4, 44.3], [80.4, 41.9]]),
         ('option_C_boundary_25', [[80.4, 41.9], [82.5, 41.9]]),
         ('option_C_boundary_26', [[82.5, 41.9], [82.5, 44.3]]),
         ('option_C_boundary_27', [[74.4, 38.0], [72.0, 40.4]])]
        self._geometry_04 = [('option_E_boundary_0', [[57.4, 6.0], [76.6, 6.0]]),
         ('option_E_boundary_1', [[79.0, 8.4], [79.0, 27.6]]),
         ('option_E_boundary_2', [[76.6, 30.0], [57.4, 30.0]]),
         ('option_E_boundary_3', [[55.0, 27.6], [55.0, 8.4]]),
         ('option_E_boundary_4', [[70.3, 18.0], [67.0, 21.3]]),
         ('option_E_boundary_5', [[67.0, 23.7], [69.1, 23.7]]),
         ('option_E_boundary_6', [[69.1, 23.7], [69.1, 26.1]]),
         ('option_E_boundary_7', [[69.1, 26.1], [67.0, 26.1]]),
         ('option_E_boundary_8', [[76.6, 30.0], [79.0, 27.6]]),
         ('option_E_boundary_9', [[70.3, 18.0], [67.0, 14.7]]),
         ('option_E_boundary_10', [[67.0, 12.3], [69.1, 12.3]]),
         ('option_E_boundary_11', [[69.1, 12.3], [69.1, 9.9]]),
         ('option_E_boundary_12', [[69.1, 9.9], [67.0, 9.9]]),
         ('option_E_boundary_13', [[76.6, 6.0], [79.0, 8.4]]),
         ('option_E_boundary_14', [[63.7, 18.0], [67.0, 21.3]]),
         ('option_E_boundary_15', [[67.0, 23.7], [64.9, 23.7]]),
         ('option_E_boundary_16', [[64.9, 23.7], [64.9, 26.1]]),
         ('option_E_boundary_17', [[64.9, 26.1], [67.0, 26.1]]),
         ('option_E_boundary_18', [[57.4, 30.0], [55.0, 27.6]]),
         ('option_E_boundary_19', [[63.7, 18.0], [67.0, 14.7]]),
         ('option_E_boundary_20', [[67.0, 12.3], [64.9, 12.3]]),
         ('option_E_boundary_21', [[64.9, 12.3], [64.9, 9.9]]),
         ('option_E_boundary_22', [[64.9, 9.9], [67.0, 9.9]]),
         ('option_E_boundary_23', [[57.4, 6.0], [55.0, 8.4]])]

    def draw(self, output_path=None, *, variant=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if variant not in self.variants:
                raise ValueError('Unknown Special variant: ' + str(variant))
            return getattr(self, 'draw_' + variant)(output_path)
        with Canvas(PLANE, xlim=[1.6559000861326467, 98.49456287683032], ylim=[-0.6010443583117961, 96.23761843238587], axes_position=[0.05, 0.05, 0.9, 0.9], coordinate_axes=False) as c:
            for object_id, points in [('original_border_0', [[14, 74], [34, 74]]), ('original_border_1', [[34, 74], [34, 94]]), ('original_border_2', [[34, 94], [14, 94]]), ('original_border_3', [[14, 94], [14, 74]])]:
                c.line(points, id=object_id)
            c.line([[24.0, 74.0], [24.0, 94.0]], id='original_fold_0_0', linestyle=(0.0, [4.0, 3.0]))
            c.line([[14.0, 84.0], [34.0, 84.0]], id='original_fold_1_0', linestyle=(0.0, [4.0, 3.0]))
            c.path([[70.0, 79.0], [80.0, 79.0], [80.0, 89.0], [70.0, 89.0], [70.0, 79.0]], [1, 2, 2, 2, 79], id='folded_paper_fill', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], capstyle='butt')
            for object_id, vertices, codes in [('cut_1_fill', [[70.0, 79.0], [72.75, 79.0], [70.0, 81.75], [70.0, 79.0]], [1, 2, 2, 79]), ('cut_2_fill', [[70.0, 83.75], [71.75, 83.75], [71.75, 85.75], [70.0, 85.75], [70.0, 83.75]], [1, 2, 2, 2, 79]), ('cut_3_fill', [[80.0, 89.0], [78.0, 89.0], [80.0, 87.0], [80.0, 89.0]], [1, 2, 2, 79])]:
                c.path(vertices, codes, id=object_id, zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.7529411764705882, 0.7529411764705882, 0.7529411764705882, 1.0], capstyle='butt')
            c.line([[70, 79], [80, 79]], id='folded_border_0', linestyle=(0.0, [4.0, 3.0]))
            c.line([[80, 79], [80, 89]], id='folded_border_1')
            c.line([[80, 89], [70, 89]], id='folded_border_2')
            c.line([[70, 89], [70, 79]], id='folded_border_3', linestyle=(0.0, [4.0, 3.0]))
            for object_id, points in self._geometry_01:
                c.line(points, id=object_id)
            for object_id, points in [('A_fold_0_0', [[16.0, 38.0], [16.0, 50.0]]), ('A_fold_0_2', [[16.0, 53.3], [16.0, 55.7]]), ('A_fold_0_4', [[16.0, 58.1], [16.0, 62.0]]), ('A_fold_1_0', [[4.0, 50.0], [12.7, 50.0]]), ('A_fold_1_3', [[19.3, 50.0], [28.0, 50.0]])]:
                c.line(points, id=object_id, linestyle=(0.0, [4.0, 3.0]))
            for object_id, points in self._geometry_02:
                c.line(points, id=object_id)
            for object_id, points in [('B_fold_0_0', [[50.0, 38.0], [50.0, 41.9]]), ('B_fold_0_2', [[50.0, 44.3], [50.0, 46.7]]), ('B_fold_0_5', [[50.0, 53.3], [50.0, 55.7]]), ('B_fold_0_7', [[50.0, 58.1], [50.0, 62.0]]), ('B_fold_1_0', [[38.0, 50.0], [46.7, 50.0]]), ('B_fold_1_3', [[53.3, 50.0], [62.0, 50.0]])]:
                c.line(points, id=object_id, linestyle=(0.0, [4.0, 3.0]))
            for object_id, points in self._geometry_03:
                c.line(points, id=object_id)
            for object_id, points in [('C_fold_0_0', [[84.0, 38.0], [84.0, 46.7]]), ('C_fold_0_3', [[84.0, 53.3], [84.0, 62.0]]), ('C_fold_1_0', [[72.0, 50.0], [80.7, 50.0]]), ('C_fold_1_3', [[87.3, 50.0], [96.0, 50.0]])]:
                c.line(points, id=object_id, linestyle=(0.0, [4.0, 3.0]))
            for object_id, points in [('option_D_boundary_0', [[21.0, 6.0], [45.0, 6.0]]), ('option_D_boundary_1', [[45.0, 6.0], [45.0, 30.0]]), ('option_D_boundary_2', [[45.0, 30.0], [21.0, 30.0]]), ('option_D_boundary_3', [[21.0, 30.0], [21.0, 6.0]]), ('option_D_boundary_4', [[36.3, 18.0], [33.0, 21.3]]), ('option_D_boundary_5', [[33.0, 23.7], [35.1, 23.7]]), ('option_D_boundary_6', [[35.1, 23.7], [35.1, 26.1]]), ('option_D_boundary_7', [[35.1, 26.1], [33.0, 26.1]]), ('option_D_boundary_8', [[36.3, 18.0], [33.0, 14.7]]), ('option_D_boundary_9', [[33.0, 12.3], [35.1, 12.3]]), ('option_D_boundary_10', [[35.1, 12.3], [35.1, 9.9]]), ('option_D_boundary_11', [[35.1, 9.9], [33.0, 9.9]]), ('option_D_boundary_12', [[29.7, 18.0], [33.0, 21.3]]), ('option_D_boundary_13', [[33.0, 23.7], [30.9, 23.7]]), ('option_D_boundary_14', [[30.9, 23.7], [30.9, 26.1]]), ('option_D_boundary_15', [[30.9, 26.1], [33.0, 26.1]]), ('option_D_boundary_16', [[29.7, 18.0], [33.0, 14.7]]), ('option_D_boundary_17', [[33.0, 12.3], [30.9, 12.3]]), ('option_D_boundary_18', [[30.9, 12.3], [30.9, 9.9]]), ('option_D_boundary_19', [[30.9, 9.9], [33.0, 9.9]])]:
                c.line(points, id=object_id)
            for object_id, points in [('D_fold_0_0', [[33.0, 6.0], [33.0, 9.9]]), ('D_fold_0_2', [[33.0, 12.3], [33.0, 14.7]]), ('D_fold_0_5', [[33.0, 21.3], [33.0, 23.7]]), ('D_fold_0_7', [[33.0, 26.1], [33.0, 30.0]]), ('D_fold_1_0', [[21.0, 18.0], [29.7, 18.0]]), ('D_fold_1_3', [[36.3, 18.0], [45.0, 18.0]])]:
                c.line(points, id=object_id, linestyle=(0.0, [4.0, 3.0]))
            for object_id, points in self._geometry_04:
                c.line(points, id=object_id)
            for object_id, points in [('E_fold_0_0', [[67.0, 6.0], [67.0, 9.9]]), ('E_fold_0_2', [[67.0, 12.3], [67.0, 14.7]]), ('E_fold_0_5', [[67.0, 21.3], [67.0, 23.7]]), ('E_fold_0_7', [[67.0, 26.1], [67.0, 30.0]]), ('E_fold_1_0', [[55.0, 18.0], [63.7, 18.0]]), ('E_fold_1_3', [[70.3, 18.0], [79.0, 18.0]])]:
                c.line(points, id=object_id, linestyle=(0.0, [4.0, 3.0]))
            for object_id, text, anchor in [('option_label_A', '(A)', [16, 35]), ('option_label_B', '(B)', [50, 35]), ('option_label_C', '(C)', [84, 35]), ('option_label_D', '(D)', [33, 3]), ('option_label_E', '(E)', [67, 3])]:
                c.text(text, anchor, id=object_id, rotation_mode='default')
            return c.save(output_path)

    def draw_C01(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane548_C01.png'
        _geometry_01 = [('option_B_boundary_0', [[40.4, 38.0], [59.6, 38.0]]),
         ('option_B_boundary_1', [[62.0, 40.4], [62.0, 59.6]]),
         ('option_B_boundary_2', [[59.6, 62.0], [40.4, 62.0]]),
         ('option_B_boundary_3', [[38.0, 59.6], [38.0, 40.4]]),
         ('option_B_boundary_4', [[53.3, 50.0], [53.3, 53.3]]),
         ('option_B_boundary_5', [[53.3, 53.3], [50.0, 53.3]]),
         ('option_B_boundary_6', [[50.0, 55.7], [52.1, 55.7]]),
         ('option_B_boundary_7', [[52.1, 55.7], [52.1, 58.1]]),
         ('option_B_boundary_8', [[52.1, 58.1], [50.0, 58.1]]),
         ('option_B_boundary_9', [[59.6, 62.0], [62.0, 59.6]]),
         ('option_B_boundary_10', [[53.3, 50.0], [53.3, 46.7]]),
         ('option_B_boundary_11', [[53.3, 46.7], [50.0, 46.7]]),
         ('option_B_boundary_12', [[50.0, 44.3], [52.1, 44.3]]),
         ('option_B_boundary_13', [[52.1, 44.3], [52.1, 41.9]]),
         ('option_B_boundary_14', [[52.1, 41.9], [50.0, 41.9]]),
         ('option_B_boundary_15', [[59.6, 38.0], [62.0, 40.4]]),
         ('option_B_boundary_16', [[46.7, 50.0], [46.7, 53.3]]),
         ('option_B_boundary_17', [[46.7, 53.3], [50.0, 53.3]]),
         ('option_B_boundary_18', [[50.0, 55.7], [47.9, 55.7]]),
         ('option_B_boundary_19', [[47.9, 55.7], [47.9, 58.1]]),
         ('option_B_boundary_20', [[47.9, 58.1], [50.0, 58.1]]),
         ('option_B_boundary_21', [[40.4, 62.0], [38.0, 59.6]]),
         ('option_B_boundary_22', [[46.7, 50.0], [46.7, 46.7]]),
         ('option_B_boundary_23', [[46.7, 46.7], [50.0, 46.7]]),
         ('option_B_boundary_24', [[50.0, 44.3], [47.9, 44.3]]),
         ('option_B_boundary_25', [[47.9, 44.3], [47.9, 41.9]]),
         ('option_B_boundary_26', [[47.9, 41.9], [50.0, 41.9]]),
         ('option_B_boundary_27', [[40.4, 38.0], [38.0, 40.4]])]
        _geometry_02 = [('option_C_boundary_0', [[74.4, 38.0], [93.6, 38.0]]),
         ('option_C_boundary_1', [[96.0, 40.4], [96.0, 59.6]]),
         ('option_C_boundary_2', [[93.6, 62.0], [74.4, 62.0]]),
         ('option_C_boundary_3', [[72.0, 59.6], [72.0, 40.4]]),
         ('option_C_boundary_4', [[87.3, 50.0], [84.0, 53.3]]),
         ('option_C_boundary_5', [[85.5, 55.7], [87.6, 55.7]]),
         ('option_C_boundary_6', [[87.6, 55.7], [87.6, 58.1]]),
         ('option_C_boundary_7', [[87.6, 58.1], [85.5, 58.1]]),
         ('option_C_boundary_8', [[85.5, 58.1], [85.5, 55.7]]),
         ('option_C_boundary_9', [[93.6, 62.0], [96.0, 59.6]]),
         ('option_C_boundary_10', [[87.3, 50.0], [84.0, 46.7]]),
         ('option_C_boundary_11', [[85.5, 44.3], [87.6, 44.3]]),
         ('option_C_boundary_12', [[87.6, 44.3], [87.6, 41.9]]),
         ('option_C_boundary_13', [[87.6, 41.9], [85.5, 41.9]]),
         ('option_C_boundary_14', [[85.5, 41.9], [85.5, 44.3]]),
         ('option_C_boundary_15', [[93.6, 38.0], [96.0, 40.4]]),
         ('option_C_boundary_16', [[80.7, 50.0], [84.0, 53.3]]),
         ('option_C_boundary_17', [[82.5, 55.7], [80.4, 55.7]]),
         ('option_C_boundary_18', [[80.4, 55.7], [80.4, 58.1]]),
         ('option_C_boundary_19', [[80.4, 58.1], [82.5, 58.1]]),
         ('option_C_boundary_20', [[82.5, 58.1], [82.5, 55.7]]),
         ('option_C_boundary_21', [[74.4, 62.0], [72.0, 59.6]]),
         ('option_C_boundary_22', [[80.7, 50.0], [84.0, 46.7]]),
         ('option_C_boundary_23', [[82.5, 44.3], [80.4, 44.3]]),
         ('option_C_boundary_24', [[80.4, 44.3], [80.4, 41.9]]),
         ('option_C_boundary_25', [[80.4, 41.9], [82.5, 41.9]]),
         ('option_C_boundary_26', [[82.5, 41.9], [82.5, 44.3]]),
         ('option_C_boundary_27', [[74.4, 38.0], [72.0, 40.4]])]
        _geometry_03 = [('option_E_boundary_0', [[57.4, 6.0], [76.6, 6.0]]),
         ('option_E_boundary_1', [[79.0, 8.4], [79.0, 27.6]]),
         ('option_E_boundary_2', [[76.6, 30.0], [57.4, 30.0]]),
         ('option_E_boundary_3', [[55.0, 27.6], [55.0, 8.4]]),
         ('option_E_boundary_4', [[70.3, 18.0], [67.0, 21.3]]),
         ('option_E_boundary_5', [[67.0, 23.7], [69.1, 23.7]]),
         ('option_E_boundary_6', [[69.1, 23.7], [69.1, 26.1]]),
         ('option_E_boundary_7', [[69.1, 26.1], [67.0, 26.1]]),
         ('option_E_boundary_8', [[76.6, 30.0], [79.0, 27.6]]),
         ('option_E_boundary_9', [[70.3, 18.0], [67.0, 14.7]]),
         ('option_E_boundary_10', [[67.0, 12.3], [69.1, 12.3]]),
         ('option_E_boundary_11', [[69.1, 12.3], [69.1, 9.9]]),
         ('option_E_boundary_12', [[69.1, 9.9], [67.0, 9.9]]),
         ('option_E_boundary_13', [[76.6, 6.0], [79.0, 8.4]]),
         ('option_E_boundary_14', [[63.7, 18.0], [67.0, 21.3]]),
         ('option_E_boundary_15', [[67.0, 23.7], [64.9, 23.7]]),
         ('option_E_boundary_16', [[64.9, 23.7], [64.9, 26.1]]),
         ('option_E_boundary_17', [[64.9, 26.1], [67.0, 26.1]]),
         ('option_E_boundary_18', [[57.4, 30.0], [55.0, 27.6]]),
         ('option_E_boundary_19', [[63.7, 18.0], [67.0, 14.7]]),
         ('option_E_boundary_20', [[67.0, 12.3], [64.9, 12.3]]),
         ('option_E_boundary_21', [[64.9, 12.3], [64.9, 9.9]]),
         ('option_E_boundary_22', [[64.9, 9.9], [67.0, 9.9]]),
         ('option_E_boundary_23', [[57.4, 6.0], [55.0, 8.4]])]
        with Canvas(PLANE, xlim=(1.6559000861326467, 98.49456287683032), ylim=(-0.6010443583117961, 96.23761843238587), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
            for object_id, points in [('original_border_0', [[14, 74], [34, 74]]), ('original_border_1', [[34, 74], [34, 94]]), ('original_border_2', [[34, 94], [14, 94]]), ('original_border_3', [[14, 94], [14, 74]])]:
                c.line(points, id=object_id)
            c.line([[24.0, 74.0], [24.0, 94.0]], id='original_fold_0_0', linestyle=(0.0, [4.0, 3.0]))
            c.line([[14.0, 84.0], [34.0, 84.0]], id='original_fold_1_0', linestyle=(0.0, [4.0, 3.0]))
            c.path([[70.0, 79.0], [80.0, 79.0], [80.0, 89.0], [70.0, 89.0], [70.0, 79.0]], [1, 2, 2, 2, 79], id='folded_paper_fill', zorder=1, edgecolor='none', facecolor=(1.0, 1.0, 1.0, 1.0), capstyle='butt')
            for object_id, vertices, codes in [('cut_1_fill', [[70.0, 79.0], [72.75, 79.0], [70.0, 81.75], [70.0, 79.0]], [1, 2, 2, 79]), ('cut_2_fill', [[70.0, 83.75], [71.75, 83.75], [71.75, 85.75], [70.0, 85.75], [70.0, 83.75]], [1, 2, 2, 2, 79]), ('cut_3_fill', [[80.0, 89.0], [78.0, 89.0], [80.0, 87.0], [80.0, 89.0]], [1, 2, 2, 79])]:
                c.path(vertices, codes, id=object_id, zorder=1, edgecolor='none', facecolor=(0.7529411764705882, 0.7529411764705882, 0.7529411764705882, 1.0), capstyle='butt')
            c.line([[70, 79], [80, 79]], id='folded_border_0', color='#EA580C', linestyle=(0.0, [4.0, 3.0]))
            c.line([[80, 79], [80, 89]], id='folded_border_1', color='#EA580C')
            c.line([[80, 89], [70, 89]], id='folded_border_2', color='#EA580C')
            c.line([[70, 89], [70, 79]], id='folded_border_3', color='#EA580C', linestyle=(0.0, [4.0, 3.0]))
            for object_id, points in [('cut_1_path_1', [[72.75, 79.0], [70.0, 81.75]]), ('cut_2_path_0', [[70.0, 83.75], [71.75, 83.75]]), ('cut_2_path_1', [[71.75, 83.75], [71.75, 85.75]]), ('cut_2_path_2', [[71.75, 85.75], [70.0, 85.75]]), ('cut_3_path_1', [[78.0, 89.0], [80.0, 87.0]])]:
                c.line(points, id=object_id, color='#EA580C')
            for object_id, points in [('fold_process_arrow', [[41, 84], [59, 84]]), ('fold_process_arrow_head_1', [[59.0, 84.0], [57.0, 85.1]]), ('fold_process_arrow_head_2', [[59.0, 84.0], [57.0, 82.9]]), ('option_A_boundary_0', [[4.0, 38.0], [28.0, 38.0]]), ('option_A_boundary_1', [[28.0, 38.0], [28.0, 59.6]]), ('option_A_boundary_2', [[25.6, 62.0], [6.4, 62.0]]), ('option_A_boundary_3', [[4.0, 59.6], [4.0, 38.0]]), ('option_A_boundary_4', [[16.0, 50.0], [19.3, 50.0]]), ('option_A_boundary_5', [[19.3, 50.0], [16.0, 53.3]]), ('option_A_boundary_6', [[16.0, 55.7], [18.1, 55.7]]), ('option_A_boundary_7', [[18.1, 55.7], [18.1, 58.1]]), ('option_A_boundary_8', [[18.1, 58.1], [16.0, 58.1]]), ('option_A_boundary_9', [[25.6, 62.0], [28.0, 59.6]]), ('option_A_boundary_10', [[16.0, 50.0], [12.7, 50.0]]), ('option_A_boundary_11', [[12.7, 50.0], [16.0, 53.3]]), ('option_A_boundary_12', [[16.0, 55.7], [13.9, 55.7]]), ('option_A_boundary_13', [[13.9, 55.7], [13.9, 58.1]]), ('option_A_boundary_14', [[13.9, 58.1], [16.0, 58.1]]), ('option_A_boundary_15', [[6.4, 62.0], [4.0, 59.6]])]:
                c.line(points, id=object_id)
            for object_id, points in [('A_fold_0_0', [[16.0, 38.0], [16.0, 50.0]]), ('A_fold_0_2', [[16.0, 53.3], [16.0, 55.7]]), ('A_fold_0_4', [[16.0, 58.1], [16.0, 62.0]]), ('A_fold_1_0', [[4.0, 50.0], [12.7, 50.0]]), ('A_fold_1_3', [[19.3, 50.0], [28.0, 50.0]])]:
                c.line(points, id=object_id, linestyle=(0.0, [4.0, 3.0]))
            for object_id, points in _geometry_01:
                c.line(points, id=object_id)
            for object_id, points in [('B_fold_0_0', [[50.0, 38.0], [50.0, 41.9]]), ('B_fold_0_2', [[50.0, 44.3], [50.0, 46.7]]), ('B_fold_0_5', [[50.0, 53.3], [50.0, 55.7]]), ('B_fold_0_7', [[50.0, 58.1], [50.0, 62.0]]), ('B_fold_1_0', [[38.0, 50.0], [46.7, 50.0]]), ('B_fold_1_3', [[53.3, 50.0], [62.0, 50.0]])]:
                c.line(points, id=object_id, linestyle=(0.0, [4.0, 3.0]))
            for object_id, points in _geometry_02:
                c.line(points, id=object_id, color='#EA580C')
            for object_id, points in [('C_fold_0_0', [[84.0, 38.0], [84.0, 46.7]]), ('C_fold_0_3', [[84.0, 53.3], [84.0, 62.0]]), ('C_fold_1_0', [[72.0, 50.0], [80.7, 50.0]]), ('C_fold_1_3', [[87.3, 50.0], [96.0, 50.0]])]:
                c.line(points, id=object_id, linestyle=(0.0, [4.0, 3.0]))
            for object_id, points in [('option_D_boundary_0', [[21.0, 6.0], [45.0, 6.0]]), ('option_D_boundary_1', [[45.0, 6.0], [45.0, 30.0]]), ('option_D_boundary_2', [[45.0, 30.0], [21.0, 30.0]]), ('option_D_boundary_3', [[21.0, 30.0], [21.0, 6.0]]), ('option_D_boundary_4', [[36.3, 18.0], [33.0, 21.3]]), ('option_D_boundary_5', [[33.0, 23.7], [35.1, 23.7]]), ('option_D_boundary_6', [[35.1, 23.7], [35.1, 26.1]]), ('option_D_boundary_7', [[35.1, 26.1], [33.0, 26.1]]), ('option_D_boundary_8', [[36.3, 18.0], [33.0, 14.7]]), ('option_D_boundary_9', [[33.0, 12.3], [35.1, 12.3]]), ('option_D_boundary_10', [[35.1, 12.3], [35.1, 9.9]]), ('option_D_boundary_11', [[35.1, 9.9], [33.0, 9.9]]), ('option_D_boundary_12', [[29.7, 18.0], [33.0, 21.3]]), ('option_D_boundary_13', [[33.0, 23.7], [30.9, 23.7]]), ('option_D_boundary_14', [[30.9, 23.7], [30.9, 26.1]]), ('option_D_boundary_15', [[30.9, 26.1], [33.0, 26.1]]), ('option_D_boundary_16', [[29.7, 18.0], [33.0, 14.7]]), ('option_D_boundary_17', [[33.0, 12.3], [30.9, 12.3]]), ('option_D_boundary_18', [[30.9, 12.3], [30.9, 9.9]]), ('option_D_boundary_19', [[30.9, 9.9], [33.0, 9.9]])]:
                c.line(points, id=object_id)
            for object_id, points in [('D_fold_0_0', [[33.0, 6.0], [33.0, 9.9]]), ('D_fold_0_2', [[33.0, 12.3], [33.0, 14.7]]), ('D_fold_0_5', [[33.0, 21.3], [33.0, 23.7]]), ('D_fold_0_7', [[33.0, 26.1], [33.0, 30.0]]), ('D_fold_1_0', [[21.0, 18.0], [29.7, 18.0]]), ('D_fold_1_3', [[36.3, 18.0], [45.0, 18.0]])]:
                c.line(points, id=object_id, linestyle=(0.0, [4.0, 3.0]))
            for object_id, points in _geometry_03:
                c.line(points, id=object_id)
            for object_id, points in [('E_fold_0_0', [[67.0, 6.0], [67.0, 9.9]]), ('E_fold_0_2', [[67.0, 12.3], [67.0, 14.7]]), ('E_fold_0_5', [[67.0, 21.3], [67.0, 23.7]]), ('E_fold_0_7', [[67.0, 26.1], [67.0, 30.0]]), ('E_fold_1_0', [[55.0, 18.0], [63.7, 18.0]]), ('E_fold_1_3', [[70.3, 18.0], [79.0, 18.0]])]:
                c.line(points, id=object_id, linestyle=(0.0, [4.0, 3.0]))
            for object_id, text, anchor in [('option_label_A', '(A)', (16, 35)), ('option_label_B', '(B)', (50, 35)), ('option_label_C', '(C)', (84, 35)), ('option_label_D', '(D)', (33, 3)), ('option_label_E', '(E)', (67, 3))]:
                c.text(text, anchor, id=object_id, rotation_mode='default')
            return c.save(output_path)

    def draw_C02(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane548_C02.png'
        _geometry_01 = [('option_B_boundary_0', [[40.4, 38.0], [59.6, 38.0]]),
         ('option_B_boundary_1', [[62.0, 40.4], [62.0, 59.6]]),
         ('option_B_boundary_2', [[59.6, 62.0], [40.4, 62.0]]),
         ('option_B_boundary_3', [[38.0, 59.6], [38.0, 40.4]]),
         ('option_B_boundary_4', [[53.3, 50.0], [53.3, 53.3]]),
         ('option_B_boundary_5', [[53.3, 53.3], [50.0, 53.3]]),
         ('option_B_boundary_6', [[50.0, 55.7], [52.1, 55.7]]),
         ('option_B_boundary_7', [[52.1, 55.7], [52.1, 58.1]]),
         ('option_B_boundary_8', [[52.1, 58.1], [50.0, 58.1]]),
         ('option_B_boundary_9', [[59.6, 62.0], [62.0, 59.6]]),
         ('option_B_boundary_10', [[53.3, 50.0], [53.3, 46.7]]),
         ('option_B_boundary_11', [[53.3, 46.7], [50.0, 46.7]]),
         ('option_B_boundary_12', [[50.0, 44.3], [52.1, 44.3]]),
         ('option_B_boundary_13', [[52.1, 44.3], [52.1, 41.9]]),
         ('option_B_boundary_14', [[52.1, 41.9], [50.0, 41.9]]),
         ('option_B_boundary_15', [[59.6, 38.0], [62.0, 40.4]]),
         ('option_B_boundary_16', [[46.7, 50.0], [46.7, 53.3]]),
         ('option_B_boundary_17', [[46.7, 53.3], [50.0, 53.3]]),
         ('option_B_boundary_18', [[50.0, 55.7], [47.9, 55.7]]),
         ('option_B_boundary_19', [[47.9, 55.7], [47.9, 58.1]]),
         ('option_B_boundary_20', [[47.9, 58.1], [50.0, 58.1]]),
         ('option_B_boundary_21', [[40.4, 62.0], [38.0, 59.6]]),
         ('option_B_boundary_22', [[46.7, 50.0], [46.7, 46.7]]),
         ('option_B_boundary_23', [[46.7, 46.7], [50.0, 46.7]]),
         ('option_B_boundary_24', [[50.0, 44.3], [47.9, 44.3]]),
         ('option_B_boundary_25', [[47.9, 44.3], [47.9, 41.9]]),
         ('option_B_boundary_26', [[47.9, 41.9], [50.0, 41.9]]),
         ('option_B_boundary_27', [[40.4, 38.0], [38.0, 40.4]])]
        _geometry_02 = [('option_C_boundary_0', [[74.4, 38.0], [93.6, 38.0]]),
         ('option_C_boundary_1', [[96.0, 40.4], [96.0, 59.6]]),
         ('option_C_boundary_2', [[93.6, 62.0], [74.4, 62.0]]),
         ('option_C_boundary_3', [[72.0, 59.6], [72.0, 40.4]]),
         ('option_C_boundary_4', [[87.3, 50.0], [84.0, 53.3]]),
         ('option_C_boundary_5', [[85.5, 55.7], [87.6, 55.7]]),
         ('option_C_boundary_6', [[87.6, 55.7], [87.6, 58.1]]),
         ('option_C_boundary_7', [[87.6, 58.1], [85.5, 58.1]]),
         ('option_C_boundary_8', [[85.5, 58.1], [85.5, 55.7]]),
         ('option_C_boundary_9', [[93.6, 62.0], [96.0, 59.6]]),
         ('option_C_boundary_10', [[87.3, 50.0], [84.0, 46.7]]),
         ('option_C_boundary_11', [[85.5, 44.3], [87.6, 44.3]]),
         ('option_C_boundary_12', [[87.6, 44.3], [87.6, 41.9]]),
         ('option_C_boundary_13', [[87.6, 41.9], [85.5, 41.9]]),
         ('option_C_boundary_14', [[85.5, 41.9], [85.5, 44.3]]),
         ('option_C_boundary_15', [[93.6, 38.0], [96.0, 40.4]]),
         ('option_C_boundary_16', [[80.7, 50.0], [84.0, 53.3]]),
         ('option_C_boundary_17', [[82.5, 55.7], [80.4, 55.7]]),
         ('option_C_boundary_18', [[80.4, 55.7], [80.4, 58.1]]),
         ('option_C_boundary_19', [[80.4, 58.1], [82.5, 58.1]]),
         ('option_C_boundary_20', [[82.5, 58.1], [82.5, 55.7]]),
         ('option_C_boundary_21', [[74.4, 62.0], [72.0, 59.6]]),
         ('option_C_boundary_22', [[80.7, 50.0], [84.0, 46.7]]),
         ('option_C_boundary_23', [[82.5, 44.3], [80.4, 44.3]]),
         ('option_C_boundary_24', [[80.4, 44.3], [80.4, 41.9]]),
         ('option_C_boundary_25', [[80.4, 41.9], [82.5, 41.9]]),
         ('option_C_boundary_26', [[82.5, 41.9], [82.5, 44.3]]),
         ('option_C_boundary_27', [[74.4, 38.0], [72.0, 40.4]])]
        _geometry_03 = [('option_E_boundary_0', [[57.4, 6.0], [76.6, 6.0]]),
         ('option_E_boundary_1', [[79.0, 8.4], [79.0, 27.6]]),
         ('option_E_boundary_2', [[76.6, 30.0], [57.4, 30.0]]),
         ('option_E_boundary_3', [[55.0, 27.6], [55.0, 8.4]]),
         ('option_E_boundary_4', [[70.3, 18.0], [67.0, 21.3]]),
         ('option_E_boundary_5', [[67.0, 23.7], [69.1, 23.7]]),
         ('option_E_boundary_6', [[69.1, 23.7], [69.1, 26.1]]),
         ('option_E_boundary_7', [[69.1, 26.1], [67.0, 26.1]]),
         ('option_E_boundary_8', [[76.6, 30.0], [79.0, 27.6]]),
         ('option_E_boundary_9', [[70.3, 18.0], [67.0, 14.7]]),
         ('option_E_boundary_10', [[67.0, 12.3], [69.1, 12.3]]),
         ('option_E_boundary_11', [[69.1, 12.3], [69.1, 9.9]]),
         ('option_E_boundary_12', [[69.1, 9.9], [67.0, 9.9]]),
         ('option_E_boundary_13', [[76.6, 6.0], [79.0, 8.4]]),
         ('option_E_boundary_14', [[63.7, 18.0], [67.0, 21.3]]),
         ('option_E_boundary_15', [[67.0, 23.7], [64.9, 23.7]]),
         ('option_E_boundary_16', [[64.9, 23.7], [64.9, 26.1]]),
         ('option_E_boundary_17', [[64.9, 26.1], [67.0, 26.1]]),
         ('option_E_boundary_18', [[57.4, 30.0], [55.0, 27.6]]),
         ('option_E_boundary_19', [[63.7, 18.0], [67.0, 14.7]]),
         ('option_E_boundary_20', [[67.0, 12.3], [64.9, 12.3]]),
         ('option_E_boundary_21', [[64.9, 12.3], [64.9, 9.9]]),
         ('option_E_boundary_22', [[64.9, 9.9], [67.0, 9.9]]),
         ('option_E_boundary_23', [[57.4, 6.0], [55.0, 8.4]])]
        with Canvas(PLANE, xlim=(1.6559000861326467, 98.49456287683032), ylim=(-0.6010443583117961, 96.23761843238587), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
            for object_id, points in [('original_border_0', [[14, 74], [34, 74]]), ('original_border_1', [[34, 74], [34, 94]]), ('original_border_2', [[34, 94], [14, 94]]), ('original_border_3', [[14, 94], [14, 74]])]:
                c.line(points, id=object_id)
            c.line([[24.0, 74.0], [24.0, 94.0]], id='original_fold_0_0', linestyle=(0.0, [4.0, 3.0]))
            c.line([[14.0, 84.0], [34.0, 84.0]], id='original_fold_1_0', linestyle=(0.0, [4.0, 3.0]))
            c.path([[70.0, 79.0], [80.0, 79.0], [80.0, 89.0], [70.0, 89.0], [70.0, 79.0]], [1, 2, 2, 2, 79], id='folded_paper_fill', zorder=1, edgecolor='none', facecolor=(1.0, 1.0, 1.0, 1.0), capstyle='butt')
            for object_id, vertices, codes in [('cut_1_fill', [[70.0, 79.0], [72.75, 79.0], [70.0, 81.75], [70.0, 79.0]], [1, 2, 2, 79]), ('cut_2_fill', [[70.0, 83.75], [71.75, 83.75], [71.75, 85.75], [70.0, 85.75], [70.0, 83.75]], [1, 2, 2, 2, 79]), ('cut_3_fill', [[80.0, 89.0], [78.0, 89.0], [80.0, 87.0], [80.0, 89.0]], [1, 2, 2, 79])]:
                c.path(vertices, codes, id=object_id, zorder=1, edgecolor='none', facecolor=(0.7529411764705882, 0.7529411764705882, 0.7529411764705882, 1.0), capstyle='butt')
            c.line([[70, 79], [80, 79]], id='folded_border_0', color='#16A34A', linestyle=(0.0, [4.0, 3.0]))
            c.line([[80, 79], [80, 89]], id='folded_border_1', color='#16A34A')
            c.line([[80, 89], [70, 89]], id='folded_border_2', color='#16A34A')
            c.line([[70, 89], [70, 79]], id='folded_border_3', color='#16A34A', linestyle=(0.0, [4.0, 3.0]))
            for object_id, points in [('cut_1_path_1', [[72.75, 79.0], [70.0, 81.75]]), ('cut_2_path_0', [[70.0, 83.75], [71.75, 83.75]]), ('cut_2_path_1', [[71.75, 83.75], [71.75, 85.75]]), ('cut_2_path_2', [[71.75, 85.75], [70.0, 85.75]]), ('cut_3_path_1', [[78.0, 89.0], [80.0, 87.0]])]:
                c.line(points, id=object_id, color='#16A34A')
            for object_id, points in [('fold_process_arrow', [[41, 84], [59, 84]]), ('fold_process_arrow_head_1', [[59.0, 84.0], [57.0, 85.1]]), ('fold_process_arrow_head_2', [[59.0, 84.0], [57.0, 82.9]]), ('option_A_boundary_0', [[4.0, 38.0], [28.0, 38.0]]), ('option_A_boundary_1', [[28.0, 38.0], [28.0, 59.6]]), ('option_A_boundary_2', [[25.6, 62.0], [6.4, 62.0]]), ('option_A_boundary_3', [[4.0, 59.6], [4.0, 38.0]]), ('option_A_boundary_4', [[16.0, 50.0], [19.3, 50.0]]), ('option_A_boundary_5', [[19.3, 50.0], [16.0, 53.3]]), ('option_A_boundary_6', [[16.0, 55.7], [18.1, 55.7]]), ('option_A_boundary_7', [[18.1, 55.7], [18.1, 58.1]]), ('option_A_boundary_8', [[18.1, 58.1], [16.0, 58.1]]), ('option_A_boundary_9', [[25.6, 62.0], [28.0, 59.6]]), ('option_A_boundary_10', [[16.0, 50.0], [12.7, 50.0]]), ('option_A_boundary_11', [[12.7, 50.0], [16.0, 53.3]]), ('option_A_boundary_12', [[16.0, 55.7], [13.9, 55.7]]), ('option_A_boundary_13', [[13.9, 55.7], [13.9, 58.1]]), ('option_A_boundary_14', [[13.9, 58.1], [16.0, 58.1]]), ('option_A_boundary_15', [[6.4, 62.0], [4.0, 59.6]])]:
                c.line(points, id=object_id)
            for object_id, points in [('A_fold_0_0', [[16.0, 38.0], [16.0, 50.0]]), ('A_fold_0_2', [[16.0, 53.3], [16.0, 55.7]]), ('A_fold_0_4', [[16.0, 58.1], [16.0, 62.0]]), ('A_fold_1_0', [[4.0, 50.0], [12.7, 50.0]]), ('A_fold_1_3', [[19.3, 50.0], [28.0, 50.0]])]:
                c.line(points, id=object_id, linestyle=(0.0, [4.0, 3.0]))
            for object_id, points in _geometry_01:
                c.line(points, id=object_id)
            for object_id, points in [('B_fold_0_0', [[50.0, 38.0], [50.0, 41.9]]), ('B_fold_0_2', [[50.0, 44.3], [50.0, 46.7]]), ('B_fold_0_5', [[50.0, 53.3], [50.0, 55.7]]), ('B_fold_0_7', [[50.0, 58.1], [50.0, 62.0]]), ('B_fold_1_0', [[38.0, 50.0], [46.7, 50.0]]), ('B_fold_1_3', [[53.3, 50.0], [62.0, 50.0]])]:
                c.line(points, id=object_id, linestyle=(0.0, [4.0, 3.0]))
            for object_id, points in _geometry_02:
                c.line(points, id=object_id, color='#16A34A')
            for object_id, points in [('C_fold_0_0', [[84.0, 38.0], [84.0, 46.7]]), ('C_fold_0_3', [[84.0, 53.3], [84.0, 62.0]]), ('C_fold_1_0', [[72.0, 50.0], [80.7, 50.0]]), ('C_fold_1_3', [[87.3, 50.0], [96.0, 50.0]])]:
                c.line(points, id=object_id, linestyle=(0.0, [4.0, 3.0]))
            for object_id, points in [('option_D_boundary_0', [[21.0, 6.0], [45.0, 6.0]]), ('option_D_boundary_1', [[45.0, 6.0], [45.0, 30.0]]), ('option_D_boundary_2', [[45.0, 30.0], [21.0, 30.0]]), ('option_D_boundary_3', [[21.0, 30.0], [21.0, 6.0]]), ('option_D_boundary_4', [[36.3, 18.0], [33.0, 21.3]]), ('option_D_boundary_5', [[33.0, 23.7], [35.1, 23.7]]), ('option_D_boundary_6', [[35.1, 23.7], [35.1, 26.1]]), ('option_D_boundary_7', [[35.1, 26.1], [33.0, 26.1]]), ('option_D_boundary_8', [[36.3, 18.0], [33.0, 14.7]]), ('option_D_boundary_9', [[33.0, 12.3], [35.1, 12.3]]), ('option_D_boundary_10', [[35.1, 12.3], [35.1, 9.9]]), ('option_D_boundary_11', [[35.1, 9.9], [33.0, 9.9]]), ('option_D_boundary_12', [[29.7, 18.0], [33.0, 21.3]]), ('option_D_boundary_13', [[33.0, 23.7], [30.9, 23.7]]), ('option_D_boundary_14', [[30.9, 23.7], [30.9, 26.1]]), ('option_D_boundary_15', [[30.9, 26.1], [33.0, 26.1]]), ('option_D_boundary_16', [[29.7, 18.0], [33.0, 14.7]]), ('option_D_boundary_17', [[33.0, 12.3], [30.9, 12.3]]), ('option_D_boundary_18', [[30.9, 12.3], [30.9, 9.9]]), ('option_D_boundary_19', [[30.9, 9.9], [33.0, 9.9]])]:
                c.line(points, id=object_id)
            for object_id, points in [('D_fold_0_0', [[33.0, 6.0], [33.0, 9.9]]), ('D_fold_0_2', [[33.0, 12.3], [33.0, 14.7]]), ('D_fold_0_5', [[33.0, 21.3], [33.0, 23.7]]), ('D_fold_0_7', [[33.0, 26.1], [33.0, 30.0]]), ('D_fold_1_0', [[21.0, 18.0], [29.7, 18.0]]), ('D_fold_1_3', [[36.3, 18.0], [45.0, 18.0]])]:
                c.line(points, id=object_id, linestyle=(0.0, [4.0, 3.0]))
            for object_id, points in _geometry_03:
                c.line(points, id=object_id)
            for object_id, points in [('E_fold_0_0', [[67.0, 6.0], [67.0, 9.9]]), ('E_fold_0_2', [[67.0, 12.3], [67.0, 14.7]]), ('E_fold_0_5', [[67.0, 21.3], [67.0, 23.7]]), ('E_fold_0_7', [[67.0, 26.1], [67.0, 30.0]]), ('E_fold_1_0', [[55.0, 18.0], [63.7, 18.0]]), ('E_fold_1_3', [[70.3, 18.0], [79.0, 18.0]])]:
                c.line(points, id=object_id, linestyle=(0.0, [4.0, 3.0]))
            for object_id, text, anchor in [('option_label_A', '(A)', (16, 35)), ('option_label_B', '(B)', (50, 35)), ('option_label_C', '(C)', (84, 35)), ('option_label_D', '(D)', (33, 3)), ('option_label_E', '(E)', (67, 3))]:
                c.text(text, anchor, id=object_id, rotation_mode='default')
            return c.save(output_path)

    def draw_C03(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane548_C03.png'
        _geometry_01 = [('option_B_boundary_0', [[40.4, 38.0], [59.6, 38.0]]),
         ('option_B_boundary_1', [[62.0, 40.4], [62.0, 59.6]]),
         ('option_B_boundary_2', [[59.6, 62.0], [40.4, 62.0]]),
         ('option_B_boundary_3', [[38.0, 59.6], [38.0, 40.4]]),
         ('option_B_boundary_4', [[53.3, 50.0], [53.3, 53.3]]),
         ('option_B_boundary_5', [[53.3, 53.3], [50.0, 53.3]]),
         ('option_B_boundary_6', [[50.0, 55.7], [52.1, 55.7]]),
         ('option_B_boundary_7', [[52.1, 55.7], [52.1, 58.1]]),
         ('option_B_boundary_8', [[52.1, 58.1], [50.0, 58.1]]),
         ('option_B_boundary_9', [[59.6, 62.0], [62.0, 59.6]]),
         ('option_B_boundary_10', [[53.3, 50.0], [53.3, 46.7]]),
         ('option_B_boundary_11', [[53.3, 46.7], [50.0, 46.7]]),
         ('option_B_boundary_12', [[50.0, 44.3], [52.1, 44.3]]),
         ('option_B_boundary_13', [[52.1, 44.3], [52.1, 41.9]]),
         ('option_B_boundary_14', [[52.1, 41.9], [50.0, 41.9]]),
         ('option_B_boundary_15', [[59.6, 38.0], [62.0, 40.4]]),
         ('option_B_boundary_16', [[46.7, 50.0], [46.7, 53.3]]),
         ('option_B_boundary_17', [[46.7, 53.3], [50.0, 53.3]]),
         ('option_B_boundary_18', [[50.0, 55.7], [47.9, 55.7]]),
         ('option_B_boundary_19', [[47.9, 55.7], [47.9, 58.1]]),
         ('option_B_boundary_20', [[47.9, 58.1], [50.0, 58.1]]),
         ('option_B_boundary_21', [[40.4, 62.0], [38.0, 59.6]]),
         ('option_B_boundary_22', [[46.7, 50.0], [46.7, 46.7]]),
         ('option_B_boundary_23', [[46.7, 46.7], [50.0, 46.7]]),
         ('option_B_boundary_24', [[50.0, 44.3], [47.9, 44.3]]),
         ('option_B_boundary_25', [[47.9, 44.3], [47.9, 41.9]]),
         ('option_B_boundary_26', [[47.9, 41.9], [50.0, 41.9]]),
         ('option_B_boundary_27', [[40.4, 38.0], [38.0, 40.4]])]
        _geometry_02 = [('option_C_boundary_0', [[74.4, 38.0], [93.6, 38.0]]),
         ('option_C_boundary_1', [[96.0, 40.4], [96.0, 59.6]]),
         ('option_C_boundary_2', [[93.6, 62.0], [74.4, 62.0]]),
         ('option_C_boundary_3', [[72.0, 59.6], [72.0, 40.4]]),
         ('option_C_boundary_4', [[87.3, 50.0], [84.0, 53.3]]),
         ('option_C_boundary_5', [[85.5, 55.7], [87.6, 55.7]]),
         ('option_C_boundary_6', [[87.6, 55.7], [87.6, 58.1]]),
         ('option_C_boundary_7', [[87.6, 58.1], [85.5, 58.1]]),
         ('option_C_boundary_8', [[85.5, 58.1], [85.5, 55.7]]),
         ('option_C_boundary_9', [[93.6, 62.0], [96.0, 59.6]]),
         ('option_C_boundary_10', [[87.3, 50.0], [84.0, 46.7]]),
         ('option_C_boundary_11', [[85.5, 44.3], [87.6, 44.3]]),
         ('option_C_boundary_12', [[87.6, 44.3], [87.6, 41.9]]),
         ('option_C_boundary_13', [[87.6, 41.9], [85.5, 41.9]]),
         ('option_C_boundary_14', [[85.5, 41.9], [85.5, 44.3]]),
         ('option_C_boundary_15', [[93.6, 38.0], [96.0, 40.4]]),
         ('option_C_boundary_16', [[80.7, 50.0], [84.0, 53.3]]),
         ('option_C_boundary_17', [[82.5, 55.7], [80.4, 55.7]]),
         ('option_C_boundary_18', [[80.4, 55.7], [80.4, 58.1]]),
         ('option_C_boundary_19', [[80.4, 58.1], [82.5, 58.1]]),
         ('option_C_boundary_20', [[82.5, 58.1], [82.5, 55.7]]),
         ('option_C_boundary_21', [[74.4, 62.0], [72.0, 59.6]]),
         ('option_C_boundary_22', [[80.7, 50.0], [84.0, 46.7]]),
         ('option_C_boundary_23', [[82.5, 44.3], [80.4, 44.3]]),
         ('option_C_boundary_24', [[80.4, 44.3], [80.4, 41.9]]),
         ('option_C_boundary_25', [[80.4, 41.9], [82.5, 41.9]]),
         ('option_C_boundary_26', [[82.5, 41.9], [82.5, 44.3]]),
         ('option_C_boundary_27', [[74.4, 38.0], [72.0, 40.4]])]
        _geometry_03 = [('option_E_boundary_0', [[57.4, 6.0], [76.6, 6.0]]),
         ('option_E_boundary_1', [[79.0, 8.4], [79.0, 27.6]]),
         ('option_E_boundary_2', [[76.6, 30.0], [57.4, 30.0]]),
         ('option_E_boundary_3', [[55.0, 27.6], [55.0, 8.4]]),
         ('option_E_boundary_4', [[70.3, 18.0], [67.0, 21.3]]),
         ('option_E_boundary_5', [[67.0, 23.7], [69.1, 23.7]]),
         ('option_E_boundary_6', [[69.1, 23.7], [69.1, 26.1]]),
         ('option_E_boundary_7', [[69.1, 26.1], [67.0, 26.1]]),
         ('option_E_boundary_8', [[76.6, 30.0], [79.0, 27.6]]),
         ('option_E_boundary_9', [[70.3, 18.0], [67.0, 14.7]]),
         ('option_E_boundary_10', [[67.0, 12.3], [69.1, 12.3]]),
         ('option_E_boundary_11', [[69.1, 12.3], [69.1, 9.9]]),
         ('option_E_boundary_12', [[69.1, 9.9], [67.0, 9.9]]),
         ('option_E_boundary_13', [[76.6, 6.0], [79.0, 8.4]]),
         ('option_E_boundary_14', [[63.7, 18.0], [67.0, 21.3]]),
         ('option_E_boundary_15', [[67.0, 23.7], [64.9, 23.7]]),
         ('option_E_boundary_16', [[64.9, 23.7], [64.9, 26.1]]),
         ('option_E_boundary_17', [[64.9, 26.1], [67.0, 26.1]]),
         ('option_E_boundary_18', [[57.4, 30.0], [55.0, 27.6]]),
         ('option_E_boundary_19', [[63.7, 18.0], [67.0, 14.7]]),
         ('option_E_boundary_20', [[67.0, 12.3], [64.9, 12.3]]),
         ('option_E_boundary_21', [[64.9, 12.3], [64.9, 9.9]]),
         ('option_E_boundary_22', [[64.9, 9.9], [67.0, 9.9]]),
         ('option_E_boundary_23', [[57.4, 6.0], [55.0, 8.4]])]
        with Canvas(PLANE, xlim=(1.6559000861326467, 98.49456287683032), ylim=(-0.6010443583117961, 96.23761843238587), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
            for object_id, points in [('original_border_0', [[14, 74], [34, 74]]), ('original_border_1', [[34, 74], [34, 94]]), ('original_border_2', [[34, 94], [14, 94]]), ('original_border_3', [[14, 94], [14, 74]])]:
                c.line(points, id=object_id)
            c.line([[24.0, 74.0], [24.0, 94.0]], id='original_fold_0_0', linestyle=(0.0, [4.0, 3.0]))
            c.line([[14.0, 84.0], [34.0, 84.0]], id='original_fold_1_0', linestyle=(0.0, [4.0, 3.0]))
            c.path([[70.0, 79.0], [80.0, 79.0], [80.0, 89.0], [70.0, 89.0], [70.0, 79.0]], [1, 2, 2, 2, 79], id='folded_paper_fill', zorder=1, edgecolor='none', facecolor=(1.0, 1.0, 1.0, 1.0), capstyle='butt')
            for object_id, vertices, codes in [('cut_1_fill', [[70.0, 79.0], [72.75, 79.0], [70.0, 81.75], [70.0, 79.0]], [1, 2, 2, 79]), ('cut_2_fill', [[70.0, 83.75], [71.75, 83.75], [71.75, 85.75], [70.0, 85.75], [70.0, 83.75]], [1, 2, 2, 2, 79]), ('cut_3_fill', [[80.0, 89.0], [78.0, 89.0], [80.0, 87.0], [80.0, 89.0]], [1, 2, 2, 79])]:
                c.path(vertices, codes, id=object_id, zorder=1, edgecolor='none', facecolor=(0.7529411764705882, 0.7529411764705882, 0.7529411764705882, 1.0), capstyle='butt')
            c.line([[70, 79], [80, 79]], id='folded_border_0', color='#2563EB', linestyle=(0.0, [4.0, 3.0]))
            c.line([[80, 79], [80, 89]], id='folded_border_1', color='#2563EB')
            c.line([[80, 89], [70, 89]], id='folded_border_2', color='#2563EB')
            c.line([[70, 89], [70, 79]], id='folded_border_3', color='#2563EB', linestyle=(0.0, [4.0, 3.0]))
            for object_id, points in [('cut_1_path_1', [[72.75, 79.0], [70.0, 81.75]]), ('cut_2_path_0', [[70.0, 83.75], [71.75, 83.75]]), ('cut_2_path_1', [[71.75, 83.75], [71.75, 85.75]]), ('cut_2_path_2', [[71.75, 85.75], [70.0, 85.75]]), ('cut_3_path_1', [[78.0, 89.0], [80.0, 87.0]])]:
                c.line(points, id=object_id, color='#2563EB')
            for object_id, points in [('fold_process_arrow', [[41, 84], [59, 84]]), ('fold_process_arrow_head_1', [[59.0, 84.0], [57.0, 85.1]]), ('fold_process_arrow_head_2', [[59.0, 84.0], [57.0, 82.9]]), ('option_A_boundary_0', [[4.0, 38.0], [28.0, 38.0]]), ('option_A_boundary_1', [[28.0, 38.0], [28.0, 59.6]]), ('option_A_boundary_2', [[25.6, 62.0], [6.4, 62.0]]), ('option_A_boundary_3', [[4.0, 59.6], [4.0, 38.0]]), ('option_A_boundary_4', [[16.0, 50.0], [19.3, 50.0]]), ('option_A_boundary_5', [[19.3, 50.0], [16.0, 53.3]]), ('option_A_boundary_6', [[16.0, 55.7], [18.1, 55.7]]), ('option_A_boundary_7', [[18.1, 55.7], [18.1, 58.1]]), ('option_A_boundary_8', [[18.1, 58.1], [16.0, 58.1]]), ('option_A_boundary_9', [[25.6, 62.0], [28.0, 59.6]]), ('option_A_boundary_10', [[16.0, 50.0], [12.7, 50.0]]), ('option_A_boundary_11', [[12.7, 50.0], [16.0, 53.3]]), ('option_A_boundary_12', [[16.0, 55.7], [13.9, 55.7]]), ('option_A_boundary_13', [[13.9, 55.7], [13.9, 58.1]]), ('option_A_boundary_14', [[13.9, 58.1], [16.0, 58.1]]), ('option_A_boundary_15', [[6.4, 62.0], [4.0, 59.6]])]:
                c.line(points, id=object_id)
            for object_id, points in [('A_fold_0_0', [[16.0, 38.0], [16.0, 50.0]]), ('A_fold_0_2', [[16.0, 53.3], [16.0, 55.7]]), ('A_fold_0_4', [[16.0, 58.1], [16.0, 62.0]]), ('A_fold_1_0', [[4.0, 50.0], [12.7, 50.0]]), ('A_fold_1_3', [[19.3, 50.0], [28.0, 50.0]])]:
                c.line(points, id=object_id, linestyle=(0.0, [4.0, 3.0]))
            for object_id, points in _geometry_01:
                c.line(points, id=object_id)
            for object_id, points in [('B_fold_0_0', [[50.0, 38.0], [50.0, 41.9]]), ('B_fold_0_2', [[50.0, 44.3], [50.0, 46.7]]), ('B_fold_0_5', [[50.0, 53.3], [50.0, 55.7]]), ('B_fold_0_7', [[50.0, 58.1], [50.0, 62.0]]), ('B_fold_1_0', [[38.0, 50.0], [46.7, 50.0]]), ('B_fold_1_3', [[53.3, 50.0], [62.0, 50.0]])]:
                c.line(points, id=object_id, linestyle=(0.0, [4.0, 3.0]))
            for object_id, points in _geometry_02:
                c.line(points, id=object_id)
            for object_id, points in [('C_fold_0_0', [[84.0, 38.0], [84.0, 46.7]]), ('C_fold_0_3', [[84.0, 53.3], [84.0, 62.0]]), ('C_fold_1_0', [[72.0, 50.0], [80.7, 50.0]]), ('C_fold_1_3', [[87.3, 50.0], [96.0, 50.0]])]:
                c.line(points, id=object_id, linestyle=(0.0, [4.0, 3.0]))
            for object_id, points in [('option_D_boundary_0', [[21.0, 6.0], [45.0, 6.0]]), ('option_D_boundary_1', [[45.0, 6.0], [45.0, 30.0]]), ('option_D_boundary_2', [[45.0, 30.0], [21.0, 30.0]]), ('option_D_boundary_3', [[21.0, 30.0], [21.0, 6.0]]), ('option_D_boundary_4', [[36.3, 18.0], [33.0, 21.3]]), ('option_D_boundary_5', [[33.0, 23.7], [35.1, 23.7]]), ('option_D_boundary_6', [[35.1, 23.7], [35.1, 26.1]]), ('option_D_boundary_7', [[35.1, 26.1], [33.0, 26.1]]), ('option_D_boundary_8', [[36.3, 18.0], [33.0, 14.7]]), ('option_D_boundary_9', [[33.0, 12.3], [35.1, 12.3]]), ('option_D_boundary_10', [[35.1, 12.3], [35.1, 9.9]]), ('option_D_boundary_11', [[35.1, 9.9], [33.0, 9.9]]), ('option_D_boundary_12', [[29.7, 18.0], [33.0, 21.3]]), ('option_D_boundary_13', [[33.0, 23.7], [30.9, 23.7]]), ('option_D_boundary_14', [[30.9, 23.7], [30.9, 26.1]]), ('option_D_boundary_15', [[30.9, 26.1], [33.0, 26.1]]), ('option_D_boundary_16', [[29.7, 18.0], [33.0, 14.7]]), ('option_D_boundary_17', [[33.0, 12.3], [30.9, 12.3]]), ('option_D_boundary_18', [[30.9, 12.3], [30.9, 9.9]]), ('option_D_boundary_19', [[30.9, 9.9], [33.0, 9.9]])]:
                c.line(points, id=object_id, color='#2563EB')
            for object_id, points in [('D_fold_0_0', [[33.0, 6.0], [33.0, 9.9]]), ('D_fold_0_2', [[33.0, 12.3], [33.0, 14.7]]), ('D_fold_0_5', [[33.0, 21.3], [33.0, 23.7]]), ('D_fold_0_7', [[33.0, 26.1], [33.0, 30.0]]), ('D_fold_1_0', [[21.0, 18.0], [29.7, 18.0]]), ('D_fold_1_3', [[36.3, 18.0], [45.0, 18.0]])]:
                c.line(points, id=object_id, linestyle=(0.0, [4.0, 3.0]))
            for object_id, points in _geometry_03:
                c.line(points, id=object_id)
            for object_id, points in [('E_fold_0_0', [[67.0, 6.0], [67.0, 9.9]]), ('E_fold_0_2', [[67.0, 12.3], [67.0, 14.7]]), ('E_fold_0_5', [[67.0, 21.3], [67.0, 23.7]]), ('E_fold_0_7', [[67.0, 26.1], [67.0, 30.0]]), ('E_fold_1_0', [[55.0, 18.0], [63.7, 18.0]]), ('E_fold_1_3', [[70.3, 18.0], [79.0, 18.0]])]:
                c.line(points, id=object_id, linestyle=(0.0, [4.0, 3.0]))
            for object_id, text, anchor in [('option_label_A', '(A)', (16, 35)), ('option_label_B', '(B)', (50, 35)), ('option_label_C', '(C)', (84, 35)), ('option_label_D', '(D)', (33, 3)), ('option_label_E', '(E)', (67, 3))]:
                c.text(text, anchor, id=object_id, rotation_mode='default')
            return c.save(output_path)

    def draw_C04(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane548_C04.png'
        _geometry_01 = [('option_B_boundary_0', [[40.4, 38.0], [59.6, 38.0]]),
         ('option_B_boundary_1', [[62.0, 40.4], [62.0, 59.6]]),
         ('option_B_boundary_2', [[59.6, 62.0], [40.4, 62.0]]),
         ('option_B_boundary_3', [[38.0, 59.6], [38.0, 40.4]]),
         ('option_B_boundary_4', [[53.3, 50.0], [53.3, 53.3]]),
         ('option_B_boundary_5', [[53.3, 53.3], [50.0, 53.3]]),
         ('option_B_boundary_6', [[50.0, 55.7], [52.1, 55.7]]),
         ('option_B_boundary_7', [[52.1, 55.7], [52.1, 58.1]]),
         ('option_B_boundary_8', [[52.1, 58.1], [50.0, 58.1]]),
         ('option_B_boundary_9', [[59.6, 62.0], [62.0, 59.6]]),
         ('option_B_boundary_10', [[53.3, 50.0], [53.3, 46.7]]),
         ('option_B_boundary_11', [[53.3, 46.7], [50.0, 46.7]]),
         ('option_B_boundary_12', [[50.0, 44.3], [52.1, 44.3]]),
         ('option_B_boundary_13', [[52.1, 44.3], [52.1, 41.9]]),
         ('option_B_boundary_14', [[52.1, 41.9], [50.0, 41.9]]),
         ('option_B_boundary_15', [[59.6, 38.0], [62.0, 40.4]]),
         ('option_B_boundary_16', [[46.7, 50.0], [46.7, 53.3]]),
         ('option_B_boundary_17', [[46.7, 53.3], [50.0, 53.3]]),
         ('option_B_boundary_18', [[50.0, 55.7], [47.9, 55.7]]),
         ('option_B_boundary_19', [[47.9, 55.7], [47.9, 58.1]]),
         ('option_B_boundary_20', [[47.9, 58.1], [50.0, 58.1]]),
         ('option_B_boundary_21', [[40.4, 62.0], [38.0, 59.6]]),
         ('option_B_boundary_22', [[46.7, 50.0], [46.7, 46.7]]),
         ('option_B_boundary_23', [[46.7, 46.7], [50.0, 46.7]]),
         ('option_B_boundary_24', [[50.0, 44.3], [47.9, 44.3]]),
         ('option_B_boundary_25', [[47.9, 44.3], [47.9, 41.9]]),
         ('option_B_boundary_26', [[47.9, 41.9], [50.0, 41.9]]),
         ('option_B_boundary_27', [[40.4, 38.0], [38.0, 40.4]])]
        _geometry_02 = [('option_C_boundary_0', [[74.4, 38.0], [93.6, 38.0]]),
         ('option_C_boundary_1', [[96.0, 40.4], [96.0, 59.6]]),
         ('option_C_boundary_2', [[93.6, 62.0], [74.4, 62.0]]),
         ('option_C_boundary_3', [[72.0, 59.6], [72.0, 40.4]]),
         ('option_C_boundary_4', [[87.3, 50.0], [84.0, 53.3]]),
         ('option_C_boundary_5', [[85.5, 55.7], [87.6, 55.7]]),
         ('option_C_boundary_6', [[87.6, 55.7], [87.6, 58.1]]),
         ('option_C_boundary_7', [[87.6, 58.1], [85.5, 58.1]]),
         ('option_C_boundary_8', [[85.5, 58.1], [85.5, 55.7]]),
         ('option_C_boundary_9', [[93.6, 62.0], [96.0, 59.6]]),
         ('option_C_boundary_10', [[87.3, 50.0], [84.0, 46.7]]),
         ('option_C_boundary_11', [[85.5, 44.3], [87.6, 44.3]]),
         ('option_C_boundary_12', [[87.6, 44.3], [87.6, 41.9]]),
         ('option_C_boundary_13', [[87.6, 41.9], [85.5, 41.9]]),
         ('option_C_boundary_14', [[85.5, 41.9], [85.5, 44.3]]),
         ('option_C_boundary_15', [[93.6, 38.0], [96.0, 40.4]]),
         ('option_C_boundary_16', [[80.7, 50.0], [84.0, 53.3]]),
         ('option_C_boundary_17', [[82.5, 55.7], [80.4, 55.7]]),
         ('option_C_boundary_18', [[80.4, 55.7], [80.4, 58.1]]),
         ('option_C_boundary_19', [[80.4, 58.1], [82.5, 58.1]]),
         ('option_C_boundary_20', [[82.5, 58.1], [82.5, 55.7]]),
         ('option_C_boundary_21', [[74.4, 62.0], [72.0, 59.6]]),
         ('option_C_boundary_22', [[80.7, 50.0], [84.0, 46.7]]),
         ('option_C_boundary_23', [[82.5, 44.3], [80.4, 44.3]]),
         ('option_C_boundary_24', [[80.4, 44.3], [80.4, 41.9]]),
         ('option_C_boundary_25', [[80.4, 41.9], [82.5, 41.9]]),
         ('option_C_boundary_26', [[82.5, 41.9], [82.5, 44.3]]),
         ('option_C_boundary_27', [[74.4, 38.0], [72.0, 40.4]])]
        _geometry_03 = [('option_E_boundary_0', [[57.4, 6.0], [76.6, 6.0]]),
         ('option_E_boundary_1', [[79.0, 8.4], [79.0, 27.6]]),
         ('option_E_boundary_2', [[76.6, 30.0], [57.4, 30.0]]),
         ('option_E_boundary_3', [[55.0, 27.6], [55.0, 8.4]]),
         ('option_E_boundary_4', [[70.3, 18.0], [67.0, 21.3]]),
         ('option_E_boundary_5', [[67.0, 23.7], [69.1, 23.7]]),
         ('option_E_boundary_6', [[69.1, 23.7], [69.1, 26.1]]),
         ('option_E_boundary_7', [[69.1, 26.1], [67.0, 26.1]]),
         ('option_E_boundary_8', [[76.6, 30.0], [79.0, 27.6]]),
         ('option_E_boundary_9', [[70.3, 18.0], [67.0, 14.7]]),
         ('option_E_boundary_10', [[67.0, 12.3], [69.1, 12.3]]),
         ('option_E_boundary_11', [[69.1, 12.3], [69.1, 9.9]]),
         ('option_E_boundary_12', [[69.1, 9.9], [67.0, 9.9]]),
         ('option_E_boundary_13', [[76.6, 6.0], [79.0, 8.4]]),
         ('option_E_boundary_14', [[63.7, 18.0], [67.0, 21.3]]),
         ('option_E_boundary_15', [[67.0, 23.7], [64.9, 23.7]]),
         ('option_E_boundary_16', [[64.9, 23.7], [64.9, 26.1]]),
         ('option_E_boundary_17', [[64.9, 26.1], [67.0, 26.1]]),
         ('option_E_boundary_18', [[57.4, 30.0], [55.0, 27.6]]),
         ('option_E_boundary_19', [[63.7, 18.0], [67.0, 14.7]]),
         ('option_E_boundary_20', [[67.0, 12.3], [64.9, 12.3]]),
         ('option_E_boundary_21', [[64.9, 12.3], [64.9, 9.9]]),
         ('option_E_boundary_22', [[64.9, 9.9], [67.0, 9.9]]),
         ('option_E_boundary_23', [[57.4, 6.0], [55.0, 8.4]])]
        with Canvas(PLANE, xlim=(1.6559000861326467, 98.49456287683032), ylim=(-0.6010443583117961, 96.23761843238587), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
            for object_id, points in [('original_border_0', [[14, 74], [34, 74]]), ('original_border_1', [[34, 74], [34, 94]]), ('original_border_2', [[34, 94], [14, 94]]), ('original_border_3', [[14, 94], [14, 74]])]:
                c.line(points, id=object_id)
            c.line([[24.0, 74.0], [24.0, 94.0]], id='original_fold_0_0', linestyle=(0.0, [4.0, 3.0]))
            c.line([[14.0, 84.0], [34.0, 84.0]], id='original_fold_1_0', linestyle=(0.0, [4.0, 3.0]))
            c.path([[70.0, 79.0], [80.0, 79.0], [80.0, 89.0], [70.0, 89.0], [70.0, 79.0]], [1, 2, 2, 2, 79], id='folded_paper_fill', zorder=1, edgecolor='none', facecolor=(1.0, 1.0, 1.0, 1.0), capstyle='butt')
            for object_id, vertices, codes in [('cut_1_fill', [[70.0, 79.0], [72.75, 79.0], [70.0, 81.75], [70.0, 79.0]], [1, 2, 2, 79]), ('cut_2_fill', [[70.0, 83.75], [71.75, 83.75], [71.75, 85.75], [70.0, 85.75], [70.0, 83.75]], [1, 2, 2, 2, 79]), ('cut_3_fill', [[80.0, 89.0], [78.0, 89.0], [80.0, 87.0], [80.0, 89.0]], [1, 2, 2, 79])]:
                c.path(vertices, codes, id=object_id, zorder=1, edgecolor='none', facecolor=(0.7529411764705882, 0.7529411764705882, 0.7529411764705882, 1.0), capstyle='butt')
            c.line([[70, 79], [80, 79]], id='folded_border_0', color='#EA580C', linewidth=1.5, linestyle=(0.0, [4.0, 3.0]))
            c.line([[80, 79], [80, 89]], id='folded_border_1', color='#EA580C', linewidth=1.5)
            c.line([[80, 89], [70, 89]], id='folded_border_2', color='#EA580C', linewidth=1.5)
            c.line([[70, 89], [70, 79]], id='folded_border_3', color='#EA580C', linewidth=1.5, linestyle=(0.0, [4.0, 3.0]))
            for object_id, points in [('cut_1_path_1', [[72.75, 79.0], [70.0, 81.75]]), ('cut_2_path_0', [[70.0, 83.75], [71.75, 83.75]]), ('cut_2_path_1', [[71.75, 83.75], [71.75, 85.75]]), ('cut_2_path_2', [[71.75, 85.75], [70.0, 85.75]]), ('cut_3_path_1', [[78.0, 89.0], [80.0, 87.0]])]:
                c.line(points, id=object_id, color='#EA580C', linewidth=1.5)
            for object_id, points in [('fold_process_arrow', [[41, 84], [59, 84]]), ('fold_process_arrow_head_1', [[59.0, 84.0], [57.0, 85.1]]), ('fold_process_arrow_head_2', [[59.0, 84.0], [57.0, 82.9]]), ('option_A_boundary_0', [[4.0, 38.0], [28.0, 38.0]]), ('option_A_boundary_1', [[28.0, 38.0], [28.0, 59.6]]), ('option_A_boundary_2', [[25.6, 62.0], [6.4, 62.0]]), ('option_A_boundary_3', [[4.0, 59.6], [4.0, 38.0]]), ('option_A_boundary_4', [[16.0, 50.0], [19.3, 50.0]]), ('option_A_boundary_5', [[19.3, 50.0], [16.0, 53.3]]), ('option_A_boundary_6', [[16.0, 55.7], [18.1, 55.7]]), ('option_A_boundary_7', [[18.1, 55.7], [18.1, 58.1]]), ('option_A_boundary_8', [[18.1, 58.1], [16.0, 58.1]]), ('option_A_boundary_9', [[25.6, 62.0], [28.0, 59.6]]), ('option_A_boundary_10', [[16.0, 50.0], [12.7, 50.0]]), ('option_A_boundary_11', [[12.7, 50.0], [16.0, 53.3]]), ('option_A_boundary_12', [[16.0, 55.7], [13.9, 55.7]]), ('option_A_boundary_13', [[13.9, 55.7], [13.9, 58.1]]), ('option_A_boundary_14', [[13.9, 58.1], [16.0, 58.1]]), ('option_A_boundary_15', [[6.4, 62.0], [4.0, 59.6]])]:
                c.line(points, id=object_id)
            for object_id, points in [('A_fold_0_0', [[16.0, 38.0], [16.0, 50.0]]), ('A_fold_0_2', [[16.0, 53.3], [16.0, 55.7]]), ('A_fold_0_4', [[16.0, 58.1], [16.0, 62.0]]), ('A_fold_1_0', [[4.0, 50.0], [12.7, 50.0]]), ('A_fold_1_3', [[19.3, 50.0], [28.0, 50.0]])]:
                c.line(points, id=object_id, linestyle=(0.0, [4.0, 3.0]))
            for object_id, points in _geometry_01:
                c.line(points, id=object_id)
            for object_id, points in [('B_fold_0_0', [[50.0, 38.0], [50.0, 41.9]]), ('B_fold_0_2', [[50.0, 44.3], [50.0, 46.7]]), ('B_fold_0_5', [[50.0, 53.3], [50.0, 55.7]]), ('B_fold_0_7', [[50.0, 58.1], [50.0, 62.0]]), ('B_fold_1_0', [[38.0, 50.0], [46.7, 50.0]]), ('B_fold_1_3', [[53.3, 50.0], [62.0, 50.0]])]:
                c.line(points, id=object_id, linestyle=(0.0, [4.0, 3.0]))
            for object_id, points in _geometry_02:
                c.line(points, id=object_id, color='#EA580C', linewidth=1.5)
            for object_id, points in [('C_fold_0_0', [[84.0, 38.0], [84.0, 46.7]]), ('C_fold_0_3', [[84.0, 53.3], [84.0, 62.0]]), ('C_fold_1_0', [[72.0, 50.0], [80.7, 50.0]]), ('C_fold_1_3', [[87.3, 50.0], [96.0, 50.0]])]:
                c.line(points, id=object_id, linestyle=(0.0, [4.0, 3.0]))
            for object_id, points in [('option_D_boundary_0', [[21.0, 6.0], [45.0, 6.0]]), ('option_D_boundary_1', [[45.0, 6.0], [45.0, 30.0]]), ('option_D_boundary_2', [[45.0, 30.0], [21.0, 30.0]]), ('option_D_boundary_3', [[21.0, 30.0], [21.0, 6.0]]), ('option_D_boundary_4', [[36.3, 18.0], [33.0, 21.3]]), ('option_D_boundary_5', [[33.0, 23.7], [35.1, 23.7]]), ('option_D_boundary_6', [[35.1, 23.7], [35.1, 26.1]]), ('option_D_boundary_7', [[35.1, 26.1], [33.0, 26.1]]), ('option_D_boundary_8', [[36.3, 18.0], [33.0, 14.7]]), ('option_D_boundary_9', [[33.0, 12.3], [35.1, 12.3]]), ('option_D_boundary_10', [[35.1, 12.3], [35.1, 9.9]]), ('option_D_boundary_11', [[35.1, 9.9], [33.0, 9.9]]), ('option_D_boundary_12', [[29.7, 18.0], [33.0, 21.3]]), ('option_D_boundary_13', [[33.0, 23.7], [30.9, 23.7]]), ('option_D_boundary_14', [[30.9, 23.7], [30.9, 26.1]]), ('option_D_boundary_15', [[30.9, 26.1], [33.0, 26.1]]), ('option_D_boundary_16', [[29.7, 18.0], [33.0, 14.7]]), ('option_D_boundary_17', [[33.0, 12.3], [30.9, 12.3]]), ('option_D_boundary_18', [[30.9, 12.3], [30.9, 9.9]]), ('option_D_boundary_19', [[30.9, 9.9], [33.0, 9.9]])]:
                c.line(points, id=object_id)
            for object_id, points in [('D_fold_0_0', [[33.0, 6.0], [33.0, 9.9]]), ('D_fold_0_2', [[33.0, 12.3], [33.0, 14.7]]), ('D_fold_0_5', [[33.0, 21.3], [33.0, 23.7]]), ('D_fold_0_7', [[33.0, 26.1], [33.0, 30.0]]), ('D_fold_1_0', [[21.0, 18.0], [29.7, 18.0]]), ('D_fold_1_3', [[36.3, 18.0], [45.0, 18.0]])]:
                c.line(points, id=object_id, linestyle=(0.0, [4.0, 3.0]))
            for object_id, points in _geometry_03:
                c.line(points, id=object_id)
            for object_id, points in [('E_fold_0_0', [[67.0, 6.0], [67.0, 9.9]]), ('E_fold_0_2', [[67.0, 12.3], [67.0, 14.7]]), ('E_fold_0_5', [[67.0, 21.3], [67.0, 23.7]]), ('E_fold_0_7', [[67.0, 26.1], [67.0, 30.0]]), ('E_fold_1_0', [[55.0, 18.0], [63.7, 18.0]]), ('E_fold_1_3', [[70.3, 18.0], [79.0, 18.0]])]:
                c.line(points, id=object_id, linestyle=(0.0, [4.0, 3.0]))
            for object_id, text, anchor in [('option_label_A', '(A)', (16, 35)), ('option_label_B', '(B)', (50, 35)), ('option_label_C', '(C)', (84, 35)), ('option_label_D', '(D)', (33, 3)), ('option_label_E', '(E)', (67, 3))]:
                c.text(text, anchor, id=object_id, rotation_mode='default')
            return c.save(output_path)

    def draw_C05(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane548_C05.png'
        _geometry_01 = [('option_B_boundary_0', [[40.4, 38.0], [59.6, 38.0]]),
         ('option_B_boundary_1', [[62.0, 40.4], [62.0, 59.6]]),
         ('option_B_boundary_2', [[59.6, 62.0], [40.4, 62.0]]),
         ('option_B_boundary_3', [[38.0, 59.6], [38.0, 40.4]]),
         ('option_B_boundary_4', [[53.3, 50.0], [53.3, 53.3]]),
         ('option_B_boundary_5', [[53.3, 53.3], [50.0, 53.3]]),
         ('option_B_boundary_6', [[50.0, 55.7], [52.1, 55.7]]),
         ('option_B_boundary_7', [[52.1, 55.7], [52.1, 58.1]]),
         ('option_B_boundary_8', [[52.1, 58.1], [50.0, 58.1]]),
         ('option_B_boundary_9', [[59.6, 62.0], [62.0, 59.6]]),
         ('option_B_boundary_10', [[53.3, 50.0], [53.3, 46.7]]),
         ('option_B_boundary_11', [[53.3, 46.7], [50.0, 46.7]]),
         ('option_B_boundary_12', [[50.0, 44.3], [52.1, 44.3]]),
         ('option_B_boundary_13', [[52.1, 44.3], [52.1, 41.9]]),
         ('option_B_boundary_14', [[52.1, 41.9], [50.0, 41.9]]),
         ('option_B_boundary_15', [[59.6, 38.0], [62.0, 40.4]]),
         ('option_B_boundary_16', [[46.7, 50.0], [46.7, 53.3]]),
         ('option_B_boundary_17', [[46.7, 53.3], [50.0, 53.3]]),
         ('option_B_boundary_18', [[50.0, 55.7], [47.9, 55.7]]),
         ('option_B_boundary_19', [[47.9, 55.7], [47.9, 58.1]]),
         ('option_B_boundary_20', [[47.9, 58.1], [50.0, 58.1]]),
         ('option_B_boundary_21', [[40.4, 62.0], [38.0, 59.6]]),
         ('option_B_boundary_22', [[46.7, 50.0], [46.7, 46.7]]),
         ('option_B_boundary_23', [[46.7, 46.7], [50.0, 46.7]]),
         ('option_B_boundary_24', [[50.0, 44.3], [47.9, 44.3]]),
         ('option_B_boundary_25', [[47.9, 44.3], [47.9, 41.9]]),
         ('option_B_boundary_26', [[47.9, 41.9], [50.0, 41.9]]),
         ('option_B_boundary_27', [[40.4, 38.0], [38.0, 40.4]])]
        _geometry_02 = [('option_C_boundary_0', [[74.4, 38.0], [93.6, 38.0]]),
         ('option_C_boundary_1', [[96.0, 40.4], [96.0, 59.6]]),
         ('option_C_boundary_2', [[93.6, 62.0], [74.4, 62.0]]),
         ('option_C_boundary_3', [[72.0, 59.6], [72.0, 40.4]]),
         ('option_C_boundary_4', [[87.3, 50.0], [84.0, 53.3]]),
         ('option_C_boundary_5', [[85.5, 55.7], [87.6, 55.7]]),
         ('option_C_boundary_6', [[87.6, 55.7], [87.6, 58.1]]),
         ('option_C_boundary_7', [[87.6, 58.1], [85.5, 58.1]]),
         ('option_C_boundary_8', [[85.5, 58.1], [85.5, 55.7]]),
         ('option_C_boundary_9', [[93.6, 62.0], [96.0, 59.6]]),
         ('option_C_boundary_10', [[87.3, 50.0], [84.0, 46.7]]),
         ('option_C_boundary_11', [[85.5, 44.3], [87.6, 44.3]]),
         ('option_C_boundary_12', [[87.6, 44.3], [87.6, 41.9]]),
         ('option_C_boundary_13', [[87.6, 41.9], [85.5, 41.9]]),
         ('option_C_boundary_14', [[85.5, 41.9], [85.5, 44.3]]),
         ('option_C_boundary_15', [[93.6, 38.0], [96.0, 40.4]]),
         ('option_C_boundary_16', [[80.7, 50.0], [84.0, 53.3]]),
         ('option_C_boundary_17', [[82.5, 55.7], [80.4, 55.7]]),
         ('option_C_boundary_18', [[80.4, 55.7], [80.4, 58.1]]),
         ('option_C_boundary_19', [[80.4, 58.1], [82.5, 58.1]]),
         ('option_C_boundary_20', [[82.5, 58.1], [82.5, 55.7]]),
         ('option_C_boundary_21', [[74.4, 62.0], [72.0, 59.6]]),
         ('option_C_boundary_22', [[80.7, 50.0], [84.0, 46.7]]),
         ('option_C_boundary_23', [[82.5, 44.3], [80.4, 44.3]]),
         ('option_C_boundary_24', [[80.4, 44.3], [80.4, 41.9]]),
         ('option_C_boundary_25', [[80.4, 41.9], [82.5, 41.9]]),
         ('option_C_boundary_26', [[82.5, 41.9], [82.5, 44.3]]),
         ('option_C_boundary_27', [[74.4, 38.0], [72.0, 40.4]])]
        _geometry_03 = [('option_E_boundary_0', [[57.4, 6.0], [76.6, 6.0]]),
         ('option_E_boundary_1', [[79.0, 8.4], [79.0, 27.6]]),
         ('option_E_boundary_2', [[76.6, 30.0], [57.4, 30.0]]),
         ('option_E_boundary_3', [[55.0, 27.6], [55.0, 8.4]]),
         ('option_E_boundary_4', [[70.3, 18.0], [67.0, 21.3]]),
         ('option_E_boundary_5', [[67.0, 23.7], [69.1, 23.7]]),
         ('option_E_boundary_6', [[69.1, 23.7], [69.1, 26.1]]),
         ('option_E_boundary_7', [[69.1, 26.1], [67.0, 26.1]]),
         ('option_E_boundary_8', [[76.6, 30.0], [79.0, 27.6]]),
         ('option_E_boundary_9', [[70.3, 18.0], [67.0, 14.7]]),
         ('option_E_boundary_10', [[67.0, 12.3], [69.1, 12.3]]),
         ('option_E_boundary_11', [[69.1, 12.3], [69.1, 9.9]]),
         ('option_E_boundary_12', [[69.1, 9.9], [67.0, 9.9]]),
         ('option_E_boundary_13', [[76.6, 6.0], [79.0, 8.4]]),
         ('option_E_boundary_14', [[63.7, 18.0], [67.0, 21.3]]),
         ('option_E_boundary_15', [[67.0, 23.7], [64.9, 23.7]]),
         ('option_E_boundary_16', [[64.9, 23.7], [64.9, 26.1]]),
         ('option_E_boundary_17', [[64.9, 26.1], [67.0, 26.1]]),
         ('option_E_boundary_18', [[57.4, 30.0], [55.0, 27.6]]),
         ('option_E_boundary_19', [[63.7, 18.0], [67.0, 14.7]]),
         ('option_E_boundary_20', [[67.0, 12.3], [64.9, 12.3]]),
         ('option_E_boundary_21', [[64.9, 12.3], [64.9, 9.9]]),
         ('option_E_boundary_22', [[64.9, 9.9], [67.0, 9.9]]),
         ('option_E_boundary_23', [[57.4, 6.0], [55.0, 8.4]])]
        with Canvas(PLANE, xlim=(1.6559000861326467, 98.49456287683032), ylim=(-0.6010443583117961, 96.23761843238587), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
            for object_id, points in [('original_border_0', [[14, 74], [34, 74]]), ('original_border_1', [[34, 74], [34, 94]]), ('original_border_2', [[34, 94], [14, 94]]), ('original_border_3', [[14, 94], [14, 74]])]:
                c.line(points, id=object_id)
            c.line([[24.0, 74.0], [24.0, 94.0]], id='original_fold_0_0', linestyle=(0.0, [4.0, 3.0]))
            c.line([[14.0, 84.0], [34.0, 84.0]], id='original_fold_1_0', linestyle=(0.0, [4.0, 3.0]))
            c.path([[70.0, 79.0], [80.0, 79.0], [80.0, 89.0], [70.0, 89.0], [70.0, 79.0]], [1, 2, 2, 2, 79], id='folded_paper_fill', zorder=1, edgecolor='none', facecolor=(1.0, 1.0, 1.0, 1.0), capstyle='butt')
            for object_id, vertices, codes in [('cut_1_fill', [[70.0, 79.0], [72.75, 79.0], [70.0, 81.75], [70.0, 79.0]], [1, 2, 2, 79]), ('cut_2_fill', [[70.0, 83.75], [71.75, 83.75], [71.75, 85.75], [70.0, 85.75], [70.0, 83.75]], [1, 2, 2, 2, 79]), ('cut_3_fill', [[80.0, 89.0], [78.0, 89.0], [80.0, 87.0], [80.0, 89.0]], [1, 2, 2, 79])]:
                c.path(vertices, codes, id=object_id, zorder=1, edgecolor='none', facecolor=(0.7529411764705882, 0.7529411764705882, 0.7529411764705882, 1.0), capstyle='butt')
            c.line([[70, 79], [80, 79]], id='folded_border_0', color='#16A34A', linestyle=(0.0, [4.0, 3.0]))
            c.line([[80, 79], [80, 89]], id='folded_border_1', color='#16A34A')
            c.line([[80, 89], [70, 89]], id='folded_border_2', color='#16A34A')
            c.line([[70, 89], [70, 79]], id='folded_border_3', color='#16A34A', linestyle=(0.0, [4.0, 3.0]))
            for object_id, points in [('cut_1_path_1', [[72.75, 79.0], [70.0, 81.75]]), ('cut_2_path_0', [[70.0, 83.75], [71.75, 83.75]]), ('cut_2_path_1', [[71.75, 83.75], [71.75, 85.75]]), ('cut_2_path_2', [[71.75, 85.75], [70.0, 85.75]]), ('cut_3_path_1', [[78.0, 89.0], [80.0, 87.0]])]:
                c.line(points, id=object_id, color='#16A34A')
            for object_id, points in [('fold_process_arrow', [[41, 84], [59, 84]]), ('fold_process_arrow_head_1', [[59.0, 84.0], [57.0, 85.1]]), ('fold_process_arrow_head_2', [[59.0, 84.0], [57.0, 82.9]]), ('option_A_boundary_0', [[4.0, 38.0], [28.0, 38.0]]), ('option_A_boundary_1', [[28.0, 38.0], [28.0, 59.6]]), ('option_A_boundary_2', [[25.6, 62.0], [6.4, 62.0]]), ('option_A_boundary_3', [[4.0, 59.6], [4.0, 38.0]]), ('option_A_boundary_4', [[16.0, 50.0], [19.3, 50.0]]), ('option_A_boundary_5', [[19.3, 50.0], [16.0, 53.3]]), ('option_A_boundary_6', [[16.0, 55.7], [18.1, 55.7]]), ('option_A_boundary_7', [[18.1, 55.7], [18.1, 58.1]]), ('option_A_boundary_8', [[18.1, 58.1], [16.0, 58.1]]), ('option_A_boundary_9', [[25.6, 62.0], [28.0, 59.6]]), ('option_A_boundary_10', [[16.0, 50.0], [12.7, 50.0]]), ('option_A_boundary_11', [[12.7, 50.0], [16.0, 53.3]]), ('option_A_boundary_12', [[16.0, 55.7], [13.9, 55.7]]), ('option_A_boundary_13', [[13.9, 55.7], [13.9, 58.1]]), ('option_A_boundary_14', [[13.9, 58.1], [16.0, 58.1]]), ('option_A_boundary_15', [[6.4, 62.0], [4.0, 59.6]])]:
                c.line(points, id=object_id)
            for object_id, points in [('A_fold_0_0', [[16.0, 38.0], [16.0, 50.0]]), ('A_fold_0_2', [[16.0, 53.3], [16.0, 55.7]]), ('A_fold_0_4', [[16.0, 58.1], [16.0, 62.0]]), ('A_fold_1_0', [[4.0, 50.0], [12.7, 50.0]]), ('A_fold_1_3', [[19.3, 50.0], [28.0, 50.0]])]:
                c.line(points, id=object_id, linestyle=(0.0, [4.0, 3.0]))
            for object_id, points in _geometry_01:
                c.line(points, id=object_id)
            for object_id, points in [('B_fold_0_0', [[50.0, 38.0], [50.0, 41.9]]), ('B_fold_0_2', [[50.0, 44.3], [50.0, 46.7]]), ('B_fold_0_5', [[50.0, 53.3], [50.0, 55.7]]), ('B_fold_0_7', [[50.0, 58.1], [50.0, 62.0]]), ('B_fold_1_0', [[38.0, 50.0], [46.7, 50.0]]), ('B_fold_1_3', [[53.3, 50.0], [62.0, 50.0]])]:
                c.line(points, id=object_id, linestyle=(0.0, [4.0, 3.0]))
            for object_id, points in _geometry_02:
                c.line(points, id=object_id)
            for object_id, points in [('C_fold_0_0', [[84.0, 38.0], [84.0, 46.7]]), ('C_fold_0_3', [[84.0, 53.3], [84.0, 62.0]]), ('C_fold_1_0', [[72.0, 50.0], [80.7, 50.0]]), ('C_fold_1_3', [[87.3, 50.0], [96.0, 50.0]])]:
                c.line(points, id=object_id, linestyle=(0.0, [4.0, 3.0]))
            for object_id, points in [('option_D_boundary_0', [[21.0, 6.0], [45.0, 6.0]]), ('option_D_boundary_1', [[45.0, 6.0], [45.0, 30.0]]), ('option_D_boundary_2', [[45.0, 30.0], [21.0, 30.0]]), ('option_D_boundary_3', [[21.0, 30.0], [21.0, 6.0]]), ('option_D_boundary_4', [[36.3, 18.0], [33.0, 21.3]]), ('option_D_boundary_5', [[33.0, 23.7], [35.1, 23.7]]), ('option_D_boundary_6', [[35.1, 23.7], [35.1, 26.1]]), ('option_D_boundary_7', [[35.1, 26.1], [33.0, 26.1]]), ('option_D_boundary_8', [[36.3, 18.0], [33.0, 14.7]]), ('option_D_boundary_9', [[33.0, 12.3], [35.1, 12.3]]), ('option_D_boundary_10', [[35.1, 12.3], [35.1, 9.9]]), ('option_D_boundary_11', [[35.1, 9.9], [33.0, 9.9]]), ('option_D_boundary_12', [[29.7, 18.0], [33.0, 21.3]]), ('option_D_boundary_13', [[33.0, 23.7], [30.9, 23.7]]), ('option_D_boundary_14', [[30.9, 23.7], [30.9, 26.1]]), ('option_D_boundary_15', [[30.9, 26.1], [33.0, 26.1]]), ('option_D_boundary_16', [[29.7, 18.0], [33.0, 14.7]]), ('option_D_boundary_17', [[33.0, 12.3], [30.9, 12.3]]), ('option_D_boundary_18', [[30.9, 12.3], [30.9, 9.9]]), ('option_D_boundary_19', [[30.9, 9.9], [33.0, 9.9]])]:
                c.line(points, id=object_id, color='#16A34A')
            for object_id, points in [('D_fold_0_0', [[33.0, 6.0], [33.0, 9.9]]), ('D_fold_0_2', [[33.0, 12.3], [33.0, 14.7]]), ('D_fold_0_5', [[33.0, 21.3], [33.0, 23.7]]), ('D_fold_0_7', [[33.0, 26.1], [33.0, 30.0]]), ('D_fold_1_0', [[21.0, 18.0], [29.7, 18.0]]), ('D_fold_1_3', [[36.3, 18.0], [45.0, 18.0]])]:
                c.line(points, id=object_id, linestyle=(0.0, [4.0, 3.0]))
            for object_id, points in _geometry_03:
                c.line(points, id=object_id)
            for object_id, points in [('E_fold_0_0', [[67.0, 6.0], [67.0, 9.9]]), ('E_fold_0_2', [[67.0, 12.3], [67.0, 14.7]]), ('E_fold_0_5', [[67.0, 21.3], [67.0, 23.7]]), ('E_fold_0_7', [[67.0, 26.1], [67.0, 30.0]]), ('E_fold_1_0', [[55.0, 18.0], [63.7, 18.0]]), ('E_fold_1_3', [[70.3, 18.0], [79.0, 18.0]])]:
                c.line(points, id=object_id, linestyle=(0.0, [4.0, 3.0]))
            for object_id, text, anchor in [('option_label_A', '(A)', (16, 35)), ('option_label_B', '(B)', (50, 35)), ('option_label_C', '(C)', (84, 35)), ('option_label_D', '(D)', (33, 3)), ('option_label_E', '(E)', (67, 3))]:
                c.text(text, anchor, id=object_id, rotation_mode='default')
            return c.save(output_path)

    def draw_C06(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane548_C06.png'
        _geometry_01 = [('cut_1_path_1', [[72.75, 79.0], [70.0, 81.75]]),
         ('cut_2_path_0', [[70.0, 83.75], [71.75, 83.75]]),
         ('cut_2_path_1', [[71.75, 83.75], [71.75, 85.75]]),
         ('cut_2_path_2', [[71.75, 85.75], [70.0, 85.75]]),
         ('cut_3_path_1', [[78.0, 89.0], [80.0, 87.0]]),
         ('fold_process_arrow', [[41, 84], [59, 84]]),
         ('fold_process_arrow_head_1', [[59.0, 84.0], [57.0, 85.1]]),
         ('fold_process_arrow_head_2', [[59.0, 84.0], [57.0, 82.9]]),
         ('option_A_boundary_0', [[4.0, 38.0], [28.0, 38.0]]),
         ('option_A_boundary_1', [[28.0, 38.0], [28.0, 59.6]]),
         ('option_A_boundary_2', [[25.6, 62.0], [6.4, 62.0]]),
         ('option_A_boundary_3', [[4.0, 59.6], [4.0, 38.0]]),
         ('option_A_boundary_4', [[16.0, 50.0], [19.3, 50.0]]),
         ('option_A_boundary_5', [[19.3, 50.0], [16.0, 53.3]]),
         ('option_A_boundary_6', [[16.0, 55.7], [18.1, 55.7]]),
         ('option_A_boundary_7', [[18.1, 55.7], [18.1, 58.1]]),
         ('option_A_boundary_8', [[18.1, 58.1], [16.0, 58.1]]),
         ('option_A_boundary_9', [[25.6, 62.0], [28.0, 59.6]]),
         ('option_A_boundary_10', [[16.0, 50.0], [12.7, 50.0]]),
         ('option_A_boundary_11', [[12.7, 50.0], [16.0, 53.3]]),
         ('option_A_boundary_12', [[16.0, 55.7], [13.9, 55.7]]),
         ('option_A_boundary_13', [[13.9, 55.7], [13.9, 58.1]]),
         ('option_A_boundary_14', [[13.9, 58.1], [16.0, 58.1]]),
         ('option_A_boundary_15', [[6.4, 62.0], [4.0, 59.6]])]
        _geometry_02 = [('option_B_boundary_0', [[40.4, 38.0], [59.6, 38.0]]),
         ('option_B_boundary_1', [[62.0, 40.4], [62.0, 59.6]]),
         ('option_B_boundary_2', [[59.6, 62.0], [40.4, 62.0]]),
         ('option_B_boundary_3', [[38.0, 59.6], [38.0, 40.4]]),
         ('option_B_boundary_4', [[53.3, 50.0], [53.3, 53.3]]),
         ('option_B_boundary_5', [[53.3, 53.3], [50.0, 53.3]]),
         ('option_B_boundary_6', [[50.0, 55.7], [52.1, 55.7]]),
         ('option_B_boundary_7', [[52.1, 55.7], [52.1, 58.1]]),
         ('option_B_boundary_8', [[52.1, 58.1], [50.0, 58.1]]),
         ('option_B_boundary_9', [[59.6, 62.0], [62.0, 59.6]]),
         ('option_B_boundary_10', [[53.3, 50.0], [53.3, 46.7]]),
         ('option_B_boundary_11', [[53.3, 46.7], [50.0, 46.7]]),
         ('option_B_boundary_12', [[50.0, 44.3], [52.1, 44.3]]),
         ('option_B_boundary_13', [[52.1, 44.3], [52.1, 41.9]]),
         ('option_B_boundary_14', [[52.1, 41.9], [50.0, 41.9]]),
         ('option_B_boundary_15', [[59.6, 38.0], [62.0, 40.4]]),
         ('option_B_boundary_16', [[46.7, 50.0], [46.7, 53.3]]),
         ('option_B_boundary_17', [[46.7, 53.3], [50.0, 53.3]]),
         ('option_B_boundary_18', [[50.0, 55.7], [47.9, 55.7]]),
         ('option_B_boundary_19', [[47.9, 55.7], [47.9, 58.1]]),
         ('option_B_boundary_20', [[47.9, 58.1], [50.0, 58.1]]),
         ('option_B_boundary_21', [[40.4, 62.0], [38.0, 59.6]]),
         ('option_B_boundary_22', [[46.7, 50.0], [46.7, 46.7]]),
         ('option_B_boundary_23', [[46.7, 46.7], [50.0, 46.7]]),
         ('option_B_boundary_24', [[50.0, 44.3], [47.9, 44.3]]),
         ('option_B_boundary_25', [[47.9, 44.3], [47.9, 41.9]]),
         ('option_B_boundary_26', [[47.9, 41.9], [50.0, 41.9]]),
         ('option_B_boundary_27', [[40.4, 38.0], [38.0, 40.4]])]
        _geometry_03 = [('option_C_boundary_0', [[74.4, 38.0], [93.6, 38.0]]),
         ('option_C_boundary_1', [[96.0, 40.4], [96.0, 59.6]]),
         ('option_C_boundary_2', [[93.6, 62.0], [74.4, 62.0]]),
         ('option_C_boundary_3', [[72.0, 59.6], [72.0, 40.4]]),
         ('option_C_boundary_4', [[87.3, 50.0], [84.0, 53.3]]),
         ('option_C_boundary_5', [[85.5, 55.7], [87.6, 55.7]]),
         ('option_C_boundary_6', [[87.6, 55.7], [87.6, 58.1]]),
         ('option_C_boundary_7', [[87.6, 58.1], [85.5, 58.1]]),
         ('option_C_boundary_8', [[85.5, 58.1], [85.5, 55.7]]),
         ('option_C_boundary_9', [[93.6, 62.0], [96.0, 59.6]]),
         ('option_C_boundary_10', [[87.3, 50.0], [84.0, 46.7]]),
         ('option_C_boundary_11', [[85.5, 44.3], [87.6, 44.3]]),
         ('option_C_boundary_12', [[87.6, 44.3], [87.6, 41.9]]),
         ('option_C_boundary_13', [[87.6, 41.9], [85.5, 41.9]]),
         ('option_C_boundary_14', [[85.5, 41.9], [85.5, 44.3]]),
         ('option_C_boundary_15', [[93.6, 38.0], [96.0, 40.4]]),
         ('option_C_boundary_16', [[80.7, 50.0], [84.0, 53.3]]),
         ('option_C_boundary_17', [[82.5, 55.7], [80.4, 55.7]]),
         ('option_C_boundary_18', [[80.4, 55.7], [80.4, 58.1]]),
         ('option_C_boundary_19', [[80.4, 58.1], [82.5, 58.1]]),
         ('option_C_boundary_20', [[82.5, 58.1], [82.5, 55.7]]),
         ('option_C_boundary_21', [[74.4, 62.0], [72.0, 59.6]]),
         ('option_C_boundary_22', [[80.7, 50.0], [84.0, 46.7]]),
         ('option_C_boundary_23', [[82.5, 44.3], [80.4, 44.3]]),
         ('option_C_boundary_24', [[80.4, 44.3], [80.4, 41.9]]),
         ('option_C_boundary_25', [[80.4, 41.9], [82.5, 41.9]]),
         ('option_C_boundary_26', [[82.5, 41.9], [82.5, 44.3]]),
         ('option_C_boundary_27', [[74.4, 38.0], [72.0, 40.4]])]
        _geometry_04 = [('option_E_boundary_0', [[57.4, 6.0], [76.6, 6.0]]),
         ('option_E_boundary_1', [[79.0, 8.4], [79.0, 27.6]]),
         ('option_E_boundary_2', [[76.6, 30.0], [57.4, 30.0]]),
         ('option_E_boundary_3', [[55.0, 27.6], [55.0, 8.4]]),
         ('option_E_boundary_4', [[70.3, 18.0], [67.0, 21.3]]),
         ('option_E_boundary_5', [[67.0, 23.7], [69.1, 23.7]]),
         ('option_E_boundary_6', [[69.1, 23.7], [69.1, 26.1]]),
         ('option_E_boundary_7', [[69.1, 26.1], [67.0, 26.1]]),
         ('option_E_boundary_8', [[76.6, 30.0], [79.0, 27.6]]),
         ('option_E_boundary_9', [[70.3, 18.0], [67.0, 14.7]]),
         ('option_E_boundary_10', [[67.0, 12.3], [69.1, 12.3]]),
         ('option_E_boundary_11', [[69.1, 12.3], [69.1, 9.9]]),
         ('option_E_boundary_12', [[69.1, 9.9], [67.0, 9.9]]),
         ('option_E_boundary_13', [[76.6, 6.0], [79.0, 8.4]]),
         ('option_E_boundary_14', [[63.7, 18.0], [67.0, 21.3]]),
         ('option_E_boundary_15', [[67.0, 23.7], [64.9, 23.7]]),
         ('option_E_boundary_16', [[64.9, 23.7], [64.9, 26.1]]),
         ('option_E_boundary_17', [[64.9, 26.1], [67.0, 26.1]]),
         ('option_E_boundary_18', [[57.4, 30.0], [55.0, 27.6]]),
         ('option_E_boundary_19', [[63.7, 18.0], [67.0, 14.7]]),
         ('option_E_boundary_20', [[67.0, 12.3], [64.9, 12.3]]),
         ('option_E_boundary_21', [[64.9, 12.3], [64.9, 9.9]]),
         ('option_E_boundary_22', [[64.9, 9.9], [67.0, 9.9]]),
         ('option_E_boundary_23', [[57.4, 6.0], [55.0, 8.4]])]
        with Canvas(PLANE, xlim=(1.6559000861326467, 98.49456287683032), ylim=(-0.6010443583117961, 96.23761843238587), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
            for object_id, points in [('original_border_0', [[14, 74], [34, 74]]), ('original_border_1', [[34, 74], [34, 94]]), ('original_border_2', [[34, 94], [14, 94]]), ('original_border_3', [[14, 94], [14, 74]])]:
                c.line(points, id=object_id)
            c.line([[24.0, 74.0], [24.0, 94.0]], id='original_fold_0_0', linestyle=(0.0, [4.0, 3.0]))
            c.line([[14.0, 84.0], [34.0, 84.0]], id='original_fold_1_0', linestyle=(0.0, [4.0, 3.0]))
            c.path([[70.0, 79.0], [80.0, 79.0], [80.0, 89.0], [70.0, 89.0], [70.0, 79.0]], [1, 2, 2, 2, 79], id='folded_paper_fill', zorder=1, edgecolor='none', facecolor=(1.0, 1.0, 1.0, 1.0), capstyle='butt')
            for object_id, vertices, codes in [('cut_1_fill', [[70.0, 79.0], [72.75, 79.0], [70.0, 81.75], [70.0, 79.0]], [1, 2, 2, 79]), ('cut_2_fill', [[70.0, 83.75], [71.75, 83.75], [71.75, 85.75], [70.0, 85.75], [70.0, 83.75]], [1, 2, 2, 2, 79]), ('cut_3_fill', [[80.0, 89.0], [78.0, 89.0], [80.0, 87.0], [80.0, 89.0]], [1, 2, 2, 79])]:
                c.path(vertices, codes, id=object_id, zorder=1, edgecolor='none', facecolor=(0.7529411764705882, 0.7529411764705882, 0.7529411764705882, 1.0), capstyle='butt')
            c.line([[70, 79], [80, 79]], id='folded_border_0', linestyle=(0.0, [4.0, 3.0]))
            c.line([[80, 79], [80, 89]], id='folded_border_1')
            c.line([[80, 89], [70, 89]], id='folded_border_2')
            c.line([[70, 89], [70, 79]], id='folded_border_3', linestyle=(0.0, [4.0, 3.0]))
            for object_id, points in _geometry_01:
                c.line(points, id=object_id)
            for object_id, points in [('A_fold_0_0', [[16.0, 38.0], [16.0, 50.0]]), ('A_fold_0_2', [[16.0, 53.3], [16.0, 55.7]]), ('A_fold_0_4', [[16.0, 58.1], [16.0, 62.0]]), ('A_fold_1_0', [[4.0, 50.0], [12.7, 50.0]]), ('A_fold_1_3', [[19.3, 50.0], [28.0, 50.0]])]:
                c.line(points, id=object_id, linestyle=(0.0, [4.0, 3.0]))
            for object_id, points in _geometry_02:
                c.line(points, id=object_id)
            for object_id, points in [('B_fold_0_0', [[50.0, 38.0], [50.0, 41.9]]), ('B_fold_0_2', [[50.0, 44.3], [50.0, 46.7]]), ('B_fold_0_5', [[50.0, 53.3], [50.0, 55.7]]), ('B_fold_0_7', [[50.0, 58.1], [50.0, 62.0]]), ('B_fold_1_0', [[38.0, 50.0], [46.7, 50.0]]), ('B_fold_1_3', [[53.3, 50.0], [62.0, 50.0]])]:
                c.line(points, id=object_id, linestyle=(0.0, [4.0, 3.0]))
            for object_id, points in _geometry_03:
                c.line(points, id=object_id)
            for object_id, points in [('C_fold_0_0', [[84.0, 38.0], [84.0, 46.7]]), ('C_fold_0_3', [[84.0, 53.3], [84.0, 62.0]]), ('C_fold_1_0', [[72.0, 50.0], [80.7, 50.0]]), ('C_fold_1_3', [[87.3, 50.0], [96.0, 50.0]])]:
                c.line(points, id=object_id, linestyle=(0.0, [4.0, 3.0]))
            for object_id, points in [('option_D_boundary_0', [[21.0, 6.0], [45.0, 6.0]]), ('option_D_boundary_1', [[45.0, 6.0], [45.0, 30.0]]), ('option_D_boundary_2', [[45.0, 30.0], [21.0, 30.0]]), ('option_D_boundary_3', [[21.0, 30.0], [21.0, 6.0]]), ('option_D_boundary_4', [[36.3, 18.0], [33.0, 21.3]]), ('option_D_boundary_5', [[33.0, 23.7], [35.1, 23.7]]), ('option_D_boundary_6', [[35.1, 23.7], [35.1, 26.1]]), ('option_D_boundary_7', [[35.1, 26.1], [33.0, 26.1]]), ('option_D_boundary_8', [[36.3, 18.0], [33.0, 14.7]]), ('option_D_boundary_9', [[33.0, 12.3], [35.1, 12.3]]), ('option_D_boundary_10', [[35.1, 12.3], [35.1, 9.9]]), ('option_D_boundary_11', [[35.1, 9.9], [33.0, 9.9]]), ('option_D_boundary_12', [[29.7, 18.0], [33.0, 21.3]]), ('option_D_boundary_13', [[33.0, 23.7], [30.9, 23.7]]), ('option_D_boundary_14', [[30.9, 23.7], [30.9, 26.1]]), ('option_D_boundary_15', [[30.9, 26.1], [33.0, 26.1]]), ('option_D_boundary_16', [[29.7, 18.0], [33.0, 14.7]]), ('option_D_boundary_17', [[33.0, 12.3], [30.9, 12.3]]), ('option_D_boundary_18', [[30.9, 12.3], [30.9, 9.9]]), ('option_D_boundary_19', [[30.9, 9.9], [33.0, 9.9]])]:
                c.line(points, id=object_id, color='#2563EB')
            for object_id, points in [('D_fold_0_0', [[33.0, 6.0], [33.0, 9.9]]), ('D_fold_0_2', [[33.0, 12.3], [33.0, 14.7]]), ('D_fold_0_5', [[33.0, 21.3], [33.0, 23.7]]), ('D_fold_0_7', [[33.0, 26.1], [33.0, 30.0]]), ('D_fold_1_0', [[21.0, 18.0], [29.7, 18.0]]), ('D_fold_1_3', [[36.3, 18.0], [45.0, 18.0]])]:
                c.line(points, id=object_id, linestyle=(0.0, [4.0, 3.0]))
            for object_id, points in _geometry_04:
                c.line(points, id=object_id)
            for object_id, points in [('E_fold_0_0', [[67.0, 6.0], [67.0, 9.9]]), ('E_fold_0_2', [[67.0, 12.3], [67.0, 14.7]]), ('E_fold_0_5', [[67.0, 21.3], [67.0, 23.7]]), ('E_fold_0_7', [[67.0, 26.1], [67.0, 30.0]]), ('E_fold_1_0', [[55.0, 18.0], [63.7, 18.0]]), ('E_fold_1_3', [[70.3, 18.0], [79.0, 18.0]])]:
                c.line(points, id=object_id, linestyle=(0.0, [4.0, 3.0]))
            for object_id, text, anchor in [('option_label_A', '(A)', (16, 35)), ('option_label_B', '(B)', (50, 35)), ('option_label_C', '(C)', (84, 35)), ('option_label_D', '(D)', (33, 3)), ('option_label_E', '(E)', (67, 3))]:
                c.text(text, anchor, id=object_id, rotation_mode='default')
            return c.save(output_path)
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Plane548')
    parser.add_argument('output', nargs='?')
    parser.add_argument('--variant', choices=('C01', 'C02', 'C03', 'C04', 'C05', 'C06'))
    args = parser.parse_args()
    print(Plane548().draw(args.output, variant=args.variant))
