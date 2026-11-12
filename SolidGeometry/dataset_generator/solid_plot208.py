"""Frozen question Solid208; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Solid208:

    def __init__(self):
        self.id = 'Solid208'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:2078'
        self.question = 'Cube $ABCDEFGH$, labeled as shown below, has edge length $1$ and is cut by a plane passing through vertex $D$ and the midpoints $M$ and $N$ of $\\overline{AB}$ and $\\overline{CG}$ respectively. The plane divides the cube into two solids. The volume of the larger of the two solids can be written in the form $\\frac{p}{q}$, where $p$ and $q$ are relatively prime positive integers. Find $p+q$.'
        self.answer = '89'
        self.answer_type = 'number'
        self.query = self.question
        self.points = {'p000': [0, 0, 0],
         'p001': [0, 0, 1],
         'p010': [0, 1, 0],
         'p011': [0, 1, 1],
         'p100': [1, 0, 0],
         'p101': [1, 0, 1],
         'p110': [1, 1, 0],
         'p111': [1, 1, 1],
         'A': [0, 0, 0],
         'B': [1, 0, 0],
         'C': [1, 1, 0],
         'D': [0, 1, 0],
         'E': [0, 0, 1],
         'F': [1, 0, 1],
         'G': [1, 1, 1],
         'H': [0, 1, 1],
         'M': [0.5, 0, 0],
         'N': [1, 1, 0.5]}
        self.subject = 'SolidGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'SolidGeometry' / 'dataset_generator/scenes/Solid208.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('SolidGeometry', self.id, variant, output_path)
        with Canvas(SOLID, xlim=[-0.1198001759600491, 1.5169698417738975], ylim=[-0.1726129877953575, 1.464157029938589], projection=[[1, 0.4, 0], [0, 0.3, 1]], origin=[0, 0, 0], offset=[0, 0]) as c:
            c.line(c.project([self.points['p000'], self.points['p100']]), id='line_0', clip_on=False, zorder=3)
            c.line(c.project([self.points['p000'], self.points['p010']]), id='line_1', linestyle=(0, [4, 3]), clip_on=False)
            for object_id, points in [('line_2', c.project([self.points['p000'], self.points['p001']])), ('line_3', c.project([self.points['p001'], self.points['p101']])), ('line_4', c.project([self.points['p001'], self.points['p011']]))]:
                c.line(points, id=object_id, clip_on=False, zorder=3)
            c.line(c.project([self.points['p010'], self.points['p110']]), id='line_5', linestyle=(0, [4, 3]), clip_on=False)
            c.line(c.project([self.points['p010'], self.points['p011']]), id='line_6', linestyle=(0, [4, 3]), clip_on=False)
            for object_id, points in [('line_7', c.project([self.points['p011'], self.points['p111']])), ('line_8', c.project([self.points['p100'], self.points['p110']])), ('line_9', c.project([self.points['p100'], self.points['p101']])), ('line_10', c.project([self.points['p101'], self.points['p111']])), ('line_11', c.project([self.points['p110'], self.points['p111']]))]:
                c.line(points, id=object_id, clip_on=False, zorder=3)
            for object_id, points in [('dot_A', c.project([self.points['A']])), ('dot_B', c.project([self.points['B']])), ('dot_C', c.project([self.points['C']])), ('dot_D', c.project([self.points['D']])), ('dot_E', c.project([self.points['E']])), ('dot_F', c.project([self.points['F']])), ('dot_G', c.project([self.points['G']])), ('dot_H', c.project([self.points['H']])), ('dot_M', c.project([self.points['M']])), ('dot_N', c.project([self.points['N']]))]:
                c.point(points, id=object_id, filled=True)
            c.text('A', c.project(self.points['A']), offset_pt=[-18, -12], vertex=True, id='label_0')
            c.text('B', c.project(self.points['B']), offset_pt=[0, -21], vertex=True, id='label_1')
            c.text('C', c.project(self.points['C']), offset_pt=[18, -8], vertex=True, id='label_2')
            c.text('D', c.project(self.points['D']), offset_pt=[-18, 12], vertex=True, id='label_3')
            c.text('E', c.project(self.points['E']), offset_pt=[-18, 0], vertex=True, id='label_4')
            c.text('F', c.project(self.points['F']), offset_pt=[14, -14], vertex=True, id='label_5')
            c.text('G', c.project(self.points['G']), offset_pt=[17, 0], vertex=True, id='label_6')
            c.text('H', c.project(self.points['H']), offset_pt=[-16, 16], vertex=True, id='label_7')
            c.text('M', c.project(self.points['M']), offset_pt=[0, -20], vertex=True, id='label_8')
            c.text('N', c.project(self.points['N']), offset_pt=[18, 0], vertex=True, id='label_9')
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Solid208().draw(sys.argv[1] if len(sys.argv) > 1 else None))
