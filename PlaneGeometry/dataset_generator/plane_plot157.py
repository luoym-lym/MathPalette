"""Frozen question Plane157; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane157:

    def __init__(self):
        self.id = 'Plane157'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:91'
        self.question = 'The floor of a room is covered with equally big rectangular tiles, as shown. The room is ____ m long.'
        self.answer = 12
        self.answer_type = 'number'
        self.query = self.question
        self._geometry_01 = [('tile_edge0', [[0.0, 0.0], [0.0, 1.0]]),
         ('tile_edge1', [[0.0, 0.0], [4.0, 0.0]]),
         ('tile_edge2', [[0.0, 1.0], [0.0, 5.0]]),
         ('tile_edge3', [[0.0, 1.0], [1.0, 1.0]]),
         ('tile_edge4', [[0.0, 1.0], [4.0, 1.0]]),
         ('tile_edge5', [[0.0, 5.0], [0.0, 6.0]]),
         ('tile_edge6', [[0.0, 5.0], [1.0, 5.0]]),
         ('tile_edge7', [[0.0, 5.0], [4.0, 5.0]]),
         ('tile_edge8', [[0.0, 6.0], [0.0, 7.0]]),
         ('tile_edge9', [[0.0, 6.0], [4.0, 6.0]]),
         ('tile_edge10', [[0.0, 7.0], [0.0, 11.0]]),
         ('tile_edge11', [[0.0, 7.0], [1.0, 7.0]]),
         ('tile_edge12', [[0.0, 7.0], [4.0, 7.0]]),
         ('tile_edge13', [[0.0, 11.0], [0.0, 12.0]]),
         ('tile_edge14', [[0.0, 11.0], [1.0, 11.0]]),
         ('tile_edge15', [[0.0, 11.0], [4.0, 11.0]]),
         ('tile_edge16', [[0.0, 12.0], [4.0, 12.0]]),
         ('tile_edge17', [[1.0, 1.0], [1.0, 5.0]]),
         ('tile_edge18', [[1.0, 1.0], [2.0, 1.0]]),
         ('tile_edge19', [[1.0, 5.0], [2.0, 5.0]]),
         ('tile_edge20', [[1.0, 7.0], [1.0, 11.0]]),
         ('tile_edge21', [[1.0, 7.0], [2.0, 7.0]]),
         ('tile_edge22', [[1.0, 11.0], [2.0, 11.0]]),
         ('tile_edge23', [[2.0, 1.0], [2.0, 2.0]]),
         ('tile_edge24', [[2.0, 1.0], [2.0, 5.0]]),
         ('tile_edge25', [[2.0, 1.0], [6.0, 1.0]]),
         ('tile_edge26', [[2.0, 2.0], [2.0, 3.0]]),
         ('tile_edge27', [[2.0, 2.0], [6.0, 2.0]]),
         ('tile_edge28', [[2.0, 3.0], [2.0, 4.0]]),
         ('tile_edge29', [[2.0, 3.0], [6.0, 3.0]]),
         ('tile_edge30', [[2.0, 4.0], [2.0, 5.0]]),
         ('tile_edge31', [[2.0, 4.0], [6.0, 4.0]]),
         ('tile_edge32', [[2.0, 5.0], [6.0, 5.0]]),
         ('tile_edge33', [[2.0, 7.0], [2.0, 11.0]]),
         ('tile_edge34', [[2.0, 7.0], [3.0, 7.0]]),
         ('tile_edge35', [[2.0, 11.0], [3.0, 11.0]]),
         ('tile_edge36', [[3.0, 7.0], [3.0, 11.0]]),
         ('tile_edge37', [[3.0, 7.0], [4.0, 7.0]]),
         ('tile_edge38', [[3.0, 11.0], [4.0, 11.0]]),
         ('tile_edge39', [[4.0, 0.0], [4.0, 1.0]]),
         ('tile_edge40', [[4.0, 0.0], [8.0, 0.0]]),
         ('tile_edge41', [[4.0, 1.0], [8.0, 1.0]]),
         ('tile_edge42', [[4.0, 5.0], [4.0, 6.0]]),
         ('tile_edge43', [[4.0, 5.0], [4.0, 9.0]]),
         ('tile_edge44', [[4.0, 5.0], [5.0, 5.0]]),
         ('tile_edge45', [[4.0, 6.0], [4.0, 7.0]]),
         ('tile_edge46', [[4.0, 7.0], [4.0, 11.0]]),
         ('tile_edge47', [[4.0, 9.0], [4.0, 10.0]]),
         ('tile_edge48', [[4.0, 9.0], [5.0, 9.0]]),
         ('tile_edge49', [[4.0, 9.0], [8.0, 9.0]]),
         ('tile_edge50', [[4.0, 10.0], [4.0, 11.0]]),
         ('tile_edge51', [[4.0, 10.0], [8.0, 10.0]]),
         ('tile_edge52', [[4.0, 11.0], [4.0, 12.0]]),
         ('tile_edge53', [[4.0, 11.0], [8.0, 11.0]]),
         ('tile_edge54', [[4.0, 12.0], [8.0, 12.0]]),
         ('tile_edge55', [[5.0, 5.0], [5.0, 9.0]]),
         ('tile_edge56', [[5.0, 5.0], [6.0, 5.0]]),
         ('tile_edge57', [[5.0, 9.0], [6.0, 9.0]]),
         ('tile_edge58', [[6.0, 1.0], [6.0, 2.0]]),
         ('tile_edge59', [[6.0, 1.0], [6.0, 5.0]]),
         ('tile_edge60', [[6.0, 1.0], [7.0, 1.0]]),
         ('tile_edge61', [[6.0, 2.0], [6.0, 3.0]]),
         ('tile_edge62', [[6.0, 3.0], [6.0, 4.0]]),
         ('tile_edge63', [[6.0, 4.0], [6.0, 5.0]]),
         ('tile_edge64', [[6.0, 5.0], [6.0, 9.0]]),
         ('tile_edge65', [[6.0, 5.0], [7.0, 5.0]]),
         ('tile_edge66', [[6.0, 9.0], [7.0, 9.0]]),
         ('tile_edge67', [[7.0, 1.0], [7.0, 5.0]]),
         ('tile_edge68', [[7.0, 1.0], [8.0, 1.0]]),
         ('tile_edge69', [[7.0, 5.0], [7.0, 9.0]]),
         ('tile_edge70', [[7.0, 5.0], [8.0, 5.0]]),
         ('tile_edge71', [[7.0, 9.0], [8.0, 9.0]]),
         ('tile_edge72', [[8.0, 0.0], [8.0, 1.0]]),
         ('tile_edge73', [[8.0, 1.0], [8.0, 5.0]]),
         ('tile_edge74', [[8.0, 5.0], [8.0, 9.0]]),
         ('tile_edge75', [[8.0, 9.0], [8.0, 10.0]]),
         ('tile_edge76', [[8.0, 10.0], [8.0, 11.0]]),
         ('tile_edge77', [[8.0, 11.0], [8.0, 12.0]]),
         ('dimension0', [[8.0, 0.0], [9.0, 0.0]]),
         ('dimension1', [[8.0, 12.0], [9.0, 12.0]])]
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane157.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-2.078369326452087, 10.53104832799903], ylim=[-0.3140950984895561, 12.295322555961562], axes_position=[0.05, 0.05, 0.9, 0.9], coordinate_axes=False) as c:
            for object_id, points in self._geometry_01:
                c.line(points, id=object_id)
            c.line([[9.0, 0.0], [9.0, 12.0]], id='dimension2', linestyle=(0.0, [4.0, 3.0]))
            c.text('?', [9.5, 6.0], id='label0', rotation_mode='default', offset_pt=[0, 0], annotation_clip=None)
            c.text('1 m', [-0.8, 0.5], id='label1', rotation_mode='default', offset_pt=[0, 0], annotation_clip=None)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane157().draw(sys.argv[1] if len(sys.argv) > 1 else None))
