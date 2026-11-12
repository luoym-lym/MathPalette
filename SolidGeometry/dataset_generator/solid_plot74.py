"""Frozen question Solid74; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Solid74:

    def __init__(self):
        self.id = 'Solid74'
        self.source_dataset = 'Author Designed'
        self.source_key = 'cube-net:vertex-coincidence'
        self.question = 'The figure shows a net made of six unit squares. When it is folded into a cube, which labeled point occupies the same cube vertex as P?\nChoices:\nA: Point Q\nB: Point R\nC: Point S\nD: None of these points'
        self.answer = 'B'
        self.answer_type = 'choice'
        self.choices = {'A': 'Point Q', 'B': 'Point R', 'C': 'Point S', 'D': 'None of these points'}
        self.query = self.question
        self.points = {'v0_0': [0.0, 0.0, 0.0],
         'v0_1': [0.0, 1.0, 0.0],
         'v1_0': [1.0, 0.0, 0.0],
         'v1_1': [1.0, 1.0, 0.0],
         'v1_2': [1.0, 2.0, 0.0],
         'v2_-1': [2.0, -1.0, 0.0],
         'v2_0': [2.0, 0.0, 0.0],
         'v2_1': [2.0, 1.0, 0.0],
         'v2_2': [2.0, 2.0, 0.0],
         'v3_-1': [3.0, -1.0, 0.0],
         'v3_0': [3.0, 0.0, 0.0],
         'v3_1': [3.0, 1.0, 0.0],
         'v4_0': [4.0, 0.0, 0.0],
         'v4_1': [4.0, 1.0, 0.0]}
        self.subject = 'SolidGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'SolidGeometry' / 'dataset_generator/scenes/Solid74.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('SolidGeometry', self.id, variant, output_path)
        with Canvas(SOLID, xlim=[-0.2784482720289403, 4.09723746072793], ylim=[-1.6698298632670028, 2.7058558694898682], projection=[[1, 0, 0], [0, 1, 0]], origin=[0, 0, 0], offset=[0, 0]) as c:
            for object_id, points in [('edge_v0_0_v1_0', c.project([self.points['v0_0'], self.points['v1_0']])), ('edge_v1_0_v1_1', c.project([self.points['v1_0'], self.points['v1_1']])), ('edge_v0_1_v1_1', c.project([self.points['v0_1'], self.points['v1_1']])), ('edge_v0_0_v0_1', c.project([self.points['v0_0'], self.points['v0_1']])), ('edge_v1_0_v2_0', c.project([self.points['v1_0'], self.points['v2_0']])), ('edge_v2_0_v2_1', c.project([self.points['v2_0'], self.points['v2_1']])), ('edge_v1_1_v2_1', c.project([self.points['v1_1'], self.points['v2_1']])), ('edge_v2_1_v2_2', c.project([self.points['v2_1'], self.points['v2_2']])), ('edge_v1_2_v2_2', c.project([self.points['v1_2'], self.points['v2_2']])), ('edge_v1_1_v1_2', c.project([self.points['v1_1'], self.points['v1_2']])), ('edge_v2_-1_v3_-1', c.project([self.points['v2_-1'], self.points['v3_-1']])), ('edge_v3_-1_v3_0', c.project([self.points['v3_-1'], self.points['v3_0']])), ('edge_v2_0_v3_0', c.project([self.points['v2_0'], self.points['v3_0']])), ('edge_v2_-1_v2_0', c.project([self.points['v2_-1'], self.points['v2_0']])), ('edge_v3_0_v3_1', c.project([self.points['v3_0'], self.points['v3_1']])), ('edge_v2_1_v3_1', c.project([self.points['v2_1'], self.points['v3_1']])), ('edge_v3_0_v4_0', c.project([self.points['v3_0'], self.points['v4_0']])), ('edge_v4_0_v4_1', c.project([self.points['v4_0'], self.points['v4_1']])), ('edge_v3_1_v4_1', c.project([self.points['v3_1'], self.points['v4_1']]))]:
                c.line(points, id=object_id, clip_on=False, zorder=3)
            c.text('P', c.project(self.points['v1_2']), offset_pt=[0, 16], vertex=True, id='P_label')
            c.text('Q', c.project(self.points['v3_-1']), offset_pt=[12, -12], vertex=True, id='Q_label')
            c.text('R', c.project(self.points['v0_1']), offset_pt=[-14, 0], vertex=True, id='R_label')
            c.text('S', c.project(self.points['v1_1']), offset_pt=[22, 17], vertex=True, id='S_label')
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Solid74().draw(sys.argv[1] if len(sys.argv) > 1 else None))
