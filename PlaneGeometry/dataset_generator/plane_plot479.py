"""Frozen question Plane479; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane479:

    def __init__(self):
        self.id = 'Plane479'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:2725'
        self.question = 'Squares $ABCD$, $EFGH$, and $GHIJ$ are equal in area. Points $C$ and $D$ are the midpoints of sides $IH$ and $HE$, respectively. What is the ratio of the area of the shaded pentagon $AJICB$ to the sum of the areas of the three squares?\n\nChoices:\nA:$\\frac{1}{4}$\nB:$\\frac{7}{24}$\nC:$\\frac{1}{3}$\nD:$\\frac{3}{8}$\nE:$\\frac{5}{12}$'
        self.answer = 'C'
        self.answer_type = 'choice'
        self.choices = {'A': '$\\frac{1}{4}$', 'B': '$\\frac{7}{24}$', 'C': '$\\frac{1}{3}$', 'D': '$\\frac{3}{8}$', 'E': '$\\frac{5}{12}$'}
        self.query = self.question
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane479.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-0.3313083916980377, 4.304631147583926], ylim=[-2.321297315937278, 2.3146422233446855], axes_position=[0.05, 0.05, 0.9, 0.9], coordinate_axes=False) as c:
            c.path([[1.0, 2.0], [4.0, -2.0], [4.0, 0.0], [3.0, 0.0], [3.0, 2.0], [1.0, 2.0]], [1, 2, 2, 2, 2, 79], id='shaded', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45], linewidth=0.0, capstyle='butt')
            c.path([[1.0, 2.0], [4.0, -2.0], [4.0, 0.0], [3.0, 0.0], [3.0, 2.0], [1.0, 2.0]], [1, 2, 2, 2, 2, 79], id='shaded', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            for object_id, vertices, codes in [('upper', [[1.0, 2.0], [3.0, 2.0], [3.0, 0.0], [1.0, 0.0], [1.0, 2.0]], [1, 2, 2, 2, 79]), ('lowerleft', [[0.0, 0.0], [0.0, -2.0], [2.0, -2.0], [2.0, 0.0], [0.0, 0.0]], [1, 2, 2, 2, 79]), ('lowerright', [[2.0, -2.0], [2.0, 0.0], [4.0, 0.0], [4.0, -2.0], [2.0, -2.0]], [1, 2, 2, 2, 79])]:
                c.path(vertices, codes, id=object_id, facecolor=[0.0, 0.0, 0.0, 0.0], capstyle='butt')
            for object_id, points in [('dotE', [[0.0, 0.0]]), ('dotF', [[0.0, -2.0]]), ('dotG', [[2.0, -2.0]]), ('dotH', [[2.0, 0.0]]), ('dotI', [[4.0, 0.0]]), ('dotJ', [[4.0, -2.0]]), ('dotD', [[1.0, 0.0]]), ('dotC', [[3.0, 0.0]]), ('dotA', [[1.0, 2.0]]), ('dotB', [[3.0, 2.0]])]:
                c.point(points, id=object_id)
            c.text('A', [1.0, 2.0], id='nameA', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[-13, 15], annotation_clip=None)
            c.text('B', [3.0, 2.0], id='nameB', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[13, 15], annotation_clip=None)
            c.text('C', [3.0, 0.0], id='nameC', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[15, 13], annotation_clip=None)
            c.text('D', [1.0, 0.0], id='nameD', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[-16, 13], annotation_clip=None)
            c.text('E', [0.0, 0.0], id='nameE', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[-15, 13], annotation_clip=None)
            c.text('F', [0.0, -2.0], id='nameF', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[-15, -15], annotation_clip=None)
            c.text('G', [2.0, -2.0], id='nameG', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[0, -17], annotation_clip=None)
            c.text('H', [2.0, 0.0], id='nameH', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[0, 16], annotation_clip=None)
            c.text('I', [4.0, 0.0], id='nameI', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[15, 13], annotation_clip=None)
            c.text('J', [4.0, -2.0], id='nameJ', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[15, -15], annotation_clip=None)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane479().draw(sys.argv[1] if len(sys.argv) > 1 else None))
