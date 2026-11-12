"""Frozen question Plane61; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane61:

    def __init__(self):
        self.id = 'Plane61'
        self.source_dataset = 'MathVista'
        self.source_key = 'testmini/786'
        self.question = 'Find $m \\angle K$\nChoices:\nA: 6\nB: 60\nC: 100\nD: 180'
        self.answer = 'C'
        self.answer_type = 'choice'
        self.choices = {'A': '6', 'B': '60', 'C': '100', 'D': '180'}
        self.query = self.question
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane61.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-0.9026580034816121, 12.829063799266496], ylim=[-3.790968438122314, 9.940753364625795], axes_position=[0.05, 0.05, 0.9, 0.9], coordinate_axes=False) as c:
            for object_id, points in [('segment5', [[0.0, 0.0], [12.0, 0.0]]), ('segment6', [[12.0, 0.0], [10.958110933998418, 5.908846518073248]]), ('segment7', [[10.958110933998418, 5.908846518073248], [1.0418890660015825, 5.908846518073248]]), ('segment8', [[1.0418890660015825, 5.908846518073248], [0.0, 0.0]])]:
                c.line(points, id=object_id)
            c.path([[0.44147768141551275, 0.0], [0.44147768141551275, 0.1037678798869404], [0.4048922320841704, 0.20428557580540468], [0.33819152460940405, 0.28377638356703294], [0.2714908171346377, 0.3632671913286612], [0.17885320748472394, 0.4167515401971224], [0.07666179485842546, 0.43477064343985056]], [1, 4, 4, 4, 4, 4, 4], id='angle_arc9', zorder=3, facecolor=[0.0, 0.0, 0.0, 0], capstyle='butt', fill=False)
            for object_id, points in [('parallel_mark15', [[5.8620382245576526, 0.06898088772117386], [6.0, 0.0]]), ('parallel_mark15', [[5.8620382245576526, -0.06898088772117386], [6.0, 0.0]]), ('parallel_mark16', [[5.8620382245576526, 5.977827405794422], [6.0, 5.908846518073248]]), ('parallel_mark16', [[5.8620382245576526, 5.839865630352074], [6.0, 5.908846518073248]])]:
                c.line(points, id=object_id, zorder=3)
            c.text('M', [0.0, 0.0], id='label1', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[-14, -8], annotation_clip=None)
            c.text('L', [12.0, 0.0], id='label2', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[14, -8], annotation_clip=None)
            c.text('J', [1.0418890660015825, 5.908846518073248], id='label3', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[-8, 14], annotation_clip=None)
            c.text('K', [10.958110933998418, 5.908846518073248], id='label4', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[10, 14], annotation_clip=None)
            c.text('80°', [0.0, 0.0], id='anglelabel10', rotation_mode='default', offset_pt=[24.513422179807296, 20.569203509969256], annotation_clip=None)
            c.text('6', [0.5209445330007912, 2.954423259036624], id='text12', rotation_mode='default', offset_pt=[-15, 0], annotation_clip=None)
            c.text('6', [11.47905546699921, 2.954423259036624], id='text14', rotation_mode='default', offset_pt=[15, 0], annotation_clip=None)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane61().draw(sys.argv[1] if len(sys.argv) > 1 else None))
