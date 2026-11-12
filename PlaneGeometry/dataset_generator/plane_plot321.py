"""Frozen question Plane321; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane321:

    def __init__(self):
        self.id = 'Plane321'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:1009'
        self.question = 'An equilateral triangle $A C D$ is rotated counterclockwise about point $A$. Through what angle has it rotated when it first covers equilateral triangle $A B C$?\nChoices:\nA:$60^{\\circ}$\nB:$120^{\\circ}$\nC:$180^{\\circ}$\nD:$240^{\\circ}$\nE:$300^{\\circ}$'
        self.answer = 'E'
        self.answer_type = 'choice'
        self.choices = {'A': '$60^{\\circ}$', 'B': '$120^{\\circ}$', 'C': '$180^{\\circ}$', 'D': '$240^{\\circ}$', 'E': '$300^{\\circ}$'}
        self.query = self.question
        self.points = {'B': [0, 5.196152422706632], 'A': [6, 5.196152422706632], 'C': [3, 0], 'D': [9, 0]}
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane321.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-0.32638266871959054, 9.359160079277684], ylim=[-2.218159019879188, 7.467383728118087]) as c:
            for object_id, points in [('o0', [self.points['A'], self.points['B']]), ('o1', [self.points['B'], self.points['C']]), ('o2', [self.points['C'], self.points['A']]), ('o3', [self.points['A'], self.points['D']]), ('o4', [self.points['D'], self.points['C']])]:
                c.line(points, id=object_id)
            c.text('B', self.points['B'], offset_pt=[0, 15], vertex=True, id='lB')
            c.text('A', self.points['A'], offset_pt=[0, 15], vertex=True, id='lA')
            c.text('C', self.points['C'], offset_pt=[0, -15], vertex=True, id='lC')
            c.text('D', self.points['D'], offset_pt=[0, -15], vertex=True, id='lD')
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane321().draw(sys.argv[1] if len(sys.argv) > 1 else None))
