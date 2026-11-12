"""Frozen question Plane63; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane63:

    def __init__(self):
        self.id = 'Plane63'
        self.source_dataset = 'MathVista'
        self.source_key = 'testmini/804'
        self.question = 'In $\\odot B$, $CE=13.5$. Find $BD$. Round to the nearest hundredth.\nChoices:\nA: 3.71\nB: 4.29\nC: 4.53\nD: 6.75'
        self.answer = 'B'
        self.answer_type = 'choice'
        self.choices = {'A': '3.71', 'B': '4.29', 'C': '4.53', 'D': '6.75'}
        self.query = self.question
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane63.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-9.21894937930976, 9.21894937930976], ylim=[-9.169981204648908, 9.267917553970614], axes_position=[0.05, 0.05, 0.9, 0.9], coordinate_axes=False) as c:
            c.point([[0.0, 0.0]], id='point2')
            c.circle([0.0, 0.0], 8.0, id='circle8', facecolor=[0.0, 0.0, 0.0, 0], fill=False)
            c.line([[0.0, 8.0], [0.0, -8.0]], id='segment13')
            c.line([[-6.75, -4.293891009329417], [6.75, -4.293891009329417]], id='segment14')
            c.line([[-0.3334400093789699, -4.293891009329417], [-0.3334400093789699, -3.9604509999504467]], id='right_angle15', zorder=3)
            c.line([[-0.3334400093789699, -3.9604509999504467], [0.0, -3.9604509999504467]], id='right_angle15', zorder=3)
            c.text('B', [0.0, 0.0], id='label1', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[14, 0], annotation_clip=None)
            c.text('A', [0.0, 8.0], id='label3', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[0, 15], annotation_clip=None)
            c.text('F', [0.0, -8.0], id='label4', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[0, -15], annotation_clip=None)
            c.text('C', [-6.75, -4.293891009329417], id='label5', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[-15, 1], annotation_clip=None)
            c.text('E', [6.75, -4.293891009329417], id='label6', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[15, 1], annotation_clip=None)
            c.text('D', [0.0, -4.293891009329417], id='label7', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[14, -13], annotation_clip=None)
            c.text('8', [0.0, 4.0], id='text18', rotation_mode='default', offset_pt=[14, 0], annotation_clip=None)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane63().draw(sys.argv[1] if len(sys.argv) > 1 else None))
