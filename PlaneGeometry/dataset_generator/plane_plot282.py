"""Frozen question Plane282; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane282:

    def __init__(self):
        self.id = 'Plane282'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:847'
        self.question = 'The shape shown consists of 6 squares of side length 1. What is its perimeter?'
        self.answer = '12'
        self.answer_type = 'number'
        self.query = self.question
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane282.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-0.07335082829735917, 3.076893579858387], ylim=[-0.07754412393862564, 3.0727002842171207]) as c:
            for object_id, vertices, codes in [('square0', [[0, 0], [1, 0], [1, 1], [0, 1], [0, 0]], [1, 2, 2, 2, 79]), ('square1', [[1, 0], [2, 0], [2, 1], [1, 1], [1, 0]], [1, 2, 2, 2, 79]), ('square2', [[2, 0], [3, 0], [3, 1], [2, 1], [2, 0]], [1, 2, 2, 2, 79]), ('square3', [[0.75, 1], [1.75, 1], [1.75, 2], [0.75, 2], [0.75, 1]], [1, 2, 2, 2, 79]), ('square4', [[1.75, 1], [2.75, 1], [2.75, 2], [1.75, 2], [1.75, 1]], [1, 2, 2, 2, 79]), ('square5', [[1, 2], [2, 2], [2, 3], [1, 3], [1, 2]], [1, 2, 2, 2, 79])]:
                c.path(vertices, codes, id=object_id)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane282().draw(sys.argv[1] if len(sys.argv) > 1 else None))
