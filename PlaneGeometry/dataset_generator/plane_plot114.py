"""Frozen question Plane114; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane114:

    def __init__(self):
        self.id = 'Plane114'
        self.source_dataset = 'Author Designed'
        self.source_key = 'intersection-counting:circle_crossing_square'
        self.question = 'How many intersection points can you find in the diagram?'
        self.answer = 8
        self.answer_type = 'number'
        self.query = self.question
        self.points = {'circle_center': [0.0, 0.0],
         'square_v0': [-1.5, -1.5],
         'square_v1': [1.5, -1.5],
         'square_v2': [1.5, 1.5],
         'square_v3': [-1.5, 1.5],
         'crossing_1': [-1.5, -0.9013878188659974],
         'crossing_2': [-1.5, 0.9013878188659974],
         'crossing_3': [-0.9013878188659974, -1.5],
         'crossing_4': [-0.9013878188659974, 1.5],
         'crossing_5': [0.9013878188659974, -1.5],
         'crossing_6': [0.9013878188659974, 1.5],
         'crossing_7': [1.5, -0.9013878188659974],
         'crossing_8': [1.5, 0.9013878188659974]}
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane114.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-1.8313953488372092, 1.8313953488372092], ylim=[-1.8313953488372092, 1.8313953488372092]) as c:
            c.circle(self.points['circle_center'], 1.75, id='circle')
            c.path([self.points['square_v0'], self.points['square_v1'], self.points['square_v2'], self.points['square_v3'], self.points['square_v0']], [1, 2, 2, 2, 79], id='square')
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane114().draw(sys.argv[1] if len(sys.argv) > 1 else None))
