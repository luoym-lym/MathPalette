"""Frozen question Plane471; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane471:

    def __init__(self):
        self.id = 'Plane471'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:2680'
        self.question = 'Tiles I, II, III and IV are translated so one tile coincides with each of the rectangles $A, B, C$ and $D$. In the final arrangement, the two numbers on any side common to two adjacent tiles must be the same. Which of the tiles is translated to Rectangle $C$?\n\nChoices:\nA:$I$\nB:$II$\nC:$III$\nD:$IV$\nE:$\\text{ cannot be determined}$'
        self.answer = 'D'
        self.answer_type = 'choice'
        self.choices = {'A': '$I$', 'B': '$II$', 'C': '$III$', 'D': '$IV$', 'E': '$\\text{ cannot be determined}$'}
        self.query = self.question
        self.points = {'tileI0': [0.0, 3],
         'tileI1': [3.0, 3],
         'tileI2': [3.0, 5.2],
         'tileI3': [0.0, 5.2],
         'nI': [1.5, 5.5],
         'vI0': [1.5, 4.9],
         'vI1': [2.75, 4.1],
         'vI2': [1.5, 3.3],
         'vI3': [0.25, 4.1],
         'tileII0': [3.2, 3],
         'tileII1': [6.2, 3],
         'tileII2': [6.2, 5.2],
         'tileII3': [3.2, 5.2],
         'nII': [4.7, 5.5],
         'vII0': [4.7, 4.9],
         'vII1': [5.95, 4.1],
         'vII2': [4.7, 3.3],
         'vII3': [3.45, 4.1],
         'tileIII0': [0.0, 0],
         'tileIII1': [3.0, 0],
         'tileIII2': [3.0, 2.2],
         'tileIII3': [0.0, 2.2],
         'nIII': [1.5, 2.5],
         'vIII0': [1.5, 1.9],
         'vIII1': [2.75, 1.1],
         'vIII2': [1.5, 0.3],
         'vIII3': [0.25, 1.1],
         'tileIV0': [3.2, 0],
         'tileIV1': [6.2, 0],
         'tileIV2': [6.2, 2.2],
         'tileIV3': [3.2, 2.2],
         'nIV': [4.7, 2.5],
         'vIV0': [4.7, 1.9],
         'vIV1': [5.95, 1.1],
         'vIV2': [4.7, 0.3],
         'vIV3': [3.45, 1.1],
         'slotA0': [7.5, 2.5],
         'slotA1': [10.5, 2.5],
         'slotA2': [10.5, 4.7],
         'slotA3': [7.5, 4.7],
         'nA': [9.0, 3.6],
         'slotB0': [10.5, 2.5],
         'slotB1': [13.5, 2.5],
         'slotB2': [13.5, 4.7],
         'slotB3': [10.5, 4.7],
         'nB': [12.0, 3.6],
         'slotC0': [7.5, 0.3],
         'slotC1': [10.5, 0.3],
         'slotC2': [10.5, 2.5],
         'slotC3': [7.5, 2.5],
         'nC': [9.0, 1.4000000000000001],
         'slotD0': [10.5, 0.3],
         'slotD1': [13.5, 0.3],
         'slotD2': [13.5, 2.5],
         'slotD3': [10.5, 2.5],
         'nD': [12.0, 1.4000000000000001]}
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane471.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-0.3345753142969823, 13.857052402979026], ylim=[-4.266257223454122, 9.925370493821886]) as c:
            for object_id, vertices, codes in [('tileI', [self.points['tileI0'], self.points['tileI1'], self.points['tileI2'], self.points['tileI3'], self.points['tileI0']], [1, 2, 2, 2, 79]), ('tileII', [self.points['tileII0'], self.points['tileII1'], self.points['tileII2'], self.points['tileII3'], self.points['tileII0']], [1, 2, 2, 2, 79]), ('tileIII', [self.points['tileIII0'], self.points['tileIII1'], self.points['tileIII2'], self.points['tileIII3'], self.points['tileIII0']], [1, 2, 2, 2, 79]), ('tileIV', [self.points['tileIV0'], self.points['tileIV1'], self.points['tileIV2'], self.points['tileIV3'], self.points['tileIV0']], [1, 2, 2, 2, 79]), ('slotA', [self.points['slotA0'], self.points['slotA1'], self.points['slotA2'], self.points['slotA3'], self.points['slotA0']], [1, 2, 2, 2, 79]), ('slotB', [self.points['slotB0'], self.points['slotB1'], self.points['slotB2'], self.points['slotB3'], self.points['slotB0']], [1, 2, 2, 2, 79]), ('slotC', [self.points['slotC0'], self.points['slotC1'], self.points['slotC2'], self.points['slotC3'], self.points['slotC0']], [1, 2, 2, 2, 79]), ('slotD', [self.points['slotD0'], self.points['slotD1'], self.points['slotD2'], self.points['slotD3'], self.points['slotD0']], [1, 2, 2, 2, 79])]:
                c.path(vertices, codes, id=object_id)
            for object_id, text, anchor in [('nI', 'I', self.points['nI']), ('vI0', '8', self.points['vI0']), ('vI1', '9', self.points['vI1']), ('vI2', '7', self.points['vI2']), ('vI3', '3', self.points['vI3']), ('nII', 'II', self.points['nII']), ('vII0', '6', self.points['vII0']), ('vII1', '3', self.points['vII1']), ('vII2', '2', self.points['vII2']), ('vII3', '4', self.points['vII3']), ('nIII', 'III', self.points['nIII']), ('vIII0', '7', self.points['vIII0']), ('vIII1', '5', self.points['vIII1']), ('vIII2', '0', self.points['vIII2']), ('vIII3', '1', self.points['vIII3']), ('nIV', 'IV', self.points['nIV']), ('vIV0', '2', self.points['vIV0']), ('vIV1', '1', self.points['vIV1']), ('vIV2', '6', self.points['vIV2']), ('vIV3', '9', self.points['vIV3']), ('nA', 'A', self.points['nA']), ('nB', 'B', self.points['nB']), ('nC', 'C', self.points['nC']), ('nD', 'D', self.points['nD'])]:
                c.text(text, anchor, id=object_id, offset_pt=[0, 0], vertex=False)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane471().draw(sys.argv[1] if len(sys.argv) > 1 else None))
