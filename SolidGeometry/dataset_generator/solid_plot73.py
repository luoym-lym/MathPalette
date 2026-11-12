"""Frozen question Solid73; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Solid73:

    def __init__(self):
        self.id = 'Solid73'
        self.source_dataset = 'Author Designed'
        self.source_key = 'triangular-prism-net:lateral-edge-from-P'
        self.question = 'The figure shows a net of a right triangular prism with equilateral triangular bases. The three rectangles are joined along the common edges shown. When the net is folded into the prism, which labeled point is the other endpoint of the lateral edge with one endpoint at P?\nChoices:\nA: Point Q\nB: Point R\nC: Point S\nD: None of these three points'
        self.answer = 'B'
        self.answer_type = 'choice'
        self.choices = {'A': 'Point Q', 'B': 'Point R', 'C': 'Point S', 'D': 'None of these three points'}
        self.query = self.question
        self.points = {'T0': [0.0, 1.5, 0.0],
         'T1': [1.0, 1.5, 0.0],
         'T2': [2.0, 1.5, 0.0],
         'T3': [3.0, 1.5, 0.0],
         'B0': [0.0, 0.0, 0.0],
         'B1': [1.0, 0.0, 0.0],
         'B2': [2.0, 0.0, 0.0],
         'B3': [3.0, 0.0, 0.0],
         'P': [0.5, 2.3660254037844384, 0.0],
         'Q': [2.5, -0.8660254037844386, 0.0]}
        self.subject = 'SolidGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'SolidGeometry' / 'dataset_generator/scenes/Solid73.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('SolidGeometry', self.id, variant, output_path)
        with Canvas(SOLID, xlim=[-0.3194144470766229, 3.4524195679314893], ylim=[-1.1292619149114638, 2.6425721000966487], projection=[[1, 0, 0], [0, 1, 0]], origin=[0, 0, 0], offset=[0, 0]) as c:
            for object_id, points in [('net_edge_B0_B1', c.project([self.points['B0'], self.points['B1']])), ('net_edge_B1_T1', c.project([self.points['B1'], self.points['T1']])), ('net_edge_T0_T1', c.project([self.points['T0'], self.points['T1']])), ('net_edge_B0_T0', c.project([self.points['B0'], self.points['T0']])), ('net_edge_B1_B2', c.project([self.points['B1'], self.points['B2']])), ('net_edge_B2_T2', c.project([self.points['B2'], self.points['T2']])), ('net_edge_T1_T2', c.project([self.points['T1'], self.points['T2']])), ('net_edge_B2_B3', c.project([self.points['B2'], self.points['B3']])), ('net_edge_B3_T3', c.project([self.points['B3'], self.points['T3']])), ('net_edge_T2_T3', c.project([self.points['T2'], self.points['T3']])), ('net_edge_P_T1', c.project([self.points['P'], self.points['T1']])), ('net_edge_P_T0', c.project([self.points['P'], self.points['T0']])), ('net_edge_B2_Q', c.project([self.points['B2'], self.points['Q']])), ('net_edge_B3_Q', c.project([self.points['B3'], self.points['Q']]))]:
                c.line(points, id=object_id, clip_on=False, zorder=3)
            c.text('P', c.project(self.points['P']), offset_pt=[0, 16], vertex=True, id='P_label')
            c.text('Q', c.project(self.points['Q']), offset_pt=[0, -16], vertex=True, id='Q_label')
            c.text('R', c.project(self.points['B2']), offset_pt=[-15, -12], vertex=True, id='R_label')
            c.text('S', c.project(self.points['B3']), offset_pt=[13, 0], vertex=True, id='S_label')
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Solid73().draw(sys.argv[1] if len(sys.argv) > 1 else None))
