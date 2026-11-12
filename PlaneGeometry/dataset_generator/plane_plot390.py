"""Frozen question Plane390; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane390:

    def __init__(self):
        self.id = 'Plane390'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:1604'
        self.question = 'The diagram shows a shaded quadrilateral $P Q R S$ drawn on a grid. Each cell of the grid has sides of length $2 \\mathrm{~cm}$. What is the area of quadrilateral $P Q R S$?\nChoices:\nA:$96 \\mathrm{~cm}^{2}$\nB:$84 \\mathrm{~cm}^{2}$\nC:$76 \\mathrm{~cm}^{2}$\nD:$88 \\mathrm{~cm}^{2}$\nE:$104 \\mathrm{~cm}^{2}$'
        self.answer = 'B'
        self.answer_type = 'choice'
        self.choices = {'A': '$96 \\mathrm{~cm}^{2}$', 'B': '$84 \\mathrm{~cm}^{2}$', 'C': '$76 \\mathrm{~cm}^{2}$', 'D': '$88 \\mathrm{~cm}^{2}$', 'E': '$104 \\mathrm{~cm}^{2}$'}
        self.query = self.question
        self._geometry_01 = [('g0_0_0', [[0.0, 0.0], [0.0, 7.0]]),
         ('g0_1_0', [[1.0, 0.0], [1.0, 7.0]]),
         ('g0_2_0', [[2.0, 0.0], [2.0, 2.0]]),
         ('g0_2_1', [[2.0, 5.857142857142857], [2.0, 7.0]]),
         ('g0_3_0', [[3.0, 0.0], [3.0, 1.6666666666666667]]),
         ('g0_3_1', [[3.0, 5.714285714285714], [3.0, 7.0]]),
         ('g0_4_0', [[4.0, 0.0], [4.0, 1.3333333333333335]]),
         ('g0_4_1', [[4.0, 5.571428571428571], [4.0, 7.0]]),
         ('g0_5_0', [[5.0, 0.0], [5.0, 1.0]]),
         ('g0_5_1', [[5.0, 5.428571428571429], [5.0, 7.0]]),
         ('g0_6_0', [[6.0, 0.0], [6.0, 2.333333333333333]]),
         ('g0_6_1', [[6.0, 5.285714285714286], [6.0, 7.0]]),
         ('g0_7_0', [[7.0, 0.0], [7.0, 3.6666666666666665]]),
         ('g0_7_1', [[7.0, 5.142857142857143], [7.0, 7.0]]),
         ('g0_8_0', [[8.0, 0.0], [8.0, 7.0]]),
         ('g0_9_0', [[9.0, 0.0], [9.0, 7.0]]),
         ('g1_0_0', [[0.0, 0.0], [9.0, 0.0]]),
         ('g1_1_0', [[0.0, 1.0], [9.0, 1.0]]),
         ('g1_2_0', [[0.0, 2.0], [2.0, 2.0]]),
         ('g1_2_1', [[5.75, 2.0], [9.0, 2.0]]),
         ('g1_3_0', [[0.0, 3.0], [1.75, 3.0]]),
         ('g1_3_1', [[6.5, 3.0], [9.0, 3.0]]),
         ('g1_4_0', [[0.0, 4.0], [1.5, 4.0]]),
         ('g1_4_1', [[7.25, 4.0], [9.0, 4.0]]),
         ('g1_5_0', [[0.0, 5.0], [1.25, 5.0]]),
         ('g1_5_1', [[8.0, 5.0], [9.0, 5.0]]),
         ('g1_6_0', [[0.0, 6.0], [9.0, 6.0]]),
         ('g1_7_0', [[0.0, 7.0], [9.0, 7.0]])]
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane390.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-0.2230502095313236, 9.238034935319352], ylim=[-1.2380295515920041, 8.223055593258671], axes_position=[0.05, 0.05, 0.9, 0.9], coordinate_axes=False) as c:
            c.path([[1.0, 6.0], [2.0, 2.0], [5.0, 1.0], [8.0, 5.0], [1.0, 6.0]], [1, 2, 2, 2, 79], id='grey', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45], linewidth=0.0, capstyle='butt')
            c.path([[1.0, 6.0], [2.0, 2.0], [5.0, 1.0], [8.0, 5.0], [1.0, 6.0]], [1, 2, 2, 2, 79], id='grey', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            for object_id, points in self._geometry_01:
                c.line(points, id=object_id)
            c.text('P', [1.0, 6.0], id='nameP', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[-15, 13], annotation_clip=None)
            c.text('Q', [2.0, 2.0], id='nameQ', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[-10, -12], annotation_clip=None)
            c.text('R', [5.0, 1.0], id='nameR', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[8, -14], annotation_clip=None)
            c.text('S', [8.0, 5.0], id='nameS', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[12, 10], annotation_clip=None)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane390().draw(sys.argv[1] if len(sys.argv) > 1 else None))
