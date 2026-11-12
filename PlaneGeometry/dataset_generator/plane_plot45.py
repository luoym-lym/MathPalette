"""Frozen question Plane45; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane45:

    def __init__(self):
        self.id = 'Plane45'
        self.source_dataset = 'MathVista'
        self.source_key = 'testmini/414'
        self.question = 'If $ST=8, TR=4$, and $PT=6$, find $QR$.\nChoices:\nA: 6\nB: 8\nC: 9\nD: 10'
        self.answer = 'C'
        self.answer_type = 'choice'
        self.choices = {'A': '6', 'B': '8', 'C': '9', 'D': '10'}
        self.query = self.question
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane45.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-0.7411519966334099, 13.712940191077855], ylim=[-11.224757055817946, 3.2293351318933183], axes_position=[0.05, 0.05, 0.9, 0.9], coordinate_axes=False) as c:
            c.path([[0.0, 0.0], [13.0, 0.0], [4.076923076923077, -8.023633729480183], [0.0, 0.0]], [1, 2, 2, 79], id='o1', facecolor=[0.0, 0.0, 0.0, 0.0], capstyle='butt')
            c.line([[4.333333333333334, 0.0], [7.051282051282051, -5.349089152986789]], id='o2')
            for object_id, points in [('o3', [[2.0374110179933713, -3.849460053044335], [2.0384615384615383, -4.011816864740092]]), ('o3', [[1.9079457768240327, -3.9152431940971706], [2.0384615384615383, -4.011816864740092]]), ('o4', [[5.691257171839526, -2.5121877647976376], [5.6923076923076925, -2.6745445764933944]]), ('o4', [[5.5617919306701875, -2.5779709058504734], [5.6923076923076925, -2.6745445764933944]])]:
                c.line(points, id=object_id, zorder=3)
            c.text('Q', [0.0, 0.0], id='v5', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[-8, 13], annotation_clip=None)
            c.text('P', [4.333333333333334, 0.0], id='v6', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[0, 13], annotation_clip=None)
            c.text('S', [13.0, 0.0], id='v7', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[8, 13], annotation_clip=None)
            c.text('T', [7.051282051282051, -5.349089152986789], id='v8', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[16, -15], annotation_clip=None)
            c.text('R', [4.076923076923077, -8.023633729480183], id='v9', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[0, -15], annotation_clip=None)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane45().draw(sys.argv[1] if len(sys.argv) > 1 else None))
