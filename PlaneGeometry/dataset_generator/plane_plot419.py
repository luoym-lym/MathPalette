"""Frozen question Plane419; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane419:

    def __init__(self):
        self.id = 'Plane419'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:1806'
        self.question = 'A rectangular sheet of paper which measures $6 \\mathrm{~cm} \\times 12 \\mathrm{~cm}$ is folded along its diagonal (Diagram A). The shaded areas in Diagram B are then cut off and the paper is unfolded leaving the rhombus shown in Diagram C. What is the length of the side of the rhombus?\nChoices:\nA:$\\frac{7}{2} \\sqrt{5} \\mathrm{~cm}$\nB:$7.35 \\mathrm{~cm}$\nC:$7.5 \\mathrm{~cm}$\nD:$7.85 \\mathrm{~cm}$\nE:$8.1 \\mathrm{~cm}$'
        self.answer = 'C'
        self.answer_type = 'choice'
        self.choices = {'A': '$\\frac{7}{2} \\sqrt{5} \\mathrm{~cm}$',
         'B': '$7.35 \\mathrm{~cm}$',
         'C': '$7.5 \\mathrm{~cm}$',
         'D': '$7.85 \\mathrm{~cm}$',
         'E': '$8.1 \\mathrm{~cm}$'}
        self.query = self.question
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane419.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-1.3051729353236858, 55.30517293532368], ylim=[-25.041284046434797, 31.569061824212575], axes_position=[0.050000000000000114, 0.05, 0.8999999999999998, 0.9], coordinate_axes=False) as c:
            c.path([[0.0, 0.0], [12.0, 0.0], [12.0, 6.0], [0.0, 0.0]], [1, 2, 2, 79], id='o0', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45], linewidth=0.0, capstyle='butt')
            c.path([[0.0, 0.0], [12.0, 0.0], [12.0, 6.0], [0.0, 0.0]], [1, 2, 2, 79], id='o0', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.line([[0.0, 0.0], [0.0, 6.0]], id='o1')
            c.line([[0.0, 6.0], [4.5, 6.0]], id='o2')
            c.path([[0.0, 0.0], [7.2, 9.6], [12.0, 6.0], [0.0, 0.0]], [1, 2, 2, 79], id='o3', facecolor=[0.0, 0.0, 0.0, 0.0], capstyle='butt')
            c.path([[21.0, 0.0], [21.0, 6.0], [25.5, 6.0], [21.0, 0.0]], [1, 2, 2, 79], id='o4', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45], linewidth=0.0, capstyle='butt')
            c.path([[21.0, 0.0], [21.0, 6.0], [25.5, 6.0], [21.0, 0.0]], [1, 2, 2, 79], id='o4', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[25.5, 6.0], [28.2, 9.6], [33.0, 6.0], [25.5, 6.0]], [1, 2, 2, 79], id='o5', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45], linewidth=0.0, capstyle='butt')
            c.path([[25.5, 6.0], [28.2, 9.6], [33.0, 6.0], [25.5, 6.0]], [1, 2, 2, 79], id='o5', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            for object_id, points in [('o6', [[21.0, 0.0], [28.2, 9.6]]), ('o7', [[21.0, 0.0], [33.0, 6.0]]), ('o8', [[21.0, 6.0], [33.0, 6.0]])]:
                c.line(points, id=object_id)
            c.path([[42.0, 0.0], [46.5, 6.0], [54.0, 6.0], [49.5, 0.0], [42.0, 0.0]], [1, 2, 2, 2, 79], id='o9', facecolor=[0.0, 0.0, 0.0, 0.0], capstyle='butt')
            for object_id, text, anchor in [('t0', 'Diagram A', [6.0, -2.3]), ('t1', 'Diagram B', [27.0, -2.3]), ('t2', 'Diagram C', [48.0, -2.3])]:
                c.text(text, anchor, id=object_id, rotation_mode='default', offset_pt=[0, 0], annotation_clip=None)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane419().draw(sys.argv[1] if len(sys.argv) > 1 else None))
