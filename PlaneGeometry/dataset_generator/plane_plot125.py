"""Frozen question Plane125; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane125:

    def __init__(self):
        self.id = 'Plane125'
        self.source_dataset = 'Author Designed'
        self.source_key = 'unit-grid-area:arrow_double_notch'
        self.question = 'The grid consists of congruent squares, each with an area of 1 square unit. Find the area of the shaded region.'
        self.answer = '14'
        self.answer_type = 'number'
        self.query = self.question
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane125.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=(-0.13953488372093048, 6.1395348837209305), ylim=(-1.1395348837209305, 5.1395348837209305), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
            c.path([[0.0, 2.0], [2.0, 0.0], [3.0, 1.0], [4.0, 0.0], [6.0, 2.0], [4.0, 4.0], [3.0, 3.0], [2.0, 4.0], [0.0, 2.0]], [1, 2, 2, 2, 2, 2, 2, 2, 79], alpha=0.45, zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), capstyle='butt')
            c.path([[0.0, 2.0], [2.0, 0.0], [3.0, 1.0], [4.0, 0.0], [6.0, 2.0], [4.0, 4.0], [3.0, 3.0], [2.0, 4.0], [0.0, 2.0]], [1, 2, 2, 2, 2, 2, 2, 2, 79], id='shade', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            for object_id, points in [('grid_v0', [[0.0, 0.0], [0.0, 4.0]]), ('grid_v1', [[1.0, 0.0], [1.0, 4.0]]), ('grid_v2', [[2.0, 0.0], [2.0, 4.0]]), ('grid_v3', [[3.0, 0.0], [3.0, 4.0]]), ('grid_v4', [[4.0, 0.0], [4.0, 4.0]]), ('grid_v5', [[5.0, 0.0], [5.0, 4.0]]), ('grid_v6', [[6.0, 0.0], [6.0, 4.0]]), ('grid_h0', [[0.0, 0.0], [6.0, 0.0]]), ('grid_h1', [[0.0, 1.0], [6.0, 1.0]]), ('grid_h2', [[0.0, 2.0], [6.0, 2.0]]), ('grid_h3', [[0.0, 3.0], [6.0, 3.0]]), ('grid_h4', [[0.0, 4.0], [6.0, 4.0]])]:
                c.line(points, id=object_id)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane125().draw(sys.argv[1] if len(sys.argv) > 1 else None))
