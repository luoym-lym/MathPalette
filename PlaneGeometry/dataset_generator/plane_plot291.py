"""Frozen question Plane291; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane291:

    def __init__(self):
        self.id = 'Plane291'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:872'
        self.question = 'A rectangle is twice as long as wide. Which fraction of the rectangle is coloured in grey?\nChoices:\nA:$\\frac{1}{4}$\nB:$\\frac{3}{8}$\nC:$\\frac{3}{4}$\nD:$\\frac{1}{2}$\nE:$\\frac{3}{5}$'
        self.answer = 'B'
        self.answer_type = 'choice'
        self.choices = {'A': '$\\frac{1}{4}$', 'B': '$\\frac{3}{8}$', 'C': '$\\frac{3}{4}$', 'D': '$\\frac{1}{2}$', 'E': '$\\frac{3}{5}$'}
        self.query = self.question
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane291.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-0.04969907522388639, 2.052425638243225], ylim=[-0.5530519310947388, 1.5490727823723727], axes_position=[0.050000000000000114, 0.05, 0.8999999999999998, 0.9], coordinate_axes=False) as c:
            c.path([[0.0, 0.0], [2.0, 0.0], [2.0, 1.0], [0.0, 1.0], [0.0, 0.0]], [1, 2, 2, 2, 79], id='rectangle', facecolor=[0.0, 0.0, 0.0, 0.0], capstyle='butt')
            c.path([[0.0, 0.0], [0.0, 1.0], [1.0, 0.5], [0.0, 0.0]], [1, 2, 2, 79], id='gray0', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45], linewidth=0.0, capstyle='butt')
            c.path([[0.0, 0.0], [0.0, 1.0], [1.0, 0.5], [0.0, 0.0]], [1, 2, 2, 79], id='gray0', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[1.0, 0.0], [2.0, 0.0], [1.0, 0.5], [1.0, 0.0]], [1, 2, 2, 79], id='gray1', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45], linewidth=0.0, capstyle='butt')
            c.path([[1.0, 0.0], [2.0, 0.0], [1.0, 0.5], [1.0, 0.0]], [1, 2, 2, 79], id='gray1', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            for object_id, points in [('diag1', [[0.0, 0.0], [2.0, 1.0]]), ('diag2', [[0.0, 1.0], [2.0, 0.0]]), ('half_divider', [[1.0, 0.0], [1.0, 0.5]])]:
                c.line(points, id=object_id)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane291().draw(sys.argv[1] if len(sys.argv) > 1 else None))
