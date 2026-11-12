"""Frozen question Plane517; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane517:

    def __init__(self):
        self.id = 'Plane517'
        self.source_dataset = 'Author Designed'
        self.source_key = 'author-expand24:Plane200/extension_03'
        self.question = 'Twelve identical coins touch in a parallelogram with 3 rows of 4 coins, as shown. What is the smallest number of coins that must be moved to make the hollow hexagonal ring shown, with 3 coins along each side, counting each corner coin on both adjoining sides? In both arrangements, neighboring coins shown touching have centers one coin diameter apart. The coins may be lifted and placed freely, and a coin counts as moved if its center changes. The entire target arrangement may be translated and rotated, but not reflected or scaled; its position in the picture is only illustrative.'
        self.answer = '6'
        self.answer_type = 'number'
        self.query = self.question
        self._geometry_01 = [('initial_coin_01', [1, -1.7320508075688772], 1),
         ('initial_coin_02', [3, -1.7320508075688772], 1),
         ('initial_coin_03', [5, -1.7320508075688772], 1),
         ('initial_coin_04', [7, -1.7320508075688772], 1),
         ('initial_coin_05', [2, 0.0], 1),
         ('initial_coin_06', [4, 0.0], 1),
         ('initial_coin_07', [6, 0.0], 1),
         ('initial_coin_08', [8, 0.0], 1),
         ('initial_coin_09', [3, 1.7320508075688772], 1),
         ('initial_coin_10', [5, 1.7320508075688772], 1),
         ('initial_coin_11', [7, 1.7320508075688772], 1),
         ('initial_coin_12', [9, 1.7320508075688772], 1),
         ('target_coin_01', [15.2, 0.0], 1),
         ('target_coin_02', [16.2, 1.7320508075688772], 1),
         ('target_coin_03', [17.2, 3.4641016151377544], 1),
         ('target_coin_04', [16.2, -1.7320508075688772], 1),
         ('target_coin_05', [19.2, 3.4641016151377544], 1),
         ('target_coin_06', [17.2, -3.4641016151377544], 1),
         ('target_coin_07', [21.2, 3.4641016151377544], 1),
         ('target_coin_08', [19.2, -3.4641016151377544], 1),
         ('target_coin_09', [22.2, 1.7320508075688772], 1),
         ('target_coin_10', [21.2, -3.4641016151377544], 1),
         ('target_coin_11', [22.2, -1.7320508075688772], 1),
         ('target_coin_12', [23.2, 0.0], 1)]
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane517.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-0.6368421052631597, 24.83684210526316], ylim=[-12.73684210526316, 12.73684210526316]) as c:
            for object_id, center, radius in self._geometry_01:
                c.circle(center, radius, id=object_id)
            c.path([[10.65, -0.22], [12.999999999999998, -0.22], [12.999999999999998, -0.55], [13.649999999999999, 0], [12.999999999999998, 0.55], [12.999999999999998, 0.22], [10.65, 0.22], [10.65, -0.22]], [1, 2, 2, 2, 2, 2, 2, 79], id='transformation_arrow')
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane517().draw(sys.argv[1] if len(sys.argv) > 1 else None))
