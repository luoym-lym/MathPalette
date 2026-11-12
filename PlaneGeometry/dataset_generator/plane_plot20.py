"""Frozen question Plane20; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane20:

    def __init__(self):
        self.id = 'Plane20'
        self.source_dataset = 'MathVista'
        self.source_key = 'testmini/56'
        self.question = 'What is the perimeter of the rectangle?'
        self.answer = '6'
        self.answer_type = 'number'
        self.query = self.question
        self.points = {'A': [0.0, 0.0],
         'B': [1.0, 0.0],
         'C': [1.0, 2.0],
         'D': [0.0, 2.0],
         'textanchor0': [0.5, 0.0],
         'textanchor1': [0.5, 2.0],
         'textanchor2': [0.0, 1.0],
         'textanchor3': [1.0, 1.0]}
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane20.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-0.6582003429820744, 1.6545764353413912], ylim=[-0.1563883891617328, 2.156388389161733]) as c:
            c.path([self.points['A'], self.points['B'], self.points['C'], self.points['D'], self.points['A']], [1, 2, 2, 2, 79], id='o1')
            c.text('1 yd', self.points['textanchor0'], offset_pt=[0, -15], vertex=False, id='l1')
            c.text('1 yd', self.points['textanchor1'], offset_pt=[0, 15], vertex=False, id='l2')
            c.text('2 yd', self.points['textanchor2'], offset_pt=[-22, 0], vertex=False, id='l3')
            c.text('2 yd', self.points['textanchor3'], offset_pt=[22, 0], vertex=False, id='l4')
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane20().draw(sys.argv[1] if len(sys.argv) > 1 else None))
