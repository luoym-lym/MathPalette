"""Frozen question Plane403; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane403:

    def __init__(self):
        self.id = 'Plane403'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:1706'
        self.question = 'Which of the shapes below cannot be divided into two trapeziums by a single straight line?\nChoices:\nA:A\nB:B\nC:C\nD:D\nE:E'
        self.answer = 'A'
        self.answer_type = 'choice'
        self.choices = {'A': 'A', 'B': 'B', 'C': 'C', 'D': 'D', 'E': 'E'}
        self.query = self.question
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane403.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=(-1.8511407979336756, 27.177400548640847), ylim=(-14.44083077331605, 14.587710573258471), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
            c.path([[0.0, 0.0], [1.0, 2.0], [2.0, 0.0], [0.0, 0.0]], [1, 2, 2, 79], id='shape0', alpha=0.45, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[0.0, 0.0], [1.0, 2.0], [2.0, 0.0], [0.0, 0.0]], [1, 2, 2, 79], id='shape0', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[6.0, 0.0], [9.0, 0.0], [9.0, 2.0], [6.0, 2.0], [6.0, 0.0]], [1, 2, 2, 2, 79], id='shape1', alpha=0.45, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[6.0, 0.0], [9.0, 0.0], [9.0, 2.0], [6.0, 2.0], [6.0, 0.0]], [1, 2, 2, 2, 79], id='shape1', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[12.0, 0.0], [15.0, 0.0], [14.4, 2.0], [13.2, 2.0], [12.0, 0.0]], [1, 2, 2, 2, 79], id='shape2', alpha=0.45, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[12.0, 0.0], [15.0, 0.0], [14.4, 2.0], [13.2, 2.0], [12.0, 0.0]], [1, 2, 2, 2, 79], id='shape2', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[20.0, 1.0], [19.5, 1.8660254037844386], [18.5, 1.8660254037844388], [18.0, 1.0000000000000002], [18.5, 0.13397459621556163], [19.5, 0.1339745962155614], [20.0, 1.0]], [1, 2, 2, 2, 2, 2, 79], id='shape3', alpha=0.45, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[20.0, 1.0], [19.5, 1.8660254037844386], [18.5, 1.8660254037844388], [18.0, 1.0000000000000002], [18.5, 0.13397459621556163], [19.5, 0.1339745962155614], [20.0, 1.0]], [1, 2, 2, 2, 2, 2, 79], id='shape3', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[24.0, 0.0], [26.0, 0.0], [26.0, 2.0], [24.0, 2.0], [24.0, 0.0]], [1, 2, 2, 2, 79], id='shape4', alpha=0.45, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[24.0, 0.0], [26.0, 0.0], [26.0, 2.0], [24.0, 2.0], [24.0, 0.0]], [1, 2, 2, 2, 79], id='shape4', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            for object_id, text, anchor in [('name0', 'triangle', (1.0, -1.0)), ('letter0', 'A', (-0.9, 1.0)), ('name1', 'rectangle', (7.0, -1.0)), ('letter1', 'B', (5.1, 1.0)), ('name2', 'trapezium', (13.0, -1.0)), ('letter2', 'C', (11.1, 1.0)), ('name3', 'regular\nhexagon', (19.0, -1.0)), ('letter3', 'D', (17.1, 1.0)), ('name4', 'square', (25.0, -1.0)), ('letter4', 'E', (23.1, 1.0))]:
                c.text(text, anchor, id=object_id, rotation_mode='default', offset_pt=(0, 0), annotation_clip=None)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane403().draw(sys.argv[1] if len(sys.argv) > 1 else None))
