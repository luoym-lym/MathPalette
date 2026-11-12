"""Frozen question Solid176; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Solid176:

    def __init__(self):
        self.id = 'Solid176'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:1605'
        self.question = 'One of the following nets cannot be folded along the dashed lines shown to form a cube. Which one?\nChoices:\nA:A\nB:B\nC:C\nD:D\nE:E'
        self.answer = 'C'
        self.answer_type = 'choice'
        self.choices = {'A': 'A', 'B': 'B', 'C': 'C', 'D': 'D', 'E': 'E'}
        self.query = self.question
        self.subject = 'SolidGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'SolidGeometry' / 'dataset_generator/scenes/Solid176.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('SolidGeometry', self.id, variant, output_path)
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
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Solid176().draw(sys.argv[1] if len(sys.argv) > 1 else None))
