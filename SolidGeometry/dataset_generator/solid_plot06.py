"""Frozen question Solid06; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Solid06:

    def __init__(self):
        self.id = 'Solid06'
        self.source_dataset = 'MathVerse'
        self.source_key = 's3414'
        self.question = 'Find the length of AF in terms of AB, BD and DF.'
        self.answer = '\\[\\sqrt{AB^2+BD^2+DF^2}\\]'
        self.answer_type = 'expression'
        self.query = self.question
        self.points = {'A': [0, 0, 0], 'B': [3, 0, 0], 'C': [0, 4, 0], 'D': [3, 4, 0], 'E': [0, 4, 5], 'F': [3, 4, 5]}
        self.subject = 'SolidGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'SolidGeometry' / 'dataset_generator/scenes/Solid06.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('SolidGeometry', self.id, variant, output_path)
        with Canvas(SOLID, xlim=[-1.0851149429061415, 9.07880565427854], ylim=[-2.383887773084407, 7.7800328241002745], projection=[[1, 1.2564935064935063, 0], [-0.5974025974025974, 0.3214285714285714, 1.1688311688311688]], origin=[0, 0, 0], offset=[0, 0]) as c:
            c.line(c.project([self.points['A'], self.points['B']]), id='AB', clip_on=False, zorder=3)
            c.line(c.project([self.points['A'], self.points['C']]), id='AC', linestyle=(0, [4, 3]), clip_on=False)
            c.line(c.project([self.points['C'], self.points['E']]), id='CE', linestyle=(0, [4, 3]), clip_on=False)
            for object_id, points in [('EA', c.project([self.points['E'], self.points['A']])), ('BD', c.project([self.points['B'], self.points['D']])), ('DF', c.project([self.points['D'], self.points['F']])), ('FB', c.project([self.points['F'], self.points['B']]))]:
                c.line(points, id=object_id, clip_on=False, zorder=3)
            c.line(c.project([self.points['C'], self.points['D']]), id='CD', linestyle=(0, [4, 3]), clip_on=False)
            c.line(c.project([self.points['E'], self.points['F']]), id='EF', clip_on=False, zorder=3)
            c.line(c.project([self.points['A'], self.points['F']]), id='AF_target', clip_on=False, zorder=3)
            c.text('A', c.project(self.points['A']), offset_pt=[-9, -3], vertex=True, id='vertex_A')
            c.text('B', c.project(self.points['B']), offset_pt=[0, -13], vertex=True, id='vertex_B')
            c.text('C', c.project(self.points['C']), offset_pt=[-15, 13], vertex=True, id='vertex_C')
            c.text('D', c.project(self.points['D']), offset_pt=[9, -5], vertex=True, id='vertex_D')
            c.text('E', c.project(self.points['E']), offset_pt=[0, 12], vertex=True, id='vertex_E')
            c.text('F', c.project(self.points['F']), offset_pt=[8, 9], vertex=True, id='vertex_F')
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Solid06().draw(sys.argv[1] if len(sys.argv) > 1 else None))
