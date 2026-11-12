"""Frozen question Plane515; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane515:

    def __init__(self):
        self.id = 'Plane515'
        self.source_dataset = 'Author Designed'
        self.source_key = 'author-expand24:Plane200/extension_01'
        self.question = 'Six identical coins touch in a triangular arrangement with rows of 3, 2 and 1, as shown. What is the smallest number of coins that must be moved to make the two-row parallelogram shown, with 3 coins in each row? In both arrangements, neighboring coins shown touching have centers one coin diameter apart. The coins may be lifted and placed freely, and a coin counts as moved if its center changes. The entire target arrangement may be translated and rotated, but not reflected or scaled; its position in the picture is only illustrative.'
        self.answer = '1'
        self.answer_type = 'number'
        self.query = self.question
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane515.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-0.4526315789473685, 17.652631578947368], ylim=[-9.052631578947368, 9.052631578947368]) as c:
            for object_id, center, radius in [('initial_coin_01', [1, -1.7320508075688772], 1), ('initial_coin_02', [3, -1.7320508075688772], 1), ('initial_coin_03', [5, -1.7320508075688772], 1), ('initial_coin_04', [2, 0.0], 1), ('initial_coin_05', [4, 0.0], 1), ('initial_coin_06', [3, 1.7320508075688772], 1), ('target_coin_01', [11.2, -0.8660254037844386], 1), ('target_coin_02', [13.2, -0.8660254037844386], 1), ('target_coin_03', [15.2, -0.8660254037844386], 1), ('target_coin_04', [12.2, 0.8660254037844386], 1), ('target_coin_05', [14.2, 0.8660254037844386], 1), ('target_coin_06', [16.2, 0.8660254037844386], 1)]:
                c.circle(center, radius, id=object_id)
            c.path([[6.65, -0.22], [8.999999999999998, -0.22], [8.999999999999998, -0.55], [9.649999999999999, 0], [8.999999999999998, 0.55], [8.999999999999998, 0.22], [6.65, 0.22], [6.65, -0.22]], [1, 2, 2, 2, 2, 2, 2, 79], id='transformation_arrow')
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane515().draw(sys.argv[1] if len(sys.argv) > 1 else None))
