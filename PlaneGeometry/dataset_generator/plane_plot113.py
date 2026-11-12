"""Frozen question Plane113; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane113:

    def __init__(self):
        self.id = 'Plane113'
        self.source_dataset = 'Author Designed'
        self.source_key = 'intersection-counting:overlapping_rectangles'
        self.question = 'Count the intersection points in the figure.'
        self.answer = 6
        self.answer_type = 'number'
        self.query = self.question
        self.points = {'rectangle_a_v0': [-2.4000000000000004, -1.15],
         'rectangle_a_v1': [2.0, -1.15],
         'rectangle_a_v2': [2.0, 1.25],
         'rectangle_a_v3': [-2.4000000000000004, 1.25],
         'rectangle_b_v0': [0.06359541457745188, -2.083568733392411],
         'rectangle_b_v1': [2.4381300838154445, -0.5997947935394372],
         'rectangle_b_v2': [0.6364045854225482, 2.2835687333924106],
         'rectangle_b_v3': [-1.7381300838154448, 0.7997947935394372],
         'crossing_1': [-1.0176511467625504, 1.25],
         'crossing_2': [-0.5197630748202755, -1.15],
         'crossing_3': [1.2822500100112082, 1.25],
         'crossing_4': [1.5576176938584463, -1.15],
         'crossing_5': [2.0, -0.8735688550651733],
         'crossing_6': [2.0, 0.10135990780206794]}
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane113.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-2.512514653111988, 2.550644736927432], ylim=[-2.4315796950197104, 2.6315796950197097]) as c:
            c.path([self.points['rectangle_a_v0'], self.points['rectangle_a_v1'], self.points['rectangle_a_v2'], self.points['rectangle_a_v3'], self.points['rectangle_a_v0']], [1, 2, 2, 2, 79], id='rectangle_a')
            c.path([self.points['rectangle_b_v0'], self.points['rectangle_b_v1'], self.points['rectangle_b_v2'], self.points['rectangle_b_v3'], self.points['rectangle_b_v0']], [1, 2, 2, 2, 79], id='rectangle_b')
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane113().draw(sys.argv[1] if len(sys.argv) > 1 else None))
