"""Frozen question Solid215; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Solid215:

    def __init__(self):
        self.id = 'Solid215'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:2220'
        self.question = 'In the rectangular parallelepiped shown, $AB = 3, BC= 1,$ and $CG = 2$. Point $M$ is the midpoint of $\\overline{FG}$. What is the volume of the rectangular pyramid with base $BCHE$ and apex $M$?\n\nChoices:\nA:$1$\nB:$\\frac{4}{3}$\nC:$\\frac{3}{2}$\nD:$\\frac{5}{3}$\nE:$2$'
        self.answer = 'E'
        self.answer_type = 'choice'
        self.choices = {'A': '$1$', 'B': '$\\frac{4}{3}$', 'C': '$\\frac{3}{2}$', 'D': '$\\frac{5}{3}$', 'E': '$2$'}
        self.query = self.question
        self.points = {'p000': [0, 0, 0],
         'p001': [0, 0, 2],
         'p010': [0, 1, 0],
         'p011': [0, 1, 2],
         'p100': [3, 0, 0],
         'p101': [3, 0, 2],
         'p110': [3, 1, 0],
         'p111': [3, 1, 2],
         'A': [0, 0, 0],
         'B': [3, 0, 0],
         'C': [3, 1, 0],
         'D': [0, 1, 0],
         'E': [0, 0, 2],
         'F': [3, 0, 2],
         'G': [3, 1, 2],
         'H': [0, 1, 2],
         'M': [3, 0.5, 2],
         'ab': [1.5, 0, 0],
         'bc': [3, 0.5, 0],
         'cg': [3, 1, 1]}
        self.subject = 'SolidGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'SolidGeometry' / 'dataset_generator/scenes/Solid215.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('SolidGeometry', self.id, variant, output_path)
        with Canvas(SOLID, xlim=[-0.28979590025899604, 3.94718884007381], ylim=[-0.7860994303515882, 3.450885309981218], projection=[[1, 0.65, 0], [0, 0.65, 1]], origin=[0, 0, 0], offset=[0, 0]) as c:
            c.line(c.project([self.points['p000'], self.points['p100']]), id='line_0', clip_on=False, zorder=3)
            c.line(c.project([self.points['p000'], self.points['p010']]), id='line_1', linestyle=(0, [4, 3]), clip_on=False)
            for object_id, points in [('line_2', c.project([self.points['p000'], self.points['p001']])), ('line_3', c.project([self.points['p001'], self.points['p101']])), ('line_4', c.project([self.points['p001'], self.points['p011']]))]:
                c.line(points, id=object_id, clip_on=False, zorder=3)
            c.line(c.project([self.points['p010'], self.points['p110']]), id='line_5', linestyle=(0, [4, 3]), clip_on=False)
            c.line(c.project([self.points['p010'], self.points['p011']]), id='line_6', linestyle=(0, [4, 3]), clip_on=False)
            for object_id, points in [('line_7', c.project([self.points['p011'], self.points['p111']])), ('line_8', c.project([self.points['p100'], self.points['p110']])), ('line_9', c.project([self.points['p100'], self.points['p101']])), ('line_10', c.project([self.points['p101'], self.points['p111']])), ('line_11', c.project([self.points['p110'], self.points['p111']])), ('line_12', c.project([self.points['E'], self.points['B']])), ('line_13', c.project([self.points['E'], self.points['M']])), ('line_14', c.project([self.points['H'], self.points['M']])), ('line_15', c.project([self.points['B'], self.points['M']])), ('line_16', c.project([self.points['C'], self.points['M']]))]:
                c.line(points, id=object_id, clip_on=False, zorder=3)
            c.line(c.project([self.points['H'], self.points['C']]), id='line_17', linestyle=(0, [4, 3]), clip_on=False)
            for object_id, points in [('dotA', c.project([self.points['A']])), ('dotB', c.project([self.points['B']])), ('dotC', c.project([self.points['C']])), ('dotD', c.project([self.points['D']])), ('dotE', c.project([self.points['E']])), ('dotF', c.project([self.points['F']])), ('dotG', c.project([self.points['G']])), ('dotH', c.project([self.points['H']])), ('dotM', c.project([self.points['M']]))]:
                c.point(points, id=object_id, filled=True)
            c.text('A', c.project(self.points['A']), offset_pt=[-15, -14], vertex=True, id='label_0')
            c.text('B', c.project(self.points['B']), offset_pt=[8, -18], vertex=True, id='label_1')
            c.text('C', c.project(self.points['C']), offset_pt=[16, -10], vertex=True, id='label_2')
            c.text('D', c.project(self.points['D']), offset_pt=[-18, 16], vertex=True, id='label_3')
            c.text('E', c.project(self.points['E']), offset_pt=[-18, 0], vertex=True, id='label_4')
            c.text('F', c.project(self.points['F']), offset_pt=[-15, -16], vertex=True, id='label_5')
            c.text('G', c.project(self.points['G']), offset_pt=[16, 12], vertex=True, id='label_6')
            c.text('H', c.project(self.points['H']), offset_pt=[-10, 18], vertex=True, id='label_7')
            c.text('M', c.project(self.points['M']), offset_pt=[0, 18], vertex=True, id='label_8')
            c.text('3', c.project(self.points['ab']), offset_pt=[0, -20], vertex=False, id='label_9')
            c.text('1', c.project(self.points['bc']), offset_pt=[15, -15], vertex=False, id='label_10')
            c.text('2', c.project(self.points['cg']), offset_pt=[20, 0], vertex=False, id='label_11')
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Solid215().draw(sys.argv[1] if len(sys.argv) > 1 else None))
