"""Frozen question Plane107; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane107:

    def __init__(self):
        self.id = 'Plane107'
        self.source_dataset = 'Author Designed'
        self.source_key = 'visual-matching:segment_length'
        self.question = 'All segments use the same scale. Which segment, A, B, or C, has the same length as R?\nChoices:\nA: Segment A\nB: Segment B\nC: Segment C'
        self.answer = 'B'
        self.answer_type = 'choice'
        self.choices = {'A': 'Segment A', 'B': 'Segment B', 'C': 'Segment C'}
        self.query = self.question
        self.points = {'R_0': [-6.25, 4.0],
         'R_1': [-1.75, 4.0],
         'name_anchor_R': [-4.0, 4.0],
         'A_0': [1.7342305324083753, 2.9434543456482514],
         'A_1': [6.265769467591625, 5.056545654351749],
         'name_anchor_A': [4.0, 2.9434543456482514],
         'B_0': [-4.769545322482755, -6.114308396768294],
         'B_1': [-3.2304546775172454, -1.8856916032317068],
         'name_anchor_B': [-4.0, -6.114308396768294],
         'C_0': [2.2145840205067744, -3.3501617276812294],
         'C_1': [5.7854159794932265, -4.649838272318771],
         'name_anchor_C': [4.0, -4.649838272318771]}
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane107.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-6.54106440622306, 6.5568338738146865], ylim=[-7.472611878174656, 5.62528640186309]) as c:
            for object_id, points in [('segment_R', [self.points['R_0'], self.points['R_1']]), ('segment_A', [self.points['A_0'], self.points['A_1']]), ('segment_B', [self.points['B_0'], self.points['B_1']]), ('segment_C', [self.points['C_0'], self.points['C_1']])]:
                c.line(points, id=object_id)
            for object_id, text, anchor in [('name_R', 'R', self.points['name_anchor_R']), ('name_A', 'A', self.points['name_anchor_A']), ('name_B', 'B', self.points['name_anchor_B']), ('name_C', 'C', self.points['name_anchor_C'])]:
                c.text(text, anchor, id=object_id, offset_pt=[0, -22], vertex=False)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane107().draw(sys.argv[1] if len(sys.argv) > 1 else None))
