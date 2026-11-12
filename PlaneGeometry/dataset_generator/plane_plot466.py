"""Frozen question Plane466; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane466:

    def __init__(self):
        self.id = 'Plane466'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:2653'
        self.question = 'In the pattern below, a large circle moves clockwise through the four squares, and a dot moves counterclockwise through the eight exterior segments of the four squares.\n\nIf the pattern is continued, where will the large circle and the dot be after the 247th move?\nThe five answer choices are shown from left to right as A, B, C, D, and E.\nChoices:\nA:A\nB:B\nC:C\nD:D\nE:E'
        self.answer = 'A'
        self.answer_type = 'choice'
        self.choices = {'A': 'A', 'B': 'B', 'C': 'C', 'D': 'D', 'E': 'E'}
        self.query = self.question
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane466.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-0.46231418116030465, 15.191752384127017], ylim=[-4.036082441337699, 11.617984123949622]) as c:
            c.path([[0.0, 5], [2.0, 5], [2.0, 7], [0.0, 7], [0.0, 5]], [1, 2, 2, 2, 79], id='o0')
            c.line([[1.0, 5], [1.0, 7]], id='o1')
            c.line([[0.0, 6], [2.0, 6]], id='o2')
            c.circle([0.5, 6.5], 0.3, id='o3')
            c.point([[1.5, 5]], filled=True, id='o4')
            c.path([[3.2, 5], [5.2, 5], [5.2, 7], [3.2, 7], [3.2, 5]], [1, 2, 2, 2, 79], id='o5')
            c.line([[4.2, 5], [4.2, 7]], id='o6')
            c.line([[3.2, 6], [5.2, 6]], id='o7')
            c.circle([4.7, 6.5], 0.3, id='o8')
            c.point([[5.2, 5.5]], filled=True, id='o9')
            c.path([[6.4, 5], [8.4, 5], [8.4, 7], [6.4, 7], [6.4, 5]], [1, 2, 2, 2, 79], id='o10')
            c.line([[7.4, 5], [7.4, 7]], id='o11')
            c.line([[6.4, 6], [8.4, 6]], id='o12')
            c.circle([7.9, 5.5], 0.3, id='o13')
            c.point([[8.4, 6.5]], filled=True, id='o14')
            c.path([[9.600000000000001, 5], [11.600000000000001, 5], [11.600000000000001, 7], [9.600000000000001, 7], [9.600000000000001, 5]], [1, 2, 2, 2, 79], id='o15')
            c.line([[10.600000000000001, 5], [10.600000000000001, 7]], id='o16')
            c.line([[9.600000000000001, 6], [11.600000000000001, 6]], id='o17')
            c.circle([10.100000000000001, 5.5], 0.3, id='o18')
            c.point([[11.100000000000001, 7]], filled=True, id='o19')
            c.path([[12.8, 5], [14.8, 5], [14.8, 7], [12.8, 7], [12.8, 5]], [1, 2, 2, 2, 79], id='o20')
            c.line([[13.8, 5], [13.8, 7]], id='o21')
            c.line([[12.8, 6], [14.8, 6]], id='o22')
            c.circle([13.3, 6.5], 0.3, id='o23')
            c.point([[13.3, 7]], filled=True, id='o24')
            c.path([[0.0, 0], [2.0, 0], [2.0, 2], [0.0, 2], [0.0, 0]], [1, 2, 2, 2, 79], id='o25')
            c.line([[1.0, 0], [1.0, 2]], id='o26')
            c.line([[0.0, 1], [2.0, 1]], id='o27')
            c.circle([1.5, 0.5], 0.3, id='o28')
            c.point([[0.0, 0.5]], filled=True, id='o29')
            c.path([[3.2, 0], [5.2, 0], [5.2, 2], [3.2, 2], [3.2, 0]], [1, 2, 2, 2, 79], id='o30')
            c.line([[4.2, 0], [4.2, 2]], id='o31')
            c.line([[3.2, 1], [5.2, 1]], id='o32')
            c.circle([4.7, 1.5], 0.3, id='o33')
            c.point([[3.2, 0.5]], filled=True, id='o34')
            c.path([[6.4, 0], [8.4, 0], [8.4, 2], [6.4, 2], [6.4, 0]], [1, 2, 2, 2, 79], id='o35')
            c.line([[7.4, 0], [7.4, 2]], id='o36')
            c.line([[6.4, 1], [8.4, 1]], id='o37')
            c.circle([7.9, 0.5], 0.3, id='o38')
            c.point([[6.4, 1.5]], filled=True, id='o39')
            c.path([[9.600000000000001, 0], [11.600000000000001, 0], [11.600000000000001, 2], [9.600000000000001, 2], [9.600000000000001, 0]], [1, 2, 2, 2, 79], id='o40')
            c.line([[10.600000000000001, 0], [10.600000000000001, 2]], id='o41')
            c.line([[9.600000000000001, 1], [11.600000000000001, 1]], id='o42')
            c.circle([10.100000000000001, 0.5], 0.3, id='o43')
            c.point([[9.600000000000001, 1.5]], filled=True, id='o44')
            c.path([[12.8, 0], [14.8, 0], [14.8, 2], [12.8, 2], [12.8, 0]], [1, 2, 2, 2, 79], id='o45')
            c.line([[13.8, 0], [13.8, 2]], id='o46')
            c.line([[12.8, 1], [14.8, 1]], id='o47')
            c.circle([13.3, 1.5], 0.3, id='o48')
            c.point([[14.3, 0]], filled=True, id='o49')
            for object_id, text, anchor in [('t0', '1', [1.0, 7.5]), ('t1', '2', [4.2, 7.5]), ('t2', '3', [7.4, 7.5]), ('t3', '4', [10.600000000000001, 7.5]), ('t4', '5', [13.8, 7.5])]:
                c.text(text, anchor, id=object_id, offset_pt=[0, 0], vertex=False)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane466().draw(sys.argv[1] if len(sys.argv) > 1 else None))
