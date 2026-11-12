"""Frozen question Plane355; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane355:

    def __init__(self):
        self.id = 'Plane355'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:1216'
        self.question = 'A rectangular strip of paper of dimensions $4 \\mathrm{~cm} \\times 13 \\mathrm{~cm}$ is folded as shown in the diagram. 2 rectangles are formed with areas $P$ and $Q$ where $P=2 Q$. What is the value of $x$?\nChoices:\nA:$5 \\mathrm{~cm}$\nB:$5.5 \\mathrm{~cm}$\nC:$6 \\mathrm{~cm}$\nD:$6.5 \\mathrm{~cm}$\nE:$4 \\sqrt{2} \\mathrm{~cm}$'
        self.answer = 'C'
        self.answer_type = 'choice'
        self.choices = {'A': '$5 \\mathrm{~cm}$', 'B': '$5.5 \\mathrm{~cm}$', 'C': '$6 \\mathrm{~cm}$', 'D': '$6.5 \\mathrm{~cm}$', 'E': '$4 \\sqrt{2} \\mathrm{~cm}$'}
        self.query = self.question
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane355.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-0.25023078545217103, 10.270463227208014], ylim=[-2.3970325394934786, 8.123661473166706], axes_position=[0.05, 0.05, 0.9, 0.9], coordinate_axes=False) as c:
            c.path([[0.0, 0.0], [6.0, 0.0], [6.0, 4.0], [0.0, 4.0], [0.0, 0.0]], [1, 2, 2, 2, 79], id='o0', facecolor=[0.0, 0.0, 0.0, 0.0], capstyle='butt')
            c.path([[6.0, 4.0], [10.0, 4.0], [10.0, 7.0], [6.0, 7.0], [6.0, 4.0]], [1, 2, 2, 2, 79], id='o1', facecolor=[0.0, 0.0, 0.0, 0.0], capstyle='butt')
            c.line([[6.0, 0.0], [10.0, 4.0]], id='o2')
            c.line([[6.0, 0.0], [10.0, 0.0]], id='o3', linestyle=(0.0, [4.0, 3.0]))
            c.line([[10.0, 0.0], [10.0, 4.0]], id='o4', linestyle=(0.0, [4.0, 3.0]))
            c.path([[6.591924335203039, 0.0], [6.591924335203039, 0.07773079149987468], [6.576613064181065, 0.1547057489832864], [6.546866778089438, 0.2265196362959229], [6.517120491997811, 0.2983335236085594], [6.473517681147967, 0.36358974159484886], [6.418553711371408, 0.41855371137140784]], [1, 4, 4, 4, 4, 4, 4], id='o5', zorder=3, facecolor=[0.0, 0.0, 0.0, 0], capstyle='butt', fill=False)
            c.line([[0.0, -0.7], [6.0, -0.7]], id='o6', linestyle=(0.0, [4.0, 3.0]))
            c.line([[0.0, 0.0], [0.0, -0.7]], id='o7')
            c.line([[6.0, 0.0], [6.0, -0.7]], id='o8')
            c.text('P', [3.0, 2.0], id='t0', rotation_mode='default', offset_pt=[0, 0], annotation_clip=None)
            c.text('Q', [8.0, 5.5], id='t1', rotation_mode='default', offset_pt=[0, 0], annotation_clip=None)
            c.text('45°', [6.0, 0.0], id='angle45', rotation_mode='default', offset_pt=[41.5745789630079, 17.220754456429038], annotation_clip=None)
            c.text('x', [3.0, -1.2], id='t3', rotation_mode='default', offset_pt=[0, 0], annotation_clip=None)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane355().draw(sys.argv[1] if len(sys.argv) > 1 else None))
