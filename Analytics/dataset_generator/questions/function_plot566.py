"""Frozen question Ana566; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[3]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Ana566:

    def __init__(self):
        self.id = 'Ana566'
        self.source_dataset = 'Author Designed'
        self.source_key = 'author_special20_20261111/Ana566'
        self.question = 'The feasible set F is the closed shaded polygon ABCDE, including its boundary. Read its vertices from the unit grid. Find the coordinates of the unique point in F maximizing 3x+y.'
        self.answer = '(5, 1)'
        self.answer_type = 'expression'
        self.query = self.question
        self.subject = 'Analytics'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'Analytics' / 'dataset_generator/scenes/Ana566.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Analytics' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('Analytics', self.id, variant, output_path)
        with Canvas(ANALYTICS, xlim=(-8.0, 8.0), ylim=(-8.0, 8.0), axes_position=(0.12, 0.12, 0.8, 0.8), coordinate_axes=True) as c:
            c.path([[-4.0, -2.0], [4.0, -2.0], [5.0, 1.0], [1.0, 5.0], [-3.0, 3.0], [-4.0, -2.0]], [1, 2, 2, 2, 2, 79], id='region_001', alpha=0.45, zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), capstyle='butt')
            c.line([[-4.0, -2.0], [4.0, -2.0], [5.0, 1.0], [1.0, 5.0], [-3.0, 3.0], [-4.0, -2.0]], id='curve_001', solid_capstyle='butt')
            c.point([[-4.0, -2.0], [4.0, -2.0], [5.0, 1.0], [1.0, 5.0], [-3.0, 3.0]], id='point_001')
            for object_id, text, anchor in [('text_001', 'A', (-4.5, -2.4)), ('text_002', 'B', (4.4, -2.5)), ('text_003', 'C', (5.5, 1.1)), ('text_004', 'D', (1.4, 5.5)), ('text_005', 'E', (-3.5, 3.3)), ('text_006', 'F', (0.5, 1.4))]:
                c.text(text, anchor, id=object_id, rotation_mode='default')
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Ana566().draw(sys.argv[1] if len(sys.argv) > 1 else None))
