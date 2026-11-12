"""Frozen question Solid86; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Solid86:

    def __init__(self):
        self.id = 'Solid86'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:104'
        self.question = 'A block is made from equal numbers of white cubes and colored cubes. How many white cubes are not visible in the picture?'
        self.answer = '2'
        self.answer_type = 'number'
        self.query = self.question
        self._geometry_01 = [('blocke0', [[0.0, 0.0], [1.0, 0.0]]),
         ('blocke1', [[0.0, 1.0], [1.0, 1.0]]),
         ('blocke2', [[0.0, 0.0], [0.0, 1.0]]),
         ('blocke3', [[1.0, 0.0], [1.0, 1.0]]),
         ('blocke4', [[0.0, 2.0], [1.0, 2.0]]),
         ('blocke5', [[0.0, 1.0], [0.0, 2.0]]),
         ('blocke6', [[1.0, 1.0], [1.0, 2.0]]),
         ('blocke7', [[0.0, 3.0], [1.0, 3.0]]),
         ('blocke8', [[0.35, 3.35], [1.35, 3.35]]),
         ('blocke9', [[0.0, 3.0], [0.35, 3.35]]),
         ('blocke10', [[1.0, 3.0], [1.35, 3.35]]),
         ('blocke11', [[0.0, 2.0], [0.0, 3.0]]),
         ('blocke12', [[1.0, 2.0], [1.0, 3.0]]),
         ('blocke13', [[0.7, 3.7], [1.7, 3.7]]),
         ('blocke14', [[0.35, 3.35], [0.7, 3.7]]),
         ('blocke15', [[1.35, 3.35], [1.7, 3.7]]),
         ('blocke16', [[1.0, 0.0], [2.0, 0.0]]),
         ('blocke17', [[1.0, 1.0], [2.0, 1.0]]),
         ('blocke18', [[2.0, 0.0], [2.0, 1.0]]),
         ('blocke19', [[1.0, 2.0], [2.0, 2.0]]),
         ('blocke20', [[2.0, 1.0], [2.0, 2.0]]),
         ('blocke21', [[1.0, 3.0], [2.0, 3.0]]),
         ('blocke22', [[1.35, 3.35], [2.35, 3.35]]),
         ('blocke23', [[2.0, 3.0], [2.35, 3.35]]),
         ('blocke24', [[2.0, 2.0], [2.0, 3.0]]),
         ('blocke25', [[1.7, 3.7], [2.7, 3.7]]),
         ('blocke26', [[2.35, 3.35], [2.7, 3.7]]),
         ('blocke27', [[2.0, 0.0], [3.0, 0.0]]),
         ('blocke28', [[2.0, 1.0], [3.0, 1.0]]),
         ('blocke29', [[3.0, 0.0], [3.0, 1.0]]),
         ('blocke30', [[2.0, 2.0], [3.0, 2.0]]),
         ('blocke31', [[3.0, 1.0], [3.0, 2.0]]),
         ('blocke32', [[2.0, 3.0], [3.0, 3.0]]),
         ('blocke33', [[2.35, 3.35], [3.35, 3.35]]),
         ('blocke34', [[3.0, 3.0], [3.35, 3.35]]),
         ('blocke35', [[3.0, 2.0], [3.0, 3.0]]),
         ('blocke36', [[2.7, 3.7], [3.7, 3.7]]),
         ('blocke37', [[3.35, 3.35], [3.7, 3.7]]),
         ('blocke38', [[3.0, 0.0], [4.0, 0.0]]),
         ('blocke39', [[3.0, 1.0], [4.0, 1.0]]),
         ('blocke40', [[4.0, 0.0], [4.35, 0.35]]),
         ('blocke41', [[4.0, 1.0], [4.35, 1.35]]),
         ('blocke42', [[4.0, 0.0], [4.0, 1.0]]),
         ('blocke43', [[4.35, 0.35], [4.35, 1.35]]),
         ('blocke44', [[3.0, 2.0], [4.0, 2.0]]),
         ('blocke45', [[4.0, 2.0], [4.35, 2.35]]),
         ('blocke46', [[4.0, 1.0], [4.0, 2.0]]),
         ('blocke47', [[4.35, 1.35], [4.35, 2.35]]),
         ('blocke48', [[3.0, 3.0], [4.0, 3.0]]),
         ('blocke49', [[3.35, 3.35], [4.35, 3.35]]),
         ('blocke50', [[4.0, 3.0], [4.35, 3.35]]),
         ('blocke51', [[4.0, 2.0], [4.0, 3.0]]),
         ('blocke52', [[4.35, 2.35], [4.35, 3.35]]),
         ('blocke53', [[4.35, 0.35], [4.7, 0.7]]),
         ('blocke54', [[4.35, 1.35], [4.7, 1.7]]),
         ('blocke55', [[4.7, 0.7], [4.7, 1.7]]),
         ('blocke56', [[4.35, 2.35], [4.7, 2.7]]),
         ('blocke57', [[4.7, 1.7], [4.7, 2.7]]),
         ('blocke58', [[3.7, 3.7], [4.7, 3.7]]),
         ('blocke59', [[4.35, 3.35], [4.7, 3.7]]),
         ('blocke60', [[4.7, 2.7], [4.7, 3.7]])]
        self.subject = 'SolidGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'SolidGeometry' / 'dataset_generator/scenes/Solid86.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('SolidGeometry', self.id, variant, output_path)
        with Canvas(SOLID, xlim=[-0.1206427515754811, 4.820615600998944], ylim=[-0.6206156009989447, 4.32064275157548], axes_position=[0.05, 0.05, 0.9, 0.9], coordinate_axes=False) as c:
            for object_id, points in self._geometry_01:
                c.line(points, id=object_id, zorder=3, clip_on=False)
            for object_id, vertices, codes in [('gray000_0', [[0.0, 0.0], [1.0, 0.0], [1.0, 1.0], [0.0, 1.0], [0.0, 0.0]], [1, 2, 2, 2, 79]), ('gray001_0', [[0.0, 1.0], [1.0, 1.0], [1.0, 2.0], [0.0, 2.0], [0.0, 1.0]], [1, 2, 2, 2, 79]), ('gray002_0', [[0.0, 2.0], [1.0, 2.0], [1.0, 3.0], [0.0, 3.0], [0.0, 2.0]], [1, 2, 2, 2, 79]), ('gray002_1', [[0.0, 3.0], [1.0, 3.0], [1.35, 3.35], [0.35, 3.35], [0.0, 3.0]], [1, 2, 2, 2, 79]), ('gray012_0', [[0.35, 3.35], [1.35, 3.35], [1.7, 3.7], [0.7, 3.7], [0.35, 3.35]], [1, 2, 2, 2, 79]), ('gray100_0', [[1.0, 0.0], [2.0, 0.0], [2.0, 1.0], [1.0, 1.0], [1.0, 0.0]], [1, 2, 2, 2, 79]), ('gray102_0', [[1.0, 2.0], [2.0, 2.0], [2.0, 3.0], [1.0, 3.0], [1.0, 2.0]], [1, 2, 2, 2, 79]), ('gray102_1', [[1.0, 3.0], [2.0, 3.0], [2.35, 3.35], [1.35, 3.35], [1.0, 3.0]], [1, 2, 2, 2, 79]), ('gray301_0', [[3.0, 1.0], [4.0, 1.0], [4.0, 2.0], [3.0, 2.0], [3.0, 1.0]], [1, 2, 2, 2, 79]), ('gray301_1', [[4.0, 1.0], [4.35, 1.35], [4.35, 2.35], [4.0, 2.0], [4.0, 1.0]], [1, 2, 2, 2, 79]), ('gray302_0', [[3.0, 2.0], [4.0, 2.0], [4.0, 3.0], [3.0, 3.0], [3.0, 2.0]], [1, 2, 2, 2, 79]), ('gray302_1', [[4.0, 2.0], [4.35, 2.35], [4.35, 3.35], [4.0, 3.0], [4.0, 2.0]], [1, 2, 2, 2, 79]), ('gray302_2', [[3.0, 3.0], [4.0, 3.0], [4.35, 3.35], [3.35, 3.35], [3.0, 3.0]], [1, 2, 2, 2, 79])]:
                c.path(vertices, codes, id=object_id, zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 1.0], linewidth=0.0, capstyle='butt')
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Solid86().draw(sys.argv[1] if len(sys.argv) > 1 else None))
