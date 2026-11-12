"""Frozen question Plane339; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane339:

    def __init__(self):
        self.id = 'Plane339'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:1118'
        self.question = 'A $5 \\times 5$ square is covered with $1 \\times 1$ tiles. The design on each tile is made up of three dark triangles and one light triangle (see diagram). The triangles of neighbouring tiles always have the same colour where they join along an edge. The border of the large square is made of dark and light triangles. What is the smallest number of dark triangles that could be amongst them?'
        self.answer = '5'
        self.answer_type = 'number'
        self.query = self.question
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane339.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-0.024783909193338616, 1.0264477735678472], ylim=[-0.026447773567847388, 1.0247839091933384], axes_position=[0.05, 0.05, 0.9, 0.9], coordinate_axes=False) as c:
            c.path([[0.0, 0.0], [0.0, 1.0], [1.0, 1.0], [1.0, 0.0], [0.5, 0.5], [0.0, 0.0]], [1, 2, 2, 2, 2, 79], id='dark', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45], linewidth=0.0, capstyle='butt')
            c.path([[0.0, 0.0], [0.0, 1.0], [1.0, 1.0], [1.0, 0.0], [0.5, 0.5], [0.0, 0.0]], [1, 2, 2, 2, 2, 79], id='dark', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[0.0, 1.0], [1.0, 1.0], [1.0, 0.0], [0.0, 0.0], [0.0, 1.0]], [1, 2, 2, 2, 79], id='outline', facecolor=[0.0, 0.0, 0.0, 0.0], capstyle='butt')
            c.line([[0.0, 1.0], [1.0, 0.0]], id='diag1')
            c.line([[0.0, 0.0], [1.0, 1.0]], id='diag2')
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane339().draw(sys.argv[1] if len(sys.argv) > 1 else None))
