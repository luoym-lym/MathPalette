"""Frozen question Solid175; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Solid175:

    def __init__(self):
        self.id = 'Solid175'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:1594'
        self.question = 'A cube is rolled on a plane around its edges. Its bottom face passes through positions $1,2,3,4,5,6$ and 7 in that order, as shown. Which two of these positions were occupied by the same face of the cube?\nChoices:\nA:1 and 7\nB:1 and 6\nC:1 and 5\nD:2 and 7\nE:2 and 6'
        self.answer = 'B'
        self.answer_type = 'choice'
        self.choices = {'A': '1 and 7', 'B': '1 and 6', 'C': '1 and 5', 'D': '2 and 7', 'E': '2 and 6'}
        self.query = self.question
        self.subject = 'SolidGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'SolidGeometry' / 'dataset_generator/scenes/Solid175.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('SolidGeometry', self.id, variant, output_path)
        with Canvas(SOLID, xlim=[-0.12452579270404929, 5.132096044642034], ylim=[-1.1320960446420338, 4.124525792704049], projection=[[1, 0, 0], [0, 1, 0]], origin=[0, 0, 0], offset=[0, 0]) as c:
            for object_id, points in [('grid0', c.project([[0, 0, 0], [1, 0, 0]])), ('grid1', c.project([[1, 0, 0], [1, 1, 0]])), ('grid2', c.project([[1, 1, 0], [0, 1, 0]])), ('grid3', c.project([[0, 1, 0], [0, 0, 0]])), ('grid4', c.project([[1, 0, 0], [2, 0, 0]])), ('grid5', c.project([[2, 0, 0], [2, 1, 0]])), ('grid6', c.project([[2, 1, 0], [1, 1, 0]])), ('grid7', c.project([[2, 0, 0], [3, 0, 0]])), ('grid8', c.project([[3, 0, 0], [3, 1, 0]])), ('grid9', c.project([[3, 1, 0], [2, 1, 0]])), ('grid10', c.project([[3, 1, 0], [3, 2, 0]])), ('grid11', c.project([[3, 2, 0], [2, 2, 0]])), ('grid12', c.project([[2, 2, 0], [2, 1, 0]])), ('grid13', c.project([[3, 1, 0], [4, 1, 0]])), ('grid14', c.project([[4, 1, 0], [4, 2, 0]])), ('grid15', c.project([[4, 2, 0], [3, 2, 0]])), ('grid16', c.project([[4, 2, 0], [4, 3, 0]])), ('grid17', c.project([[4, 3, 0], [3, 3, 0]])), ('grid18', c.project([[3, 3, 0], [3, 2, 0]])), ('grid19', c.project([[4, 2, 0], [5, 2, 0]])), ('grid20', c.project([[5, 2, 0], [5, 3, 0]])), ('grid21', c.project([[5, 3, 0], [4, 3, 0]]))]:
                c.line(points, id=object_id, clip_on=False, zorder=3)
            for object_id, text, anchor in [('position1', '1', c.project([0.5, 0.5, 0])), ('position2', '2', c.project([1.5, 0.5, 0])), ('position3', '3', c.project([2.5, 0.5, 0])), ('position4', '4', c.project([2.5, 1.5, 0])), ('position5', '5', c.project([3.5, 1.5, 0])), ('position6', '6', c.project([3.5, 2.5, 0])), ('position7', '7', c.project([4.5, 2.5, 0]))]:
                c.text(text, anchor, id=object_id, offset_pt=[0, 0], vertex=False)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Solid175().draw(sys.argv[1] if len(sys.argv) > 1 else None))
