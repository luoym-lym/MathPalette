"""Frozen question Plane243; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane243:

    def __init__(self):
        self.id = 'Plane243'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:687'
        self.question = 'Using the pieces $A, B, C, D$ and $E$ one can fill this shape completely: Which of the pieces lies on the dot?\nChoices:\nA:A\nB:B\nC:C\nD:D\nE:E'
        self.answer = 'E'
        self.answer_type = 'choice'
        self.choices = {'A': 'A', 'B': 'B', 'C': 'C', 'D': 'D', 'E': 'E'}
        self.query = self.question
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane243.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=(-2.0198108138658313, 23.594252237646113), ylim=(-8.329627045512648, 17.284436005999297), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
            c.path([[9.0, 5.0], [10.0, 5.0], [10.0, 6.0], [9.0, 6.0], [9.0, 5.0]], [1, 2, 2, 2, 79], id='target0', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[9.0, 5.0], [10.0, 5.0], [10.0, 6.0], [9.0, 6.0], [9.0, 5.0]], [1, 2, 2, 2, 79], id='target0', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[10.0, 5.0], [11.0, 5.0], [11.0, 6.0], [10.0, 6.0], [10.0, 5.0]], [1, 2, 2, 2, 79], id='target1', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[10.0, 5.0], [11.0, 5.0], [11.0, 6.0], [10.0, 6.0], [10.0, 5.0]], [1, 2, 2, 2, 79], id='target1', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[11.0, 5.0], [12.0, 5.0], [12.0, 6.0], [11.0, 6.0], [11.0, 5.0]], [1, 2, 2, 2, 79], id='target2', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[11.0, 5.0], [12.0, 5.0], [12.0, 6.0], [11.0, 6.0], [11.0, 5.0]], [1, 2, 2, 2, 79], id='target2', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[12.0, 5.0], [13.0, 5.0], [13.0, 6.0], [12.0, 6.0], [12.0, 5.0]], [1, 2, 2, 2, 79], id='target3', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[12.0, 5.0], [13.0, 5.0], [13.0, 6.0], [12.0, 6.0], [12.0, 5.0]], [1, 2, 2, 2, 79], id='target3', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[13.0, 5.0], [14.0, 5.0], [14.0, 6.0], [13.0, 6.0], [13.0, 5.0]], [1, 2, 2, 2, 79], id='target4', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[13.0, 5.0], [14.0, 5.0], [14.0, 6.0], [13.0, 6.0], [13.0, 5.0]], [1, 2, 2, 2, 79], id='target4', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[13.0, 6.0], [14.0, 6.0], [14.0, 7.0], [13.0, 7.0], [13.0, 6.0]], [1, 2, 2, 2, 79], id='target5', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[13.0, 6.0], [14.0, 6.0], [14.0, 7.0], [13.0, 7.0], [13.0, 6.0]], [1, 2, 2, 2, 79], id='target5', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[13.0, 7.0], [14.0, 7.0], [14.0, 8.0], [13.0, 8.0], [13.0, 7.0]], [1, 2, 2, 2, 79], id='target6', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[13.0, 7.0], [14.0, 7.0], [14.0, 8.0], [13.0, 8.0], [13.0, 7.0]], [1, 2, 2, 2, 79], id='target6', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[13.0, 8.0], [14.0, 8.0], [14.0, 9.0], [13.0, 9.0], [13.0, 8.0]], [1, 2, 2, 2, 79], id='target7', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[13.0, 8.0], [14.0, 8.0], [14.0, 9.0], [13.0, 9.0], [13.0, 8.0]], [1, 2, 2, 2, 79], id='target7', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.circle([12.2, 5.8], 0.08, id='target_dot', facecolor=(0.0, 0.0, 0.0, 1.0))
            c.line([[11.55, 7.0], [12.0, 6.2]], id='pointer_shaft')
            c.path([[12.0, 6.2], [11.72, 6.36], [12.02, 6.55], [12.0, 6.2]], [1, 2, 2, 79], id='pointer_head', zorder=1, edgecolor='none', facecolor=(0.0, 0.0, 0.0, 1.0), linewidth=0.0, capstyle='butt')
            c.path([[12.0, 6.2], [11.72, 6.36], [12.02, 6.55], [12.0, 6.2]], [1, 2, 2, 79], id='pointer_head', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[0.0, 0.0], [1.0, 1.0], [0.0, 3.0], [0.0, 0.0]], [1, 2, 2, 79], id='pieceA', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[0.0, 0.0], [1.0, 1.0], [0.0, 3.0], [0.0, 0.0]], [1, 2, 2, 79], id='pieceA', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.line([[0.0, 1.0], [1.0, 1.0]], id='grid0_0')
            c.line([[0.0, 2.0], [0.5, 2.0]], id='grid0_1')
            c.path([[5.0, 2.0], [6.0, 0.0], [6.0, 2.0], [5.0, 2.0]], [1, 2, 2, 79], id='pieceB', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[5.0, 2.0], [6.0, 0.0], [6.0, 2.0], [5.0, 2.0]], [1, 2, 2, 79], id='pieceB', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.line([[5.5, 1.0], [6.0, 1.0]], id='grid1_0')
            c.path([[10.0, 0.0], [12.0, 0.0], [12.0, 2.0], [10.0, 0.0]], [1, 2, 2, 79], id='pieceC', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[10.0, 0.0], [12.0, 0.0], [12.0, 2.0], [10.0, 0.0]], [1, 2, 2, 79], id='pieceC', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.line([[11.0, 0.0], [11.0, 1.0]], id='grid2_0')
            c.line([[11.0, 1.0], [12.0, 1.0]], id='grid2_1')
            c.path([[15.0, 0.0], [16.0, 0.0], [17.0, 1.0], [15.0, 1.0], [15.0, 0.0]], [1, 2, 2, 2, 79], id='pieceD', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[15.0, 0.0], [16.0, 0.0], [17.0, 1.0], [15.0, 1.0], [15.0, 0.0]], [1, 2, 2, 2, 79], id='pieceD', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.line([[16.0, 0.0], [16.0, 1.0]], id='grid3_0')
            c.path([[20.0, 0.0], [22.0, 0.0], [23.0, 1.0], [21.0, 1.0], [20.0, 0.0]], [1, 2, 2, 2, 79], id='pieceE', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[20.0, 0.0], [22.0, 0.0], [23.0, 1.0], [21.0, 1.0], [20.0, 0.0]], [1, 2, 2, 2, 79], id='pieceE', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.line([[21.0, 0.0], [21.0, 1.0]], id='grid4_0')
            c.line([[22.0, 0.0], [22.0, 1.0]], id='grid4_1')
            for object_id, text, anchor in [('label0', '(A)', (-0.9, 0.35)), ('label1', '(B)', (4.1, 0.35)), ('label2', '(C)', (9.1, 0.35)), ('label3', '(D)', (14.1, 0.35)), ('label4', '(E)', (19.1, 0.35))]:
                c.text(text, anchor, id=object_id, rotation_mode='default', offset_pt=(0, 0), annotation_clip=None)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane243().draw(sys.argv[1] if len(sys.argv) > 1 else None))
