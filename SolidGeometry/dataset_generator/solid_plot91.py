"""Frozen question Solid91; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Solid91:

    def __init__(self):
        self.id = 'Solid91'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:195'
        self.question = 'A die is in the position shown in the picture. It can be rolled along the path of 12 squares as shown. How many times must the die go around the path in order for it to return to its initial position with all faces in the initial positions?'
        self.answer = '3'
        self.answer_type = 'number'
        self.query = self.question
        self.subject = 'SolidGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'SolidGeometry' / 'dataset_generator/scenes/Solid91.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('SolidGeometry', self.id, variant, output_path)
        with Canvas(SOLID, xlim=[-0.1394688878285355, 5.747947569999077], ylim=[-1.687947569999078, 4.199468887828536], projection=[[1, 0.4, 0], [0, 0.38, 1]], origin=[0, 0, 0], offset=[0, 0]) as c:
            for object_id, points in [('ground0part0', c.project([[0.0, 0.0, 0.0], [1.0, 0.0, 0.0]])), ('ground1part0', c.project([[1.0, 0.0, 0.0], [1.0, 1.0, 0.0]])), ('ground2part0', c.project([[1.0, 1.0, 0.0], [0.0, 1.0, 0.0]])), ('ground3part0', c.project([[0.0, 1.0, 0.0], [0.0, 0.0, 0.0]])), ('ground4part0', c.project([[1.0, 1.0, 0.0], [1.0, 2.0, 0.0]])), ('ground5part0', c.project([[1.0, 2.0, 0.0], [0.0, 2.0, 0.0]])), ('ground6part0', c.project([[0.0, 2.0, 0.0], [0.0, 1.0, 0.0]])), ('ground7part0', c.project([[1.0, 2.0, 0.0], [1.0, 3.0, 0.0]])), ('ground8part0', c.project([[1.0, 3.0, 0.0], [0.0, 3.0, 0.0]])), ('ground9part0', c.project([[0.0, 3.0, 0.0], [0.0, 2.0, 0.0]])), ('ground10part0', c.project([[1.0, 3.0, 0.0], [1.0, 4.0, 0.0]])), ('ground13part0', c.project([[1.0, 0.0, 0.0], [2.0, 0.0, 0.0]])), ('ground14part0', c.project([[2.0, 0.0, 0.0], [2.0, 1.0, 0.0]])), ('ground15part0', c.project([[2.0, 1.0, 0.0], [1.0, 1.0, 0.0]])), ('ground16part0', c.project([[1.0, 3.0, 0.0], [2.0, 3.0, 0.0]])), ('ground17part0', c.project([[2.0, 3.0, 0.0], [2.0, 4.0, 0.0]])), ('ground18part0', c.project([[2.0, 4.0, 0.0], [1.0, 4.0, 0.0]])), ('ground19part0', c.project([[2.0, 0.0, 0.0], [3.0, 0.0, 0.0]])), ('ground20part0', c.project([[3.0, 0.0, 0.0], [3.0, 1.0, 0.0]])), ('ground21part0', c.project([[3.0, 1.0, 0.0], [2.0, 1.0, 0.0]])), ('ground22part0', c.project([[2.0, 3.0, 0.0], [3.0, 3.0, 0.0]])), ('ground23part0', c.project([[3.0, 3.0, 0.0], [3.0, 4.0, 0.0]])), ('ground24part0', c.project([[3.0, 4.0, 0.0], [2.0, 4.0, 0.0]])), ('ground25part0', c.project([[3.0, 0.0, 0.0], [4.0, 0.0, 0.0]])), ('ground26part0', c.project([[4.0, 0.0, 0.0], [4.0, 1.0, 0.0]])), ('ground27part0', c.project([[4.0, 1.0, 0.0], [3.0, 1.0, 0.0]])), ('ground28part0', c.project([[4.0, 1.0, 0.0], [4.0, 2.0, 0.0]])), ('ground29part0', c.project([[4.0, 2.0, 0.0], [3.0, 2.0, 0.0]])), ('ground30part0', c.project([[3.0, 2.0, 0.0], [3.0, 1.0, 0.0]])), ('ground31part0', c.project([[4.0, 2.0, 0.0], [4.0, 3.0, 0.0]])), ('ground32part0', c.project([[4.0, 3.0, 0.0], [3.0, 3.0, 0.0]])), ('ground33part0', c.project([[3.0, 3.0, 0.0], [3.0, 2.0, 0.0]])), ('ground34part0', c.project([[4.0, 3.0, 0.0], [4.0, 4.0, 0.0]])), ('ground35part0', c.project([[4.0, 4.0, 0.0], [3.0, 4.0, 0.0]])), ('diee0', c.project([[0.0, 3.0, 0.0], [1.0, 3.0, 0.0]])), ('diee1', c.project([[0.0, 3.0, 1.0], [1.0, 3.0, 1.0]])), ('diee2', c.project([[0.0, 4.0, 1.0], [1.0, 4.0, 1.0]])), ('diee3', c.project([[0.0, 3.0, 1.0], [0.0, 4.0, 1.0]])), ('diee4', c.project([[1.0, 3.0, 0.0], [1.0, 4.0, 0.0]])), ('diee5', c.project([[1.0, 3.0, 1.0], [1.0, 4.0, 1.0]])), ('diee6', c.project([[0.0, 3.0, 0.0], [0.0, 3.0, 1.0]])), ('diee7', c.project([[1.0, 3.0, 0.0], [1.0, 3.0, 1.0]])), ('diee8', c.project([[1.0, 4.0, 0.0], [1.0, 4.0, 1.0]]))]:
                c.line(points, id=object_id, clip_on=False, zorder=3)
            for object_id, points in [('toppip0', c.project([[0.3, 3.7, 1]])), ('toppip1', c.project([[0.7, 3.3, 1]])), ('frontpip0', c.project([[0.25, 3, 0.75]])), ('frontpip1', c.project([[0.5, 3, 0.5]])), ('frontpip2', c.project([[0.75, 3, 0.25]])), ('rightpip0', c.project([[1, 3.5, 0.5]]))]:
                c.point(points, id=object_id, filled=True)
            for object_id, points in [('arrowshaft', c.project([[1.4, 3.5, 0.6], [1.9, 3.5, 0.6]])), ('arrowhead1', c.project([[1.9, 3.5, 0.6], [1.78, 3.5, 0.64]])), ('arrowhead2', c.project([[1.9, 3.5, 0.6], [1.78, 3.5, 0.56]]))]:
                c.line(points, id=object_id, clip_on=False, zorder=3)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Solid91().draw(sys.argv[1] if len(sys.argv) > 1 else None))
