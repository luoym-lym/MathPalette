"""Frozen question Plane115; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane115:

    def __init__(self):
        self.id = 'Plane115'
        self.source_dataset = 'Author Designed'
        self.source_key = 'straight-line-continuation:PO_beyond_O'
        self.question = 'Which labeled point A, B, or C lies on the straight-line continuation of segment PO beyond O?\nChoices:\nA: Point A\nB: Point B\nC: Point C'
        self.answer = 'A'
        self.answer_type = 'choice'
        self.choices = {'A': 'Point A', 'B': 'Point B', 'C': 'Point C'}
        self.query = self.question
        self.points = {'P': [0.0, 0.0], 'O': [3.0, 2.0], 'A': [6.0, 4.0], 'B': [6.0, 2.7], 'C': [6.0, 5.3]}
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane115.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-0.6057423859990472, 6.562513219332381], ylim=[-1.0343598046020168, 6.133895800729411]) as c:
            c.line([self.points['P'], self.points['O']], id='PO')
            for object_id, points in [('A_dot', [self.points['A']]), ('B_dot', [self.points['B']]), ('C_dot', [self.points['C']])]:
                c.point(points, id=object_id, filled=True)
            c.text('P', self.points['P'], offset_pt=[-20, -17], vertex=True, ha='right', id='P_label')
            c.text('O', self.points['O'], offset_pt=[0, -20], vertex=True, id='O_label')
            for object_id, text, anchor in [('A_label', 'A', self.points['A']), ('B_label', 'B', self.points['B']), ('C_label', 'C', self.points['C'])]:
                c.text(text, anchor, id=object_id, offset_pt=[15, 0], vertex=True, ha='left')
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane115().draw(sys.argv[1] if len(sys.argv) > 1 else None))
