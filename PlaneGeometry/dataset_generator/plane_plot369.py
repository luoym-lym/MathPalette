"""Frozen question Plane369; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane369:

    def __init__(self):
        self.id = 'Plane369'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:1377'
        self.question = '$a, b$ and $c$ denote the lengths of the different pieces of wire shown. Which of the following inequalities is correct?\nChoices:\nA:$a<b<c$\nB:$a<c<b$\nC:$b<a<c$\nD:$b<c<a$\nE:$c<b<a$'
        self.answer = 'E'
        self.answer_type = 'choice'
        self.choices = {'A': '$a<b<c$', 'B': '$a<c<b$', 'C': '$b<a<c$', 'D': '$b<c<a$', 'E': '$c<b<a$'}
        self.query = self.question
        self._geometry_01 = [('gv0', [[0.0, 0.0], [0.0, 4.0]]),
         ('gv1', [[1.0, 0.0], [1.0, 4.0]]),
         ('gv2', [[2.0, 0.0], [2.0, 4.0]]),
         ('gv3', [[3.0, 0.0], [3.0, 4.0]]),
         ('gv4', [[4.0, 0.0], [4.0, 4.0]]),
         ('gv5', [[5.0, 0.0], [5.0, 4.0]]),
         ('gv6', [[6.0, 0.0], [6.0, 4.0]]),
         ('gv7', [[7.0, 0.0], [7.0, 4.0]]),
         ('gv8', [[8.0, 0.0], [8.0, 4.0]]),
         ('gv9', [[9.0, 0.0], [9.0, 4.0]]),
         ('gv10', [[10.0, 0.0], [10.0, 4.0]]),
         ('gv11', [[11.0, 0.0], [11.0, 4.0]]),
         ('gv12', [[12.0, 0.0], [12.0, 4.0]]),
         ('gv13', [[13.0, 0.0], [13.0, 4.0]]),
         ('gv14', [[14.0, 0.0], [14.0, 4.0]]),
         ('gv15', [[15.0, 0.0], [15.0, 4.0]]),
         ('gv16', [[16.0, 0.0], [16.0, 4.0]]),
         ('gv17', [[17.0, 0.0], [17.0, 4.0]]),
         ('gv18', [[18.0, 0.0], [18.0, 4.0]]),
         ('gv19', [[19.0, 0.0], [19.0, 4.0]]),
         ('gv20', [[20.0, 0.0], [20.0, 4.0]]),
         ('gv21', [[21.0, 0.0], [21.0, 4.0]]),
         ('gv22', [[22.0, 0.0], [22.0, 4.0]]),
         ('gv23', [[23.0, 0.0], [23.0, 4.0]]),
         ('gv24', [[24.0, 0.0], [24.0, 4.0]]),
         ('gv25', [[25.0, 0.0], [25.0, 4.0]]),
         ('gv26', [[26.0, 0.0], [26.0, 4.0]]),
         ('gv27', [[27.0, 0.0], [27.0, 4.0]]),
         ('gv28', [[28.0, 0.0], [28.0, 4.0]]),
         ('gh0', [[0.0, 0.0], [28.0, 0.0]]),
         ('gh1', [[0.0, 1.0], [28.0, 1.0]]),
         ('gh2', [[0.0, 2.0], [28.0, 2.0]]),
         ('gh3', [[0.0, 3.0], [28.0, 3.0]]),
         ('gh4', [[0.0, 4.0], [28.0, 4.0]])]
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane369.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-0.6939339852085595, 28.74055313210465], ylim=[-12.74052217836848, 16.69396493894473], axes_position=[0.05, 0.05, 0.9, 0.9], coordinate_axes=False) as c:
            for object_id, points in self._geometry_01:
                c.line(points, id=object_id, zorder=0.5, color='#999999')
            for object_id, points in [('wire0_0', [[0.0, 2.0], [2.0, 2.0]]), ('wire0_1', [[2.0, 2.0], [2.0, 4.0]]), ('wire0_2', [[2.0, 4.0], [4.0, 4.0]]), ('wire0_3', [[4.0, 4.0], [4.0, 0.0]]), ('wire0_4', [[4.0, 0.0], [6.0, 0.0]]), ('wire0_5', [[6.0, 0.0], [6.0, 2.0]]), ('wire0_6', [[6.0, 2.0], [8.0, 2.0]]), ('wire1_0', [[10.0, 2.0], [12.0, 2.0]]), ('wire1_1', [[12.0, 2.0], [12.0, 3.0]]), ('wire1_2', [[12.0, 3.0], [14.0, 4.0]]), ('wire1_3', [[14.0, 4.0], [14.0, 0.0]]), ('wire1_4', [[14.0, 0.0], [16.0, 1.0]]), ('wire1_5', [[16.0, 1.0], [16.0, 2.0]]), ('wire1_6', [[16.0, 2.0], [18.0, 2.0]]), ('wire2_0', [[20.0, 2.0], [22.0, 2.0]]), ('wire2_1', [[22.0, 2.0], [24.0, 0.0]])]:
                c.line(points, id=object_id)
            c.line([[24.0, 0.0], [24.0, 4.0]], id='wire2_2', zorder=0.5)
            c.line([[24.0, 4.0], [26.0, 2.0]], id='wire2_3')
            c.line([[26.0, 2.0], [28.0, 2.0]], id='wire2_4')
            for object_id, text, anchor in [('label0', 'a', [7.0, 2.4]), ('label1', 'b', [17.0, 2.4]), ('label2', 'c', [27.0, 2.4])]:
                c.text(text, anchor, id=object_id, rotation_mode='default', offset_pt=[0, 0], annotation_clip=None)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane369().draw(sys.argv[1] if len(sys.argv) > 1 else None))
