"""Frozen question Plane335; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane335:

    def __init__(self):
        self.id = 'Plane335'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:1084'
        self.question = 'One vertex of the triangle on the left is connected to one vertex of the triangle on the right using a straight line so that no connecting line segment dissects either of the two triangles into two parts. In how many ways is this possible?'
        self.answer = '4'
        self.answer_type = 'number'
        self.query = self.question
        self.points = {'0L': [0, 0], '0U': [2, 1], '0D': [2, -1], '1L': [2.3, 0], '1U': [4.3, 1], '1D': [4.3, -1]}
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane335.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-0.1057762150301218, 4.406403185378116], ylim=[-2.2560897002041185, 2.2560897002041185]) as c:
            c.path([self.points['0L'], self.points['0U'], self.points['0D'], self.points['0L']], [1, 2, 2, 79], id='triangle0')
            c.path([self.points['1L'], self.points['1U'], self.points['1D'], self.points['1L']], [1, 2, 2, 79], id='triangle1')
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane335().draw(sys.argv[1] if len(sys.argv) > 1 else None))
