"""Frozen question Plane256; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane256:

    def __init__(self):
        self.id = 'Plane256'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:751'
        self.question = 'Figure $\\mathrm{S}$ is made from four paper ribbons $10 \\mathrm{~cm}$ wide. Each of the ribbons is $25 \\mathrm{~cm}$ longer than the previous one (see the picture). By how many centimetres will the perimeter of figure $\\mathrm{T}$ (made from the same ribbons) exceed that of figure $\\mathrm{S}$?'
        self.answer = '50'
        self.answer_type = 'number'
        self.query = self.question
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane256.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-5.523646453186636, 110.74936107747502], ylim=[-13.58621215266357, 102.68679537799807]) as c:
            for object_id, vertices, codes in [('ribbon0_0', [[0, 0], [10, 0], [10, 25], [0, 25], [0, 0]], [1, 2, 2, 2, 79]), ('ribbon0_1', [[10, 0], [20, 0], [20, 50], [10, 50], [10, 0]], [1, 2, 2, 2, 79]), ('ribbon0_2', [[20, 0], [30, 0], [30, 75], [20, 75], [20, 0]], [1, 2, 2, 2, 79]), ('ribbon0_3', [[30, 0], [40, 0], [40, 100], [30, 100], [30, 0]], [1, 2, 2, 2, 79]), ('ribbon1_0', [[65, 0], [75, 0], [75, 75], [65, 75], [65, 0]], [1, 2, 2, 2, 79]), ('ribbon1_1', [[75, 0], [85, 0], [85, 50], [75, 50], [75, 0]], [1, 2, 2, 2, 79]), ('ribbon1_2', [[85, 0], [95, 0], [95, 100], [85, 100], [85, 0]], [1, 2, 2, 2, 79]), ('ribbon1_3', [[95, 0], [105, 0], [105, 25], [95, 25], [95, 0]], [1, 2, 2, 2, 79])]:
                c.path(vertices, codes, id=object_id)
            c.text('S', [20, -10], offset_pt=[0, 0], vertex=False, id='label0')
            c.text('T', [85, -10], offset_pt=[0, 0], vertex=False, id='label1')
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane256().draw(sys.argv[1] if len(sys.argv) > 1 else None))
