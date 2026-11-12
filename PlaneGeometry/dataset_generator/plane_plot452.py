"""Frozen question Plane452; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane452:

    def __init__(self):
        self.id = 'Plane452'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:2497'
        self.question = 'Five rectangles, $A$, $B$, $C$, $D$, and $E$, are arranged in a square as shown below. These rectangles have dimensions $1\\times6$, $2\\times4$, $5\\times6$, $2\\times7$, and $2\\times3$, respectively. (The figure is not drawn to scale.) Which of the five rectangles is the shaded one in the middle?\nChoices:\nA:A\nB:B\nC:C\nD:D\nE:E'
        self.answer = 'B'
        self.answer_type = 'choice'
        self.choices = {'A': 'A', 'B': 'B', 'C': 'C', 'D': 'D', 'E': 'E'}
        self.query = self.question
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane452.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-0.12391678307295706, 5.132241630732973], ylim=[-0.13224163073297301, 5.123916783072957], axes_position=[0.05, 0.05, 0.9, 0.9], coordinate_axes=False) as c:
            for object_id, vertices, codes in [('r0', [[0.0, 3.2], [3.8, 3.2], [3.8, 5.0], [0.0, 5.0], [0.0, 3.2]], [1, 2, 2, 2, 79]), ('r1', [[3.8, 1.8], [5.0, 1.8], [5.0, 5.0], [3.8, 5.0], [3.8, 1.8]], [1, 2, 2, 2, 79]), ('r2', [[2.15, 0.0], [5.0, 0.0], [5.0, 1.8], [2.15, 1.8], [2.15, 0.0]], [1, 2, 2, 2, 79]), ('r3', [[0.0, 0.0], [2.15, 0.0], [2.15, 3.2], [0.0, 3.2], [0.0, 0.0]], [1, 2, 2, 2, 79])]:
                c.path(vertices, codes, id=object_id, facecolor=[0.0, 0.0, 0.0, 0.0], capstyle='butt')
            c.path([[2.15, 1.8], [3.8, 1.8], [3.8, 3.2], [2.15, 3.2], [2.15, 1.8]], [1, 2, 2, 2, 79], id='r4', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45], linewidth=0.0, capstyle='butt')
            c.path([[2.15, 1.8], [3.8, 1.8], [3.8, 3.2], [2.15, 3.2], [2.15, 1.8]], [1, 2, 2, 2, 79], id='r4', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane452().draw(sys.argv[1] if len(sys.argv) > 1 else None))
