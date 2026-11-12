"""Frozen question Solid101; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Solid101:

    def __init__(self):
        self.id = 'Solid101'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:327'
        self.question = 'Each side of a die is marked with either 1,2 or 3 dots so that the probability of rolling a 1 is equal to $\\frac{1}{2}$, the probability of rolling a 2 is equal to $\\frac{1}{3}$ and the probability of rolling a 3 is equal to $\\frac{1}{6}$. Which of these pictures cannot be a picture of this particular die?\nChoices:\nA:A\nB:B\nC:C\nD:D\nE:E'
        self.answer = 'C'
        self.answer_type = 'choice'
        self.choices = {'A': 'A', 'B': 'B', 'C': 'C', 'D': 'D', 'E': 'E'}
        self.query = self.question
        self.subject = 'SolidGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'SolidGeometry' / 'dataset_generator/scenes/Solid101.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('SolidGeometry', self.id, variant, output_path)
        with Canvas(SOLID, xlim=[-0.7664851963866655, 10.48268553553395], ylim=[-5.156434602436827, 6.092736129483789], projection=[[1, -0.5, 0], [0.18, 0.3, 1]], origin=[0, 0, 0], offset=[0, 0]) as c:
            for object_id, points in [('die0e0', c.project([[0.0, 0.0, 0.0], [1.0, 0.0, 0.0]])), ('die0e1', c.project([[0.0, 0.0, 1.0], [1.0, 0.0, 1.0]])), ('die0e2', c.project([[0.0, 1.0, 1.0], [1.0, 1.0, 1.0]])), ('die0e3', c.project([[0.0, 0.0, 0.0], [0.0, 1.0, 0.0]])), ('die0e4', c.project([[0.0, 0.0, 1.0], [0.0, 1.0, 1.0]])), ('die0e5', c.project([[1.0, 0.0, 1.0], [1.0, 1.0, 1.0]])), ('die0e6', c.project([[0.0, 0.0, 0.0], [0.0, 0.0, 1.0]])), ('die0e7', c.project([[0.0, 1.0, 0.0], [0.0, 1.0, 1.0]])), ('die0e8', c.project([[1.0, 0.0, 0.0], [1.0, 0.0, 1.0]]))]:
                c.line(points, id=object_id, clip_on=False, zorder=3)
            for object_id, points in [('die0toppip0', c.project([[0.25, 0.75, 1.0]])), ('die0toppip1', c.project([[0.75, 0.25, 1.0]])), ('die0frontpip0', c.project([[0.5, 0.0, 0.5]]))]:
                c.point(points, id=object_id, filled=True)
            for object_id, points in [('die1e0', c.project([[2.3, 0.0, -0.414], [3.3, 0.0, -0.414]])), ('die1e1', c.project([[2.3, 0.0, 0.5860000000000001], [3.3, 0.0, 0.5860000000000001]])), ('die1e2', c.project([[2.3, 1.0, 0.5860000000000001], [3.3, 1.0, 0.5860000000000001]])), ('die1e3', c.project([[2.3, 0.0, -0.414], [2.3, 1.0, -0.414]])), ('die1e4', c.project([[2.3, 0.0, 0.5860000000000001], [2.3, 1.0, 0.5860000000000001]])), ('die1e5', c.project([[3.3, 0.0, 0.5860000000000001], [3.3, 1.0, 0.5860000000000001]])), ('die1e6', c.project([[2.3, 0.0, -0.414], [2.3, 0.0, 0.5860000000000001]])), ('die1e7', c.project([[2.3, 1.0, -0.414], [2.3, 1.0, 0.5860000000000001]])), ('die1e8', c.project([[3.3, 0.0, -0.414], [3.3, 0.0, 0.5860000000000001]]))]:
                c.line(points, id=object_id, clip_on=False, zorder=3)
            for object_id, points in [('die1toppip0', c.project([[2.8, 0.5, 0.5860000000000001]])), ('die1leftpip0', c.project([[2.3, 0.5, 0.08600000000000002]])), ('die1frontpip0', c.project([[2.8, 0.0, 0.08600000000000002]]))]:
                c.point(points, id=object_id, filled=True)
            for object_id, points in [('die2e0', c.project([[4.6, 0.0, -0.828], [5.6, 0.0, -0.828]])), ('die2e1', c.project([[4.6, 0.0, 0.17200000000000004], [5.6, 0.0, 0.17200000000000004]])), ('die2e2', c.project([[4.6, 1.0, 0.17200000000000004], [5.6, 1.0, 0.17200000000000004]])), ('die2e3', c.project([[4.6, 0.0, -0.828], [4.6, 1.0, -0.828]])), ('die2e4', c.project([[4.6, 0.0, 0.17200000000000004], [4.6, 1.0, 0.17200000000000004]])), ('die2e5', c.project([[5.6, 0.0, 0.17200000000000004], [5.6, 1.0, 0.17200000000000004]])), ('die2e6', c.project([[4.6, 0.0, -0.828], [4.6, 0.0, 0.17200000000000004]])), ('die2e7', c.project([[4.6, 1.0, -0.828], [4.6, 1.0, 0.17200000000000004]])), ('die2e8', c.project([[5.6, 0.0, -0.828], [5.6, 0.0, 0.17200000000000004]]))]:
                c.line(points, id=object_id, clip_on=False, zorder=3)
            for object_id, points in [('die2toppip0', c.project([[4.8, 0.5, 0.17200000000000004]])), ('die2toppip1', c.project([[5.1, 0.5, 0.17200000000000004]])), ('die2toppip2', c.project([[5.3999999999999995, 0.5, 0.17200000000000004]])), ('die2leftpip0', c.project([[4.6, 0.5, -0.32799999999999996]])), ('die2frontpip0', c.project([[4.85, 0.0, -0.578]])), ('die2frontpip1', c.project([[5.1, 0.0, -0.32799999999999996]])), ('die2frontpip2', c.project([[5.35, 0.0, -0.07799999999999996]]))]:
                c.point(points, id=object_id, filled=True)
            for object_id, points in [('die3e0', c.project([[6.8999999999999995, 0.0, -1.2419999999999998], [7.8999999999999995, 0.0, -1.2419999999999998]])), ('die3e1', c.project([[6.8999999999999995, 0.0, -0.24199999999999977], [7.8999999999999995, 0.0, -0.24199999999999977]])), ('die3e2', c.project([[6.8999999999999995, 1.0, -0.24199999999999977], [7.8999999999999995, 1.0, -0.24199999999999977]])), ('die3e3', c.project([[6.8999999999999995, 0.0, -1.2419999999999998], [6.8999999999999995, 1.0, -1.2419999999999998]])), ('die3e4', c.project([[6.8999999999999995, 0.0, -0.24199999999999977], [6.8999999999999995, 1.0, -0.24199999999999977]])), ('die3e5', c.project([[7.8999999999999995, 0.0, -0.24199999999999977], [7.8999999999999995, 1.0, -0.24199999999999977]])), ('die3e6', c.project([[6.8999999999999995, 0.0, -1.2419999999999998], [6.8999999999999995, 0.0, -0.24199999999999977]])), ('die3e7', c.project([[6.8999999999999995, 1.0, -1.2419999999999998], [6.8999999999999995, 1.0, -0.24199999999999977]])), ('die3e8', c.project([[7.8999999999999995, 0.0, -1.2419999999999998], [7.8999999999999995, 0.0, -0.24199999999999977]]))]:
                c.line(points, id=object_id, clip_on=False, zorder=3)
            for object_id, points in [('die3toppip0', c.project([[7.1, 0.5, -0.24199999999999977]])), ('die3toppip1', c.project([[7.3999999999999995, 0.5, -0.24199999999999977]])), ('die3toppip2', c.project([[7.699999999999999, 0.5, -0.24199999999999977]])), ('die3leftpip0', c.project([[6.8999999999999995, 0.25, -0.49199999999999977]])), ('die3leftpip1', c.project([[6.8999999999999995, 0.75, -0.9919999999999998]]))]:
                c.point(points, id=object_id, filled=True)
            for object_id, points in [('die4e0', c.project([[9.2, 0.0, -1.656], [10.2, 0.0, -1.656]])), ('die4e1', c.project([[9.2, 0.0, -0.6559999999999999], [10.2, 0.0, -0.6559999999999999]])), ('die4e2', c.project([[9.2, 1.0, -0.6559999999999999], [10.2, 1.0, -0.6559999999999999]])), ('die4e3', c.project([[9.2, 0.0, -1.656], [9.2, 1.0, -1.656]])), ('die4e4', c.project([[9.2, 0.0, -0.6559999999999999], [9.2, 1.0, -0.6559999999999999]])), ('die4e5', c.project([[10.2, 0.0, -0.6559999999999999], [10.2, 1.0, -0.6559999999999999]])), ('die4e6', c.project([[9.2, 0.0, -1.656], [9.2, 0.0, -0.6559999999999999]])), ('die4e7', c.project([[9.2, 1.0, -1.656], [9.2, 1.0, -0.6559999999999999]])), ('die4e8', c.project([[10.2, 0.0, -1.656], [10.2, 0.0, -0.6559999999999999]]))]:
                c.line(points, id=object_id, clip_on=False, zorder=3)
            for object_id, points in [('die4toppip0', c.project([[9.7, 0.5, -0.6559999999999999]])), ('die4leftpip0', c.project([[9.2, 0.25, -0.9059999999999999]])), ('die4leftpip1', c.project([[9.2, 0.75, -1.406]])), ('die0leftpip0', c.project([[0.0, 0.25, 0.75]])), ('die0leftpip1', c.project([[0.0, 0.5, 0.5]])), ('die0leftpip2', c.project([[0.0, 0.75, 0.25]])), ('die3frontpip0', c.project([[7.1499999999999995, 0.0, -0.9919999999999998]])), ('die3frontpip1', c.project([[7.6499999999999995, 0.0, -0.49199999999999977]])), ('die4frontpip0', c.project([[9.45, 0.0, -1.406]])), ('die4frontpip1', c.project([[9.95, 0.0, -0.9059999999999999]]))]:
                c.point(points, id=object_id, filled=True)
            for object_id, text, anchor in [('option0', '(A)', c.project([0.2, 0, 0.0])), ('option1', '(B)', c.project([2.5, 0, -0.414])), ('option2', '(C)', c.project([4.8, 0, -0.828])), ('option3', '(D)', c.project([7.1, 0, -1.2419999999999998])), ('option4', '(E)', c.project([9.399999999999999, 0, -1.656]))]:
                c.text(text, anchor, id=object_id, offset_pt=[0, -20], vertex=False)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Solid101().draw(sys.argv[1] if len(sys.argv) > 1 else None))
