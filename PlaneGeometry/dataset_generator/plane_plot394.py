"""Frozen question Plane394; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane394:

    def __init__(self):
        self.id = 'Plane394'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:1632'
        self.question = 'A $3 \\mathrm{~cm}$ wide strip is grey on one side and white on the other. The strip is folded so that it fits inside a rectangle of length $27 \\mathrm{~cm}$, as shown. The grey trapeziums are identical. What is the length of the original strip?\nChoices:\nA:$36 \\mathrm{~cm}$\nB:$48 \\mathrm{~cm}$\nC:$54 \\mathrm{~cm}$\nD:$57 \\mathrm{~cm}$\nE:$81 \\mathrm{~cm}$'
        self.answer = 'D'
        self.answer_type = 'choice'
        self.choices = {'A': '$36 \\mathrm{~cm}$', 'B': '$48 \\mathrm{~cm}$', 'C': '$54 \\mathrm{~cm}$', 'D': '$57 \\mathrm{~cm}$', 'E': '$81 \\mathrm{~cm}$'}
        self.query = self.question
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane394.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-5.284929651842361, 27.818672666194708], ylim=[-13.775688048022982, 19.327914270014087], axes_position=[0.05, 0.05, 0.9, 0.9], coordinate_axes=False) as c:
            c.path([[0.0, 6.0], [3.0, 9.0], [6.0, 9.0], [9.0, 6.0], [0.0, 6.0]], [1, 2, 2, 2, 79], id='o0', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45], linewidth=0.0, capstyle='butt')
            c.path([[0.0, 6.0], [3.0, 9.0], [6.0, 9.0], [9.0, 6.0], [0.0, 6.0]], [1, 2, 2, 2, 79], id='o0', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[12.0, 6.0], [15.0, 9.0], [18.0, 9.0], [21.0, 6.0], [12.0, 6.0]], [1, 2, 2, 2, 79], id='o1', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45], linewidth=0.0, capstyle='butt')
            c.path([[12.0, 6.0], [15.0, 9.0], [18.0, 9.0], [21.0, 6.0], [12.0, 6.0]], [1, 2, 2, 2, 79], id='o1', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[6.0, 3.0], [9.0, 0.0], [12.0, 0.0], [15.0, 3.0], [6.0, 3.0]], [1, 2, 2, 2, 79], id='o2', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45], linewidth=0.0, capstyle='butt')
            c.path([[6.0, 3.0], [9.0, 0.0], [12.0, 0.0], [15.0, 3.0], [6.0, 3.0]], [1, 2, 2, 2, 79], id='o2', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[18.0, 3.0], [21.0, 0.0], [24.0, 0.0], [27.0, 3.0], [18.0, 3.0]], [1, 2, 2, 2, 79], id='o3', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45], linewidth=0.0, capstyle='butt')
            c.path([[18.0, 3.0], [21.0, 0.0], [24.0, 0.0], [27.0, 3.0], [18.0, 3.0]], [1, 2, 2, 2, 79], id='o3', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            for object_id, points in [('o4', [[0.0, 0.0], [0.0, 6.0]]), ('o5', [[3.0, 0.0], [3.0, 6.0]]), ('o6', [[6.0, 3.0], [6.0, 6.0]]), ('o7', [[9.0, 3.0], [9.0, 6.0]]), ('o8', [[12.0, 3.0], [12.0, 6.0]]), ('o9', [[15.0, 3.0], [15.0, 6.0]]), ('o10', [[18.0, 3.0], [18.0, 6.0]]), ('o11', [[21.0, 3.0], [21.0, 6.0]]), ('o12', [[24.0, 3.0], [24.0, 9.0]]), ('o13', [[27.0, 3.0], [27.0, 9.0]]), ('o14', [[0.0, 0.0], [3.0, 0.0]]), ('o15', [[24.0, 9.0], [27.0, 9.0]])]:
                c.line(points, id=object_id)
            for object_id, points in [('o16', [[0.0, 9.0], [3.0, 9.0]]), ('o17', [[6.0, 9.0], [15.0, 9.0]]), ('o18', [[18.0, 9.0], [24.0, 9.0]]), ('o19', [[3.0, 0.0], [9.0, 0.0]]), ('o20', [[12.0, 0.0], [21.0, 0.0]]), ('o21', [[24.0, 0.0], [27.0, 0.0]]), ('o22', [[0.0, 6.0], [0.0, 9.0]]), ('o23', [[27.0, 0.0], [27.0, 3.0]]), ('o24', [[-1.8, 0.0], [-1.8, 6.0]])]:
                c.line(points, id=object_id, linestyle=(0.0, [4.0, 3.0]))
            c.line([[0.0, 0.0], [-1.8, 0.0]], id='o25')
            c.line([[0.0, 6.0], [-1.8, 6.0]], id='o26')
            c.line([[0.0, -2.2], [27.0, -2.2]], id='o27', linestyle=(0.0, [4.0, 3.0]))
            c.line([[0.0, 0.0], [0.0, -2.2]], id='o28')
            c.line([[27.0, 0.0], [27.0, -2.2]], id='o29')
            c.text('6 cm', [-3.3, 3.0], id='t0', rotation_mode='default', offset_pt=[0, 0], annotation_clip=None)
            c.text('27 cm', [13.5, -3.2], id='t1', rotation_mode='default', offset_pt=[0, 0], annotation_clip=None)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane394().draw(sys.argv[1] if len(sys.argv) > 1 else None))
