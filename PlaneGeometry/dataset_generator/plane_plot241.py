"""Frozen question Plane241; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane241:

    def __init__(self):
        self.id = 'Plane241'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:682'
        self.question = 'Which two of the four jigsaw pieces shown can be joined to form the displayed square?\nChoices:\nA:1 and 2\nB:1 and 3\nC:2 and 3\nD:2 and 4\nE:1 and 4'
        self.answer = 'E'
        self.answer_type = 'choice'
        self.choices = {'A': '1 and 2', 'B': '1 and 3', 'C': '2 and 3', 'D': '2 and 4', 'E': '1 and 4'}
        self.query = self.question
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane241.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=(-0.5702673525116495, 21.570594836002897), ylim=(-9.529828748937145, 12.611033439577401), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
            for object_id, center, radius in [('dot0_0_0', [0.0, 0.0], 0.025), ('dot0_0_1', [0.0, 1.0], 0.025), ('dot0_0_2', [0.0, 2.0], 0.025), ('dot0_1_0', [1.0, 0.0], 0.025), ('dot0_1_1', [1.0, 1.0], 0.025)]:
                c.circle(center, radius, id=object_id)
            c.path([[0.0, 3.0], [1.0, 3.0], [1.0, 2.0], [2.0, 2.0], [2.0, 3.0], [3.0, 3.0], [3.0, 2.0], [3.0, 1.0], [2.0, 1.0], [2.0, 0.0], [3.0, 0.0], [4.0, 0.0], [4.0, 1.0], [4.0, 2.0], [4.0, 3.0], [4.0, 4.0], [3.0, 4.0], [2.0, 4.0], [1.0, 4.0], [0.0, 4.0], [0.0, 3.0]], [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 79], id='piece1', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[0.0, 3.0], [1.0, 3.0], [1.0, 2.0], [2.0, 2.0], [2.0, 3.0], [3.0, 3.0], [3.0, 2.0], [3.0, 1.0], [2.0, 1.0], [2.0, 0.0], [3.0, 0.0], [4.0, 0.0], [4.0, 1.0], [4.0, 2.0], [4.0, 3.0], [4.0, 4.0], [3.0, 4.0], [2.0, 4.0], [1.0, 4.0], [0.0, 4.0], [0.0, 3.0]], [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 79], id='piece1', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            for object_id, center, radius in [('dot1_2_4', [8.0, 4.0], 0.025), ('dot1_3_0', [9.0, 0.0], 0.025), ('dot1_3_4', [9.0, 4.0], 0.025)]:
                c.circle(center, radius, id=object_id)
            c.path([[6.0, 0.0], [7.0, 0.0], [8.0, 0.0], [8.0, 1.0], [9.0, 1.0], [9.0, 2.0], [9.0, 3.0], [8.0, 3.0], [8.0, 2.0], [7.0, 2.0], [7.0, 3.0], [7.0, 4.0], [6.0, 4.0], [6.0, 3.0], [6.0, 2.0], [6.0, 1.0], [6.0, 0.0]], [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 79], id='piece2', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[6.0, 0.0], [7.0, 0.0], [8.0, 0.0], [8.0, 1.0], [9.0, 1.0], [9.0, 2.0], [9.0, 3.0], [8.0, 3.0], [8.0, 2.0], [7.0, 2.0], [7.0, 3.0], [7.0, 4.0], [6.0, 4.0], [6.0, 3.0], [6.0, 2.0], [6.0, 1.0], [6.0, 0.0]], [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 79], id='piece2', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            for object_id, center, radius in [('dot2_0_0', [12.0, 0.0], 0.025), ('dot2_0_1', [12.0, 1.0], 0.025), ('dot2_0_2', [12.0, 2.0], 0.025)]:
                c.circle(center, radius, id=object_id)
            c.path([[12.0, 3.0], [13.0, 3.0], [13.0, 2.0], [14.0, 2.0], [14.0, 3.0], [15.0, 3.0], [15.0, 2.0], [15.0, 1.0], [14.0, 1.0], [13.0, 1.0], [13.0, 0.0], [14.0, 0.0], [15.0, 0.0], [16.0, 0.0], [16.0, 1.0], [16.0, 2.0], [16.0, 3.0], [16.0, 4.0], [15.0, 4.0], [14.0, 4.0], [13.0, 4.0], [12.0, 4.0], [12.0, 3.0]], [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 79], id='piece3', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[12.0, 3.0], [13.0, 3.0], [13.0, 2.0], [14.0, 2.0], [14.0, 3.0], [15.0, 3.0], [15.0, 2.0], [15.0, 1.0], [14.0, 1.0], [13.0, 1.0], [13.0, 0.0], [14.0, 0.0], [15.0, 0.0], [16.0, 0.0], [16.0, 1.0], [16.0, 2.0], [16.0, 3.0], [16.0, 4.0], [15.0, 4.0], [14.0, 4.0], [13.0, 4.0], [12.0, 4.0], [12.0, 3.0]], [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 79], id='piece3', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            for object_id, center, radius in [('dot3_0_4', [18.0, 4.0], 0.025), ('dot3_1_4', [19.0, 4.0], 0.025), ('dot3_2_4', [20.0, 4.0], 0.025), ('dot3_3_0', [21.0, 0.0], 0.025), ('dot3_3_4', [21.0, 4.0], 0.025)]:
                c.circle(center, radius, id=object_id)
            c.path([[18.0, 0.0], [19.0, 0.0], [20.0, 0.0], [20.0, 1.0], [21.0, 1.0], [21.0, 2.0], [21.0, 3.0], [20.0, 3.0], [20.0, 2.0], [19.0, 2.0], [19.0, 3.0], [18.0, 3.0], [18.0, 2.0], [18.0, 1.0], [18.0, 0.0]], [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 79], id='piece4', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[18.0, 0.0], [19.0, 0.0], [20.0, 0.0], [20.0, 1.0], [21.0, 1.0], [21.0, 2.0], [21.0, 3.0], [20.0, 3.0], [20.0, 2.0], [19.0, 2.0], [19.0, 3.0], [18.0, 3.0], [18.0, 2.0], [18.0, 1.0], [18.0, 0.0]], [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 79], id='piece4', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            for object_id, text, anchor in [('label0', '1', (1.8, -0.8)), ('label1', '2', (7.8, -0.8)), ('label2', '3', (13.8, -0.8)), ('label3', '4', (19.8, -0.8))]:
                c.text(text, anchor, id=object_id, rotation_mode='default', offset_pt=(0, 0), annotation_clip=None)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane241().draw(sys.argv[1] if len(sys.argv) > 1 else None))
