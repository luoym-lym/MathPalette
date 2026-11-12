"""Frozen question Solid102; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Solid102:

    def __init__(self):
        self.id = 'Solid102'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:339'
        self.question = 'The structure shown has eight faces and is formed from six equal cubes and two different rectangular blocks. Painting every piece entirely before gluing them together requires 18 liters of paint, regardless of color. How many liters of paint are needed to paint the whole structure after the pieces are glued together?'
        self.answer = '11.5'
        self.answer_type = 'number'
        self.query = self.question
        self.subject = 'SolidGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'SolidGeometry' / 'dataset_generator/scenes/Solid102.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('SolidGeometry', self.id, variant, output_path)
        with Canvas(SOLID, xlim=[-0.10833743965252207, 4.46492355883857], ylim=[-0.1149235588385693, 4.458337439652523], projection=[[1, 0.35, 0], [0, 0.35, 1]], origin=[0, 0, 0], offset=[0, 0]) as c:
            for object_id, points in [('outlinee0', c.project([[0.0, 0.0, 0.0], [1.0, 0.0, 0.0]])), ('outlinee1', c.project([[0.0, 0.0, 0.0], [0.0, 0.0, 1.0]])), ('outlinee2', c.project([[0.0, 0.0, 1.0], [0.0, 0.0, 2.0]])), ('outlinee3', c.project([[0.0, 0.0, 3.0], [1.0, 0.0, 3.0]])), ('outlinee4', c.project([[0.0, 1.0, 3.0], [0.65, 1.0, 3.0]])), ('outlinee5', c.project([[0.0, 0.0, 3.0], [0.0, 1.0, 3.0]])), ('outlinee6', c.project([[0.0, 0.0, 2.0], [0.0, 0.0, 3.0]])), ('outlinee7', c.project([[1.0, 0.0, 0.0], [2.0, 0.0, 0.0]])), ('outlinee8', c.project([[1.0, 0.0, 4.0], [2.0, 0.0, 4.0]])), ('outlinee9', c.project([[1.0, 1.0, 4.0], [2.0, 1.0, 4.0]])), ('outlinee10', c.project([[1.0, 0.0, 4.0], [1.0, 1.0, 4.0]])), ('outlinee11', c.project([[1.0, 0.0, 3.0], [1.0, 0.0, 4.0]])), ('outlinee12', c.project([[2.0, 0.0, 0.0], [3.0, 0.0, 0.0]])), ('outlinee13', c.project([[2.0, 0.0, 4.0], [3.0, 0.0, 4.0]])), ('outlinee14', c.project([[2.0, 1.0, 4.0], [3.0, 1.0, 4.0]])), ('outlinee15', c.project([[3.0, 0.0, 0.0], [4.0, 0.0, 0.0]])), ('outlinee16', c.project([[4.0, 0.0, 0.0], [4.0, 1.0, 0.0]])), ('outlinee17', c.project([[4.0, 0.0, 0.0], [4.0, 0.0, 1.0]])), ('outlinee18', c.project([[4.0, 1.0, 0.0], [4.0, 1.0, 1.0]])), ('outlinee19', c.project([[4.0, 0.0, 1.0], [4.0, 0.0, 2.0]])), ('outlinee20', c.project([[4.0, 1.0, 1.0], [4.0, 1.0, 2.0]])), ('outlinee21', c.project([[4.0, 0.0, 2.0], [4.0, 0.0, 3.0]])), ('outlinee22', c.project([[4.0, 1.0, 2.0], [4.0, 1.0, 3.0]])), ('outlinee23', c.project([[3.0, 0.0, 4.0], [4.0, 0.0, 4.0]])), ('outlinee24', c.project([[3.0, 1.0, 4.0], [4.0, 1.0, 4.0]])), ('outlinee25', c.project([[4.0, 0.0, 4.0], [4.0, 1.0, 4.0]])), ('outlinee26', c.project([[4.0, 0.0, 3.0], [4.0, 0.0, 4.0]])), ('outlinee27', c.project([[4.0, 1.0, 3.0], [4.0, 1.0, 4.0]])), ('partseam0', c.project([[0, 0, 1], [1, 0, 1]])), ('partseam1', c.project([[0, 0, 2], [1, 0, 2]])), ('partseam2', c.project([[1, 0, 0], [1, 0, 3]])), ('partseam3', c.project([[1, 0, 2], [4, 0, 2]])), ('partseam4', c.project([[1, 0, 3], [4, 0, 3]])), ('partseam5', c.project([[4, 0, 2], [4, 1, 2]])), ('partseam6', c.project([[4, 0, 3], [4, 1, 3]])), ('partseam7', c.project([[2, 0, 3], [2, 0, 4]])), ('partseam8', c.project([[3, 0, 3], [3, 0, 4]])), ('partseam9', c.project([[2, 0, 4], [2, 1, 4]])), ('partseam10', c.project([[3, 0, 4], [3, 1, 4]]))]:
                c.line(points, id=object_id, clip_on=False, zorder=3)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Solid102().draw(sys.argv[1] if len(sys.argv) > 1 else None))
