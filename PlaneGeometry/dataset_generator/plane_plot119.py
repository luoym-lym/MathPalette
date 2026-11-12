"""Frozen question Plane119; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane119:

    def __init__(self):
        self.id = 'Plane119'
        self.source_dataset = 'Author Designed'
        self.source_key = 'polygon-side-count:irregular_hexagon'
        self.question = 'How many sides does the closed polygonal outline have?'
        self.answer = 6
        self.answer_type = 'number'
        self.query = self.question
        self.points = {'V1': [1.86, 6.58], 'V2': [5.81, 7.13], 'V3': [7.12, 3.84], 'V4': [6.03, 1.1], 'V5': [2.74, 0.56], 'V6': [0.55, 1.65]}
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane119.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[0.395, 7.275], ylim=[0.405, 7.285]) as c:
            for object_id, points in [('edge_01', [self.points['V1'], self.points['V2']]), ('edge_02', [self.points['V2'], self.points['V3']]), ('edge_03', [self.points['V3'], self.points['V4']]), ('edge_04', [self.points['V4'], self.points['V5']]), ('edge_05', [self.points['V5'], self.points['V6']]), ('edge_06', [self.points['V6'], self.points['V1']])]:
                c.line(points, id=object_id)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane119().draw(sys.argv[1] if len(sys.argv) > 1 else None))
