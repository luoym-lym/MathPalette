"""Frozen question Plane178; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane178:

    def __init__(self):
        self.id = 'Plane178'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:225'
        self.question = 'A box contains seven blocks. What is the minimum number of blocks that must be moved to rearrange them so that another block can be placed in the box?'
        self.answer = '3'
        self.answer_type = 'number'
        self.query = self.question
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane178.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-0.12667099149054195, 5.130592591748275], ylim=[-0.12979189053362905, 5.127471692705188], axes_position=[0.05, 0.05, 0.9, 0.9], coordinate_axes=False) as c:
            c.path([[0.0, 0.0], [5.0, 0.0], [5.0, 5.0], [0.0, 5.0], [0.0, 0.0]], [1, 2, 2, 2, 79], id='box', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.6, 0.6, 0.6, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[0.0, 0.0], [5.0, 0.0], [5.0, 5.0], [0.0, 5.0], [0.0, 0.0]], [1, 2, 2, 2, 79], id='box', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[0.0, 2.0], [1.0, 2.0], [1.0, 5.0], [0.0, 5.0], [0.0, 2.0]], [1, 2, 2, 2, 79], id='block0', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.8666666666666667, 0.8666666666666667, 0.8666666666666667, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[0.0, 2.0], [1.0, 2.0], [1.0, 5.0], [0.0, 5.0], [0.0, 2.0]], [1, 2, 2, 2, 79], id='block0', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[1.0, 4.0], [4.0, 4.0], [4.0, 5.0], [1.0, 5.0], [1.0, 4.0]], [1, 2, 2, 2, 79], id='block1', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.8666666666666667, 0.8666666666666667, 0.8666666666666667, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[1.0, 4.0], [4.0, 4.0], [4.0, 5.0], [1.0, 5.0], [1.0, 4.0]], [1, 2, 2, 2, 79], id='block1', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[1.0, 3.0], [4.0, 3.0], [4.0, 4.0], [1.0, 4.0], [1.0, 3.0]], [1, 2, 2, 2, 79], id='block2', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.8666666666666667, 0.8666666666666667, 0.8666666666666667, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[1.0, 3.0], [4.0, 3.0], [4.0, 4.0], [1.0, 4.0], [1.0, 3.0]], [1, 2, 2, 2, 79], id='block2', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[4.0, 2.0], [5.0, 2.0], [5.0, 5.0], [4.0, 5.0], [4.0, 2.0]], [1, 2, 2, 2, 79], id='block3', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.8666666666666667, 0.8666666666666667, 0.8666666666666667, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[4.0, 2.0], [5.0, 2.0], [5.0, 5.0], [4.0, 5.0], [4.0, 2.0]], [1, 2, 2, 2, 79], id='block3', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[1.0, 0.0], [2.0, 0.0], [2.0, 3.0], [1.0, 3.0], [1.0, 0.0]], [1, 2, 2, 2, 79], id='block4', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.8666666666666667, 0.8666666666666667, 0.8666666666666667, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[1.0, 0.0], [2.0, 0.0], [2.0, 3.0], [1.0, 3.0], [1.0, 0.0]], [1, 2, 2, 2, 79], id='block4', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[2.0, 1.0], [5.0, 1.0], [5.0, 2.0], [2.0, 2.0], [2.0, 1.0]], [1, 2, 2, 2, 79], id='block5', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.8666666666666667, 0.8666666666666667, 0.8666666666666667, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[2.0, 1.0], [5.0, 1.0], [5.0, 2.0], [2.0, 2.0], [2.0, 1.0]], [1, 2, 2, 2, 79], id='block5', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[2.0, 0.0], [5.0, 0.0], [5.0, 1.0], [2.0, 1.0], [2.0, 0.0]], [1, 2, 2, 2, 79], id='block6', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.8666666666666667, 0.8666666666666667, 0.8666666666666667, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[2.0, 0.0], [5.0, 0.0], [5.0, 1.0], [2.0, 1.0], [2.0, 0.0]], [1, 2, 2, 2, 79], id='block6', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane178().draw(sys.argv[1] if len(sys.argv) > 1 else None))
