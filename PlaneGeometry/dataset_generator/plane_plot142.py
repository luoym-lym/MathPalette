"""Frozen question Plane142; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane142:

    def __init__(self):
        self.id = 'Plane142'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:23'
        self.question = 'The heart-shaped chocolate is divided into squares as shown.\nWhat is its mass in grams if each square weighs 10 grams?'
        self.answer = '140'
        self.answer_type = 'number'
        self.query = self.question
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane142.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-0.6259048588000917, 4.6313587244387255], ylim=[-0.12979189053362905, 5.127471692705188]) as c:
            c.path([[0, 2], [0, 4], [1, 5], [2, 4], [3, 5], [4, 4], [4, 2], [2, 0], [0, 2]], [1, 2, 2, 2, 2, 2, 2, 2, 79], id='heart')
            for object_id, points in [('grid0', [[0, 4], [4, 4]]), ('grid1', [[0, 3], [4, 3]]), ('grid2', [[0, 2], [4, 2]]), ('grid3', [[1, 1], [3, 1]]), ('grid4', [[1, 1], [1, 5]]), ('grid5', [[2, 0], [2, 4]]), ('grid6', [[3, 1], [3, 5]])]:
                c.line(points, id=object_id)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane142().draw(sys.argv[1] if len(sys.argv) > 1 else None))
