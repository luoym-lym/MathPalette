"""Frozen question Plane116; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane116:

    def __init__(self):
        self.id = 'Plane116'
        self.source_dataset = 'Author Designed'
        self.source_key = 'parallel:reference_PQ:detached_candidates_A_B_C'
        self.question = 'Which labeled segment A, B, or C is parallel to segment PQ? All segments are drawn to scale.\nChoices:\nA: Segment A\nB: Segment B\nC: Segment C'
        self.answer = 'A'
        self.answer_type = 'choice'
        self.choices = {'A': 'Segment A', 'B': 'Segment B', 'C': 'Segment C'}
        self.query = self.question
        self.points = {'P': [0, 4.8], 'Q': [2.8, 5.92], 'A1': [4.8, 5], 'A2': [7.6, 6.12], 'B1': [4.8, 2.7], 'B2': [7.6, 3.12], 'C1': [4.8, 0.2], 'C2': [7.6, 2.02]}
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane116.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-0.5855539405684755, 7.79562338501292], ylim=[-0.8812136627906977, 7.499963662790698]) as c:
            for object_id, points in [('PQ', [self.points['P'], self.points['Q']]), ('line_A', [self.points['A1'], self.points['A2']]), ('line_B', [self.points['B1'], self.points['B2']]), ('line_C', [self.points['C1'], self.points['C2']])]:
                c.line(points, id=object_id)
            c.text('P', self.points['P'], offset_pt=[-13, -13], vertex=True, ha='right', va='top', id='P_label')
            c.text('Q', self.points['Q'], offset_pt=[-2, 13], vertex=True, va='bottom', id='Q_label')
            c.text('A', self.points['A1'], offset_pt=[81.14894917833432, 49.692107054164154], vertex=False, id='A_tag')
            c.text('B', self.points['B1'], offset_pt=[84.71775275311607, 28.886661645892758], vertex=False, id='B_tag')
            c.text('C', self.points['C1'], offset_pt=[78.37138639047336, 70.02437786081019], vertex=False, id='C_tag')
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane116().draw(sys.argv[1] if len(sys.argv) > 1 else None))
