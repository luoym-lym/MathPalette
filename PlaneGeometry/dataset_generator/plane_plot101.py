"""Frozen question Plane101; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane101:

    def __init__(self):
        self.id = 'Plane101'
        self.source_dataset = 'Author Designed'
        self.source_key = 'shortest-path:offset'
        self.question = 'Find the length of the shortest path from A to B that stays outside the interior of the disk.'
        self.answer = 'sqrt(3) + 2 + pi/6'
        self.answer_type = 'number'
        self.query = self.question
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane101.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-2.31002994234985, 2.323436964650199], ylim=[-1.9403879098452548, 2.693078997154794], axes_position=[0.05, 0.05, 0.9, 0.9], coordinate_axes=False) as c:
            c.circle([0.0, 0.0], 1.0, id='O_circle', facecolor=[0.0, 0.0, 0.0, 0], fill=False)
            for object_id, points in [('O_radius', [[0.0, 0.0], [-0.7071067811865475, 0.7071067811865476]]), ('baseline', [[-2.0, 0.0], [2.0, 0.0]]), ('height', [[2.0, 0.0], [2.0, 1.0]])]:
                c.line(points, id=object_id)
            for object_id, points in [('A_dot', [[-2.0, 0.0]]), ('O_dot', [[0.0, 0.0]]), ('B_dot', [[2.0, 1.0]]), ('H_dot', [[2.0, 0.0]])]:
                c.point(points, id=object_id)
            c.line([[-2.0, 1.6], [0.0, 1.6]], id='AO_dash', linestyle=(0, [4, 3]))
            c.line([[-2.0, 0.0], [-2.0, 1.6]], id='AO_connector0')
            c.line([[0.0, 0.0], [0.0, 1.6]], id='AO_connector1')
            c.line([[0.0, 1.6], [2.0, 1.6]], id='OH_dash', linestyle=(0, [4, 3]))
            c.line([[0.0, 0.0], [0.0, 1.6]], id='OH_connector0')
            c.line([[2.0, 0.0], [2.0, 1.6]], id='OH_connector1')
            c.line([[1.916206110622829, 0.0], [1.916206110622829, 0.083793889377171]], id='right_angle_H', zorder=3)
            c.line([[1.916206110622829, 0.083793889377171], [2.0, 0.083793889377171]], id='right_angle_H', zorder=3)
            c.text('1', [-0.35355339059327373, 0.3535533905932738], id='O_radius_value', rotation_mode='default', offset_pt=[-7.0710678118654755, -7.071067811865475], annotation_clip=None)
            c.text('A', [-2.0, 0.0], id='A_label', fontsize=18.0, fontstyle='italic', ha='right', rotation_mode='default', offset_pt=[-10, 0], annotation_clip=None)
            c.text('O', [0.0, 0.0], id='O_label', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[0, -14], annotation_clip=None)
            c.text('B', [2.0, 1.0], id='B_label', fontsize=18.0, fontstyle='italic', ha='left', rotation_mode='default', offset_pt=[10, 0], annotation_clip=None)
            c.text('H', [2.0, 0.0], id='H_label', fontsize=18.0, fontstyle='italic', ha='left', rotation_mode='default', offset_pt=[10, -10], annotation_clip=None)
            c.text('2', [-1.0, 1.6], id='AO_value', rotation_mode='default', offset_pt=[0.0, 12.0], annotation_clip=None)
            c.text('2', [1.0, 1.6], id='OH_value', rotation_mode='default', offset_pt=[0.0, 12.0], annotation_clip=None)
            c.text('1', [2.0, 0.5], id='height_value', rotation_mode='default', offset_pt=[12, 0], annotation_clip=None)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane101().draw(sys.argv[1] if len(sys.argv) > 1 else None))
