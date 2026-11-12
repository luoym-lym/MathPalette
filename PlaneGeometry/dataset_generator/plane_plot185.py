"""Frozen question Plane185; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane185:

    def __init__(self):
        self.id = 'Plane185'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:275'
        self.question = 'A square bit of paper is folded along the dashed lines in some order and direction. One of the corners of the resulting small square is cut off. The piece of paper is then unfolded. How many holes are on the inner area of the piece of paper?'
        self.answer = '1'
        self.answer_type = 'number'
        self.query = self.question
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane185.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=(-0.21592863991803046, 8.717115046065565), ylim=(-2.970092817979433, 5.962950868004164), axes_position=(0.050000000000000114, 0.05, 0.8999999999999998, 0.9), coordinate_axes=False) as c:
            c.path([[0.0, 0.0], [3.0, 0.0], [3.0, 3.0], [0.0, 3.0], [0.0, 0.0]], [1, 2, 2, 2, 79], id='o0', capstyle='butt')
            for object_id, points in [('o1', [[1.0, 0.0], [1.0, 3.0]]), ('o2', [[0.0, 1.0], [3.0, 1.0]]), ('o3', [[2.0, 0.0], [2.0, 3.0]]), ('o4', [[0.0, 2.0], [3.0, 2.0]])]:
                c.line(points, id=object_id, linestyle=(0.0, [4.0, 3.0]))
            c.line([[3.5, 1.5], [4.2, 1.5]], id='o5')
            c.path([[4.2, 1.5], [3.92, 1.65], [3.92, 1.35], [4.2, 1.5]], [1, 2, 2, 79], id='o6', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[4.2, 1.5], [3.92, 1.65], [3.92, 1.35], [4.2, 1.5]], [1, 2, 2, 79], id='o6', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.line([[6.2, 1.5], [6.9, 1.5]], id='o7')
            c.path([[6.9, 1.5], [6.62, 1.65], [6.62, 1.35], [6.9, 1.5]], [1, 2, 2, 79], id='o8', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[6.9, 1.5], [6.62, 1.65], [6.62, 1.35], [6.9, 1.5]], [1, 2, 2, 79], id='o8', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[4.7, 1.0], [5.7, 1.0], [5.7, 2.0], [4.7, 2.0], [4.7, 1.0]], [1, 2, 2, 2, 79], id='o9', capstyle='butt')
            c.path([[7.5, 1.0], [8.5, 1.0], [8.5, 1.7], [8.2, 2.0], [7.5, 2.0], [7.5, 1.0]], [1, 2, 2, 2, 2, 79], id='o10', capstyle='butt')
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane185().draw(sys.argv[1] if len(sys.argv) > 1 else None))
