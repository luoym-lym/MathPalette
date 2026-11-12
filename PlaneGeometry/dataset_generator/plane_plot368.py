"""Frozen question Plane368; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane368:

    def __init__(self):
        self.id = 'Plane368'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:1368'
        self.question = 'Six points are marked on a grid of unit squares as shown on the right. What is the smallest area of a triangle formed by three of these points?\nChoices:\nA:$1 / 2$\nB:$1 / 3$\nC:$1 / 4$\nD:1\nE:2'
        self.answer = 'A'
        self.answer_type = 'choice'
        self.choices = {'A': '$1 / 2$', 'B': '$1 / 3$', 'C': '$1 / 4$', 'D': '1', 'E': '2'}
        self.query = self.question
        self.points = {'v0a': [0, -0.25],
         'v0b': [0, 5.25],
         'v1a': [1, -0.25],
         'v1b': [1, 5.25],
         'v2a': [2, -0.25],
         'v2b': [2, 5.25],
         'v3a': [3, -0.25],
         'v3b': [3, 5.25],
         'v4a': [4, -0.25],
         'v4b': [4, 5.25],
         'v5a': [5, -0.25],
         'v5b': [5, 5.25],
         'h0a': [-0.25, 0],
         'h0b': [5.25, 0],
         'h1a': [-0.25, 1],
         'h1b': [5.25, 1],
         'h2a': [-0.25, 2],
         'h2b': [5.25, 2],
         'h3a': [-0.25, 3],
         'h3b': [5.25, 3],
         'h4a': [-0.25, 4],
         'h4b': [5.25, 4],
         'h5a': [-0.25, 5],
         'h5b': [5.25, 5],
         'P0': [1, 5],
         'P1': [4, 4],
         'P2': [0, 2],
         'P3': [0, 1],
         'P4': [5, 1],
         'P5': [3, 0]}
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane368.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-0.3863084613802523, 5.39546579380627], ylim=[-0.3954657938062698, 5.386308461380253]) as c:
            for object_id, points in [('v0', [self.points['v0a'], self.points['v0b']]), ('v1', [self.points['v1a'], self.points['v1b']]), ('v2', [self.points['v2a'], self.points['v2b']]), ('v3', [self.points['v3a'], self.points['v3b']]), ('v4', [self.points['v4a'], self.points['v4b']]), ('v5', [self.points['v5a'], self.points['v5b']]), ('h0', [self.points['h0a'], self.points['h0b']]), ('h1', [self.points['h1a'], self.points['h1b']]), ('h2', [self.points['h2a'], self.points['h2b']]), ('h3', [self.points['h3a'], self.points['h3b']]), ('h4', [self.points['h4a'], self.points['h4b']]), ('h5', [self.points['h5a'], self.points['h5b']])]:
                c.line(points, id=object_id)
            for object_id, points in [('dot0', [self.points['P0']]), ('dot1', [self.points['P1']]), ('dot2', [self.points['P2']]), ('dot3', [self.points['P3']]), ('dot4', [self.points['P4']]), ('dot5', [self.points['P5']])]:
                c.point(points, id=object_id, filled=True)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane368().draw(sys.argv[1] if len(sys.argv) > 1 else None))
