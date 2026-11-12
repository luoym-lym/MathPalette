"""Frozen question Plane420; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane420:

    def __init__(self):
        self.id = 'Plane420'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:1819'
        self.question = 'In the diagram there are 7 squares. What is the difference between the number of triangles and the number of squares in the diagram?'
        self.answer = '3'
        self.answer_type = 'number'
        self.query = self.question
        self.points = {'va0': [0, 0],
         'vb0': [0, 4],
         'va1': [1, 0],
         'vb1': [1, 3],
         'va2': [2, 0],
         'vb2': [2, 2],
         'va3': [3, 0],
         'vb3': [3, 1],
         'ha0': [0, 0],
         'hb0': [4, 0],
         'ha1': [0, 1],
         'hb1': [3, 1],
         'ha2': [0, 2],
         'hb2': [2, 2],
         'ha3': [0, 3],
         'hb3': [1, 3],
         'A': [0, 4],
         'B': [4, 0]}
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane420.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-0.09913342645836565, 4.105793304586378], ylim=[-0.10579330458637859, 4.099133426458365]) as c:
            for object_id, points in [('v0', [self.points['va0'], self.points['vb0']]), ('v1', [self.points['va1'], self.points['vb1']]), ('v2', [self.points['va2'], self.points['vb2']]), ('v3', [self.points['va3'], self.points['vb3']]), ('h0', [self.points['ha0'], self.points['hb0']]), ('h1', [self.points['ha1'], self.points['hb1']]), ('h2', [self.points['ha2'], self.points['hb2']]), ('h3', [self.points['ha3'], self.points['hb3']]), ('diagonal', [self.points['A'], self.points['B']])]:
                c.line(points, id=object_id)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane420().draw(sys.argv[1] if len(sys.argv) > 1 else None))
