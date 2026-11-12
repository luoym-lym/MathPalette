"""Frozen question Plane323; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane323:

    def __init__(self):
        self.id = 'Plane323'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:1025'
        self.question = 'The rectangle shown on the right is divided into 7 squares. Each grey square has side length 8. What is the side length of the large white square?'
        self.answer = '18'
        self.answer_type = 'number'
        self.query = self.question
        self._geometry_01 = [('hatch0_-12', [[25.2, 0.0], [26, 0.8000000000000007]]),
         ('hatch0_-11', [[24.6, 0.0], [26, 1.4000000000000004]]),
         ('hatch0_-10', [[24.0, 0.0], [26, 2.0]]),
         ('hatch0_-9', [[23.4, 0.0], [26, 2.6000000000000005]]),
         ('hatch0_-8', [[22.8, 0.0], [26, 3.2]]),
         ('hatch0_-7', [[22.2, 0.0], [26, 3.8]]),
         ('hatch0_-6', [[21.6, 0.0], [26, 4.4]]),
         ('hatch0_-5', [[21.0, 0.0], [26, 5.0]]),
         ('hatch0_-4', [[20.4, 0.0], [26, 5.6]]),
         ('hatch0_-3', [[19.8, 0.0], [26, 6.2]]),
         ('hatch0_-2', [[19.2, 0.0], [26, 6.8]]),
         ('hatch0_-1', [[18.6, 0.0], [26, 7.4]]),
         ('hatch0_0', [[18, 0.0], [26, 8.0]]),
         ('hatch0_1', [[18, 0.6], [25.4, 8.0]]),
         ('hatch0_2', [[18, 1.2], [24.8, 8.0]]),
         ('hatch0_3', [[18, 1.7999999999999998], [24.2, 8.0]]),
         ('hatch0_4', [[18, 2.4], [23.6, 8.0]]),
         ('hatch0_5', [[18, 3.0], [23.0, 8.0]]),
         ('hatch0_6', [[18, 3.5999999999999996], [22.4, 8.0]]),
         ('hatch0_7', [[18, 4.2], [21.8, 8.0]]),
         ('hatch0_8', [[18, 4.8], [21.2, 8.0]]),
         ('hatch0_9', [[18, 5.3999999999999995], [20.6, 8.0]]),
         ('hatch0_10', [[18, 6.0], [20.0, 8.0]]),
         ('hatch0_11', [[18, 6.6], [19.4, 8.0]]),
         ('hatch0_12', [[18, 7.199999999999999], [18.8, 8.0]])]
        self._geometry_02 = [('hatch1_-12', [[25.2, 8.0], [26, 8.8]]),
         ('hatch1_-11', [[24.6, 8.0], [26, 9.4]]),
         ('hatch1_-10', [[24.0, 8.0], [26, 10.0]]),
         ('hatch1_-9', [[23.4, 7.999999999999999], [26, 10.600000000000001]]),
         ('hatch1_-8', [[22.8, 8.0], [26, 11.2]]),
         ('hatch1_-7', [[22.2, 7.999999999999999], [26, 11.8]]),
         ('hatch1_-6', [[21.6, 8.0], [26, 12.4]]),
         ('hatch1_-5', [[21.0, 8.0], [26, 13.0]]),
         ('hatch1_-4', [[20.4, 8.0], [26, 13.6]]),
         ('hatch1_-3', [[19.8, 8.0], [26, 14.2]]),
         ('hatch1_-2', [[19.2, 7.999999999999999], [26, 14.8]]),
         ('hatch1_-1', [[18.6, 8.0], [26, 15.4]]),
         ('hatch1_0', [[18, 8.0], [26, 16.0]]),
         ('hatch1_1', [[18, 8.6], [25.4, 16.0]]),
         ('hatch1_2', [[18, 9.2], [24.8, 16.0]]),
         ('hatch1_3', [[18, 9.8], [24.2, 16.0]]),
         ('hatch1_4', [[18, 10.4], [23.6, 16.0]]),
         ('hatch1_5', [[18, 11.0], [23.0, 16.0]]),
         ('hatch1_6', [[18, 11.6], [22.4, 16.0]]),
         ('hatch1_7', [[18, 12.2], [21.8, 16.0]]),
         ('hatch1_8', [[18, 12.8], [21.2, 16.0]]),
         ('hatch1_9', [[18, 13.399999999999999], [20.6, 16.0]]),
         ('hatch1_10', [[18, 14.0], [20.0, 16.0]]),
         ('hatch1_11', [[18, 14.6], [19.4, 16.0]]),
         ('hatch1_12', [[18, 15.2], [18.8, 16.0]])]
        self._geometry_03 = [('hatch2_-12', [[25.2, 16.0], [26, 16.8]]),
         ('hatch2_-11', [[24.6, 16.0], [26, 17.4]]),
         ('hatch2_-10', [[24.0, 16.0], [26, 18.0]]),
         ('hatch2_-9', [[23.4, 16.0], [26, 18.6]]),
         ('hatch2_-8', [[22.8, 16.0], [26, 19.2]]),
         ('hatch2_-7', [[22.2, 16.0], [26, 19.8]]),
         ('hatch2_-6', [[21.6, 16.0], [26, 20.4]]),
         ('hatch2_-5', [[21.0, 16.0], [26, 21.0]]),
         ('hatch2_-4', [[20.4, 15.999999999999998], [26, 21.6]]),
         ('hatch2_-3', [[19.8, 16.0], [26, 22.2]]),
         ('hatch2_-2', [[19.2, 16.0], [26, 22.8]]),
         ('hatch2_-1', [[18.6, 16.0], [26, 23.4]]),
         ('hatch2_0', [[18, 16.0], [26, 24.0]]),
         ('hatch2_1', [[18, 16.6], [25.4, 24.0]]),
         ('hatch2_2', [[18, 17.2], [24.8, 24.0]]),
         ('hatch2_3', [[18, 17.8], [24.2, 24.0]]),
         ('hatch2_4', [[18, 18.4], [23.6, 24.0]]),
         ('hatch2_5', [[18, 19.0], [23.0, 24.0]]),
         ('hatch2_6', [[18, 19.6], [22.4, 24.0]]),
         ('hatch2_7', [[18, 20.2], [21.8, 24.0]]),
         ('hatch2_8', [[18, 20.8], [21.2, 24.0]]),
         ('hatch2_9', [[18, 21.4], [20.6, 24.0]]),
         ('hatch2_10', [[18, 22.0], [20.0, 24.0]]),
         ('hatch2_11', [[18, 22.6], [19.4, 24.0]]),
         ('hatch2_12', [[18, 23.2], [18.8, 24.0]])]
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane323.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-0.6362021313635111, 26.673747216419493], ylim=[-1.6737472164194962, 25.636202131363508]) as c:
            for object_id, vertices, codes in [('large_white', [[0, 6], [18, 6], [18, 24], [0, 24], [0, 6]], [1, 2, 2, 2, 79]), ('small_white0', [[0, 0], [6, 0], [6, 6], [0, 6], [0, 0]], [1, 2, 2, 2, 79]), ('small_white1', [[6, 0], [12, 0], [12, 6], [6, 6], [6, 0]], [1, 2, 2, 2, 79]), ('small_white2', [[12, 0], [18, 0], [18, 6], [12, 6], [12, 0]], [1, 2, 2, 2, 79]), ('hatched_square0', [[18, 0], [26, 0], [26, 8], [18, 8], [18, 0]], [1, 2, 2, 2, 79])]:
                c.path(vertices, codes, id=object_id)
            for object_id, points in self._geometry_01:
                c.line(points, id=object_id)
            c.path([[18, 8], [26, 8], [26, 16], [18, 16], [18, 8]], [1, 2, 2, 2, 79], id='hatched_square1')
            for object_id, points in self._geometry_02:
                c.line(points, id=object_id)
            c.path([[18, 16], [26, 16], [26, 24], [18, 24], [18, 16]], [1, 2, 2, 2, 79], id='hatched_square2')
            for object_id, points in self._geometry_03:
                c.line(points, id=object_id)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane323().draw(sys.argv[1] if len(sys.argv) > 1 else None))
