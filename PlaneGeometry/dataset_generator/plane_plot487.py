"""Frozen question Plane487; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane487:

    def __init__(self):
        self.id = 'Plane487'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:2874'
        self.question = 'Determine the number of non-degenerate rectangles whose edges lie completely on the grid lines of the following figure.'
        self.answer = '297'
        self.answer_type = 'number'
        self.query = self.question
        self.points = {'l0_0_0a': [0, 0],
         'l0_0_0b': [0, 6],
         'l0_1_0a': [1, 0],
         'l0_1_0b': [1, 6],
         'l0_2_0a': [2, 0],
         'l0_2_0b': [2, 6],
         'l0_3_0a': [3, 0],
         'l0_3_0b': [3, 2],
         'l0_3_1a': [3, 4],
         'l0_3_1b': [3, 6],
         'l0_4_0a': [4, 0],
         'l0_4_0b': [4, 6],
         'l0_5_0a': [5, 0],
         'l0_5_0b': [5, 6],
         'l0_6_0a': [6, 0],
         'l0_6_0b': [6, 6],
         'l1_0_0a': [0, 0],
         'l1_0_0b': [6, 0],
         'l1_1_0a': [0, 1],
         'l1_1_0b': [6, 1],
         'l1_2_0a': [0, 2],
         'l1_2_0b': [6, 2],
         'l1_3_0a': [0, 3],
         'l1_3_0b': [2, 3],
         'l1_3_1a': [4, 3],
         'l1_3_1b': [6, 3],
         'l1_4_0a': [0, 4],
         'l1_4_0b': [6, 4],
         'l1_5_0a': [0, 5],
         'l1_5_0b': [6, 5],
         'l1_6_0a': [0, 6],
         'l1_6_0b': [6, 6]}
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane487.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-0.14870013968754936, 6.158689956879568], ylim=[-0.15868995687956833, 6.148700139687549]) as c:
            for object_id, points in [('l0_0_0', [self.points['l0_0_0a'], self.points['l0_0_0b']]), ('l0_1_0', [self.points['l0_1_0a'], self.points['l0_1_0b']]), ('l0_2_0', [self.points['l0_2_0a'], self.points['l0_2_0b']]), ('l0_3_0', [self.points['l0_3_0a'], self.points['l0_3_0b']]), ('l0_3_1', [self.points['l0_3_1a'], self.points['l0_3_1b']]), ('l0_4_0', [self.points['l0_4_0a'], self.points['l0_4_0b']]), ('l0_5_0', [self.points['l0_5_0a'], self.points['l0_5_0b']]), ('l0_6_0', [self.points['l0_6_0a'], self.points['l0_6_0b']]), ('l1_0_0', [self.points['l1_0_0a'], self.points['l1_0_0b']]), ('l1_1_0', [self.points['l1_1_0a'], self.points['l1_1_0b']]), ('l1_2_0', [self.points['l1_2_0a'], self.points['l1_2_0b']]), ('l1_3_0', [self.points['l1_3_0a'], self.points['l1_3_0b']]), ('l1_3_1', [self.points['l1_3_1a'], self.points['l1_3_1b']]), ('l1_4_0', [self.points['l1_4_0a'], self.points['l1_4_0b']]), ('l1_5_0', [self.points['l1_5_0a'], self.points['l1_5_0b']]), ('l1_6_0', [self.points['l1_6_0a'], self.points['l1_6_0b']])]:
                c.line(points, id=object_id)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane487().draw(sys.argv[1] if len(sys.argv) > 1 else None))
