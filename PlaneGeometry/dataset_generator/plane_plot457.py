"""Frozen question Plane457; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane457:

    def __init__(self):
        self.id = 'Plane457'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:2581'
        self.question = 'The area of each of the four congruent L-shaped regions of this 100-inch by 100-inch square is 3/16 of the total area.  How many inches long is the side of the center square?'
        self.answer = '50'
        self.answer_type = 'number'
        self.query = self.question
        self.points = {'outer0': [0, 0],
         'outer1': [4, 0],
         'outer2': [4, 4],
         'outer3': [0, 4],
         'inner0': [1, 1],
         'inner1': [3, 1],
         'inner2': [3, 3],
         'inner3': [1, 3],
         'topa': [2, 4],
         'topb': [2, 3],
         'righta': [4, 2],
         'rightb': [3, 2],
         'bottoma': [2, 0],
         'bottomb': [2, 1],
         'lefta': [0, 2],
         'leftb': [1, 2]}
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane457.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-0.09913342645836565, 4.105793304586378], ylim=[-0.10579330458637859, 4.099133426458365]) as c:
            c.path([self.points['outer0'], self.points['outer1'], self.points['outer2'], self.points['outer3'], self.points['outer0']], [1, 2, 2, 2, 79], id='outer')
            c.path([self.points['inner0'], self.points['inner1'], self.points['inner2'], self.points['inner3'], self.points['inner0']], [1, 2, 2, 2, 79], id='inner')
            for object_id, points in [('top', [self.points['topa'], self.points['topb']]), ('right', [self.points['righta'], self.points['rightb']]), ('bottom', [self.points['bottoma'], self.points['bottomb']]), ('left', [self.points['lefta'], self.points['leftb']])]:
                c.line(points, id=object_id)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane457().draw(sys.argv[1] if len(sys.argv) > 1 else None))
