"""Frozen question Plane37; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane37:

    def __init__(self):
        self.id = 'Plane37'
        self.source_dataset = 'MathVista'
        self.source_key = 'testmini/310'
        self.question = 'Find z\nChoices:\nA: 10\nB: \\frac { 32 } { 3 }\nC: \\frac { 40 } { 3 }\nD: \\frac { 50 } { 3 }'
        self.answer = 'C'
        self.answer_type = 'choice'
        self.choices = {'A': '10', 'B': '\\frac { 32 } { 3 }', 'C': '\\frac { 40 } { 3 }', 'D': '\\frac { 50 } { 3 }'}
        self.query = self.question
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane37.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-0.37184478419682865, 15.295488475429245], ylim=[-2.051989667603734, 13.615343592022338], axes_position=[0.05, 0.05, 0.9, 0.9], coordinate_axes=False) as c:
            c.path([[0.0, 10.0], [0.0, 0.0], [13.333333333333334, 0.0], [0.0, 10.0]], [1, 2, 2, 79], id='o1', facecolor=[0.0, 0.0, 0.0, 0.0], capstyle='butt')
            c.line([[0.0, 0.0], [4.8, 6.4]], id='o2')
            for object_id, points in [('o3', [[0.0, 0.2833357432658072], [0.2833357432658072, 0.2833357432658072]]), ('o3', [[0.2833357432658072, 0.2833357432658072], [0.2833357432658072, 0.0]]), ('o5', [[4.573331405387354, 6.570001445959485], [4.40332995942787, 6.343332851346839]]), ('o5', [[4.40332995942787, 6.343332851346839], [4.629998554040515, 6.173331405387355]])]:
                c.line(points, id=object_id, zorder=3)
            c.line([[1.6, 12.133333333333333], [14.933333333333334, 2.1333333333333333]], id='o17', linestyle=(0, [4, 3]))
            c.line([[0.0, 10.0], [1.6, 12.133333333333333]], id='o18')
            c.line([[13.333333333333334, 0.0], [14.933333333333334, 2.1333333333333333]], id='o19')
            c.text('y', [0.0, 5.0], id='t8', rotation_mode='default', offset_pt=[14, 0], annotation_clip=None)
            c.text('z', [6.666666666666667, 0.0], id='t10', rotation_mode='default', offset_pt=[0, -15], annotation_clip=None)
            c.text('6', [2.4, 8.2], id='t12', rotation_mode='default', offset_pt=[0, 13], annotation_clip=None)
            c.text('8', [2.4, 3.2], id='t14', rotation_mode='default', offset_pt=[13, 0], annotation_clip=None)
            c.text('x', [8.266666666666667, 7.133333333333333], id='t21', rotation_mode='default', offset_pt=[8, 10], annotation_clip=None)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane37().draw(sys.argv[1] if len(sys.argv) > 1 else None))
