"""Frozen question Plane109; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane109:

    def __init__(self):
        self.id = 'Plane109'
        self.source_dataset = 'Author Designed'
        self.source_key = 'intersection-counting:equal_circles_small_center'
        self.question = 'How many intersection points are there in the diagram?'
        self.answer = 6
        self.answer_type = 'number'
        self.query = self.question
        self.points = {'top_center': [0, 1.3279056191361391],
         'left_center': [-1.15, -0.6639528095680696],
         'right_center': [1.15, -0.6639528095680696],
         'crossing_1': [-1.5996950765959597, 0.9235843830939964],
         'crossing_2': [-0.44969507659595975, -0.2596315735259268],
         'crossing_3': [0.0, -1.8471687661879928],
         'crossing_4': [0.0, 0.5192631470518536],
         'crossing_5': [0.44969507659595975, -0.2596315735259268],
         'crossing_6': [1.5996950765959597, 0.9235843830939964]}
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane109.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-2.9302325581395348, 2.9302325581395348], ylim=[-2.5982561533555, 3.2622089629235695]) as c:
            for object_id, center, radius in [('top', self.points['top_center'], 1.65), ('left', self.points['left_center'], 1.65), ('right', self.points['right_center'], 1.65)]:
                c.circle(center, radius, id=object_id)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane109().draw(sys.argv[1] if len(sys.argv) > 1 else None))
