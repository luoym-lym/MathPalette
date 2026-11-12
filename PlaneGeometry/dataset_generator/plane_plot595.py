"""Frozen question Plane595; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane595:

    def __init__(self):
        self.id = 'Plane595'
        self.source_dataset = 'Author Designed'
        self.source_key = 'author-extensions95-v1:Plane456/extension_01'
        self.question = 'Each of the three large squares shown below is the same size. Where a segment meets a side of a square, or a side of the inner diamond in I, it meets that side at its midpoint. How do the shaded areas of these squares compare?\n\nChoices:\nA: $S_{I} = S_{II} = S_{III}$\nB: $S_{I} < S_{II} < S_{III}$\nC: $S_{II} < S_{I} < S_{III}$\nD: $S_{I} = S_{II} < S_{III}$\nE: $S_{III} < S_{II} < S_{I}$'
        self.answer = 'B'
        self.answer_type = 'choice'
        self.choices = {'A': '$S_{I} = S_{II} = S_{III}$',
         'B': '$S_{I} < S_{II} < S_{III}$',
         'C': '$S_{II} < S_{I} < S_{III}$',
         'D': '$S_{I} = S_{II} < S_{III}$',
         'E': '$S_{III} < S_{II} < S_{I}$'}
        self.query = self.question
        self.points = {'I_point_1': [0.0, 0.0],
         'I_point_2': [0.0, 1.0],
         'I_point_3': [0.0, 2.0],
         'I_point_4': [0.5, 0.5],
         'I_point_5': [0.5, 1.5],
         'I_point_6': [1.0, 0.0],
         'I_point_7': [1.0, 2.0],
         'I_point_8': [1.5, 0.5],
         'I_point_9': [1.5, 1.5],
         'I_point_10': [2.0, 0.0],
         'I_point_11': [2.0, 1.0],
         'I_point_12': [2.0, 2.0],
         'I_panel_anchor': [1.0, 2.25],
         'II_point_1': [3.0, 0.0],
         'II_point_2': [3.0, 2.0],
         'II_point_3': [4.0, 2.0],
         'II_point_4': [5.0, 0.0],
         'II_point_5': [5.0, 1.0],
         'II_point_6': [5.0, 2.0],
         'II_panel_anchor': [4.0, 2.25],
         'III_point_1': [6.0, 0.0],
         'III_point_2': [6.0, 2.0],
         'III_point_3': [7.0, 0.0],
         'III_point_4': [8.0, 0.0],
         'III_point_5': [8.0, 2.0],
         'III_panel_anchor': [7.0, 2.25]}
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane595.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-0.205, 8.205], ylim=[-3.027, 5.383]) as c:
            for object_id, points in [('I_shade_1', [self.points['I_point_2'], self.points['I_point_4'], self.points['I_point_5']]), ('I_shade_3', [self.points['I_point_4'], self.points['I_point_6'], self.points['I_point_8']]), ('I_shade_5', [self.points['I_point_5'], self.points['I_point_9'], self.points['I_point_7']]), ('I_shade_8', [self.points['I_point_8'], self.points['I_point_11'], self.points['I_point_9']])]:
                c.fill(points, id=object_id, facecolor='#E8E8E8', alpha=1)
            for object_id, points in [('I_outer_AB', [self.points['I_point_1'], self.points['I_point_10']]), ('I_outer_BC', [self.points['I_point_10'], self.points['I_point_12']]), ('I_outer_CD', [self.points['I_point_12'], self.points['I_point_3']]), ('I_outer_DA', [self.points['I_point_3'], self.points['I_point_1']]), ('I_cut_1', [self.points['I_point_6'], self.points['I_point_11']]), ('I_cut_2', [self.points['I_point_11'], self.points['I_point_7']]), ('I_cut_3', [self.points['I_point_7'], self.points['I_point_2']]), ('I_cut_4', [self.points['I_point_2'], self.points['I_point_6']]), ('I_cut_5', [self.points['I_point_8'], self.points['I_point_9']]), ('I_cut_6', [self.points['I_point_9'], self.points['I_point_5']]), ('I_cut_7', [self.points['I_point_5'], self.points['I_point_4']]), ('I_cut_8', [self.points['I_point_4'], self.points['I_point_8']])]:
                c.line(points, id=object_id)
            c.fill([self.points['II_point_1'], self.points['II_point_5'], self.points['II_point_3']], facecolor='#E8E8E8', alpha=1, id='II_shade_2')
            for object_id, points in [('II_outer_AB', [self.points['II_point_1'], self.points['II_point_4']]), ('II_outer_BC', [self.points['II_point_4'], self.points['II_point_6']]), ('II_outer_CD', [self.points['II_point_6'], self.points['II_point_2']]), ('II_outer_DA', [self.points['II_point_2'], self.points['II_point_1']]), ('II_cut_1', [self.points['II_point_1'], self.points['II_point_3']]), ('II_cut_2', [self.points['II_point_3'], self.points['II_point_5']]), ('II_cut_3', [self.points['II_point_5'], self.points['II_point_1']])]:
                c.line(points, id=object_id)
            c.fill([self.points['III_point_2'], self.points['III_point_3'], self.points['III_point_5']], facecolor='#E8E8E8', alpha=1, id='III_shade_1')
            for object_id, points in [('III_outer_AB', [self.points['III_point_1'], self.points['III_point_4']]), ('III_outer_BC', [self.points['III_point_4'], self.points['III_point_5']]), ('III_outer_CD', [self.points['III_point_5'], self.points['III_point_2']]), ('III_outer_DA', [self.points['III_point_2'], self.points['III_point_1']]), ('III_cut_1', [self.points['III_point_2'], self.points['III_point_3']]), ('III_cut_2', [self.points['III_point_3'], self.points['III_point_5']])]:
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
    print(Plane595().draw(sys.argv[1] if len(sys.argv) > 1 else None))
