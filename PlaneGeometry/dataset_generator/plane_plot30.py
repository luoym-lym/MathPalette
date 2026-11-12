"""Frozen question Plane30; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane30:

    def __init__(self):
        self.id = 'Plane30'
        self.source_dataset = 'MathVista'
        self.source_key = 'testmini/238'
        self.question = 'Find PT\nChoices:\nA: 6\nB: \\frac { 20 } { 3 }\nC: 7\nD: 22 / 3'
        self.answer = 'B'
        self.answer_type = 'choice'
        self.choices = {'A': '6', 'B': '\\frac { 20 } { 3 }', 'C': '7', 'D': '22 / 3'}
        self.query = self.question
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane30.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-5.69087943544375, 19.49548969368871], ylim=[-3.474947322964164, 21.711421806168296], axes_position=[0.05, 0.05000000000000006, 0.9, 0.8999999999999999], coordinate_axes=False) as c:
            c.path([[0.0, 20.0], [0.0, 0.0], [15.0, 0.0], [0.0, 20.0]], [1, 2, 2, 79], id='o1', facecolor=[0.0, 0.0, 0.0, 0.0], capstyle='butt')
            c.line([[0.0, 13.333333333333334], [10.0, 0.0]], id='o2')
            for object_id, points in [('o3', [[0.0, 0.45548265930867443], [0.45548265930867443, 0.45548265930867443]]), ('o3', [[0.45548265930867443, 0.45548265930867443], [0.45548265930867443, 0.0]]), ('o4', [[5.85060918436763, 5.321649485978032], [5.8, 5.6]]), ('o4', [[6.0530459218381525, 5.473477039080924], [5.8, 5.6]]), ('o5', [[8.750609184367631, 8.121649485978033], [8.7, 8.4]]), ('o5', [[8.953045921838152, 8.273477039080923], [8.7, 8.4]])]:
                c.line(points, id=object_id, zorder=3)
            c.line([[0.0, -2.0], [10.0, -2.0]], id='o6', linestyle=(0, [4, 3]))
            c.line([[0.0, 0.0], [0.0, -2.0]], id='o7')
            c.line([[10.0, 0.0], [10.0, -2.0]], id='o8')
            c.line([[10.0, -2.0], [15.0, -2.0]], id='o9', linestyle=(0, [4, 3]))
            c.line([[10.0, 0.0], [10.0, -2.0]], id='o10')
            c.line([[15.0, 0.0], [15.0, -2.0]], id='o11')
            c.line([[-2.0, 0.0], [-2.0, 13.333333333333334]], id='o12', linestyle=(0, [4, 3]))
            c.line([[0.0, 0.0], [-2.0, 0.0]], id='o13')
            c.line([[0.0, 13.333333333333334], [-2.0, 13.333333333333334]], id='o14')
            c.text('R', [0.0, 0.0], id='l1', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[-12, -13], annotation_clip=None)
            c.text('P', [0.0, 20.0], id='l2', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[0, 15], annotation_clip=None)
            c.text('Q', [15.0, 0.0], id='l3', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[10, -10], annotation_clip=None)
            c.text('S', [10.0, 0.0], id='l4', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[-13, -12], annotation_clip=None)
            c.text('T', [0.0, 13.333333333333334], id='l5', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[-18, 12], annotation_clip=None)
            c.text('25', [7.5, 10.0], id='l6', rotation_mode='default', offset_pt=[15, 7], annotation_clip=None)
            c.text('10', [5.0, -2.0], id='l7', rotation_mode='default', offset_pt=[0, -14], annotation_clip=None)
            c.text('5', [12.5, -2.0], id='l8', rotation_mode='default', offset_pt=[0, -14], annotation_clip=None)
            c.text('x', [-2.0, 6.666666666666667], id='l9', rotation_mode='default', offset_pt=[14, 0], annotation_clip=None)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane30().draw(sys.argv[1] if len(sys.argv) > 1 else None))
