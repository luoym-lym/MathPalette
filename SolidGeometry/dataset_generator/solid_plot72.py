"""Frozen question Solid72; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Solid72:

    def __init__(self):
        self.id = 'Solid72'
        self.source_dataset = 'Author Designed'
        self.source_key = 'midpoint-cut:rectangular_prism_corner'
        self.question = 'The rectangular prism shown has volume 960. Each marked point is the midpoint of the edge on which it lies. Find the volume of the part containing vertex A after the prism is cut along the shaded plane.'
        self.answer = 40
        self.answer_type = 'number'
        self.query = self.question
        self.points = {'A': [0, 0, 0],
         'B': [10, 0, 0],
         'C': [10, 8, 0],
         'D': [0, 8, 0],
         'T': [0, 0, 12],
         'U': [10, 0, 12],
         'V': [10, 8, 12],
         'W': [0, 8, 12],
         'M': [5, 0, 0],
         'N': [0, 4, 0]}
        self.subject = 'SolidGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'SolidGeometry' / 'dataset_generator/scenes/Solid72.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('SolidGeometry', self.id, variant, output_path)
        with Canvas(SOLID, xlim=[-7.6668456833941105, 6.0869105355540745], ylim=[-0.9189339495038924, 12.834822269444292], projection=[[-0.6, 0.55, 0.0], [0.25, 0.2, 0.7]], origin=[0, 0, 0], offset=[0, 0]) as c:
            c.fill(c.project([self.points['T'], self.points['M'], self.points['N']]), facecolor='#E6E6E6', alpha=1, id='cut_fill')
            c.line(c.project([self.points['C'], self.points['D']]), id='edge_CD', linestyle=(0, [4, 3]), clip_on=False)
            c.line(c.project([self.points['B'], self.points['C']]), id='edge_BC', linestyle=(0, [4, 3]), clip_on=False)
            for object_id, points in [('edge_AB', c.project([self.points['A'], self.points['B']])), ('edge_AD', c.project([self.points['A'], self.points['D']])), ('edge_TU', c.project([self.points['T'], self.points['U']])), ('edge_UV', c.project([self.points['U'], self.points['V']])), ('edge_VW', c.project([self.points['V'], self.points['W']])), ('edge_TW', c.project([self.points['T'], self.points['W']])), ('edge_BU', c.project([self.points['B'], self.points['U']])), ('edge_AT', c.project([self.points['A'], self.points['T']]))]:
                c.line(points, id=object_id, clip_on=False, zorder=3)
            c.line(c.project([self.points['C'], self.points['V']]), id='edge_CV', linestyle=(0, [4, 3]), clip_on=False)
            c.line(c.project([self.points['D'], self.points['W']]), id='edge_DW', clip_on=False, zorder=3)
            c.line(c.project([self.points['T'], self.points['M']]), id='section_TM', clip_on=False, zorder=3)
            c.line(c.project([self.points['M'], self.points['N']]), id='section_MN', linestyle=(0, [4, 3]), clip_on=False)
            c.line(c.project([self.points['N'], self.points['T']]), id='section_NT', clip_on=False, zorder=3)
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
    print(Solid72().draw(sys.argv[1] if len(sys.argv) > 1 else None))
