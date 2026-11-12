"""Frozen question Plane308; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane308:

    def __init__(self):
        self.id = 'Plane308'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:960'
        self.question = 'Six points are placed and numbered as shown on the right. Two triangles are drawn: one by connecting the even numbered points, and one by connecting the odd numbered points. Which of the following shapes is the result?\nChoices:\nA:A\nB:B\nC:C\nD:D\nE:E'
        self.answer = 'E'
        self.answer_type = 'choice'
        self.choices = {'A': 'A', 'B': 'B', 'C': 'C', 'D': 'D', 'E': 'E'}
        self.query = self.question
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane308.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=(-2.741648736260336, 21.60590377298287), ylim=(-8.988760979535469, 15.358791529707736), axes_position=(0.05, 0.05000000000000006, 0.9, 0.8999999999999999), coordinate_axes=False) as c:
            for object_id, center, radius in [('source_dot1', [9.0, 6.732050807568877], 0.04), ('source_dot2', [8.0, 5.0], 0.04), ('source_dot6', [9.0, 3.267949192431123], 0.04), ('source_dot3', [11.0, 3.267949192431123], 0.04), ('source_dot4', [12.0, 5.0], 0.04), ('source_dot5', [11.0, 6.732050807568877], 0.04)]:
                c.circle(center, radius, id=object_id, facecolor=(0.0, 0.0, 0.0, 1.0))
            c.path([[-0.5, 0.8660254037844386], [-1.0, 0.0], [0.5, -0.8660254037844386], [-0.5, 0.8660254037844386]], [1, 2, 2, 79], id='option0_0', alpha=0.5, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[-0.5, 0.8660254037844386], [-1.0, 0.0], [0.5, -0.8660254037844386], [-0.5, 0.8660254037844386]], [1, 2, 2, 79], id='option0_0', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[0.5, 0.8660254037844386], [1.0, 0.0], [-0.5, -0.8660254037844386], [0.5, 0.8660254037844386]], [1, 2, 2, 79], id='option0_1', alpha=0.5, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[0.5, 0.8660254037844386], [1.0, 0.0], [-0.5, -0.8660254037844386], [0.5, 0.8660254037844386]], [1, 2, 2, 79], id='option0_1', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            for object_id, center, radius in [('dot0_1', [-0.5, 0.8660254037844386], 0.04), ('dot0_2', [-1.0, 0.0], 0.04), ('dot0_6', [-0.5, -0.8660254037844386], 0.04), ('dot0_3', [0.5, -0.8660254037844386], 0.04), ('dot0_4', [1.0, 0.0], 0.04), ('dot0_5', [0.5, 0.8660254037844386], 0.04)]:
                c.circle(center, radius, id=object_id, facecolor=(0.0, 0.0, 0.0, 1.0))
            c.path([[4.5, 0.8660254037844386], [5.5, 0.8660254037844386], [4.5, -0.8660254037844386], [4.5, 0.8660254037844386]], [1, 2, 2, 79], id='option1_0', alpha=0.5, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[4.5, 0.8660254037844386], [5.5, 0.8660254037844386], [4.5, -0.8660254037844386], [4.5, 0.8660254037844386]], [1, 2, 2, 79], id='option1_0', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[4.0, 0.0], [6.0, 0.0], [5.5, -0.8660254037844386], [4.0, 0.0]], [1, 2, 2, 79], id='option1_1', alpha=0.5, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[4.0, 0.0], [6.0, 0.0], [5.5, -0.8660254037844386], [4.0, 0.0]], [1, 2, 2, 79], id='option1_1', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            for object_id, center, radius in [('dot1_1', [4.5, 0.8660254037844386], 0.04), ('dot1_2', [4.0, 0.0], 0.04), ('dot1_6', [4.5, -0.8660254037844386], 0.04), ('dot1_3', [5.5, -0.8660254037844386], 0.04), ('dot1_4', [6.0, 0.0], 0.04), ('dot1_5', [5.5, 0.8660254037844386], 0.04)]:
                c.circle(center, radius, id=object_id, facecolor=(0.0, 0.0, 0.0, 1.0))
            c.path([[9.5, 0.8660254037844386], [9.0, 0.0], [11.0, 0.0], [9.5, 0.8660254037844386]], [1, 2, 2, 79], id='option2_0', alpha=0.5, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[9.5, 0.8660254037844386], [9.0, 0.0], [11.0, 0.0], [9.5, 0.8660254037844386]], [1, 2, 2, 79], id='option2_0', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[10.5, 0.8660254037844386], [9.5, -0.8660254037844386], [10.5, -0.8660254037844386], [10.5, 0.8660254037844386]], [1, 2, 2, 79], id='option2_1', alpha=0.5, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[10.5, 0.8660254037844386], [9.5, -0.8660254037844386], [10.5, -0.8660254037844386], [10.5, 0.8660254037844386]], [1, 2, 2, 79], id='option2_1', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            for object_id, center, radius in [('dot2_1', [9.5, 0.8660254037844386], 0.04), ('dot2_2', [9.0, 0.0], 0.04), ('dot2_6', [9.5, -0.8660254037844386], 0.04), ('dot2_3', [10.5, -0.8660254037844386], 0.04), ('dot2_4', [11.0, 0.0], 0.04), ('dot2_5', [10.5, 0.8660254037844386], 0.04)]:
                c.circle(center, radius, id=object_id, facecolor=(0.0, 0.0, 0.0, 1.0))
            c.path([[14.5, 0.8660254037844386], [16.0, 0.0], [15.5, -0.8660254037844386], [14.5, 0.8660254037844386]], [1, 2, 2, 79], id='option3_0', alpha=0.5, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[14.5, 0.8660254037844386], [16.0, 0.0], [15.5, -0.8660254037844386], [14.5, 0.8660254037844386]], [1, 2, 2, 79], id='option3_0', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[15.5, 0.8660254037844386], [14.0, 0.0], [14.5, -0.8660254037844386], [15.5, 0.8660254037844386]], [1, 2, 2, 79], id='option3_1', alpha=0.5, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[15.5, 0.8660254037844386], [14.0, 0.0], [14.5, -0.8660254037844386], [15.5, 0.8660254037844386]], [1, 2, 2, 79], id='option3_1', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            for object_id, center, radius in [('dot3_1', [14.5, 0.8660254037844386], 0.04), ('dot3_2', [14.0, 0.0], 0.04), ('dot3_6', [14.5, -0.8660254037844386], 0.04), ('dot3_3', [15.5, -0.8660254037844386], 0.04), ('dot3_4', [16.0, 0.0], 0.04), ('dot3_5', [15.5, 0.8660254037844386], 0.04)]:
                c.circle(center, radius, id=object_id, facecolor=(0.0, 0.0, 0.0, 1.0))
            c.path([[19.5, 0.8660254037844386], [20.5, 0.8660254037844386], [20.5, -0.8660254037844386], [19.5, 0.8660254037844386]], [1, 2, 2, 79], id='option4_0', alpha=0.5, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[19.5, 0.8660254037844386], [20.5, 0.8660254037844386], [20.5, -0.8660254037844386], [19.5, 0.8660254037844386]], [1, 2, 2, 79], id='option4_0', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[19.0, 0.0], [21.0, 0.0], [19.5, -0.8660254037844386], [19.0, 0.0]], [1, 2, 2, 79], id='option4_1', alpha=0.5, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[19.0, 0.0], [21.0, 0.0], [19.5, -0.8660254037844386], [19.0, 0.0]], [1, 2, 2, 79], id='option4_1', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            for object_id, center, radius in [('dot4_1', [19.5, 0.8660254037844386], 0.04), ('dot4_2', [19.0, 0.0], 0.04), ('dot4_6', [19.5, -0.8660254037844386], 0.04), ('dot4_3', [20.5, -0.8660254037844386], 0.04), ('dot4_4', [21.0, 0.0], 0.04), ('dot4_5', [20.5, 0.8660254037844386], 0.04)]:
                c.circle(center, radius, id=object_id, facecolor=(0.0, 0.0, 0.0, 1.0))
            for object_id, text, anchor in [('label0', '1', (8.55, 7.132050807568877)), ('label1', '2', (7.55, 5.0)), ('label2', '6', (8.55, 2.867949192431123)), ('label3', '3', (11.45, 2.867949192431123)), ('label4', '4', (12.45, 5.0)), ('label5', '5', (11.45, 7.132050807568877)), ('label6', '(A)', (-1.7, -0.8)), ('label7', '(B)', (3.3, -0.8)), ('label8', '(C)', (8.3, -0.8)), ('label9', '(D)', (13.3, -0.8)), ('label10', '(E)', (18.3, -0.8))]:
                c.text(text, anchor, id=object_id, rotation_mode='default', offset_pt=(0, 0), annotation_clip=None)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane308().draw(sys.argv[1] if len(sys.argv) > 1 else None))
