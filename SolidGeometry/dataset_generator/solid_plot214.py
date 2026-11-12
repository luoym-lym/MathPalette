"""Frozen question Solid214; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Solid214:

    def __init__(self):
        self.id = 'Solid214'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:2206'
        self.question = 'The centers of the faces of the right rectangular prism shown below are joined to create an octahedron. What is the volume of the octahedron?\n\nChoices:\nA:$\\frac{75}{12}$\nB:$10$\nC:$12$\nD:$10\\sqrt{2}$\nE:$15$'
        self.answer = 'B'
        self.answer_type = 'choice'
        self.choices = {'A': '$\\frac{75}{12}$', 'B': '$10$', 'C': '$12$', 'D': '$10\\sqrt{2}$', 'E': '$15$'}
        self.query = self.question
        self.points = {'p000': [0, 0, 0],
         'p001': [0, 0, 3],
         'p010': [0, 5, 0],
         'p011': [0, 5, 3],
         'p100': [4, 0, 0],
         'p101': [4, 0, 3],
         'p110': [4, 5, 0],
         'p111': [4, 5, 3],
         'A': [0, 0, 0],
         'B': [4, 0, 0],
         'C': [4, 5, 0],
         'D': [0, 5, 0],
         'E': [0, 0, 3],
         'F': [4, 0, 3],
         'G': [4, 5, 3],
         'H': [0, 5, 3],
         'd3': [0, 0, 1.5],
         'd4': [2, 0, 0],
         'd5': [4, 2.5, 0]}
        self.subject = 'SolidGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'SolidGeometry' / 'dataset_generator/scenes/Solid214.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('SolidGeometry', self.id, variant, output_path)
        with Canvas(SOLID, xlim=[-0.5041142903133959, 6.6803409935640055], ylim=[-1.4961588763986562, 5.688296407478745], projection=[[1, 0.5, 0], [-0.2, 0.4, 1]], origin=[0, 0, 0], offset=[0, 0]) as c:
            c.line(c.project([self.points['p000'], self.points['p100']]), id='line_0', clip_on=False, zorder=3)
            c.line(c.project([self.points['p000'], self.points['p010']]), id='line_1', linestyle=(0, [4, 3]), clip_on=False)
            for object_id, points in [('line_2', c.project([self.points['p000'], self.points['p001']])), ('line_3', c.project([self.points['p001'], self.points['p101']])), ('line_4', c.project([self.points['p001'], self.points['p011']]))]:
                c.line(points, id=object_id, clip_on=False, zorder=3)
            c.line(c.project([self.points['p010'], self.points['p110']]), id='line_5', linestyle=(0, [4, 3]), clip_on=False)
            c.line(c.project([self.points['p010'], self.points['p011']]), id='line_6', linestyle=(0, [4, 3]), clip_on=False)
            for object_id, points in [('line_7', c.project([self.points['p011'], self.points['p111']])), ('line_8', c.project([self.points['p100'], self.points['p110']])), ('line_9', c.project([self.points['p100'], self.points['p101']])), ('line_10', c.project([self.points['p101'], self.points['p111']])), ('line_11', c.project([self.points['p110'], self.points['p111']]))]:
                c.line(points, id=object_id, clip_on=False, zorder=3)
            c.text('3', c.project(self.points['d3']), offset_pt=[-20, 0], vertex=False, id='label_0')
            c.text('4', c.project(self.points['d4']), offset_pt=[0, -20], vertex=False, id='label_1')
            c.text('5', c.project(self.points['d5']), offset_pt=[18, -14], vertex=False, id='label_2')
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Solid214().draw(sys.argv[1] if len(sys.argv) > 1 else None))
