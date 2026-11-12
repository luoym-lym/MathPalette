"""Frozen question Plane549; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane549:

    def __init__(self):
        self.id = 'Plane549'
        self.source_dataset = 'Author Designed'
        self.source_key = 'author-extensions95-v1:Plane220/extension_05'
        self.question = 'A piece of paper is folded exactly in half, and a figure is cut out as shown.\nWhich of the five pictures can result when the paper is unfolded?\nChoices:\nA:A\nB:B\nC:C\nD:D\nE:E'
        self.answer = 'C'
        self.answer_type = 'choice'
        self.choices = {'A': 'A', 'B': 'B', 'C': 'C', 'D': 'D', 'E': 'E'}
        self.query = self.question
        self._geometry_01 = [('cut_1_path_1', [[77.25, 86.25], [78.0, 81.0]]),
         ('cut_1_path_2', [[78.0, 81.0], [72.75, 81.75]]),
         ('cut_2_path_1', [[71.75, 74.0], [70.0, 76.75]]),
         ('cut_2_path_2', [[70.0, 76.75], [68.25, 74.0]]),
         ('cut_3_path_0', [[80.0, 77.5], [82.25, 77.5]]),
         ('cut_3_path_1', [[82.25, 77.5], [81.0, 79.5]]),
         ('cut_3_path_2', [[81.0, 79.5], [80.0, 77.5]]),
         ('fold_process_arrow', [[41, 84], [59, 84]]),
         ('fold_process_arrow_head_1', [[59.0, 84.0], [57.0, 85.1]]),
         ('fold_process_arrow_head_2', [[59.0, 84.0], [57.0, 82.9]]),
         ('option_A_boundary_0', [[4.0, 38.0], [7.9, 38.0]]),
         ('option_A_boundary_1', [[12.1, 38.0], [19.9, 38.0]]),
         ('option_A_boundary_2', [[24.1, 38.0], [28.0, 38.0]]),
         ('option_A_boundary_3', [[28.0, 38.0], [28.0, 62.0]]),
         ('option_A_boundary_4', [[28.0, 62.0], [4.0, 62.0]]),
         ('option_A_boundary_5', [[4.0, 62.0], [4.0, 38.0]]),
         ('option_A_boundary_6', [[16.0, 50.0], [18.7, 52.7]]),
         ('option_A_boundary_7', [[18.7, 52.7], [19.6, 46.4]]),
         ('option_A_boundary_8', [[19.6, 46.4], [16.0, 46.9142857142]]),
         ('option_A_boundary_9', [[12.1, 38.0], [10.0, 41.3]]),
         ('option_A_boundary_10', [[10.0, 41.3], [7.9, 38.0]]),
         ('option_A_boundary_11', [[22.0, 42.2], [24.7, 42.2]]),
         ('option_A_boundary_12', [[24.7, 42.2], [23.2, 44.6]]),
         ('option_A_boundary_13', [[23.2, 44.6], [22.0, 42.2]]),
         ('option_A_boundary_14', [[16.0, 50.0], [13.3, 52.7]]),
         ('option_A_boundary_15', [[13.3, 52.7], [12.4, 46.4]]),
         ('option_A_boundary_16', [[12.4, 46.4], [16.0, 46.9142857142]]),
         ('option_A_boundary_17', [[19.9, 38.0], [22.0, 41.3]]),
         ('option_A_boundary_18', [[22.0, 41.3], [24.1, 38.0]]),
         ('option_A_boundary_19', [[10.0, 42.2], [7.3, 42.2]]),
         ('option_A_boundary_20', [[7.3, 42.2], [8.8, 44.6]]),
         ('option_A_boundary_21', [[8.8, 44.6], [10.0, 42.2]])]
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane549.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[1.6559000861326467, 98.49456287683032], ylim=[-0.6010443583117961, 96.23761843238587], axes_position=[0.05, 0.05, 0.9, 0.9], coordinate_axes=False) as c:
            for object_id, points in [('original_border_0', [[14, 74], [34, 74]]), ('original_border_1', [[34, 74], [34, 94]]), ('original_border_2', [[34, 94], [14, 94]]), ('original_border_3', [[14, 94], [14, 74]])]:
                c.line(points, id=object_id)
            c.line([[14, 74], [34, 94]], id='original_fold_0_0', linestyle=(0.0, [4.0, 3.0]))
            c.path([[65.0, 74.0], [85.0, 74.0], [85.0, 94.0], [65.0, 74.0]], [1, 2, 2, 79], id='folded_paper_fill', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], capstyle='butt')
            for object_id, vertices, codes in [('cut_1_fill', [[72.75, 81.75], [77.25, 86.25], [78.0, 81.0], [72.75, 81.75]], [1, 2, 2, 79]), ('cut_2_fill', [[68.25, 74.0], [71.75, 74.0], [70.0, 76.75], [68.25, 74.0]], [1, 2, 2, 79]), ('cut_3_fill', [[80.0, 77.5], [82.25, 77.5], [81.0, 79.5], [80.0, 77.5]], [1, 2, 2, 79])]:
                c.path(vertices, codes, id=object_id, zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.7529411764705882, 0.7529411764705882, 0.7529411764705882, 1.0], capstyle='butt')
            c.line([[65, 74], [85, 74]], id='folded_border_0')
            c.line([[85, 74], [85, 94]], id='folded_border_1')
            c.line([[85, 94], [65, 74]], id='folded_border_2', linestyle=(0.0, [4.0, 3.0]))
            for object_id, points in self._geometry_01:
                c.line(points, id=object_id)
            for object_id, points in [('A_fold_0_0', [[4.0, 38.0], [8.2, 42.2]]), ('A_fold_0_2', [[9.4, 43.4], [12.4, 46.4]]), ('A_fold_0_5', [[18.7, 52.7], [28.0, 62.0]])]:
                c.line(points, id=object_id, linestyle=(0.0, [4.0, 3.0]))
            for object_id, points in [('option_B_boundary_0', [[38.0, 38.0], [41.9, 38.0]]), ('option_B_boundary_1', [[46.1, 38.0], [62.0, 38.0]]), ('option_B_boundary_2', [[62.0, 38.0], [62.0, 62.0]]), ('option_B_boundary_3', [[62.0, 62.0], [38.0, 62.0]]), ('option_B_boundary_4', [[38.0, 62.0], [38.0, 38.0]]), ('option_B_boundary_5', [[47.3, 47.3], [52.7, 52.7]]), ('option_B_boundary_6', [[52.7, 52.7], [53.6, 46.4]]), ('option_B_boundary_7', [[53.6, 46.4], [47.3, 47.3]]), ('option_B_boundary_8', [[46.1, 38.0], [44.0, 41.3]]), ('option_B_boundary_9', [[44.0, 41.3], [41.9, 38.0]]), ('option_B_boundary_10', [[56.0, 42.2], [58.7, 42.2]]), ('option_B_boundary_11', [[58.7, 42.2], [57.2, 44.6]]), ('option_B_boundary_12', [[57.2, 44.6], [56.0, 42.2]])]:
                c.line(points, id=object_id)
            c.line([[38.0, 38.0], [52.7, 52.7]], id='B_fold_0_0', linestyle=(0.0, [4.0, 3.0]))
            c.line([[52.7, 52.7], [62.0, 62.0]], id='B_fold_0_1', linestyle=(0.0, [4.0, 3.0]))
            for object_id, points in [('option_C_boundary_0', [[72.0, 38.0], [75.9, 38.0]]), ('option_C_boundary_1', [[80.1, 38.0], [96.0, 38.0]]), ('option_C_boundary_2', [[96.0, 38.0], [96.0, 62.0]]), ('option_C_boundary_3', [[96.0, 62.0], [72.0, 62.0]]), ('option_C_boundary_4', [[72.0, 62.0], [72.0, 46.1]]), ('option_C_boundary_5', [[72.0, 41.9], [72.0, 38.0]]), ('option_C_boundary_6', [[86.7, 52.7], [87.6, 46.4]]), ('option_C_boundary_7', [[87.6, 46.4], [81.3, 47.3]]), ('option_C_boundary_8', [[80.1, 38.0], [78.0, 41.3]]), ('option_C_boundary_9', [[78.0, 41.3], [75.9, 38.0]]), ('option_C_boundary_10', [[90.0, 42.2], [92.7, 42.2]]), ('option_C_boundary_11', [[92.7, 42.2], [91.2, 44.6]]), ('option_C_boundary_12', [[91.2, 44.6], [90.0, 42.2]]), ('option_C_boundary_13', [[86.7, 52.7], [80.4, 53.6]]), ('option_C_boundary_14', [[80.4, 53.6], [81.3, 47.3]]), ('option_C_boundary_15', [[72.0, 46.1], [75.3, 44.0]]), ('option_C_boundary_16', [[75.3, 44.0], [72.0, 41.9]]), ('option_C_boundary_17', [[76.2, 56.0], [76.2, 58.7]]), ('option_C_boundary_18', [[76.2, 58.7], [78.6, 57.2]]), ('option_C_boundary_19', [[78.6, 57.2], [76.2, 56.0]])]:
                c.line(points, id=object_id)
            c.line([[72.0, 38.0], [86.7, 52.7]], id='C_fold_0_0', linestyle=(0.0, [4.0, 3.0]))
            c.line([[86.7, 52.7], [96.0, 62.0]], id='C_fold_0_1', linestyle=(0.0, [4.0, 3.0]))
            for object_id, points in [('option_D_boundary_0', [[21.0, 6.0], [24.9, 6.0]]), ('option_D_boundary_1', [[29.1, 6.0], [45.0, 6.0]]), ('option_D_boundary_2', [[45.0, 6.0], [45.0, 30.0]]), ('option_D_boundary_3', [[45.0, 30.0], [21.0, 30.0]]), ('option_D_boundary_4', [[21.0, 30.0], [21.0, 14.1]]), ('option_D_boundary_5', [[21.0, 9.9], [21.0, 6.0]]), ('option_D_boundary_6', [[30.3, 15.3], [35.7, 20.7]]), ('option_D_boundary_7', [[35.7, 20.7], [36.6, 14.4]]), ('option_D_boundary_8', [[36.6, 14.4], [30.3, 15.3]]), ('option_D_boundary_9', [[29.1, 6.0], [27.0, 9.3]]), ('option_D_boundary_10', [[27.0, 9.3], [24.9, 6.0]]), ('option_D_boundary_11', [[39.0, 10.2], [41.7, 10.2]]), ('option_D_boundary_12', [[41.7, 10.2], [40.2, 12.6]]), ('option_D_boundary_13', [[40.2, 12.6], [39.0, 10.2]]), ('option_D_boundary_14', [[21.0, 14.1], [24.3, 12.0]]), ('option_D_boundary_15', [[24.3, 12.0], [21.0, 9.9]]), ('option_D_boundary_16', [[25.2, 24.0], [25.2, 26.7]]), ('option_D_boundary_17', [[25.2, 26.7], [27.6, 25.2]]), ('option_D_boundary_18', [[27.6, 25.2], [25.2, 24.0]])]:
                c.line(points, id=object_id)
            c.line([[21.0, 6.0], [35.7, 20.7]], id='D_fold_0_0', linestyle=(0.0, [4.0, 3.0]))
            c.line([[35.7, 20.7], [45.0, 30.0]], id='D_fold_0_1', linestyle=(0.0, [4.0, 3.0]))
            for object_id, points in [('option_E_boundary_0', [[55.0, 6.0], [58.9, 6.0]]), ('option_E_boundary_1', [[63.1, 6.0], [79.0, 6.0]]), ('option_E_boundary_2', [[79.0, 6.0], [79.0, 30.0]]), ('option_E_boundary_3', [[79.0, 30.0], [55.0, 30.0]]), ('option_E_boundary_4', [[55.0, 30.0], [55.0, 26.1]]), ('option_E_boundary_5', [[55.0, 21.9], [55.0, 6.0]]), ('option_E_boundary_6', [[69.7, 20.7], [70.6, 14.4]]), ('option_E_boundary_7', [[70.6, 14.4], [64.3, 15.3]]), ('option_E_boundary_8', [[73.0, 10.2], [75.7, 10.2]]), ('option_E_boundary_9', [[75.7, 10.2], [74.2, 12.6]]), ('option_E_boundary_10', [[74.2, 12.6], [73.0, 10.2]]), ('option_E_boundary_11', [[69.7, 20.7], [63.4, 21.6]]), ('option_E_boundary_12', [[63.4, 21.6], [64.3, 15.3]]), ('option_E_boundary_13', [[59.2, 24.0], [59.2, 26.7]]), ('option_E_boundary_14', [[59.2, 26.7], [61.6, 25.2]]), ('option_E_boundary_15', [[61.6, 25.2], [59.2, 24.0]]), ('option_E_boundary_16', [[63.1, 6.0], [61.0, 9.3]]), ('option_E_boundary_17', [[61.0, 9.3], [58.9, 6.0]]), ('option_E_boundary_18', [[55.0, 26.1], [58.3, 24.0]]), ('option_E_boundary_19', [[58.3, 24.0], [55.0, 21.9]])]:
                c.line(points, id=object_id)
            c.line([[55.0, 6.0], [69.7, 20.7]], id='E_fold_0_0', linestyle=(0.0, [4.0, 3.0]))
            c.line([[69.7, 20.7], [79.0, 30.0]], id='E_fold_0_1', linestyle=(0.0, [4.0, 3.0]))
            for object_id, text, anchor in [('option_label_A', '(A)', [16, 35]), ('option_label_B', '(B)', [50, 35]), ('option_label_C', '(C)', [84, 35]), ('option_label_D', '(D)', [33, 3]), ('option_label_E', '(E)', [67, 3])]:
                c.text(text, anchor, id=object_id, rotation_mode='default')
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane549().draw(sys.argv[1] if len(sys.argv) > 1 else None))
