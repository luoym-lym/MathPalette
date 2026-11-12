"""Frozen question Plane430; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane430:

    def __init__(self):
        self.id = 'Plane430'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:1908'
        self.question = "In the grid, each small square has side of length 1. What is the minimum distance from 'Start' to 'Finish' travelling only on edges or diagonals of the squares?\nChoices:\nA:$2 \\sqrt{2}$\nB:$\\sqrt{10}+\\sqrt{2}$\nC:$2+2 \\sqrt{2}$\nD:$4 \\sqrt{2}$\nE:$6$"
        self.answer = 'C'
        self.answer_type = 'choice'
        self.choices = {'A': '$2 \\sqrt{2}$', 'B': '$\\sqrt{10}+\\sqrt{2}$', 'C': '$2+2 \\sqrt{2}$', 'D': '$4 \\sqrt{2}$', 'E': '$6$'}
        self.query = self.question
        self.points = {'gva0': [0, 0],
         'gvb0': [0, 2],
         'gva1': [1, 0],
         'gvb1': [1, 2],
         'gva2': [2, 0],
         'gvb2': [2, 2],
         'gva3': [3, 0],
         'gvb3': [3, 2],
         'gva4': [4, 0],
         'gvb4': [4, 2],
         'gha0': [0, 0],
         'ghb0': [4, 0],
         'gha1': [0, 1],
         'ghb1': [4, 1],
         'gha2': [0, 2],
         'ghb2': [4, 2],
         'Start': [0, 2],
         'Ziel': [4, 0]}
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane430.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-0.12691745666567344, 4.133582239192938], ylim=[-1.1269223016330092, 3.1335773942256018]) as c:
            for object_id, points in [('gv0', [self.points['gva0'], self.points['gvb0']]), ('gv1', [self.points['gva1'], self.points['gvb1']]), ('gv2', [self.points['gva2'], self.points['gvb2']]), ('gv3', [self.points['gva3'], self.points['gvb3']]), ('gv4', [self.points['gva4'], self.points['gvb4']]), ('gh0', [self.points['gha0'], self.points['ghb0']]), ('gh1', [self.points['gha1'], self.points['ghb1']]), ('gh2', [self.points['gha2'], self.points['ghb2']])]:
                c.line(points, id=object_id)
            c.point([self.points['Start']], filled=True, id='start')
            c.point([self.points['Ziel']], filled=True, id='end')
            c.text('Start', self.points['Start'], offset_pt=[17, 18], vertex=False, id='startname')
            c.text('Finish', self.points['Ziel'], offset_pt=[-18, -20], vertex=False, id='zielname')
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane430().draw(sys.argv[1] if len(sys.argv) > 1 else None))
