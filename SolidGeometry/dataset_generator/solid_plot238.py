"""Frozen question Solid238; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Solid238:

    def __init__(self):
        self.id = 'Solid238'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:2781'
        self.question = 'The figure below shows a polygon $ABCDEFGH$, consisting of rectangles and right triangles. When cut out and folded on the dotted lines, the polygon forms a triangular prism. Suppose that $AH = EF = 8$ and $GH = 14$. What is the volume of the prism?'
        self.answer = '192'
        self.answer_type = 'number'
        self.query = self.question
        self.points = {'B': [0, 10, 0],
         'G': [0, 0, 0],
         'C': [8, 10, 0],
         'F': [8, 0, 0],
         'J': [-4.8, 3.6, 0],
         'H': [-11.2, 8.4, 0],
         'A': [-6.4, 14.8, 0],
         'I': [12.8, 3.6, 0],
         'D': [17.6, -2.8, 0],
         'E': [12.8, -6.4, 0],
         'Ja': [-4.41, 4.12, 0.0],
         'Jb': [-3.8899999999999997, 3.73, 0.0],
         'Jc': [-4.279999999999999, 3.21, 0.0],
         'Ia': [12.41, 4.12, 0.0],
         'Ib': [11.89, 3.73, 0.0],
         'Ic': [12.280000000000001, 3.21, 0.0]}
        self.subject = 'SolidGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'SolidGeometry' / 'dataset_generator/scenes/Solid238.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('SolidGeometry', self.id, variant, output_path)
        with Canvas(SOLID, xlim=[-13.724759442853491, 20.056928297209616], ylim=[-12.599083332240856, 21.18260440782225], projection=[[1, 0, 0], [0, 1, 0]], origin=[0, 0, 0], offset=[0, 0]) as c:
            for object_id, points in [('line_0', c.project([self.points['A'], self.points['B']])), ('line_1', c.project([self.points['B'], self.points['C']])), ('line_2', c.project([self.points['C'], self.points['D']])), ('line_3', c.project([self.points['D'], self.points['E']])), ('line_4', c.project([self.points['E'], self.points['F']])), ('line_5', c.project([self.points['F'], self.points['G']])), ('line_6', c.project([self.points['G'], self.points['H']])), ('line_7', c.project([self.points['H'], self.points['A']]))]:
                c.line(points, id=object_id, clip_on=False, zorder=3)
            for object_id, points in [('line_8', c.project([self.points['B'], self.points['J']])), ('line_9', c.project([self.points['B'], self.points['G']])), ('line_10', c.project([self.points['C'], self.points['F']])), ('line_11', c.project([self.points['F'], self.points['I']]))]:
                c.line(points, id=object_id, linestyle=(0, [4, 3]), clip_on=False, zorder=3)
            for object_id, points in [('line_12', c.project([self.points['Ja'], self.points['Jb']])), ('line_13', c.project([self.points['Jb'], self.points['Jc']])), ('line_14', c.project([self.points['Ia'], self.points['Ib']])), ('line_15', c.project([self.points['Ib'], self.points['Ic']]))]:
                c.line(points, id=object_id, clip_on=False, zorder=3)
            for object_id, points in [('dotA', c.project([self.points['A']])), ('dotB', c.project([self.points['B']])), ('dotC', c.project([self.points['C']])), ('dotD', c.project([self.points['D']])), ('dotE', c.project([self.points['E']])), ('dotF', c.project([self.points['F']])), ('dotG', c.project([self.points['G']])), ('dotH', c.project([self.points['H']])), ('dotI', c.project([self.points['I']])), ('dotJ', c.project([self.points['J']]))]:
                c.point(points, id=object_id, filled=True)
            for object_id, text, anchor in [('label_0', 'A', c.project(self.points['A'])), ('label_1', 'B', c.project(self.points['B'])), ('label_2', 'C', c.project(self.points['C']))]:
                c.text(text, anchor, id=object_id, offset_pt=[0, 20], vertex=True)
            c.text('D', c.project(self.points['D']), offset_pt=[18, 0], vertex=True, id='label_3')
            for object_id, text, anchor in [('label_4', 'E', c.project(self.points['E'])), ('label_5', 'F', c.project(self.points['F'])), ('label_6', 'G', c.project(self.points['G']))]:
                c.text(text, anchor, id=object_id, offset_pt=[0, -20], vertex=True)
            c.text('H', c.project(self.points['H']), offset_pt=[-20, 0], vertex=True, id='label_7')
            c.text('I', c.project(self.points['I']), offset_pt=[20, 3], vertex=True, id='label_8')
            c.text('J', c.project(self.points['J']), offset_pt=[0, -20], vertex=True, id='label_9')
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Solid238().draw(sys.argv[1] if len(sys.argv) > 1 else None))
