"""Frozen question Solid135; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Solid135:

    def __init__(self):
        self.id = 'Solid135'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:935'
        self.question = 'The sculpture shown is made by gluing together cubic boxes with side length half a meter. Its surface, excluding the support base, is painted. Each can of paint covers 4 square meters. How many cans of paint are needed?'
        self.answer = '4'
        self.answer_type = 'number'
        self.query = self.question
        self.subject = 'SolidGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'SolidGeometry' / 'dataset_generator/scenes/Solid135.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('SolidGeometry', self.id, variant, output_path)
        with Canvas(SOLID, xlim=[-0.1494309512448595, 6.158515253570441], ylim=[-0.5289731024076509, 5.778973102407649], projection=[[1, 0.5, 0], [0, 0.5, 1]], origin=[0, 0, 0], offset=[0, 0]) as c:
            for object_id, points in [('pyramide0', c.project([[0.0, 0.0, 0.0], [1.0, 0.0, 0.0]])), ('pyramide1', c.project([[0.0, 0.0, 1.0], [1.0, 0.0, 1.0]])), ('pyramide2', c.project([[0.0, 1.0, 1.0], [0.25, 1.0, 1.0]])), ('pyramide3', c.project([[0.0, 0.0, 1.0], [0.0, 1.0, 1.0]])), ('pyramide4', c.project([[1.0, 0.0, 1.0], [1.0, 0.5, 1.0]])), ('pyramide5', c.project([[0.0, 0.0, 0.0], [0.0, 0.0, 1.0]])), ('pyramide6', c.project([[1.0, 0.0, 0.0], [1.0, 0.0, 1.0]])), ('pyramide7', c.project([[0.0, 1.0, 1.0], [0.0, 1.5, 1.0]])), ('pyramide8', c.project([[1.0, 0.0, 0.0], [2.0, 0.0, 0.0]])), ('pyramide9', c.project([[1.0, 0.0, 1.0], [2.0, 0.0, 1.0]])), ('pyramide10', c.project([[2.0, 0.0, 1.0], [2.0, 0.5, 1.0]])), ('pyramide11', c.project([[2.0, 0.0, 0.0], [2.0, 0.0, 1.0]])), ('pyramide12', c.project([[2.0, 0.0, 0.0], [3.0, 0.0, 0.0]])), ('pyramide13', c.project([[2.0, 0.0, 1.0], [3.0, 0.0, 1.0]])), ('pyramide14', c.project([[3.0, 0.0, 1.0], [3.0, 0.5, 1.0]])), ('pyramide15', c.project([[3.0, 0.0, 0.0], [3.0, 0.0, 1.0]])), ('pyramide16', c.project([[3.0, 0.0, 0.0], [4.0, 0.0, 0.0]])), ('pyramide17', c.project([[3.0, 0.0, 1.0], [4.0, 0.0, 1.0]])), ('pyramide18', c.project([[3.5, 1.0, 1.0], [4.0, 1.0, 1.0]])), ('pyramide19', c.project([[4.0, 0.0, 0.0], [4.0, 1.0, 0.0]])), ('pyramide20', c.project([[4.0, 0.0, 1.0], [4.0, 1.0, 1.0]])), ('pyramide21', c.project([[4.0, 0.0, 0.0], [4.0, 0.0, 1.0]])), ('pyramide22', c.project([[4.0, 1.0, 0.0], [4.0, 1.0, 1.0]])), ('pyramide23', c.project([[3.5, 2.0, 1.0], [4.0, 2.0, 1.0]])), ('pyramide24', c.project([[4.0, 1.0, 0.0], [4.0, 2.0, 0.0]])), ('pyramide25', c.project([[4.0, 1.0, 1.0], [4.0, 2.0, 1.0]])), ('pyramide26', c.project([[4.0, 2.0, 0.0], [4.0, 2.0, 1.0]])), ('pyramide27', c.project([[3.5, 3.0, 1.0], [4.0, 3.0, 1.0]])), ('pyramide28', c.project([[4.0, 2.0, 0.0], [4.0, 3.0, 0.0]])), ('pyramide29', c.project([[4.0, 2.0, 1.0], [4.0, 3.0, 1.0]])), ('pyramide30', c.project([[4.0, 3.0, 0.0], [4.0, 3.0, 1.0]])), ('pyramide31', c.project([[3.25, 4.0, 1.0], [4.0, 4.0, 1.0]])), ('pyramide32', c.project([[4.0, 3.0, 0.0], [4.0, 4.0, 0.0]])), ('pyramide33', c.project([[4.0, 3.0, 1.0], [4.0, 4.0, 1.0]])), ('pyramide34', c.project([[4.0, 4.0, 0.0], [4.0, 4.0, 1.0]])), ('pyramide35', c.project([[0.5, 0.5, 1.0], [1.5, 0.5, 1.0]])), ('pyramide36', c.project([[0.5, 0.5, 2.0], [1.5, 0.5, 2.0]])), ('pyramide37', c.project([[0.5, 1.5, 2.0], [0.75, 1.5, 2.0]])), ('pyramide38', c.project([[0.5, 0.5, 2.0], [0.5, 1.5, 2.0]])), ('pyramide39', c.project([[1.5, 0.5, 2.0], [1.5, 1.0, 2.0]])), ('pyramide40', c.project([[0.5, 0.5, 1.0], [0.5, 0.5, 2.0]])), ('pyramide41', c.project([[1.5, 0.5, 1.0], [1.5, 0.5, 2.0]])), ('pyramide42', c.project([[0.5, 1.5, 2.0], [0.5, 2.0, 2.0]])), ('pyramide43', c.project([[1.5, 0.5, 1.0], [2.5, 0.5, 1.0]])), ('pyramide44', c.project([[1.5, 0.5, 2.0], [2.5, 0.5, 2.0]])), ('pyramide45', c.project([[2.5, 0.5, 2.0], [2.5, 1.0, 2.0]])), ('pyramide46', c.project([[2.5, 0.5, 1.0], [2.5, 0.5, 2.0]])), ('pyramide47', c.project([[2.5, 0.5, 1.0], [3.5, 0.5, 1.0]])), ('pyramide48', c.project([[2.5, 0.5, 2.0], [3.5, 0.5, 2.0]])), ('pyramide49', c.project([[3.0, 1.5, 2.0], [3.5, 1.5, 2.0]])), ('pyramide50', c.project([[3.5, 0.5, 1.0], [3.5, 1.5, 1.0]])), ('pyramide51', c.project([[3.5, 0.5, 2.0], [3.5, 1.5, 2.0]])), ('pyramide52', c.project([[3.5, 0.5, 1.0], [3.5, 0.5, 2.0]])), ('pyramide53', c.project([[3.5, 1.5, 1.0], [3.5, 1.5, 2.0]])), ('pyramide54', c.project([[3.0, 2.5, 2.0], [3.5, 2.5, 2.0]])), ('pyramide55', c.project([[3.5, 1.5, 1.0], [3.5, 2.5, 1.0]])), ('pyramide56', c.project([[3.5, 1.5, 2.0], [3.5, 2.5, 2.0]])), ('pyramide57', c.project([[3.5, 2.5, 1.0], [3.5, 2.5, 2.0]])), ('pyramide58', c.project([[2.75, 3.5, 2.0], [3.5, 3.5, 2.0]])), ('pyramide59', c.project([[3.5, 2.5, 1.0], [3.5, 3.5, 1.0]])), ('pyramide60', c.project([[3.5, 2.5, 2.0], [3.5, 3.5, 2.0]])), ('pyramide61', c.project([[3.5, 3.5, 1.0], [3.5, 3.5, 2.0]])), ('pyramide62', c.project([[1.0, 1.0, 2.0], [2.0, 1.0, 2.0]])), ('pyramide63', c.project([[1.0, 1.0, 3.0], [2.0, 1.0, 3.0]])), ('pyramide64', c.project([[1.0, 2.0, 3.0], [1.25, 2.0, 3.0]])), ('pyramide65', c.project([[1.0, 1.0, 3.0], [1.0, 2.0, 3.0]])), ('pyramide66', c.project([[2.0, 1.0, 3.0], [2.0, 1.5, 3.0]])), ('pyramide67', c.project([[1.0, 1.0, 2.0], [1.0, 1.0, 3.0]])), ('pyramide68', c.project([[2.0, 1.0, 2.0], [2.0, 1.0, 3.0]])), ('pyramide69', c.project([[1.0, 2.0, 3.0], [1.0, 2.5, 3.0]])), ('pyramide70', c.project([[2.0, 1.0, 2.0], [3.0, 1.0, 2.0]])), ('pyramide71', c.project([[2.0, 1.0, 3.0], [3.0, 1.0, 3.0]])), ('pyramide72', c.project([[2.5, 2.0, 3.0], [3.0, 2.0, 3.0]])), ('pyramide73', c.project([[3.0, 1.0, 2.0], [3.0, 2.0, 2.0]])), ('pyramide74', c.project([[3.0, 1.0, 3.0], [3.0, 2.0, 3.0]])), ('pyramide75', c.project([[3.0, 1.0, 2.0], [3.0, 1.0, 3.0]])), ('pyramide76', c.project([[3.0, 2.0, 2.0], [3.0, 2.0, 3.0]])), ('pyramide77', c.project([[2.25, 3.0, 3.0], [3.0, 3.0, 3.0]])), ('pyramide78', c.project([[3.0, 2.0, 2.0], [3.0, 3.0, 2.0]])), ('pyramide79', c.project([[3.0, 2.0, 3.0], [3.0, 3.0, 3.0]])), ('pyramide80', c.project([[3.0, 3.0, 2.0], [3.0, 3.0, 3.0]])), ('pyramide81', c.project([[1.5, 1.5, 3.0], [2.5, 1.5, 3.0]])), ('pyramide82', c.project([[1.5, 1.5, 4.0], [2.5, 1.5, 4.0]])), ('pyramide83', c.project([[1.5, 2.5, 4.0], [2.5, 2.5, 4.0]])), ('pyramide84', c.project([[1.5, 1.5, 4.0], [1.5, 2.5, 4.0]])), ('pyramide85', c.project([[2.5, 1.5, 3.0], [2.5, 2.5, 3.0]])), ('pyramide86', c.project([[2.5, 1.5, 4.0], [2.5, 2.5, 4.0]])), ('pyramide87', c.project([[1.5, 1.5, 3.0], [1.5, 1.5, 4.0]])), ('pyramide88', c.project([[2.5, 1.5, 3.0], [2.5, 1.5, 4.0]])), ('pyramide89', c.project([[2.5, 2.5, 3.0], [2.5, 2.5, 4.0]]))]:
                c.line(points, id=object_id, clip_on=False, zorder=3)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Solid135().draw(sys.argv[1] if len(sys.argv) > 1 else None))
