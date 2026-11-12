"""Frozen question Solid89; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Solid89:

    def __init__(self):
        self.id = 'Solid89'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:180'
        self.question = 'A $3 \\times 3 \\times 3$ cube weighs 810 grams. Three holes are drilled through it as shown, each in the shape of a $1 \\times 1 \\times 3$ rectangular parallelepiped. What is the weight of the remaining solid?\nChoices:\nA:$540 \\mathrm{~g}$\nB:$570 \\mathrm{~g}$\nC:$600 \\mathrm{~g}$\nD:$630 \\mathrm{~g}$\nE:$660 \\mathrm{~g}$'
        self.answer = 'C'
        self.answer_type = 'choice'
        self.choices = {'A': '$540 \\mathrm{~g}$', 'B': '$570 \\mathrm{~g}$', 'C': '$600 \\mathrm{~g}$', 'D': '$630 \\mathrm{~g}$', 'E': '$660 \\mathrm{~g}$'}
        self.query = self.question
        self.subject = 'SolidGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'SolidGeometry' / 'dataset_generator/scenes/Solid89.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('SolidGeometry', self.id, variant, output_path)
        with Canvas(SOLID, xlim=[-0.10310735635895396, 4.249375524963606], ylim=[-0.10937552496360459, 4.243107356358955], axes_position=[0.05, 0.05, 0.9, 0.9], coordinate_axes=False) as c:
            for object_id, points in [('cube000_cube100', [[0.0, 0.0], [3.0, 0.0]]), ('cube000_cube001', [[0.0, 0.0], [0.0, 3.0]]), ('cube001_cube101', [[0.0, 3.0], [3.0, 3.0]]), ('cube001_cube011', [[0.0, 3.0], [1.1400000000000001, 4.140000000000001]]), ('cube011_cube111', [[1.1400000000000001, 4.140000000000001], [4.14, 4.140000000000001]]), ('cube100_cube110', [[3.0, 0.0], [4.14, 1.1400000000000001]]), ('cube100_cube101', [[3.0, 0.0], [3.0, 3.0]]), ('cube101_cube111', [[3.0, 3.0], [4.14, 4.140000000000001]]), ('cube110_cube111', [[4.14, 1.1400000000000001], [4.14, 4.140000000000001]]), ('frontrim0', [[1.0, 1.0], [2.0, 1.0]]), ('frontrim1', [[2.0, 1.0], [2.0, 2.0]]), ('frontrim2', [[2.0, 2.0], [1.0, 2.0]]), ('frontrim3', [[1.0, 2.0], [1.0, 1.0]]), ('toprim0', [[1.38, 3.38], [2.38, 3.38]]), ('toprim1', [[2.38, 3.38], [2.76, 3.76]]), ('toprim2', [[2.76, 3.76], [1.76, 3.76]]), ('toprim3', [[1.76, 3.76], [1.38, 3.38]]), ('rightrim0', [[3.38, 1.38], [3.76, 1.76]]), ('rightrim1', [[3.76, 1.76], [3.76, 2.76]]), ('rightrim2', [[3.76, 2.76], [3.38, 2.38]]), ('rightrim3', [[3.38, 2.38], [3.38, 1.38]])]:
                c.line(points, id=object_id, zorder=3, clip_on=False)
            c.path([[1.0, 1.0], [1.38, 1.38], [1.38, 2.0], [1.0, 2.0], [1.0, 1.0]], [1, 2, 2, 2, 79], id='frontleft', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 1.0], linewidth=0.0, capstyle='butt')
            for object_id, points in [('frontleftcontour0', [[1.0, 1.0], [1.38, 1.38]]), ('frontleftcontour1', [[1.38, 1.38], [1.38, 2.0]]), ('frontleftcontour2', [[1.38, 2.0], [1.0, 2.0]]), ('frontleftcontour3', [[1.0, 2.0], [1.0, 1.0]])]:
                c.line(points, id=object_id, zorder=3, clip_on=False)
            c.path([[1.0, 1.0], [2.0, 1.0], [2.0, 1.38], [1.38, 1.38], [1.0, 1.0]], [1, 2, 2, 2, 79], id='frontfloor', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 1.0], linewidth=0.0, capstyle='butt')
            for object_id, points in [('frontfloorcontour0', [[1.0, 1.0], [2.0, 1.0]]), ('frontfloorcontour1', [[2.0, 1.0], [2.0, 1.38]]), ('frontfloorcontour2', [[2.0, 1.38], [1.38, 1.38]]), ('frontfloorcontour3', [[1.38, 1.38], [1.0, 1.0]])]:
                c.line(points, id=object_id, zorder=3, clip_on=False)
            c.path([[1.7600000000000002, 3.3800000000000003], [1.7600000000000002, 3.7600000000000002], [1.38, 3.38], [1.7600000000000002, 3.3800000000000003]], [1, 2, 2, 79], id='topleft', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 1.0], linewidth=0.0, capstyle='butt')
            for object_id, points in [('topleftcontour0', [[1.7600000000000002, 3.3800000000000003], [1.7600000000000002, 3.7600000000000002]]), ('topleftcontour1', [[1.7600000000000002, 3.7600000000000002], [1.38, 3.38]]), ('topleftcontour2', [[1.38, 3.38], [1.7600000000000002, 3.3800000000000003]])]:
                c.line(points, id=object_id, zorder=3, clip_on=False)
            c.path([[2.76, 3.76], [1.76, 3.76], [1.76, 3.38], [2.38, 3.38], [2.76, 3.76]], [1, 2, 2, 2, 79], id='topback', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 1.0], linewidth=0.0, capstyle='butt')
            for object_id, points in [('topbackcontour0', [[2.76, 3.76], [1.76, 3.76]]), ('topbackcontour1', [[1.76, 3.76], [1.76, 3.38]]), ('topbackcontour2', [[1.76, 3.38], [2.38, 3.38]]), ('topbackcontour3', [[2.38, 3.38], [2.76, 3.76]])]:
                c.line(points, id=object_id, zorder=3, clip_on=False)
            c.path([[3.38, 1.76], [3.76, 1.76], [3.76, 2.76], [3.38, 2.38], [3.38, 1.76]], [1, 2, 2, 2, 79], id='rightback', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 1.0], linewidth=0.0, capstyle='butt')
            for object_id, points in [('rightbackcontour0', [[3.38, 1.76], [3.76, 1.76]]), ('rightbackcontour1', [[3.76, 1.76], [3.76, 2.76]]), ('rightbackcontour2', [[3.76, 2.76], [3.38, 2.38]]), ('rightbackcontour3', [[3.38, 2.38], [3.38, 1.76]])]:
                c.line(points, id=object_id, zorder=3, clip_on=False)
            c.path([[3.38, 1.38], [3.7600000000000002, 1.7600000000000002], [3.3800000000000003, 1.7600000000000002], [3.38, 1.38]], [1, 2, 2, 79], id='rightfloor', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 1.0], linewidth=0.0, capstyle='butt')
            for object_id, points in [('rightfloorcontour0', [[3.38, 1.38], [3.7600000000000002, 1.7600000000000002]]), ('rightfloorcontour1', [[3.7600000000000002, 1.7600000000000002], [3.3800000000000003, 1.7600000000000002]]), ('rightfloorcontour2', [[3.3800000000000003, 1.7600000000000002], [3.38, 1.38]])]:
                c.line(points, id=object_id, zorder=3, clip_on=False)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Solid89().draw(sys.argv[1] if len(sys.argv) > 1 else None))
