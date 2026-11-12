"""Frozen question Solid16; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Solid16:

    def __init__(self):
        self.id = 'Solid16'
        self.source_dataset = 'MathVerse'
        self.source_key = 's3634'
        self.question = 'Calculate the volume of the rectangular prism in the figure.'
        self.answer = '$1690cm^2$'
        self.answer_type = 'number'
        self.query = self.question
        self.points = {'A': [0, 0, 0],
         'B': [13, 0, 0],
         'C': [13, 13, 0],
         'D': [0, 13, 0],
         'E': [0, 0, 10],
         'F': [13, 0, 10],
         'G': [13, 13, 10],
         'H': [0, 13, 10],
         'M13a': [6.5, 0.0, 0.0],
         'M13b': [0, 6.5, 0],
         'M10': [13.0, 0.0, 5.0]}
        self.subject = 'SolidGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'SolidGeometry' / 'dataset_generator/scenes/Solid16.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('SolidGeometry', self.id, variant, output_path)
        with Canvas(SOLID, xlim=[-7.323381974383926, 16.234614796840887], ylim=[-6.0932863325595905, 17.464710438665225], projection=[[1, -0.52, 0], [0, 0.18, 1]], origin=[0, 0, 0], offset=[0, 0]) as c:
            for object_id, points in [('AB', c.project([self.points['A'], self.points['B']])), ('EF', c.project([self.points['E'], self.points['F']])), ('FG', c.project([self.points['F'], self.points['G']])), ('GH', c.project([self.points['G'], self.points['H']])), ('HE', c.project([self.points['H'], self.points['E']])), ('AE', c.project([self.points['A'], self.points['E']])), ('BF', c.project([self.points['B'], self.points['F']])), ('DA', c.project([self.points['D'], self.points['A']])), ('DH', c.project([self.points['D'], self.points['H']]))]:
                c.line(points, id=object_id, clip_on=False, zorder=3)
            c.text('13 cm', c.project(self.points['M13a']), offset_pt=[0, -17], vertex=False, id='dimension_13a')
            c.text('13 cm', c.project(self.points['M13b']), offset_pt=[-8, -19], vertex=False, id='dimension_13b')
            c.text('10 cm', c.project(self.points['M10']), offset_pt=[33, 0], vertex=False, id='dimension_10')
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Solid16().draw(sys.argv[1] if len(sys.argv) > 1 else None))
