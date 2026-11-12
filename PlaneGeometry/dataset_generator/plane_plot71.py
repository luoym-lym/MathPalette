"""Frozen question Plane71; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane71:

    def __init__(self):
        self.id = 'Plane71'
        self.source_dataset = 'MathVista'
        self.source_key = 'testmini/990'
        self.question = 'In $\\odot S$, $m \\widehat {PQR}=98$, Find $m \\widehat {PQ}$.\nChoices:\nA: 45\nB: 49\nC: 90\nD: 98'
        self.answer = 'B'
        self.answer_type = 'choice'
        self.choices = {'A': '45', 'B': '49', 'C': '90', 'D': '98'}
        self.query = self.question
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane71.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-8.755793227946146, 8.755793227946146], ylim=[-8.3641292557989, 9.147457200093392], axes_position=[0.05, 0.05, 0.9, 0.9], coordinate_axes=False) as c:
            c.point([[0.0, 0.0]], id='point2')
            c.circle([0.0, 0.0], 7.950077960092868, id='circle7', facecolor=[0.0, 0.0, 0.0, 0], fill=False)
            c.line([[-6.0, 5.215720426897359], [6.0, 5.215720426897359]], id='segment11')
            c.line([[0.0, 0.0], [4.868018763399825e-16, 7.950077960092868]], id='segment12')
            c.line([[-0.31668812311726513, 5.215720426897359], [-0.3166881231172651, 5.532408550014624]], id='right_angle13', zorder=3)
            c.line([[-0.3166881231172651, 5.532408550014624], [5.638047353957687e-17, 5.532408550014624]], id='right_angle13', zorder=3)
            c.text('S', [0.0, 0.0], id='label1', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[0, -15], annotation_clip=None)
            c.text('Q', [4.868018763399825e-16, 7.950077960092868], id='label3', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[9.18485099360515e-16, 15.0], annotation_clip=None)
            c.text('P', [-6.0, 5.215720426897359], id='label4', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[-11.320643703341581, 9.84088543485761], annotation_clip=None)
            c.text('R', [6.0, 5.215720426897359], id='label5', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[11.320643703341581, 9.84088543485761], annotation_clip=None)
            c.text('T', [0.0, 5.215720426897359], id='label6', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[-14, -14], annotation_clip=None)
            c.text('6', [3.0, 5.215720426897359], id='text16', rotation_mode='default', offset_pt=[0, -14], annotation_clip=None)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane71().draw(sys.argv[1] if len(sys.argv) > 1 else None))
