"""Frozen question Solid110; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Solid110:

    def __init__(self):
        self.id = 'Solid110'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:400'
        self.question = 'The construction in the picture is built of cubes of the same size and weighs 189 grams. How many grams does one cube weigh?'
        self.answer = '21'
        self.answer_type = 'number'
        self.query = self.question
        self.subject = 'SolidGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'SolidGeometry' / 'dataset_generator/scenes/Solid110.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('SolidGeometry', self.id, variant, output_path)
        with Canvas(SOLID, xlim=[0.2167574018066678, 5.841342767766978], ylim=[-1.4663427677669767, 4.158242598193333], projection=[[1, 0.35, 0], [0, 0.35, 1]], origin=[0, 0, 0], offset=[0, 0]) as c:
            for object_id, points in [('structuree0', c.project([[0.0, 1.0, 0.0], [0.65, 1.0, 0.0]])), ('structuree1', c.project([[0.0, 1.0, 1.0], [1.0, 1.0, 1.0]])), ('structuree2', c.project([[0.0, 2.0, 1.0], [0.65, 2.0, 1.0]])), ('structuree3', c.project([[0.0, 1.0, 1.0], [0.0, 2.0, 1.0]])), ('structuree4', c.project([[0.0, 1.0, 0.0], [0.0, 1.0, 1.0]])), ('structuree5', c.project([[1.0, 1.0, 1.0], [2.0, 1.0, 1.0]])), ('structuree6', c.project([[2.0, 1.0, 1.0], [2.0, 2.0, 1.0]])), ('structuree7', c.project([[2.0, 1.0, 0.0], [2.0, 1.0, 1.0]])), ('structuree8', c.project([[2.0, 1.0, 0.0], [2.65, 1.0, 0.0]])), ('structuree9', c.project([[2.0, 1.0, 1.0], [3.0, 1.0, 1.0]])), ('structuree10', c.project([[2.0, 2.0, 1.0], [2.65, 2.0, 1.0]])), ('structuree11', c.project([[3.0, 1.0, 1.0], [4.0, 1.0, 1.0]])), ('structuree12', c.project([[4.0, 1.0, 1.0], [4.0, 2.0, 1.0]])), ('structuree13', c.project([[4.0, 1.0, 0.0], [4.0, 1.0, 1.0]])), ('structuree14', c.project([[4.0, 1.0, 0.0], [5.0, 1.0, 0.0]])), ('structuree15', c.project([[4.0, 1.0, 1.0], [5.0, 1.0, 1.0]])), ('structuree16', c.project([[4.0, 2.0, 1.0], [5.0, 2.0, 1.0]])), ('structuree17', c.project([[5.0, 1.0, 0.0], [5.0, 2.0, 0.0]])), ('structuree18', c.project([[5.0, 1.0, 1.0], [5.0, 2.0, 1.0]])), ('structuree19', c.project([[5.0, 1.0, 0.0], [5.0, 1.0, 1.0]])), ('structuree20', c.project([[5.0, 2.0, 0.0], [5.0, 2.0, 1.0]])), ('structuree21', c.project([[1.0, 0.0, 0.0], [2.0, 0.0, 0.0]])), ('structuree22', c.project([[1.0, 0.0, 1.0], [2.0, 0.0, 1.0]])), ('structuree23', c.project([[1.0, 0.0, 1.0], [1.0, 1.0, 1.0]])), ('structuree24', c.project([[2.0, 0.0, 0.0], [2.0, 1.0, 0.0]])), ('structuree25', c.project([[2.0, 0.0, 1.0], [2.0, 1.0, 1.0]])), ('structuree26', c.project([[1.0, 0.0, 0.0], [1.0, 0.0, 1.0]])), ('structuree27', c.project([[2.0, 0.0, 0.0], [2.0, 0.0, 1.0]])), ('structuree28', c.project([[3.0, 0.0, 0.0], [4.0, 0.0, 0.0]])), ('structuree29', c.project([[3.0, 0.0, 1.0], [4.0, 0.0, 1.0]])), ('structuree30', c.project([[3.0, 0.0, 1.0], [3.0, 1.0, 1.0]])), ('structuree31', c.project([[4.0, 0.0, 0.0], [4.0, 1.0, 0.0]])), ('structuree32', c.project([[4.0, 0.0, 1.0], [4.0, 1.0, 1.0]])), ('structuree33', c.project([[3.0, 0.0, 0.0], [3.0, 0.0, 1.0]])), ('structuree34', c.project([[4.0, 0.0, 0.0], [4.0, 0.0, 1.0]])), ('structuree35', c.project([[1.0, 1.0, 2.0], [2.0, 1.0, 2.0]])), ('structuree36', c.project([[1.0, 2.0, 2.0], [2.0, 2.0, 2.0]])), ('structuree37', c.project([[1.0, 1.0, 2.0], [1.0, 2.0, 2.0]])), ('structuree38', c.project([[2.0, 1.0, 2.0], [2.0, 2.0, 2.0]])), ('structuree39', c.project([[1.0, 1.0, 1.0], [1.0, 1.0, 2.0]])), ('structuree40', c.project([[2.0, 1.0, 1.0], [2.0, 1.0, 2.0]])), ('structuree41', c.project([[2.0, 2.0, 1.0], [2.0, 2.0, 2.0]])), ('structuree42', c.project([[3.0, 1.0, 2.0], [4.0, 1.0, 2.0]])), ('structuree43', c.project([[3.0, 2.0, 2.0], [4.0, 2.0, 2.0]])), ('structuree44', c.project([[3.0, 1.0, 2.0], [3.0, 2.0, 2.0]])), ('structuree45', c.project([[4.0, 1.0, 2.0], [4.0, 2.0, 2.0]])), ('structuree46', c.project([[3.0, 1.0, 1.0], [3.0, 1.0, 2.0]])), ('structuree47', c.project([[4.0, 1.0, 1.0], [4.0, 1.0, 2.0]])), ('structuree48', c.project([[4.0, 2.0, 1.0], [4.0, 2.0, 2.0]]))]:
                c.line(points, id=object_id, clip_on=False, zorder=3)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Solid110().draw(sys.argv[1] if len(sys.argv) > 1 else None))
