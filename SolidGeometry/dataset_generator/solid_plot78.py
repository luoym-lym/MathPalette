"""Frozen question Solid78; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Solid78:

    def __init__(self):
        self.id = 'Solid78'
        self.source_dataset = 'Author Designed'
        self.source_key = 'solid82:net-edge-endpoint-identification'
        self.question = 'The figure shows a net of a square pyramid. After folding, which of the following edges has no endpoint in common with edge AB?\nChoices:\nA: Edge DE\nB: Edge CD\nC: Edge CE\nD: None of these three edges'
        self.answer = 'A'
        self.answer_type = 'choice'
        self.choices = {'A': 'Edge DE', 'B': 'Edge CD', 'C': 'Edge CE', 'D': 'None of these three edges'}
        self.query = self.question
        self.points = {'v00': [0.0, 0.0, 0.0],
         'v01': [1.0, 0.0, 0.0],
         'v02': [0.5, 1.118033988749895, 0.0],
         'v03': [1.6666666666666665, 0.7453559924999298, 0.0],
         'v04': [1.5555555555555556, 1.7391639824998364, 0.0],
         'v05': [0.7407407407407409, 2.3188853099997817, 0.0],
         'v06': [1.0, -1.0, 0.0],
         'v07': [0.0, -1.0, 0.0]}
        self.subject = 'SolidGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'SolidGeometry' / 'dataset_generator/scenes/Solid78.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('SolidGeometry', self.id, variant, output_path)
        with Canvas(SOLID, xlim=[-1.0690872749445486, 2.6044840987074416], ylim=[-1.0909815619277845, 2.5825898117242057], projection=[[1, 0, 0], [0, 1, 0]], origin=[0, 0, 0], offset=[0, 0]) as c:
            for object_id, points in [('edge_v00_v01', c.project([self.points['v00'], self.points['v01']])), ('edge_v01_v02', c.project([self.points['v01'], self.points['v02']])), ('edge_v00_v02', c.project([self.points['v00'], self.points['v02']])), ('edge_v01_v03', c.project([self.points['v01'], self.points['v03']])), ('edge_v02_v03', c.project([self.points['v02'], self.points['v03']])), ('edge_v03_v04', c.project([self.points['v03'], self.points['v04']])), ('edge_v02_v04', c.project([self.points['v02'], self.points['v04']])), ('edge_v04_v05', c.project([self.points['v04'], self.points['v05']])), ('edge_v02_v05', c.project([self.points['v02'], self.points['v05']])), ('edge_v01_v06', c.project([self.points['v01'], self.points['v06']])), ('edge_v06_v07', c.project([self.points['v06'], self.points['v07']])), ('edge_v00_v07', c.project([self.points['v00'], self.points['v07']]))]:
                c.line(points, id=object_id, clip_on=False, zorder=3)
            c.text('A', c.project(self.points['v00']), offset_pt=[-16.625578163355026, 3.548260240480185], vertex=True, id='label_A')
            c.text('B', c.project(self.points['v01']), offset_pt=[15.880930102366165, -6.065975526142535], vertex=True, id='label_B')
            c.text('C', c.project(self.points['v05']), offset_pt=[-6.262662537244549, 15.80439995522113], vertex=True, id='label_C')
            c.text('D', c.project(self.points['v04']), offset_pt=[14.651577535536417, 8.621558775544282], vertex=True, id='label_D')
            c.text('E', c.project(self.points['v02']), offset_pt=[-16.193848855066566, 5.172935265326576], vertex=True, id='label_E')
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Solid78().draw(sys.argv[1] if len(sys.argv) > 1 else None))
