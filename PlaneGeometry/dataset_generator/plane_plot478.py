"""Frozen question Plane478; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane478:

    def __init__(self):
        self.id = 'Plane478'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:2715'
        self.question = 'How many rectangles are in this figure?'
        self.answer = '11'
        self.answer_type = 'number'
        self.query = self.question
        self.points = {'r00': [1, 2],
         'r01': [3, 2],
         'r02': [3, 4],
         'r03': [1, 4],
         'r10': [0, 1.5],
         'r11': [2.3, 1.5],
         'r12': [2.3, 2.5],
         'r13': [0, 2.5],
         'r20': [2, 0],
         'r21': [2.8, 0],
         'r22': [2.8, 3.3],
         'r23': [2, 3.3]}
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane478.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-0.5991358192260754, 3.605790911818668], ylim=[-0.10579330458637815, 4.099133426458366]) as c:
            for object_id, vertices, codes in [('r0', [self.points['r00'], self.points['r01'], self.points['r02'], self.points['r03'], self.points['r00']], [1, 2, 2, 2, 79]), ('r1', [self.points['r10'], self.points['r11'], self.points['r12'], self.points['r13'], self.points['r10']], [1, 2, 2, 2, 79]), ('r2', [self.points['r20'], self.points['r21'], self.points['r22'], self.points['r23'], self.points['r20']], [1, 2, 2, 2, 79])]:
                c.path(vertices, codes, id=object_id)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane478().draw(sys.argv[1] if len(sys.argv) > 1 else None))
