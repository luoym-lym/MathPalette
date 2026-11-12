"""Frozen question Plane596; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane596:

    def __init__(self):
        self.id = 'Plane596'
        self.source_dataset = 'Author Designed'
        self.source_key = 'author-extensions95-v1:Plane456/extension_02'
        self.question = 'Each of the three large squares shown below is the same size. In I the vertical lines trisect the square and the slanting line is a diagonal. In II the horizontal lines trisect the square, and the slanting segments join the bottom corners to the midpoint of the top side. In III the lines divide the square into nine equal squares. How do the shaded areas of these squares compare?\n\nChoices:\nA: $S_{I} = S_{II} = S_{III}$\nB: $S_{I} = S_{II} > S_{III}$\nC: $S_{II} = S_{III} > S_{I}$\nD: $S_{I} = S_{III} > S_{II}$\nE: $S_{I} < S_{II} < S_{III}$'
        self.answer = 'D'
        self.answer_type = 'choice'
        self.choices = {'A': '$S_{I} = S_{II} = S_{III}$',
         'B': '$S_{I} = S_{II} > S_{III}$',
         'C': '$S_{II} = S_{III} > S_{I}$',
         'D': '$S_{I} = S_{III} > S_{II}$',
         'E': '$S_{I} < S_{II} < S_{III}$'}
        self.query = self.question
        self.points = {'I_point_1': [0.0, 0.0],
         'I_point_2': [0.0, 0.6666666666666666],
         'I_point_3': [0.0, 1.3333333333333333],
         'I_point_4': [0.0, 2.0],
         'I_point_5': [0.6666666666666666, 0.0],
         'I_point_6': [0.6666666666666666, 0.6666666666666666],
         'I_point_7': [0.6666666666666666, 2.0],
         'I_point_8': [1.3333333333333333, 0.0],
         'I_point_9': [1.3333333333333333, 1.3333333333333333],
         'I_point_10': [1.3333333333333333, 2.0],
         'I_point_11': [2.0, 0.0],
         'I_point_12': [2.0, 0.6666666666666666],
         'I_point_13': [2.0, 1.3333333333333333],
         'I_point_14': [2.0, 2.0],
         'I_panel_anchor': [1.0, 2.25],
         'II_point_1': [3.0, 0.0],
         'II_point_2': [3.0, 0.6666666666666666],
         'II_point_3': [3.0, 1.3333333333333333],
         'II_point_4': [3.0, 2.0],
         'II_point_5': [3.3333333333333335, 0.6666666666666666],
         'II_point_6': [3.6666666666666665, 0.0],
         'II_point_7': [3.6666666666666665, 1.3333333333333333],
         'II_point_8': [3.6666666666666665, 2.0],
         'II_point_9': [4.0, 2.0],
         'II_point_10': [4.333333333333333, 0.0],
         'II_point_11': [4.333333333333333, 1.3333333333333333],
         'II_point_12': [4.333333333333333, 2.0],
         'II_point_13': [4.666666666666667, 0.6666666666666666],
         'II_point_14': [5.0, 0.0],
         'II_point_15': [5.0, 0.6666666666666666],
         'II_point_16': [5.0, 1.3333333333333333],
         'II_point_17': [5.0, 2.0],
         'II_panel_anchor': [4.0, 2.25],
         'III_point_1': [6.0, 0.0],
         'III_point_2': [6.0, 0.6666666666666666],
         'III_point_3': [6.0, 1.3333333333333333],
         'III_point_4': [6.0, 2.0],
         'III_point_5': [6.666666666666667, 0.0],
         'III_point_6': [6.666666666666667, 0.6666666666666666],
         'III_point_7': [6.666666666666667, 1.3333333333333333],
         'III_point_8': [6.666666666666667, 2.0],
         'III_point_9': [7.333333333333333, 0.0],
         'III_point_10': [7.333333333333333, 0.6666666666666666],
         'III_point_11': [7.333333333333333, 1.3333333333333333],
         'III_point_12': [7.333333333333333, 2.0],
         'III_point_13': [8.0, 0.0],
         'III_point_14': [8.0, 0.6666666666666666],
         'III_point_15': [8.0, 1.3333333333333333],
         'III_point_16': [8.0, 2.0],
         'III_panel_anchor': [7.0, 2.25]}
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane596.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-0.205, 8.205], ylim=[-3.027, 5.383]) as c:
            c.fill([self.points['I_point_1'], self.points['I_point_5'], self.points['I_point_6']], facecolor='#E8E8E8', alpha=1, id='I_shade_0')
            c.fill([self.points['I_point_8'], self.points['I_point_11'], self.points['I_point_14'], self.points['I_point_9']], facecolor='#E8E8E8', alpha=1, id='I_shade_4')
            for object_id, points in [('I_outer_AB', [self.points['I_point_1'], self.points['I_point_11']]), ('I_outer_BC', [self.points['I_point_11'], self.points['I_point_14']]), ('I_outer_CD', [self.points['I_point_14'], self.points['I_point_4']]), ('I_outer_DA', [self.points['I_point_4'], self.points['I_point_1']]), ('I_cut_1', [self.points['I_point_5'], self.points['I_point_7']]), ('I_cut_2', [self.points['I_point_8'], self.points['I_point_10']]), ('I_cut_3', [self.points['I_point_1'], self.points['I_point_14']])]:
                c.line(points, id=object_id)
            c.fill([self.points['II_point_5'], self.points['II_point_13'], self.points['II_point_11'], self.points['II_point_7']], facecolor='#E8E8E8', alpha=1, id='II_shade_4')
            for object_id, points in [('II_outer_AB', [self.points['II_point_1'], self.points['II_point_14']]), ('II_outer_BC', [self.points['II_point_14'], self.points['II_point_17']]), ('II_outer_CD', [self.points['II_point_17'], self.points['II_point_4']]), ('II_outer_DA', [self.points['II_point_4'], self.points['II_point_1']]), ('II_cut_1', [self.points['II_point_2'], self.points['II_point_15']]), ('II_cut_2', [self.points['II_point_3'], self.points['II_point_16']]), ('II_cut_3', [self.points['II_point_1'], self.points['II_point_9']]), ('II_cut_4', [self.points['II_point_14'], self.points['II_point_9']])]:
                c.line(points, id=object_id)
            for object_id, points in [('III_shade_0', [self.points['III_point_1'], self.points['III_point_5'], self.points['III_point_6'], self.points['III_point_2']]), ('III_shade_4', [self.points['III_point_6'], self.points['III_point_10'], self.points['III_point_11'], self.points['III_point_7']]), ('III_shade_8', [self.points['III_point_11'], self.points['III_point_15'], self.points['III_point_16'], self.points['III_point_12']])]:
                c.fill(points, id=object_id, facecolor='#E8E8E8', alpha=1)
            for object_id, points in [('III_outer_AB', [self.points['III_point_1'], self.points['III_point_13']]), ('III_outer_BC', [self.points['III_point_13'], self.points['III_point_16']]), ('III_outer_CD', [self.points['III_point_16'], self.points['III_point_4']]), ('III_outer_DA', [self.points['III_point_4'], self.points['III_point_1']]), ('III_cut_1', [self.points['III_point_5'], self.points['III_point_8']]), ('III_cut_2', [self.points['III_point_9'], self.points['III_point_12']]), ('III_cut_3', [self.points['III_point_2'], self.points['III_point_14']]), ('III_cut_4', [self.points['III_point_3'], self.points['III_point_15']])]:
                c.line(points, id=object_id)
            for object_id, text, anchor in [('I_panel_label', 'I', self.points['I_panel_anchor']), ('II_panel_label', 'II', self.points['II_panel_anchor']), ('III_panel_label', 'III', self.points['III_panel_anchor'])]:
                c.text(text, anchor, id=object_id, offset_pt=[0, 0], vertex=False)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane596().draw(sys.argv[1] if len(sys.argv) > 1 else None))
