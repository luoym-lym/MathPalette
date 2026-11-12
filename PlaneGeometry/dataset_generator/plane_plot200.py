"""Frozen question Plane200; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane200:

    def __init__(self):
        self.id = 'Plane200'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:469'
        self.question = 'Six coins are arranged in a triangle, as shown. What is the smallest number of coins that must be moved to form the circle shown?'
        self.answer = '2'
        self.answer_type = 'number'
        self.query = self.question
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane200.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-1.4878458591050734, 18.994709910248375], ylim=[-8.505176642386582, 11.977379126966868]) as c:
            for object_id, center, radius in [('tri0', [0.0, 0.0], 1), ('tri1', [2.0, 0.0], 1), ('tri2', [4.0, 0.0], 1), ('tri3', [1.0, 1.7320508075688772], 1), ('tri4', [3.0, 1.7320508075688772], 1), ('tri5', [2.0, 3.4641016151377544], 1), ('hex0', [17.5, 1.7320508075688772], 1), ('hex1', [16.5, 3.4641016151377544], 1), ('hex2', [14.5, 3.4641016151377544], 1), ('hex3', [13.5, 1.7320508075688774], 1), ('hex4', [14.5, 4.440892098500626e-16], 1), ('hex5', [16.5, 0.0], 1)]:
                c.circle(center, radius, id=object_id)
            c.path([[6.5, 1.2320508075688772], [10.5, 1.2320508075688772], [10.5, 0.7320508075688772], [11.5, 1.7320508075688772], [10.5, 2.732050807568877], [10.5, 2.232050807568877], [6.5, 2.232050807568877], [6.5, 1.2320508075688772]], [1, 2, 2, 2, 2, 2, 2, 79], id='transformation_arrow')
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane200().draw(sys.argv[1] if len(sys.argv) > 1 else None))
