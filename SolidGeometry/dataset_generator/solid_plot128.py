"""Frozen question Solid128; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Solid128:

    def __init__(self):
        self.id = 'Solid128'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:798'
        self.question = 'A wall around a square area is made from 36 identical cubes. A section of the wall is shown. How many cubes are needed to completely fill the square area?'
        self.answer = '64'
        self.answer_type = 'number'
        self.query = self.question
        self.subject = 'SolidGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'SolidGeometry' / 'dataset_generator/scenes/Solid128.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('SolidGeometry', self.id, variant, output_path)
        with Canvas(SOLID, xlim=[-0.12709958463601412, 5.127099584636014], ylim=[-2.4157280568582364, 2.838471112413792], projection=[[1, 0.9, 0], [-0.28, 0.35, 1]], origin=[0, 0, 0], offset=[0, 0]) as c:
            for object_id, points in [('front_bottom', c.project([[0, 0, 0], [5, 0, 0]])), ('front_top', c.project([[0, 0, 1], [5, 0, 1]])), ('front_vertical0', c.project([[0, 0, 0], [0, 0, 1]])), ('front_vertical1', c.project([[1, 0, 0], [1, 0, 1]])), ('front_vertical2', c.project([[2, 0, 0], [2, 0, 1]])), ('front_vertical3', c.project([[3, 0, 0], [3, 0, 1]])), ('front_vertical4', c.project([[4, 0, 0], [4, 0, 1]])), ('return_outer_top', c.project([[0, 0, 1], [0, 2.35, 1]])), ('return_inner_top', c.project([[1, 0, 1], [1, 2.7, 1]])), ('front_depth_grid2', c.project([[2, 0, 1], [2, 1, 1]])), ('front_depth_grid3', c.project([[3, 0, 1], [3, 1, 1]])), ('front_depth_grid4', c.project([[4, 0, 1], [4, 1, 1]])), ('front_rear_top', c.project([[0, 1, 1], [4.1, 1, 1]])), ('return_top_grid2', c.project([[0, 2, 1], [1, 2, 1]])), ('inner_vertical2', c.project([[1, 2, 0.398], [1, 2, 1]])), ('inner_vertical3', c.project([[1, 3, 0], [1, 3, 1]])), ('inner_vertical4', c.project([[1, 4, 0], [1, 4, 0.12]])), ('inner_bottom', c.project([[1, 2.661129568106312, 0], [1, 4.2, 0]]))]:
                c.line(points, id=object_id, clip_on=False, zorder=3)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Solid128().draw(sys.argv[1] if len(sys.argv) > 1 else None))
