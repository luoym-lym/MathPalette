"""Frozen question Plane472; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane472:

    def __init__(self):
        self.id = 'Plane472'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:2684'
        self.question = 'What is the area of the shaded pinwheel shown in the $5\\times 5$ grid?\n\nChoices:\nA:$4$\nB:$6$\nC:$8$\nD:$10$\nE:$12$'
        self.answer = 'B'
        self.answer_type = 'choice'
        self.choices = {'A': '$4$', 'B': '$6$', 'C': '$8$', 'D': '$10$', 'E': '$12$'}
        self.query = self.question
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane472.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-0.12391678307295706, 5.132241630732973], ylim=[-0.13224163073297301, 5.123916783072957], axes_position=[0.05, 0.05, 0.9, 0.9], coordinate_axes=False) as c:
            for object_id, points in [('v0', [[0.0, 0.0], [0.0, 5.0]]), ('v1', [[1.0, 0.0], [1.0, 5.0]]), ('v2', [[2.0, 0.0], [2.0, 5.0]]), ('v3', [[3.0, 0.0], [3.0, 5.0]]), ('v4', [[4.0, 0.0], [4.0, 5.0]]), ('v5', [[5.0, 0.0], [5.0, 5.0]]), ('h0', [[0.0, 0.0], [5.0, 0.0]]), ('h1', [[0.0, 1.0], [5.0, 1.0]]), ('h2', [[0.0, 2.0], [5.0, 2.0]]), ('h3', [[0.0, 3.0], [5.0, 3.0]]), ('h4', [[0.0, 4.0], [5.0, 4.0]]), ('h5', [[0.0, 5.0], [5.0, 5.0]])]:
                c.line(points, id=object_id)
            c.path([[2.5, 2.5], [1.0, 5.0], [1.0, 4.0], [0.0, 4.0], [2.5, 2.5]], [1, 2, 2, 2, 79], id='blade0', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45], linewidth=0.0, capstyle='butt')
            c.path([[2.5, 2.5], [1.0, 5.0], [1.0, 4.0], [0.0, 4.0], [2.5, 2.5]], [1, 2, 2, 2, 79], id='blade0', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[2.5, 2.5], [0.0, 1.0], [1.0, 1.0], [1.0, 0.0], [2.5, 2.5]], [1, 2, 2, 2, 79], id='blade1', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45], linewidth=0.0, capstyle='butt')
            c.path([[2.5, 2.5], [0.0, 1.0], [1.0, 1.0], [1.0, 0.0], [2.5, 2.5]], [1, 2, 2, 2, 79], id='blade1', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[2.5, 2.5], [4.0, 0.0], [4.0, 1.0], [5.0, 1.0], [2.5, 2.5]], [1, 2, 2, 2, 79], id='blade2', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45], linewidth=0.0, capstyle='butt')
            c.path([[2.5, 2.5], [4.0, 0.0], [4.0, 1.0], [5.0, 1.0], [2.5, 2.5]], [1, 2, 2, 2, 79], id='blade2', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[2.5, 2.5], [5.0, 4.0], [4.0, 4.0], [4.0, 5.0], [2.5, 2.5]], [1, 2, 2, 2, 79], id='blade3', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45], linewidth=0.0, capstyle='butt')
            c.path([[2.5, 2.5], [5.0, 4.0], [4.0, 4.0], [4.0, 5.0], [2.5, 2.5]], [1, 2, 2, 2, 79], id='blade3', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane472().draw(sys.argv[1] if len(sys.argv) > 1 else None))
