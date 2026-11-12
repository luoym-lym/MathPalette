"""Frozen question Solid191; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Solid191:

    def __init__(self):
        self.id = 'Solid191'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:1824'
        self.question = 'The numbers on each pair of opposite faces on a die add up to 7. A die is rolled without slipping around the circuit shown. At the start the top face is 3. What number will be displayed on the top face at the end point?'
        self.answer = '6'
        self.answer_type = 'number'
        self.query = self.question
        self.subject = 'SolidGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'SolidGeometry' / 'dataset_generator/scenes/Solid191.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('SolidGeometry', self.id, variant, output_path)
        with Canvas(SOLID, xlim=[0.6605311121714643, 6.547947569999078], ylim=[-0.22294756999907817, 5.664468887828535], projection=[[1, 0.4, 0], [0, 0.35, 1]], origin=[0, 0, 0], offset=[0, 0]) as c:
            for object_id, points in [('panel0grid0part0', c.project([[0.0, 2.0, 3.4], [1.0, 2.0, 3.4]])), ('panel0grid1part0', c.project([[1.0, 2.0, 3.4], [1.0, 3.0, 3.4]])), ('panel0grid4part0', c.project([[1.0, 2.0, 3.4], [2.0, 2.0, 3.4]])), ('panel0grid5part0', c.project([[2.0, 2.0, 3.4], [2.0, 3.0, 3.4]])), ('panel0grid6part0', c.project([[2.0, 3.0, 3.4], [1.0, 3.0, 3.4]])), ('panel0grid7part0', c.project([[2.0, 2.0, 3.4], [3.0, 2.0, 3.4]])), ('panel0grid8part0', c.project([[3.0, 2.0, 3.4], [3.0, 3.0, 3.4]])), ('panel0grid9part0', c.project([[3.0, 3.0, 3.4], [2.0, 3.0, 3.4]])), ('panel0grid10part0', c.project([[2.0, 1.0, 3.4], [3.0, 1.0, 3.4]])), ('panel0grid11part0', c.project([[3.0, 1.0, 3.4], [3.0, 2.0, 3.4]])), ('panel0grid12part0', c.project([[2.0, 2.0, 3.4], [2.0, 1.0, 3.4]])), ('panel0grid13part0', c.project([[2.0, 0.0, 3.4], [3.0, 0.0, 3.4]])), ('panel0grid14part0', c.project([[3.0, 0.0, 3.4], [3.0, 1.0, 3.4]])), ('panel0grid15part0', c.project([[2.0, 1.0, 3.4], [2.0, 0.0, 3.4]])), ('panel0grid16part0', c.project([[3.0, 0.0, 3.4], [4.0, 0.0, 3.4]])), ('panel0grid17part0', c.project([[4.0, 0.0, 3.4], [4.0, 1.0, 3.4]])), ('panel0grid18part0', c.project([[4.0, 1.0, 3.4], [3.0, 1.0, 3.4]])), ('panel0grid19part0', c.project([[4.0, 0.0, 3.4], [5.0, 0.0, 3.4]])), ('panel0grid20part0', c.project([[5.0, 0.0, 3.4], [5.0, 1.0, 3.4]])), ('panel0grid21part0', c.project([[5.0, 1.0, 3.4], [4.0, 1.0, 3.4]])), ('panel0grid22part0', c.project([[5.0, 0.0, 3.4], [6.0, 0.0, 3.4]])), ('panel0grid23part0', c.project([[6.0, 0.0, 3.4], [6.0, 1.0, 3.4]])), ('panel0grid24part0', c.project([[6.0, 1.0, 3.4], [5.0, 1.0, 3.4]])), ('panel0diee0', c.project([[0.0, 2.0, 3.4], [1.0, 2.0, 3.4]])), ('panel0diee1', c.project([[0.0, 2.0, 4.4], [1.0, 2.0, 4.4]])), ('panel0diee2', c.project([[0.0, 3.0, 4.4], [1.0, 3.0, 4.4]])), ('panel0diee3', c.project([[0.0, 2.0, 4.4], [0.0, 3.0, 4.4]])), ('panel0diee4', c.project([[1.0, 2.0, 3.4], [1.0, 3.0, 3.4]])), ('panel0diee5', c.project([[1.0, 2.0, 4.4], [1.0, 3.0, 4.4]])), ('panel0diee6', c.project([[0.0, 2.0, 3.4], [0.0, 2.0, 4.4]])), ('panel0diee7', c.project([[1.0, 2.0, 3.4], [1.0, 2.0, 4.4]])), ('panel0diee8', c.project([[1.0, 3.0, 3.4], [1.0, 3.0, 4.4]]))]:
                c.line(points, id=object_id, clip_on=False, zorder=3)
            for object_id, points in [('uppertop0', c.project([[0.25, 2.25, 4.4]])), ('uppertop1', c.project([[0.5, 2.5, 4.4]])), ('uppertop2', c.project([[0.75, 2.75, 4.4]])), ('upperfront0', c.project([[0.25, 2.0, 3.65]])), ('upperfront1', c.project([[0.75, 2.0, 4.15]])), ('upperright0', c.project([[1.0, 2.5, 3.9]]))]:
                c.point(points, id=object_id, filled=True)
            for object_id, points in [('panel1grid0part0', c.project([[0.0, 2.0, 0.0], [1.0, 2.0, 0.0]])), ('panel1grid2part0', c.project([[0.6, 3.0, 0.0], [0.0, 3.0, 0.0]])), ('panel1grid3part0', c.project([[0.0, 3.0, 0.0], [0.0, 2.0, 0.0]])), ('panel1grid4part0', c.project([[1.0, 2.0, 0.0], [2.0, 2.0, 0.0]])), ('panel1grid5part0', c.project([[2.0, 2.0, 0.0], [2.0, 3.0, 0.0]])), ('panel1grid7part0', c.project([[2.0, 2.0, 0.0], [3.0, 2.0, 0.0]])), ('panel1grid8part0', c.project([[3.0, 2.0, 0.0], [3.0, 3.0, 0.0]])), ('panel1grid9part0', c.project([[3.0, 3.0, 0.0], [2.0, 3.0, 0.0]])), ('panel1grid10part0', c.project([[2.0, 1.0, 0.0], [3.0, 1.0, 0.0]])), ('panel1grid11part0', c.project([[3.0, 1.0, 0.0], [3.0, 2.0, 0.0]])), ('panel1grid12part0', c.project([[2.0, 2.0, 0.0], [2.0, 1.0, 0.0]])), ('panel1grid13part0', c.project([[2.0, 0.0, 0.0], [3.0, 0.0, 0.0]])), ('panel1grid14part0', c.project([[3.0, 0.0, 0.0], [3.0, 1.0, 0.0]])), ('panel1grid15part0', c.project([[2.0, 1.0, 0.0], [2.0, 0.0, 0.0]])), ('panel1grid16part0', c.project([[3.0, 0.0, 0.0], [4.0, 0.0, 0.0]])), ('panel1grid17part0', c.project([[4.0, 0.0, 0.0], [4.0, 1.0, 0.0]])), ('panel1grid18part0', c.project([[4.0, 1.0, 0.0], [3.0, 1.0, 0.0]])), ('panel1grid19part0', c.project([[4.0, 0.0, 0.0], [5.0, 0.0, 0.0]])), ('panel1grid20part0', c.project([[5.0, 0.0, 0.0], [5.0, 1.0, 0.0]])), ('panel1grid21part0', c.project([[5.0, 1.0, 0.0], [4.0, 1.0, 0.0]])), ('panel1grid22part0', c.project([[5.0, 0.0, 0.0], [6.0, 0.0, 0.0]])), ('panel1grid23part0', c.project([[6.0, 0.0, 0.0], [6.0, 1.0, 0.0]])), ('panel1grid24part0', c.project([[6.0, 1.0, 0.0], [5.0, 1.0, 0.0]])), ('panel1diee0', c.project([[1.0, 2.0, 0.0], [2.0, 2.0, 0.0]])), ('panel1diee1', c.project([[1.0, 2.0, 1.0], [2.0, 2.0, 1.0]])), ('panel1diee2', c.project([[1.0, 3.0, 1.0], [2.0, 3.0, 1.0]])), ('panel1diee3', c.project([[1.0, 2.0, 1.0], [1.0, 3.0, 1.0]])), ('panel1diee4', c.project([[2.0, 2.0, 0.0], [2.0, 3.0, 0.0]])), ('panel1diee5', c.project([[2.0, 2.0, 1.0], [2.0, 3.0, 1.0]])), ('panel1diee6', c.project([[1.0, 2.0, 0.0], [1.0, 2.0, 1.0]])), ('panel1diee7', c.project([[2.0, 2.0, 0.0], [2.0, 2.0, 1.0]])), ('panel1diee8', c.project([[2.0, 3.0, 0.0], [2.0, 3.0, 1.0]]))]:
                c.line(points, id=object_id, clip_on=False, zorder=3)
            for object_id, points in [('lowertop0', c.project([[1.22, 2.25, 1.0]])), ('lowertop1', c.project([[1.22, 2.75, 1.0]])), ('lowertop2', c.project([[1.5, 2.25, 1.0]])), ('lowertop3', c.project([[1.5, 2.75, 1.0]])), ('lowertop4', c.project([[1.78, 2.25, 1.0]])), ('lowertop5', c.project([[1.78, 2.75, 1.0]])), ('lowerfront0', c.project([[1.25, 2.0, 0.75]])), ('lowerfront1', c.project([[1.75, 2.0, 0.25]])), ('lowerright0', c.project([[2.0, 2.25, 0.75]])), ('lowerright1', c.project([[2.0, 2.5, 0.5]])), ('lowerright2', c.project([[2.0, 2.75, 0.25]]))]:
                c.point(points, id=object_id, filled=True)
            c.text('Start', c.project([0.4, 2, 3.4]), offset_pt=[0, -20], vertex=False, id='start')
            c.text('End', c.project([5.5, 0, 3.4]), offset_pt=[0, -20], vertex=False, id='end')
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Solid191().draw(sys.argv[1] if len(sys.argv) > 1 else None))
