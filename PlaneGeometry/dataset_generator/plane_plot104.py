"""Frozen question Plane104; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane104:

    def __init__(self):
        self.id = 'Plane104'
        self.source_dataset = 'Author Designed'
        self.source_key = 'visual-matching:notched_arrow'
        self.question = 'All outlines use the same scale. Which outline, A, B, or C, is congruent to R? Rotations and reflections are allowed.\nChoices:\nA: Outline A\nB: Outline B\nC: Outline C'
        self.answer = 'B'
        self.answer_type = 'choice'
        self.choices = {'A': 'Outline A', 'B': 'Outline B', 'C': 'Outline C'}
        self.query = self.question
        self.points = {'R_0': [-6.5, 2.0],
         'R_1': [-3.5, 2.0],
         'R_2': [-1.5, 4.0],
         'R_3': [-3.5, 6.0],
         'R_4': [-6.5, 6.0],
         'R_5': [-5.0, 4.5],
         'name_anchor_R': [-4.0, 2.0],
         'A_0': [1.5, 2.0],
         'A_1': [4.5, 2.0],
         'A_2': [6.5, 4.0],
         'A_3': [4.5, 6.0],
         'A_4': [1.5, 6.0],
         'A_5': [2.25, 4.5],
         'name_anchor_A': [4.0, 2.0],
         'B_0': [-2.0, -1.5],
         'B_1': [-2.0, -4.5],
         'B_2': [-4.0, -6.5],
         'B_3': [-6.0, -4.5],
         'B_4': [-6.0, -1.4999999999999998],
         'B_5': [-4.5, -3.0],
         'name_anchor_B': [-4.0, -6.5],
         'C_0': [1.5, -6.0],
         'C_1': [4.5, -6.0],
         'C_2': [6.5, -3.0],
         'C_3': [4.5, -2.0],
         'C_4': [1.5, -2.0],
         'C_5': [3.0, -3.5],
         'name_anchor_C': [4.0, -6.0]}
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane104.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-6.981103617740445, 6.981103617740446], ylim=[-7.651935963581318, 6.310271271899573]) as c:
            for object_id, vertices, codes in [('outline_R', [self.points['R_0'], self.points['R_1'], self.points['R_2'], self.points['R_3'], self.points['R_4'], self.points['R_5'], self.points['R_0']], [1, 2, 2, 2, 2, 2, 79]), ('outline_A', [self.points['A_0'], self.points['A_1'], self.points['A_2'], self.points['A_3'], self.points['A_4'], self.points['A_5'], self.points['A_0']], [1, 2, 2, 2, 2, 2, 79]), ('outline_B', [self.points['B_0'], self.points['B_1'], self.points['B_2'], self.points['B_3'], self.points['B_4'], self.points['B_5'], self.points['B_0']], [1, 2, 2, 2, 2, 2, 79]), ('outline_C', [self.points['C_0'], self.points['C_1'], self.points['C_2'], self.points['C_3'], self.points['C_4'], self.points['C_5'], self.points['C_0']], [1, 2, 2, 2, 2, 2, 79])]:
                c.path(vertices, codes, id=object_id)
            for object_id, text, anchor in [('name_R', 'R', self.points['name_anchor_R']), ('name_A', 'A', self.points['name_anchor_A']), ('name_B', 'B', self.points['name_anchor_B']), ('name_C', 'C', self.points['name_anchor_C'])]:
                c.text(text, anchor, id=object_id, offset_pt=[0, -22], vertex=False)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane104().draw(sys.argv[1] if len(sys.argv) > 1 else None))
