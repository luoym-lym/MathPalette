"""Frozen question Plane490; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane490:

    def __init__(self):
        self.id = 'Plane490'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:2994'
        self.question = 'What is the angle of rotation in degrees about point $C$ that maps the darker figure to the lighter image?'
        self.answer = '180'
        self.answer_type = 'number'
        self.query = self.question
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane490.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-6.306743346479205, 6.306786284688002], ylim=[-6.306657470061612, 6.306872161105595], axes_position=[0.05, 0.05, 0.9, 0.9], coordinate_axes=False) as c:
            c.path([[-4.0, 0.0], [4.0, 0.0], [4.0, -2.0], [6.0, 1.0], [4.0, 4.0], [4.0, 2.0], [-4.0, 2.0], [-4.0, 0.0]], [1, 2, 2, 2, 2, 2, 2, 79], id='o0', edgecolor=[0.6, 0.6, 0.6, 1.0], facecolor=[0.0, 0.0, 0.0, 0.0], capstyle='butt')
            c.path([[4.0, 0.0], [-4.0, 0.0], [-4.0, 2.0], [-6.0, -1.0], [-4.0, -4.0], [-4.0, -2.0], [4.0, -2.0], [4.0, 0.0]], [1, 2, 2, 2, 2, 2, 2, 79], id='o1', facecolor=[0.0, 0.0, 0.0, 0.0], capstyle='butt')
            c.point([[0.0, 0.0]], id='o2')
            c.text('C', [0.0, 0.0], id='lC', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[0, 15], annotation_clip=None)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane490().draw(sys.argv[1] if len(sys.argv) > 1 else None))
