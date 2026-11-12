"""Frozen question Plane103; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane103:

    def __init__(self):
        self.id = 'Plane103'
        self.source_dataset = 'Author Designed'
        self.source_key = 'visual-matching:l_outline'
        self.question = 'All shapes use the same scale. Which outline, A, B, or C, is congruent to R? Reflections are allowed.\nChoices:\nA: Outline A\nB: Outline B\nC: Outline C'
        self.answer = 'A'
        self.answer_type = 'choice'
        self.choices = {'A': 'Outline A', 'B': 'Outline B', 'C': 'Outline C'}
        self.query = self.question
        self.points = {'R0': [0, 7],
         'R1': [4, 7],
         'R2': [4, 8],
         'R3': [1, 8],
         'R4': [1, 10],
         'R5': [0, 10],
         'A0': [7, 6.5],
         'A1': [10, 6.5],
         'A2': [10, 10.5],
         'A3': [9, 10.5],
         'A4': [9, 7.5],
         'A5': [7, 7.5],
         'B0': [0, 0],
         'B1': [4, 0],
         'B2': [4, 2],
         'B3': [1, 2],
         'B4': [1, 3],
         'B5': [0, 3],
         'C0': [7, 0],
         'C1': [11, 0],
         'C2': [11, 1],
         'C3': [9, 1],
         'C4': [9, 3],
         'C5': [7, 3],
         'label_R': [2, 7],
         'label_A': [8.5, 6.5],
         'label_B': [2, 0],
         'label_C': [9, 0]}
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane103.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-0.41, 11.41], ylim=[-1.005, 10.815]) as c:
            for object_id, vertices, codes in [('R', [self.points['R0'], self.points['R1'], self.points['R2'], self.points['R3'], self.points['R4'], self.points['R5'], self.points['R0']], [1, 2, 2, 2, 2, 2, 79]), ('A', [self.points['A0'], self.points['A1'], self.points['A2'], self.points['A3'], self.points['A4'], self.points['A5'], self.points['A0']], [1, 2, 2, 2, 2, 2, 79]), ('B', [self.points['B0'], self.points['B1'], self.points['B2'], self.points['B3'], self.points['B4'], self.points['B5'], self.points['B0']], [1, 2, 2, 2, 2, 2, 79]), ('C', [self.points['C0'], self.points['C1'], self.points['C2'], self.points['C3'], self.points['C4'], self.points['C5'], self.points['C0']], [1, 2, 2, 2, 2, 2, 79])]:
                c.path(vertices, codes, id=object_id)
            for object_id, text, anchor in [('name_R', 'R', self.points['label_R']), ('name_A', 'A', self.points['label_A']), ('name_B', 'B', self.points['label_B']), ('name_C', 'C', self.points['label_C'])]:
                c.text(text, anchor, id=object_id, offset_pt=[0, -22], vertex=False)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane103().draw(sys.argv[1] if len(sys.argv) > 1 else None))
