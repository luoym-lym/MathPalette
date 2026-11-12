"""Frozen question Plane516; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane516:

    def __init__(self):
        self.id = 'Plane516'
        self.source_dataset = 'Author Designed'
        self.source_key = 'author-expand24:Plane200/extension_02'
        self.question = 'Ten identical coins touch in a triangular arrangement with rows of 4, 3, 2 and 1, as shown. What is the smallest number of coins that must be moved to make the two-row parallelogram shown, with 5 coins in each row? In both arrangements, neighboring coins shown touching have centers one coin diameter apart. The coins may be lifted and placed freely, and a coin counts as moved if its center changes. The entire target arrangement may be translated and rotated, but not reflected or scaled; its position in the picture is only illustrative.'
        self.answer = '3'
        self.answer_type = 'number'
        self.query = self.question
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane516.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-0.6105263157894729, 23.810526315789474], ylim=[-12.210526315789473, 12.210526315789473]) as c:
            for object_id, center, radius in [('initial_coin_01', [1, -2.598076211353316], 1), ('initial_coin_02', [3, -2.598076211353316], 1), ('initial_coin_03', [5, -2.598076211353316], 1), ('initial_coin_04', [7, -2.598076211353316], 1), ('initial_coin_05', [2, -0.8660254037844388], 1), ('initial_coin_06', [4, -0.8660254037844388], 1), ('initial_coin_07', [6, -0.8660254037844388], 1), ('initial_coin_08', [3, 0.8660254037844384], 1), ('initial_coin_09', [5, 0.8660254037844384], 1), ('initial_coin_10', [4, 2.598076211353316], 1), ('target_coin_01', [13.2, -0.8660254037844386], 1), ('target_coin_02', [15.2, -0.8660254037844386], 1), ('target_coin_03', [17.2, -0.8660254037844386], 1), ('target_coin_04', [19.2, -0.8660254037844386], 1), ('target_coin_05', [21.2, -0.8660254037844386], 1), ('target_coin_06', [14.2, 0.8660254037844386], 1), ('target_coin_07', [16.2, 0.8660254037844386], 1), ('target_coin_08', [18.2, 0.8660254037844386], 1), ('target_coin_09', [20.2, 0.8660254037844386], 1), ('target_coin_10', [22.2, 0.8660254037844386], 1)]:
                c.circle(center, radius, id=object_id)
            c.path([[8.65, -0.22], [10.999999999999998, -0.22], [10.999999999999998, -0.55], [11.649999999999999, 0], [10.999999999999998, 0.55], [10.999999999999998, 0.22], [8.65, 0.22], [8.65, -0.22]], [1, 2, 2, 2, 2, 2, 2, 79], id='transformation_arrow')
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane516().draw(sys.argv[1] if len(sys.argv) > 1 else None))
