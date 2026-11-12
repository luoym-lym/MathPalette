"""Frozen question Plane212; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane212:

    def __init__(self):
        self.id = 'Plane212'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:540'
        self.question = 'The shape in figure 1 is cut into equally sized small triangles like those in figure 2. One such triangle is already drawn in figure 1. How many of these triangles result?'
        self.answer = '15'
        self.answer_type = 'number'
        self.query = self.question
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane212.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-0.5440288163105693, 10.55290383222978], ylim=[-3.830374303194927, 7.266558345345422], axes_position=[0.05, 0.05, 0.9, 0.9], coordinate_axes=False) as c:
            c.path([[2.0, 0.0], [2.0, 2.0], [3.0, 1.0], [2.0, 0.0]], [1, 2, 2, 79], id='example_triangle', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45], linewidth=0.0, capstyle='butt')
            c.path([[2.0, 0.0], [2.0, 2.0], [3.0, 1.0], [2.0, 0.0]], [1, 2, 2, 79], id='example_triangle', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            for object_id, points in [('gridv0', [[0.0, -0.3], [0.0, 4.3]]), ('gridv1', [[1.0, -0.3], [1.0, 4.3]]), ('gridv2', [[2.0, -0.3], [2.0, 4.3]]), ('gridv3', [[3.0, -0.3], [3.0, 4.3]]), ('gridv4', [[4.0, -0.3], [4.0, 4.3]]), ('gridv5', [[5.0, -0.3], [5.0, 4.3]]), ('gridv6', [[6.0, -0.3], [6.0, 4.3]]), ('gridv7', [[7.0, -0.3], [7.0, 4.3]]), ('gridh0', [[-0.3, 0.0], [7.3, 0.0]]), ('gridh1', [[-0.3, 1.0], [7.3, 1.0]]), ('gridh2', [[-0.3, 2.0], [7.3, 2.0]]), ('gridh3', [[-0.3, 3.0], [7.3, 3.0]]), ('gridh4', [[-0.3, 4.0], [7.3, 4.0]])]:
                c.line(points, id=object_id, linestyle=(0.0, [4.0, 3.0]))
            c.path([[0.0, 2.0], [2.0, 4.0], [4.0, 4.0], [4.0, 3.0], [6.0, 3.0], [7.0, 2.0], [6.0, 1.0], [4.0, 1.0], [4.0, 0.0], [2.0, 0.0], [2.0, 2.0], [0.0, 2.0]], [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 79], id='figure1', facecolor=[0.0, 0.0, 0.0, 0.0], capstyle='butt')
            c.path([[8.0, 2.0], [10.0, 2.0], [9.0, 3.0], [8.0, 2.0]], [1, 2, 2, 79], id='figure2', facecolor=[0.0, 0.0, 0.0, 0.0], capstyle='butt')
            for object_id, points in [('grid2v8', [[8.0, 1.7], [8.0, 3.3]]), ('grid2v9', [[9.0, 1.7], [9.0, 3.3]]), ('grid2v10', [[10.0, 1.7], [10.0, 3.3]]), ('grid2h2', [[7.7, 2.0], [10.3, 2.0]]), ('grid2h3', [[7.7, 3.0], [10.3, 3.0]])]:
                c.line(points, id=object_id, linestyle=(0.0, [4.0, 3.0]))
            c.text('Figure 1', [3.5, -0.7], id='label0', rotation_mode='default', offset_pt=[0, 0], annotation_clip=None)
            c.text('Figure 2', [9.0, 1.4], id='label1', rotation_mode='default', offset_pt=[0, 0], annotation_clip=None)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane212().draw(sys.argv[1] if len(sys.argv) > 1 else None))
