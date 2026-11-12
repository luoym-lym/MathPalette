"""Frozen question Solid241; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Solid241:

    def __init__(self):
        self.id = 'Solid241'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:2850'
        self.question = 'In the diagram below, $ABCDEFGH$ is a rectangular prism, $\\angle BAF = 30^o$ and $\\angle DAH = 60^o$. What is the cosine of $\\angle CEG$?'
        self.answer = '\\frac{\\sqrt{130}}{13}'
        self.answer_type = 'number'
        self.query = self.question
        self.points = {'p000': [0.0, 0.0, 0],
         'p001': [0.0, 0.0, 1],
         'p010': [0.0, 0.5773502691896258, 0],
         'p011': [0.0, 0.5773502691896258, 1],
         'p100': [1.7320508075688772, 0.0, 0],
         'p101': [1.7320508075688772, 0.0, 1],
         'p110': [1.7320508075688772, 0.5773502691896258, 0],
         'p111': [1.7320508075688772, 0.5773502691896258, 1],
         'A': [0.0, 0.0, 0],
         'B': [1.7320508075688772, 0.0, 0],
         'C': [1.7320508075688772, 0.5773502691896258, 0],
         'D': [0.0, 0.5773502691896258, 0],
         'E': [0.0, 0.0, 1],
         'F': [1.7320508075688772, 0.0, 1],
         'G': [1.7320508075688772, 0.5773502691896258, 1],
         'H': [0.0, 0.5773502691896258, 1]}
        self.subject = 'SolidGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'SolidGeometry' / 'dataset_generator/scenes/Solid241.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('SolidGeometry', self.id, variant, output_path)
        with Canvas(SOLID, xlim=[-0.13557256597322742, 2.1104913774043377], ylim=[-0.41665507007167524, 1.8294088733058902], projection=[[1, 0.4, 0], [0, 0.7, 1]], origin=[0, 0, 0], offset=[0, 0]) as c:
            c.line(c.project([self.points['p000'], self.points['p100']]), id='line_0', clip_on=False, zorder=3)
            c.line(c.project([self.points['p000'], self.points['p010']]), id='line_1', linestyle=(0, [4, 3]), clip_on=False)
            for object_id, points in [('line_2', c.project([self.points['p000'], self.points['p001']])), ('line_3', c.project([self.points['p001'], self.points['p101']])), ('line_4', c.project([self.points['p001'], self.points['p011']]))]:
                c.line(points, id=object_id, clip_on=False, zorder=3)
            c.line(c.project([self.points['p010'], self.points['p110']]), id='line_5', linestyle=(0, [4, 3]), clip_on=False)
            c.line(c.project([self.points['p010'], self.points['p011']]), id='line_6', linestyle=(0, [4, 3]), clip_on=False)
            for object_id, points in [('line_7', c.project([self.points['p011'], self.points['p111']])), ('line_8', c.project([self.points['p100'], self.points['p110']])), ('line_9', c.project([self.points['p100'], self.points['p101']])), ('line_10', c.project([self.points['p101'], self.points['p111']])), ('line_11', c.project([self.points['p110'], self.points['p111']]))]:
                c.line(points, id=object_id, clip_on=False, zorder=3)
            c.text('A', c.project(self.points['A']), offset_pt=[-12, -13], vertex=True, id='label_0')
            c.text('B', c.project(self.points['B']), offset_pt=[10, -14], vertex=True, id='label_1')
            c.text('C', c.project(self.points['C']), offset_pt=[15, 0], vertex=True, id='label_2')
            c.text('D', c.project(self.points['D']), offset_pt=[10, -14], vertex=True, id='label_3')
            c.text('E', c.project(self.points['E']), offset_pt=[-14, 0], vertex=True, id='label_4')
            c.text('F', c.project(self.points['F']), offset_pt=[12, 0], vertex=True, id='label_5')
            c.text('G', c.project(self.points['G']), offset_pt=[12, 13], vertex=True, id='label_6')
            c.text('H', c.project(self.points['H']), offset_pt=[-10, 13], vertex=True, id='label_7')
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Solid241().draw(sys.argv[1] if len(sys.argv) > 1 else None))
