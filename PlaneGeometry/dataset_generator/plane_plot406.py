"""Frozen question Plane406; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane406:

    def __init__(self):
        self.id = 'Plane406'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:1729'
        self.question = 'A piece of paper in the shape of a regular hexagon, as shown, is folded so that the three marked vertices meet at the centre $O$ of the hexagon. What is the shape of the figure that is formed?\nChoices:\nA:Six-pointed star\nB:Dodecagon\nC:Hexagon\nD:Square\nE:Equilateral Triangle'
        self.answer = 'E'
        self.answer_type = 'choice'
        self.choices = {'A': 'Six-pointed star', 'B': 'Dodecagon', 'C': 'Hexagon', 'D': 'Square', 'E': 'Equilateral Triangle'}
        self.query = self.question
        self.points = {'O': [0, 0]}
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane406.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-1.0500052197346705, 1.0657457783579942], ylim=[-1.0597563788341569, 1.055994619258508]) as c:
            c.path([[1.0, 0.0], [0.5000000000000001, 0.8660254037844386], [-0.4999999999999998, 0.8660254037844387], [-1.0, 1.2246467991473532e-16], [-0.5000000000000004, -0.8660254037844384], [0.49999999999999933, -0.866025403784439], [1.0, 0.0]], [1, 2, 2, 2, 2, 2, 79], id='o0')
            for object_id, points in [('o1', [[1.0, 0.0]]), ('o2', [[-0.4999999999999998, 0.8660254037844387]]), ('o3', [[-0.5000000000000004, -0.8660254037844384]]), ('o4', [self.points['O']])]:
                c.point(points, id=object_id, filled=True)
            c.text('O', self.points['O'], offset_pt=[-17, -8], vertex=True, id='labelO')
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane406().draw(sys.argv[1] if len(sys.argv) > 1 else None))
