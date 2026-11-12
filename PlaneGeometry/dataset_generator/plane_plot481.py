"""Frozen question Plane481; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane481:

    def __init__(self):
        self.id = 'Plane481'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:2772'
        self.question = 'A shape resembling a multiplication symbol is shown below on a grid of 1-inch squares. What is its area in square inches?'
        self.answer = '10'
        self.answer_type = 'number'
        self.query = self.question
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane481.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-0.14870013968754936, 6.158689956879568], ylim=[-0.15868995687956833, 6.148700139687549], axes_position=[0.05, 0.05, 0.9, 0.9], coordinate_axes=False) as c:
            for object_id, points in [('v0', [[0.0, 0.0], [0.0, 6.0]]), ('v1', [[1.0, 0.0], [1.0, 6.0]]), ('v2', [[2.0, 0.0], [2.0, 6.0]]), ('v3', [[3.0, 0.0], [3.0, 6.0]]), ('v4', [[4.0, 0.0], [4.0, 6.0]]), ('v5', [[5.0, 0.0], [5.0, 6.0]]), ('v6', [[6.0, 0.0], [6.0, 6.0]]), ('h0', [[0.0, 0.0], [6.0, 0.0]]), ('h1', [[0.0, 1.0], [6.0, 1.0]]), ('h2', [[0.0, 2.0], [6.0, 2.0]]), ('h3', [[0.0, 3.0], [6.0, 3.0]]), ('h4', [[0.0, 4.0], [6.0, 4.0]]), ('h5', [[0.0, 5.0], [6.0, 5.0]]), ('h6', [[0.0, 6.0], [6.0, 6.0]])]:
                c.line(points, id=object_id, zorder=0.5)
            c.path([[1.0, 4.0], [2.0, 5.0], [3.0, 4.0], [4.0, 5.0], [5.0, 4.0], [4.0, 3.0], [5.0, 2.0], [4.0, 1.0], [3.0, 2.0], [2.0, 1.0], [1.0, 2.0], [2.0, 3.0], [1.0, 4.0]], [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 79], id='logo', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45], linewidth=0.0, capstyle='butt')
            c.path([[1.0, 4.0], [2.0, 5.0], [3.0, 4.0], [4.0, 5.0], [5.0, 4.0], [4.0, 3.0], [5.0, 2.0], [4.0, 1.0], [3.0, 2.0], [2.0, 1.0], [1.0, 2.0], [2.0, 3.0], [1.0, 4.0]], [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 79], id='logo', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.text('Math', [3.0, 3.3], id='math', rotation_mode='default', offset_pt=[0, 0], annotation_clip=None)
            c.text('Team', [3.0, 2.7], id='team', rotation_mode='default', offset_pt=[0, 0], annotation_clip=None)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane481().draw(sys.argv[1] if len(sys.argv) > 1 else None))
