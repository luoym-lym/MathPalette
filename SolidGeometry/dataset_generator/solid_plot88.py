"""Frozen question Solid88; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Solid88:

    def __init__(self):
        self.id = 'Solid88'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:158'
        self.question = 'The figure shown is made by gluing 12 cubes together, using one drop of glue between each pair of cubes joined together. How many drops of glue are needed?'
        self.answer = '11'
        self.answer_type = 'number'
        self.query = self.question
        self.subject = 'SolidGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'SolidGeometry' / 'dataset_generator/scenes/Solid88.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('SolidGeometry', self.id, variant, output_path)
        with Canvas(SOLID, xlim=[-0.1232096186302778, 4.923181890381899], ylim=[-1.4731818903818996, 3.5732096186302775], projection=[[1, 0.4, 0], [-0.15, 0.45, 1]], origin=[0, 0, 0], offset=[0, 0]) as c:
            for object_id, points in [('treee0', c.project([[0.0, 0.0, 0.0], [1.0, 0.0, 0.0]])), ('treee1', c.project([[0.0, 0.0, 1.0], [1.0, 0.0, 1.0]])), ('treee2', c.project([[0.0, 1.0, 1.0], [1.0, 1.0, 1.0]])), ('treee3', c.project([[0.0, 0.0, 1.0], [0.0, 1.0, 1.0]])), ('treee4', c.project([[1.0, 0.0, 1.0], [1.0, 1.0, 1.0]])), ('treee5', c.project([[0.0, 0.0, 0.0], [0.0, 0.0, 1.0]])), ('treee6', c.project([[1.0, 0.0, 0.0], [1.0, 0.0, 1.0]])), ('treee7', c.project([[1.0, 0.0, 0.0], [1.2156862745099999, 0.0, 0.0]])), ('treee8', c.project([[1.0, 0.0, 1.0], [2.0, 0.0, 1.0]])), ('treee9', c.project([[1.0, 1.0, 1.0], [2.0, 1.0, 1.0]])), ('treee10', c.project([[2.0, 0.0, 1.0], [2.0, 1.0, 1.0]])), ('treee11', c.project([[2.0, 0.0, 1.0], [3.0, 0.0, 1.0]])), ('treee12', c.project([[2.0, 1.0, 1.0], [3.0, 1.0, 1.0]])), ('treee13', c.project([[3.0, 0.0, 1.0], [3.0, 1.0, 1.0]])), ('treee14', c.project([[3.0, 0.0, 0.0], [3.0, 0.0, 1.0]])), ('treee15', c.project([[3.0, 0.0, 0.0], [4.0, 0.0, 0.0]])), ('treee16', c.project([[3.0, 0.0, 1.0], [4.0, 0.0, 1.0]])), ('treee17', c.project([[3.0, 1.0, 1.0], [4.0, 1.0, 1.0]])), ('treee18', c.project([[4.0, 0.0, 0.0], [4.0, 1.0, 0.0]])), ('treee19', c.project([[4.0, 0.0, 1.0], [4.0, 1.0, 1.0]])), ('treee20', c.project([[4.0, 0.0, 0.0], [4.0, 0.0, 1.0]])), ('treee21', c.project([[4.0, 1.0, 0.0], [4.0, 1.0, 1.0]])), ('treee22', c.project([[2.0, -1.0, 1.0], [3.0, -1.0, 1.0]])), ('treee23', c.project([[2.0, -1.0, 1.0], [2.0, 0.0, 1.0]])), ('treee24', c.project([[3.0, -1.0, 0.0], [3.0, 0.0, 0.0]])), ('treee25', c.project([[3.0, -1.0, 1.0], [3.0, 0.0, 1.0]])), ('treee26', c.project([[3.0, -1.0, 0.0], [3.0, -1.0, 1.0]])), ('treee27', c.project([[2.0, -2.0, 0.0], [3.0, -2.0, 0.0]])), ('treee28', c.project([[2.0, -2.0, 1.0], [3.0, -2.0, 1.0]])), ('treee29', c.project([[2.0, -2.0, 1.0], [2.0, -1.0, 1.0]])), ('treee30', c.project([[3.0, -2.0, 0.0], [3.0, -1.0, 0.0]])), ('treee31', c.project([[3.0, -2.0, 1.0], [3.0, -1.0, 1.0]])), ('treee32', c.project([[2.0, -2.0, 0.0], [2.0, -2.0, 1.0]])), ('treee33', c.project([[3.0, -2.0, 0.0], [3.0, -2.0, 1.0]])), ('treee34', c.project([[0.0, 2.0, 1.0], [1.0, 2.0, 1.0]])), ('treee35', c.project([[0.0, 1.0, 1.0], [0.0, 2.0, 1.0]])), ('treee36', c.project([[1.0, 1.0, 1.0], [1.0, 2.0, 1.0]])), ('treee37', c.project([[1.0, 2.0, 0.49], [1.0, 2.0, 1.0]])), ('treee38', c.project([[1.0, 2.960784313725, 0.0], [1.0, 3.0, 0.0]])), ('treee39', c.project([[1.0, 2.0, 1.0], [1.0, 3.0, 1.0]])), ('treee40', c.project([[1.0, 3.0, 0.0], [1.0, 3.0, 1.0]])), ('treee41', c.project([[0.0, 2.0, 2.0], [1.0, 2.0, 2.0]])), ('treee42', c.project([[0.0, 3.0, 2.0], [1.0, 3.0, 2.0]])), ('treee43', c.project([[0.0, 2.0, 2.0], [0.0, 3.0, 2.0]])), ('treee44', c.project([[1.0, 2.0, 2.0], [1.0, 3.0, 2.0]])), ('treee45', c.project([[0.0, 2.0, 1.0], [0.0, 2.0, 2.0]])), ('treee46', c.project([[1.0, 2.0, 1.0], [1.0, 2.0, 2.0]])), ('treee47', c.project([[1.0, 3.0, 1.0], [1.0, 3.0, 2.0]])), ('treee48', c.project([[4.0, 1.0, 0.0], [4.0, 2.0, 0.0]])), ('treee49', c.project([[4.0, 1.0, 1.0], [4.0, 2.0, 1.0]])), ('treee50', c.project([[4.0, 2.0, 0.0], [4.0, 2.0, 1.0]])), ('treee51', c.project([[3.0, 1.0, 2.0], [4.0, 1.0, 2.0]])), ('treee52', c.project([[4.0, 1.0, 2.0], [4.0, 2.0, 2.0]])), ('treee53', c.project([[3.0, 1.0, 1.0], [3.0, 1.0, 2.0]])), ('treee54', c.project([[4.0, 1.0, 1.0], [4.0, 1.0, 2.0]])), ('treee55', c.project([[4.0, 2.0, 1.0], [4.0, 2.0, 2.0]])), ('treee56', c.project([[3.0, 1.0, 3.0], [4.0, 1.0, 3.0]])), ('treee57', c.project([[3.0, 2.0, 3.0], [4.0, 2.0, 3.0]])), ('treee58', c.project([[3.0, 1.0, 3.0], [3.0, 2.0, 3.0]])), ('treee59', c.project([[4.0, 1.0, 3.0], [4.0, 2.0, 3.0]])), ('treee60', c.project([[3.0, 1.0, 2.0], [3.0, 1.0, 3.0]])), ('treee61', c.project([[4.0, 1.0, 2.0], [4.0, 1.0, 3.0]])), ('treee62', c.project([[4.0, 2.0, 2.0], [4.0, 2.0, 3.0]]))]:
                c.line(points, id=object_id, clip_on=False, zorder=3)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Solid88().draw(sys.argv[1] if len(sys.argv) > 1 else None))
