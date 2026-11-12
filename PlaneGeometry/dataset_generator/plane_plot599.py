"""Frozen question Plane599; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane599:

    def __init__(self):
        self.id = 'Plane599'
        self.source_dataset = 'Author Designed'
        self.source_key = 'author-extensions95-v1:Plane456/extension_05'
        self.question = 'Each of the three large squares shown below is the same size. In I and II, $P$, $Q$, $R$ and $S$ lie one third of a side from the bottom-left, bottom-right, top-right and top-left corners respectively, and consecutive points are joined; I also draws $PR$. In III, $U$ is one third of a side from the bottom-left corner and $V$ is two thirds of a side above the bottom-right corner. How do the shaded areas of these squares compare?\n\nChoices:\nA: $S_{I} = S_{II} = S_{III}$\nB: $S_{I} = S_{II} > S_{III}$\nC: $S_{III} > S_{I} > S_{II}$\nD: $S_{II} = S_{III} > S_{I}$\nE: $S_{I} > S_{II} = S_{III}$'
        self.answer = 'E'
        self.answer_type = 'choice'
        self.choices = {'A': '$S_{I} = S_{II} = S_{III}$',
         'B': '$S_{I} = S_{II} > S_{III}$',
         'C': '$S_{III} > S_{I} > S_{II}$',
         'D': '$S_{II} = S_{III} > S_{I}$',
         'E': '$S_{I} > S_{II} = S_{III}$'}
        self.query = self.question
        self.points = {'I_point_1': [0.0, 0.0],
         'I_point_2': [0.0, 1.3333333333333333],
         'I_point_3': [0.0, 2.0],
         'I_point_4': [0.6666666666666666, 0.0],
         'I_point_5': [1.3333333333333333, 2.0],
         'I_point_6': [2.0, 0.0],
         'I_point_7': [2.0, 0.6666666666666666],
         'I_point_8': [2.0, 2.0],
         'I_panel_anchor': [1.0, 2.58],
         'II_point_1': [3.0, 0.0],
         'II_point_2': [3.0, 1.3333333333333333],
         'II_point_3': [3.0, 2.0],
         'II_point_4': [3.6666666666666665, 0.0],
         'II_point_5': [4.333333333333333, 2.0],
         'II_point_6': [5.0, 0.0],
         'II_point_7': [5.0, 0.6666666666666666],
         'II_point_8': [5.0, 2.0],
         'II_panel_anchor': [4.0, 2.58],
         'III_point_1': [6.0, 0.0],
         'III_point_2': [6.0, 2.0],
         'III_point_3': [6.666666666666667, 0.0],
         'III_point_4': [8.0, 0.0],
         'III_point_5': [8.0, 1.3333333333333333],
         'III_point_6': [8.0, 2.0],
         'III_panel_anchor': [7.0, 2.58]}
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane599.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-0.57, 8.57], ylim=[-3.392, 5.748]) as c:
            c.fill([self.points['I_point_4'], self.points['I_point_7'], self.points['I_point_5']], facecolor='#E8E8E8', alpha=1, id='I_shade_4')
            for object_id, points in [('I_outer_AB', [self.points['I_point_1'], self.points['I_point_6']]), ('I_outer_BC', [self.points['I_point_6'], self.points['I_point_8']]), ('I_outer_CD', [self.points['I_point_8'], self.points['I_point_3']]), ('I_outer_DA', [self.points['I_point_3'], self.points['I_point_1']]), ('I_cut_1', [self.points['I_point_4'], self.points['I_point_7']]), ('I_cut_2', [self.points['I_point_7'], self.points['I_point_5']]), ('I_cut_3', [self.points['I_point_5'], self.points['I_point_2']]), ('I_cut_4', [self.points['I_point_2'], self.points['I_point_4']]), ('I_cut_5', [self.points['I_point_4'], self.points['I_point_5']])]:
                c.line(points, id=object_id)
            c.fill([self.points['II_point_2'], self.points['II_point_5'], self.points['II_point_3']], facecolor='#E8E8E8', alpha=1, id='II_shade_2')
            c.fill([self.points['II_point_4'], self.points['II_point_6'], self.points['II_point_7']], facecolor='#E8E8E8', alpha=1, id='II_shade_3')
            for object_id, points in [('II_outer_AB', [self.points['II_point_1'], self.points['II_point_6']]), ('II_outer_BC', [self.points['II_point_6'], self.points['II_point_8']]), ('II_outer_CD', [self.points['II_point_8'], self.points['II_point_3']]), ('II_outer_DA', [self.points['II_point_3'], self.points['II_point_1']]), ('II_cut_1', [self.points['II_point_4'], self.points['II_point_7']]), ('II_cut_2', [self.points['II_point_7'], self.points['II_point_5']]), ('II_cut_3', [self.points['II_point_5'], self.points['II_point_2']]), ('II_cut_4', [self.points['II_point_2'], self.points['II_point_4']])]:
                c.line(points, id=object_id)
            c.fill([self.points['III_point_3'], self.points['III_point_4'], self.points['III_point_5']], facecolor='#E8E8E8', alpha=1, id='III_shade_1')
            for object_id, points in [('III_outer_AB', [self.points['III_point_1'], self.points['III_point_4']]), ('III_outer_BC', [self.points['III_point_4'], self.points['III_point_6']]), ('III_outer_CD', [self.points['III_point_6'], self.points['III_point_2']]), ('III_outer_DA', [self.points['III_point_2'], self.points['III_point_1']]), ('III_cut_1', [self.points['III_point_3'], self.points['III_point_5']])]:
                c.line(points, id=object_id)
            c.text('I', self.points['I_panel_anchor'], offset_pt=[0, 0], vertex=False, id='I_panel_label')
            c.text('P', self.points['I_point_4'], offset_pt=[0, -15], vertex=True, id='I_label_P')
            c.text('Q', self.points['I_point_7'], offset_pt=[13, 0], vertex=True, id='I_label_Q')
            c.text('R', self.points['I_point_5'], offset_pt=[0, 15], vertex=True, id='I_label_R')
            c.text('S', self.points['I_point_2'], offset_pt=[-13, 0], vertex=True, id='I_label_S')
            c.text('II', self.points['II_panel_anchor'], offset_pt=[0, 0], vertex=False, id='II_panel_label')
            c.text('P', self.points['II_point_4'], offset_pt=[0, -15], vertex=True, id='II_label_P')
            c.text('Q', self.points['II_point_7'], offset_pt=[13, 0], vertex=True, id='II_label_Q')
            c.text('R', self.points['II_point_5'], offset_pt=[0, 15], vertex=True, id='II_label_R')
            c.text('S', self.points['II_point_2'], offset_pt=[-13, 0], vertex=True, id='II_label_S')
            c.text('III', self.points['III_panel_anchor'], offset_pt=[0, 0], vertex=False, id='III_panel_label')
            c.text('U', self.points['III_point_3'], offset_pt=[0, -15], vertex=True, id='III_label_U')
            c.text('V', self.points['III_point_5'], offset_pt=[13, 0], vertex=True, id='III_label_V')
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane599().draw(sys.argv[1] if len(sys.argv) > 1 else None))
