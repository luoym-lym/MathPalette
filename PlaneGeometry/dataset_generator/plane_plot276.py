"""Frozen question Plane276; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane276:

    def __init__(self):
        self.id = 'Plane276'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:832'
        self.question = 'A square with perimeter $48 \\mathrm{~cm}$ is cut into two equally big pieces with one cut. They are fitted together to make a rectangle as shown in the diagram. How big is the perimeter of that rectangle?\nChoices:\nA:$24 \\mathrm{~cm}$\nB:$30 \\mathrm{~cm}$\nC:$48 \\mathrm{~cm}$\nD:$60 \\mathrm{~cm}$\nE:$72 \\mathrm{~cm}$'
        self.answer = 'D'
        self.answer_type = 'choice'
        self.choices = {'A': '$24 \\mathrm{~cm}$', 'B': '$30 \\mathrm{~cm}$', 'C': '$48 \\mathrm{~cm}$', 'D': '$60 \\mathrm{~cm}$', 'E': '$72 \\mathrm{~cm}$'}
        self.query = self.question
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane276.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-0.39032402927445453, 15.903790233651373], ylim=[-6.161524724055507, 10.13258953887032], axes_position=[0.05, 0.05, 0.9, 0.9], coordinate_axes=False) as c:
            c.path([[0.0, 0.0], [4.0, 0.0], [4.0, 4.0], [0.0, 4.0], [0.0, 0.0]], [1, 2, 2, 2, 79], id='o0', facecolor=[0.0, 0.0, 0.0, 0.0], capstyle='butt')
            c.line([[0.0, 2.0], [4.0, 2.0]], id='o1', linestyle=(0.0, [4.0, 3.0]))
            c.line([[4.7, 2.0], [6.8, 2.0]], id='o2')
            c.path([[6.8, 2.0], [6.4, 2.16], [6.4, 1.84], [6.8, 2.0]], [1, 2, 2, 79], id='o3', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.0, 0.0, 0.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[6.8, 2.0], [6.4, 2.16], [6.4, 1.84], [6.8, 2.0]], [1, 2, 2, 79], id='o3', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[7.5, 1.0], [15.5, 1.0], [15.5, 3.0], [7.5, 3.0], [7.5, 1.0]], [1, 2, 2, 2, 79], id='o4', facecolor=[0.0, 0.0, 0.0, 0.0], capstyle='butt')
            c.line([[11.5, 1.0], [11.5, 3.0]], id='o5', linestyle=(0.0, [4.0, 3.0]))
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane276().draw(sys.argv[1] if len(sys.argv) > 1 else None))
