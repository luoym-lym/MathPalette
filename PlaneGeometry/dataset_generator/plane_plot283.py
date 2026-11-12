"""Frozen question Plane283; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane283:

    def __init__(self):
        self.id = 'Plane283'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:848'
        self.question = 'A rectangle is formed from 4 equally sized smaller rectangles. The shorter side is $10 \\mathrm{~cm}$ long. How long is the longer side?\nChoices:\nA:$40 \\mathrm{~cm}$\nB:$30 \\mathrm{~cm}$\nC:$20 \\mathrm{~cm}$\nD:$10 \\mathrm{~cm}$\nE:$5 \\mathrm{~cm}$'
        self.answer = 'C'
        self.answer_type = 'choice'
        self.choices = {'A': '$40 \\mathrm{~cm}$', 'B': '$30 \\mathrm{~cm}$', 'C': '$20 \\mathrm{~cm}$', 'D': '$10 \\mathrm{~cm}$', 'E': '$5 \\mathrm{~cm}$'}
        self.query = self.question
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane283.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-0.6161605844763596, 25.86097982146562], ylim=[-8.255977576732834, 18.22116282920915], axes_position=[0.05, 0.05, 0.9, 0.9], coordinate_axes=False) as c:
            for object_id, vertices, codes in [('rectangle0', [[0.0, 0.0], [5.0, 0.0], [5.0, 10.0], [0.0, 10.0], [0.0, 0.0]], [1, 2, 2, 2, 79]), ('rectangle1', [[5.0, 0.0], [15.0, 0.0], [15.0, 5.0], [5.0, 5.0], [5.0, 0.0]], [1, 2, 2, 2, 79]), ('rectangle2', [[5.0, 5.0], [15.0, 5.0], [15.0, 10.0], [5.0, 10.0], [5.0, 5.0]], [1, 2, 2, 2, 79]), ('rectangle3', [[15.0, 0.0], [20.0, 0.0], [20.0, 10.0], [15.0, 10.0], [15.0, 0.0]], [1, 2, 2, 2, 79])]:
                c.path(vertices, codes, id=object_id, facecolor=[0.0, 0.0, 0.0, 0.0], capstyle='butt')
            c.line([[20.0, 0.0], [21.0, 0.0]], id='dimc1')
            c.line([[20.0, 10.0], [21.0, 10.0]], id='dimc2')
            c.line([[21.0, 0.0], [21.0, 10.0]], id='dimdash', linestyle=(0.0, [4.0, 3.0]))
            c.text('10 cm', [24.0, 5.0], id='label0', rotation_mode='default', offset_pt=[0, 0], annotation_clip=None)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane283().draw(sys.argv[1] if len(sys.argv) > 1 else None))
