"""Frozen question Solid134; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Solid134:

    def __init__(self):
        self.id = 'Solid134'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:929'
        self.question = 'Vases I, II and III contain 4 liters, 3 liters and 4 liters of water, respectively, as shown. Viewed from the front, the three vases appear to have the same size. Which of the following images could show the vases viewed from above?\nChoices:\nA:(A)\nB:(B)\nC:(C)\nD:(D)\nE:(E)'
        self.answer = 'A'
        self.answer_type = 'choice'
        self.choices = {'A': '(A)', 'B': '(B)', 'C': '(C)', 'D': '(D)', 'E': '(E)'}
        self.query = self.question
        self.subject = 'SolidGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'SolidGeometry' / 'dataset_generator/scenes/Solid134.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('SolidGeometry', self.id, variant, output_path)
        with Canvas(SOLID, xlim=[-0.699709598922098, 21.543203448342414], ylim=[-5.171664756833834, 17.071248290430677], axes_position=[0.05, 0.05, 0.9, 0.9], coordinate_axes=False) as c:
            for object_id, points in [('front0edge0', [[7.0, 11.3], [8.4, 11.3]]), ('front0edge1', [[8.4, 11.3], [8.4, 13.4]]), ('front0edge2', [[8.4, 13.4], [7.0, 13.4]]), ('front0edge3', [[7.0, 13.4], [7.0, 11.3]])]:
                c.line(points, id=object_id, zorder=3, clip_on=False)
            c.path([[7.0, 11.3], [8.4, 11.3], [8.4, 12.392000000000001], [7.0, 12.392000000000001], [7.0, 11.3]], [1, 2, 2, 2, 79], id='water0', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 1.0], linewidth=0.0, capstyle='butt')
            for object_id, points in [('front1edge0', [[9.0, 11.3], [10.4, 11.3]]), ('front1edge1', [[10.4, 11.3], [10.4, 13.4]]), ('front1edge2', [[10.4, 13.4], [9.0, 13.4]]), ('front1edge3', [[9.0, 13.4], [9.0, 11.3]])]:
                c.line(points, id=object_id, zorder=3, clip_on=False)
            c.path([[9.0, 11.3], [10.4, 11.3], [10.4, 12.665000000000001], [9.0, 12.665000000000001], [9.0, 11.3]], [1, 2, 2, 2, 79], id='water1', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 1.0], linewidth=0.0, capstyle='butt')
            for object_id, points in [('front2edge0', [[11.0, 11.3], [12.4, 11.3]]), ('front2edge1', [[12.4, 11.3], [12.4, 13.4]]), ('front2edge2', [[12.4, 13.4], [11.0, 13.4]]), ('front2edge3', [[11.0, 13.4], [11.0, 11.3]])]:
                c.line(points, id=object_id, zorder=3, clip_on=False)
            c.path([[11.0, 11.3], [12.4, 11.3], [12.4, 12.119000000000002], [11.0, 12.119000000000002], [11.0, 11.3]], [1, 2, 2, 2, 79], id='water2', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[0.0, 6.2], [1.4, 6.2], [1.4, 8.3], [0.0, 8.3], [0.0, 6.2]], [1, 2, 2, 2, 79], id='option0vase0fill', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 1.0], linewidth=0.0, capstyle='butt')
            for object_id, points in [('option0vase0edge0', [[0.0, 6.2], [1.4, 6.2]]), ('option0vase0edge1', [[1.4, 6.2], [1.4, 8.3]]), ('option0vase0edge2', [[1.4, 8.3], [0.0, 8.3]]), ('option0vase0edge3', [[0.0, 8.3], [0.0, 6.2]])]:
                c.line(points, id=object_id, zorder=3, clip_on=False)
            c.path([[2.0, 6.2], [3.4, 6.2], [3.4, 7.88], [2.0, 7.88], [2.0, 6.2]], [1, 2, 2, 2, 79], id='option0vase1fill', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 1.0], linewidth=0.0, capstyle='butt')
            for object_id, points in [('option0vase1edge0', [[2.0, 6.2], [3.4, 6.2]]), ('option0vase1edge1', [[3.4, 6.2], [3.4, 7.88]]), ('option0vase1edge2', [[3.4, 7.88], [2.0, 7.88]]), ('option0vase1edge3', [[2.0, 7.88], [2.0, 6.2]])]:
                c.line(points, id=object_id, zorder=3, clip_on=False)
            c.path([[4.0, 6.2], [5.4, 6.2], [5.4, 9.0], [4.0, 9.0], [4.0, 6.2]], [1, 2, 2, 2, 79], id='option0vase2fill', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 1.0], linewidth=0.0, capstyle='butt')
            for object_id, points in [('option0vase2edge0', [[4.0, 6.2], [5.4, 6.2]]), ('option0vase2edge1', [[5.4, 6.2], [5.4, 9.0]]), ('option0vase2edge2', [[5.4, 9.0], [4.0, 9.0]]), ('option0vase2edge3', [[4.0, 9.0], [4.0, 6.2]])]:
                c.line(points, id=object_id, zorder=3, clip_on=False)
            c.path([[7.8, 6.2], [9.2, 6.2], [9.2, 9.0], [7.8, 9.0], [7.8, 6.2]], [1, 2, 2, 2, 79], id='option1vase0fill', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 1.0], linewidth=0.0, capstyle='butt')
            for object_id, points in [('option1vase0edge0', [[7.8, 6.2], [9.2, 6.2]]), ('option1vase0edge1', [[9.2, 6.2], [9.2, 9.0]]), ('option1vase0edge2', [[9.2, 9.0], [7.8, 9.0]]), ('option1vase0edge3', [[7.8, 9.0], [7.8, 6.2]])]:
                c.line(points, id=object_id, zorder=3, clip_on=False)
            c.path([[9.8, 6.2], [11.200000000000001, 6.2], [11.200000000000001, 7.88], [9.8, 7.88], [9.8, 6.2]], [1, 2, 2, 2, 79], id='option1vase1fill', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 1.0], linewidth=0.0, capstyle='butt')
            for object_id, points in [('option1vase1edge0', [[9.8, 6.2], [11.200000000000001, 6.2]]), ('option1vase1edge1', [[11.200000000000001, 6.2], [11.200000000000001, 7.88]]), ('option1vase1edge2', [[11.200000000000001, 7.88], [9.8, 7.88]]), ('option1vase1edge3', [[9.8, 7.88], [9.8, 6.2]])]:
                c.line(points, id=object_id, zorder=3, clip_on=False)
            c.path([[11.8, 6.2], [13.200000000000001, 6.2], [13.200000000000001, 8.3], [11.8, 8.3], [11.8, 6.2]], [1, 2, 2, 2, 79], id='option1vase2fill', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 1.0], linewidth=0.0, capstyle='butt')
            for object_id, points in [('option1vase2edge0', [[11.8, 6.2], [13.200000000000001, 6.2]]), ('option1vase2edge1', [[13.200000000000001, 6.2], [13.200000000000001, 8.3]]), ('option1vase2edge2', [[13.200000000000001, 8.3], [11.8, 8.3]]), ('option1vase2edge3', [[11.8, 8.3], [11.8, 6.2]])]:
                c.line(points, id=object_id, zorder=3, clip_on=False)
            c.path([[15.6, 6.2], [17.0, 6.2], [17.0, 9.0], [15.6, 9.0], [15.6, 6.2]], [1, 2, 2, 2, 79], id='option2vase0fill', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 1.0], linewidth=0.0, capstyle='butt')
            for object_id, points in [('option2vase0edge0', [[15.6, 6.2], [17.0, 6.2]]), ('option2vase0edge1', [[17.0, 6.2], [17.0, 9.0]]), ('option2vase0edge2', [[17.0, 9.0], [15.6, 9.0]]), ('option2vase0edge3', [[15.6, 9.0], [15.6, 6.2]])]:
                c.line(points, id=object_id, zorder=3, clip_on=False)
            c.path([[17.6, 6.2], [19.0, 6.2], [19.0, 8.440000000000001], [17.6, 8.440000000000001], [17.6, 6.2]], [1, 2, 2, 2, 79], id='option2vase1fill', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 1.0], linewidth=0.0, capstyle='butt')
            for object_id, points in [('option2vase1edge0', [[17.6, 6.2], [19.0, 6.2]]), ('option2vase1edge1', [[19.0, 6.2], [19.0, 8.440000000000001]]), ('option2vase1edge2', [[19.0, 8.440000000000001], [17.6, 8.440000000000001]]), ('option2vase1edge3', [[17.6, 8.440000000000001], [17.6, 6.2]])]:
                c.line(points, id=object_id, zorder=3, clip_on=False)
            c.path([[19.6, 6.2], [21.0, 6.2], [21.0, 8.3], [19.6, 8.3], [19.6, 6.2]], [1, 2, 2, 2, 79], id='option2vase2fill', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 1.0], linewidth=0.0, capstyle='butt')
            for object_id, points in [('option2vase2edge0', [[19.6, 6.2], [21.0, 6.2]]), ('option2vase2edge1', [[21.0, 6.2], [21.0, 8.3]]), ('option2vase2edge2', [[21.0, 8.3], [19.6, 8.3]]), ('option2vase2edge3', [[19.6, 8.3], [19.6, 6.2]])]:
                c.line(points, id=object_id, zorder=3, clip_on=False)
            c.path([[0.0, 0.5], [1.4, 0.5], [1.4, 2.075], [0.0, 2.075], [0.0, 0.5]], [1, 2, 2, 2, 79], id='option3vase0fill', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 1.0], linewidth=0.0, capstyle='butt')
            for object_id, points in [('option3vase0edge0', [[0.0, 0.5], [1.4, 0.5]]), ('option3vase0edge1', [[1.4, 0.5], [1.4, 2.075]]), ('option3vase0edge2', [[1.4, 2.075], [0.0, 2.075]]), ('option3vase0edge3', [[0.0, 2.075], [0.0, 0.5]])]:
                c.line(points, id=object_id, zorder=3, clip_on=False)
            c.path([[2.0, 0.5], [3.4, 0.5], [3.4, 3.2], [2.0, 3.2], [2.0, 0.5]], [1, 2, 2, 2, 79], id='option3vase1fill', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 1.0], linewidth=0.0, capstyle='butt')
            for object_id, points in [('option3vase1edge0', [[2.0, 0.5], [3.4, 0.5]]), ('option3vase1edge1', [[3.4, 0.5], [3.4, 3.2]]), ('option3vase1edge2', [[3.4, 3.2], [2.0, 3.2]]), ('option3vase1edge3', [[2.0, 3.2], [2.0, 0.5]])]:
                c.line(points, id=object_id, zorder=3, clip_on=False)
            c.path([[4.0, 0.5], [5.4, 0.5], [5.4, 2.6], [4.0, 2.6], [4.0, 0.5]], [1, 2, 2, 2, 79], id='option3vase2fill', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 1.0], linewidth=0.0, capstyle='butt')
            for object_id, points in [('option3vase2edge0', [[4.0, 0.5], [5.4, 0.5]]), ('option3vase2edge1', [[5.4, 0.5], [5.4, 2.6]]), ('option3vase2edge2', [[5.4, 2.6], [4.0, 2.6]]), ('option3vase2edge3', [[4.0, 2.6], [4.0, 0.5]])]:
                c.line(points, id=object_id, zorder=3, clip_on=False)
            c.path([[7.8, 0.5], [9.2, 0.5], [9.2, 2.6], [7.8, 2.6], [7.8, 0.5]], [1, 2, 2, 2, 79], id='option4vase0fill', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 1.0], linewidth=0.0, capstyle='butt')
            for object_id, points in [('option4vase0edge0', [[7.8, 0.5], [9.2, 0.5]]), ('option4vase0edge1', [[9.2, 0.5], [9.2, 2.6]]), ('option4vase0edge2', [[9.2, 2.6], [7.8, 2.6]]), ('option4vase0edge3', [[7.8, 2.6], [7.8, 0.5]])]:
                c.line(points, id=object_id, zorder=3, clip_on=False)
            c.path([[9.8, 0.5], [11.200000000000001, 0.5], [11.200000000000001, 2.6], [9.8, 2.6], [9.8, 0.5]], [1, 2, 2, 2, 79], id='option4vase1fill', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 1.0], linewidth=0.0, capstyle='butt')
            for object_id, points in [('option4vase1edge0', [[9.8, 0.5], [11.200000000000001, 0.5]]), ('option4vase1edge1', [[11.200000000000001, 0.5], [11.200000000000001, 2.6]]), ('option4vase1edge2', [[11.200000000000001, 2.6], [9.8, 2.6]]), ('option4vase1edge3', [[9.8, 2.6], [9.8, 0.5]])]:
                c.line(points, id=object_id, zorder=3, clip_on=False)
            c.path([[11.8, 0.5], [13.200000000000001, 0.5], [13.200000000000001, 2.6], [11.8, 2.6], [11.8, 0.5]], [1, 2, 2, 2, 79], id='option4vase2fill', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 1.0], linewidth=0.0, capstyle='butt')
            for object_id, points in [('option4vase2edge0', [[11.8, 0.5], [13.200000000000001, 0.5]]), ('option4vase2edge1', [[13.200000000000001, 0.5], [13.200000000000001, 2.6]]), ('option4vase2edge2', [[13.200000000000001, 2.6], [11.8, 2.6]]), ('option4vase2edge3', [[11.8, 2.6], [11.8, 0.5]])]:
                c.line(points, id=object_id, zorder=3, clip_on=False)
            for object_id, text, anchor in [('frontlabel0', 'I', [7.7, 11.3]), ('frontlabel1', 'II', [9.7, 11.3]), ('frontlabel2', 'III', [11.7, 11.3]), ('roman00', 'I', [0.7, 6.2]), ('roman01', 'II', [2.7, 6.2]), ('roman02', 'III', [4.7, 6.2])]:
                c.text(text, anchor, id=object_id, rotation_mode='default', offset_pt=[0, -17], annotation_clip=None)
            c.text('(A)', [0.3, 6.2], id='choice0', rotation_mode='default', offset_pt=[0, -39], annotation_clip=None)
            for object_id, text, anchor in [('roman10', 'I', [8.5, 6.2]), ('roman11', 'II', [10.5, 6.2]), ('roman12', 'III', [12.5, 6.2])]:
                c.text(text, anchor, id=object_id, rotation_mode='default', offset_pt=[0, -17], annotation_clip=None)
            c.text('(B)', [8.1, 6.2], id='choice1', rotation_mode='default', offset_pt=[0, -39], annotation_clip=None)
            for object_id, text, anchor in [('roman20', 'I', [16.3, 6.2]), ('roman21', 'II', [18.3, 6.2]), ('roman22', 'III', [20.3, 6.2])]:
                c.text(text, anchor, id=object_id, rotation_mode='default', offset_pt=[0, -17], annotation_clip=None)
            c.text('(C)', [15.9, 6.2], id='choice2', rotation_mode='default', offset_pt=[0, -39], annotation_clip=None)
            for object_id, text, anchor in [('roman30', 'I', [0.7, 0.5]), ('roman31', 'II', [2.7, 0.5]), ('roman32', 'III', [4.7, 0.5])]:
                c.text(text, anchor, id=object_id, rotation_mode='default', offset_pt=[0, -17], annotation_clip=None)
            c.text('(D)', [0.3, 0.5], id='choice3', rotation_mode='default', offset_pt=[0, -39], annotation_clip=None)
            for object_id, text, anchor in [('roman40', 'I', [8.5, 0.5]), ('roman41', 'II', [10.5, 0.5]), ('roman42', 'III', [12.5, 0.5])]:
                c.text(text, anchor, id=object_id, rotation_mode='default', offset_pt=[0, -17], annotation_clip=None)
            c.text('(E)', [8.1, 0.5], id='choice4', rotation_mode='default', offset_pt=[0, -39], annotation_clip=None)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Solid134().draw(sys.argv[1] if len(sys.argv) > 1 else None))
