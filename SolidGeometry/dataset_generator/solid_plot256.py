"""Frozen question Solid256; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Solid256:

    def __init__(self):
        self.id = 'Solid256'
        self.source_dataset = 'Author Designed'
        self.source_key = 'author-promote15:Solid267'
        self.question = 'A solid rectangular block has width 15, depth 8, and height 10. Measure x horizontally from its left end. A rectangular section (or sections) is removed all the way through the depth as follows: from x = 7 to x = 15, remove everything above height 5. The figure shows the remaining solid; dashed lines indicate some edges of the original block before cutting. All cuts are perpendicular to the faces of the block. By what percentage does the total surface area decrease? Give the exact percentage.'
        self.answer = '80/7'
        self.answer_type = 'number'
        self.query = self.question
        self.subject = 'SolidGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'SolidGeometry' / 'dataset_generator/scenes/Solid256.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('SolidGeometry', self.id, variant, output_path)
        with Canvas(SOLID, xlim=[-4.248837209302327, 16.448837209302326], ylim=[-2.7488372093023266, 17.948837209302326], axes_position=[0.05, 0.05, 0.9, 0.9], coordinate_axes=False) as c:
            for object_id, points in [('old_0_front', [[7.0, 10.0], [15.0, 10.0]]), ('old_0_back', [[4.2, 15.2], [12.2, 15.2]]), ('old_0_depth', [[15.0, 10.0], [12.2, 15.2]]), ('old_0_vertical', [[15.0, 5.0], [15.0, 10.0]])]:
                c.line(points, id=object_id, linestyle=(0.0, [4.0, 3.0]), solid_capstyle='butt')
            for object_id, points in [('front_0part0', [[0.0, 0.0], [0.0, 5.0]]), ('back_0part0', [[-2.8, 5.2], [-2.8, 10.2]]), ('front_1part0', [[0.0, 0.0], [7.0, 0.0]]), ('front_2part0', [[0.0, 5.0], [0.0, 10.0]]), ('back_2part0', [[-2.8, 10.2], [-2.8, 15.2]]), ('front_3part0', [[7.0, 5.0], [7.0, 10.0]]), ('front_4part0', [[0.0, 10.0], [7.0, 10.0]]), ('back_4part0', [[-2.8, 15.2], [4.2, 15.2]]), ('front_5part0', [[15.0, 0.0], [15.0, 5.0]]), ('front_6part0', [[7.0, 0.0], [15.0, 0.0]]), ('front_7part0', [[7.0, 5.0], [15.0, 5.0]]), ('back_7part0', [[6.892307679999999, 10.2], [12.2, 10.2]]), ('depth_0part0', [[0.0, 0.0], [-2.8, 5.2]]), ('depth_1part0', [[0.0, 10.0], [-2.8, 15.2]]), ('depth_3part0', [[7.0, 10.0], [4.2, 15.2]]), ('depth_5part0', [[15.0, 5.0], [12.2, 10.2]])]:
                c.line(points, id=object_id, solid_capstyle='butt')
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Solid256().draw(sys.argv[1] if len(sys.argv) > 1 else None))
