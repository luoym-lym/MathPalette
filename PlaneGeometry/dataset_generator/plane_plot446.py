"""Frozen question Plane446; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane446:

    def __init__(self):
        self.id = 'Plane446'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:2222'
        self.question = 'The figure below shows line $\\ell$ with a regular, infinite, recurring pattern of squares and line segments.\nHow many of the following four kinds of rigid motion transformations of the plane in which this figure is drawn, other than the identity transformation, will transform this figure into itself?\n\nsome rotation around a point of line $\\ell$\nsome translation in the direction parallel to line $\\ell$\nthe reflection across line $\\ell$\nsome reflection across a line perpendicular to line $\\ell$'
        self.answer = '2'
        self.answer_type = 'number'
        self.query = self.question
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane446.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-1.498654751974664, 19.021177526814967], ylim=[-10.259916139394816, 10.259916139394816]) as c:
            c.line([[-1, 0], [18.5, 0]], id='o0')
            c.path([[0, 0], [1, 0], [1, 1], [0, 1], [0, 0]], [1, 2, 2, 2, 79], id='o1')
            c.line([[1, 1], [1.37, 1.37]], id='o2')
            c.path([[2, -1], [3, -1], [3, 0], [2, 0], [2, -1]], [1, 2, 2, 2, 79], id='o3')
            c.line([[2, -1], [1.63, -1.37]], id='o4')
            c.path([[4, 0], [5, 0], [5, 1], [4, 1], [4, 0]], [1, 2, 2, 2, 79], id='o5')
            c.line([[5, 1], [5.37, 1.37]], id='o6')
            c.path([[6, -1], [7, -1], [7, 0], [6, 0], [6, -1]], [1, 2, 2, 2, 79], id='o7')
            c.line([[6, -1], [5.63, -1.37]], id='o8')
            c.path([[8, 0], [9, 0], [9, 1], [8, 1], [8, 0]], [1, 2, 2, 2, 79], id='o9')
            c.line([[9, 1], [9.370000000000001, 1.37]], id='o10')
            c.path([[10, -1], [11, -1], [11, 0], [10, 0], [10, -1]], [1, 2, 2, 2, 79], id='o11')
            c.line([[10, -1], [9.63, -1.37]], id='o12')
            c.path([[12, 0], [13, 0], [13, 1], [12, 1], [12, 0]], [1, 2, 2, 2, 79], id='o13')
            c.line([[13, 1], [13.370000000000001, 1.37]], id='o14')
            c.path([[14, -1], [15, -1], [15, 0], [14, 0], [14, -1]], [1, 2, 2, 2, 79], id='o15')
            c.line([[14, -1], [13.63, -1.37]], id='o16')
            c.path([[16, 0], [17, 0], [17, 1], [16, 1], [16, 0]], [1, 2, 2, 2, 79], id='o17')
            for object_id, points in [('o18', [[17, 1], [17.37, 1.37]]), ('o19', [[-1, 0], [-0.8, 0.2]]), ('o20', [[-1, 0], [-0.8, -0.2]]), ('o21', [[18.5, 0], [18.3, 0.2]]), ('o22', [[18.5, 0], [18.3, -0.2]])]:
                c.line(points, id=object_id)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane446().draw(sys.argv[1] if len(sys.argv) > 1 else None))
