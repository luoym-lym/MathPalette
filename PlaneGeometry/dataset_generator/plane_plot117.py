"""Frozen question Plane117; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane117:

    def __init__(self):
        self.id = 'Plane117'
        self.source_dataset = 'Author Designed'
        self.source_key = 'perpendicularity:reference_PQ:candidates_OA_OB_OC'
        self.question = 'Which segment OA, OB, or OC is perpendicular to segment PQ? All segments are drawn to scale.\nChoices:\nA: Segment OA\nB: Segment OB\nC: Segment OC'
        self.answer = 'C'
        self.answer_type = 'choice'
        self.choices = {'A': 'Segment OA', 'B': 'Segment OB', 'C': 'Segment OC'}
        self.query = self.question
        self.points = {'P': [0.5, 4.2], 'Q': [3, 5.45], 'O': [6.3, 1], 'A': [6.3, 4.6], 'B': [3.754415587728429, 3.545584412271571], 'C': [4.690031056200151, 4.219937887599697]}
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane117.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[0.047923313001905665, 6.768743353664762], ylim=[-0.13818779810920567, 6.58263224255365]) as c:
            for object_id, points in [('PQ', [self.points['P'], self.points['Q']]), ('OA', [self.points['O'], self.points['A']]), ('OB', [self.points['O'], self.points['B']]), ('OC', [self.points['O'], self.points['C']])]:
                c.line(points, id=object_id)
            for object_id, points in [('P_dot', [self.points['P']]), ('Q_dot', [self.points['Q']]), ('O_dot', [self.points['O']]), ('A_dot', [self.points['A']]), ('B_dot', [self.points['B']]), ('C_dot', [self.points['C']])]:
                c.point(points, id=object_id, filled=True)
            c.text('P', self.points['P'], offset_pt=[-12, -13], vertex=True, ha='right', id='P_label')
            c.text('Q', self.points['Q'], offset_pt=[10, 10], vertex=True, ha='left', id='Q_label')
            c.text('O', self.points['O'], offset_pt=[10, -14], vertex=True, ha='left', id='O_label')
            c.text('A', self.points['A'], offset_pt=[0, 12], vertex=True, va='bottom', id='A_label')
            c.text('B', self.points['B'], offset_pt=[-12, 9], vertex=True, ha='right', id='B_label')
            c.text('C', self.points['C'], offset_pt=[3, 13], vertex=True, va='bottom', id='C_label')
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane117().draw(sys.argv[1] if len(sys.argv) > 1 else None))
