"""Frozen question Plane483; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane483:

    def __init__(self):
        self.id = 'Plane483'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:2808'
        self.question = 'If each of the $16$ small squares in the grid is a unit square, what is the area of the shaded region?'
        self.answer = '6'
        self.answer_type = 'number'
        self.query = self.question
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane483.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-0.09913342645836565, 4.105793304586378], ylim=[-0.10579330458637859, 4.099133426458365], axes_position=[0.05, 0.05, 0.9, 0.9], coordinate_axes=False) as c:
            for object_id, points in [('v0', [[0.0, 0.0], [0.0, 4.0]]), ('v1', [[1.0, 0.0], [1.0, 4.0]]), ('v2', [[2.0, 0.0], [2.0, 4.0]]), ('v3', [[3.0, 0.0], [3.0, 4.0]]), ('v4', [[4.0, 0.0], [4.0, 4.0]]), ('h0', [[0.0, 0.0], [4.0, 0.0]]), ('h1', [[0.0, 1.0], [4.0, 1.0]]), ('h2', [[0.0, 2.0], [4.0, 2.0]]), ('h3', [[0.0, 3.0], [4.0, 3.0]]), ('h4', [[0.0, 4.0], [4.0, 4.0]])]:
                c.line(points, id=object_id)
            c.path([[0.0, 0.0], [2.0, 2.0], [1.0, 2.0], [2.0, 4.0], [2.0, 3.0], [4.0, 4.0], [3.0, 2.0], [4.0, 0.0], [2.0, 1.0], [0.0, 0.0]], [1, 2, 2, 2, 2, 2, 2, 2, 2, 79], id='gray', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45], linewidth=0.0, capstyle='butt')
            c.path([[0.0, 0.0], [2.0, 2.0], [1.0, 2.0], [2.0, 4.0], [2.0, 3.0], [4.0, 4.0], [3.0, 2.0], [4.0, 0.0], [2.0, 1.0], [0.0, 0.0]], [1, 2, 2, 2, 2, 2, 2, 2, 2, 79], id='gray', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane483().draw(sys.argv[1] if len(sys.argv) > 1 else None))
