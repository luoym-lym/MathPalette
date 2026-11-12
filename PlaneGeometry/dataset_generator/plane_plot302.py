"""Frozen question Plane302; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane302:

    def __init__(self):
        self.id = 'Plane302'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:932'
        self.question = 'A panel consists of 4 circles. Touching a circle changes its color and the color of every circle touching it, from white to black or from black to white, as shown. Starting with all circles white, what is the minimum number of successive touches needed to turn all circles black?'
        self.answer = '4'
        self.answer_type = 'number'
        self.query = self.question
        self._geometry_01 = [[-1.65, 1.75],
         [-1.85, 1.95],
         [-1.65, 2.15],
         [-1.5, 2.15],
         [-1.5, 2.3],
         [-1.25, 2.3],
         [-1.2, 2.23],
         [-0.85, 2.32],
         [-0.4, 2.12],
         [-0.42, 1.95],
         [-0.4, 1.84],
         [-0.55, 1.83],
         [-0.58, 1.9],
         [-0.38, 1.72],
         [-0.42, 1.63],
         [-0.52, 1.62],
         [-0.2, 1.4],
         [0.02, 1.25],
         [-0.08, 1.15],
         [-0.23, 1.02],
         [-0.53, 1.28],
         [-0.83, 1.4],
         [-1.04, 1.55],
         [-1.2, 1.57],
         [-1.23, 1.58],
         [-1.23, 1.38],
         [-1.37, 1.22],
         [-1.62, 1.26],
         [-1.87, 1.25],
         [-1.58, 1.58],
         [-1.65, 1.75],
         [-1.65, 1.75]]
        self._geometry_02 = [1, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 79]
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane302.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-1.9162533209526806, 5.6787443204332755], ylim=[-2.91124989428306, 4.683747747102896], axes_position=[0.05, 0.05, 0.9, 0.9], coordinate_axes=False) as c:
            c.circle([0.0, 1.0], 0.5, id='circle0_0', facecolor=[0.0, 0.0, 0.0, 1.0])
            for object_id, center, radius in [('circle0_1', [1.0, 1.0], 0.5), ('circle0_2', [0.0, 0.0], 0.5), ('circle0_3', [1.0, 0.0], 0.5), ('circle1_0', [4.0, 1.0], 0.5)]:
                c.circle(center, radius, id=object_id, facecolor=[1.0, 1.0, 1.0, 1.0])
            c.circle([5.0, 1.0], 0.5, id='circle1_1', facecolor=[0.0, 0.0, 0.0, 1.0])
            c.circle([4.0, 0.0], 0.5, id='circle1_2', facecolor=[0.0, 0.0, 0.0, 1.0])
            c.circle([5.0, 0.0], 0.5, id='circle1_3', facecolor=[1.0, 1.0, 1.0, 1.0])
            c.path([[2.2, 0.35], [2.65, 0.35], [2.65, 0.2], [3.1, 0.5], [2.65, 0.8], [2.65, 0.65], [2.2, 0.65], [2.2, 0.35]], [1, 2, 2, 2, 2, 2, 2, 79], id='transition_arrow', facecolor=[0.0, 0.0, 0.0, 0.0], capstyle='butt')
            c.path(self._geometry_01, self._geometry_02, id='touching_hand', facecolor=[1.0, 1.0, 1.0, 1.0], capstyle='butt')
            c.line([[-0.83, 1.7], [-0.52, 1.43]], id='finger_crease')
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane302().draw(sys.argv[1] if len(sys.argv) > 1 else None))
