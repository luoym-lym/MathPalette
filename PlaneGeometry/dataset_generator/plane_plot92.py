"""Frozen question Plane92; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane92:

    def __init__(self):
        self.id = 'Plane92'
        self.source_dataset = 'MathVerse'
        self.source_key = 'testmini:509'
        self.question = 'As shown in the figure, and point C is the midpoint of arc BD, passing point C to draw the perpendicular line EF of AD, then the length of CE is ()\nChoices:\nA:3\nB:\\frac{20}{3}\nC:\\frac{12}{5}\nD:\\frac{16}{5}'
        self.answer = 'C'
        self.answer_type = 'choice'
        self.choices = {'A': '3', 'B': '\\frac{20}{3}', 'C': '\\frac{12}{5}', 'D': '\\frac{16}{5}'}
        self.query = self.question
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane92.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-2.9555694740595833, 4.105337992578102], ylim=[-3.9547272027821285, 3.1061802638555567], axes_position=[0.05, 0.05, 0.9, 0.9], coordinate_axes=False) as c:
            c.circle([0.0, 0.0], 2.5, id='o0', facecolor=[0.0, 0.0, 0.0, 0], fill=False)
            for object_id, points in [('o1', [[-2.5, 0.0], [2.5, 0.0]]), ('o2', [[-2.5, 0.0], [0.7, -2.4]]), ('o3', [[-2.5, 0.0], [-1.604, -3.072]]), ('o4', [[-1.604, -3.072], [3.7, -1.525]])]:
                c.line(points, id=object_id)
            c.point([[0.0, 0.0]], id='o5')
            c.line([[-2.5, 0.4], [0.0, 0.4]], id='o6', linestyle=(0, [4, 3]))
            c.line([[-2.5, 0.0], [-2.5, 0.4]], id='o7')
            c.line([[0.0, 0.0], [0.0, 0.4]], id='o8')
            c.text('2.5', [-1.25, 0.4], id='l0', rotation_mode='default', offset_pt=[0.0, 12.0], annotation_clip=None)
            c.text('4', [-0.8999999999999999, -1.2], id='l1', rotation_mode='default', offset_pt=[0, -17], annotation_clip=None)
            c.text('A', [-2.5, 0.0], id='l2', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[-14, 5], annotation_clip=None)
            c.text('B', [2.5, 0.0], id='l3', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[14, 0], annotation_clip=None)
            c.text('C', [0.7, -2.4], id='l4', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[4, -15], annotation_clip=None)
            c.text('D', [-2.108, -1.344], id='l5', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[-14, -2], annotation_clip=None)
            c.text('E', [-1.604, -3.072], id='l6', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[-10, -15], annotation_clip=None)
            c.text('F', [3.7, -1.525], id='l7', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[12, 7], annotation_clip=None)
            c.text('O', [0.0, 0.0], id='l8', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[0, -16], annotation_clip=None)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane92().draw(sys.argv[1] if len(sys.argv) > 1 else None))
