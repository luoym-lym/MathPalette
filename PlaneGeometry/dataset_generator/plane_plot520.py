"""Frozen question Plane520; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane520:

    def __init__(self):
        self.id = 'Plane520'
        self.source_dataset = 'Author Designed'
        self.source_key = 'author-expand24:Plane307/extension_03'
        self.question = 'What is the smallest number of additional whole squares that must be shaded to make the entire design, including the square grid, have 4 axes of reflection symmetry? The squares already shaded must remain shaded.'
        self.answer = '26'
        self.answer_type = 'number'
        self.query = self.question
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane520.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-0.1860465116279073, 8.186046511627907], ylim=[-0.1860465116279073, 8.186046511627907], axes_position=[0.05, 0.05, 0.9, 0.9], coordinate_axes=False) as c:
            for object_id, vertices, codes in [(None, [[0.0, 7.0], [1.0, 7.0], [1.0, 8.0], [0.0, 8.0], [0.0, 7.0]], [1, 2, 2, 2, 79]), (None, [[1.0, 7.0], [2.0, 7.0], [2.0, 8.0], [1.0, 8.0], [1.0, 7.0]], [1, 2, 2, 2, 79]), (None, [[6.0, 7.0], [7.0, 7.0], [7.0, 8.0], [6.0, 8.0], [6.0, 7.0]], [1, 2, 2, 2, 79]), (None, [[2.0, 6.0], [3.0, 6.0], [3.0, 7.0], [2.0, 7.0], [2.0, 6.0]], [1, 2, 2, 2, 79]), (None, [[3.0, 5.0], [4.0, 5.0], [4.0, 6.0], [3.0, 6.0], [3.0, 5.0]], [1, 2, 2, 2, 79]), (None, [[3.0, 4.0], [4.0, 4.0], [4.0, 5.0], [3.0, 5.0], [3.0, 4.0]], [1, 2, 2, 2, 79])]:
                c.path(vertices, codes, id=object_id, zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 1.0], capstyle='butt')
            for object_id, points in [('v0', [[0, 0], [0, 8]]), ('v1', [[1, 0], [1, 8]]), ('v2', [[2, 0], [2, 8]]), ('v3', [[3, 0], [3, 8]]), ('v4', [[4, 0], [4, 8]]), ('v5', [[5, 0], [5, 8]]), ('v6', [[6, 0], [6, 8]]), ('v7', [[7, 0], [7, 8]]), ('v8', [[8, 0], [8, 8]]), ('h0', [[0, 0], [8, 0]]), ('h1', [[0, 1], [8, 1]]), ('h2', [[0, 2], [8, 2]]), ('h3', [[0, 3], [8, 3]]), ('h4', [[0, 4], [8, 4]]), ('h5', [[0, 5], [8, 5]]), ('h6', [[0, 6], [8, 6]]), ('h7', [[0, 7], [8, 7]]), ('h8', [[0, 8], [8, 8]])]:
                c.line(points, id=object_id)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane520().draw(sys.argv[1] if len(sys.argv) > 1 else None))
