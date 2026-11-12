"""Frozen question Plane34; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane34:

    def __init__(self):
        self.id = 'Plane34'
        self.source_dataset = 'MathVista'
        self.source_key = 'testmini/300'
        self.question = '$\\overline{HK}$ and $\\overline{IG}$ are diameters of $\\odot L$. Find $m \\widehat {IHJ}$.\nChoices:\nA: 59\nB: 135\nC: 270\nD: 301'
        self.answer = 'C'
        self.answer_type = 'choice'
        self.choices = {'A': '59', 'B': '135', 'C': '270', 'D': '301'}
        self.query = self.question
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane34.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-1.1015066376196063, 1.1724257040561372], ylim=[-1.1321782714546789, 1.1417540702210647], axes_position=[0.05, 0.05, 0.9, 0.9], coordinate_axes=False) as c:
            c.circle([0.0, 0.0], 1.0, id='o1', facecolor=[0.0, 0.0, 0.0, 0], fill=False)
            for object_id, points in [('o2', [[6.123233995736766e-17, 1.0], [-1.8369701987210297e-16, -1.0]]), ('o3', [[-0.8571673007021122, 0.5150380749100544], [0.8571673007021121, -0.5150380749100545]]), ('o4', [[0.0, 0.0], [1.0, 0.0]])]:
                c.line(points, id=object_id)
            c.point([[0.0, 0.0]], id='o5')
            c.line([[2.5180519058438627e-18, 0.041122908378105894], [0.041122908378105894, 0.041122908378105894]], id='o12', zorder=3)
            c.line([[0.041122908378105894, 0.041122908378105894], [0.041122908378105894, 0.0]], id='o12', zorder=3)
            c.path([[6.994588627344064e-18, 0.11423030105029415], [-0.019712289138694838, 0.11423030105029415], [-0.03909298838299938, 0.10912778876351804], [-0.05624969151487665, 0.09942099316805302], [-0.07340639464675393, 0.089714197572588], [-0.08776189935960653, 0.0757296840210141], [-0.09791447880967029, 0.05883295434933946]], [1, 4, 4, 4, 4, 4, 4], id='o14', zorder=3, facecolor=[0.0, 0.0, 0.0, 0], capstyle='butt', fill=False)
            c.text('H', [-0.8571673007021122, 0.5150380749100544], id='v6', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[-12, 8], annotation_clip=None)
            c.text('I', [6.123233995736766e-17, 1.0], id='v7', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[0, 12], annotation_clip=None)
            c.text('J', [1.0, 0.0], id='v8', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[13, 0], annotation_clip=None)
            c.text('G', [-1.8369701987210297e-16, -1.0], id='v9', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[0, -13], annotation_clip=None)
            c.text('K', [0.8571673007021121, -0.5150380749100545], id='v10', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[8, -10], annotation_clip=None)
            c.text('L', [0.0, 0.0], id='v11', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[-10, -11], annotation_clip=None)
            c.text('59°', [0.0, 0.0], id='a15', rotation_mode='default', offset_pt=[-24.62117800517335, 43.51778479699499], annotation_clip=None)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane34().draw(sys.argv[1] if len(sys.argv) > 1 else None))
