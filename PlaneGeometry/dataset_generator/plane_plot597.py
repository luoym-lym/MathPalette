"""Frozen question Plane597; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane597:

    def __init__(self):
        self.id = 'Plane597'
        self.source_dataset = 'Author Designed'
        self.source_key = 'author-extensions95-v1:Plane456/extension_03'
        self.question = 'Each of the three large squares shown below is the same size. Every segment that meets a side, other than at a corner, meets that side at its midpoint. How do the shaded areas of these squares compare?\n\nChoices:\nA: $S_{I} < S_{II} < S_{III}$\nB: $S_{I} = S_{II} = S_{III}$\nC: $S_{II} < S_{III} < S_{I}$\nD: $S_{III} < S_{II} < S_{I}$\nE: $S_{II} < S_{I} < S_{III}$'
        self.answer = 'C'
        self.answer_type = 'choice'
        self.choices = {'A': '$S_{I} < S_{II} < S_{III}$',
         'B': '$S_{I} = S_{II} = S_{III}$',
         'C': '$S_{II} < S_{III} < S_{I}$',
         'D': '$S_{III} < S_{II} < S_{I}$',
         'E': '$S_{II} < S_{I} < S_{III}$'}
        self.query = self.question
        self.points = {'I_point_1': [0.0, 0.0],
         'I_point_2': [0.0, 2.0],
         'I_point_3': [0.6666666666666666, 1.3333333333333333],
         'I_point_4': [1.0, 2.0],
         'I_point_5': [2.0, 0.0],
         'I_point_6': [2.0, 2.0],
         'I_panel_anchor': [1.0, 2.25],
         'II_point_1': [3.0, 0.0],
         'II_point_2': [3.0, 2.0],
         'II_point_3': [4.333333333333333, 0.6666666666666666],
         'II_point_4': [5.0, 0.0],
         'II_point_5': [5.0, 1.0],
         'II_point_6': [5.0, 2.0],
         'II_panel_anchor': [4.0, 2.25],
         'III_point_1': [6.0, 0.0],
         'III_point_2': [6.0, 2.0],
         'III_point_3': [6.8, 0.4],
         'III_point_4': [7.0, 0.0],
         'III_point_5': [8.0, 0.0],
         'III_point_6': [8.0, 1.0],
         'III_point_7': [8.0, 2.0],
         'III_panel_anchor': [7.0, 2.25]}
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane597.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-0.205, 8.205], ylim=[-3.027, 5.383]) as c:
            c.fill([self.points['I_point_1'], self.points['I_point_5'], self.points['I_point_3']], facecolor='#E8E8E8', alpha=1, id='I_shade_1')
            for object_id, points in [('I_outer_AB', [self.points['I_point_1'], self.points['I_point_5']]), ('I_outer_BC', [self.points['I_point_5'], self.points['I_point_6']]), ('I_outer_CD', [self.points['I_point_6'], self.points['I_point_2']]), ('I_outer_DA', [self.points['I_point_2'], self.points['I_point_1']]), ('I_cut_1', [self.points['I_point_1'], self.points['I_point_4']]), ('I_cut_2', [self.points['I_point_5'], self.points['I_point_2']])]:
                c.line(points, id=object_id)
            c.fill([self.points['II_point_1'], self.points['II_point_4'], self.points['II_point_3']], facecolor='#E8E8E8', alpha=1, id='II_shade_1')
            for object_id, points in [('II_outer_AB', [self.points['II_point_1'], self.points['II_point_4']]), ('II_outer_BC', [self.points['II_point_4'], self.points['II_point_6']]), ('II_outer_CD', [self.points['II_point_6'], self.points['II_point_2']]), ('II_outer_DA', [self.points['II_point_2'], self.points['II_point_1']]), ('II_cut_1', [self.points['II_point_1'], self.points['II_point_5']]), ('II_cut_2', [self.points['II_point_4'], self.points['II_point_2']])]:
                c.line(points, id=object_id)
            c.fill([self.points['III_point_1'], self.points['III_point_3'], self.points['III_point_2']], facecolor='#E8E8E8', alpha=1, id='III_shade_0')
            for object_id, points in [('III_outer_AB', [self.points['III_point_1'], self.points['III_point_5']]), ('III_outer_BC', [self.points['III_point_5'], self.points['III_point_7']]), ('III_outer_CD', [self.points['III_point_7'], self.points['III_point_2']]), ('III_outer_DA', [self.points['III_point_2'], self.points['III_point_1']]), ('III_cut_1', [self.points['III_point_1'], self.points['III_point_6']]), ('III_cut_2', [self.points['III_point_2'], self.points['III_point_4']])]:
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
    print(Plane597().draw(sys.argv[1] if len(sys.argv) > 1 else None))
