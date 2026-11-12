"""Frozen question Solid114; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Solid114:

    def __init__(self):
        self.id = 'Solid114'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:443'
        self.question = 'A cubical aquarium has edges $3 \\mathrm{dm}$ long and contains some cubes with edges $1 \\mathrm{dm}$ long, arranged as shown. How many more such cubes can fit in the aquarium?'
        self.answer = '17'
        self.answer_type = 'number'
        self.query = self.question
        self.points = {'aquarium000': [0, 0, 0],
         'aquarium001': [0, 0, 3],
         'aquarium010': [0, 3, 0],
         'aquarium011': [0, 3, 3],
         'aquarium100': [3, 0, 0],
         'aquarium101': [3, 0, 3],
         'aquarium110': [3, 3, 0],
         'aquarium111': [3, 3, 3]}
        self.subject = 'SolidGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'SolidGeometry' / 'dataset_generator/scenes/Solid114.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('SolidGeometry', self.id, variant, output_path)
        with Canvas(SOLID, xlim=[-0.10086589209028052, 4.156997796160048], ylim=[-0.1069977961600479, 4.15086589209028], projection=[[1, 0.35, 0], [0, 0.35, 1]], origin=[0, 0, 0], offset=[0, 0]) as c:
            for object_id, points in [('stairse0', c.project([[0.0, 0.0, 0.0], [1.0, 0.0, 0.0]])), ('stairse1', c.project([[0.0, 0.0, 1.0], [1.0, 0.0, 1.0]])), ('stairse2', c.project([[0.0, 1.0, 1.0], [1.0, 1.0, 1.0]])), ('stairse3', c.project([[0.0, 0.0, 1.0], [0.0, 1.0, 1.0]])), ('stairse4', c.project([[1.0, 0.0, 0.0], [1.0, 1.0, 0.0]])), ('stairse5', c.project([[1.0, 0.0, 1.0], [1.0, 1.0, 1.0]])), ('stairse6', c.project([[0.0, 0.0, 0.0], [0.0, 0.0, 1.0]])), ('stairse7', c.project([[1.0, 0.0, 0.0], [1.0, 0.0, 1.0]])), ('stairse8', c.project([[1.0, 1.0, 0.0], [1.0, 1.0, 1.0]])), ('stairse9', c.project([[1.0, 1.0, 1.0], [1.0, 2.0, 1.0]])), ('stairse10', c.project([[0.0, 1.0, 2.0], [1.0, 1.0, 2.0]])), ('stairse11', c.project([[0.0, 2.0, 2.0], [1.0, 2.0, 2.0]])), ('stairse12', c.project([[0.0, 1.0, 2.0], [0.0, 2.0, 2.0]])), ('stairse13', c.project([[1.0, 1.0, 2.0], [1.0, 2.0, 2.0]])), ('stairse14', c.project([[0.0, 1.0, 1.0], [0.0, 1.0, 2.0]])), ('stairse15', c.project([[1.0, 1.0, 1.0], [1.0, 1.0, 2.0]])), ('stairse16', c.project([[1.0, 2.0, 1.0], [1.0, 2.0, 2.0]])), ('stairse17', c.project([[1.0, 2.0, 2.0], [1.0, 3.0, 2.0]])), ('stairse18', c.project([[0.0, 2.0, 3.0], [1.0, 2.0, 3.0]])), ('stairse19', c.project([[0.0, 3.0, 3.0], [1.0, 3.0, 3.0]])), ('stairse20', c.project([[0.0, 2.0, 3.0], [0.0, 3.0, 3.0]])), ('stairse21', c.project([[1.0, 2.0, 3.0], [1.0, 3.0, 3.0]])), ('stairse22', c.project([[0.0, 2.0, 2.0], [0.0, 2.0, 3.0]])), ('stairse23', c.project([[1.0, 2.0, 2.0], [1.0, 2.0, 3.0]])), ('stairse24', c.project([[1.0, 3.0, 2.0], [1.0, 3.0, 3.0]])), ('stairse25', c.project([[1.0, 1.0, 0.0], [2.0, 1.0, 0.0]])), ('stairse26', c.project([[1.0, 1.0, 1.0], [2.0, 1.0, 1.0]])), ('stairse27', c.project([[1.0, 2.0, 1.0], [2.0, 2.0, 1.0]])), ('stairse28', c.project([[2.0, 1.0, 0.0], [2.0, 2.0, 0.0]])), ('stairse29', c.project([[2.0, 1.0, 1.0], [2.0, 2.0, 1.0]])), ('stairse30', c.project([[2.0, 1.0, 0.0], [2.0, 1.0, 1.0]])), ('stairse31', c.project([[2.0, 2.0, 0.0], [2.0, 2.0, 1.0]])), ('stairse32', c.project([[2.0, 2.0, 1.0], [2.0, 3.0, 1.0]])), ('stairse33', c.project([[1.0, 2.0, 2.0], [2.0, 2.0, 2.0]])), ('stairse34', c.project([[1.0, 3.0, 2.0], [2.0, 3.0, 2.0]])), ('stairse35', c.project([[2.0, 2.0, 2.0], [2.0, 3.0, 2.0]])), ('stairse36', c.project([[2.0, 2.0, 1.0], [2.0, 2.0, 2.0]])), ('stairse37', c.project([[2.0, 3.0, 1.0], [2.0, 3.0, 2.0]])), ('stairse38', c.project([[2.0, 2.0, 0.0], [3.0, 2.0, 0.0]])), ('stairse39', c.project([[2.0, 2.0, 1.0], [3.0, 2.0, 1.0]])), ('stairse40', c.project([[2.0, 3.0, 1.0], [3.0, 3.0, 1.0]])), ('stairse41', c.project([[3.0, 2.0, 0.0], [3.0, 3.0, 0.0]])), ('stairse42', c.project([[3.0, 2.0, 1.0], [3.0, 3.0, 1.0]])), ('stairse43', c.project([[3.0, 2.0, 0.0], [3.0, 2.0, 1.0]])), ('stairse44', c.project([[3.0, 3.0, 0.0], [3.0, 3.0, 1.0]])), ('aquarium000_aquarium100part0', c.project([[0.0, 0.0, 0.0], [3.0, 0.0, 0.0]])), ('aquarium000_aquarium001part0', c.project([[0.0, 0.0, 0.0], [0.0, 0.0, 3.0]])), ('aquarium001_aquarium101part0', c.project([[0.0, 0.0, 3.0], [3.0, 0.0, 3.0]])), ('aquarium001_aquarium011part0', c.project([[0.0, 0.0, 3.0], [0.0, 3.0, 3.0]])), ('aquarium011_aquarium111part0', c.project([[0.0, 3.0, 3.0], [3.0, 3.0, 3.0]])), ('aquarium100_aquarium110part0', c.project([[3.0, 0.0, 0.0], [3.0, 3.0, 0.0]])), ('aquarium100_aquarium101part0', c.project([[3.0, 0.0, 0.0], [3.0, 0.0, 3.0]])), ('aquarium101_aquarium111part0', c.project([[3.0, 0.0, 3.0], [3.0, 3.0, 3.0]])), ('aquarium110_aquarium111part0', c.project([[3.0, 3.0, 0.0], [3.0, 3.0, 3.0]]))]:
                c.line(points, id=object_id, clip_on=False, zorder=3)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Solid114().draw(sys.argv[1] if len(sys.argv) > 1 else None))
