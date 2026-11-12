"""Frozen question Solid71; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Solid71:

    def __init__(self):
        self.id = 'Solid71'
        self.source_dataset = 'Author Designed'
        self.source_key = 'midpoint-cut:triangular_prism_corner'
        self.question = 'The triangular prism shown has volume 504. Each marked point is the midpoint of the edge on which it lies. Find the volume of the part containing vertex A after the prism is cut along the shaded plane.'
        self.answer = 42
        self.answer_type = 'number'
        self.query = self.question
        self.points = {'A': [0, 0, 0], 'B': [12, 0, 0], 'C': [0, 7, 0], 'T': [0, 0, 12], 'U': [12, 0, 12], 'V': [0, 7, 12], 'M': [6, 0, 0], 'N': [0, 3.5, 0]}
        self.subject = 'SolidGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'SolidGeometry' / 'dataset_generator/scenes/Solid71.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('SolidGeometry', self.id, variant, output_path)
        with Canvas(SOLID, xlim=[-7.49184549297819, 4.509142039446911], ylim=[-0.9722550051596937, 11.028732527265408], projection=[[-0.6, 0.6, 0.0], [0.18, 0.3, 0.7]], origin=[0, 0, 0], offset=[0, 0]) as c:
            c.fill(c.project([self.points['T'], self.points['M'], self.points['N']]), facecolor='#E6E6E6', alpha=1, id='cut_fill')
            c.line(c.project([self.points['B'], self.points['C']]), id='edge_BC', linestyle=(0, [4, 3]), clip_on=False)
            for object_id, points in [('edge_AB', c.project([self.points['A'], self.points['B']])), ('edge_AC', c.project([self.points['A'], self.points['C']])), ('edge_TU', c.project([self.points['T'], self.points['U']])), ('edge_UV', c.project([self.points['U'], self.points['V']])), ('edge_TV', c.project([self.points['T'], self.points['V']])), ('edge_BU', c.project([self.points['B'], self.points['U']])), ('edge_AT', c.project([self.points['A'], self.points['T']])), ('edge_CV', c.project([self.points['C'], self.points['V']])), ('section_TM', c.project([self.points['T'], self.points['M']]))]:
                c.line(points, id=object_id, clip_on=False, zorder=3)
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
    print(Solid71().draw(sys.argv[1] if len(sys.argv) > 1 else None))
