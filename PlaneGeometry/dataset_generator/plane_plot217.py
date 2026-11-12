"""Frozen question Plane217; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane217:

    def __init__(self):
        self.id = 'Plane217'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:571'
        self.question = 'A piece of paper is folded, a hole is punched through it, and it is unfolded. The result is shown below.\nAlong which dotted line was the paper folded?\nChoices:\nA:A\nB:B\nC:C\nD:D\nE:E'
        self.answer = 'C'
        self.answer_type = 'choice'
        self.choices = {'A': 'A', 'B': 'B', 'C': 'C', 'D': 'D', 'E': 'E'}
        self.query = self.question
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane217.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=(-1.4453489548654161, 20.3311548245613), ylim=(-5.916018220009818, 15.860485559416897), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
            c.path([[8.0, 6.0], [12.0, 6.0], [12.0, 10.0], [8.0, 10.0], [8.0, 6.0]], [1, 2, 2, 2, 79], id='o0', capstyle='butt')
            for object_id, center, radius in [('o1', [9.0, 7.45], 0.09), ('o2', [9.0, 8.55], 0.09), ('o3', [11.0, 7.45], 0.09), ('o4', [11.0, 8.55], 0.09)]:
                c.circle(center, radius, id=object_id, facecolor=(0.0, 0.0, 0.0, 0), fill=False)
            c.path([[0.0, 0.0], [3.0, 0.0], [3.0, 3.0], [0.0, 3.0], [0.0, 0.0]], [1, 2, 2, 2, 79], id='o5', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[0.0, 0.0], [3.0, 0.0], [3.0, 3.0], [0.0, 3.0], [0.0, 0.0]], [1, 2, 2, 2, 79], id='o5', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.line([[0.0, 0.0], [3.0, 3.0]], id='o6', linestyle=(0.0, [4.0, 3.0]))
            c.line([[0.0, 3.0], [3.0, 0.0]], id='o7', linestyle=(0.0, [4.0, 3.0]))
            c.path([[4.2, 0.0], [7.2, 0.0], [7.2, 3.0], [4.2, 3.0], [4.2, 0.0]], [1, 2, 2, 2, 79], id='o8', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[4.2, 0.0], [7.2, 0.0], [7.2, 3.0], [4.2, 3.0], [4.2, 0.0]], [1, 2, 2, 2, 79], id='o8', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            for object_id, points in [('o9', [[4.95, 0.0], [4.95, 3.0]]), ('o10', [[5.7, 0.0], [5.7, 3.0]]), ('o11', [[6.45, 0.0], [6.45, 3.0]])]:
                c.line(points, id=object_id, linestyle=(0.0, [4.0, 3.0]))
            c.path([[8.4, 0.0], [11.4, 0.0], [11.4, 3.0], [8.4, 3.0], [8.4, 0.0]], [1, 2, 2, 2, 79], id='o12', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[8.4, 0.0], [11.4, 0.0], [11.4, 3.0], [8.4, 3.0], [8.4, 0.0]], [1, 2, 2, 2, 79], id='o12', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.line([[9.9, 0.0], [9.9, 3.0]], id='o13', linestyle=(0.0, [4.0, 3.0]))
            c.line([[8.4, 1.5], [11.4, 1.5]], id='o14', linestyle=(0.0, [4.0, 3.0]))
            c.path([[12.600000000000001, 0.0], [15.600000000000001, 0.0], [15.600000000000001, 3.0], [12.600000000000001, 3.0], [12.600000000000001, 0.0]], [1, 2, 2, 2, 79], id='o15', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[12.600000000000001, 0.0], [15.600000000000001, 0.0], [15.600000000000001, 3.0], [12.600000000000001, 3.0], [12.600000000000001, 0.0]], [1, 2, 2, 2, 79], id='o15', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            for object_id, points in [('o16', [[12.600000000000001, 0.0], [15.600000000000001, 3.0]]), ('o17', [[12.600000000000001, 1.5], [14.100000000000001, 3.0]]), ('o18', [[14.100000000000001, 0.0], [15.600000000000001, 1.5]])]:
                c.line(points, id=object_id, linestyle=(0.0, [4.0, 3.0]))
            c.path([[16.8, 0.0], [19.8, 0.0], [19.8, 3.0], [16.8, 3.0], [16.8, 0.0]], [1, 2, 2, 2, 79], id='o19', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[16.8, 0.0], [19.8, 0.0], [19.8, 3.0], [16.8, 3.0], [16.8, 0.0]], [1, 2, 2, 2, 79], id='o19', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.line([[17.8, 0.0], [17.8, 3.0]], id='o20', linestyle=(0.0, [4.0, 3.0]))
            c.line([[18.8, 0.0], [18.8, 3.0]], id='o21', linestyle=(0.0, [4.0, 3.0]))
            for object_id, text, anchor in [('t0', '(A)', (-0.5, 0.2)), ('t1', '(B)', (3.7, 0.2)), ('t2', '(C)', (7.9, 0.2)), ('t3', '(D)', (12.100000000000001, 0.2)), ('t4', '(E)', (16.3, 0.2))]:
                c.text(text, anchor, id=object_id, rotation_mode='default', offset_pt=(0, 0), annotation_clip=None)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane217().draw(sys.argv[1] if len(sys.argv) > 1 else None))
