"""Frozen question Plane122; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane122:

    def __init__(self):
        self.id = 'Plane122'
        self.source_dataset = 'Author Designed'
        self.source_key = 'reflection:point_P:line_l:candidates_A_B_C'
        self.question = 'Which labeled point is the reflection of P in the straight line l?\nChoices:\nA: Point A\nB: Point B\nC: Point C'
        self.answer = 'A'
        self.answer_type = 'choice'
        self.choices = {'A': 'Point A', 'B': 'Point B', 'C': 'Point C'}
        self.query = self.question
        self.points = {'L1': [0.54, 1.82],
         'L2': [6.94, 5.82],
         'P': [3.48, 6.62],
         'A': [6.142921348314605, 2.359325842696628],
         'B': [5.230561797752809, 1.7891011235955059],
         'C': [4.011685393258427, 1.0273033707865171],
         'H': [4.811460674157303, 4.489662921348314]}
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane122.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[0.38156223083548646, 7.096678509905254], ylim=[0.49270227713178283, 7.20781855620155]) as c:
            c.line([self.points['L1'], self.points['L2']], id='axis_l')
            for object_id, points in [('P_dot', [self.points['P']]), ('A_dot', [self.points['A']]), ('B_dot', [self.points['B']]), ('C_dot', [self.points['C']])]:
                c.point(points, id=object_id, filled=True)
            c.text('P', self.points['P'], offset_pt=[0, 16], vertex=True, id='P_label')
            c.text('A', self.points['A'], offset_pt=[9, -15], vertex=True, id='A_label')
            c.text('B', self.points['B'], offset_pt=[-9, -15], vertex=True, id='B_label')
            c.text('C', self.points['C'], offset_pt=[0, -16], vertex=True, id='C_label')
            c.text('l', self.points['L2'], offset_pt=[-13, 8], vertex=True, id='l_label')
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane122().draw(sys.argv[1] if len(sys.argv) > 1 else None))
