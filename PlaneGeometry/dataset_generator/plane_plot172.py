"""Frozen question Plane172; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane172:

    def __init__(self):
        self.id = 'Plane172'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:154'
        self.question = 'The parts shown are rearranged to form the kangaroo-shaped figure.\nWhich part is missing?\nChoices:\nA:A\nB:B\nC:C\nD:D\nE:E'
        self.answer = 'A'
        self.answer_type = 'choice'
        self.choices = {'A': 'A', 'B': 'B', 'C': 'C', 'D': 'D', 'E': 'E'}
        self.query = self.question
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane172.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=(-1.4521597015863072, 18.485111318252773), ylim=(-4.462575492302271, 15.47469552753681), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
            c.path([[0.0, 6.0], [0.0, 10.0], [2.0, 8.0], [0.0, 6.0]], [1, 2, 2, 79], id='squarepiece0', alpha=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[0.0, 6.0], [0.0, 10.0], [2.0, 8.0], [0.0, 6.0]], [1, 2, 2, 79], id='squarepiece0', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[0.0, 6.0], [4.0, 6.0], [2.0, 8.0], [0.0, 6.0]], [1, 2, 2, 79], id='squarepiece1', alpha=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[0.0, 6.0], [4.0, 6.0], [2.0, 8.0], [0.0, 6.0]], [1, 2, 2, 79], id='squarepiece1', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[2.0, 10.0], [4.0, 10.0], [4.0, 8.0], [2.0, 10.0]], [1, 2, 2, 79], id='squarepiece2', alpha=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[2.0, 10.0], [4.0, 10.0], [4.0, 8.0], [2.0, 10.0]], [1, 2, 2, 79], id='squarepiece2', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[1.0, 9.0], [3.0, 9.0], [2.0, 8.0], [1.0, 9.0]], [1, 2, 2, 79], id='squarepiece3', alpha=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[1.0, 9.0], [3.0, 9.0], [2.0, 8.0], [1.0, 9.0]], [1, 2, 2, 79], id='squarepiece3', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[3.0, 7.0], [4.0, 8.0], [4.0, 6.0], [3.0, 7.0]], [1, 2, 2, 79], id='squarepiece4', alpha=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[3.0, 7.0], [4.0, 8.0], [4.0, 6.0], [3.0, 7.0]], [1, 2, 2, 79], id='squarepiece4', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[2.0, 8.0], [3.0, 9.0], [4.0, 8.0], [3.0, 7.0], [2.0, 8.0]], [1, 2, 2, 2, 79], id='squarepiece5', alpha=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[2.0, 8.0], [3.0, 9.0], [4.0, 8.0], [3.0, 7.0], [2.0, 8.0]], [1, 2, 2, 2, 79], id='squarepiece5', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[0.0, 10.0], [2.0, 10.0], [3.0, 9.0], [1.0, 9.0], [0.0, 10.0]], [1, 2, 2, 2, 79], id='squarepiece6', alpha=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[0.0, 10.0], [2.0, 10.0], [3.0, 9.0], [1.0, 9.0], [0.0, 10.0]], [1, 2, 2, 2, 79], id='squarepiece6', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[7.585786437626905, 10.121320343559642], [9.0, 10.121320343559642], [9.0, 11.535533905932738], [7.585786437626905, 10.121320343559642]], [1, 2, 2, 79], id='kangaroopiece0', alpha=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[7.585786437626905, 10.121320343559642], [9.0, 10.121320343559642], [9.0, 11.535533905932738], [7.585786437626905, 10.121320343559642]], [1, 2, 2, 79], id='kangaroopiece0', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[9.0, 8.0], [9.0, 10.82842712474619], [11.82842712474619, 8.0], [9.0, 8.0]], [1, 2, 2, 79], id='kangaroopiece1', alpha=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[9.0, 8.0], [9.0, 10.82842712474619], [11.82842712474619, 8.0], [9.0, 8.0]], [1, 2, 2, 79], id='kangaroopiece1', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[8.0, 8.0], [9.0, 9.0], [9.0, 7.0], [8.0, 8.0]], [1, 2, 2, 79], id='kangaroopiece2', alpha=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[8.0, 8.0], [9.0, 9.0], [9.0, 7.0], [8.0, 8.0]], [1, 2, 2, 79], id='kangaroopiece2', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[9.707106781186548, 8.0], [12.535533905932738, 8.0], [12.535533905932738, 5.17157287525381], [9.707106781186548, 8.0]], [1, 2, 2, 79], id='kangaroopiece3', alpha=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[9.707106781186548, 8.0], [12.535533905932738, 8.0], [12.535533905932738, 5.17157287525381], [9.707106781186548, 8.0]], [1, 2, 2, 79], id='kangaroopiece3', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[10.535533905932738, 5.17157287525381], [11.535533905932738, 6.17157287525381], [12.535533905932738, 5.17157287525381], [11.535533905932738, 4.17157287525381], [10.535533905932738, 5.17157287525381]], [1, 2, 2, 2, 79], id='kangaroopiece4', alpha=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[10.535533905932738, 5.17157287525381], [11.535533905932738, 6.17157287525381], [12.535533905932738, 5.17157287525381], [11.535533905932738, 4.17157287525381], [10.535533905932738, 5.17157287525381]], [1, 2, 2, 2, 79], id='kangaroopiece4', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[11.121320343559642, 3.7573593128807143], [13.949747468305834, 3.7573593128807143], [12.535533905932738, 5.17157287525381], [11.121320343559642, 3.7573593128807143]], [1, 2, 2, 79], id='kangaroopiece5', alpha=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[11.121320343559642, 3.7573593128807143], [13.949747468305834, 3.7573593128807143], [12.535533905932738, 5.17157287525381], [11.121320343559642, 3.7573593128807143]], [1, 2, 2, 79], id='kangaroopiece5', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[5.4, 7.9], [5.75, 7.9], [5.75, 7.75], [6.5, 8.0], [5.75, 8.25], [5.75, 8.1], [5.4, 8.1], [5.4, 7.9]], [1, 2, 2, 2, 2, 2, 2, 79], id='rearrangement_arrow', edgecolor='none', facecolor=(0.0, 0.0, 0.0, 1.0), linewidth=0.0, capstyle='butt')
            c.path([[5.4, 7.9], [5.75, 7.9], [5.75, 7.75], [6.5, 8.0], [5.75, 8.25], [5.75, 8.1], [5.4, 8.1], [5.4, 7.9]], [1, 2, 2, 2, 2, 2, 2, 79], id='rearrangement_arrow', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[0.0, 1.0], [2.0, 1.0], [3.0, 0.0], [1.0, 0.0], [0.0, 1.0]], [1, 2, 2, 2, 79], id='option0', alpha=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[0.0, 1.0], [2.0, 1.0], [3.0, 0.0], [1.0, 0.0], [0.0, 1.0]], [1, 2, 2, 2, 79], id='option0', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[4.0, 1.0], [6.0, 1.0], [5.0, 0.0], [4.0, 1.0]], [1, 2, 2, 79], id='option1', alpha=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[4.0, 1.0], [6.0, 1.0], [5.0, 0.0], [4.0, 1.0]], [1, 2, 2, 79], id='option1', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[8.0, 1.0], [9.0, 2.0], [10.0, 1.0], [9.0, 0.0], [8.0, 1.0]], [1, 2, 2, 2, 79], id='option2', alpha=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[8.0, 1.0], [9.0, 2.0], [10.0, 1.0], [9.0, 0.0], [8.0, 1.0]], [1, 2, 2, 2, 79], id='option2', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[12.0, 1.0], [13.0, 2.0], [13.0, 0.0], [12.0, 1.0]], [1, 2, 2, 79], id='option3', alpha=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[12.0, 1.0], [13.0, 2.0], [13.0, 0.0], [12.0, 1.0]], [1, 2, 2, 79], id='option3', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[16.0, 2.0], [18.0, 2.0], [18.0, 0.0], [16.0, 2.0]], [1, 2, 2, 79], id='option4', alpha=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[16.0, 2.0], [18.0, 2.0], [18.0, 0.0], [16.0, 2.0]], [1, 2, 2, 79], id='option4', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            for object_id, text, anchor in [('label0', '(A)', (-0.6, -0.3)), ('label1', '(B)', (3.4, -0.3)), ('label2', '(C)', (7.4, -0.3)), ('label3', '(D)', (11.4, -0.3)), ('label4', '(E)', (15.4, -0.3))]:
                c.text(text, anchor, id=object_id, rotation_mode='default', offset_pt=(0, 0), annotation_clip=None)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane172().draw(sys.argv[1] if len(sys.argv) > 1 else None))
