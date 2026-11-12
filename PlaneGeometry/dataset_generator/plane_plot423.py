"""Frozen question Plane423; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane423:

    def __init__(self):
        self.id = 'Plane423'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:1859'
        self.question = 'Six points are marked on a sheet of squared paper as shown. Which of the following shapes cannot be made by connecting some of these points using straight lines?\nChoices:\nA:parallelogram\nB:trapezium\nC:right-angled triangle\nD:obtuse-angled triangle\nE:all the shapes $\\mathrm{A}-\\mathrm{D}$ can be made'
        self.answer = 'E'
        self.answer_type = 'choice'
        self.choices = {'A': 'parallelogram',
         'B': 'trapezium',
         'C': 'right-angled triangle',
         'D': 'obtuse-angled triangle',
         'E': 'all the shapes $\\mathrm{A}-\\mathrm{D}$ can be made'}
        self.query = self.question
        self.points = {'v0a': [0, -0.25],
         'v0b': [0, 7.25],
         'v1a': [1, -0.25],
         'v1b': [1, 7.25],
         'v2a': [2, -0.25],
         'v2b': [2, 7.25],
         'v3a': [3, -0.25],
         'v3b': [3, 7.25],
         'v4a': [4, -0.25],
         'v4b': [4, 7.25],
         'v5a': [5, -0.25],
         'v5b': [5, 7.25],
         'v6a': [6, -0.25],
         'v6b': [6, 7.25],
         'v7a': [7, -0.25],
         'v7b': [7, 7.25],
         'v8a': [8, -0.25],
         'v8b': [8, 7.25],
         'h0a': [-0.25, 0],
         'h0b': [8.25, 0],
         'h1a': [-0.25, 1],
         'h1b': [8.25, 1],
         'h2a': [-0.25, 2],
         'h2b': [8.25, 2],
         'h3a': [-0.25, 3],
         'h3b': [8.25, 3],
         'h4a': [-0.25, 4],
         'h4b': [8.25, 4],
         'h5a': [-0.25, 5],
         'h5b': [8.25, 5],
         'h6a': [-0.25, 6],
         'h6b': [8.25, 6],
         'h7a': [-0.25, 7],
         'h7b': [8.25, 7],
         'P0': [6, 6],
         'P1': [3, 5],
         'P2': [7, 5],
         'P3': [1, 3],
         'P4': [5, 3],
         'P5': [3, 1]}
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane423.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-0.460658531224027, 8.474810772246055], ylim=[-0.9748056876146709, 7.960663615855411]) as c:
            for object_id, points in [('v0', [self.points['v0a'], self.points['v0b']]), ('v1', [self.points['v1a'], self.points['v1b']]), ('v2', [self.points['v2a'], self.points['v2b']]), ('v3', [self.points['v3a'], self.points['v3b']]), ('v4', [self.points['v4a'], self.points['v4b']]), ('v5', [self.points['v5a'], self.points['v5b']]), ('v6', [self.points['v6a'], self.points['v6b']]), ('v7', [self.points['v7a'], self.points['v7b']]), ('v8', [self.points['v8a'], self.points['v8b']]), ('h0', [self.points['h0a'], self.points['h0b']]), ('h1', [self.points['h1a'], self.points['h1b']]), ('h2', [self.points['h2a'], self.points['h2b']]), ('h3', [self.points['h3a'], self.points['h3b']]), ('h4', [self.points['h4a'], self.points['h4b']]), ('h5', [self.points['h5a'], self.points['h5b']]), ('h6', [self.points['h6a'], self.points['h6b']]), ('h7', [self.points['h7a'], self.points['h7b']])]:
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
    print(Plane423().draw(sys.argv[1] if len(sys.argv) > 1 else None))
