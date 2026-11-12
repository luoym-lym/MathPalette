"""Frozen question Plane120; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane120:

    def __init__(self):
        self.id = 'Plane120'
        self.source_dataset = 'Author Designed'
        self.source_key = 'structure-count:open-path-turns'
        self.question = 'How many times does the direction change along the polygonal path from P to Q?'
        self.answer = 5
        self.answer_type = 'number'
        self.query = self.question
        self.points = {'P': [-4.0, -2.0], 'T1': [-2.8, -0.3], 'T2': [-0.8, -0.3], 'T3': [0.2, 1.6], 'T4': [2.1, 1.6], 'T5': [2.1, -0.9], 'Q': [4.0, -0.9]}
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane120.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-4.6457628047975135, 4.61567021220492], ylim=[-5.00564200460506, 4.255791012397373]) as c:
            for object_id, points in [('edge_00', [self.points['P'], self.points['T1']]), ('edge_01', [self.points['T1'], self.points['T2']]), ('edge_02', [self.points['T2'], self.points['T3']]), ('edge_03', [self.points['T3'], self.points['T4']]), ('edge_04', [self.points['T4'], self.points['T5']]), ('edge_05', [self.points['T5'], self.points['Q']])]:
                c.line(points, id=object_id)
            c.text('P', self.points['P'], offset_pt=[-18.0, -16.0], vertex=True, id='label_P')
            c.text('Q', self.points['Q'], offset_pt=[15.0, 13.0], vertex=True, id='label_Q')
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane120().draw(sys.argv[1] if len(sys.argv) > 1 else None))
