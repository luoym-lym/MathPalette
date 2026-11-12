"""Frozen question Solid243; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Solid243:

    def __init__(self):
        self.id = 'Solid243'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:2981'
        self.question = 'The right pyramid shown has a square base and all eight of its edges are the same length. What is the degree measure of angle $ABD$?'
        self.answer = '45'
        self.answer_type = 'number'
        self.query = self.question
        self.points = {'B': [-0.5, -0.5, 0], 'C': [0.5, -0.5, 0], 'D': [0.5, 0.5, 0], 'E': [-0.5, 0.5, 0], 'A': [0, 0, 0.7071067811865476]}
        self.subject = 'SolidGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'SolidGeometry' / 'dataset_generator/scenes/Solid243.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('SolidGeometry', self.id, variant, output_path)
        with Canvas(SOLID, xlim=[-1.0763039900117934, 1.1082969746363218], ylim=[-0.6058817899997693, 1.578719174648346], projection=[[1, 0.9, 0], [-0.1, 0.1, 1.5]], origin=[0, 0, 0], offset=[0, 0]) as c:
            for object_id, points in [('line_0', c.project([self.points['A'], self.points['B']])), ('line_1', c.project([self.points['A'], self.points['C']])), ('line_2', c.project([self.points['A'], self.points['D']])), ('line_3', c.project([self.points['B'], self.points['C']])), ('line_4', c.project([self.points['C'], self.points['D']]))]:
                c.line(points, id=object_id, clip_on=False, zorder=3)
            for object_id, points in [('line_5', c.project([self.points['A'], self.points['E']])), ('line_6', c.project([self.points['B'], self.points['E']])), ('line_7', c.project([self.points['E'], self.points['D']]))]:
                c.line(points, id=object_id, linestyle=(0, [4, 3]), clip_on=False)
            c.text('A', c.project(self.points['A']), offset_pt=[0, 18], vertex=True, id='label_0')
            c.text('B', c.project(self.points['B']), offset_pt=[-12, -15], vertex=True, id='label_1')
            c.text('C', c.project(self.points['C']), offset_pt=[0, -18], vertex=True, id='label_2')
            c.text('D', c.project(self.points['D']), offset_pt=[18, 0], vertex=True, id='label_3')
            c.text('E', c.project(self.points['E']), offset_pt=[-18, 12], vertex=True, id='label_4')
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Solid243().draw(sys.argv[1] if len(sys.argv) > 1 else None))
