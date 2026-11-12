"""Frozen question Plane304; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane304:

    def __init__(self):
        self.id = 'Plane304'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:945'
        self.question = 'A sheet of paper is folded exactly in half and then exactly in half again, giving the shape shown. Which of the shapes P, Q or R could have been the original shape of the paper?\nChoices:\nA:only P\nB:only Q\nC:only R\nD:only P or Q\nE:any of P, Q or R'
        self.answer = 'E'
        self.answer_type = 'choice'
        self.choices = {'A': 'only P', 'B': 'only Q', 'C': 'only R', 'D': 'only P or Q', 'E': 'any of P, Q or R'}
        self.query = self.question
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane304.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=(-0.2939558539743805, 12.506906460497028), ylim=(-2.7835143288437343, 10.017347985627673), axes_position=(0.05, 0.05000000000000006, 0.9, 0.8999999999999999), coordinate_axes=False) as c:
            c.path([[7.0, 6.0], [9.0, 6.0], [7.0, 8.0], [7.0, 6.0]], [1, 2, 2, 79], id='o0', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[7.0, 6.0], [9.0, 6.0], [7.0, 8.0], [7.0, 6.0]], [1, 2, 2, 79], id='o0', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[0.0, 0.0], [4.0, 0.0], [4.0, 2.0], [0.0, 2.0], [0.0, 0.0]], [1, 2, 2, 2, 79], id='o1', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[0.0, 0.0], [4.0, 0.0], [4.0, 2.0], [0.0, 2.0], [0.0, 0.0]], [1, 2, 2, 2, 79], id='o1', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[4.6, 0.0], [7.4284271247461895, 0.0], [7.4284271247461895, 2.8284271247461903], [4.6, 2.8284271247461903], [4.6, 0.0]], [1, 2, 2, 2, 79], id='o2', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[4.6, 0.0], [7.4284271247461895, 0.0], [7.4284271247461895, 2.8284271247461903], [4.6, 2.8284271247461903], [4.6, 0.0]], [1, 2, 2, 2, 79], id='o2', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[8.2, 0.0], [12.2, 0.0], [12.2, 4.0], [8.2, 0.0]], [1, 2, 2, 79], id='o3', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[8.2, 0.0], [12.2, 0.0], [12.2, 4.0], [8.2, 0.0]], [1, 2, 2, 79], id='o3', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            for object_id, text, anchor in [('t0', 'P', (2.0, -0.6)), ('t1', 'Q', (6.0, -0.6)), ('t2', 'R', (10.2, -0.6))]:
                c.text(text, anchor, id=object_id, rotation_mode='default', offset_pt=(0, 0), annotation_clip=None)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane304().draw(sys.argv[1] if len(sys.argv) > 1 else None))
