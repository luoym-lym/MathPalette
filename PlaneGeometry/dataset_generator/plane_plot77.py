"""Frozen question Plane77; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane77:

    def __init__(self):
        self.id = 'Plane77'
        self.source_dataset = 'MathVerse'
        self.source_key = 'testmini:44'
        self.question = 'As shown in the figure, AC = BC, AD bisects angle CAB, then the perimeter of triangle DBE is ()\nChoices:\nA:6cm\nB:7cm\nC:8cm\nD:9cm'
        self.answer = 'A'
        self.answer_type = 'choice'
        self.choices = {'A': '6cm', 'B': '7cm', 'C': '8cm', 'D': '9cm'}
        self.query = self.question
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane77.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-0.41863883221958664, 6.392208454144383], ylim=[-2.104687709551224, 4.706159576812745], axes_position=[0.05, 0.05000000000000006, 0.9, 0.8999999999999999], coordinate_axes=False) as c:
            for object_id, points in [('o0', [[0.0, 0.0], [6.0, 0.0]]), ('o1', [[6.0, 0.0], [3.0, 3.0]]), ('o2', [[3.0, 3.0], [0.0, 0.0]]), ('o3', [[0.0, 0.0], [4.242640687119286, 1.7573593128807143]]), ('o4', [[4.242640687119286, 1.7573593128807143], [4.242640687119286, 0.0]])]:
                c.line(points, id=object_id)
            for object_id, points in [('o5', [[2.912905159472404, 2.912905159472404], [3.0, 2.825810318944808]]), ('o5', [[3.0, 2.825810318944808], [3.087094840527596, 2.912905159472404]]), ('o6', [[4.242640687119286, 0.1231707046868484], [4.365811391806134, 0.1231707046868484]]), ('o6', [[4.365811391806134, 0.1231707046868484], [4.365811391806134, 0.0]])]:
                c.line(points, id=object_id, zorder=3)
            c.line([[0.0, -0.5], [6.0, -0.5]], id='o7', linestyle=(0, [4, 3]))
            c.line([[0.0, 0.0], [0.0, -0.5]], id='o8')
            c.line([[6.0, 0.0], [6.0, -0.5]], id='o9')
            c.text('6.0', [3.0, -0.5], id='l0', rotation_mode='default', offset_pt=[0.0, -12.0], annotation_clip=None)
            c.text('A', [0.0, 0.0], id='l1', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[-12, 2], annotation_clip=None)
            c.text('B', [6.0, 0.0], id='l2', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[12, 2], annotation_clip=None)
            c.text('C', [3.0, 3.0], id='l3', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[0, 15], annotation_clip=None)
            c.text('D', [4.242640687119286, 1.7573593128807143], id='l4', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[12, 9], annotation_clip=None)
            c.text('E', [4.242640687119286, 0.0], id='l5', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[0, -13], annotation_clip=None)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane77().draw(sys.argv[1] if len(sys.argv) > 1 else None))
