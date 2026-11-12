"""Frozen question Solid75; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Solid75:

    def __init__(self):
        self.id = 'Solid75'
        self.source_dataset = 'Author Designed'
        self.source_key = 'regular-tetrahedron-net:opposite-edge-AD'
        self.question = 'The four equilateral triangles in the net fold to form a regular tetrahedron. Which edge is opposite AD? Opposite edges have no common endpoint. Choices:\nA: Edge BE\nB: Edge BC\nC: Edge CF\nD: None of these three edges'
        self.answer = 'B'
        self.answer_type = 'choice'
        self.choices = {'A': 'Edge BE', 'B': 'Edge BC', 'C': 'Edge CF', 'D': 'None of these three edges'}
        self.query = self.question
        self.points = {'A': [0.0, 0.0, 0.0],
         'B': [1.0, 0.0, 0.0],
         'C': [0.5, 0.8660254037844386, 0.0],
         'D': [0.5, -0.8660254037844386, 0.0],
         'E': [1.5, 0.8660254037844386, 0.0],
         'F': [-0.5, 0.8660254037844386, 0.0]}
        self.subject = 'SolidGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'SolidGeometry' / 'dataset_generator/scenes/Solid75.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('SolidGeometry', self.id, variant, output_path)
        with Canvas(SOLID, xlim=[-0.6492580056577061, 1.6527826121541414], ylim=[-1.1387820919044127, 1.1632585259074346], projection=[[1, 0, 0], [0, 1, 0]], origin=[0, 0, 0], offset=[0, 0]) as c:
            for object_id, points in [('edge_A_B', c.project([self.points['A'], self.points['B']])), ('edge_B_C', c.project([self.points['B'], self.points['C']])), ('edge_A_C', c.project([self.points['A'], self.points['C']])), ('edge_A_D', c.project([self.points['A'], self.points['D']])), ('edge_B_D', c.project([self.points['B'], self.points['D']])), ('edge_B_E', c.project([self.points['B'], self.points['E']])), ('edge_C_E', c.project([self.points['C'], self.points['E']])), ('edge_C_F', c.project([self.points['C'], self.points['F']])), ('edge_A_F', c.project([self.points['A'], self.points['F']]))]:
                c.line(points, id=object_id, clip_on=False, zorder=3)
            c.text('A', c.project(self.points['A']), offset_pt=[-15, -12], vertex=True, id='vertex_A')
            c.text('B', c.project(self.points['B']), offset_pt=[15, -12], vertex=True, id='vertex_B')
            c.text('C', c.project(self.points['C']), offset_pt=[0, 15], vertex=True, id='vertex_C')
            c.text('D', c.project(self.points['D']), offset_pt=[0, -10], vertex=True, id='vertex_D')
            c.text('E', c.project(self.points['E']), offset_pt=[15, 2], vertex=True, id='vertex_E')
            c.text('F', c.project(self.points['F']), offset_pt=[-15, 2], vertex=True, id='vertex_F')
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Solid75().draw(sys.argv[1] if len(sys.argv) > 1 else None))
