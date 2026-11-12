"""Frozen question Plane69; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane69:

    def __init__(self):
        self.id = 'Plane69'
        self.source_dataset = 'MathVista'
        self.source_key = 'testmini/920'
        self.question = 'The measure of angle BAC equals x*\\degree. What is the value of x?'
        self.answer = '30'
        self.answer_type = 'number'
        self.query = self.question
        self.points = {'A': [0.0, 12.0],
         'B': [0.0, 0.0],
         'C': [6.928203230275509, 0.0],
         'anchor7': [0.0, 6.0],
         'anchor9': [3.4641016151377544, 0.0],
         'anchor11': [3.4641016151377544, 6.0]}
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane69.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-3.544967519175769, 10.355983249451278], ylim=[-0.9489587316518229, 12.951992036975223]) as c:
            for object_id, points in [('segment4', [self.points['A'], self.points['B']]), ('segment5', [self.points['B'], self.points['C']]), ('segment6', [self.points['C'], self.points['A']])]:
                c.line(points, id=object_id)
            c.text('A', self.points['A'], offset_pt=[-2, 15], vertex=True, id='label1')
            c.text('B', self.points['B'], offset_pt=[-12, -10], vertex=True, id='label2')
            c.text('C', self.points['C'], offset_pt=[14, -9], vertex=True, id='label3')
            c.text('12', self.points['anchor7'], offset_pt=[-16, 0], vertex=False, id='text8')
            c.text('$4\\sqrt{3}$', self.points['anchor9'], offset_pt=[0, -16], vertex=False, id='text10')
            c.text('$8\\sqrt{3}$', self.points['anchor11'], offset_pt=[24, 3], vertex=False, id='text12')
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane69().draw(sys.argv[1] if len(sys.argv) > 1 else None))
