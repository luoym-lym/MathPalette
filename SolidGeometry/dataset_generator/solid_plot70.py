"""Frozen question Solid70; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Solid70:

    def __init__(self):
        self.id = 'Solid70'
        self.source_dataset = 'Author Designed'
        self.source_key = 'midpoint-cut:square_pyramid_corner'
        self.question = 'The pyramid shown has a square base and volume 480. Each marked point is the midpoint of the edge on which it lies. Find the volume of the part containing vertex A after the pyramid is cut along the shaded plane.'
        self.answer = 60
        self.answer_type = 'number'
        self.query = self.question
        self.points = {'A': [0, 0, 0], 'B': [12, 0, 0], 'C': [12, 12, 0], 'D': [0, 12, 0], 'S': [6, 6, 10], 'M': [6, 0, 0], 'N': [0, 6, 0]}
        self.subject = 'SolidGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'SolidGeometry' / 'dataset_generator/scenes/Solid70.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('SolidGeometry', self.id, variant, output_path)
        with Canvas(SOLID, xlim=[-6.983477957515103, 8.7834779575151], ylim=[-2.6261220524907607, 13.140833862539441], projection=[[-0.55, 0.7, 0.14], [0.25, 0.2, 0.85]], origin=[0, 0, 0], offset=[0, 0]) as c:
            c.fill(c.project([self.points['S'], self.points['M'], self.points['N']]), facecolor='#E6E6E6', alpha=1, id='cut_fill')
            c.line(c.project([self.points['C'], self.points['D']]), id='edge_CD', linestyle=(0, [4, 3]), clip_on=False)
            c.line(c.project([self.points['B'], self.points['C']]), id='edge_BC', linestyle=(0, [4, 3]), clip_on=False)
            for object_id, points in [('edge_AB', c.project([self.points['A'], self.points['B']])), ('edge_AD', c.project([self.points['A'], self.points['D']])), ('edge_AS', c.project([self.points['A'], self.points['S']])), ('edge_BS', c.project([self.points['B'], self.points['S']]))]:
                c.line(points, id=object_id, clip_on=False, zorder=3)
            c.line(c.project([self.points['C'], self.points['S']]), id='edge_CS', linestyle=(0, [4, 3]), clip_on=False)
            c.line(c.project([self.points['D'], self.points['S']]), id='edge_DS', clip_on=False, zorder=3)
            c.line(c.project([self.points['S'], self.points['M']]), id='section_SM', clip_on=False, zorder=3)
            c.line(c.project([self.points['M'], self.points['N']]), id='section_MN', linestyle=(0, [4, 3]), clip_on=False)
            c.line(c.project([self.points['N'], self.points['S']]), id='section_NS', clip_on=False, zorder=3)
            c.point(c.project([self.points['M']]), filled=True, id='midpoint_M')
            c.point(c.project([self.points['N']]), filled=True, id='midpoint_N')
            c.text('A', c.project(self.points['A']), offset_pt=[0, -8], vertex=True, va='top', id='label_A')
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Solid70().draw(sys.argv[1] if len(sys.argv) > 1 else None))
