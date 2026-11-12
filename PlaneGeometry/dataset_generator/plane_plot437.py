"""Frozen question Plane437; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane437:

    def __init__(self):
        self.id = 'Plane437'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:2030'
        self.question = 'A rectangle is divided into five smaller congruent rectangles as shown. When written in its lowest terms, the ratio of the side lengths of the smaller rectangle is $\\lambda: 1$, where $\\lambda<1$. What is the value of $360 \\lambda$?'
        self.answer = '120'
        self.answer_type = 'number'
        self.query = self.question
        self.points = {'left_0': [0, 0],
         'left_1': [1, 0],
         'left_2': [1, 3],
         'left_3': [0, 3],
         'right_0': [4, 0],
         'right_1': [5, 0],
         'right_2': [5, 3],
         'right_3': [4, 3],
         'middle0_0': [1, 0],
         'middle0_1': [4, 0],
         'middle0_2': [4, 1],
         'middle0_3': [1, 1],
         'middle1_0': [1, 1],
         'middle1_1': [4, 1],
         'middle1_2': [4, 2],
         'middle1_3': [1, 2],
         'middle2_0': [1, 2],
         'middle2_1': [4, 2],
         'middle2_2': [4, 3],
         'middle2_3': [1, 3]}
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane437.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-0.12391678307295706, 5.132241630732973], ylim=[-1.1322358728593835, 4.1239225409465465]) as c:
            for object_id, vertices, codes in [('left', [self.points['left_0'], self.points['left_1'], self.points['left_2'], self.points['left_3'], self.points['left_0']], [1, 2, 2, 2, 79]), ('right', [self.points['right_0'], self.points['right_1'], self.points['right_2'], self.points['right_3'], self.points['right_0']], [1, 2, 2, 2, 79]), ('middle0', [self.points['middle0_0'], self.points['middle0_1'], self.points['middle0_2'], self.points['middle0_3'], self.points['middle0_0']], [1, 2, 2, 2, 79]), ('middle1', [self.points['middle1_0'], self.points['middle1_1'], self.points['middle1_2'], self.points['middle1_3'], self.points['middle1_0']], [1, 2, 2, 2, 79]), ('middle2', [self.points['middle2_0'], self.points['middle2_1'], self.points['middle2_2'], self.points['middle2_3'], self.points['middle2_0']], [1, 2, 2, 2, 79])]:
                c.path(vertices, codes, id=object_id)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane437().draw(sys.argv[1] if len(sys.argv) > 1 else None))
