"""Frozen question Plane15; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane15:

    def __init__(self):
        self.id = 'Plane15'
        self.source_dataset = 'MathVerse'
        self.source_key = 's3834'
        self.question = 'In rectangle ABDF above, C and E are midpoints of sides BD and DF, respectively. What fraction of the area of the rectangle is shaded?'
        self.answer = '5/8'
        self.answer_type = 'number'
        self.query = self.question
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane15.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=(-0.28066337213891, 4.273664604127317), ylim=(-1.25651744303689, 3.297810533229337), axes_position=(0.05, 0.050000000000000114, 0.9, 0.8999999999999998), coordinate_axes=False) as c:
            c.path([[0.0, 0.0], [4.0, 0.0], [4.0, 2.0], [0.0, 2.0], [0.0, 0.0]], [1, 2, 2, 2, 79], id='rectangle', capstyle='butt')
            c.path([[0.0, 0.0], [2.0, 2.0], [4.0, 1.0], [4.0, 0.0], [0.0, 0.0]], [1, 2, 2, 2, 79], alpha=0.45, zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), capstyle='butt')
            c.path([[0.0, 0.0], [2.0, 2.0], [4.0, 1.0], [4.0, 0.0], [0.0, 0.0]], [1, 2, 2, 2, 79], id='shade', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.line([[0.0, 0.0], [2.0, 2.0]], id='AC')
            c.line([[2.0, 2.0], [4.0, 1.0]], id='CE')
            c.text('A', (0.0, 0.0), id='v_A', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(-12.0, -12.0), annotation_clip=None)
            c.text('B', (0.0, 2.0), id='v_B', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(-12.0, 12.0), annotation_clip=None)
            c.text('C', (2.0, 2.0), id='v_C', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(0.0, 13.5), annotation_clip=None)
            c.text('D', (4.0, 2.0), id='v_D', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(12.0, 12.0), annotation_clip=None)
            c.text('E', (4.0, 1.0), id='v_E', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(12.0, 0.0), annotation_clip=None)
            c.text('F', (4.0, 0.0), id='v_F', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(12.0, -12.0), annotation_clip=None)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane15().draw(sys.argv[1] if len(sys.argv) > 1 else None))
