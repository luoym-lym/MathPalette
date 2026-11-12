"""Frozen question Plane230; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane230:

    def __init__(self):
        self.id = 'Plane230'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:618'
        self.question = 'The star shown is formed by placing triangles on top of one another. What is the minimum number of triangles required?'
        self.answer = '3'
        self.answer_type = 'number'
        self.query = self.question
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane230.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=(-3.1498780943562075, 3.1498780943562075), ylim=(-3.202997204065766, 3.096758984646649), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
            c.path([[-0.8, 2.2], [-1.1733333333333333, 1.0], [-3.0, 1.0], [-1.4503008423586041, 0.10974729241877257], [-2.2, -2.3], [0.14923857868020304, -0.8091370558375635], [1.7, -1.7], [0.8456361724500526, -0.36719242902208205], [3.0, 1.0], [-0.03076923076923077, 1.0], [-0.8, 2.2]], [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 79], id='irregular_pentagram', alpha=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[-0.8, 2.2], [-1.1733333333333333, 1.0], [-3.0, 1.0], [-1.4503008423586041, 0.10974729241877257], [-2.2, -2.3], [0.14923857868020304, -0.8091370558375635], [1.7, -1.7], [0.8456361724500526, -0.36719242902208205], [3.0, 1.0], [-0.03076923076923077, 1.0], [-0.8, 2.2]], [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 79], id='irregular_pentagram', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane230().draw(sys.argv[1] if len(sys.argv) > 1 else None))
