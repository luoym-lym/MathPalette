"""Frozen question Plane100; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane100:

    def __init__(self):
        self.id = 'Plane100'
        self.source_dataset = 'Author Designed'
        self.source_key = 'shortest-path:equal'
        self.question = 'Find the length of the shortest path from A to B that stays outside the interiors of both disks.'
        self.answer = '2*sqrt(3) + 2 + pi/3'
        self.answer_type = 'number'
        self.query = self.question
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane100.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-3.465, 3.465], ylim=[-3.155, 3.775], axes_position=[0.05, 0.05, 0.9, 0.9], coordinate_axes=False) as c:
            c.circle([-1.0, 0.0], 1.0, id='left_circle', facecolor=[0.0, 0.0, 0.0, 0], fill=False)
            c.circle([1.0, 0.0], 1.0, id='right_circle', facecolor=[0.0, 0.0, 0.0, 0], fill=False)
            c.line([[-3.0, 0.0], [3.0, 0.0]], id='AB_baseline')
            for object_id, points in [('L_dot', [[-1.0, 0.0]]), ('R_dot', [[1.0, 0.0]]), ('A_dot', [[-3.0, 0.0]]), ('B_dot', [[3.0, 0.0]])]:
                c.point(points, id=object_id)
            c.line([[-1.0, 0.0], [-0.5, 0.8660254037844386]], id='L_radius')
            c.line([[1.0, 0.0], [0.5, 0.8660254037844386]], id='R_radius')
            c.line([[-3.0, 1.35], [-1.0, 1.35]], id='AL_dimension_line', linestyle=(0, [4, 3]))
            c.line([[-3.0, 0.0], [-3.0, 1.35]], id='AL_connector_0')
            c.line([[-1.0, 0.0], [-1.0, 1.35]], id='AL_connector_1')
            c.line([[3.0, 1.35], [1.0, 1.35]], id='BR_dimension_line', linestyle=(0, [4, 3]))
            c.line([[3.0, 0.0], [3.0, 1.35]], id='BR_connector_0')
            c.line([[1.0, 0.0], [1.0, 1.35]], id='BR_connector_1')
            c.text('A', [-3.0, 0.0], id='A_label', fontsize=18.0, fontstyle='italic', ha='right', rotation_mode='default', offset_pt=[-10, 0], annotation_clip=None)
            c.text('B', [3.0, 0.0], id='B_label', fontsize=18.0, fontstyle='italic', ha='left', rotation_mode='default', offset_pt=[10, 0], annotation_clip=None)
            c.text('L', [-1.0, 0.0], id='L_label', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[0, -14], annotation_clip=None)
            c.text('R', [1.0, 0.0], id='R_label', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[0, -14], annotation_clip=None)
            c.text('1', [-0.75, 0.4330127018922193], id='L_radius_value', rotation_mode='default', offset_pt=[10, 0], annotation_clip=None)
            c.text('1', [0.75, 0.4330127018922193], id='R_radius_value', rotation_mode='default', offset_pt=[-10, 0], annotation_clip=None)
            c.text('2', [-2.0, 1.35], id='AL_value', rotation_mode='default', offset_pt=[0, 12], annotation_clip=None)
            c.text('2', [2.0, 1.35], id='BR_value', rotation_mode='default', offset_pt=[0, 12], annotation_clip=None)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane100().draw(sys.argv[1] if len(sys.argv) > 1 else None))
