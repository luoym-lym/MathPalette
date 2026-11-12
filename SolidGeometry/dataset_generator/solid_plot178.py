"""Frozen question Solid178; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Solid178:

    def __init__(self):
        self.id = 'Solid178'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:1635'
        self.question = "The cube shown is divided into 64 small cubes. Exactly one of the cubes is grey, as shown in the diagram. Two cubes are said to be 'neighbours' if they have a common face.\nOn the first day, the white neighbours of the grey cube are changed to grey. On the second day, the white neighbours of all the grey cubes are changed to grey.\nHow many grey cubes are there at the end of the second day?"
        self.answer = '17'
        self.answer_type = 'number'
        self.query = self.question
        self.subject = 'SolidGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'SolidGeometry' / 'dataset_generator/scenes/Solid178.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('SolidGeometry', self.id, variant, output_path)
        with Canvas(SOLID, xlim=[-0.1344878561203724, 5.542663728213396], ylim=[-0.14266372821339557, 5.534487856120373], projection=[[1, 0.35, 0], [0, 0.35, 1]], origin=[0, 0, 0], offset=[0, 0]) as c:
            for object_id, points in [('gride0', c.project([[0.0, 0.0, 0.0], [1.0, 0.0, 0.0]])), ('gride1', c.project([[0.0, 0.0, 1.0], [1.0, 0.0, 1.0]])), ('gride2', c.project([[0.0, 0.0, 0.0], [0.0, 0.0, 1.0]])), ('gride3', c.project([[1.0, 0.0, 0.0], [1.0, 0.0, 1.0]])), ('gride4', c.project([[0.0, 0.0, 2.0], [1.0, 0.0, 2.0]])), ('gride5', c.project([[0.0, 0.0, 1.0], [0.0, 0.0, 2.0]])), ('gride6', c.project([[1.0, 0.0, 1.0], [1.0, 0.0, 2.0]])), ('gride7', c.project([[0.0, 0.0, 3.0], [1.0, 0.0, 3.0]])), ('gride8', c.project([[0.0, 0.0, 2.0], [0.0, 0.0, 3.0]])), ('gride9', c.project([[1.0, 0.0, 2.0], [1.0, 0.0, 3.0]])), ('gride10', c.project([[0.0, 0.0, 4.0], [1.0, 0.0, 4.0]])), ('gride11', c.project([[0.0, 1.0, 4.0], [1.0, 1.0, 4.0]])), ('gride12', c.project([[0.0, 0.0, 4.0], [0.0, 1.0, 4.0]])), ('gride13', c.project([[1.0, 0.0, 4.0], [1.0, 1.0, 4.0]])), ('gride14', c.project([[0.0, 0.0, 3.0], [0.0, 0.0, 4.0]])), ('gride15', c.project([[1.0, 0.0, 3.0], [1.0, 0.0, 4.0]])), ('gride16', c.project([[0.0, 2.0, 4.0], [1.0, 2.0, 4.0]])), ('gride17', c.project([[0.0, 1.0, 4.0], [0.0, 2.0, 4.0]])), ('gride18', c.project([[1.0, 1.0, 4.0], [1.0, 2.0, 4.0]])), ('gride19', c.project([[0.0, 3.0, 4.0], [1.0, 3.0, 4.0]])), ('gride20', c.project([[0.0, 2.0, 4.0], [0.0, 3.0, 4.0]])), ('gride21', c.project([[1.0, 2.0, 4.0], [1.0, 3.0, 4.0]])), ('gride22', c.project([[0.0, 4.0, 4.0], [1.0, 4.0, 4.0]])), ('gride23', c.project([[0.0, 3.0, 4.0], [0.0, 4.0, 4.0]])), ('gride24', c.project([[1.0, 3.0, 4.0], [1.0, 4.0, 4.0]])), ('gride25', c.project([[1.0, 0.0, 0.0], [2.0, 0.0, 0.0]])), ('gride26', c.project([[1.0, 0.0, 1.0], [2.0, 0.0, 1.0]])), ('gride27', c.project([[2.0, 0.0, 0.0], [2.0, 0.0, 1.0]])), ('gride28', c.project([[1.0, 0.0, 2.0], [2.0, 0.0, 2.0]])), ('gride29', c.project([[2.0, 0.0, 1.0], [2.0, 0.0, 2.0]])), ('gride30', c.project([[1.0, 0.0, 3.0], [2.0, 0.0, 3.0]])), ('gride31', c.project([[2.0, 0.0, 2.0], [2.0, 0.0, 3.0]])), ('gride32', c.project([[1.0, 0.0, 4.0], [2.0, 0.0, 4.0]])), ('gride33', c.project([[1.0, 1.0, 4.0], [2.0, 1.0, 4.0]])), ('gride34', c.project([[2.0, 0.0, 4.0], [2.0, 1.0, 4.0]])), ('gride35', c.project([[2.0, 0.0, 3.0], [2.0, 0.0, 4.0]])), ('gride36', c.project([[1.0, 2.0, 4.0], [2.0, 2.0, 4.0]])), ('gride37', c.project([[2.0, 1.0, 4.0], [2.0, 2.0, 4.0]])), ('gride38', c.project([[1.0, 3.0, 4.0], [2.0, 3.0, 4.0]])), ('gride39', c.project([[2.0, 2.0, 4.0], [2.0, 3.0, 4.0]])), ('gride40', c.project([[1.0, 4.0, 4.0], [2.0, 4.0, 4.0]])), ('gride41', c.project([[2.0, 3.0, 4.0], [2.0, 4.0, 4.0]])), ('gride42', c.project([[2.0, 0.0, 0.0], [3.0, 0.0, 0.0]])), ('gride43', c.project([[2.0, 0.0, 1.0], [3.0, 0.0, 1.0]])), ('gride44', c.project([[3.0, 0.0, 0.0], [3.0, 0.0, 1.0]])), ('gride45', c.project([[2.0, 0.0, 2.0], [3.0, 0.0, 2.0]])), ('gride46', c.project([[3.0, 0.0, 1.0], [3.0, 0.0, 2.0]])), ('gride47', c.project([[2.0, 0.0, 3.0], [3.0, 0.0, 3.0]])), ('gride48', c.project([[3.0, 0.0, 2.0], [3.0, 0.0, 3.0]])), ('gride49', c.project([[2.0, 0.0, 4.0], [3.0, 0.0, 4.0]])), ('gride50', c.project([[2.0, 1.0, 4.0], [3.0, 1.0, 4.0]])), ('gride51', c.project([[3.0, 0.0, 4.0], [3.0, 1.0, 4.0]])), ('gride52', c.project([[3.0, 0.0, 3.0], [3.0, 0.0, 4.0]])), ('gride53', c.project([[2.0, 2.0, 4.0], [3.0, 2.0, 4.0]])), ('gride54', c.project([[3.0, 1.0, 4.0], [3.0, 2.0, 4.0]])), ('gride55', c.project([[2.0, 3.0, 4.0], [3.0, 3.0, 4.0]])), ('gride56', c.project([[3.0, 2.0, 4.0], [3.0, 3.0, 4.0]])), ('gride57', c.project([[2.0, 4.0, 4.0], [3.0, 4.0, 4.0]])), ('gride58', c.project([[3.0, 3.0, 4.0], [3.0, 4.0, 4.0]])), ('gride59', c.project([[3.0, 0.0, 0.0], [4.0, 0.0, 0.0]])), ('gride60', c.project([[3.0, 0.0, 1.0], [4.0, 0.0, 1.0]])), ('gride61', c.project([[4.0, 0.0, 0.0], [4.0, 1.0, 0.0]])), ('gride62', c.project([[4.0, 0.0, 1.0], [4.0, 1.0, 1.0]])), ('gride63', c.project([[4.0, 0.0, 0.0], [4.0, 0.0, 1.0]])), ('gride64', c.project([[4.0, 1.0, 0.0], [4.0, 1.0, 1.0]])), ('gride65', c.project([[3.0, 0.0, 2.0], [4.0, 0.0, 2.0]])), ('gride66', c.project([[4.0, 0.0, 2.0], [4.0, 1.0, 2.0]])), ('gride67', c.project([[4.0, 0.0, 1.0], [4.0, 0.0, 2.0]])), ('gride68', c.project([[4.0, 1.0, 1.0], [4.0, 1.0, 2.0]])), ('gride69', c.project([[3.0, 0.0, 3.0], [4.0, 0.0, 3.0]])), ('gride70', c.project([[4.0, 0.0, 3.0], [4.0, 1.0, 3.0]])), ('gride71', c.project([[4.0, 0.0, 2.0], [4.0, 0.0, 3.0]])), ('gride72', c.project([[4.0, 1.0, 2.0], [4.0, 1.0, 3.0]])), ('gride73', c.project([[3.0, 0.0, 4.0], [4.0, 0.0, 4.0]])), ('gride74', c.project([[3.0, 1.0, 4.0], [4.0, 1.0, 4.0]])), ('gride75', c.project([[4.0, 0.0, 4.0], [4.0, 1.0, 4.0]])), ('gride76', c.project([[4.0, 0.0, 3.0], [4.0, 0.0, 4.0]])), ('gride77', c.project([[4.0, 1.0, 3.0], [4.0, 1.0, 4.0]])), ('gride78', c.project([[4.0, 1.0, 0.0], [4.0, 2.0, 0.0]])), ('gride79', c.project([[4.0, 1.0, 1.0], [4.0, 2.0, 1.0]])), ('gride80', c.project([[4.0, 2.0, 0.0], [4.0, 2.0, 1.0]])), ('gride81', c.project([[4.0, 1.0, 2.0], [4.0, 2.0, 2.0]])), ('gride82', c.project([[4.0, 2.0, 1.0], [4.0, 2.0, 2.0]])), ('gride83', c.project([[4.0, 1.0, 3.0], [4.0, 2.0, 3.0]])), ('gride84', c.project([[4.0, 2.0, 2.0], [4.0, 2.0, 3.0]])), ('gride85', c.project([[3.0, 2.0, 4.0], [4.0, 2.0, 4.0]])), ('gride86', c.project([[4.0, 1.0, 4.0], [4.0, 2.0, 4.0]])), ('gride87', c.project([[4.0, 2.0, 3.0], [4.0, 2.0, 4.0]])), ('gride88', c.project([[4.0, 2.0, 0.0], [4.0, 3.0, 0.0]])), ('gride89', c.project([[4.0, 2.0, 1.0], [4.0, 3.0, 1.0]])), ('gride90', c.project([[4.0, 3.0, 0.0], [4.0, 3.0, 1.0]])), ('gride91', c.project([[4.0, 2.0, 2.0], [4.0, 3.0, 2.0]])), ('gride92', c.project([[4.0, 3.0, 1.0], [4.0, 3.0, 2.0]])), ('gride93', c.project([[4.0, 2.0, 3.0], [4.0, 3.0, 3.0]])), ('gride94', c.project([[4.0, 3.0, 2.0], [4.0, 3.0, 3.0]])), ('gride95', c.project([[3.0, 3.0, 4.0], [4.0, 3.0, 4.0]])), ('gride96', c.project([[4.0, 2.0, 4.0], [4.0, 3.0, 4.0]])), ('gride97', c.project([[4.0, 3.0, 3.0], [4.0, 3.0, 4.0]])), ('gride98', c.project([[4.0, 3.0, 0.0], [4.0, 4.0, 0.0]])), ('gride99', c.project([[4.0, 3.0, 1.0], [4.0, 4.0, 1.0]])), ('gride100', c.project([[4.0, 4.0, 0.0], [4.0, 4.0, 1.0]])), ('gride101', c.project([[4.0, 3.0, 2.0], [4.0, 4.0, 2.0]])), ('gride102', c.project([[4.0, 4.0, 1.0], [4.0, 4.0, 2.0]])), ('gride103', c.project([[4.0, 3.0, 3.0], [4.0, 4.0, 3.0]])), ('gride104', c.project([[4.0, 4.0, 2.0], [4.0, 4.0, 3.0]])), ('gride105', c.project([[3.0, 4.0, 4.0], [4.0, 4.0, 4.0]])), ('gride106', c.project([[4.0, 3.0, 4.0], [4.0, 4.0, 4.0]])), ('gride107', c.project([[4.0, 4.0, 3.0], [4.0, 4.0, 4.0]]))]:
                c.line(points, id=object_id, clip_on=False, zorder=3)
            c.fill(c.project([[1, 2, 4], [2, 2, 4], [2, 3, 4], [1, 3, 4]]), facecolor='#E6E6E6', alpha=1, id='graycell')
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Solid178().draw(sys.argv[1] if len(sys.argv) > 1 else None))
