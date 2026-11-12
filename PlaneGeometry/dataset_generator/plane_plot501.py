"""Frozen question Plane501; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane501:

    def __init__(self):
        self.id = 'Plane501'
        self.source_dataset = 'Author Designed'
        self.source_key = 'authored-extension:Plane172:ext03'
        self.question = 'The rectangle on the left was divided into six pieces along the drawn lines. Five of these pieces were rearranged to make the figure on the right. Which piece is missing? Pieces may be rotated or turned over.\nChoices:\nA: A\nB: B\nC: C\nD: D\nE: E'
        self.answer = 'D'
        self.answer_type = 'choice'
        self.choices = {'A': 'A', 'B': 'B', 'C': 'C', 'D': 'D', 'E': 'E'}
        self.query = self.question
        self._geometry_01 = [('sourcepiece0_0', [[3, 24], [3, 25]]),
         ('sourcepiece0_1', [[3, 24], [4, 24]]),
         ('sourcepiece0_2', [[3, 25], [4, 25]]),
         ('sourcepiece0_3', [[4, 24], [5, 24]]),
         ('sourcepiece0_4', [[4, 25], [5, 25]]),
         ('sourcepiece0_5', [[5, 24], [6, 24]]),
         ('sourcepiece0_6', [[5, 25], [6, 25]]),
         ('sourcepiece0_7', [[6, 24], [7, 24]]),
         ('sourcepiece0_8', [[6, 25], [7, 25]]),
         ('sourcepiece0_9', [[7, 24], [7, 25]]),
         ('sourcepiece1_0', [[3, 26], [3, 27]]),
         ('sourcepiece1_1', [[3, 26], [4, 26]]),
         ('sourcepiece1_2', [[3, 27], [3, 28]]),
         ('sourcepiece1_3', [[3, 28], [4, 28]]),
         ('sourcepiece1_4', [[4, 26], [5, 26]]),
         ('sourcepiece1_5', [[4, 28], [5, 28]]),
         ('sourcepiece1_6', [[5, 26], [5, 27]]),
         ('sourcepiece1_7', [[5, 27], [5, 28]]),
         ('sourcepiece2_0', [[5, 27], [5, 28]]),
         ('sourcepiece2_1', [[5, 27], [6, 27]]),
         ('sourcepiece2_2', [[5, 28], [6, 28]]),
         ('sourcepiece2_3', [[6, 26], [6, 27]]),
         ('sourcepiece2_4', [[6, 26], [7, 26]]),
         ('sourcepiece2_5', [[6, 28], [7, 28]]),
         ('sourcepiece2_6', [[7, 26], [7, 27]]),
         ('sourcepiece2_7', [[7, 27], [8, 27]]),
         ('sourcepiece2_8', [[7, 28], [8, 28]]),
         ('sourcepiece2_9', [[8, 27], [8, 28]]),
         ('sourcepiece3_0', [[7, 26], [7, 27]]),
         ('sourcepiece3_1', [[7, 26], [8, 26]]),
         ('sourcepiece3_2', [[7, 27], [8, 27]]),
         ('sourcepiece3_3', [[8, 25], [8, 26]]),
         ('sourcepiece3_4', [[8, 25], [9, 25]]),
         ('sourcepiece3_5', [[8, 27], [8, 28]]),
         ('sourcepiece3_6', [[8, 28], [9, 28]]),
         ('sourcepiece3_7', [[9, 25], [9, 26]]),
         ('sourcepiece3_8', [[9, 26], [9, 27]]),
         ('sourcepiece3_9', [[9, 27], [9, 28]]),
         ('sourcepiece4_0', [[3, 25], [3, 26]]),
         ('sourcepiece4_1', [[3, 25], [4, 25]]),
         ('sourcepiece4_2', [[3, 26], [4, 26]]),
         ('sourcepiece4_3', [[4, 25], [5, 25]]),
         ('sourcepiece4_4', [[4, 26], [5, 26]]),
         ('sourcepiece4_5', [[5, 25], [6, 25]]),
         ('sourcepiece4_6', [[5, 26], [5, 27]]),
         ('sourcepiece4_7', [[5, 27], [6, 27]]),
         ('sourcepiece4_8', [[6, 25], [6, 26]]),
         ('sourcepiece4_9', [[6, 26], [6, 27]]),
         ('sourcepiece5_0', [[6, 25], [6, 26]]),
         ('sourcepiece5_1', [[6, 25], [7, 25]]),
         ('sourcepiece5_2', [[6, 26], [7, 26]]),
         ('sourcepiece5_3', [[7, 24], [7, 25]]),
         ('sourcepiece5_4', [[7, 24], [8, 24]]),
         ('sourcepiece5_5', [[7, 26], [8, 26]]),
         ('sourcepiece5_6', [[8, 24], [9, 24]]),
         ('sourcepiece5_7', [[8, 25], [8, 26]]),
         ('sourcepiece5_8', [[8, 25], [9, 25]]),
         ('sourcepiece5_9', [[9, 24], [9, 25]]),
         ('targetpiece0_0', [[18, 22], [18, 23]]),
         ('targetpiece0_1', [[18, 22], [19, 22]]),
         ('targetpiece0_2', [[18, 23], [19, 23]]),
         ('targetpiece0_3', [[19, 22], [20, 22]]),
         ('targetpiece0_4', [[19, 23], [20, 23]]),
         ('targetpiece0_5', [[20, 22], [21, 22]]),
         ('targetpiece0_6', [[20, 23], [21, 23]]),
         ('targetpiece0_7', [[21, 22], [22, 22]]),
         ('targetpiece0_8', [[21, 23], [22, 23]]),
         ('targetpiece0_9', [[22, 22], [22, 23]]),
         ('targetpiece1_0', [[20, 23], [20, 24]]),
         ('targetpiece1_1', [[20, 23], [21, 23]]),
         ('targetpiece1_2', [[20, 24], [20, 25]]),
         ('targetpiece1_3', [[20, 25], [21, 25]]),
         ('targetpiece1_4', [[21, 23], [22, 23]]),
         ('targetpiece1_5', [[21, 25], [22, 25]]),
         ('targetpiece1_6', [[22, 23], [22, 24]]),
         ('targetpiece1_7', [[22, 24], [22, 25]]),
         ('targetpiece2_0', [[22, 22], [22, 23]]),
         ('targetpiece2_1', [[22, 22], [23, 22]]),
         ('targetpiece2_2', [[22, 23], [22, 24]]),
         ('targetpiece2_3', [[22, 24], [22, 25]]),
         ('targetpiece2_4', [[22, 25], [23, 25]]),
         ('targetpiece2_5', [[23, 22], [23, 23]]),
         ('targetpiece2_6', [[23, 23], [24, 23]]),
         ('targetpiece2_7', [[23, 24], [23, 25]]),
         ('targetpiece2_8', [[23, 24], [24, 24]]),
         ('targetpiece2_9', [[24, 23], [24, 24]]),
         ('targetpiece3_0', [[19, 26], [19, 27]]),
         ('targetpiece3_1', [[19, 26], [20, 26]]),
         ('targetpiece3_2', [[19, 27], [20, 27]]),
         ('targetpiece3_3', [[20, 25], [20, 26]]),
         ('targetpiece3_4', [[20, 25], [21, 25]]),
         ('targetpiece3_5', [[20, 27], [20, 28]]),
         ('targetpiece3_6', [[20, 28], [21, 28]]),
         ('targetpiece3_7', [[21, 25], [21, 26]]),
         ('targetpiece3_8', [[21, 26], [21, 27]]),
         ('targetpiece3_9', [[21, 27], [21, 28]]),
         ('targetpiece4_0', [[23, 22], [23, 23]]),
         ('targetpiece4_1', [[23, 22], [24, 22]]),
         ('targetpiece4_2', [[23, 23], [24, 23]]),
         ('targetpiece4_3', [[24, 22], [25, 22]]),
         ('targetpiece4_4', [[24, 23], [24, 24]]),
         ('targetpiece4_5', [[24, 24], [25, 24]]),
         ('targetpiece4_6', [[25, 22], [25, 23]]),
         ('targetpiece4_7', [[25, 23], [26, 23]]),
         ('targetpiece4_8', [[25, 24], [26, 24]]),
         ('targetpiece4_9', [[26, 23], [26, 24]]),
         ('A_0', [[1, 13], [1, 14]]),
         ('A_1', [[1, 13], [2, 13]]),
         ('A_2', [[1, 14], [2, 14]]),
         ('A_3', [[2, 13], [3, 13]]),
         ('A_4', [[2, 14], [3, 14]]),
         ('A_5', [[3, 13], [4, 13]]),
         ('A_6', [[3, 14], [4, 14]]),
         ('A_7', [[4, 13], [5, 13]]),
         ('A_8', [[4, 14], [5, 14]]),
         ('A_9', [[5, 13], [5, 14]]),
         ('B_0', [[12, 13], [12, 14]]),
         ('B_1', [[12, 13], [13, 13]]),
         ('B_2', [[12, 14], [12, 15]]),
         ('B_3', [[12, 15], [13, 15]]),
         ('B_4', [[13, 13], [14, 13]]),
         ('B_5', [[13, 15], [14, 15]]),
         ('B_6', [[14, 13], [14, 14]]),
         ('B_7', [[14, 14], [14, 15]]),
         ('C_0', [[23, 13], [23, 14]]),
         ('C_1', [[23, 13], [24, 13]]),
         ('C_2', [[23, 14], [24, 14]]),
         ('C_3', [[24, 13], [25, 13]]),
         ('C_4', [[24, 14], [24, 15]]),
         ('C_5', [[24, 15], [25, 15]]),
         ('C_6', [[25, 13], [26, 13]]),
         ('C_7', [[25, 14], [25, 15]]),
         ('C_8', [[25, 14], [26, 14]]),
         ('C_9', [[26, 13], [26, 14]]),
         ('D_0', [[6, 3], [6, 4]]),
         ('D_1', [[6, 3], [7, 3]]),
         ('D_2', [[6, 4], [6, 5]]),
         ('D_3', [[6, 5], [7, 5]]),
         ('D_4', [[7, 3], [8, 3]]),
         ('D_5', [[7, 4], [7, 5]]),
         ('D_6', [[7, 4], [8, 4]]),
         ('D_7', [[8, 3], [9, 3]]),
         ('D_8', [[8, 4], [9, 4]]),
         ('D_9', [[9, 3], [9, 4]]),
         ('E_0', [[19, 3], [19, 4]]),
         ('E_1', [[19, 3], [20, 3]]),
         ('E_2', [[19, 4], [20, 4]]),
         ('E_3', [[20, 3], [21, 3]]),
         ('E_4', [[20, 4], [20, 5]]),
         ('E_5', [[20, 5], [21, 5]]),
         ('E_6', [[21, 3], [21, 4]]),
         ('E_7', [[21, 4], [22, 4]]),
         ('E_8', [[21, 5], [22, 5]]),
         ('E_9', [[22, 4], [22, 5]])]
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane501.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-0.8059209987091052, 30.42629221021858], ylim=[0.9987660807213405, 32.23097928964903], axes_position=[0.050000000000000114, 0.05, 0.8999999999999998, 0.9], coordinate_axes=False) as c:
            for object_id, points in self._geometry_01:
                c.line(points, id=object_id)
            c.text('Original partition', [6, 31], zorder=3, rotation_mode='default')
            c.text('Rearranged pieces', [24, 31], zorder=3, rotation_mode='default')
            for object_id, text, anchor in [(None, 'A', [3.0, 12]), (None, 'B', [13.0, 12]), (None, 'C', [24.5, 12]), (None, 'D', [7.5, 2]), (None, 'E', [20.5, 2])]:
                c.text(text, anchor, id=object_id, zorder=3, fontsize=18.0, rotation_mode='default')
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane501().draw(sys.argv[1] if len(sys.argv) > 1 else None))
