"""Frozen question Plane434; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane434:

    def __init__(self):
        self.id = 'Plane434'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:1953'
        self.question = 'Two identical rectangles with sides of length $3 \\mathrm{~cm}$ and $9 \\mathrm{~cm}$ are overlapping as in the diagram. What is the area of the overlap of the two rectangles?\nChoices:\nA:$12 \\mathrm{~cm}^{2}$\nB:$13.5 \\mathrm{~cm}^{2}$\nC:$14 \\mathrm{~cm}^{2}$\nD:$15 \\mathrm{~cm}^{2}$\nE:$16 \\mathrm{~cm}^{2}$'
        self.answer = 'D'
        self.answer_type = 'choice'
        self.choices = {'A': '$12 \\mathrm{~cm}^{2}$', 'B': '$13.5 \\mathrm{~cm}^{2}$', 'C': '$14 \\mathrm{~cm}^{2}$', 'D': '$15 \\mathrm{~cm}^{2}$', 'E': '$16 \\mathrm{~cm}^{2}$'}
        self.query = self.question
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane434.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-0.22394136191791336, 9.239866484323109], ylim=[-3.2319039231205107, 6.231903923120511], axes_position=[0.05, 0.05, 0.9, 0.9], coordinate_axes=False) as c:
            c.path([[0.0, 0.0], [5.0, 0.0], [9.0, 3.0], [4.0, 3.0], [0.0, 0.0]], [1, 2, 2, 2, 79], id='o0', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45], linewidth=0.0, capstyle='butt')
            c.path([[0.0, 0.0], [5.0, 0.0], [9.0, 3.0], [4.0, 3.0], [0.0, 0.0]], [1, 2, 2, 2, 79], id='o0', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[0.0, 0.0], [9.0, 0.0], [9.0, 3.0], [0.0, 3.0], [0.0, 0.0]], [1, 2, 2, 2, 79], id='o1', facecolor=[0.0, 0.0, 0.0, 0.0], capstyle='butt')
            c.path([[0.0, 0.0], [7.2, 5.4], [9.0, 3.0], [1.8, -2.4], [0.0, 0.0]], [1, 2, 2, 2, 79], id='o2', facecolor=[0.0, 0.0, 0.0, 0.0], capstyle='butt')
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane434().draw(sys.argv[1] if len(sys.argv) > 1 else None))
