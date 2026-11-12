"""Frozen question Plane386; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane386:

    def __init__(self):
        self.id = 'Plane386'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:1571'
        self.question = 'The diagram, which is not drawn to scale, shows a box measuring $5 \\mathrm{~cm}$ by $5 \\mathrm{~cm}$ containing seven bars, each measuring $1 \\mathrm{~cm}$ by $3 \\mathrm{~cm}$. What is the minimum number of bars that must be slid within the box to make room for one more bar?'
        self.answer = '3'
        self.answer_type = 'number'
        self.query = self.question
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane386.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-0.12391678307295706, 5.132241630732973], ylim=[-0.13224163073297301, 5.123916783072957], axes_position=[0.05, 0.05, 0.9, 0.9], coordinate_axes=False) as c:
            c.path([[0.0, 0.0], [1.0, 0.0], [1.0, 2.0], [0.0, 2.0], [0.0, 0.0]], [1, 2, 2, 2, 79], id='empty0', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45], linewidth=0.0, capstyle='butt')
            c.path([[0.0, 0.0], [1.0, 0.0], [1.0, 2.0], [0.0, 2.0], [0.0, 0.0]], [1, 2, 2, 2, 79], id='empty0', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[2.0, 2.0], [4.0, 2.0], [4.0, 3.0], [2.0, 3.0], [2.0, 2.0]], [1, 2, 2, 2, 79], id='empty1', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45], linewidth=0.0, capstyle='butt')
            c.path([[2.0, 2.0], [4.0, 2.0], [4.0, 3.0], [2.0, 3.0], [2.0, 2.0]], [1, 2, 2, 2, 79], id='empty1', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            for object_id, vertices, codes in [('bar0', [[0.0, 2.0], [1.0, 2.0], [1.0, 5.0], [0.0, 5.0], [0.0, 2.0]], [1, 2, 2, 2, 79]), ('bar1', [[1.0, 4.0], [4.0, 4.0], [4.0, 5.0], [1.0, 5.0], [1.0, 4.0]], [1, 2, 2, 2, 79]), ('bar2', [[1.0, 3.0], [4.0, 3.0], [4.0, 4.0], [1.0, 4.0], [1.0, 3.0]], [1, 2, 2, 2, 79]), ('bar3', [[4.0, 2.0], [5.0, 2.0], [5.0, 5.0], [4.0, 5.0], [4.0, 2.0]], [1, 2, 2, 2, 79]), ('bar4', [[1.0, 0.0], [2.0, 0.0], [2.0, 3.0], [1.0, 3.0], [1.0, 0.0]], [1, 2, 2, 2, 79]), ('bar5', [[2.0, 1.0], [5.0, 1.0], [5.0, 2.0], [2.0, 2.0], [2.0, 1.0]], [1, 2, 2, 2, 79]), ('bar6', [[2.0, 0.0], [5.0, 0.0], [5.0, 1.0], [2.0, 1.0], [2.0, 0.0]], [1, 2, 2, 2, 79]), ('box', [[0.0, 0.0], [5.0, 0.0], [5.0, 5.0], [0.0, 5.0], [0.0, 0.0]], [1, 2, 2, 2, 79])]:
                c.path(vertices, codes, id=object_id, facecolor=[0.0, 0.0, 0.0, 0.0], capstyle='butt')
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane386().draw(sys.argv[1] if len(sys.argv) > 1 else None))
