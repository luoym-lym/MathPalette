"""Frozen question Plane324; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane324:

    def __init__(self):
        self.id = 'Plane324'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:1028'
        self.question = 'What is the smallest number of dots that need be removed from the pattern shown, so that no three of the remaining dots are at the vertices of an equilateral triangle?'
        self.answer = '4'
        self.answer_type = 'number'
        self.query = self.question
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane324.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-0.16814956219310906, 3.172145258471985], ylim=[-0.3707154221712696, 2.9695793984938246], axes_position=[0.05, 0.05, 0.9, 0.9], coordinate_axes=False) as c:
            for object_id, center, radius in [('dot0', [0.0, 0.0], 0.09), ('dot1', [1.0, 0.0], 0.09), ('dot2', [2.0, 0.0], 0.09), ('dot3', [3.0, 0.0], 0.09), ('dot4', [0.5, 0.8660254037844386], 0.09), ('dot5', [1.5, 0.8660254037844386], 0.09), ('dot6', [2.5, 0.8660254037844386], 0.09), ('dot7', [1.0, 1.7320508075688772], 0.09), ('dot8', [2.0, 1.7320508075688772], 0.09), ('dot9', [1.5, 2.598076211353316], 0.09)]:
                c.circle(center, radius, id=object_id, facecolor=[0.0, 0.0, 0.0, 1.0])
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane324().draw(sys.argv[1] if len(sys.argv) > 1 else None))
