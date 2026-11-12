"""Frozen question Solid257; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Solid257:

    def __init__(self):
        self.id = 'Solid257'
        self.source_dataset = 'Author Designed'
        self.source_key = 'author-promote15:Solid268'
        self.question = 'A solid rectangular block has width 16, depth 4, and height 8. Measure x horizontally from its left end. A rectangular section (or sections) is removed all the way through the depth as follows: from x = 4 to x = 13, remove everything above height 3. The figure shows the remaining solid; dashed lines indicate some edges of the original block before cutting. All cuts are perpendicular to the faces of the block. By what percentage does the total surface area decrease? Give the exact percentage.'
        self.answer = '625/56'
        self.answer_type = 'number'
        self.query = self.question
        self._geometry_01 = [('front_0part0', [[0.0, 0.0], [0.0, 3.0]]),
         ('back_0part0', [[-1.4, 2.6], [-1.4, 5.6]]),
         ('front_1part0', [[0.0, 0.0], [4.0, 0.0]]),
         ('front_2part0', [[0.0, 3.0], [0.0, 8.0]]),
         ('back_2part0', [[-1.4, 5.6], [-1.4, 10.6]]),
         ('front_3part0', [[4.0, 3.0], [4.0, 8.0]]),
         ('front_4part0', [[0.0, 8.0], [4.0, 8.0]]),
         ('back_4part0', [[-1.4, 10.6], [2.6, 10.6]]),
         ('front_5part0', [[4.0, 0.0], [13.0, 0.0]]),
         ('front_6part0', [[4.0, 3.0], [13.0, 3.0]]),
         ('back_6part0', [[3.999999986, 5.6], [11.6, 5.6]]),
         ('front_7part0', [[16.0, 0.0], [16.0, 3.0]]),
         ('front_8part0', [[13.0, 0.0], [16.0, 0.0]]),
         ('front_9part0', [[13.0, 3.0], [13.0, 8.0]]),
         ('back_9part0', [[11.6, 5.6], [11.6, 10.6]]),
         ('front_10part0', [[16.0, 3.0], [16.0, 8.0]]),
         ('front_11part0', [[13.0, 8.0], [16.0, 8.0]]),
         ('back_11part0', [[11.6, 10.6], [14.6, 10.6]]),
         ('depth_0part0', [[0.0, 0.0], [-1.4, 2.6]]),
         ('depth_1part0', [[0.0, 8.0], [-1.4, 10.6]]),
         ('depth_3part0', [[4.0, 8.0], [2.6, 10.6]]),
         ('depth_4part0', [[13.0, 3.0], [11.6, 5.6]]),
         ('depth_5part0', [[13.0, 8.0], [11.6, 10.6]]),
         ('depth_7part0', [[16.0, 8.0], [14.6, 10.6]])]
        self.subject = 'SolidGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'SolidGeometry' / 'dataset_generator/scenes/Solid257.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('SolidGeometry', self.id, variant, output_path)
        with Canvas(SOLID, xlim=[-2.8162790697674422, 17.41627906976744], ylim=[-4.816279069767442, 15.416279069767441], axes_position=[0.05, 0.05, 0.9, 0.9], coordinate_axes=False) as c:
            c.line([[4.0, 8.0], [13.0, 8.0]], id='old_0_front', linestyle=(0.0, [4.0, 3.0]), solid_capstyle='butt')
            c.line([[2.6, 10.6], [11.6, 10.6]], id='old_0_back', linestyle=(0.0, [4.0, 3.0]), solid_capstyle='butt')
            for object_id, points in self._geometry_01:
                c.line(points, id=object_id, solid_capstyle='butt')
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Solid257().draw(sys.argv[1] if len(sys.argv) > 1 else None))
