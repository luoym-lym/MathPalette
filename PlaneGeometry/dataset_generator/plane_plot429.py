"""Frozen question Plane429; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane429:

    def __init__(self):
        self.id = 'Plane429'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:1897'
        self.question = "If $r, s$, and $t$ denote the lengths of the 'lines' in the picture, then which of the following inequalities is correct?\nChoices:\nA:$r<s<t$\nB:$r<t<s$\nC:$s<r<t$\nD:$s<t<r$\nE:$t<s<r$"
        self.answer = 'E'
        self.answer_type = 'choice'
        self.choices = {'A': '$r<s<t$', 'B': '$r<t<s$', 'C': '$s<r<t$', 'D': '$s<t<r$', 'E': '$t<s<r$'}
        self.query = self.question
        self._geometry_01 = [('gridv0', [[0.0, 0.0], [0.0, 5.0]]),
         ('gridv1', [[1.0, 0.0], [1.0, 5.0]]),
         ('gridv2', [[2.0, 0.0], [2.0, 5.0]]),
         ('gridv3', [[3.0, 0.0], [3.0, 5.0]]),
         ('gridv4', [[4.0, 0.0], [4.0, 5.0]]),
         ('gridv5', [[5.0, 0.0], [5.0, 5.0]]),
         ('gridv6', [[6.0, 0.0], [6.0, 5.0]]),
         ('gridv7', [[7.0, 0.0], [7.0, 5.0]]),
         ('gridv8', [[8.0, 0.0], [8.0, 5.0]]),
         ('gridv9', [[9.0, 0.0], [9.0, 5.0]]),
         ('gridv10', [[10.0, 0.0], [10.0, 5.0]]),
         ('gridv11', [[11.0, 0.0], [11.0, 5.0]]),
         ('gridv12', [[12.0, 0.0], [12.0, 5.0]]),
         ('gridv13', [[13.0, 0.0], [13.0, 5.0]]),
         ('gridv14', [[14.0, 0.0], [14.0, 5.0]]),
         ('gridv15', [[15.0, 0.0], [15.0, 5.0]]),
         ('gridv16', [[16.0, 0.0], [16.0, 5.0]]),
         ('gridv17', [[17.0, 0.0], [17.0, 5.0]]),
         ('gridv18', [[18.0, 0.0], [18.0, 5.0]]),
         ('gridv19', [[19.0, 0.0], [19.0, 5.0]]),
         ('gridv20', [[20.0, 0.0], [20.0, 5.0]]),
         ('gridv21', [[21.0, 0.0], [21.0, 5.0]]),
         ('gridv22', [[22.0, 0.0], [22.0, 5.0]]),
         ('gridv23', [[23.0, 0.0], [23.0, 5.0]]),
         ('gridv24', [[24.0, 0.0], [24.0, 5.0]]),
         ('gridv25', [[25.0, 0.0], [25.0, 5.0]]),
         ('gridv26', [[26.0, 0.0], [26.0, 5.0]]),
         ('gridv27', [[27.0, 0.0], [27.0, 5.0]]),
         ('gridv28', [[28.0, 0.0], [28.0, 5.0]]),
         ('gridv29', [[29.0, 0.0], [29.0, 5.0]]),
         ('gridv30', [[30.0, 0.0], [30.0, 5.0]]),
         ('gridh0', [[0.0, 0.0], [30.0, 0.0]]),
         ('gridh1', [[0.0, 1.0], [30.0, 1.0]]),
         ('gridh2', [[0.0, 2.0], [30.0, 2.0]]),
         ('gridh3', [[0.0, 3.0], [30.0, 3.0]]),
         ('gridh4', [[0.0, 4.0], [30.0, 4.0]]),
         ('gridh5', [[0.0, 5.0], [30.0, 5.0]])]
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane429.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-0.7435006984377441, 30.793449784397836], ylim=[-13.293431838640014, 18.243518644195568], axes_position=[0.050000000000000114, 0.05, 0.8999999999999998, 0.9], coordinate_axes=False) as c:
            for object_id, points in self._geometry_01:
                c.line(points, id=object_id, zorder=0.5, color='#AAAAAA')
            for object_id, points in [('r0', [[1.0, 2.0], [3.0, 2.0]]), ('r1', [[3.0, 2.0], [3.0, 4.0]]), ('r2', [[3.0, 4.0], [5.0, 4.0]]), ('r3', [[5.0, 4.0], [5.0, 0.0]]), ('r4', [[5.0, 0.0], [7.0, 0.0]]), ('r5', [[7.0, 0.0], [7.0, 2.0]]), ('r6', [[7.0, 2.0], [9.0, 2.0]]), ('t0', [[21.0, 2.0], [23.0, 2.0]]), ('t1', [[23.0, 2.0], [25.0, 0.0]]), ('t2', [[25.0, 0.0], [25.0, 4.0]]), ('t3', [[25.0, 4.0], [27.0, 2.0]]), ('t4', [[27.0, 2.0], [29.0, 2.0]]), ('s0', [[11.0, 2.0], [13.0, 2.0]]), ('s1', [[13.0, 2.0], [13.0, 3.0]]), ('s2', [[15.0, 3.0], [15.0, 1.0]]), ('s3', [[17.0, 1.0], [17.0, 2.0]]), ('s4', [[17.0, 2.0], [19.0, 2.0]])]:
                c.line(points, id=object_id, zorder=3)
            c.path([[15.0, 3.0], [15.0, 3.2651147734913026], [14.894571235314983, 3.519642327058112], [14.707106781186548, 3.7071067811865475], [14.519642327058111, 3.894571235314983], [14.265114773491302, 4.0], [14.0, 4.0], [13.734885226508698, 4.0], [13.480357672941889, 3.894571235314983], [13.292893218813452, 3.7071067811865475], [13.105428764685017, 3.5196423270581123], [13.0, 3.2651147734913026], [13.0, 3.0]], [1, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4], id='upperarc', facecolor=[0.0, 0.0, 0.0, 0], capstyle='butt', fill=False)
            c.path([[15.0, 1.0000000000000002], [15.0, 0.7348852265086976], [15.105428764685017, 0.48035767294188814], [15.292893218813452, 0.29289321881345254], [15.480357672941889, 0.10542876468501694], [15.734885226508698, 0.0], [16.0, 0.0], [16.2651147734913, 0.0], [16.51964232705811, 0.10542876468501683], [16.707106781186546, 0.2928932188134523], [16.894571235314984, 0.4803576729418878], [17.0, 0.7348852265086974], [17.0, 0.9999999999999998]], [1, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4], id='lowerarc', facecolor=[0.0, 0.0, 0.0, 0], capstyle='butt', fill=False)
            for object_id, text, anchor in [('labelr', 'r', [1.5, 3.4]), ('labels', 's', [11.5, 3.4]), ('labelt', 't', [21.5, 3.4])]:
                c.text(text, anchor, id=object_id, rotation_mode='default', offset_pt=[0, 0], annotation_clip=None)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane429().draw(sys.argv[1] if len(sys.argv) > 1 else None))
