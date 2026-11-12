"""Frozen question Plane361; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane361:

    def __init__(self):
        self.id = 'Plane361'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:1299'
        self.question = 'A square with sides of length 10 is rolled without slipping along a line. The rolling stops when $P$ first returns to the line. What is the length of the curve that $P$ has travelled?\nChoices:\nA:$10 \\pi$\nB:$5 \\pi+5 \\pi \\sqrt{2}$\nC:$10 \\pi+5 \\pi \\sqrt{2}$\nD:$5 \\pi+10 \\pi \\sqrt{2}$\nE:$10 \\pi+10 \\pi \\sqrt{2}$'
        self.answer = 'C'
        self.answer_type = 'choice'
        self.choices = {'A': '$10 \\pi$',
         'B': '$5 \\pi+5 \\pi \\sqrt{2}$',
         'C': '$10 \\pi+5 \\pi \\sqrt{2}$',
         'D': '$5 \\pi+10 \\pi \\sqrt{2}$',
         'E': '$10 \\pi+10 \\pi \\sqrt{2}$'}
        self.query = self.question
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane361.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-1.370897503303972, 10.08879248977171], ylim=[-4.536286243091408, 6.923403749984273], axes_position=[0.05, 0.05, 0.9, 0.9], coordinate_axes=False) as c:
            c.path([[0.0, 0.0], [2.0, 0.0], [2.0, 2.0], [0.0, 2.0], [0.0, 0.0]], [1, 2, 2, 2, 79], id='o0', facecolor=[0.0, 0.0, 0.0, 0.0], capstyle='butt')
            c.line([[-1.1, 0.0], [3.3, 0.0]], id='o1')
            c.point([[0.0, 0.0]], id='o2')
            for object_id, points in [('o3', [[0.5857864376269049, 1.414213562373095], [2.0, 0.0]]), ('o4', [[2.0, 0.0], [3.414213562373095, 1.4142135623730951]]), ('o5', [[3.414213562373095, 1.4142135623730951], [1.9999999999999998, 2.82842712474619]]), ('o6', [[1.9999999999999998, 2.82842712474619], [0.5857864376269049, 1.414213562373095]])]:
                c.line(points, id=object_id, linestyle=(0.0, [4.0, 3.0]))
            c.path([[0.5857864376269051, 1.4142135623730951], [0.40007361418738374, 1.2285007389335738], [0.25274799077003474, 1.0080123619388839], [0.15224093497742652, 0.7653668647301798], [0.05173387918481831, 0.5227213675214757], [0.0, 0.2626375936147714], [0.0, 2.4492935982947064e-16]], [1, 4, 4, 4, 4, 4, 4], id='o7', facecolor=[0.0, 0.0, 0.0, 0], capstyle='butt', fill=False)
            c.circle([0.5857864376269049, 1.414213562373095], 0.055, id='o8', facecolor=[0.0, 0.0, 0.0, 0], fill=False)
            for object_id, points in [('o9', [[3.55, 0.0]]), ('o10', [[3.8499999999999996, 0.0]]), ('o11', [[4.1499999999999995, 0.0]]), ('o12', [[4.449999999999999, 0.0]]), ('o13', [[4.749999999999999, 0.0]]), ('o14', [[5.049999999999999, 0.0]]), ('o15', [[5.349999999999999, 0.0]])]:
                c.point(points, id=object_id)
            c.line([[5.8, 0.0], [9.8, 0.0]], id='o16')
            for object_id, points in [('o17', [[7.0, 0.0], [9.0, 0.0]]), ('o18', [[9.0, 0.0], [9.0, 2.0]]), ('o19', [[9.0, 2.0], [7.0, 2.0]]), ('o20', [[7.0, 2.0], [7.0, 0.0]])]:
                c.line(points, id=object_id, linestyle=(0.0, [4.0, 3.0]))
            c.path([[9.0, 0.0], [9.0, 0.2626375936147712], [8.948266120815182, 0.5227213675214755], [8.847759065022574, 0.7653668647301796], [8.747252009229966, 1.0080123619388837], [8.599926385812616, 1.2285007389335736], [8.414213562373096, 1.414213562373095]], [1, 4, 4, 4, 4, 4, 4], id='o21', facecolor=[0.0, 0.0, 0.0, 0], capstyle='butt', fill=False)
            c.point([[9.0, 0.0]], id='o22')
            c.text('P', [0.0, 0.0], id='lP', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[-8, -15], annotation_clip=None)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane361().draw(sys.argv[1] if len(sys.argv) > 1 else None))
