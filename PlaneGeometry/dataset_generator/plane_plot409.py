"""Frozen question Plane409; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane409:

    def __init__(self):
        self.id = 'Plane409'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:1748'
        self.question = 'Three congruent isosceles trapeziums are assembled to form an equilateral triangle with a hole in the middle, as shown in the diagram.\nWhat is the perimeter of the hole?\nChoices:\nA:$3 a+6 b$\nB:$3 b-6 a$\nC:$6 b-3 a$\nD:$6 a+3 b$\nE:$6 a-3 b$'
        self.answer = 'E'
        self.answer_type = 'choice'
        self.choices = {'A': '$3 a+6 b$', 'B': '$3 b-6 a$', 'C': '$6 b-3 a$', 'D': '$6 a+3 b$', 'E': '$6 a-3 b$'}
        self.query = self.question
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane409.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-0.3464050739698479, 14.344377955014274], ylim=[-2.631850118352496, 12.058932910631626], axes_position=[0.05, 0.05, 0.9, 0.9], coordinate_axes=False) as c:
            c.path([[9.5, 1.8660254037844386], [12.5, 1.8660254037844386], [11.0, 4.464101615137754], [9.5, 1.8660254037844386]], [1, 2, 2, 79], id='greyhole', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.0, 0.0, 0.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[9.5, 1.8660254037844386], [12.5, 1.8660254037844386], [11.0, 4.464101615137754], [9.5, 1.8660254037844386]], [1, 2, 2, 79], id='greyhole', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            for object_id, vertices, codes in [('trapezium0', [[0.0, 7.0], [5.0, 7.0], [4.5, 7.866025403784438], [0.5, 7.866025403784438], [0.0, 7.0]], [1, 2, 2, 2, 79]), ('trapezium1', [[0.0, 4.0], [5.0, 4.0], [4.5, 4.866025403784438], [0.5, 4.866025403784438], [0.0, 4.0]], [1, 2, 2, 2, 79]), ('trapezium2', [[0.0, 1.0], [5.0, 1.0], [4.5, 1.8660254037844386], [0.5, 1.8660254037844386], [0.0, 1.0]], [1, 2, 2, 2, 79]), ('joinedtrapezium0', [[8.0, 1.0], [13.0, 1.0], [12.5, 1.8660254037844386], [8.5, 1.8660254037844386], [8.0, 1.0]], [1, 2, 2, 2, 79]), ('joinedtrapezium1', [[14.0, 0.9999999999999993], [11.5, 5.330127018922193], [11.0, 4.464101615137754], [13.0, 0.9999999999999996], [14.0, 0.9999999999999993]], [1, 2, 2, 2, 79]), ('joinedtrapezium2', [[11.000000000000002, 6.196152422706632], [8.5, 1.8660254037844397], [9.5, 1.8660254037844393], [11.500000000000002, 5.330127018922193], [11.000000000000002, 6.196152422706632]], [1, 2, 2, 2, 79])]:
                c.path(vertices, codes, id=object_id, facecolor=[0.0, 0.0, 0.0, 0.0], capstyle='butt')
            c.text('a', [2.5, 7.866025403784438], id='alabel', rotation_mode='default', offset_pt=[0, 15], annotation_clip=None)
            c.text('b', [2.5, 7.0], id='blabel', rotation_mode='default', offset_pt=[0, -15], annotation_clip=None)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane409().draw(sys.argv[1] if len(sys.argv) > 1 else None))
