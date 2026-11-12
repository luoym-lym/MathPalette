"""Frozen question Plane285; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane285:

    def __init__(self):
        self.id = 'Plane285'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:855'
        self.question = '$A 10 \\mathrm{~cm}$ long piece of wire is folded so that every part is equally long (see diagram). The wire is then cut through in the two positions marked. How long are the three pieces created in this way?\nChoices:\nA:$2 \\mathrm{~cm}, 3 \\mathrm{~cm}, 5 \\mathrm{~cm}$\nB:$2 \\mathrm{~cm}, 2 \\mathrm{~cm}, 6 \\mathrm{~cm}$\nC:$1 \\mathrm{~cm}, 4 \\mathrm{~cm}, 5 \\mathrm{~cm}$\nD:$1 \\mathrm{~cm}, 3 \\mathrm{~cm}, 6 \\mathrm{~cm}$\nE:$3 \\mathrm{~cm}, 3 \\mathrm{~cm}, 4 \\mathrm{~cm}$'
        self.answer = 'A'
        self.answer_type = 'choice'
        self.choices = {'A': '$2 \\mathrm{~cm}, 3 \\mathrm{~cm}, 5 \\mathrm{~cm}$',
         'B': '$2 \\mathrm{~cm}, 2 \\mathrm{~cm}, 6 \\mathrm{~cm}$',
         'C': '$1 \\mathrm{~cm}, 4 \\mathrm{~cm}, 5 \\mathrm{~cm}$',
         'D': '$1 \\mathrm{~cm}, 3 \\mathrm{~cm}, 6 \\mathrm{~cm}$',
         'E': '$3 \\mathrm{~cm}, 3 \\mathrm{~cm}, 4 \\mathrm{~cm}$'}
        self.query = self.question
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane285.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-0.16300097809036096, 6.6650652911657], ylim=[-2.8960891319973987, 3.931977137258662]) as c:
            for object_id, points in [('o0', [[0.0, 0], [0.65, 2.5]]), ('o1', [[0.65, 2.5], [1.3, 0]]), ('o2', [[1.3, 0], [1.9500000000000002, 2.5]]), ('o3', [[1.9500000000000002, 2.5], [2.6, 0]]), ('o4', [[2.6, 0], [3.25, 2.5]]), ('o5', [[3.25, 2.5], [3.9000000000000004, 0]]), ('o6', [[3.9000000000000004, 0], [4.55, 2.5]]), ('o7', [[4.55, 2.5], [5.2, 0]]), ('o8', [[5.2, 0], [5.8500000000000005, 2.5]]), ('o9', [[5.8500000000000005, 2.5], [6.5, 0]])]:
                c.line(points, id=object_id)
            c.line([[1.95, 2], [1.95, 2.9]], id='o10', linestyle=(0, [4, 3]))
            c.line([[5.2, -0.6], [5.2, 1.1]], id='o11', linestyle=(0, [4, 3]))
            c.circle([4.95, -1.65], 0.2, id='o12')
            c.circle([5.45, -1.65], 0.2, id='o13')
            c.line([[4.98, -1.48], [5.5, -0.75]], id='o14')
            c.line([[5.42, -1.48], [4.9, -0.75]], id='o15')
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane285().draw(sys.argv[1] if len(sys.argv) > 1 else None))
