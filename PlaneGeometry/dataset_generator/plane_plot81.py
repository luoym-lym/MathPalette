"""Frozen question Plane81; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane81:

    def __init__(self):
        self.id = 'Plane81'
        self.source_dataset = 'MathVerse'
        self.source_key = 'testmini:64'
        self.question = 'As shown in the figure, AB parallel EF, then angle ACD = ()\nChoices:\nA:120°\nB:130°\nC:140°\nD:150°'
        self.answer = 'C'
        self.answer_type = 'choice'
        self.choices = {'A': '120°', 'B': '130°', 'C': '140°', 'D': '150°'}
        self.query = self.question
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane81.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-3.4225196692949775, 3.392692278581625], ylim=[-3.4656797320196473, 3.3495322158569554], axes_position=[0.05, 0.05, 0.9, 0.9], coordinate_axes=False) as c:
            for object_id, points in [('segment_0', [[-3.0, 3.0], [3.0, 3.0]]), ('segment_1', [[-3.0, 3.0], [0.0, -0.57526077778263]]), ('segment_2', [[0.0, -0.57526077778263], [0.0, -3.0]]), ('segment_3', [[-3.0, -3.0], [3.0, -3.0]])]:
                c.line(points, id=object_id)
            c.line([[0.0, -2.87675036263244], [0.12324963736756009, -2.87675036263244]], id='right_angle_4', zorder=3)
            c.line([[0.12324963736756009, -2.87675036263244], [0.12324963736756009, -3.0]], id='right_angle_4', zorder=3)
            c.path([[-2.8327507270926326, 2.800680078153875], [-2.803646325341679, 2.8251015709287355], [-2.780241019805241, 2.855603958962922], [-2.7641844426869335, 2.890037399712828], [-2.748127865568626, 2.9244708404627344], [-2.739806321112929, 2.96200690180265], [-2.739806321112929, 3.0]], [1, 4, 4, 4, 4, 4, 4], id='angle_arc_5', zorder=3, facecolor=[0.0, 0.0, 0.0, 0], capstyle='butt', fill=False)
            c.text('A', [-3.0, 3.0], id='label_0', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[-12, 5], annotation_clip=None)
            c.text('B', [3.0, 3.0], id='label_1', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[12, 0], annotation_clip=None)
            c.text('C', [0.0, -0.57526077778263], id='label_2', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[4.658742811845373, 17.38666487320323], annotation_clip=None)
            c.text('D', [0.0, -3.0], id='label_3', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[0, -17], annotation_clip=None)
            c.text('E', [-3.0, -3.0], id='label_4', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[-12, 0], annotation_clip=None)
            c.text('F', [3.0, -3.0], id='label_5', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[12, 0], annotation_clip=None)
            c.text('50°', [-3.0, 3.0], id='label_6', rotation_mode='default', offset_pt=[45.31538935183249, -21.130913087034976], annotation_clip=None)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane81().draw(sys.argv[1] if len(sys.argv) > 1 else None))
