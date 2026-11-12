"""Frozen question Solid112; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Solid112:

    def __init__(self):
        self.id = 'Solid112'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:427'
        self.question = 'How many cubes have been taken from the block?'
        self.answer = '7'
        self.answer_type = 'number'
        self.query = self.question
        self.subject = 'SolidGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'SolidGeometry' / 'dataset_generator/scenes/Solid112.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('SolidGeometry', self.id, variant, output_path)
        with Canvas(SOLID, xlim=[-0.23286323235657225, 9.597019603480604], ylim=[-3.3970196034806035, 6.432863232356573], projection=[[1, 0.35, 0], [0, 0.35, 1]], origin=[0, 0, 0], offset=[0, 0]) as c:
            for object_id, points in [('beforee0', c.project([[0.0, 0.0, 0.0], [1.0, 0.0, 0.0]])), ('beforee1', c.project([[0.0, 0.0, 1.0], [1.0, 0.0, 1.0]])), ('beforee2', c.project([[0.0, 0.0, 0.0], [0.0, 0.0, 1.0]])), ('beforee3', c.project([[1.0, 0.0, 0.0], [1.0, 0.0, 1.0]])), ('beforee4', c.project([[0.0, 0.0, 2.0], [1.0, 0.0, 2.0]])), ('beforee5', c.project([[0.0, 1.0, 2.0], [1.0, 1.0, 2.0]])), ('beforee6', c.project([[0.0, 0.0, 2.0], [0.0, 1.0, 2.0]])), ('beforee7', c.project([[1.0, 0.0, 2.0], [1.0, 1.0, 2.0]])), ('beforee8', c.project([[0.0, 0.0, 1.0], [0.0, 0.0, 2.0]])), ('beforee9', c.project([[1.0, 0.0, 1.0], [1.0, 0.0, 2.0]])), ('beforee10', c.project([[0.0, 2.0, 2.0], [1.0, 2.0, 2.0]])), ('beforee11', c.project([[0.0, 1.0, 2.0], [0.0, 2.0, 2.0]])), ('beforee12', c.project([[1.0, 1.0, 2.0], [1.0, 2.0, 2.0]])), ('beforee13', c.project([[0.0, 3.0, 2.0], [1.0, 3.0, 2.0]])), ('beforee14', c.project([[0.0, 2.0, 2.0], [0.0, 3.0, 2.0]])), ('beforee15', c.project([[1.0, 2.0, 2.0], [1.0, 3.0, 2.0]])), ('beforee16', c.project([[1.0, 0.0, 0.0], [2.0, 0.0, 0.0]])), ('beforee17', c.project([[1.0, 0.0, 1.0], [2.0, 0.0, 1.0]])), ('beforee18', c.project([[2.0, 0.0, 0.0], [2.0, 0.0, 1.0]])), ('beforee19', c.project([[1.0, 0.0, 2.0], [2.0, 0.0, 2.0]])), ('beforee20', c.project([[1.0, 1.0, 2.0], [2.0, 1.0, 2.0]])), ('beforee21', c.project([[2.0, 0.0, 2.0], [2.0, 1.0, 2.0]])), ('beforee22', c.project([[2.0, 0.0, 1.0], [2.0, 0.0, 2.0]])), ('beforee23', c.project([[1.0, 2.0, 2.0], [2.0, 2.0, 2.0]])), ('beforee24', c.project([[2.0, 1.0, 2.0], [2.0, 2.0, 2.0]])), ('beforee25', c.project([[1.0, 3.0, 2.0], [2.0, 3.0, 2.0]])), ('beforee26', c.project([[2.0, 2.0, 2.0], [2.0, 3.0, 2.0]])), ('beforee27', c.project([[2.0, 0.0, 0.0], [3.0, 0.0, 0.0]])), ('beforee28', c.project([[2.0, 0.0, 1.0], [3.0, 0.0, 1.0]])), ('beforee29', c.project([[3.0, 0.0, 0.0], [3.0, 1.0, 0.0]])), ('beforee30', c.project([[3.0, 0.0, 1.0], [3.0, 1.0, 1.0]])), ('beforee31', c.project([[3.0, 0.0, 0.0], [3.0, 0.0, 1.0]])), ('beforee32', c.project([[3.0, 1.0, 0.0], [3.0, 1.0, 1.0]])), ('beforee33', c.project([[2.0, 0.0, 2.0], [3.0, 0.0, 2.0]])), ('beforee34', c.project([[2.0, 1.0, 2.0], [3.0, 1.0, 2.0]])), ('beforee35', c.project([[3.0, 0.0, 2.0], [3.0, 1.0, 2.0]])), ('beforee36', c.project([[3.0, 0.0, 1.0], [3.0, 0.0, 2.0]])), ('beforee37', c.project([[3.0, 1.0, 1.0], [3.0, 1.0, 2.0]])), ('beforee38', c.project([[3.0, 1.0, 0.0], [3.0, 2.0, 0.0]])), ('beforee39', c.project([[3.0, 1.0, 1.0], [3.0, 2.0, 1.0]])), ('beforee40', c.project([[3.0, 2.0, 0.0], [3.0, 2.0, 1.0]])), ('beforee41', c.project([[2.0, 2.0, 2.0], [3.0, 2.0, 2.0]])), ('beforee42', c.project([[3.0, 1.0, 2.0], [3.0, 2.0, 2.0]])), ('beforee43', c.project([[3.0, 2.0, 1.0], [3.0, 2.0, 2.0]])), ('beforee44', c.project([[3.0, 2.0, 0.0], [3.0, 3.0, 0.0]])), ('beforee45', c.project([[3.0, 2.0, 1.0], [3.0, 3.0, 1.0]])), ('beforee46', c.project([[3.0, 3.0, 0.0], [3.0, 3.0, 1.0]])), ('beforee47', c.project([[2.0, 3.0, 2.0], [3.0, 3.0, 2.0]])), ('beforee48', c.project([[3.0, 2.0, 2.0], [3.0, 3.0, 2.0]])), ('beforee49', c.project([[3.0, 3.0, 1.0], [3.0, 3.0, 2.0]])), ('aftere0', c.project([[5.3, 0.0, 0.0], [6.3, 0.0, 0.0]])), ('aftere1', c.project([[5.3, 0.0, 1.0], [6.3, 0.0, 1.0]])), ('aftere2', c.project([[6.3, 0.0, 1.0], [6.3, 1.0, 1.0]])), ('aftere3', c.project([[5.3, 0.0, 0.0], [5.3, 0.0, 1.0]])), ('aftere4', c.project([[6.3, 0.0, 0.0], [6.3, 0.0, 1.0]])), ('aftere5', c.project([[5.95, 2.0, 1.0], [6.3, 2.0, 1.0]])), ('aftere6', c.project([[6.3, 1.0, 1.0], [6.3, 2.0, 1.0]])), ('aftere7', c.project([[5.6, 3.0, 1.0], [6.3, 3.0, 1.0]])), ('aftere8', c.project([[6.3, 2.0, 1.0], [6.3, 3.0, 1.0]])), ('aftere9', c.project([[6.3, 0.0, 0.0], [7.3, 0.0, 0.0]])), ('aftere10', c.project([[6.3, 0.0, 1.0], [7.3, 0.0, 1.0]])), ('aftere11', c.project([[6.3, 1.0, 1.0], [7.3, 1.0, 1.0]])), ('aftere12', c.project([[7.3, 0.0, 1.0], [7.3, 1.0, 1.0]])), ('aftere13', c.project([[7.3, 0.0, 0.0], [7.3, 0.0, 1.0]])), ('aftere14', c.project([[6.3, 2.0, 1.0], [7.3, 2.0, 1.0]])), ('aftere15', c.project([[7.3, 1.0, 1.0], [7.3, 2.0, 1.0]])), ('aftere16', c.project([[6.3, 3.0, 1.0], [6.95, 3.0, 1.0]])), ('aftere17', c.project([[7.3, 0.0, 0.0], [8.3, 0.0, 0.0]])), ('aftere18', c.project([[7.3, 0.0, 1.0], [8.3, 0.0, 1.0]])), ('aftere19', c.project([[7.3, 1.0, 1.0], [8.3, 1.0, 1.0]])), ('aftere20', c.project([[8.3, 0.0, 0.0], [8.3, 1.0, 0.0]])), ('aftere21', c.project([[8.3, 0.0, 1.0], [8.3, 1.0, 1.0]])), ('aftere22', c.project([[8.3, 0.0, 0.0], [8.3, 0.0, 1.0]])), ('aftere23', c.project([[8.3, 1.0, 0.0], [8.3, 1.0, 1.0]])), ('aftere24', c.project([[7.3, 2.0, 1.0], [8.3, 2.0, 1.0]])), ('aftere25', c.project([[8.3, 1.0, 0.0], [8.3, 2.0, 0.0]])), ('aftere26', c.project([[8.3, 1.0, 1.0], [8.3, 2.0, 1.0]])), ('aftere27', c.project([[8.3, 2.0, 0.0], [8.3, 2.0, 1.0]])), ('aftere28', c.project([[8.3, 2.0, 0.0], [8.3, 3.0, 0.0]])), ('aftere29', c.project([[8.3, 2.0, 1.0], [8.3, 3.0, 1.0]])), ('aftere30', c.project([[8.3, 3.0, 0.0], [8.3, 3.0, 1.0]])), ('aftere31', c.project([[5.3, 0.0, 2.0], [6.3, 0.0, 2.0]])), ('aftere32', c.project([[5.3, 1.0, 2.0], [6.3, 1.0, 2.0]])), ('aftere33', c.project([[5.3, 0.0, 2.0], [5.3, 1.0, 2.0]])), ('aftere34', c.project([[6.3, 0.0, 2.0], [6.3, 1.0, 2.0]])), ('aftere35', c.project([[5.3, 0.0, 1.0], [5.3, 0.0, 2.0]])), ('aftere36', c.project([[6.3, 0.0, 1.0], [6.3, 0.0, 2.0]])), ('aftere37', c.project([[6.3, 1.0, 1.0], [6.3, 1.0, 2.0]])), ('aftere38', c.project([[7.3, 2.0, 2.0], [8.3, 2.0, 2.0]])), ('aftere39', c.project([[7.3, 3.0, 2.0], [8.3, 3.0, 2.0]])), ('aftere40', c.project([[7.3, 2.0, 2.0], [7.3, 3.0, 2.0]])), ('aftere41', c.project([[8.3, 2.0, 2.0], [8.3, 3.0, 2.0]])), ('aftere42', c.project([[7.3, 2.0, 1.0], [7.3, 2.0, 2.0]])), ('aftere43', c.project([[8.3, 2.0, 1.0], [8.3, 2.0, 2.0]])), ('aftere44', c.project([[8.3, 3.0, 1.0], [8.3, 3.0, 2.0]]))]:
                c.line(points, id=object_id, clip_on=False, zorder=3)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Solid112().draw(sys.argv[1] if len(sys.argv) > 1 else None))
