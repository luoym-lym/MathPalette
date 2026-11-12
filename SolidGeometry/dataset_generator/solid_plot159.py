"""Frozen question Solid159; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Solid159:

    def __init__(self):
        self.id = 'Solid159'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:1323'
        self.question = 'The diagram on the right shows a solid made up of 6 triangles. Each vertex is assigned a number, two of which are indicated. The total of the three numbers on each triangle is the same. What is the total of all five numbers?'
        self.answer = '17'
        self.answer_type = 'number'
        self.query = self.question
        self.points = {'L': [0, 0, 0], 'F': [1.66, -1, 0], 'R': [2.49, 0, 0.84], 'T': [1.39, -0.3, 1.4], 'B': [1.29, -0.3, -0.84]}
        self.subject = 'SolidGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'SolidGeometry' / 'dataset_generator/scenes/Solid159.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('SolidGeometry', self.id, variant, output_path)
        with Canvas(SOLID, xlim=[-0.15310670059892106, 2.556161314760404], ylim=[-1.0317330909298073, 1.677534924429518], projection=[[1, 0, 0], [0, 0, 1]], origin=[0, 0, 0], offset=[0, 0]) as c:
            c.line(c.project([self.points['L'], self.points['F']]), id='edgeLF', clip_on=False, zorder=3)
            c.line(c.project([self.points['F'], self.points['R']]), id='edgeFR', clip_on=False, zorder=3)
            c.line(c.project([self.points['L'], self.points['R']]), id='edgeLR', linestyle=(0, [4, 3]), clip_on=False)
            for object_id, points in [('edgeTL', c.project([self.points['T'], self.points['L']])), ('edgeTF', c.project([self.points['T'], self.points['F']])), ('edgeTR', c.project([self.points['T'], self.points['R']])), ('edgeBL', c.project([self.points['B'], self.points['L']])), ('edgeBF', c.project([self.points['B'], self.points['F']])), ('edgeBR', c.project([self.points['B'], self.points['R']]))]:
                c.line(points, id=object_id, clip_on=False, zorder=3)
            c.text('1', c.project(self.points['T']), offset_pt=[-12, 10], vertex=False, id='label1')
            c.text('5', c.project(self.points['L']), offset_pt=[-13, 0], vertex=False, id='label5')
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Solid159().draw(sys.argv[1] if len(sys.argv) > 1 else None))
