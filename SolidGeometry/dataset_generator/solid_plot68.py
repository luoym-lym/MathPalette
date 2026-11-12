"""Frozen question Solid68; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Solid68:

    def __init__(self):
        self.id = 'Solid68'
        self.source_dataset = 'Author Designed'
        self.source_key = 'midpoint-cut:tetrahedron_edge_midpoint'
        self.question = 'The tetrahedron shown has volume 216. Each marked point is the midpoint of the edge on which it lies. Find the volume of the part containing vertex A after the tetrahedron is cut along the shaded plane.'
        self.answer = 108
        self.answer_type = 'number'
        self.query = self.question
        self.points = {'A': [0, 0, 0], 'B': [12, 0, 0], 'C': [0, 9, 0], 'D': [0, 0, 12], 'P': [0, 0, 6]}
        self.subject = 'SolidGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'SolidGeometry' / 'dataset_generator/scenes/Solid68.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('SolidGeometry', self.id, variant, output_path)
        with Canvas(SOLID, xlim=[-5.256004818401922, 5.271177227585009], ylim=[-1.2711772275850106, 9.256004818401921], projection=[[-0.4166666666666667, 0.5555555555555556, 0.0], [-0.16666666666666666, -0.2222222222222222, 0.5]], origin=[0, 0, 0], offset=[0, 2]) as c:
            c.fill(c.project([self.points['B'], self.points['C'], self.points['P']]), facecolor='#E6E6E6', alpha=1, id='cut_fill')
            for object_id, points in [('edge_BC', c.project([self.points['B'], self.points['C']])), ('edge_AB', c.project([self.points['A'], self.points['B']])), ('edge_AC', c.project([self.points['A'], self.points['C']])), ('edge_BD', c.project([self.points['B'], self.points['D']])), ('edge_AD', c.project([self.points['A'], self.points['D']])), ('edge_CD', c.project([self.points['C'], self.points['D']])), ('section_CP', c.project([self.points['C'], self.points['P']])), ('section_PB', c.project([self.points['P'], self.points['B']]))]:
                c.line(points, id=object_id, clip_on=False, zorder=3)
            c.point(c.project([self.points['P']]), filled=True, id='midpoint_P')
            c.text('A', c.project(self.points['A']), offset_pt=[8, 6], vertex=True, ha='left', va='bottom', id='label_A')
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Solid68().draw(sys.argv[1] if len(sys.argv) > 1 else None))
