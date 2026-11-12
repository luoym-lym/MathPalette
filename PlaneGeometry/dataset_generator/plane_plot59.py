"""Frozen question Plane59; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane59:

    def __init__(self):
        self.id = 'Plane59'
        self.source_dataset = 'MathVista'
        self.source_key = 'testmini/733'
        self.question = 'Square ABCD. CT: tangent to semicircle. Find the angle ∠CTD. Return the numeric value.'
        self.answer = '63.4'
        self.answer_type = 'number'
        self.query = self.question
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane59.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-0.29461314294746854, 4.296651399627228], ylim=[-0.2831803897012293, 4.308084152873468], axes_position=[0.05, 0.05, 0.9, 0.9], coordinate_axes=False) as c:
            for object_id, points in [('point2', [[0.0, 0.0]]), ('point4', [[0.0, 4.0]]), ('point6', [[4.0, 4.0]]), ('point8', [[4.0, 0.0]]), ('point10', [[0.8, 1.6]])]:
                c.point(points, id=object_id)
            for object_id, points in [('segment11', [[0.0, 0.0], [0.0, 4.0]]), ('segment12', [[0.0, 4.0], [4.0, 4.0]]), ('segment13', [[4.0, 4.0], [4.0, 0.0]]), ('segment14', [[4.0, 0.0], [0.0, 0.0]])]:
                c.line(points, id=object_id)
            c.path([[4.0, 0.0], [4.0, 0.5302295469826049], [3.789142470629966, 1.0392846541162237], [3.414213562373095, 1.414213562373095], [3.039284654116224, 1.7891424706299661], [2.5302295469826053, 2.0], [2.0, 2.0], [1.4697704530173952, 2.0], [0.9607153458837763, 1.7891424706299661], [0.5857864376269051, 1.4142135623730951], [0.21085752937003388, 1.0392846541162242], [0.0, 0.5302295469826052], [0.0, 2.4492935982947064e-16]], [1, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4], id='arc15', facecolor=[0.0, 0.0, 0.0, 0], capstyle='butt', fill=False)
            c.line([[0.8, 1.6], [4.0, 4.0]], id='segment16')
            c.line([[0.8, 1.6], [4.0, 0.0]], id='segment17')
            c.text('A', [0.0, 0.0], id='label1', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[-14, -14], annotation_clip=None)
            c.text('B', [0.0, 4.0], id='label3', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[-14, 14], annotation_clip=None)
            c.text('C', [4.0, 4.0], id='label5', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[14, 14], annotation_clip=None)
            c.text('D', [4.0, 0.0], id='label7', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[14, -14], annotation_clip=None)
            c.text('T', [0.8, 1.6], id='label9', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[-14, 12], annotation_clip=None)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane59().draw(sys.argv[1] if len(sys.argv) > 1 else None))
