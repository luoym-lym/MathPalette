"""Frozen question Plane58; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane58:

    def __init__(self):
        self.id = 'Plane58'
        self.source_dataset = 'MathVista'
        self.source_key = 'testmini/747'
        self.question = 'In $\\odot M$, $FL=24,HJ=48$, and $m \\widehat {HP}=65$. Find $m \\widehat {HJ}$.\nChoices:\nA: 65\nB: 120\nC: 130\nD: 155'
        self.answer = 'C'
        self.answer_type = 'choice'
        self.choices = {'A': '65', 'B': '120', 'C': '130', 'D': '155'}
        self.query = self.question
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane58.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-30.420362496381877, 28.058913986349445], ylim=[-28.445929368874925, 30.033347113856397], axes_position=[0.05, 0.05, 0.9, 0.9], coordinate_axes=False) as c:
            c.point([[0.0, 0.0]], id='point2')
            c.circle([0.0, 0.0], 26.481070055099803, id='circle11', facecolor=[0.0, 0.0, 0.0, 0], fill=False)
            for object_id, points in [('segment18', [[-25.578749473990978, 6.853805264953895], [21.69202267059501, 15.188917792966544]]), ('segment19', [[-26.38030158868651, -2.3079773294049932], [18.724944209037094, -18.72494420903709]]), ('segment20', [[0.0, 0.0], [-4.598389557738399, 26.078763098321705]]), ('segment21', [[0.0, 0.0], [-9.057059375662309, -24.884066121291973]])]:
                c.line(points, id=object_id)
            for object_id, points in [('right_angle22', [[-2.127008146209461, 12.062862629776523], [-1.0855070453931581, 12.246507374288004]]), ('right_angle22', [[-1.0855070453931581, 12.246507374288004], [-0.9018623008816766, 11.205006273471701]]), ('right_angle24', [[-4.189388226214414, -11.510249552853159], [-3.1955994425822976, -11.871959089242864]]), ('right_angle24', [[-3.1955994425822976, -11.871959089242864], [-2.8338899061925913, -10.878170305610748]])]:
                c.line(points, id=object_id, zorder=3)
            c.text('M', [0.0, 0.0], id='label1', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[15, 0], annotation_clip=None)
            c.text('P', [-9.057059375662309, -24.884066121291973], id='label3', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[-5.130302149885031, -14.095389311788626], annotation_clip=None)
            c.text('H', [-26.38030158868651, -2.3079773294049932], id='label4', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[-14.942920471376183, -1.307336141214873], annotation_clip=None)
            c.text('J', [18.724944209037094, -18.72494420903709], id='label5', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[10.606601717798213, -10.606601717798211], annotation_clip=None)
            c.text('K', [-4.598389557738399, 26.078763098321705], id='label6', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[-2.6047226650039548, 14.772116295183121], annotation_clip=None)
            c.text('F', [-25.578749473990978, 6.853805264953895], id='label7', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[-14.488887394336023, 3.882285676537815], annotation_clip=None)
            c.text('G', [21.69202267059501, 15.188917792966544], id='label8', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[12.287280664334878, 8.60364654526569], annotation_clip=None)
            c.text('N', [-3.827678689824708, -10.516460769221043], id='label9', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[13.85640646055102, 7.999999999999999], annotation_clip=None)
            c.text('L', [-1.9433634016979795, 11.02136152896022], id='label10', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[-15, 10], annotation_clip=None)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane58().draw(sys.argv[1] if len(sys.argv) > 1 else None))
