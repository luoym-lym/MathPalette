"""Frozen question Plane102; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane102:

    def __init__(self):
        self.id = 'Plane102'
        self.source_dataset = 'Author Designed'
        self.source_key = 'shortest-path:unequal'
        self.question = 'Find the length of the shortest path from A to B that stays outside the interiors of both disks.'
        self.answer = '3*sqrt(3) + 2*sqrt(2) + acos(-1/3)'
        self.answer_type = 'number'
        self.query = self.question
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane102.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-2.695237105442904, 7.695237105442904], ylim=[-4.77403346497611, 5.616440745909697], axes_position=[0.05, 0.05, 0.9, 0.9], coordinate_axes=False) as c:
            c.line([[-2.0, 0.0], [7.0, 0.0]], id='baseline')
            for object_id, points in [('A_dot', [[-2.0, 0.0]]), ('L_dot', [[0.0, 0.0]]), ('R_dot', [[3.0, 0.0]]), ('B_dot', [[7.0, 0.0]])]:
                c.point(points, id=object_id)
            c.circle([0.0, 0.0], 1.0, id='L_circle', facecolor=[0.0, 0.0, 0.0, 0], fill=False)
            c.line([[0.0, 0.0], [0.5000000000000001, 0.8660254037844386]], id='L_radius')
            c.circle([3.0, 0.0], 2.0, id='R_circle', facecolor=[0.0, 0.0, 0.0, 0], fill=False)
            c.line([[3.0, 0.0], [2.0000000000000004, 1.7320508075688774]], id='R_radius')
            c.line([[-2.0, 2.5], [0.0, 2.5]], id='AL_dash', linestyle=(0, [4, 3]))
            c.line([[-2.0, 0.0], [-2.0, 2.5]], id='AL_connector0')
            c.line([[0.0, 0.0], [0.0, 2.5]], id='AL_connector1')
            c.line([[0.0, 2.5], [3.0, 2.5]], id='LR_dash', linestyle=(0, [4, 3]))
            c.line([[0.0, 0.0], [0.0, 2.5]], id='LR_connector0')
            c.line([[3.0, 0.0], [3.0, 2.5]], id='LR_connector1')
            c.line([[3.0, 2.5], [7.0, 2.5]], id='RB_dash', linestyle=(0, [4, 3]))
            c.line([[3.0, 0.0], [3.0, 2.5]], id='RB_connector0')
            c.line([[7.0, 0.0], [7.0, 2.5]], id='RB_connector1')
            c.text('A', [-2.0, 0.0], id='A_label', fontsize=18.0, fontstyle='italic', ha='right', rotation_mode='default', offset_pt=[-10, 0], annotation_clip=None)
            c.text('L', [0.0, 0.0], id='L_label', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[0, -14], annotation_clip=None)
            c.text('R', [3.0, 0.0], id='R_label', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[0, -14], annotation_clip=None)
            c.text('B', [7.0, 0.0], id='B_label', fontsize=18.0, fontstyle='italic', ha='left', rotation_mode='default', offset_pt=[10, 0], annotation_clip=None)
            c.text('1', [0.25000000000000006, 0.4330127018922193], id='L_radius_value', rotation_mode='default', offset_pt=[8.660254037844386, -5.000000000000001], annotation_clip=None)
            c.text('2', [2.5, 0.8660254037844387], id='R_radius_value', rotation_mode='default', offset_pt=[-8.660254037844387, -4.999999999999998], annotation_clip=None)
            for object_id, text, anchor in [('AL_value', '2', [-1.0, 2.5]), ('LR_value', '3', [1.5, 2.5]), ('RB_value', '4', [5.0, 2.5])]:
                c.text(text, anchor, id=object_id, rotation_mode='default', offset_pt=[0.0, 12.0], annotation_clip=None)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane102().draw(sys.argv[1] if len(sys.argv) > 1 else None))
