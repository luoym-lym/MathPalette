"""Frozen question Plane357; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane357:

    def __init__(self):
        self.id = 'Plane357'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:1240'
        self.question = 'Which of the following shapes cannot be cut into two trapeziums with one single straight line?\nChoices:\nA:A\nB:B\nC:C\nD:D\nE:E'
        self.answer = 'A'
        self.answer_type = 'choice'
        self.choices = {'A': 'A', 'B': 'B', 'C': 'C', 'D': 'D', 'E': 'E'}
        self.query = self.question
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane357.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=(-2.376795772500266, 21.559955494722487), ylim=(-9.22548370064007, 14.711267566582684), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
            c.path([[0.0, 5.0], [2.0, 5.0], [1.0, 6.732050807568877], [0.0, 5.0]], [1, 2, 2, 79], id='shape0', alpha=0.45, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[0.0, 5.0], [2.0, 5.0], [1.0, 6.732050807568877], [0.0, 5.0]], [1, 2, 2, 79], id='shape0', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[8.0, 5.0], [11.0, 5.0], [11.0, 7.0], [8.0, 7.0], [8.0, 5.0]], [1, 2, 2, 2, 79], id='shape1', alpha=0.45, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[8.0, 5.0], [11.0, 5.0], [11.0, 7.0], [8.0, 7.0], [8.0, 5.0]], [1, 2, 2, 2, 79], id='shape1', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[17.0, 5.0], [21.0, 5.0], [20.0, 7.0], [18.0, 7.0], [17.0, 5.0]], [1, 2, 2, 2, 79], id='shape2', alpha=0.45, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[17.0, 5.0], [21.0, 5.0], [20.0, 7.0], [18.0, 7.0], [17.0, 5.0]], [1, 2, 2, 2, 79], id='shape2', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[2.0, 0.0], [1.5, 0.8660254037844386], [0.5000000000000002, 0.8660254037844387], [0.0, 1.2246467991473532e-16], [0.49999999999999956, -0.8660254037844384], [1.5, -0.8660254037844386], [2.0, 0.0]], [1, 2, 2, 2, 2, 2, 79], id='shape3', alpha=0.45, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[2.0, 0.0], [1.5, 0.8660254037844386], [0.5000000000000002, 0.8660254037844387], [0.0, 1.2246467991473532e-16], [0.49999999999999956, -0.8660254037844384], [1.5, -0.8660254037844386], [2.0, 0.0]], [1, 2, 2, 2, 2, 2, 79], id='shape3', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[8.0, 0.0], [10.0, 0.0], [10.0, 2.0], [8.0, 2.0], [8.0, 0.0]], [1, 2, 2, 2, 79], id='shape4', alpha=0.45, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[8.0, 0.0], [10.0, 0.0], [10.0, 2.0], [8.0, 2.0], [8.0, 0.0]], [1, 2, 2, 2, 79], id='shape4', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            for object_id, text, anchor in [('label0', '(A) triangle', (1.0, 3.8)), ('label1', '(B) rectangle', (9.0, 3.8)), ('label2', '(C) trapezium', (18.0, 3.8)), ('label3', '(D) regular hexagon', (2.0, -1.2)), ('label4', '(E) square', (9.0, -1.2))]:
                c.text(text, anchor, id=object_id, rotation_mode='default', offset_pt=(0, 0), annotation_clip=None)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane357().draw(sys.argv[1] if len(sys.argv) > 1 else None))
