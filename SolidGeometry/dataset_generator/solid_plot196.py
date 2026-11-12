"""Frozen question Solid196; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Solid196:

    def __init__(self):
        self.id = 'Solid196'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:1857'
        self.question = 'Four cubes, each with surface area $24 \\mathrm{~cm}^{2}$, are placed together to form a cuboid as shown. What is the surface area of this cuboid, in $\\mathrm{cm}^{2}$?'
        self.answer = '64'
        self.answer_type = 'number'
        self.query = self.question
        self.subject = 'SolidGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'SolidGeometry' / 'dataset_generator/scenes/Solid196.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('SolidGeometry', self.id, variant, output_path)
        with Canvas(SOLID, xlim=[-0.05852712257090298, 2.412085140981756], ylim=[-0.06208514098175533, 2.4085271225709035], projection=[[1, 0.35, 0], [0, 0.35, 1]], origin=[0, 0, 0], offset=[0, 0]) as c:
            for object_id, points in [('slabe0', c.project([[0.0, 0.0, 0.0], [1.0, 0.0, 0.0]])), ('slabe1', c.project([[0.0, 0.0, 1.0], [1.0, 0.0, 1.0]])), ('slabe2', c.project([[0.0, 0.0, 0.0], [0.0, 0.0, 1.0]])), ('slabe3', c.project([[1.0, 0.0, 0.0], [1.0, 0.0, 1.0]])), ('slabe4', c.project([[0.0, 0.0, 2.0], [1.0, 0.0, 2.0]])), ('slabe5', c.project([[0.0, 1.0, 2.0], [1.0, 1.0, 2.0]])), ('slabe6', c.project([[0.0, 0.0, 2.0], [0.0, 1.0, 2.0]])), ('slabe7', c.project([[1.0, 0.0, 2.0], [1.0, 1.0, 2.0]])), ('slabe8', c.project([[0.0, 0.0, 1.0], [0.0, 0.0, 2.0]])), ('slabe9', c.project([[1.0, 0.0, 1.0], [1.0, 0.0, 2.0]])), ('slabe10', c.project([[1.0, 0.0, 0.0], [2.0, 0.0, 0.0]])), ('slabe11', c.project([[1.0, 0.0, 1.0], [2.0, 0.0, 1.0]])), ('slabe12', c.project([[2.0, 0.0, 0.0], [2.0, 1.0, 0.0]])), ('slabe13', c.project([[2.0, 0.0, 1.0], [2.0, 1.0, 1.0]])), ('slabe14', c.project([[2.0, 0.0, 0.0], [2.0, 0.0, 1.0]])), ('slabe15', c.project([[2.0, 1.0, 0.0], [2.0, 1.0, 1.0]])), ('slabe16', c.project([[1.0, 0.0, 2.0], [2.0, 0.0, 2.0]])), ('slabe17', c.project([[1.0, 1.0, 2.0], [2.0, 1.0, 2.0]])), ('slabe18', c.project([[2.0, 0.0, 2.0], [2.0, 1.0, 2.0]])), ('slabe19', c.project([[2.0, 0.0, 1.0], [2.0, 0.0, 2.0]])), ('slabe20', c.project([[2.0, 1.0, 1.0], [2.0, 1.0, 2.0]]))]:
                c.line(points, id=object_id, clip_on=False, zorder=3)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Solid196().draw(sys.argv[1] if len(sys.argv) > 1 else None))
