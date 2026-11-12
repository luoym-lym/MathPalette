"""Frozen question Plane518; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane518:

    def __init__(self):
        self.id = 'Plane518'
        self.source_dataset = 'Author Designed'
        self.source_key = 'author-expand24:Plane307/extension_01'
        self.question = 'What is the smallest number of additional whole squares that must be shaded to make the entire design, including the square grid, have 4 axes of reflection symmetry? The squares already shaded must remain shaded.'
        self.answer = '13'
        self.answer_type = 'number'
        self.query = self.question
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane518.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-0.11627906976744207, 5.116279069767442], ylim=[-0.11627906976744207, 5.116279069767442], axes_position=[0.05, 0.05, 0.9, 0.9], coordinate_axes=False) as c:
            for object_id, vertices, codes in [(None, [[0.0, 4.0], [1.0, 4.0], [1.0, 5.0], [0.0, 5.0], [0.0, 4.0]], [1, 2, 2, 2, 79]), (None, [[1.0, 4.0], [2.0, 4.0], [2.0, 5.0], [1.0, 5.0], [1.0, 4.0]], [1, 2, 2, 2, 79]), (None, [[2.0, 3.0], [3.0, 3.0], [3.0, 4.0], [2.0, 4.0], [2.0, 3.0]], [1, 2, 2, 2, 79])]:
                c.path(vertices, codes, id=object_id, zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 1.0], capstyle='butt')
            for object_id, points in [('v0', [[0, 0], [0, 5]]), ('v1', [[1, 0], [1, 5]]), ('v2', [[2, 0], [2, 5]]), ('v3', [[3, 0], [3, 5]]), ('v4', [[4, 0], [4, 5]]), ('v5', [[5, 0], [5, 5]]), ('h0', [[0, 0], [5, 0]]), ('h1', [[0, 1], [5, 1]]), ('h2', [[0, 2], [5, 2]]), ('h3', [[0, 3], [5, 3]]), ('h4', [[0, 4], [5, 4]]), ('h5', [[0, 5], [5, 5]])]:
                c.line(points, id=object_id)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane518().draw(sys.argv[1] if len(sys.argv) > 1 else None))
