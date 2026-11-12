"""Frozen question Plane289; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane289:

    def __init__(self):
        self.id = 'Plane289'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:866'
        self.question = 'The arrangement shown is to be completed to form one large triangle using identical small triangles. What is the minimum number of small triangles that must be added?'
        self.answer = '9'
        self.answer_type = 'number'
        self.query = self.question
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane289.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=(-0.07705037288351635, 3.0764963425935368), ylim=(-2.0088524965915266, 1.1446942188855265), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
            c.path([[0.0, 0.0], [0.5, 0.8660254037844386], [1.0, 0.0], [0.0, 0.0]], [1, 2, 2, 79], id='triangle0', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[0.0, 0.0], [0.5, 0.8660254037844386], [1.0, 0.0], [0.0, 0.0]], [1, 2, 2, 79], id='triangle0', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[0.5, 0.8660254037844386], [1.5, 0.8660254037844386], [1.0, 0.0], [0.5, 0.8660254037844386]], [1, 2, 2, 79], id='triangle1', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[0.5, 0.8660254037844386], [1.5, 0.8660254037844386], [1.0, 0.0], [0.5, 0.8660254037844386]], [1, 2, 2, 79], id='triangle1', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[1.5, 0.8660254037844386], [1.0, 0.0], [2.0, 0.0], [1.5, 0.8660254037844386]], [1, 2, 2, 79], id='triangle2', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[1.5, 0.8660254037844386], [1.0, 0.0], [2.0, 0.0], [1.5, 0.8660254037844386]], [1, 2, 2, 79], id='triangle2', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[1.0, 0.0], [2.0, 0.0], [1.5, -0.8660254037844386], [1.0, 0.0]], [1, 2, 2, 79], id='triangle3', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[1.0, 0.0], [2.0, 0.0], [1.5, -0.8660254037844386], [1.0, 0.0]], [1, 2, 2, 79], id='triangle3', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[2.0, 0.0], [1.5, -0.8660254037844386], [2.5, -0.8660254037844386], [2.0, 0.0]], [1, 2, 2, 79], id='triangle4', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[2.0, 0.0], [1.5, -0.8660254037844386], [2.5, -0.8660254037844386], [2.0, 0.0]], [1, 2, 2, 79], id='triangle4', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[2.0, 0.0], [3.0, 0.0], [2.5, -0.8660254037844386], [2.0, 0.0]], [1, 2, 2, 79], id='triangle5', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[2.0, 0.0], [3.0, 0.0], [2.5, -0.8660254037844386], [2.0, 0.0]], [1, 2, 2, 79], id='triangle5', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[1.5, -0.8660254037844386], [2.5, -0.8660254037844386], [2.0, -1.7320508075688772], [1.5, -0.8660254037844386]], [1, 2, 2, 79], id='triangle6', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[1.5, -0.8660254037844386], [2.5, -0.8660254037844386], [2.0, -1.7320508075688772], [1.5, -0.8660254037844386]], [1, 2, 2, 79], id='triangle6', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane289().draw(sys.argv[1] if len(sys.argv) > 1 else None))
