"""Frozen question Solid156; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Solid156:

    def __init__(self):
        self.id = 'Solid156'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:1225'
        self.question = 'The cube shown is built from equally sized bricks. The shortest side of one brick is $4 \\mathrm{~cm}$ long. What are the dimensions of one brick in $\\mathrm{cm}$?\nChoices:\nA:$4 \\times 6 \\times 12$\nB:$4 \\times 6 \\times 16$\nC:$4 \\times 8 \\times 12$\nD:$4 \\times 8 \\times 16$\nE:$4 \\times 12 \\times 16$'
        self.answer = 'C'
        self.answer_type = 'choice'
        self.choices = {'A': '$4 \\times 6 \\times 12$',
         'B': '$4 \\times 6 \\times 16$',
         'C': '$4 \\times 8 \\times 12$',
         'D': '$4 \\times 8 \\times 16$',
         'E': '$4 \\times 12 \\times 16$'}
        self.query = self.question
        self._geometry_01 = [('frontvertical0', [[0.0, 0.0], [0.0, 3.0]]),
         ('topdepth0', [[0.0, 3.0], [1.0499999999999998, 4.05]]),
         ('frontvertical1', [[1.0, 0.0], [1.0, 3.0]]),
         ('topdepth1', [[1.0, 3.0], [2.05, 4.05]]),
         ('frontvertical2', [[2.0, 0.0], [2.0, 3.0]]),
         ('topdepth2', [[2.0, 3.0], [3.05, 4.05]]),
         ('frontvertical3', [[3.0, 0.0], [3.0, 3.0]]),
         ('topdepth3', [[3.0, 3.0], [4.05, 4.05]]),
         ('fronthorizontal0', [[0.0, 0.0], [3.0, 0.0]]),
         ('rightdepth0', [[3.0, 0.0], [4.05, 1.0499999999999998]]),
         ('fronthorizontal1', [[0.0, 0.5], [3.0, 0.5]]),
         ('rightdepth1', [[3.0, 0.5], [4.05, 1.5499999999999998]]),
         ('fronthorizontal2', [[0.0, 1.0], [3.0, 1.0]]),
         ('rightdepth2', [[3.0, 1.0], [4.05, 2.05]]),
         ('fronthorizontal3', [[0.0, 1.5], [3.0, 1.5]]),
         ('rightdepth3', [[3.0, 1.5], [4.05, 2.55]]),
         ('fronthorizontal4', [[0.0, 2.0], [3.0, 2.0]]),
         ('rightdepth4', [[3.0, 2.0], [4.05, 3.05]]),
         ('fronthorizontal5', [[0.0, 2.5], [3.0, 2.5]]),
         ('rightdepth5', [[3.0, 2.5], [4.05, 3.55]]),
         ('fronthorizontal6', [[0.0, 3.0], [3.0, 3.0]]),
         ('rightdepth6', [[3.0, 3.0], [4.05, 4.05]]),
         ('topwidth0', [[0.0, 3.0], [3.0, 3.0]]),
         ('rightvertical0', [[3.0, 0.0], [3.0, 3.0]]),
         ('topwidth1', [[0.5249999999999999, 3.525], [3.525, 3.525]]),
         ('rightvertical1', [[3.525, 0.5249999999999999], [3.525, 3.525]]),
         ('topwidth2', [[1.0499999999999998, 4.05], [4.05, 4.05]]),
         ('rightvertical2', [[4.05, 1.0499999999999998], [4.05, 4.05]])]
        self.subject = 'SolidGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'SolidGeometry' / 'dataset_generator/scenes/Solid156.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('SolidGeometry', self.id, variant, output_path)
        with Canvas(SOLID, xlim=(-0.10086589209027919, 4.156997796160047), ylim=(-0.10699779616004745, 4.150865892090279), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
            for object_id, vertices, codes in [('front', [[0.0, 0.0], [3.0, 0.0], [3.0, 3.0], [0.0, 3.0], [0.0, 0.0]], [1, 2, 2, 2, 79]), ('right', [[3.0, 0.0], [4.05, 1.0499999999999998], [4.05, 4.05], [3.0, 3.0], [3.0, 0.0]], [1, 2, 2, 2, 79]), ('top', [[0.0, 3.0], [3.0, 3.0], [4.05, 4.05], [1.0499999999999998, 4.05], [0.0, 3.0]], [1, 2, 2, 2, 79])]:
                c.path(vertices, codes, id=object_id, alpha=1.0, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            for object_id, points in self._geometry_01:
                c.line(points, id=object_id, zorder=3, clip_on=False)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Solid156().draw(sys.argv[1] if len(sys.argv) > 1 else None))
