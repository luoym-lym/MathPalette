"""Frozen question Plane76; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane76:

    def __init__(self):
        self.id = 'Plane76'
        self.source_dataset = 'MathVerse'
        self.source_key = 'testmini:39'
        self.question = 'As shown in the figure, triangle ABC congruent triangle DEF, then the length of EC is ()\nChoices:\nA:1cm\nB:2cm\nC:3cm\nD:4cm'
        self.answer = 'C'
        self.answer_type = 'choice'
        self.choices = {'A': '1cm', 'B': '2cm', 'C': '3cm', 'D': '4cm'}
        self.query = self.question
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane76.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-0.46425021342581196, 7.458428896216078], ylim=[-2.481309089469966, 5.441370020171924], axes_position=[0.05, 0.05, 0.9, 0.9], coordinate_axes=False) as c:
            for object_id, points in [('o0', [[3.0, 4.0], [0.0, 0.0]]), ('o1', [[0.0, 0.0], [5.0, 0.0]]), ('o2', [[5.0, 0.0], [3.0, 4.0]]), ('o3', [[5.0, 4.0], [2.0, 0.0]]), ('o4', [[2.0, 0.0], [7.0, 0.0]]), ('o5', [[7.0, 0.0], [5.0, 4.0]])]:
                c.line(points, id=object_id)
            c.line([[0.0, -0.55], [5.0, -0.55]], id='o6', linestyle=(0, [4, 3]))
            c.line([[0.0, 0.0], [0.0, -0.55]], id='o7')
            c.line([[5.0, 0.0], [5.0, -0.55]], id='o8')
            c.line([[0.0, -1.15], [7.0, -1.15]], id='o9', linestyle=(0, [4, 3]))
            c.line([[0.0, 0.0], [0.0, -1.15]], id='o10')
            c.line([[7.0, 0.0], [7.0, -1.15]], id='o11')
            c.text('5.0', [2.5, -0.55], id='l0', rotation_mode='default', offset_pt=[0.0, -12.0], annotation_clip=None)
            c.text('7.0', [3.5, -1.15], id='l1', rotation_mode='default', offset_pt=[0.0, -12.0], annotation_clip=None)
            c.text('A', [3.0, 4.0], id='l2', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[0, 15], annotation_clip=None)
            c.text('D', [5.0, 4.0], id='l3', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[0, 15], annotation_clip=None)
            c.text('B', [0.0, 0.0], id='l4', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[-12, 4], annotation_clip=None)
            c.text('E', [2.0, 0.0], id='l5', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[-1.5862345180073758, 18.13074350526977], annotation_clip=None)
            c.text('C', [5.0, 0.0], id='l6', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[4.7105066208658775, 17.579850038461043], annotation_clip=None)
            c.text('F', [7.0, 0.0], id='l7', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[12, 4], annotation_clip=None)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane76().draw(sys.argv[1] if len(sys.argv) > 1 else None))
