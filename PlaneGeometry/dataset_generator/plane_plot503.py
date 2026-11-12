"""Frozen question Plane503; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane503:

    def __init__(self):
        self.id = 'Plane503'
        self.source_dataset = 'Author Designed'
        self.source_key = 'authored-extension:Plane312:ext02'
        self.question = 'Which pair of the four numbered pieces can be fitted together, without gaps or overlap, to make the six-sided target at the bottom? All pieces and the target are drawn at the same scale. Pieces may be rotated or turned over.\nChoices:\nA: 1 and 2\nB: 1 and 3\nC: 2 and 3\nD: 2 and 4\nE: 1 and 4\nF: 3 and 4'
        self.answer = 'C'
        self.answer_type = 'choice'
        self.choices = {'A': '1 and 2', 'B': '1 and 3', 'C': '2 and 3', 'D': '2 and 4', 'E': '1 and 4', 'F': '3 and 4'}
        self.query = self.question
        self._geometry_01 = [('piece2_0', [[2, 22], [2, 23]]),
         ('piece2_1', [[2, 22], [3, 22]]),
         ('piece2_2', [[2, 23], [2, 24]]),
         ('piece2_3', [[2, 24], [2, 25]]),
         ('piece2_4', [[2, 25], [2, 26]]),
         ('piece2_5', [[2, 26], [2, 27]]),
         ('piece2_6', [[2, 27], [3, 27]]),
         ('piece2_7', [[3, 22], [4, 22]]),
         ('piece2_8', [[3, 27], [4, 27]]),
         ('piece2_9', [[4, 22], [5, 22]]),
         ('piece2_10', [[4, 23], [4, 24]]),
         ('piece2_11', [[4, 23], [5, 23]]),
         ('piece2_12', [[4, 24], [5, 24]]),
         ('piece2_13', [[4, 25], [4, 26]]),
         ('piece2_14', [[4, 25], [5, 25]]),
         ('piece2_15', [[4, 26], [5, 26]]),
         ('piece2_16', [[4, 27], [5, 27]]),
         ('piece2_17', [[5, 22], [5, 23]]),
         ('piece2_18', [[5, 24], [5, 25]]),
         ('piece2_19', [[5, 26], [5, 27]]),
         ('piece3_0', [[2, 13], [2, 14]]),
         ('piece3_1', [[2, 13], [3, 13]]),
         ('piece3_2', [[2, 14], [3, 14]]),
         ('piece3_3', [[2, 15], [2, 16]]),
         ('piece3_4', [[2, 15], [3, 15]]),
         ('piece3_5', [[2, 16], [3, 16]]),
         ('piece3_6', [[3, 12], [3, 13]]),
         ('piece3_7', [[3, 12], [4, 12]]),
         ('piece3_8', [[3, 14], [3, 15]]),
         ('piece3_9', [[3, 16], [3, 17]]),
         ('piece3_10', [[3, 17], [4, 17]]),
         ('piece3_11', [[4, 12], [5, 12]]),
         ('piece3_12', [[4, 17], [5, 17]]),
         ('piece3_13', [[5, 12], [6, 12]]),
         ('piece3_14', [[5, 15], [5, 16]]),
         ('piece3_15', [[5, 15], [6, 15]]),
         ('piece3_16', [[5, 16], [5, 17]]),
         ('piece3_17', [[6, 12], [7, 12]]),
         ('piece3_18', [[6, 15], [7, 15]]),
         ('piece3_19', [[7, 12], [8, 12]]),
         ('piece3_20', [[7, 15], [8, 15]]),
         ('piece3_21', [[8, 12], [8, 13]]),
         ('piece3_22', [[8, 13], [8, 14]]),
         ('piece3_23', [[8, 14], [8, 15]]),
         ('piece4_0', [[21, 13], [21, 14]]),
         ('piece4_1', [[21, 13], [22, 13]]),
         ('piece4_2', [[21, 14], [22, 14]]),
         ('piece4_3', [[21, 15], [21, 16]]),
         ('piece4_4', [[21, 15], [22, 15]]),
         ('piece4_5', [[21, 16], [22, 16]]),
         ('piece4_6', [[22, 12], [22, 13]]),
         ('piece4_7', [[22, 12], [23, 12]]),
         ('piece4_8', [[22, 14], [22, 15]]),
         ('piece4_9', [[22, 16], [22, 17]]),
         ('piece4_10', [[22, 17], [23, 17]]),
         ('piece4_11', [[23, 12], [24, 12]]),
         ('piece4_12', [[23, 16], [23, 17]]),
         ('piece4_13', [[23, 16], [24, 16]]),
         ('piece4_14', [[24, 12], [25, 12]]),
         ('piece4_15', [[24, 15], [24, 16]]),
         ('piece4_16', [[24, 15], [25, 15]]),
         ('piece4_17', [[25, 12], [26, 12]]),
         ('piece4_18', [[25, 15], [25, 16]]),
         ('piece4_19', [[25, 16], [26, 16]]),
         ('piece4_20', [[26, 12], [27, 12]]),
         ('piece4_21', [[26, 15], [26, 16]]),
         ('piece4_22', [[26, 15], [27, 15]]),
         ('piece4_23', [[27, 12], [27, 13]]),
         ('piece4_24', [[27, 13], [27, 14]]),
         ('piece4_25', [[27, 14], [27, 15]]),
         ('target_0', [[12, 2], [12, 3]]),
         ('target_1', [[12, 2], [13, 2]]),
         ('target_2', [[12, 3], [12, 4]]),
         ('target_3', [[12, 4], [12, 5]]),
         ('target_4', [[12, 5], [12, 6]]),
         ('target_5', [[12, 6], [12, 7]]),
         ('target_6', [[12, 7], [13, 7]]),
         ('target_7', [[13, 2], [14, 2]]),
         ('target_8', [[13, 7], [14, 7]]),
         ('target_9', [[14, 2], [15, 2]]),
         ('target_10', [[14, 7], [15, 7]]),
         ('target_11', [[15, 2], [16, 2]]),
         ('target_12', [[15, 7], [16, 7]]),
         ('target_13', [[16, 2], [17, 2]]),
         ('target_14', [[16, 7], [17, 7]]),
         ('target_15', [[17, 2], [18, 2]]),
         ('target_16', [[17, 5], [17, 6]]),
         ('target_17', [[17, 5], [18, 5]]),
         ('target_18', [[17, 6], [17, 7]]),
         ('target_19', [[18, 2], [19, 2]]),
         ('target_20', [[18, 5], [19, 5]]),
         ('target_21', [[19, 2], [20, 2]]),
         ('target_22', [[19, 5], [20, 5]]),
         ('target_23', [[20, 2], [20, 3]]),
         ('target_24', [[20, 3], [20, 4]]),
         ('target_25', [[20, 4], [20, 5]]),
         ('piece1_0', [[21.0, 22.0], [24.0, 22.0]]),
         ('piece1_1', [[23.0, 23.0], [24.0, 23.0]]),
         ('piece1_2', [[23.0, 24.5], [24.0, 24.5]]),
         ('piece1_3', [[23.0, 25.5], [24.0, 25.5]]),
         ('piece1_4', [[23.0, 26.0], [24.0, 26.0]]),
         ('piece1_5', [[21.0, 27.0], [24.0, 27.0]]),
         ('piece1_6', [[21.0, 22.0], [21.0, 27.0]]),
         ('piece1_7', [[23.0, 23.0], [23.0, 24.5]]),
         ('piece1_8', [[23.0, 25.5], [23.0, 26.0]]),
         ('piece1_9', [[24.0, 22.0], [24.0, 23.0]]),
         ('piece1_10', [[24.0, 24.5], [24.0, 25.5]]),
         ('piece1_11', [[24.0, 26.0], [24.0, 27.0]])]
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane503.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[0.44673162148224144, 28.60187948962887], ylim=[-0.4715825212624303, 27.6835653468842], axes_position=[0.050000000000000114, 0.05, 0.8999999999999998, 0.9], coordinate_axes=False) as c:
            for object_id, points in self._geometry_01:
                c.line(points, id=object_id)
            for object_id, text, anchor in [(None, '1', [22.5, 21]), (None, '2', [3.5, 21]), (None, '3', [5.0, 11]), (None, '4', [24.0, 11])]:
                c.text(text, anchor, id=object_id, zorder=3, fontsize=18.0, rotation_mode='default')
            c.text('Target hexagon', [16.0, 0.6], zorder=3, rotation_mode='default')
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane503().draw(sys.argv[1] if len(sys.argv) > 1 else None))
