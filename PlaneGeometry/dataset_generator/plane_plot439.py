"""Frozen question Plane439; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane439:

    def __init__(self):
        self.id = 'Plane439'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:2080'
        self.question = 'In the array of $13$ squares shown below, $8$ squares are colored red, and the remaining $5$ squares are colored blue. If one of all possible such colorings is chosen at random, the probability that the chosen colored array appears the same when rotated $90^{\\circ}$ around the central square is $\\frac{1}{n}$, where $n$ is a positive integer. Find $n$.'
        self.answer = '429'
        self.answer_type = 'number'
        self.query = self.question
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane439.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-0.17452289054730263, 7.187543723880635], ylim=[-0.18754372388063478, 7.174522890547303]) as c:
            for object_id, vertices, codes in [('o0', [[3, 3], [4, 3], [4, 4], [3, 4], [3, 3]], [1, 2, 2, 2, 79]), ('o1', [[3, 6], [4, 6], [4, 7], [3, 7], [3, 6]], [1, 2, 2, 2, 79]), ('o2', [[2, 5], [3, 5], [3, 6], [2, 6], [2, 5]], [1, 2, 2, 2, 79]), ('o3', [[3, 5], [4, 5], [4, 6], [3, 6], [3, 5]], [1, 2, 2, 2, 79]), ('o4', [[5, 4], [6, 4], [6, 5], [5, 5], [5, 4]], [1, 2, 2, 2, 79]), ('o5', [[5, 3], [6, 3], [6, 4], [5, 4], [5, 3]], [1, 2, 2, 2, 79]), ('o6', [[6, 3], [7, 3], [7, 4], [6, 4], [6, 3]], [1, 2, 2, 2, 79]), ('o7', [[3, 1], [4, 1], [4, 2], [3, 2], [3, 1]], [1, 2, 2, 2, 79]), ('o8', [[4, 1], [5, 1], [5, 2], [4, 2], [4, 1]], [1, 2, 2, 2, 79]), ('o9', [[3, 0], [4, 0], [4, 1], [3, 1], [3, 0]], [1, 2, 2, 2, 79]), ('o10', [[0, 3], [1, 3], [1, 4], [0, 4], [0, 3]], [1, 2, 2, 2, 79]), ('o11', [[1, 3], [2, 3], [2, 4], [1, 4], [1, 3]], [1, 2, 2, 2, 79]), ('o12', [[1, 2], [2, 2], [2, 3], [1, 3], [1, 2]], [1, 2, 2, 2, 79])]:
                c.path(vertices, codes, id=object_id)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane439().draw(sys.argv[1] if len(sys.argv) > 1 else None))
