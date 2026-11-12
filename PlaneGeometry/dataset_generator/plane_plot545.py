"""Frozen question Plane545; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane545:

    def __init__(self):
        self.id = 'Plane545'
        self.source_dataset = 'Author Designed'
        self.source_key = 'author-extensions95-v1:Plane220/extension_01'
        self.question = 'A piece of paper is folded exactly in half, and a figure is cut out as shown.\nWhich of the five pictures can result when the paper is unfolded?\nChoices:\nA:A\nB:B\nC:C\nD:D\nE:E'
        self.answer = 'B'
        self.answer_type = 'choice'
        self.choices = {'A': 'A', 'B': 'B', 'C': 'C', 'D': 'D', 'E': 'E'}
        self.query = self.question
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane545.json'

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
            c.line([[24.0, 74.0], [24.0, 94.0]], id='original_fold_0_0', linestyle=(0.0, [4.0, 3.0]))
            c.path([[70.0, 74.0], [80.0, 74.0], [80.0, 94.0], [70.0, 94.0], [70.0, 74.0]], [1, 2, 2, 2, 79], id='folded_paper_fill', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], capstyle='butt')
            c.path([[70.0, 80.0], [72.75, 80.0], [72.75, 82.25], [75.75, 82.25], [75.75, 85.75], [72.75, 85.75], [72.75, 88.0], [70.0, 88.0], [70.0, 80.0]], [1, 2, 2, 2, 2, 2, 2, 2, 79], id='cut_1_fill', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.7529411764705882, 0.7529411764705882, 0.7529411764705882, 1.0], capstyle='butt')
            for object_id, points in [('folded_border_0', [[70, 74], [80, 74]]), ('folded_border_1', [[80, 74], [80, 94]]), ('folded_border_2', [[80, 94], [70, 94]])]:
                c.line(points, id=object_id)
            c.line([[70, 94], [70, 74]], id='folded_border_3', linestyle=(0.0, [4.0, 3.0]))
            for object_id, points in [('cut_1_path_0', [[70.0, 80.0], [72.75, 80.0]]), ('cut_1_path_1', [[72.75, 80.0], [72.75, 82.25]]), ('cut_1_path_2', [[72.75, 82.25], [75.75, 82.25]]), ('cut_1_path_3', [[75.75, 82.25], [75.75, 85.75]]), ('cut_1_path_4', [[75.75, 85.75], [72.75, 85.75]]), ('cut_1_path_5', [[72.75, 85.75], [72.75, 88.0]]), ('cut_1_path_6', [[72.75, 88.0], [70.0, 88.0]]), ('fold_process_arrow', [[41, 84], [59, 84]]), ('fold_process_arrow_head_1', [[59.0, 84.0], [57.0, 85.1]]), ('fold_process_arrow_head_2', [[59.0, 84.0], [57.0, 82.9]]), ('option_A_boundary_0', [[4.0, 38.0], [28.0, 38.0]]), ('option_A_boundary_1', [[28.0, 38.0], [28.0, 62.0]]), ('option_A_boundary_2', [[28.0, 62.0], [4.0, 62.0]]), ('option_A_boundary_3', [[4.0, 62.0], [4.0, 38.0]]), ('option_A_boundary_4', [[16.0, 45.2], [19.3, 45.2]]), ('option_A_boundary_5', [[19.3, 45.2], [19.3, 47.9]]), ('option_A_boundary_6', [[19.3, 47.9], [22.9, 47.9]]), ('option_A_boundary_7', [[22.9, 47.9], [22.9, 52.1]]), ('option_A_boundary_8', [[22.9, 52.1], [19.3, 52.1]]), ('option_A_boundary_9', [[19.3, 52.1], [19.3, 54.8]]), ('option_A_boundary_10', [[19.3, 54.8], [16.0, 54.8]]), ('option_A_boundary_11', [[16.0, 54.8], [16.0, 45.2]])]:
                c.line(points, id=object_id)
            c.line([[16.0, 38.0], [16.0, 45.2]], id='A_fold_0_0', linestyle=(0.0, [4.0, 3.0]))
            c.line([[16.0, 54.8], [16.0, 62.0]], id='A_fold_0_2', linestyle=(0.0, [4.0, 3.0]))
            for object_id, points in [('option_B_boundary_0', [[38.0, 38.0], [62.0, 38.0]]), ('option_B_boundary_1', [[62.0, 38.0], [62.0, 62.0]]), ('option_B_boundary_2', [[62.0, 62.0], [38.0, 62.0]]), ('option_B_boundary_3', [[38.0, 62.0], [38.0, 38.0]]), ('option_B_boundary_4', [[50.0, 45.2], [53.3, 45.2]]), ('option_B_boundary_5', [[53.3, 45.2], [53.3, 47.9]]), ('option_B_boundary_6', [[53.3, 47.9], [56.9, 47.9]]), ('option_B_boundary_7', [[56.9, 47.9], [56.9, 52.1]]), ('option_B_boundary_8', [[56.9, 52.1], [53.3, 52.1]]), ('option_B_boundary_9', [[53.3, 52.1], [53.3, 54.8]]), ('option_B_boundary_10', [[53.3, 54.8], [50.0, 54.8]]), ('option_B_boundary_11', [[50.0, 45.2], [46.7, 45.2]]), ('option_B_boundary_12', [[46.7, 45.2], [46.7, 47.9]]), ('option_B_boundary_13', [[46.7, 47.9], [43.1, 47.9]]), ('option_B_boundary_14', [[43.1, 47.9], [43.1, 52.1]]), ('option_B_boundary_15', [[43.1, 52.1], [46.7, 52.1]]), ('option_B_boundary_16', [[46.7, 52.1], [46.7, 54.8]]), ('option_B_boundary_17', [[46.7, 54.8], [50.0, 54.8]])]:
                c.line(points, id=object_id)
            c.line([[50.0, 38.0], [50.0, 45.2]], id='B_fold_0_0', linestyle=(0.0, [4.0, 3.0]))
            c.line([[50.0, 54.8], [50.0, 62.0]], id='B_fold_0_2', linestyle=(0.0, [4.0, 3.0]))
            for object_id, points in [('option_C_boundary_0', [[72.0, 38.0], [96.0, 38.0]]), ('option_C_boundary_1', [[96.0, 38.0], [96.0, 62.0]]), ('option_C_boundary_2', [[96.0, 62.0], [72.0, 62.0]]), ('option_C_boundary_3', [[72.0, 62.0], [72.0, 38.0]]), ('option_C_boundary_4', [[77.1, 45.2], [90.9, 45.2]]), ('option_C_boundary_5', [[90.9, 45.2], [90.9, 54.8]]), ('option_C_boundary_6', [[90.9, 54.8], [77.1, 54.8]]), ('option_C_boundary_7', [[77.1, 54.8], [77.1, 45.2]])]:
                c.line(points, id=object_id)
            c.line([[84.0, 38.0], [84.0, 45.2]], id='C_fold_0_0', linestyle=(0.0, [4.0, 3.0]))
            c.line([[84.0, 54.8], [84.0, 62.0]], id='C_fold_0_2', linestyle=(0.0, [4.0, 3.0]))
            for object_id, points in [('option_D_boundary_0', [[21.0, 6.0], [45.0, 6.0]]), ('option_D_boundary_1', [[45.0, 6.0], [45.0, 30.0]]), ('option_D_boundary_2', [[45.0, 30.0], [21.0, 30.0]]), ('option_D_boundary_3', [[21.0, 30.0], [21.0, 6.0]]), ('option_D_boundary_4', [[34.8, 13.2], [38.1, 13.2]]), ('option_D_boundary_5', [[38.1, 13.2], [38.1, 15.9]]), ('option_D_boundary_6', [[38.1, 15.9], [41.7, 15.9]]), ('option_D_boundary_7', [[41.7, 15.9], [41.7, 20.1]]), ('option_D_boundary_8', [[41.7, 20.1], [38.1, 20.1]]), ('option_D_boundary_9', [[38.1, 20.1], [38.1, 22.8]]), ('option_D_boundary_10', [[38.1, 22.8], [34.8, 22.8]]), ('option_D_boundary_11', [[34.8, 22.8], [34.8, 13.2]]), ('option_D_boundary_12', [[31.2, 13.2], [27.9, 13.2]]), ('option_D_boundary_13', [[27.9, 13.2], [27.9, 15.9]]), ('option_D_boundary_14', [[27.9, 15.9], [24.3, 15.9]]), ('option_D_boundary_15', [[24.3, 15.9], [24.3, 20.1]]), ('option_D_boundary_16', [[24.3, 20.1], [27.9, 20.1]]), ('option_D_boundary_17', [[27.9, 20.1], [27.9, 22.8]]), ('option_D_boundary_18', [[27.9, 22.8], [31.2, 22.8]]), ('option_D_boundary_19', [[31.2, 22.8], [31.2, 13.2]])]:
                c.line(points, id=object_id)
            c.line([[33.0, 6.0], [33.0, 30.0]], id='D_fold_0_0', linestyle=(0.0, [4.0, 3.0]))
            for object_id, points in [('option_E_boundary_0', [[55.0, 6.0], [79.0, 6.0]]), ('option_E_boundary_1', [[79.0, 6.0], [79.0, 15.9]]), ('option_E_boundary_2', [[79.0, 20.1], [79.0, 30.0]]), ('option_E_boundary_3', [[79.0, 30.0], [55.0, 30.0]]), ('option_E_boundary_4', [[55.0, 30.0], [55.0, 20.1]]), ('option_E_boundary_5', [[55.0, 15.9], [55.0, 6.0]]), ('option_E_boundary_6', [[72.1, 13.2], [75.4, 13.2]]), ('option_E_boundary_7', [[75.4, 13.2], [75.4, 15.9]]), ('option_E_boundary_8', [[75.4, 15.9], [79.0, 15.9]]), ('option_E_boundary_9', [[79.0, 20.1], [75.4, 20.1]]), ('option_E_boundary_10', [[75.4, 20.1], [75.4, 22.8]]), ('option_E_boundary_11', [[75.4, 22.8], [72.1, 22.8]]), ('option_E_boundary_12', [[72.1, 22.8], [72.1, 13.2]]), ('option_E_boundary_13', [[61.9, 13.2], [58.6, 13.2]]), ('option_E_boundary_14', [[58.6, 13.2], [58.6, 15.9]]), ('option_E_boundary_15', [[58.6, 15.9], [55.0, 15.9]]), ('option_E_boundary_16', [[55.0, 20.1], [58.6, 20.1]]), ('option_E_boundary_17', [[58.6, 20.1], [58.6, 22.8]]), ('option_E_boundary_18', [[58.6, 22.8], [61.9, 22.8]]), ('option_E_boundary_19', [[61.9, 22.8], [61.9, 13.2]])]:
                c.line(points, id=object_id)
            c.line([[67.0, 6.0], [67.0, 30.0]], id='E_fold_0_0', linestyle=(0.0, [4.0, 3.0]))
            for object_id, text, anchor in [('option_label_A', '(A)', [16, 35]), ('option_label_B', '(B)', [50, 35]), ('option_label_C', '(C)', [84, 35]), ('option_label_D', '(D)', [33, 3]), ('option_label_E', '(E)', [67, 3])]:
                c.text(text, anchor, id=object_id, rotation_mode='default')
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane545().draw(sys.argv[1] if len(sys.argv) > 1 else None))
