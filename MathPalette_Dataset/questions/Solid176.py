"""Collected question Solid176; construction on the shared drawing protocol."""
from pathlib import Path
import sys
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from MathPalette_Dataset.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Solid176:
    variants = ('C01', 'C02')

    def __init__(self):
        self.id = 'Solid176'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:1605'
        self.question = 'One of the following nets cannot be folded along the dashed lines shown to form a cube. Which one?\nChoices:\nA:A\nB:B\nC:C\nD:D\nE:E'
        self.answer = 'C'
        self.answer_type = 'choice'
        self.choices = {'A': 'A', 'B': 'B', 'C': 'C', 'D': 'D', 'E': 'E'}
        self.query = self.question

    def draw(self, output_path=None, *, variant=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if variant not in self.variants:
                raise ValueError('Unknown Special variant: ' + str(variant))
            return getattr(self, 'draw_' + variant)(output_path)
        with Canvas(SOLID, xlim=[-0.6574961854773811, 27.097467115709936], ylim=[-12.662446120877894, 15.092517180309423], projection=[[1, 0, 0], [0, 1, 0]], origin=[0, 0, 0], offset=[0, 0]) as c:
            c.line(c.project([[0.0, 1, 0], [1.0, 1, 0]]), id='base010', clip_on=False, zorder=3)
            c.line(c.project([[1.0, 1, 0], [2.0, 1, 0]]), id='base011', linestyle=(0, [4, 3]), clip_on=False, zorder=3)
            c.line(c.project([[2.0, 1, 0], [3.0, 1, 0]]), id='base012', linestyle=(0, [4, 3]), clip_on=False, zorder=3)
            for object_id, points in [('base013', c.project([[3.0, 1, 0], [4.0, 1, 0]])), ('flap010a', c.project([[1.0, 1, 0], [1.0, 2, 0]])), ('flap010b', c.project([[1.0, 2, 0], [2.0, 1, 0]])), ('flap011a', c.project([[2.0, 1, 0], [3.0, 2, 0]])), ('flap011b', c.project([[3.0, 2, 0], [3.0, 1, 0]])), ('base000', c.project([[0.0, 0, 0], [1.0, 0, 0]]))]:
                c.line(points, id=object_id, clip_on=False, zorder=3)
            c.line(c.project([[1.0, 0, 0], [2.0, 0, 0]]), id='base001', linestyle=(0, [4, 3]), clip_on=False, zorder=3)
            c.line(c.project([[2.0, 0, 0], [3.0, 0, 0]]), id='base002', linestyle=(0, [4, 3]), clip_on=False, zorder=3)
            for object_id, points in [('base003', c.project([[3.0, 0, 0], [4.0, 0, 0]])), ('flap000a', c.project([[1.0, 0, 0], [1.0, -1, 0]])), ('flap000b', c.project([[1.0, -1, 0], [2.0, 0, 0]])), ('flap001a', c.project([[2.0, 0, 0], [3.0, -1, 0]])), ('flap001b', c.project([[3.0, -1, 0], [3.0, 0, 0]])), ('vert00', c.project([[0.0, 0, 0], [0.0, 1, 0]]))]:
                c.line(points, id=object_id, clip_on=False, zorder=3)
            for object_id, points in [('vert01', c.project([[1.0, 0, 0], [1.0, 1, 0]])), ('vert02', c.project([[2.0, 0, 0], [2.0, 1, 0]])), ('vert03', c.project([[3.0, 0, 0], [3.0, 1, 0]]))]:
                c.line(points, id=object_id, linestyle=(0, [4, 3]), clip_on=False, zorder=3)
            c.line(c.project([[4.0, 0, 0], [4.0, 1, 0]]), id='vert04', clip_on=False, zorder=3)
            c.line(c.project([[5.6, 1, 0], [6.6, 1, 0]]), id='base110', clip_on=False, zorder=3)
            c.line(c.project([[6.6, 1, 0], [7.6, 1, 0]]), id='base111', linestyle=(0, [4, 3]), clip_on=False, zorder=3)
            c.line(c.project([[7.6, 1, 0], [8.6, 1, 0]]), id='base112', linestyle=(0, [4, 3]), clip_on=False, zorder=3)
            for object_id, points in [('base113', c.project([[8.6, 1, 0], [9.6, 1, 0]])), ('flap110a', c.project([[6.6, 1, 0], [6.6, 2, 0]])), ('flap110b', c.project([[6.6, 2, 0], [7.6, 1, 0]])), ('flap111a', c.project([[7.6, 1, 0], [8.6, 2, 0]])), ('flap111b', c.project([[8.6, 2, 0], [8.6, 1, 0]]))]:
                c.line(points, id=object_id, clip_on=False, zorder=3)
            c.line(c.project([[5.6, 0, 0], [6.6, 0, 0]]), id='base100', linestyle=(0, [4, 3]), clip_on=False, zorder=3)
            c.line(c.project([[6.6, 0, 0], [7.6, 0, 0]]), id='base101', clip_on=False, zorder=3)
            c.line(c.project([[7.6, 0, 0], [8.6, 0, 0]]), id='base102', clip_on=False, zorder=3)
            c.line(c.project([[8.6, 0, 0], [9.6, 0, 0]]), id='base103', linestyle=(0, [4, 3]), clip_on=False, zorder=3)
            for object_id, points in [('flap100a', c.project([[5.6, 0, 0], [6.6, -1, 0]])), ('flap100b', c.project([[6.6, -1, 0], [6.6, 0, 0]])), ('flap101a', c.project([[8.6, 0, 0], [8.6, -1, 0]])), ('flap101b', c.project([[8.6, -1, 0], [9.6, 0, 0]])), ('vert10', c.project([[5.6, 0, 0], [5.6, 1, 0]]))]:
                c.line(points, id=object_id, clip_on=False, zorder=3)
            for object_id, points in [('vert11', c.project([[6.6, 0, 0], [6.6, 1, 0]])), ('vert12', c.project([[7.6, 0, 0], [7.6, 1, 0]])), ('vert13', c.project([[8.6, 0, 0], [8.6, 1, 0]]))]:
                c.line(points, id=object_id, linestyle=(0, [4, 3]), clip_on=False, zorder=3)
            c.line(c.project([[9.6, 0, 0], [9.6, 1, 0]]), id='vert14', clip_on=False, zorder=3)
            c.line(c.project([[11.2, 1, 0], [12.2, 1, 0]]), id='base210', linestyle=(0, [4, 3]), clip_on=False, zorder=3)
            c.line(c.project([[12.2, 1, 0], [13.2, 1, 0]]), id='base211', clip_on=False, zorder=3)
            c.line(c.project([[13.2, 1, 0], [14.2, 1, 0]]), id='base212', clip_on=False, zorder=3)
            c.line(c.project([[14.2, 1, 0], [15.2, 1, 0]]), id='base213', linestyle=(0, [4, 3]), clip_on=False, zorder=3)
            for object_id, points in [('flap210a', c.project([[11.2, 1, 0], [12.2, 2, 0]])), ('flap210b', c.project([[12.2, 2, 0], [12.2, 1, 0]])), ('flap211a', c.project([[14.2, 1, 0], [14.2, 2, 0]])), ('flap211b', c.project([[14.2, 2, 0], [15.2, 1, 0]]))]:
                c.line(points, id=object_id, clip_on=False, zorder=3)
            c.line(c.project([[11.2, 0, 0], [12.2, 0, 0]]), id='base200', linestyle=(0, [4, 3]), clip_on=False, zorder=3)
            c.line(c.project([[12.2, 0, 0], [13.2, 0, 0]]), id='base201', clip_on=False, zorder=3)
            c.line(c.project([[13.2, 0, 0], [14.2, 0, 0]]), id='base202', clip_on=False, zorder=3)
            c.line(c.project([[14.2, 0, 0], [15.2, 0, 0]]), id='base203', linestyle=(0, [4, 3]), clip_on=False, zorder=3)
            for object_id, points in [('flap200a', c.project([[11.2, 0, 0], [11.2, -1, 0]])), ('flap200b', c.project([[11.2, -1, 0], [12.2, 0, 0]])), ('flap201a', c.project([[14.2, 0, 0], [15.2, -1, 0]])), ('flap201b', c.project([[15.2, -1, 0], [15.2, 0, 0]])), ('vert20', c.project([[11.2, 0, 0], [11.2, 1, 0]]))]:
                c.line(points, id=object_id, clip_on=False, zorder=3)
            for object_id, points in [('vert21', c.project([[12.2, 0, 0], [12.2, 1, 0]])), ('vert22', c.project([[13.2, 0, 0], [13.2, 1, 0]])), ('vert23', c.project([[14.2, 0, 0], [14.2, 1, 0]]))]:
                c.line(points, id=object_id, linestyle=(0, [4, 3]), clip_on=False, zorder=3)
            c.line(c.project([[15.2, 0, 0], [15.2, 1, 0]]), id='vert24', clip_on=False, zorder=3)
            c.line(c.project([[16.799999999999997, 1, 0], [17.799999999999997, 1, 0]]), id='base310', linestyle=(0, [4, 3]), clip_on=False, zorder=3)
            c.line(c.project([[17.799999999999997, 1, 0], [18.799999999999997, 1, 0]]), id='base311', clip_on=False, zorder=3)
            c.line(c.project([[18.799999999999997, 1, 0], [19.799999999999997, 1, 0]]), id='base312', linestyle=(0, [4, 3]), clip_on=False, zorder=3)
            for object_id, points in [('base313', c.project([[19.799999999999997, 1, 0], [20.799999999999997, 1, 0]])), ('flap310a', c.project([[16.799999999999997, 1, 0], [17.799999999999997, 2, 0]])), ('flap310b', c.project([[17.799999999999997, 2, 0], [17.799999999999997, 1, 0]])), ('flap311a', c.project([[18.799999999999997, 1, 0], [19.799999999999997, 2, 0]])), ('flap311b', c.project([[19.799999999999997, 2, 0], [19.799999999999997, 1, 0]]))]:
                c.line(points, id=object_id, clip_on=False, zorder=3)
            c.line(c.project([[16.799999999999997, 0, 0], [17.799999999999997, 0, 0]]), id='base300', linestyle=(0, [4, 3]), clip_on=False, zorder=3)
            c.line(c.project([[17.799999999999997, 0, 0], [18.799999999999997, 0, 0]]), id='base301', clip_on=False, zorder=3)
            c.line(c.project([[18.799999999999997, 0, 0], [19.799999999999997, 0, 0]]), id='base302', linestyle=(0, [4, 3]), clip_on=False, zorder=3)
            for object_id, points in [('base303', c.project([[19.799999999999997, 0, 0], [20.799999999999997, 0, 0]])), ('flap300a', c.project([[16.799999999999997, 0, 0], [16.799999999999997, -1, 0]])), ('flap300b', c.project([[16.799999999999997, -1, 0], [17.799999999999997, 0, 0]])), ('flap301a', c.project([[18.799999999999997, 0, 0], [18.799999999999997, -1, 0]])), ('flap301b', c.project([[18.799999999999997, -1, 0], [19.799999999999997, 0, 0]])), ('vert30', c.project([[16.799999999999997, 0, 0], [16.799999999999997, 1, 0]]))]:
                c.line(points, id=object_id, clip_on=False, zorder=3)
            for object_id, points in [('vert31', c.project([[17.799999999999997, 0, 0], [17.799999999999997, 1, 0]])), ('vert32', c.project([[18.799999999999997, 0, 0], [18.799999999999997, 1, 0]])), ('vert33', c.project([[19.799999999999997, 0, 0], [19.799999999999997, 1, 0]]))]:
                c.line(points, id=object_id, linestyle=(0, [4, 3]), clip_on=False, zorder=3)
            c.line(c.project([[20.799999999999997, 0, 0], [20.799999999999997, 1, 0]]), id='vert34', clip_on=False, zorder=3)
            c.line(c.project([[22.4, 1, 0], [23.4, 1, 0]]), id='base410', linestyle=(0, [4, 3]), clip_on=False, zorder=3)
            c.line(c.project([[23.4, 1, 0], [24.4, 1, 0]]), id='base411', clip_on=False, zorder=3)
            c.line(c.project([[24.4, 1, 0], [25.4, 1, 0]]), id='base412', linestyle=(0, [4, 3]), clip_on=False, zorder=3)
            for object_id, points in [('base413', c.project([[25.4, 1, 0], [26.4, 1, 0]])), ('flap410a', c.project([[22.4, 1, 0], [23.4, 2, 0]])), ('flap410b', c.project([[23.4, 2, 0], [23.4, 1, 0]])), ('flap411a', c.project([[24.4, 1, 0], [25.4, 2, 0]])), ('flap411b', c.project([[25.4, 2, 0], [25.4, 1, 0]])), ('base400', c.project([[22.4, 0, 0], [23.4, 0, 0]]))]:
                c.line(points, id=object_id, clip_on=False, zorder=3)
            c.line(c.project([[23.4, 0, 0], [24.4, 0, 0]]), id='base401', linestyle=(0, [4, 3]), clip_on=False, zorder=3)
            c.line(c.project([[24.4, 0, 0], [25.4, 0, 0]]), id='base402', clip_on=False, zorder=3)
            c.line(c.project([[25.4, 0, 0], [26.4, 0, 0]]), id='base403', linestyle=(0, [4, 3]), clip_on=False, zorder=3)
            for object_id, points in [('flap400a', c.project([[23.4, 0, 0], [23.4, -1, 0]])), ('flap400b', c.project([[23.4, -1, 0], [24.4, 0, 0]])), ('flap401a', c.project([[25.4, 0, 0], [25.4, -1, 0]])), ('flap401b', c.project([[25.4, -1, 0], [26.4, 0, 0]])), ('vert40', c.project([[22.4, 0, 0], [22.4, 1, 0]]))]:
                c.line(points, id=object_id, clip_on=False, zorder=3)
            for object_id, points in [('vert41', c.project([[23.4, 0, 0], [23.4, 1, 0]])), ('vert42', c.project([[24.4, 0, 0], [24.4, 1, 0]])), ('vert43', c.project([[25.4, 0, 0], [25.4, 1, 0]]))]:
                c.line(points, id=object_id, linestyle=(0, [4, 3]), clip_on=False, zorder=3)
            c.line(c.project([[26.4, 0, 0], [26.4, 1, 0]]), id='vert44', clip_on=False, zorder=3)
            for object_id, text, anchor in [('option0', 'A', c.project([2.0, 2, 0])), ('option1', 'B', c.project([7.6, 2, 0])), ('option2', 'C', c.project([13.2, 2, 0])), ('option3', 'D', c.project([18.799999999999997, 2, 0])), ('option4', 'E', c.project([24.4, 2, 0]))]:
                c.text(text, anchor, id=object_id, offset_pt=[0, 20], vertex=False)
            return c.save(output_path)

    def draw_C01(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Solid176_C01.png'
        with Canvas(SOLID, xlim=(-0.6574961854773811, 27.097467115709936), ylim=(-12.662446120877894, 15.092517180309423), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
            c.line([[0.0, 1.0], [1.0, 1.0]], id='base010', zorder=3, clip_on=False)
            c.line([[1.0, 1.0], [2.0, 1.0]], id='base011', zorder=3, clip_on=False, linestyle=(0.0, [4.0, 3.0]))
            c.line([[2.0, 1.0], [3.0, 1.0]], id='base012', zorder=3, clip_on=False, linestyle=(0.0, [4.0, 3.0]))
            for object_id, points in [('base013', [[3.0, 1.0], [4.0, 1.0]]), ('flap010a', [[1.0, 1.0], [1.0, 2.0]]), ('flap010b', [[1.0, 2.0], [2.0, 1.0]]), ('flap011a', [[2.0, 1.0], [3.0, 2.0]]), ('flap011b', [[3.0, 2.0], [3.0, 1.0]]), ('base000', [[0.0, 0.0], [1.0, 0.0]])]:
                c.line(points, id=object_id, zorder=3, clip_on=False)
            c.line([[1.0, 0.0], [2.0, 0.0]], id='base001', zorder=3, clip_on=False, linestyle=(0.0, [4.0, 3.0]))
            c.line([[2.0, 0.0], [3.0, 0.0]], id='base002', zorder=3, clip_on=False, linestyle=(0.0, [4.0, 3.0]))
            for object_id, points in [('base003', [[3.0, 0.0], [4.0, 0.0]]), ('flap000a', [[1.0, 0.0], [1.0, -1.0]]), ('flap000b', [[1.0, -1.0], [2.0, 0.0]]), ('flap001a', [[2.0, 0.0], [3.0, -1.0]]), ('flap001b', [[3.0, -1.0], [3.0, 0.0]]), ('vert00', [[0.0, 0.0], [0.0, 1.0]])]:
                c.line(points, id=object_id, zorder=3, clip_on=False)
            for object_id, points in [('vert01', [[1.0, 0.0], [1.0, 1.0]]), ('vert02', [[2.0, 0.0], [2.0, 1.0]]), ('vert03', [[3.0, 0.0], [3.0, 1.0]])]:
                c.line(points, id=object_id, zorder=3, clip_on=False, linestyle=(0.0, [4.0, 3.0]))
            c.line([[4.0, 0.0], [4.0, 1.0]], id='vert04', zorder=3, clip_on=False)
            c.line([[5.6, 1.0], [6.6, 1.0]], id='base110', zorder=3, clip_on=False)
            c.line([[6.6, 1.0], [7.6, 1.0]], id='base111', zorder=3, clip_on=False, linestyle=(0.0, [4.0, 3.0]))
            c.line([[7.6, 1.0], [8.6, 1.0]], id='base112', zorder=3, clip_on=False, linestyle=(0.0, [4.0, 3.0]))
            for object_id, points in [('base113', [[8.6, 1.0], [9.6, 1.0]]), ('flap110a', [[6.6, 1.0], [6.6, 2.0]]), ('flap110b', [[6.6, 2.0], [7.6, 1.0]]), ('flap111a', [[7.6, 1.0], [8.6, 2.0]]), ('flap111b', [[8.6, 2.0], [8.6, 1.0]])]:
                c.line(points, id=object_id, zorder=3, clip_on=False)
            c.line([[5.6, 0.0], [6.6, 0.0]], id='base100', zorder=3, clip_on=False, linestyle=(0.0, [4.0, 3.0]))
            c.line([[6.6, 0.0], [7.6, 0.0]], id='base101', zorder=3, clip_on=False)
            c.line([[7.6, 0.0], [8.6, 0.0]], id='base102', zorder=3, clip_on=False)
            c.line([[8.6, 0.0], [9.6, 0.0]], id='base103', zorder=3, clip_on=False, linestyle=(0.0, [4.0, 3.0]))
            for object_id, points in [('flap100a', [[5.6, 0.0], [6.6, -1.0]]), ('flap100b', [[6.6, -1.0], [6.6, 0.0]]), ('flap101a', [[8.6, 0.0], [8.6, -1.0]]), ('flap101b', [[8.6, -1.0], [9.6, 0.0]]), ('vert10', [[5.6, 0.0], [5.6, 1.0]])]:
                c.line(points, id=object_id, zorder=3, clip_on=False)
            for object_id, points in [('vert11', [[6.6, 0.0], [6.6, 1.0]]), ('vert12', [[7.6, 0.0], [7.6, 1.0]]), ('vert13', [[8.6, 0.0], [8.6, 1.0]])]:
                c.line(points, id=object_id, zorder=3, clip_on=False, linestyle=(0.0, [4.0, 3.0]))
            c.line([[9.6, 0.0], [9.6, 1.0]], id='vert14', zorder=3, clip_on=False)
            c.line([[11.2, 1.0], [12.2, 1.0]], id='base210', zorder=3, clip_on=False, linestyle=(0.0, [4.0, 3.0]))
            c.line([[12.2, 1.0], [13.2, 1.0]], id='base211', zorder=3, clip_on=False)
            c.line([[13.2, 1.0], [14.2, 1.0]], id='base212', zorder=3, clip_on=False)
            c.line([[14.2, 1.0], [15.2, 1.0]], id='base213', zorder=3, clip_on=False, linestyle=(0.0, [4.0, 3.0]))
            for object_id, points in [('flap210a', [[11.2, 1.0], [12.2, 2.0]]), ('flap210b', [[12.2, 2.0], [12.2, 1.0]]), ('flap211a', [[14.2, 1.0], [14.2, 2.0]]), ('flap211b', [[14.2, 2.0], [15.2, 1.0]])]:
                c.line(points, id=object_id, zorder=3, clip_on=False)
            c.line([[11.2, 0.0], [12.2, 0.0]], id='base200', zorder=3, clip_on=False, linestyle=(0.0, [4.0, 3.0]))
            c.line([[12.2, 0.0], [13.2, 0.0]], id='base201', zorder=3, clip_on=False)
            c.line([[13.2, 0.0], [14.2, 0.0]], id='base202', zorder=3, clip_on=False)
            c.line([[14.2, 0.0], [15.2, 0.0]], id='base203', zorder=3, clip_on=False, linestyle=(0.0, [4.0, 3.0]))
            for object_id, points in [('flap200a', [[11.2, 0.0], [11.2, -1.0]]), ('flap200b', [[11.2, -1.0], [12.2, 0.0]]), ('flap201a', [[14.2, 0.0], [15.2, -1.0]]), ('flap201b', [[15.2, -1.0], [15.2, 0.0]]), ('vert20', [[11.2, 0.0], [11.2, 1.0]])]:
                c.line(points, id=object_id, zorder=3, clip_on=False)
            for object_id, points in [('vert21', [[12.2, 0.0], [12.2, 1.0]]), ('vert22', [[13.2, 0.0], [13.2, 1.0]]), ('vert23', [[14.2, 0.0], [14.2, 1.0]])]:
                c.line(points, id=object_id, zorder=3, clip_on=False, linestyle=(0.0, [4.0, 3.0]))
            c.line([[15.2, 0.0], [15.2, 1.0]], id='vert24', zorder=3, clip_on=False)
            c.line([[16.799999999999997, 1.0], [17.799999999999997, 1.0]], id='base310', zorder=3, clip_on=False, linestyle=(0.0, [4.0, 3.0]))
            c.line([[17.799999999999997, 1.0], [18.799999999999997, 1.0]], id='base311', zorder=3, clip_on=False)
            c.line([[18.799999999999997, 1.0], [19.799999999999997, 1.0]], id='base312', zorder=3, clip_on=False, linestyle=(0.0, [4.0, 3.0]))
            c.line([[19.799999999999997, 1.0], [20.799999999999997, 1.0]], id='base313', zorder=3, clip_on=False)
            c.line([[16.799999999999997, 1.0], [17.799999999999997, 2.0]], id='flap310a', zorder=3, clip_on=False, color='#DC2626')
            c.line([[17.799999999999997, 2.0], [17.799999999999997, 1.0]], id='flap310b', zorder=3, clip_on=False)
            c.line([[18.799999999999997, 1.0], [19.799999999999997, 2.0]], id='flap311a', zorder=3, clip_on=False, color='#DC2626')
            c.line([[19.799999999999997, 2.0], [19.799999999999997, 1.0]], id='flap311b', zorder=3, clip_on=False)
            c.line([[16.799999999999997, 0.0], [17.799999999999997, 0.0]], id='base300', zorder=3, clip_on=False, linestyle=(0.0, [4.0, 3.0]))
            c.line([[17.799999999999997, 0.0], [18.799999999999997, 0.0]], id='base301', zorder=3, clip_on=False)
            c.line([[18.799999999999997, 0.0], [19.799999999999997, 0.0]], id='base302', zorder=3, clip_on=False, linestyle=(0.0, [4.0, 3.0]))
            c.line([[19.799999999999997, 0.0], [20.799999999999997, 0.0]], id='base303', zorder=3, clip_on=False)
            c.line([[16.799999999999997, 0.0], [16.799999999999997, -1.0]], id='flap300a', zorder=3, clip_on=False)
            c.line([[16.799999999999997, -1.0], [17.799999999999997, 0.0]], id='flap300b', zorder=3, clip_on=False, color='#DC2626')
            c.line([[18.799999999999997, 0.0], [18.799999999999997, -1.0]], id='flap301a', zorder=3, clip_on=False)
            c.line([[18.799999999999997, -1.0], [19.799999999999997, 0.0]], id='flap301b', zorder=3, clip_on=False, color='#DC2626')
            c.line([[16.799999999999997, 0.0], [16.799999999999997, 1.0]], id='vert30', zorder=3, clip_on=False)
            for object_id, points in [('vert31', [[17.799999999999997, 0.0], [17.799999999999997, 1.0]]), ('vert32', [[18.799999999999997, 0.0], [18.799999999999997, 1.0]]), ('vert33', [[19.799999999999997, 0.0], [19.799999999999997, 1.0]])]:
                c.line(points, id=object_id, zorder=3, clip_on=False, linestyle=(0.0, [4.0, 3.0]))
            c.line([[20.799999999999997, 0.0], [20.799999999999997, 1.0]], id='vert34', zorder=3, clip_on=False)
            c.line([[22.4, 1.0], [23.4, 1.0]], id='base410', zorder=3, clip_on=False, linestyle=(0.0, [4.0, 3.0]))
            c.line([[23.4, 1.0], [24.4, 1.0]], id='base411', zorder=3, clip_on=False)
            c.line([[24.4, 1.0], [25.4, 1.0]], id='base412', zorder=3, clip_on=False, linestyle=(0.0, [4.0, 3.0]))
            for object_id, points in [('base413', [[25.4, 1.0], [26.4, 1.0]]), ('flap410a', [[22.4, 1.0], [23.4, 2.0]]), ('flap410b', [[23.4, 2.0], [23.4, 1.0]]), ('flap411a', [[24.4, 1.0], [25.4, 2.0]]), ('flap411b', [[25.4, 2.0], [25.4, 1.0]]), ('base400', [[22.4, 0.0], [23.4, 0.0]])]:
                c.line(points, id=object_id, zorder=3, clip_on=False)
            c.line([[23.4, 0.0], [24.4, 0.0]], id='base401', zorder=3, clip_on=False, linestyle=(0.0, [4.0, 3.0]))
            c.line([[24.4, 0.0], [25.4, 0.0]], id='base402', zorder=3, clip_on=False)
            c.line([[25.4, 0.0], [26.4, 0.0]], id='base403', zorder=3, clip_on=False, linestyle=(0.0, [4.0, 3.0]))
            for object_id, points in [('flap400a', [[23.4, 0.0], [23.4, -1.0]]), ('flap400b', [[23.4, -1.0], [24.4, 0.0]]), ('flap401a', [[25.4, 0.0], [25.4, -1.0]]), ('flap401b', [[25.4, -1.0], [26.4, 0.0]]), ('vert40', [[22.4, 0.0], [22.4, 1.0]])]:
                c.line(points, id=object_id, zorder=3, clip_on=False)
            for object_id, points in [('vert41', [[23.4, 0.0], [23.4, 1.0]]), ('vert42', [[24.4, 0.0], [24.4, 1.0]]), ('vert43', [[25.4, 0.0], [25.4, 1.0]])]:
                c.line(points, id=object_id, zorder=3, clip_on=False, linestyle=(0.0, [4.0, 3.0]))
            c.line([[26.4, 0.0], [26.4, 1.0]], id='vert44', zorder=3, clip_on=False)
            for object_id, text, anchor in [('option0', 'A', (2.0, 2.0)), ('option1', 'B', (7.6, 2.0)), ('option2', 'C', (13.2, 2.0)), ('option3', 'D', (18.799999999999997, 2.0)), ('option4', 'E', (24.4, 2.0))]:
                c.text(text, anchor, id=object_id, rotation_mode='default', offset_pt=(0, 20), annotation_clip=None)
            return c.save(output_path)

    def draw_C02(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Solid176_C02.png'
        with Canvas(SOLID, xlim=(-0.6574961854773811, 27.097467115709936), ylim=(-12.662446120877894, 15.092517180309423), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
            c.line([[0.0, 1.0], [1.0, 1.0]], id='base010', zorder=3, clip_on=False, simplify=False)
            c.line([[1.0, 1.0], [2.0, 1.0]], id='base011', zorder=3, clip_on=False, linestyle=(0.0, [4.0, 3.0]), simplify=False)
            c.line([[2.0, 1.0], [3.0, 1.0]], id='base012', zorder=3, clip_on=False, linestyle=(0.0, [4.0, 3.0]), simplify=False)
            c.line([[3.0, 1.0], [4.0, 1.0]], id='base013', zorder=3, clip_on=False, simplify=False)
            c.line([[1.0, 1.0], [1.0, 2.0]], id='flap010a', zorder=3, clip_on=False, simplify=False)
            c.line([[1.0, 2.0], [2.0, 1.0]], id='flap010b', zorder=3, clip_on=False, color='#2563EB', linewidth=1.5, solid_capstyle='butt', simplify=False)
            c.line([[2.0, 1.0], [3.0, 2.0]], id='flap011a', zorder=3, clip_on=False, color='#2563EB', linewidth=1.5, solid_capstyle='butt', simplify=False)
            c.line([[3.0, 2.0], [3.0, 1.0]], id='flap011b', zorder=3, clip_on=False, simplify=False)
            c.line([[0.0, 0.0], [1.0, 0.0]], id='base000', zorder=3, clip_on=False, simplify=False)
            c.line([[1.0, 0.0], [2.0, 0.0]], id='base001', zorder=3, clip_on=False, linestyle=(0.0, [4.0, 3.0]), simplify=False)
            c.line([[2.0, 0.0], [3.0, 0.0]], id='base002', zorder=3, clip_on=False, linestyle=(0.0, [4.0, 3.0]), simplify=False)
            c.line([[3.0, 0.0], [4.0, 0.0]], id='base003', zorder=3, clip_on=False, simplify=False)
            c.line([[1.0, 0.0], [1.0, -1.0]], id='flap000a', zorder=3, clip_on=False, simplify=False)
            c.line([[1.0, -1.0], [2.0, 0.0]], id='flap000b', zorder=3, clip_on=False, color='#2563EB', linewidth=1.5, solid_capstyle='butt', simplify=False)
            c.line([[2.0, 0.0], [3.0, -1.0]], id='flap001a', zorder=3, clip_on=False, color='#2563EB', linewidth=1.5, solid_capstyle='butt', simplify=False)
            c.line([[3.0, -1.0], [3.0, 0.0]], id='flap001b', zorder=3, clip_on=False, simplify=False)
            c.line([[0.0, 0.0], [0.0, 1.0]], id='vert00', zorder=3, clip_on=False, simplify=False)
            for object_id, points in [('vert01', [[1.0, 0.0], [1.0, 1.0]]), ('vert02', [[2.0, 0.0], [2.0, 1.0]]), ('vert03', [[3.0, 0.0], [3.0, 1.0]])]:
                c.line(points, id=object_id, zorder=3, clip_on=False, linestyle=(0.0, [4.0, 3.0]), simplify=False)
            c.line([[4.0, 0.0], [4.0, 1.0]], id='vert04', zorder=3, clip_on=False, simplify=False)
            c.line([[5.6, 1.0], [6.6, 1.0]], id='base110', zorder=3, clip_on=False, simplify=False)
            c.line([[6.6, 1.0], [7.6, 1.0]], id='base111', zorder=3, clip_on=False, linestyle=(0.0, [4.0, 3.0]), simplify=False)
            c.line([[7.6, 1.0], [8.6, 1.0]], id='base112', zorder=3, clip_on=False, linestyle=(0.0, [4.0, 3.0]), simplify=False)
            for object_id, points in [('base113', [[8.6, 1.0], [9.6, 1.0]]), ('flap110a', [[6.6, 1.0], [6.6, 2.0]]), ('flap110b', [[6.6, 2.0], [7.6, 1.0]]), ('flap111a', [[7.6, 1.0], [8.6, 2.0]]), ('flap111b', [[8.6, 2.0], [8.6, 1.0]])]:
                c.line(points, id=object_id, zorder=3, clip_on=False, simplify=False)
            c.line([[5.6, 0.0], [6.6, 0.0]], id='base100', zorder=3, clip_on=False, linestyle=(0.0, [4.0, 3.0]), simplify=False)
            c.line([[6.6, 0.0], [7.6, 0.0]], id='base101', zorder=3, clip_on=False, simplify=False)
            c.line([[7.6, 0.0], [8.6, 0.0]], id='base102', zorder=3, clip_on=False, simplify=False)
            c.line([[8.6, 0.0], [9.6, 0.0]], id='base103', zorder=3, clip_on=False, linestyle=(0.0, [4.0, 3.0]), simplify=False)
            for object_id, points in [('flap100a', [[5.6, 0.0], [6.6, -1.0]]), ('flap100b', [[6.6, -1.0], [6.6, 0.0]]), ('flap101a', [[8.6, 0.0], [8.6, -1.0]]), ('flap101b', [[8.6, -1.0], [9.6, 0.0]]), ('vert10', [[5.6, 0.0], [5.6, 1.0]])]:
                c.line(points, id=object_id, zorder=3, clip_on=False, simplify=False)
            for object_id, points in [('vert11', [[6.6, 0.0], [6.6, 1.0]]), ('vert12', [[7.6, 0.0], [7.6, 1.0]]), ('vert13', [[8.6, 0.0], [8.6, 1.0]])]:
                c.line(points, id=object_id, zorder=3, clip_on=False, linestyle=(0.0, [4.0, 3.0]), simplify=False)
            c.line([[9.6, 0.0], [9.6, 1.0]], id='vert14', zorder=3, clip_on=False, simplify=False)
            c.line([[11.2, 1.0], [12.2, 1.0]], id='base210', zorder=3, clip_on=False, linestyle=(0.0, [4.0, 3.0]), simplify=False)
            c.line([[12.2, 1.0], [13.2, 1.0]], id='base211', zorder=3, clip_on=False, simplify=False)
            c.line([[13.2, 1.0], [14.2, 1.0]], id='base212', zorder=3, clip_on=False, simplify=False)
            c.line([[14.2, 1.0], [15.2, 1.0]], id='base213', zorder=3, clip_on=False, linestyle=(0.0, [4.0, 3.0]), simplify=False)
            for object_id, points in [('flap210a', [[11.2, 1.0], [12.2, 2.0]]), ('flap210b', [[12.2, 2.0], [12.2, 1.0]]), ('flap211a', [[14.2, 1.0], [14.2, 2.0]]), ('flap211b', [[14.2, 2.0], [15.2, 1.0]])]:
                c.line(points, id=object_id, zorder=3, clip_on=False, simplify=False)
            c.line([[11.2, 0.0], [12.2, 0.0]], id='base200', zorder=3, clip_on=False, linestyle=(0.0, [4.0, 3.0]), simplify=False)
            c.line([[12.2, 0.0], [13.2, 0.0]], id='base201', zorder=3, clip_on=False, simplify=False)
            c.line([[13.2, 0.0], [14.2, 0.0]], id='base202', zorder=3, clip_on=False, simplify=False)
            c.line([[14.2, 0.0], [15.2, 0.0]], id='base203', zorder=3, clip_on=False, linestyle=(0.0, [4.0, 3.0]), simplify=False)
            for object_id, points in [('flap200a', [[11.2, 0.0], [11.2, -1.0]]), ('flap200b', [[11.2, -1.0], [12.2, 0.0]]), ('flap201a', [[14.2, 0.0], [15.2, -1.0]]), ('flap201b', [[15.2, -1.0], [15.2, 0.0]]), ('vert20', [[11.2, 0.0], [11.2, 1.0]])]:
                c.line(points, id=object_id, zorder=3, clip_on=False, simplify=False)
            for object_id, points in [('vert21', [[12.2, 0.0], [12.2, 1.0]]), ('vert22', [[13.2, 0.0], [13.2, 1.0]]), ('vert23', [[14.2, 0.0], [14.2, 1.0]])]:
                c.line(points, id=object_id, zorder=3, clip_on=False, linestyle=(0.0, [4.0, 3.0]), simplify=False)
            c.line([[15.2, 0.0], [15.2, 1.0]], id='vert24', zorder=3, clip_on=False, simplify=False)
            c.line([[16.799999999999997, 1.0], [17.799999999999997, 1.0]], id='base310', zorder=3, clip_on=False, linestyle=(0.0, [4.0, 3.0]), simplify=False)
            c.line([[17.799999999999997, 1.0], [18.799999999999997, 1.0]], id='base311', zorder=3, clip_on=False, simplify=False)
            c.line([[18.799999999999997, 1.0], [19.799999999999997, 1.0]], id='base312', zorder=3, clip_on=False, linestyle=(0.0, [4.0, 3.0]), simplify=False)
            for object_id, points in [('base313', [[19.799999999999997, 1.0], [20.799999999999997, 1.0]]), ('flap310a', [[16.799999999999997, 1.0], [17.799999999999997, 2.0]]), ('flap310b', [[17.799999999999997, 2.0], [17.799999999999997, 1.0]]), ('flap311a', [[18.799999999999997, 1.0], [19.799999999999997, 2.0]]), ('flap311b', [[19.799999999999997, 2.0], [19.799999999999997, 1.0]])]:
                c.line(points, id=object_id, zorder=3, clip_on=False, simplify=False)
            c.line([[16.799999999999997, 0.0], [17.799999999999997, 0.0]], id='base300', zorder=3, clip_on=False, linestyle=(0.0, [4.0, 3.0]), simplify=False)
            c.line([[17.799999999999997, 0.0], [18.799999999999997, 0.0]], id='base301', zorder=3, clip_on=False, simplify=False)
            c.line([[18.799999999999997, 0.0], [19.799999999999997, 0.0]], id='base302', zorder=3, clip_on=False, linestyle=(0.0, [4.0, 3.0]), simplify=False)
            for object_id, points in [('base303', [[19.799999999999997, 0.0], [20.799999999999997, 0.0]]), ('flap300a', [[16.799999999999997, 0.0], [16.799999999999997, -1.0]]), ('flap300b', [[16.799999999999997, -1.0], [17.799999999999997, 0.0]]), ('flap301a', [[18.799999999999997, 0.0], [18.799999999999997, -1.0]]), ('flap301b', [[18.799999999999997, -1.0], [19.799999999999997, 0.0]]), ('vert30', [[16.799999999999997, 0.0], [16.799999999999997, 1.0]])]:
                c.line(points, id=object_id, zorder=3, clip_on=False, simplify=False)
            for object_id, points in [('vert31', [[17.799999999999997, 0.0], [17.799999999999997, 1.0]]), ('vert32', [[18.799999999999997, 0.0], [18.799999999999997, 1.0]]), ('vert33', [[19.799999999999997, 0.0], [19.799999999999997, 1.0]])]:
                c.line(points, id=object_id, zorder=3, clip_on=False, linestyle=(0.0, [4.0, 3.0]), simplify=False)
            c.line([[20.799999999999997, 0.0], [20.799999999999997, 1.0]], id='vert34', zorder=3, clip_on=False, simplify=False)
            c.line([[22.4, 1.0], [23.4, 1.0]], id='base410', zorder=3, clip_on=False, linestyle=(0.0, [4.0, 3.0]), simplify=False)
            c.line([[23.4, 1.0], [24.4, 1.0]], id='base411', zorder=3, clip_on=False, simplify=False)
            c.line([[24.4, 1.0], [25.4, 1.0]], id='base412', zorder=3, clip_on=False, linestyle=(0.0, [4.0, 3.0]), simplify=False)
            for object_id, points in [('base413', [[25.4, 1.0], [26.4, 1.0]]), ('flap410a', [[22.4, 1.0], [23.4, 2.0]]), ('flap410b', [[23.4, 2.0], [23.4, 1.0]]), ('flap411a', [[24.4, 1.0], [25.4, 2.0]]), ('flap411b', [[25.4, 2.0], [25.4, 1.0]]), ('base400', [[22.4, 0.0], [23.4, 0.0]])]:
                c.line(points, id=object_id, zorder=3, clip_on=False, simplify=False)
            c.line([[23.4, 0.0], [24.4, 0.0]], id='base401', zorder=3, clip_on=False, linestyle=(0.0, [4.0, 3.0]), simplify=False)
            c.line([[24.4, 0.0], [25.4, 0.0]], id='base402', zorder=3, clip_on=False, simplify=False)
            c.line([[25.4, 0.0], [26.4, 0.0]], id='base403', zorder=3, clip_on=False, linestyle=(0.0, [4.0, 3.0]), simplify=False)
            for object_id, points in [('flap400a', [[23.4, 0.0], [23.4, -1.0]]), ('flap400b', [[23.4, -1.0], [24.4, 0.0]]), ('flap401a', [[25.4, 0.0], [25.4, -1.0]]), ('flap401b', [[25.4, -1.0], [26.4, 0.0]]), ('vert40', [[22.4, 0.0], [22.4, 1.0]])]:
                c.line(points, id=object_id, zorder=3, clip_on=False, simplify=False)
            for object_id, points in [('vert41', [[23.4, 0.0], [23.4, 1.0]]), ('vert42', [[24.4, 0.0], [24.4, 1.0]]), ('vert43', [[25.4, 0.0], [25.4, 1.0]])]:
                c.line(points, id=object_id, zorder=3, clip_on=False, linestyle=(0.0, [4.0, 3.0]), simplify=False)
            c.line([[26.4, 0.0], [26.4, 1.0]], id='vert44', zorder=3, clip_on=False, simplify=False)
            for object_id, text, anchor in [('option0', 'A', (2.0, 2.0)), ('option1', 'B', (7.6, 2.0)), ('option2', 'C', (13.2, 2.0)), ('option3', 'D', (18.799999999999997, 2.0)), ('option4', 'E', (24.4, 2.0))]:
                c.text(text, anchor, id=object_id, rotation_mode='default', offset_pt=(0, 20), annotation_clip=None)
            return c.save(output_path)
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Solid176')
    parser.add_argument('output', nargs='?')
    parser.add_argument('--variant', choices=('C01', 'C02'))
    args = parser.parse_args()
    print(Solid176().draw(args.output, variant=args.variant))
