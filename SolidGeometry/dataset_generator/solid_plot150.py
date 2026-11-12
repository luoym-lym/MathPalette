"""Frozen question Solid150; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Solid150:

    def __init__(self):
        self.id = 'Solid150'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:1139'
        self.question = 'Seven identical dice (each with 1, 2, 3, 4, 5 and 6 points on their faces) are glued together to form the solid shown. Faces that are glued together each have the same number of points. How many points can be seen on the surface of the solid?'
        self.answer = '105'
        self.answer_type = 'number'
        self.query = self.question
        self._geometry_01 = [('crosse0', [[0.0, 1.0], [1.0, 1.0]]),
         ('crosse1', [[1.0, 1.0], [1.34, 1.34]]),
         ('crosse2', [[1.0, 0.0], [1.0, 1.0]]),
         ('crosse3', [[1.0, 0.0], [2.0, 0.0]]),
         ('crosse4', [[1.0, 1.0], [2.0, 1.0]]),
         ('crosse5', [[1.34, 1.34], [2.34, 1.34]]),
         ('crosse6', [[2.0, 0.0], [2.34, 0.34]]),
         ('crosse7', [[2.0, 1.0], [2.34, 1.34]]),
         ('crosse8', [[2.0, 0.0], [2.0, 1.0]]),
         ('crosse9', [[2.34, 0.34], [2.34, 1.34]]),
         ('crosse10', [[-1.0, 0.0], [-0.33999999999999997, 0.0]]),
         ('crosse11', [[-1.0, 1.0], [0.0, 1.0]]),
         ('crosse12', [[-0.6599999999999999, 1.34], [5.551115123125783e-17, 1.34]]),
         ('crosse13', [[-1.0, 1.0], [-0.6599999999999999, 1.34]]),
         ('crosse14', [[-1.0, 0.0], [-1.0, 1.0]]),
         ('crosse15', [[1.34, 1.6800000000000002], [1.6800000000000002, 1.6800000000000002]]),
         ('crosse16', [[1.34, 1.34], [1.6800000000000002, 1.6800000000000002]]),
         ('crosse17', [[1.6800000000000002, 1.34], [1.6800000000000002, 1.6800000000000002]]),
         ('crosse18', [[-0.34, -0.34], [0.6599999999999999, -0.34]]),
         ('crosse19', [[-0.34, 0.6599999999999999], [0.6599999999999999, 0.6599999999999999]]),
         ('crosse20', [[-0.34, 0.6599999999999999], [0.0, 1.0]]),
         ('crosse21', [[0.6599999999999999, -0.34], [1.0, 0.0]]),
         ('crosse22', [[0.6599999999999999, 0.6599999999999999], [1.0, 1.0]]),
         ('crosse23', [[-0.34, -0.34], [-0.34, 0.6599999999999999]]),
         ('crosse24', [[0.6599999999999999, -0.34], [0.6599999999999999, 0.6599999999999999]]),
         ('crosse25', [[0.0, 2.0], [1.0, 2.0]]),
         ('crosse26', [[0.34, 2.34], [1.34, 2.34]]),
         ('crosse27', [[0.0, 2.0], [0.34, 2.34]]),
         ('crosse28', [[1.0, 2.0], [1.34, 2.34]]),
         ('crosse29', [[0.0, 1.0], [0.0, 2.0]]),
         ('crosse30', [[1.0, 1.0], [1.0, 2.0]]),
         ('crosse31', [[1.34, 1.34], [1.34, 2.34]]),
         ('crosse32', [[0.0, -1.0], [1.0, -1.0]]),
         ('crosse33', [[1.0, -1.0], [1.34, -0.6599999999999999]]),
         ('crosse34', [[0.0, -1.0], [0.0, -0.33999999999999997]]),
         ('crosse35', [[1.0, -1.0], [1.0, 0.0]]),
         ('crosse36', [[1.34, -0.6599999999999999], [1.34, 5.551115123125783e-17]])]
        self.subject = 'SolidGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'SolidGeometry' / 'dataset_generator/scenes/Solid150.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('SolidGeometry', self.id, variant, output_path)
        with Canvas(SOLID, xlim=(-1.0831832295263042, 2.428240157820878), ylim=(-1.0882401578208776, 2.4231832295263045), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
            for object_id, points in self._geometry_01:
                c.line(points, id=object_id, zorder=3, clip_on=False)
            for object_id, vertices, codes in [('mergedmaterial0_0', [[1.0, 0.0], [2.0, 0.0], [2.0, 1.0], [1.0, 1.0], [1.0, 0.0]], [1, 2, 2, 2, 79]), ('mergedmaterial0_1', [[-0.34, 0.66], [0.0, 1.0], [-1.0, 1.0], [-1.0, 0.0], [-0.34, 0.0], [-0.34, 0.66]], [1, 2, 2, 2, 2, 79]), ('mergedmaterial0_2', [[0.0, 1.0], [1.0, 1.0], [1.0, 2.0], [0.0, 2.0], [0.0, 1.0]], [1, 2, 2, 2, 79]), ('mergedmaterial0_3', [[0.0, -1.0], [1.0, -1.0], [1.0, -0.34], [1.0, 0.0], [0.66, -0.34], [0.0, -0.34], [0.0, -1.0]], [1, 2, 2, 2, 2, 2, 79]), ('mergedmaterial1_0', [[2.0, 0.0], [2.34, 0.34], [2.34, 1.34], [2.0, 1.0], [2.0, 0.0]], [1, 2, 2, 2, 79]), ('mergedmaterial2_0', [[1.0, 1.0], [2.0, 1.0], [2.34, 1.34], [1.34, 1.34], [1.0, 1.0]], [1, 2, 2, 2, 79]), ('mergedmaterial2_1', [[-1.0, 1.0], [0.0, 1.0], [0.0, 1.34], [-0.6599999999999999, 1.34], [-1.0, 1.0]], [1, 2, 2, 2, 79]), ('mergedmaterial2_2', [[1.34, 1.34], [1.6800000000000002, 1.6800000000000002], [1.34, 1.6800000000000002], [1.34, 1.34]], [1, 2, 2, 79]), ('mergedmaterial2_3', [[-0.34, 0.6599999999999999], [0.6599999999999999, 0.6599999999999999], [1.0, 1.0], [0.0, 1.0], [-0.34, 0.6599999999999999]], [1, 2, 2, 2, 79]), ('mergedmaterial3_0', [[1.6800000000000002, 1.34], [1.6800000000000002, 1.6800000000000002], [1.34, 1.34], [1.6800000000000002, 1.34]], [1, 2, 2, 79]), ('mergedmaterial3_1', [[0.6599999999999999, -0.34], [1.0, 0.0], [1.0, 1.0], [0.6599999999999999, 0.6599999999999999], [0.6599999999999999, -0.34]], [1, 2, 2, 2, 79]), ('mergedmaterial3_2', [[1.0, 1.0], [1.34, 1.34], [1.34, 2.34], [1.0, 2.0], [1.0, 1.0]], [1, 2, 2, 2, 79]), ('mergedmaterial3_3', [[1.0, -1.0], [1.34, -0.6599999999999999], [1.34, 0.0], [1.0, 0.0], [1.0, -1.0]], [1, 2, 2, 2, 79]), ('mergedmaterial4_0', [[-0.34, -0.34], [0.6599999999999999, -0.34], [0.6599999999999999, 0.6599999999999999], [-0.34, 0.6599999999999999], [-0.34, -0.34]], [1, 2, 2, 2, 79]), ('mergedmaterial5_0', [[0.0, 2.0], [1.0, 2.0], [1.34, 2.34], [0.34, 2.34], [0.0, 2.0]], [1, 2, 2, 2, 79])]:
                c.path(vertices, codes, id=object_id, alpha=1.0, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Solid150().draw(sys.argv[1] if len(sys.argv) > 1 else None))
