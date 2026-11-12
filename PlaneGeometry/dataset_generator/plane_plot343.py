"""Frozen question Plane343; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane343:

    def __init__(self):
        self.id = 'Plane343'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:1142'
        self.question = 'The diagram shows a pentagon and indicates the length of each side. Five circles are drawn with centres A, B, C, D and E. On each side of the pentagon the two circles that are drawn around the ends of that side touch each other. Which point is the centre of the biggest circle?\nChoices:\nA:A\nB:B\nC:C\nD:D\nE:E'
        self.answer = 'A'
        self.answer_type = 'choice'
        self.choices = {'A': 'A', 'B': 'B', 'C': 'C', 'D': 'D', 'E': 'E'}
        self.query = self.question
        self.points = {'A': [0, 0],
         'B': [15, 5.5677643628300215],
         'C': [13.536601514252851, 19.491070897985846],
         'D': [-2.80484731669857, 24.176905946874832],
         'E': [-7.2665216769089715, 11.966522582563908],
         'mid0': [7.5, 2.7838821814150108],
         'mid1': [14.268300757126426, 12.529417630407934],
         'mid2': [5.3658770987771405, 21.833988422430338],
         'mid3': [-5.035684496803771, 18.07171426471937],
         'mid4': [-3.6332608384544858, 5.983261291281954]}
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane343.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-10.099579188323316, 17.75260773757492], ylim=[-1.7772556638362484, 26.074931262061988]) as c:
            c.path([self.points['A'], self.points['B'], self.points['C'], self.points['D'], self.points['E'], self.points['A']], [1, 2, 2, 2, 2, 79], id='pentagon')
            c.text('A', self.points['A'], offset_pt=[-6, -16], vertex=True, id='nameA')
            c.text('B', self.points['B'], offset_pt=[13, -6], vertex=True, id='nameB')
            c.text('C', self.points['C'], offset_pt=[10, 10], vertex=True, id='nameC')
            c.text('D', self.points['D'], offset_pt=[-5, 15], vertex=True, id='nameD')
            c.text('E', self.points['E'], offset_pt=[-15, 0], vertex=True, id='nameE')
            c.text('16', self.points['mid0'], offset_pt=[0, -17], vertex=False, id='length0')
            c.text('14', self.points['mid1'], offset_pt=[17, 0], vertex=False, id='length1')
            c.text('17', self.points['mid2'], offset_pt=[0, 16], vertex=False, id='length2')
            c.text('13', self.points['mid3'], offset_pt=[-16, 0], vertex=False, id='length3')
            c.text('14', self.points['mid4'], offset_pt=[-14, -3], vertex=False, id='length4')
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane343().draw(sys.argv[1] if len(sys.argv) > 1 else None))
