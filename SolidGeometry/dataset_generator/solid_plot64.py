"""Frozen question Solid64; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Solid64:

    def __init__(self):
        self.id = 'Solid64'
        self.source_dataset = 'MathVerse'
        self.source_key = 'testmini:3654'
        self.question = 'Find the volume of the prism.'
        self.answer = '32 cm³'
        self.answer_type = 'number'
        self.query = self.question
        self.subject = 'SolidGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'SolidGeometry' / 'dataset_generator/scenes/Solid64.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('SolidGeometry', self.id, variant, output_path)
        with Canvas(SOLID, xlim=(-3.580987343425347, 6.806907401257858), ylim=(-1.2325295132207392, 9.155365231462465), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
            c.path([[0.0, 4.0], [2.0, 0.0], [4.0, 4.0], [2.0, 8.0], [0.0, 4.0]], [1, 2, 2, 2, 79], id='front_section', alpha=1.0, zorder=1, edgecolor='none', facecolor=(0.9019607843137255, 0.9019607843137255, 0.9019607843137255, 1.0), capstyle='butt')
            for object_id, points in [('edge_0_0', [[0.0, 4.0], [2.0, 0.0]]), ('edge_1_0', [[2.0, 0.0], [4.0, 4.0]]), ('edge_2_0', [[4.0, 4.0], [2.0, 8.0]]), ('edge_3_0', [[2.0, 8.0], [0.0, 4.0]]), ('edge_5_0', [[3.3, 0.6], [5.3, 4.6]]), ('edge_6_0', [[5.3, 4.6], [3.3, 8.6]]), ('edge_9_0', [[2.0, 0.0], [3.3, 0.6]]), ('edge_10_0', [[4.0, 4.0], [5.3, 4.6]]), ('edge_11_0', [[2.0, 8.0], [3.3, 8.6]]), ('diagonal_horizontal', [[0.0, 4.0], [4.0, 4.0]]), ('diagonal_vertical', [[2.0, 0.0], [2.0, 8.0]]), ('right_angle', [[2.25, 4.0], [2.25, 4.25], [2.0, 4.25]])]:
                c.line(points, id=object_id, zorder=3, clip_on=False)
            c.line([[-1.026629890807984, 0.0], [-1.026629890807984, 8.0]], id='vertical_diagonal_range', zorder=3, clip_on=False, linestyle=(0, [4, 3]))
            c.line([[2.0, 0.0], [-1.026629890807984, 0.0]], id='vertical_diagonal_start', zorder=3, clip_on=False)
            c.line([[2.0, 8.0], [-1.026629890807984, 8.0]], id='vertical_diagonal_end', zorder=3, clip_on=False)
            c.text('8 cm', (-1.026629890807984, 4.0), rotation_mode='default', offset_pt=(-32, 0), annotation_clip=None)
            c.line([[0.0, -0.5921281101914246], [4.0, -0.5921281101914246]], id='horizontal_diagonal_range', zorder=3, clip_on=False, linestyle=(0, [4, 3]))
            c.line([[0.0, 4.0], [0.0, -0.5921281101914246]], id='horizontal_diagonal_start', zorder=3, clip_on=False)
            c.line([[4.0, 4.0], [4.0, -0.5921281101914246]], id='horizontal_diagonal_end', zorder=3, clip_on=False)
            c.text('4 cm', (2.0, -0.5921281101914246), rotation_mode='default', offset_pt=(0, -15), annotation_clip=None)
            c.text('2 cm', (2.65, 8.3), rotation_mode='default', offset_pt=(0.0, 22.1), annotation_clip=None)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Solid64().draw(sys.argv[1] if len(sys.argv) > 1 else None))
