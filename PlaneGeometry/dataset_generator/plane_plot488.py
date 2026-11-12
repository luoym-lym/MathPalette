"""Frozen question Plane488; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane488:

    def __init__(self):
        self.id = 'Plane488'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:2876'
        self.question = 'A rectangular piece of paper with side lengths 5 by 8 is folded along the dashed lines shown below, so that the folded flaps just touch at the corners as shown by the dotted lines. Find the area of the resulting trapezoid.'
        self.answer = '55/2'
        self.answer_type = 'number'
        self.query = self.question
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane488.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-0.6639796993638072, 8.22676804562696], ylim=[-2.176781123450917, 6.71396662153985], axes_position=[0.05, 0.05, 0.9, 0.9], coordinate_axes=False) as c:
            c.path([[0.0, 0.0], [8.0, 0.0], [8.0, 5.0], [0.0, 5.0], [0.0, 0.0]], [1, 2, 2, 2, 79], id='o0', facecolor=[0.0, 0.0, 0.0, 0.0], capstyle='butt')
            c.line([[0.0, 0.0], [2.5, 5.0]], id='o1', linestyle=(0.0, [4.0, 3.0]))
            c.line([[8.0, 0.0], [5.5, 5.0]], id='o2', linestyle=(0.0, [4.0, 3.0]))
            for object_id, points in [('o3', [[0.0, 0.0], [4.0, 3.0]]), ('o4', [[2.5, 5.0], [4.0, 3.0]]), ('o5', [[8.0, 0.0], [4.0, 3.0]]), ('o6', [[5.5, 5.0], [4.0, 3.0]])]:
                c.line(points, id=object_id, linestyle=(0.0, [1.0, 1.65]))
            c.text('5', [-0.4, 2.5], id='t0', rotation_mode='default', offset_pt=[0, 0], annotation_clip=None)
            c.text('8', [4.0, -0.4], id='t1', rotation_mode='default', offset_pt=[0, 0], annotation_clip=None)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane488().draw(sys.argv[1] if len(sys.argv) > 1 else None))
