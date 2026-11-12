"""Frozen question Plane486; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane486:

    def __init__(self):
        self.id = 'Plane486'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:2859'
        self.question = 'How many lines pass through exactly two points in the following hexagonal grid?'
        self.answer = '60'
        self.answer_type = 'number'
        self.query = self.question
        self.points = {'0': [-2.0, 0.0],
         '1': [-1.5, 0.8660254037844386],
         '2': [-1.0, 1.7320508075688772],
         '3': [-1.5, -0.8660254037844386],
         '4': [-1.0, 0.0],
         '5': [-0.5, 0.8660254037844386],
         '6': [0.0, 1.7320508075688772],
         '7': [-1.0, -1.7320508075688772],
         '8': [-0.5, -0.8660254037844386],
         '9': [0.0, 0.0],
         '10': [0.5, 0.8660254037844386],
         '11': [1.0, 1.7320508075688772],
         '12': [0.0, -1.7320508075688772],
         '13': [0.5, -0.8660254037844386],
         '14': [1.0, 0.0],
         '15': [1.5, 0.8660254037844386],
         '16': [1.0, -1.7320508075688772],
         '17': [1.5, -0.8660254037844386],
         '18': [2.0, 0.0]}
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane486.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-2.1269174566656734, 2.1335822391929367], ylim=[-2.1335751546987463, 2.126924541159864]) as c:
            for object_id, points in [('d0', [self.points['0']]), ('d1', [self.points['1']]), ('d2', [self.points['2']]), ('d3', [self.points['3']]), ('d4', [self.points['4']]), ('d5', [self.points['5']]), ('d6', [self.points['6']]), ('d7', [self.points['7']]), ('d8', [self.points['8']]), ('d9', [self.points['9']]), ('d10', [self.points['10']]), ('d11', [self.points['11']]), ('d12', [self.points['12']]), ('d13', [self.points['13']]), ('d14', [self.points['14']]), ('d15', [self.points['15']]), ('d16', [self.points['16']]), ('d17', [self.points['17']]), ('d18', [self.points['18']])]:
                c.point(points, id=object_id, filled=True)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane486().draw(sys.argv[1] if len(sys.argv) > 1 else None))
