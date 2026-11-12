"""Frozen question Plane189; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane189:

    def __init__(self):
        self.id = 'Plane189'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:406'
        self.question = "Which numbers are written in the area that belongs to the rectangle and to the circle but doesn't belong to the triangle?\nChoices:\nA:5 and 11\nB:1 and 10\nC:13\nD:3 and 9\nE:6, 7, and 4"
        self.answer = 'B'
        self.answer_type = 'choice'
        self.choices = {'A': '5 and 11', 'B': '1 and 10', 'C': '13', 'D': '3 and 9', 'E': '6, 7, and 4'}
        self.query = self.question
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane189.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-0.21014089856961427, 8.616984881607177], ylim=[-0.8883804470166909, 7.9387453331601]) as c:
            c.path([[0, 2.2], [8.4, 2.2], [8.4, 4.4], [0, 4.4], [0, 2.2]], [1, 2, 2, 2, 79], id='rectangle')
            c.path([[0.3, 1.2], [6.15, 0], [6.15, 7.05], [0.3, 1.2]], [1, 2, 2, 79], id='triangle')
            c.circle([4.65, 3.15], 2.6, id='circle')
            for object_id, text, anchor in [('label0', '1', [2.65, 4]), ('label1', '2', [1.2, 3.3]), ('label2', '3', [1.9, 2.45]), ('label3', '4', [4.5, 1.4]), ('label4', '5', [1.8, 1.55]), ('label5', '6', [3.4, 4.9]), ('label6', '7', [5.1, 5]), ('label7', '8', [5.8, 6.2]), ('label8', '9', [6.4, 4.85]), ('label9', '10', [6.65, 3.3]), ('label10', '11', [7.8, 3.3]), ('label11', '12', [6.5, 1.8]), ('label12', '13', [4.3, 3.3])]:
                c.text(text, anchor, id=object_id, offset_pt=[0, 0], vertex=False)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane189().draw(sys.argv[1] if len(sys.argv) > 1 else None))
