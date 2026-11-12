"""Frozen question Plane261; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane261:

    def __init__(self):
        self.id = 'Plane261'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:786'
        self.question = 'The figure should be rotated $180^{\\circ}$ around point $\\mathrm{F}$. What is the result?\nChoices:\nA:A\nB:B\nC:C\nD:D\nE:E'
        self.answer = 'C'
        self.answer_type = 'choice'
        self.choices = {'A': 'A', 'B': 'B', 'C': 'C', 'D': 'D', 'E': 'E'}
        self.query = self.question
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane261.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-0.45083861550911664, 18.471628880930734], ylim=[-5.97203860058319, 12.95042889585666], axes_position=[0.05, 0.05, 0.9, 0.9], coordinate_axes=False) as c:
            c.path([[8.0, 6.0], [9.0, 6.0], [9.0, 7.0], [8.0, 7.0], [8.0, 6.0]], [1, 2, 2, 2, 79], id='o0', facecolor=[0.0, 0.0, 0.0, 0.0], capstyle='butt')
            c.path([[9.0, 6.0], [10.0, 6.0], [10.0, 7.0], [9.0, 7.0], [9.0, 6.0]], [1, 2, 2, 2, 79], id='o1', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.31372549019607837, 0.31372549019607837, 0.31372549019607837, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[9.0, 6.0], [10.0, 6.0], [10.0, 7.0], [9.0, 7.0], [9.0, 6.0]], [1, 2, 2, 2, 79], id='o1', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[9.0, 7.0], [10.0, 7.0], [10.0, 8.0], [9.0, 8.0], [9.0, 7.0]], [1, 2, 2, 2, 79], id='o2', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.7333333333333333, 0.7333333333333333, 0.7333333333333333, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[9.0, 7.0], [10.0, 7.0], [10.0, 8.0], [9.0, 8.0], [9.0, 7.0]], [1, 2, 2, 2, 79], id='o2', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.circle([8.0, 6.0], 0.07, id='o3', facecolor=[0.0, 0.0, 0.0, 0], fill=False)
            c.path([[0.0, 1.0], [1.0, 1.0], [1.0, 2.0], [0.0, 2.0], [0.0, 1.0]], [1, 2, 2, 2, 79], id='o4', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.7333333333333333, 0.7333333333333333, 0.7333333333333333, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[0.0, 1.0], [1.0, 1.0], [1.0, 2.0], [0.0, 2.0], [0.0, 1.0]], [1, 2, 2, 2, 79], id='o4', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[1.0, 1.0], [2.0, 1.0], [2.0, 2.0], [1.0, 2.0], [1.0, 1.0]], [1, 2, 2, 2, 79], id='o5', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.31372549019607837, 0.31372549019607837, 0.31372549019607837, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[1.0, 1.0], [2.0, 1.0], [2.0, 2.0], [1.0, 2.0], [1.0, 1.0]], [1, 2, 2, 2, 79], id='o5', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[1.0, 0.0], [2.0, 0.0], [2.0, 1.0], [1.0, 1.0], [1.0, 0.0]], [1, 2, 2, 2, 79], id='o6', facecolor=[0.0, 0.0, 0.0, 0.0], capstyle='butt')
            c.circle([2.0, 0.0], 0.07, id='o7', facecolor=[0.0, 0.0, 0.0, 0], fill=False)
            c.path([[4.0, 0.0], [5.0, 0.0], [5.0, 1.0], [4.0, 1.0], [4.0, 0.0]], [1, 2, 2, 2, 79], id='o8', facecolor=[0.0, 0.0, 0.0, 0.0], capstyle='butt')
            c.path([[5.0, 0.0], [6.0, 0.0], [6.0, 1.0], [5.0, 1.0], [5.0, 0.0]], [1, 2, 2, 2, 79], id='o9', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.31372549019607837, 0.31372549019607837, 0.31372549019607837, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[5.0, 0.0], [6.0, 0.0], [6.0, 1.0], [5.0, 1.0], [5.0, 0.0]], [1, 2, 2, 2, 79], id='o9', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[5.0, 1.0], [6.0, 1.0], [6.0, 2.0], [5.0, 2.0], [5.0, 1.0]], [1, 2, 2, 2, 79], id='o10', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.7333333333333333, 0.7333333333333333, 0.7333333333333333, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[5.0, 1.0], [6.0, 1.0], [6.0, 2.0], [5.0, 2.0], [5.0, 1.0]], [1, 2, 2, 2, 79], id='o10', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.circle([4.0, 0.0], 0.07, id='o11', facecolor=[0.0, 0.0, 0.0, 0], fill=False)
            c.path([[8.0, 1.0], [9.0, 1.0], [9.0, 2.0], [8.0, 2.0], [8.0, 1.0]], [1, 2, 2, 2, 79], id='o12', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.31372549019607837, 0.31372549019607837, 0.31372549019607837, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[8.0, 1.0], [9.0, 1.0], [9.0, 2.0], [8.0, 2.0], [8.0, 1.0]], [1, 2, 2, 2, 79], id='o12', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[9.0, 1.0], [10.0, 1.0], [10.0, 2.0], [9.0, 2.0], [9.0, 1.0]], [1, 2, 2, 2, 79], id='o13', facecolor=[0.0, 0.0, 0.0, 0.0], capstyle='butt')
            c.path([[8.0, 0.0], [9.0, 0.0], [9.0, 1.0], [8.0, 1.0], [8.0, 0.0]], [1, 2, 2, 2, 79], id='o14', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.7333333333333333, 0.7333333333333333, 0.7333333333333333, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[8.0, 0.0], [9.0, 0.0], [9.0, 1.0], [8.0, 1.0], [8.0, 0.0]], [1, 2, 2, 2, 79], id='o14', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.circle([10.0, 2.0], 0.07, id='o15', facecolor=[0.0, 0.0, 0.0, 0], fill=False)
            c.path([[12.0, 0.0], [13.0, 0.0], [13.0, 1.0], [12.0, 1.0], [12.0, 0.0]], [1, 2, 2, 2, 79], id='o16', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.7333333333333333, 0.7333333333333333, 0.7333333333333333, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[12.0, 0.0], [13.0, 0.0], [13.0, 1.0], [12.0, 1.0], [12.0, 0.0]], [1, 2, 2, 2, 79], id='o16', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[13.0, 0.0], [14.0, 0.0], [14.0, 1.0], [13.0, 1.0], [13.0, 0.0]], [1, 2, 2, 2, 79], id='o17', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.31372549019607837, 0.31372549019607837, 0.31372549019607837, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[13.0, 0.0], [14.0, 0.0], [14.0, 1.0], [13.0, 1.0], [13.0, 0.0]], [1, 2, 2, 2, 79], id='o17', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[13.0, 1.0], [14.0, 1.0], [14.0, 2.0], [13.0, 2.0], [13.0, 1.0]], [1, 2, 2, 2, 79], id='o18', facecolor=[0.0, 0.0, 0.0, 0.0], capstyle='butt')
            c.circle([14.0, 2.0], 0.07, id='o19', facecolor=[0.0, 0.0, 0.0, 0], fill=False)
            c.path([[16.0, 1.0], [17.0, 1.0], [17.0, 2.0], [16.0, 2.0], [16.0, 1.0]], [1, 2, 2, 2, 79], id='o20', facecolor=[0.0, 0.0, 0.0, 0.0], capstyle='butt')
            c.path([[16.0, 0.0], [17.0, 0.0], [17.0, 1.0], [16.0, 1.0], [16.0, 0.0]], [1, 2, 2, 2, 79], id='o21', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.31372549019607837, 0.31372549019607837, 0.31372549019607837, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[16.0, 0.0], [17.0, 0.0], [17.0, 1.0], [16.0, 1.0], [16.0, 0.0]], [1, 2, 2, 2, 79], id='o21', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[17.0, 0.0], [18.0, 0.0], [18.0, 1.0], [17.0, 1.0], [17.0, 0.0]], [1, 2, 2, 2, 79], id='o22', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.7333333333333333, 0.7333333333333333, 0.7333333333333333, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[17.0, 0.0], [18.0, 0.0], [18.0, 1.0], [17.0, 1.0], [17.0, 0.0]], [1, 2, 2, 2, 79], id='o22', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.circle([16.0, 2.0], 0.07, id='o23', facecolor=[0.0, 0.0, 0.0, 0], fill=False)
            c.text('F', [8.0, 6.0], id='label_F0', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[-9.199471357281155, 0.0], annotation_clip=None)
            c.text('F', [2.0, 0.0], id='label_F1', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[9.199471357281165, -5.256840775589237], annotation_clip=None)
            c.text('A)', [1.0, -0.8], id='t2', rotation_mode='default', offset_pt=[0, 0], annotation_clip=None)
            c.text('F', [4.0, 0.0], id='label_F2', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[-9.199471357281165, -5.256840775589237], annotation_clip=None)
            c.text('B)', [5.0, -0.8], id='t4', rotation_mode='default', offset_pt=[0, 0], annotation_clip=None)
            c.text('F', [10.0, 2.0], id='label_F3', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[9.199471357281155, 6.571050969486546], annotation_clip=None)
            c.text('C)', [9.0, -0.8], id='t6', rotation_mode='default', offset_pt=[0, 0], annotation_clip=None)
            c.text('F', [14.0, 2.0], id='label_F4', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[9.199471357281155, 6.571050969486546], annotation_clip=None)
            c.text('D)', [13.0, -0.8], id='t8', rotation_mode='default', offset_pt=[0, 0], annotation_clip=None)
            c.text('F', [16.0, 2.0], id='label_F5', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[-9.199471357281155, 6.571050969486546], annotation_clip=None)
            c.text('E)', [17.0, -0.8], id='t10', rotation_mode='default', offset_pt=[0, 0], annotation_clip=None)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane261().draw(sys.argv[1] if len(sys.argv) > 1 else None))
