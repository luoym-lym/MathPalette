"""Frozen question Solid77; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Solid77:

    def __init__(self):
        self.id = 'Solid77'
        self.source_dataset = 'Author Designed'
        self.source_key = 'solid81:net-edge-endpoint-identification'
        self.question = 'The figure shows a net of a right triangular prism with equilateral triangular bases. After folding, which of the following edges has no endpoint in common with edge AB?\nChoices:\nA: Edge CE\nB: Edge DE\nC: Edge CD\nD: None of these three edges'
        self.answer = 'B'
        self.answer_type = 'choice'
        self.choices = {'A': 'Edge CE', 'B': 'Edge DE', 'C': 'Edge CD', 'D': 'None of these three edges'}
        self.query = self.question
        self.points = {'v00': [0.0, 0.0, 0.0],
         'v01': [1.0, 0.0, 0.0],
         'v02': [0.5, 0.8660254037844386, 0.0],
         'v03': [1.0, -1.35, 0.0],
         'v04': [0.0, -1.35, 0.0],
         'v05': [1.669134295108992, 1.5410254037844389, 0.0],
         'v06': [2.169134295108992, 0.6750000000000002, 0.0],
         'v07': [-1.1691342951089922, 0.6750000000000002, 0.0],
         'v08': [-0.6691342951089921, 1.5410254037844389, 0.0],
         'v09': [2.669134295108992, 1.5410254037844386, 0.0]}
        self.subject = 'SolidGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'SolidGeometry' / 'dataset_generator/scenes/Solid77.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('SolidGeometry', self.id, variant, output_path)
        with Canvas(SOLID, xlim=[-1.267295072236705, 2.94183927741128], ylim=[-1.9747766719168385, 2.2343576777311465], projection=[[1, 0, 0], [0, 1, 0]], origin=[0, 0, 0], offset=[0, 0]) as c:
            for object_id, points in [('edge_v00_v01', c.project([self.points['v00'], self.points['v01']])), ('edge_v01_v02', c.project([self.points['v01'], self.points['v02']])), ('edge_v00_v02', c.project([self.points['v00'], self.points['v02']])), ('edge_v01_v03', c.project([self.points['v01'], self.points['v03']])), ('edge_v03_v04', c.project([self.points['v03'], self.points['v04']])), ('edge_v00_v04', c.project([self.points['v00'], self.points['v04']])), ('edge_v02_v05', c.project([self.points['v02'], self.points['v05']])), ('edge_v05_v06', c.project([self.points['v05'], self.points['v06']])), ('edge_v01_v06', c.project([self.points['v01'], self.points['v06']])), ('edge_v00_v07', c.project([self.points['v00'], self.points['v07']])), ('edge_v07_v08', c.project([self.points['v07'], self.points['v08']])), ('edge_v02_v08', c.project([self.points['v02'], self.points['v08']])), ('edge_v06_v09', c.project([self.points['v06'], self.points['v09']])), ('edge_v05_v09', c.project([self.points['v05'], self.points['v09']]))]:
                c.line(points, id=object_id, clip_on=False, zorder=3)
            c.text('A', c.project(self.points['v00']), offset_pt=[-14.722431864335457, -8.500000000000002], vertex=True, id='label_A')
            c.text('B', c.project(self.points['v04']), offset_pt=[-12.02081528017131, -12.020815280171307], vertex=True, id='label_B')
            c.text('C', c.project(self.points['v09']), offset_pt=[14.722431864335464, 8.499999999999988], vertex=True, id='label_C')
            c.text('D', c.project(self.points['v06']), offset_pt=[12.020815280171306, -12.02081528017131], vertex=True, id='label_D')
            c.text('E', c.project(self.points['v05']), offset_pt=[-4.399923766742843, 16.420739046914164], vertex=True, id='label_E')
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Solid77().draw(sys.argv[1] if len(sys.argv) > 1 else None))
