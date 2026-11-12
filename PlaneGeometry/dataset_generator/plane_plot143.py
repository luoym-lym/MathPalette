"""Frozen question Plane143; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane143:

    def __init__(self):
        self.id = 'Plane143'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:34'
        self.question = 'A rectangle is cut into two pieces. One piece is shown here:\nWhat does the other piece look like?\nChoices:\nA:A\nB:B\nC:C\nD:D\nE:E'
        self.answer = 'E'
        self.answer_type = 'choice'
        self.choices = {'A': 'A', 'B': 'B', 'C': 'C', 'D': 'D', 'E': 'E'}
        self.query = self.question
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane143.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=(-3.9021095661614638, 49.24300703085192), ylim=(-16.633964504742366, 36.51115209227102), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
            c.path([[16.0, 16.0], [16.0, 20.0], [19.0, 17.0], [21.0, 19.0], [22.0, 18.0], [23.0, 19.0], [25.0, 17.0], [28.0, 20.0], [28.0, 16.0], [16.0, 16.0]], [1, 2, 2, 2, 2, 2, 2, 2, 2, 79], id='source', alpha=0.45, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[16.0, 16.0], [16.0, 20.0], [19.0, 17.0], [21.0, 19.0], [22.0, 18.0], [23.0, 19.0], [25.0, 17.0], [28.0, 20.0], [28.0, 16.0], [16.0, 16.0]], [1, 2, 2, 2, 2, 2, 2, 2, 2, 79], id='source', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[0.0, 8.0], [0.0, 9.0], [3.0, 12.0], [6.0, 9.0], [9.0, 12.0], [12.0, 9.0], [12.0, 8.0], [0.0, 8.0]], [1, 2, 2, 2, 2, 2, 2, 79], id='A', alpha=0.45, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[0.0, 8.0], [0.0, 9.0], [3.0, 12.0], [6.0, 9.0], [9.0, 12.0], [12.0, 9.0], [12.0, 8.0], [0.0, 8.0]], [1, 2, 2, 2, 2, 2, 2, 79], id='A', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[18.0, 8.0], [18.0, 9.3], [20.8, 12.0], [22.2, 10.7], [23.6, 12.0], [26.4, 9.3], [29.2, 12.0], [30.6, 10.7], [32.0, 12.0], [34.8, 9.3], [34.8, 8.0], [18.0, 8.0]], [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 79], id='B', alpha=0.45, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[18.0, 8.0], [18.0, 9.3], [20.8, 12.0], [22.2, 10.7], [23.6, 12.0], [26.4, 9.3], [29.2, 12.0], [30.6, 10.7], [32.0, 12.0], [34.8, 9.3], [34.8, 8.0], [18.0, 8.0]], [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 79], id='B', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[0.0, 0.0], [0.0, 1.0], [3.0, 4.0], [4.0, 3.0], [5.0, 4.0], [6.0, 3.0], [7.0, 4.0], [8.0, 3.0], [9.0, 4.0], [12.0, 1.0], [12.0, 0.0], [0.0, 0.0]], [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 79], id='C', alpha=0.45, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[0.0, 0.0], [0.0, 1.0], [3.0, 4.0], [4.0, 3.0], [5.0, 4.0], [6.0, 3.0], [7.0, 4.0], [8.0, 3.0], [9.0, 4.0], [12.0, 1.0], [12.0, 0.0], [0.0, 0.0]], [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 79], id='C', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[18.0, 0.0], [18.0, 1.0], [20.0, 2.3], [21.0, 1.4], [24.0, 4.0], [27.0, 1.4], [28.0, 2.2], [30.0, 1.0], [30.0, 0.0], [18.0, 0.0]], [1, 2, 2, 2, 2, 2, 2, 2, 2, 79], id='D', alpha=0.45, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[18.0, 0.0], [18.0, 1.0], [20.0, 2.3], [21.0, 1.4], [24.0, 4.0], [27.0, 1.4], [28.0, 2.2], [30.0, 1.0], [30.0, 0.0], [18.0, 0.0]], [1, 2, 2, 2, 2, 2, 2, 2, 2, 79], id='D', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[36.0, 0.0], [36.0, 1.0], [39.0, 4.0], [41.0, 2.0], [42.0, 3.0], [43.0, 2.0], [45.0, 4.0], [48.0, 1.0], [48.0, 0.0], [36.0, 0.0]], [1, 2, 2, 2, 2, 2, 2, 2, 2, 79], id='E', alpha=0.45, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[36.0, 0.0], [36.0, 1.0], [39.0, 4.0], [41.0, 2.0], [42.0, 3.0], [43.0, 2.0], [45.0, 4.0], [48.0, 1.0], [48.0, 0.0], [36.0, 0.0]], [1, 2, 2, 2, 2, 2, 2, 2, 2, 79], id='E', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            for object_id, text, anchor in [('label0', '(A)', (-1.6, 8.5)), ('label1', '(B)', (16.4, 8.5)), ('label2', '(C)', (-1.6, 0.5)), ('label3', '(D)', (16.4, 0.5)), ('label4', '(E)', (34.4, 0.5))]:
                c.text(text, anchor, id=object_id, rotation_mode='default', offset_pt=(0, 0), annotation_clip=None)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane143().draw(sys.argv[1] if len(sys.argv) > 1 else None))
