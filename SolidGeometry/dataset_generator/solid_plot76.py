"""Frozen question Solid76; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Solid76:

    def __init__(self):
        self.id = 'Solid76'
        self.source_dataset = 'Author Designed'
        self.source_key = 'solid80:net-edge-endpoint-identification'
        self.question = 'The figure shows a net of a cube. After folding, which of the following edges has no endpoint in common with edge AB?\nChoices:\nA: Edge CD\nB: Edge CE\nC: Edge DF\nD: None of these three edges'
        self.answer = 'C'
        self.answer_type = 'choice'
        self.choices = {'A': 'Edge CD', 'B': 'Edge CE', 'C': 'Edge DF', 'D': 'None of these three edges'}
        self.query = self.question
        self.points = {'v00': [0.0, 0.0, 0.0],
         'v01': [1.0, 0.0, 0.0],
         'v02': [1.0, 1.0, 0.0],
         'v03': [0.0, 1.0, 0.0],
         'v04': [1.0, -1.0, 0.0],
         'v05': [0.0, -1.0, 0.0],
         'v06': [2.0, 1.0, 0.0],
         'v07': [2.0, 0.0, 0.0],
         'v08': [0.0, 2.0, 0.0],
         'v09': [1.0, 2.0, 0.0],
         'v10': [-1.0, 0.0, 0.0],
         'v11': [-1.0, 1.0, 0.0],
         'v12': [3.0, 0.0, 0.0],
         'v13': [3.0, 1.0, 0.0]}
        self.subject = 'SolidGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'SolidGeometry' / 'dataset_generator/scenes/Solid76.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('SolidGeometry', self.id, variant, output_path)
        with Canvas(SOLID, xlim=[-1.2513832967391, 3.1079658886499373], ylim=[-1.7516644263061463, 2.607684759082891], projection=[[1, 0, 0], [0, 1, 0]], origin=[0, 0, 0], offset=[0, 0]) as c:
            for object_id, points in [('edge_v00_v01', c.project([self.points['v00'], self.points['v01']])), ('edge_v01_v02', c.project([self.points['v01'], self.points['v02']])), ('edge_v02_v03', c.project([self.points['v02'], self.points['v03']])), ('edge_v00_v03', c.project([self.points['v00'], self.points['v03']])), ('edge_v01_v04', c.project([self.points['v01'], self.points['v04']])), ('edge_v04_v05', c.project([self.points['v04'], self.points['v05']])), ('edge_v00_v05', c.project([self.points['v00'], self.points['v05']])), ('edge_v02_v06', c.project([self.points['v02'], self.points['v06']])), ('edge_v06_v07', c.project([self.points['v06'], self.points['v07']])), ('edge_v01_v07', c.project([self.points['v01'], self.points['v07']])), ('edge_v03_v08', c.project([self.points['v03'], self.points['v08']])), ('edge_v08_v09', c.project([self.points['v08'], self.points['v09']])), ('edge_v02_v09', c.project([self.points['v02'], self.points['v09']])), ('edge_v00_v10', c.project([self.points['v00'], self.points['v10']])), ('edge_v10_v11', c.project([self.points['v10'], self.points['v11']])), ('edge_v03_v11', c.project([self.points['v03'], self.points['v11']])), ('edge_v07_v12', c.project([self.points['v07'], self.points['v12']])), ('edge_v06_v13', c.project([self.points['v06'], self.points['v13']])), ('edge_v12_v13', c.project([self.points['v12'], self.points['v13']]))]:
                c.line(points, id=object_id, clip_on=False, zorder=3)
            c.text('A', c.project(self.points['v05']), offset_pt=[-12.02081528017131, -12.020815280171307], vertex=True, id='label_A')
            c.text('B', c.project(self.points['v04']), offset_pt=[12.020815280171306, -12.02081528017131], vertex=True, id='label_B')
            c.text('C', c.project(self.points['v10']), offset_pt=[-12.02081528017131, -12.020815280171307], vertex=True, id='label_C')
            c.text('D', c.project(self.points['v00']), offset_pt=[12.020815280171306, -12.02081528017131], vertex=True, id='label_D')
            c.text('E', c.project(self.points['v11']), offset_pt=[-12.020815280171307, 12.020815280171309], vertex=True, id='label_E')
            c.text('F', c.project(self.points['v03']), offset_pt=[12.020815280171306, -12.02081528017131], vertex=True, id='label_F')
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Solid76().draw(sys.argv[1] if len(sys.argv) > 1 else None))
