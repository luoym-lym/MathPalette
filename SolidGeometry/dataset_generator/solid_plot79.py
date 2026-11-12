"""Frozen question Solid79; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Solid79:

    def __init__(self):
        self.id = 'Solid79'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:11'
        self.question = 'A construction of equal cubes is shown in the upper picture. After several cubes are removed, it has the form shown in the lower picture. How many cubes were removed?'
        self.answer = '7'
        self.answer_type = 'number'
        self.query = self.question
        self.subject = 'SolidGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'SolidGeometry' / 'dataset_generator/scenes/Solid79.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('SolidGeometry', self.id, variant, output_path)
        with Canvas(SOLID, xlim=[-1.4131523583170558, 5.473069388355814], ylim=[-0.16809195458363613, 6.718129792089234], projection=[[1, 0.35, 0], [0, 0.35, 1]], origin=[0, 0, 0], offset=[0, 0]) as c:
            for object_id, points in [('uppere0', c.project([[0.0, 0.0, 3.5], [1.0, 0.0, 3.5]])), ('uppere1', c.project([[0.0, 0.0, 4.5], [1.0, 0.0, 4.5]])), ('uppere2', c.project([[0.0, 0.0, 3.5], [0.0, 0.0, 4.5]])), ('uppere3', c.project([[1.0, 0.0, 3.5], [1.0, 0.0, 4.5]])), ('uppere4', c.project([[0.0, 0.0, 5.5], [1.0, 0.0, 5.5]])), ('uppere5', c.project([[0.0, 1.0, 5.5], [1.0, 1.0, 5.5]])), ('uppere6', c.project([[0.0, 0.0, 5.5], [0.0, 1.0, 5.5]])), ('uppere7', c.project([[1.0, 0.0, 5.5], [1.0, 1.0, 5.5]])), ('uppere8', c.project([[0.0, 0.0, 4.5], [0.0, 0.0, 5.5]])), ('uppere9', c.project([[1.0, 0.0, 4.5], [1.0, 0.0, 5.5]])), ('uppere10', c.project([[0.0, 2.0, 5.5], [1.0, 2.0, 5.5]])), ('uppere11', c.project([[0.0, 1.0, 5.5], [0.0, 2.0, 5.5]])), ('uppere12', c.project([[1.0, 1.0, 5.5], [1.0, 2.0, 5.5]])), ('uppere13', c.project([[0.0, 3.0, 5.5], [1.0, 3.0, 5.5]])), ('uppere14', c.project([[0.0, 2.0, 5.5], [0.0, 3.0, 5.5]])), ('uppere15', c.project([[1.0, 2.0, 5.5], [1.0, 3.0, 5.5]])), ('uppere16', c.project([[1.0, 0.0, 3.5], [2.0, 0.0, 3.5]])), ('uppere17', c.project([[1.0, 0.0, 4.5], [2.0, 0.0, 4.5]])), ('uppere18', c.project([[2.0, 0.0, 3.5], [2.0, 0.0, 4.5]])), ('uppere19', c.project([[1.0, 0.0, 5.5], [2.0, 0.0, 5.5]])), ('uppere20', c.project([[1.0, 1.0, 5.5], [2.0, 1.0, 5.5]])), ('uppere21', c.project([[2.0, 0.0, 5.5], [2.0, 1.0, 5.5]])), ('uppere22', c.project([[2.0, 0.0, 4.5], [2.0, 0.0, 5.5]])), ('uppere23', c.project([[1.0, 2.0, 5.5], [2.0, 2.0, 5.5]])), ('uppere24', c.project([[2.0, 1.0, 5.5], [2.0, 2.0, 5.5]])), ('uppere25', c.project([[1.0, 3.0, 5.5], [2.0, 3.0, 5.5]])), ('uppere26', c.project([[2.0, 2.0, 5.5], [2.0, 3.0, 5.5]])), ('uppere27', c.project([[2.0, 0.0, 3.5], [3.0, 0.0, 3.5]])), ('uppere28', c.project([[2.0, 0.0, 4.5], [3.0, 0.0, 4.5]])), ('uppere29', c.project([[3.0, 0.0, 3.5], [3.0, 1.0, 3.5]])), ('uppere30', c.project([[3.0, 0.0, 4.5], [3.0, 1.0, 4.5]])), ('uppere31', c.project([[3.0, 0.0, 3.5], [3.0, 0.0, 4.5]])), ('uppere32', c.project([[3.0, 1.0, 3.5], [3.0, 1.0, 4.5]])), ('uppere33', c.project([[2.0, 0.0, 5.5], [3.0, 0.0, 5.5]])), ('uppere34', c.project([[2.0, 1.0, 5.5], [3.0, 1.0, 5.5]])), ('uppere35', c.project([[3.0, 0.0, 5.5], [3.0, 1.0, 5.5]])), ('uppere36', c.project([[3.0, 0.0, 4.5], [3.0, 0.0, 5.5]])), ('uppere37', c.project([[3.0, 1.0, 4.5], [3.0, 1.0, 5.5]])), ('uppere38', c.project([[3.0, 1.0, 3.5], [3.0, 2.0, 3.5]])), ('uppere39', c.project([[3.0, 1.0, 4.5], [3.0, 2.0, 4.5]])), ('uppere40', c.project([[3.0, 2.0, 3.5], [3.0, 2.0, 4.5]])), ('uppere41', c.project([[2.0, 2.0, 5.5], [3.0, 2.0, 5.5]])), ('uppere42', c.project([[3.0, 1.0, 5.5], [3.0, 2.0, 5.5]])), ('uppere43', c.project([[3.0, 2.0, 4.5], [3.0, 2.0, 5.5]])), ('uppere44', c.project([[3.0, 2.0, 3.5], [3.0, 3.0, 3.5]])), ('uppere45', c.project([[3.0, 2.0, 4.5], [3.0, 3.0, 4.5]])), ('uppere46', c.project([[3.0, 3.0, 3.5], [3.0, 3.0, 4.5]])), ('uppere47', c.project([[2.0, 3.0, 5.5], [3.0, 3.0, 5.5]])), ('uppere48', c.project([[3.0, 2.0, 5.5], [3.0, 3.0, 5.5]])), ('uppere49', c.project([[3.0, 3.0, 4.5], [3.0, 3.0, 5.5]])), ('lowere0', c.project([[0.0, 0.0, 0.0], [1.0, 0.0, 0.0]])), ('lowere1', c.project([[0.0, 0.0, 1.0], [1.0, 0.0, 1.0]])), ('lowere2', c.project([[1.0, 0.0, 1.0], [1.0, 1.0, 1.0]])), ('lowere3', c.project([[0.0, 0.0, 0.0], [0.0, 0.0, 1.0]])), ('lowere4', c.project([[1.0, 0.0, 0.0], [1.0, 0.0, 1.0]])), ('lowere5', c.project([[0.65, 2.0, 1.0], [1.0, 2.0, 1.0]])), ('lowere6', c.project([[1.0, 1.0, 1.0], [1.0, 2.0, 1.0]])), ('lowere7', c.project([[0.3, 3.0, 1.0], [1.0, 3.0, 1.0]])), ('lowere8', c.project([[1.0, 2.0, 1.0], [1.0, 3.0, 1.0]])), ('lowere9', c.project([[1.0, 0.0, 0.0], [2.0, 0.0, 0.0]])), ('lowere10', c.project([[1.0, 0.0, 1.0], [2.0, 0.0, 1.0]])), ('lowere11', c.project([[1.0, 1.0, 1.0], [2.0, 1.0, 1.0]])), ('lowere12', c.project([[2.0, 0.0, 1.0], [2.0, 1.0, 1.0]])), ('lowere13', c.project([[2.0, 0.0, 0.0], [2.0, 0.0, 1.0]])), ('lowere14', c.project([[1.0, 2.0, 1.0], [2.0, 2.0, 1.0]])), ('lowere15', c.project([[2.0, 1.0, 1.0], [2.0, 2.0, 1.0]])), ('lowere16', c.project([[1.0, 3.0, 1.0], [1.65, 3.0, 1.0]])), ('lowere17', c.project([[2.0, 0.0, 0.0], [3.0, 0.0, 0.0]])), ('lowere18', c.project([[2.0, 0.0, 1.0], [3.0, 0.0, 1.0]])), ('lowere19', c.project([[2.0, 1.0, 1.0], [3.0, 1.0, 1.0]])), ('lowere20', c.project([[3.0, 0.0, 0.0], [3.0, 1.0, 0.0]])), ('lowere21', c.project([[3.0, 0.0, 1.0], [3.0, 1.0, 1.0]])), ('lowere22', c.project([[3.0, 0.0, 0.0], [3.0, 0.0, 1.0]])), ('lowere23', c.project([[3.0, 1.0, 0.0], [3.0, 1.0, 1.0]])), ('lowere24', c.project([[2.0, 2.0, 1.0], [3.0, 2.0, 1.0]])), ('lowere25', c.project([[3.0, 1.0, 0.0], [3.0, 2.0, 0.0]])), ('lowere26', c.project([[3.0, 1.0, 1.0], [3.0, 2.0, 1.0]])), ('lowere27', c.project([[3.0, 2.0, 0.0], [3.0, 2.0, 1.0]])), ('lowere28', c.project([[3.0, 2.0, 0.0], [3.0, 3.0, 0.0]])), ('lowere29', c.project([[3.0, 2.0, 1.0], [3.0, 3.0, 1.0]])), ('lowere30', c.project([[3.0, 3.0, 0.0], [3.0, 3.0, 1.0]])), ('lowere31', c.project([[0.0, 0.0, 2.0], [1.0, 0.0, 2.0]])), ('lowere32', c.project([[0.0, 1.0, 2.0], [1.0, 1.0, 2.0]])), ('lowere33', c.project([[0.0, 0.0, 2.0], [0.0, 1.0, 2.0]])), ('lowere34', c.project([[1.0, 0.0, 2.0], [1.0, 1.0, 2.0]])), ('lowere35', c.project([[0.0, 0.0, 1.0], [0.0, 0.0, 2.0]])), ('lowere36', c.project([[1.0, 0.0, 1.0], [1.0, 0.0, 2.0]])), ('lowere37', c.project([[1.0, 1.0, 1.0], [1.0, 1.0, 2.0]])), ('lowere38', c.project([[2.0, 2.0, 2.0], [3.0, 2.0, 2.0]])), ('lowere39', c.project([[2.0, 3.0, 2.0], [3.0, 3.0, 2.0]])), ('lowere40', c.project([[2.0, 2.0, 2.0], [2.0, 3.0, 2.0]])), ('lowere41', c.project([[3.0, 2.0, 2.0], [3.0, 3.0, 2.0]])), ('lowere42', c.project([[2.0, 2.0, 1.0], [2.0, 2.0, 2.0]])), ('lowere43', c.project([[3.0, 2.0, 1.0], [3.0, 2.0, 2.0]])), ('lowere44', c.project([[3.0, 3.0, 1.0], [3.0, 3.0, 2.0]]))]:
                c.line(points, id=object_id, clip_on=False, zorder=3)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Solid79().draw(sys.argv[1] if len(sys.argv) > 1 else None))
