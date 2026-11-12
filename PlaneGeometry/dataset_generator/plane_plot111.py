"""Frozen question Plane111; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane111:

    def __init__(self):
        self.id = 'Plane111'
        self.source_dataset = 'Author Designed'
        self.source_key = 'intersection-counting:circle_nonparallel_lines'
        self.question = 'How many intersection points are shown?'
        self.answer = 5
        self.answer_type = 'number'
        self.query = self.question
        self.points = {'circle_center': [0, 0],
         'line_a_a': [-2.7, -0.32500000000000007],
         'line_a_b': [2.7, 1.025],
         'line_b_a': [-2.7, 1.7899999999999998],
         'line_b_b': [2.7, -1.99],
         'crossing_1': [-1.7478381048599623, -0.08695952621499062],
         'crossing_2': [-1.4790639505617877, 0.9353447653932512],
         'crossing_3': [-0.47368421052631593, 0.231578947368421],
         'crossing_4': [1.3851042190181628, -1.0695729533127138],
         'crossing_5': [1.5831322225070208, 0.7457830556267552]}
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane111.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-2.8255813953488373, 2.8255813953488373], ylim=[-2.9255813953488374, 2.7255813953488373]) as c:
            c.circle(self.points['circle_center'], 1.75, id='circle')
            c.line([self.points['line_a_a'], self.points['line_a_b']], id='line_a')
            c.line([self.points['line_b_a'], self.points['line_b_b']], id='line_b')
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane111().draw(sys.argv[1] if len(sys.argv) > 1 else None))
