"""Frozen question Plane258; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane258:

    def __init__(self):
        self.id = 'Plane258'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:771'
        self.question = 'The diagram shows squares of different sizes. The side length of the smallest square is $20 \\mathrm{~cm}$. How long is the black line?\nChoices:\nA:$380 \\mathrm{~cm}$\nB:$400 \\mathrm{~cm}$\nC:$420 \\mathrm{~cm}$\nD:$440 \\mathrm{~cm}$\nE:$1680 \\mathrm{~cm}$'
        self.answer = 'C'
        self.answer_type = 'choice'
        self.choices = {'A': '$380 \\mathrm{~cm}$', 'B': '$400 \\mathrm{~cm}$', 'C': '$420 \\mathrm{~cm}$', 'D': '$440 \\mathrm{~cm}$', 'E': '$1680 \\mathrm{~cm}$'}
        self.query = self.question
        self._geometry_01 = [('square0_0', [[0.0, 6.0], [1.0, 6.0]]),
         ('square0_1', [[1.0, 6.0], [1.0, 7.0]]),
         ('square0_2', [[1.0, 7.0], [0.0, 7.0]]),
         ('square0_3', [[0.0, 7.0], [0.0, 6.0]]),
         ('square1_0', [[1.0, 6.0], [2.0, 6.0]]),
         ('square1_1', [[2.0, 6.0], [2.0, 7.0]]),
         ('square1_2', [[2.0, 7.0], [1.0, 7.0]]),
         ('square1_3', [[1.0, 7.0], [1.0, 6.0]]),
         ('square2_0', [[0.0, 4.0], [2.0, 4.0]]),
         ('square2_1', [[2.0, 4.0], [2.0, 6.0]]),
         ('square2_2', [[2.0, 6.0], [0.0, 6.0]]),
         ('square2_3', [[0.0, 6.0], [0.0, 4.0]]),
         ('square3_0', [[2.0, 4.0], [5.0, 4.0]]),
         ('square3_1', [[5.0, 4.0], [5.0, 7.0]]),
         ('square3_2', [[5.0, 7.0], [2.0, 7.0]]),
         ('square3_3', [[2.0, 7.0], [2.0, 4.0]]),
         ('square4_0', [[0.0, 2.0], [2.0, 2.0]]),
         ('square4_1', [[2.0, 2.0], [2.0, 4.0]]),
         ('square4_2', [[2.0, 4.0], [0.0, 4.0]]),
         ('square4_3', [[0.0, 4.0], [0.0, 2.0]]),
         ('square5_0', [[2.0, 3.0], [3.0, 3.0]]),
         ('square5_1', [[3.0, 3.0], [3.0, 4.0]]),
         ('square5_2', [[3.0, 4.0], [2.0, 4.0]]),
         ('square5_3', [[2.0, 4.0], [2.0, 3.0]]),
         ('square6_0', [[3.0, 3.0], [4.0, 3.0]]),
         ('square6_1', [[4.0, 3.0], [4.0, 4.0]]),
         ('square6_2', [[4.0, 4.0], [3.0, 4.0]]),
         ('square6_3', [[3.0, 4.0], [3.0, 3.0]]),
         ('square7_0', [[4.0, 3.0], [5.0, 3.0]]),
         ('square7_1', [[5.0, 3.0], [5.0, 4.0]]),
         ('square7_2', [[5.0, 4.0], [4.0, 4.0]]),
         ('square7_3', [[4.0, 4.0], [4.0, 3.0]]),
         ('square8_0', [[0.0, 0.0], [2.0, 0.0]]),
         ('square8_1', [[2.0, 0.0], [2.0, 2.0]]),
         ('square8_2', [[2.0, 2.0], [0.0, 2.0]]),
         ('square8_3', [[0.0, 2.0], [0.0, 0.0]]),
         ('square9_0', [[2.0, 0.0], [5.0, 0.0]]),
         ('square9_1', [[5.0, 0.0], [5.0, 3.0]]),
         ('square9_2', [[5.0, 3.0], [2.0, 3.0]]),
         ('square9_3', [[2.0, 3.0], [2.0, 0.0]])]
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane258.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-1.1785007324251682, 6.1828046738412175], ylim=[-0.18350058239477285, 7.177804823871613], axes_position=[0.05, 0.05, 0.9, 0.9], coordinate_axes=False) as c:
            for object_id, points in self._geometry_01:
                c.line(points, id=object_id, color='#999999')
            for object_id, points in [('black_path0', [[1.0, 7.0], [1.0, 6.0]]), ('black_path1', [[1.0, 6.0], [2.0, 6.0]]), ('black_path2', [[2.0, 6.0], [2.0, 4.0]]), ('black_path3', [[2.0, 4.0], [0.0, 4.0]]), ('black_path4', [[0.0, 4.0], [0.0, 2.0]]), ('black_path5', [[0.0, 2.0], [2.0, 2.0]]), ('black_path6', [[2.0, 2.0], [2.0, 0.0]]), ('black_path7', [[2.0, 0.0], [5.0, 0.0]]), ('black_path8', [[5.0, 0.0], [5.0, 4.0]]), ('black_path9', [[5.0, 4.0], [4.0, 4.0]]), ('black_path10', [[4.0, 4.0], [4.0, 3.0]])]:
                c.line(points, id=object_id)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane258().draw(sys.argv[1] if len(sys.argv) > 1 else None))
