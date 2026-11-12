"""Frozen question Plane311; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane311:

    def __init__(self):
        self.id = 'Plane311'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:979'
        self.question = 'Which of the shapes cannot be split into two triangles using a single straight line?\nChoices:\nA:A\nB:B\nC:C\nD:D\nE:E'
        self.answer = 'A'
        self.answer_type = 'choice'
        self.choices = {'A': 'A', 'B': 'B', 'C': 'C', 'D': 'D', 'E': 'E'}
        self.query = self.question
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane311.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=(-2.62550890308016, 19.142023926517325), ylim=(-10.068593004779524, 11.69893982481796), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
            c.path([[1.0, 1.0], [0.5000000000000001, 1.8660254037844386], [-0.4999999999999998, 1.8660254037844388], [-1.0, 1.0000000000000002], [-0.5000000000000004, 0.13397459621556163], [0.5000000000000001, 0.1339745962155614], [1.0, 1.0]], [1, 2, 2, 2, 2, 2, 79], id='shape0', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[1.0, 1.0], [0.5000000000000001, 1.8660254037844386], [-0.4999999999999998, 1.8660254037844388], [-1.0, 1.0000000000000002], [-0.5000000000000004, 0.13397459621556163], [0.5000000000000001, 0.1339745962155614], [1.0, 1.0]], [1, 2, 2, 2, 2, 2, 79], id='shape0', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[3.0, 0.0], [6.0, 0.0], [6.0, 1.6], [3.0, 1.6], [3.0, 0.0]], [1, 2, 2, 2, 79], id='shape1', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[3.0, 0.0], [6.0, 0.0], [6.0, 1.6], [3.0, 1.6], [3.0, 0.0]], [1, 2, 2, 2, 79], id='shape1', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[8.0, 0.0], [11.0, 0.0], [10.0, 1.6], [8.8, 1.6], [8.0, 0.0]], [1, 2, 2, 2, 79], id='shape2', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[8.0, 0.0], [11.0, 0.0], [10.0, 1.6], [8.8, 1.6], [8.0, 0.0]], [1, 2, 2, 2, 79], id='shape2', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[13.0, 0.0], [15.4, 0.0], [14.2, 1.6], [13.0, 0.0]], [1, 2, 2, 79], id='shape3', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[13.0, 0.0], [15.4, 0.0], [14.2, 1.6], [13.0, 0.0]], [1, 2, 2, 79], id='shape3', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[17.0, 0.0], [18.6, 0.0], [18.6, 1.6], [17.0, 1.6], [17.0, 0.0]], [1, 2, 2, 2, 79], id='shape4', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[17.0, 0.0], [18.6, 0.0], [18.6, 1.6], [17.0, 1.6], [17.0, 0.0]], [1, 2, 2, 2, 79], id='shape4', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            for object_id, text, anchor in [('label0', '(A)', (-1.7, 0.0)), ('label1', '(B)', (2.2, 0.0)), ('label2', '(C)', (7.2, 0.0)), ('label3', '(D)', (12.2, 0.0)), ('label4', '(E)', (16.2, 0.0))]:
                c.text(text, anchor, id=object_id, rotation_mode='default', offset_pt=(0, 0), annotation_clip=None)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane311().draw(sys.argv[1] if len(sys.argv) > 1 else None))
