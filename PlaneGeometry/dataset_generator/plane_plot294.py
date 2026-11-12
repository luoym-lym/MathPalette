"""Frozen question Plane294; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane294:

    def __init__(self):
        self.id = 'Plane294'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:898'
        self.question = 'The figure shown on the right consists of one square part and eight rectangular parts. Each part is $8 \\mathrm{~cm}$ wide. All the parts are assembled to form one long rectangle of width $8 \\mathrm{~cm}$. How long is this rectangle?\nChoices:\nA:$150 \\mathrm{~cm}$\nB:$168 \\mathrm{~cm}$\nC:$196 \\mathrm{~cm}$\nD:$200 \\mathrm{~cm}$\nE:$232 \\mathrm{~cm}$'
        self.answer = 'D'
        self.answer_type = 'choice'
        self.choices = {'A': '$150 \\mathrm{~cm}$', 'B': '$168 \\mathrm{~cm}$', 'C': '$196 \\mathrm{~cm}$', 'D': '$200 \\mathrm{~cm}$', 'E': '$232 \\mathrm{~cm}$'}
        self.query = self.question
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane294.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=(-0.12667099149054195, 5.130592591748275), ylim=(-0.12979189053362905, 5.127471692705188), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
            c.path([[0.0, 1.0], [1.0, 1.0], [1.0, 5.0], [0.0, 5.0], [0.0, 1.0]], [1, 2, 2, 2, 79], id='part0', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[0.0, 1.0], [1.0, 1.0], [1.0, 5.0], [0.0, 5.0], [0.0, 1.0]], [1, 2, 2, 2, 79], id='part0', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[1.0, 4.0], [5.0, 4.0], [5.0, 5.0], [1.0, 5.0], [1.0, 4.0]], [1, 2, 2, 2, 79], id='part1', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[1.0, 4.0], [5.0, 4.0], [5.0, 5.0], [1.0, 5.0], [1.0, 4.0]], [1, 2, 2, 2, 79], id='part1', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[4.0, 0.0], [5.0, 0.0], [5.0, 4.0], [4.0, 4.0], [4.0, 0.0]], [1, 2, 2, 2, 79], id='part2', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[4.0, 0.0], [5.0, 0.0], [5.0, 4.0], [4.0, 4.0], [4.0, 0.0]], [1, 2, 2, 2, 79], id='part2', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[0.0, 0.0], [4.0, 0.0], [4.0, 1.0], [0.0, 1.0], [0.0, 0.0]], [1, 2, 2, 2, 79], id='part3', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[0.0, 0.0], [4.0, 0.0], [4.0, 1.0], [0.0, 1.0], [0.0, 0.0]], [1, 2, 2, 2, 79], id='part3', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[1.0, 2.0], [2.0, 2.0], [2.0, 4.0], [1.0, 4.0], [1.0, 2.0]], [1, 2, 2, 2, 79], id='part4', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[1.0, 2.0], [2.0, 2.0], [2.0, 4.0], [1.0, 4.0], [1.0, 2.0]], [1, 2, 2, 2, 79], id='part4', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[2.0, 3.0], [4.0, 3.0], [4.0, 4.0], [2.0, 4.0], [2.0, 3.0]], [1, 2, 2, 2, 79], id='part5', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[2.0, 3.0], [4.0, 3.0], [4.0, 4.0], [2.0, 4.0], [2.0, 3.0]], [1, 2, 2, 2, 79], id='part5', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[3.0, 1.0], [4.0, 1.0], [4.0, 3.0], [3.0, 3.0], [3.0, 1.0]], [1, 2, 2, 2, 79], id='part6', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[3.0, 1.0], [4.0, 1.0], [4.0, 3.0], [3.0, 3.0], [3.0, 1.0]], [1, 2, 2, 2, 79], id='part6', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[1.0, 1.0], [3.0, 1.0], [3.0, 2.0], [1.0, 2.0], [1.0, 1.0]], [1, 2, 2, 2, 79], id='part7', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[1.0, 1.0], [3.0, 1.0], [3.0, 2.0], [1.0, 2.0], [1.0, 1.0]], [1, 2, 2, 2, 79], id='part7', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[2.0, 2.0], [3.0, 2.0], [3.0, 3.0], [2.0, 3.0], [2.0, 2.0]], [1, 2, 2, 2, 79], id='part8', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[2.0, 2.0], [3.0, 2.0], [3.0, 3.0], [2.0, 3.0], [2.0, 2.0]], [1, 2, 2, 2, 79], id='part8', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane294().draw(sys.argv[1] if len(sys.argv) > 1 else None))
