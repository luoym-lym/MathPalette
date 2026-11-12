"""Frozen question Plane145; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane145:

    def __init__(self):
        self.id = 'Plane145'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:40'
        self.question = 'Which shape cannot be seen in every picture?\nChoices:\nA:A\nB:B\nC:C\nD:D\nE:E'
        self.answer = 'D'
        self.answer_type = 'choice'
        self.choices = {'A': 'A', 'B': 'B', 'C': 'C', 'D': 'D', 'E': 'E'}
        self.query = self.question
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane145.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=(-2.24870317315286, 29.184403337977592), ylim=(-15.620169228460359, 15.812937282670092), axes_position=(0.05, 0.05000000000000006, 0.9, 0.8999999999999999), coordinate_axes=False) as c:
            c.path([[0.0, 0.0], [6.5, 0.0], [6.5, 5.0], [0.0, 5.0], [0.0, 0.0]], [1, 2, 2, 2, 79], id='panel1', capstyle='butt')
            c.circle([1.0, 3.7], 0.8, id='p1_big_circle0')
            c.circle([0.9, 1.2], 0.52, id='p1_small_circle1')
            c.path([[2.0, 1.5], [3.6, 1.5], [3.6, 3.6], [2.0, 3.6], [2.0, 1.5]], [1, 2, 2, 2, 79], id='p1_rectangle2', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[2.0, 1.5], [3.6, 1.5], [3.6, 3.6], [2.0, 3.6], [2.0, 1.5]], [1, 2, 2, 2, 79], id='p1_rectangle2', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[3.9, 3.1], [6.0, 3.1], [5.25, 4.3], [3.9, 3.1]], [1, 2, 2, 79], id='p1_small_triangle3', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[3.9, 3.1], [6.0, 3.1], [5.25, 4.3], [3.9, 3.1]], [1, 2, 2, 79], id='p1_small_triangle3', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[2.8, 0.4], [6.055, 0.4], [4.8925, 2.26], [2.8, 0.4]], [1, 2, 2, 79], id='p1_big_triangle4', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[2.8, 0.4], [6.055, 0.4], [4.8925, 2.26], [2.8, 0.4]], [1, 2, 2, 79], id='p1_big_triangle4', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[7.3, 0.0], [13.8, 0.0], [13.8, 5.0], [7.3, 5.0], [7.3, 0.0]], [1, 2, 2, 2, 79], id='panel2', capstyle='butt')
            for object_id, center, radius in [('p2_small_circle0', [8.1, 4.1], 0.52), ('p2_big_circle1', [12.2, 3.7], 0.8), ('p2_small_circle2', [10.3, 2.6], 0.52)]:
                c.circle(center, radius, id=object_id)
            c.path([[7.8, 0.9], [9.9, 0.9], [9.15, 2.1], [7.8, 0.9]], [1, 2, 2, 79], id='p2_small_triangle3', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[7.8, 0.9], [9.9, 0.9], [9.15, 2.1], [7.8, 0.9]], [1, 2, 2, 79], id='p2_small_triangle3', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[10.1, 0.4], [13.355, 0.4], [12.192499999999999, 2.26], [10.1, 0.4]], [1, 2, 2, 79], id='p2_big_triangle4', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[10.1, 0.4], [13.355, 0.4], [12.192499999999999, 2.26], [10.1, 0.4]], [1, 2, 2, 79], id='p2_big_triangle4', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[14.6, 0.0], [21.1, 0.0], [21.1, 5.0], [14.6, 5.0], [14.6, 0.0]], [1, 2, 2, 2, 79], id='panel3', capstyle='butt')
            c.path([[15.1, 2.6], [18.355, 2.6], [17.1925, 4.46], [15.1, 2.6]], [1, 2, 2, 79], id='p3_big_triangle0', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[15.1, 2.6], [18.355, 2.6], [17.1925, 4.46], [15.1, 2.6]], [1, 2, 2, 79], id='p3_big_triangle0', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[19.0, 2.5], [20.6, 2.5], [20.6, 4.6], [19.0, 4.6], [19.0, 2.5]], [1, 2, 2, 2, 79], id='p3_rectangle1', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[19.0, 2.5], [20.6, 2.5], [20.6, 4.6], [19.0, 4.6], [19.0, 2.5]], [1, 2, 2, 2, 79], id='p3_rectangle1', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.circle([15.799999999999999, 1.3], 0.8, id='p3_big_circle2')
            c.circle([17.8, 1.6], 0.52, id='p3_small_circle3')
            c.path([[18.5, 0.5], [20.6, 0.5], [19.85, 1.7], [18.5, 0.5]], [1, 2, 2, 79], id='p3_small_triangle4', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[18.5, 0.5], [20.6, 0.5], [19.85, 1.7], [18.5, 0.5]], [1, 2, 2, 79], id='p3_small_triangle4', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[21.9, 0.0], [28.4, 0.0], [28.4, 5.0], [21.9, 5.0], [21.9, 0.0]], [1, 2, 2, 2, 79], id='panel4', capstyle='butt')
            c.path([[22.4, 2.5], [24.0, 2.5], [24.0, 4.6], [22.4, 4.6], [22.4, 2.5]], [1, 2, 2, 2, 79], id='p4_rectangle0', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[22.4, 2.5], [24.0, 2.5], [24.0, 4.6], [22.4, 4.6], [22.4, 2.5]], [1, 2, 2, 2, 79], id='p4_rectangle0', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.circle([27.4, 4.1], 0.52, id='p4_small_circle1')
            c.path([[24.9, 2.6], [27.0, 2.6], [26.25, 3.8], [24.9, 2.6]], [1, 2, 2, 79], id='p4_small_triangle2', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[24.9, 2.6], [27.0, 2.6], [26.25, 3.8], [24.9, 2.6]], [1, 2, 2, 79], id='p4_small_triangle2', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[22.2, 0.4], [25.455, 0.4], [24.2925, 2.26], [22.2, 0.4]], [1, 2, 2, 79], id='p4_big_triangle3', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[22.2, 0.4], [25.455, 0.4], [24.2925, 2.26], [22.2, 0.4]], [1, 2, 2, 79], id='p4_big_triangle3', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            for object_id, center, radius in [('p4_big_circle4', [27.299999999999997, 1.4], 0.8), ('optionA', [1.0, -4.0], 0.52), ('optionB', [7.0, -4.0], 0.8)]:
                c.circle(center, radius, id=object_id)
            c.path([[13.0, -4.0], [15.1, -4.0], [14.35, -2.8], [13.0, -4.0]], [1, 2, 2, 79], id='optionC', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[13.0, -4.0], [15.1, -4.0], [14.35, -2.8], [13.0, -4.0]], [1, 2, 2, 79], id='optionC', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[19.0, -4.0], [20.6, -4.0], [20.6, -1.9], [19.0, -1.9], [19.0, -4.0]], [1, 2, 2, 2, 79], id='optionD', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[19.0, -4.0], [20.6, -4.0], [20.6, -1.9], [19.0, -1.9], [19.0, -4.0]], [1, 2, 2, 2, 79], id='optionD', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[25.0, -4.0], [28.255, -4.0], [27.0925, -2.14], [25.0, -4.0]], [1, 2, 2, 79], id='optionE', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[25.0, -4.0], [28.255, -4.0], [27.0925, -2.14], [25.0, -4.0]], [1, 2, 2, 79], id='optionE', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            for object_id, text, anchor in [('label0', '(A)', (-0.9, -4.3)), ('label1', '(B)', (5.1, -4.3)), ('label2', '(C)', (11.1, -4.3)), ('label3', '(D)', (17.1, -4.3)), ('label4', '(E)', (23.1, -4.3))]:
                c.text(text, anchor, id=object_id, rotation_mode='default', offset_pt=(0, 0), annotation_clip=None)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane145().draw(sys.argv[1] if len(sys.argv) > 1 else None))
