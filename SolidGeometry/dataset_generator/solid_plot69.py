"""Frozen question Solid69; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Solid69:

    def __init__(self):
        self.id = 'Solid69'
        self.source_dataset = 'Author Designed'
        self.source_key = 'midpoint-cut:tetrahedron_midpoint_quadrilateral'
        self.question = 'The tetrahedron shown has volume 288. Each marked point is the midpoint of the edge on which it lies. Find the volume of the part containing vertex A after the tetrahedron is cut along the shaded plane.'
        self.answer = 144
        self.answer_type = 'number'
        self.query = self.question
        self.points = {'A': [0, 0, 0], 'B': [12, 0, 0], 'C': [0, 8, 0], 'D': [0, 0, 18], 'M': [0, 4, 0], 'N': [0, 0, 9], 'P': [6, 0, 9], 'Q': [6, 4, 0]}
        self.subject = 'SolidGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'SolidGeometry' / 'dataset_generator/scenes/Solid69.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('SolidGeometry', self.id, variant, output_path)
        with Canvas(SOLID, xlim=[-5.23008677450906, 4.230086774509061], ylim=[-0.9288456473620674, 8.531327901656054], projection=[[0.0, -0.625, 0.2222222222222222], [0.6666666666666666, 0.375, 0.07500000000000001]], origin=[0, 0, 0], offset=[0, 0]) as c:
            c.fill(c.project([self.points['M'], self.points['N'], self.points['P'], self.points['Q']]), facecolor='#E6E6E6', alpha=1, id='cut_fill')
            for object_id, points in [('edge_BC', c.project([self.points['B'], self.points['C']])), ('edge_AB', c.project([self.points['A'], self.points['B']])), ('edge_AC', c.project([self.points['A'], self.points['C']])), ('edge_BD', c.project([self.points['B'], self.points['D']])), ('edge_AD', c.project([self.points['A'], self.points['D']]))]:
                c.line(points, id=object_id, clip_on=False, zorder=3)
            c.line(c.project([self.points['C'], self.points['D']]), id='edge_CD', linestyle=(0, [4, 3]), clip_on=False)
            c.line(c.project([self.points['M'], self.points['N']]), id='section_MN', linestyle=(0, [4, 3]), clip_on=False)
            c.line(c.project([self.points['N'], self.points['P']]), id='section_NP', clip_on=False, zorder=3)
            c.line(c.project([self.points['P'], self.points['Q']]), id='section_PQ', linestyle=(0, [4, 3]), clip_on=False)
            c.line(c.project([self.points['Q'], self.points['M']]), id='section_QM', clip_on=False, zorder=3)
            for object_id, points in [('midpoint_M', c.project([self.points['M']])), ('midpoint_N', c.project([self.points['N']])), ('midpoint_P', c.project([self.points['P']])), ('midpoint_Q', c.project([self.points['Q']]))]:
                c.point(points, id=object_id, filled=True)
            c.text('A', c.project(self.points['A']), offset_pt=[0, -8], vertex=True, va='top', id='label_A')
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Solid69().draw(sys.argv[1] if len(sys.argv) > 1 else None))
