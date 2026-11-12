"""Frozen question Plane199; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane199:

    def __init__(self):
        self.id = 'Plane199'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:464'
        self.question = 'Which of the following diagrams is impossible to make with the two dominos?\nChoices:\nA:A\nB:B\nC:C\nD:D\nE:E'
        self.answer = 'E'
        self.answer_type = 'choice'
        self.choices = {'A': 'A', 'B': 'B', 'C': 'C', 'D': 'D', 'E': 'E'}
        self.query = self.question
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane199.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-1.6710556181220166, 18.517823184874523], ylim=[-7.158470321966744, 13.030408481029797]) as c:
            c.path([[6, 5], [7, 5], [7, 6], [6, 6], [6, 5]], [1, 2, 2, 2, 79], id='source0top_border')
            c.point([[6.5, 5.5]], filled=True, id='source0top_pip0')
            c.path([[6, 4], [7, 4], [7, 5], [6, 5], [6, 4]], [1, 2, 2, 2, 79], id='source0bottom_border')
            c.point([[6.18, 4.82]], filled=True, id='source0bottom_pip0')
            c.point([[6.82, 4.18]], filled=True, id='source0bottom_pip1')
            c.path([[8, 5], [9, 5], [9, 6], [8, 6], [8, 5]], [1, 2, 2, 2, 79], id='source1top_border')
            c.point([[8.5, 5.5]], filled=True, id='source1top_pip0')
            c.path([[8, 4], [9, 4], [9, 5], [8, 5], [8, 4]], [1, 2, 2, 2, 79], id='source1bottom_border')
            for object_id, points in [('source1bottom_pip0', [[8.18, 4.82]]), ('source1bottom_pip1', [[8.82, 4.18]]), ('source1bottom_pip2', [[8.5, 4.5]])]:
                c.point(points, id=object_id, filled=True)
            c.path([[0, 1], [1, 1], [1, 2], [0, 2], [0, 1]], [1, 2, 2, 2, 79], id='opt0_0_border')
            c.point([[0.5, 1.5]], filled=True, id='opt0_0_pip0')
            c.path([[1, 1], [2, 1], [2, 2], [1, 2], [1, 1]], [1, 2, 2, 2, 79], id='opt0_1_border')
            c.point([[1.5, 1.5]], filled=True, id='opt0_1_pip0')
            c.path([[0, 0], [1, 0], [1, 1], [0, 1], [0, 0]], [1, 2, 2, 2, 79], id='opt0_2_border')
            c.point([[0.18, 0.82]], filled=True, id='opt0_2_pip0')
            c.point([[0.82, 0.18]], filled=True, id='opt0_2_pip1')
            c.path([[1, 0], [2, 0], [2, 1], [1, 1], [1, 0]], [1, 2, 2, 2, 79], id='opt0_3_border')
            for object_id, points in [('opt0_3_pip0', [[1.18, 0.82]]), ('opt0_3_pip1', [[1.8199999999999998, 0.18]]), ('opt0_3_pip2', [[1.5, 0.5]])]:
                c.point(points, id=object_id, filled=True)
            c.path([[4, 1], [5, 1], [5, 2], [4, 2], [4, 1]], [1, 2, 2, 2, 79], id='opt1_0_border')
            c.point([[4.18, 1.8199999999999998]], filled=True, id='opt1_0_pip0')
            c.point([[4.82, 1.18]], filled=True, id='opt1_0_pip1')
            c.path([[5, 1], [6, 1], [6, 2], [5, 2], [5, 1]], [1, 2, 2, 2, 79], id='opt1_1_border')
            c.point([[5.5, 1.5]], filled=True, id='opt1_1_pip0')
            c.path([[4, 0], [5, 0], [5, 1], [4, 1], [4, 0]], [1, 2, 2, 2, 79], id='opt1_2_border')
            c.point([[4.5, 0.5]], filled=True, id='opt1_2_pip0')
            c.path([[5, 0], [6, 0], [6, 1], [5, 1], [5, 0]], [1, 2, 2, 2, 79], id='opt1_3_border')
            for object_id, points in [('opt1_3_pip0', [[5.18, 0.82]]), ('opt1_3_pip1', [[5.82, 0.18]]), ('opt1_3_pip2', [[5.5, 0.5]])]:
                c.point(points, id=object_id, filled=True)
            c.path([[8, 1], [9, 1], [9, 2], [8, 2], [8, 1]], [1, 2, 2, 2, 79], id='opt2_0_border')
            c.point([[8.5, 1.5]], filled=True, id='opt2_0_pip0')
            c.path([[9, 1], [10, 1], [10, 2], [9, 2], [9, 1]], [1, 2, 2, 2, 79], id='opt2_1_border')
            c.point([[9.18, 1.18]], filled=True, id='opt2_1_pip0')
            c.point([[9.82, 1.8199999999999998]], filled=True, id='opt2_1_pip1')
            c.path([[8, 0], [9, 0], [9, 1], [8, 1], [8, 0]], [1, 2, 2, 2, 79], id='opt2_2_border')
            c.point([[8.5, 0.5]], filled=True, id='opt2_2_pip0')
            c.path([[9, 0], [10, 0], [10, 1], [9, 1], [9, 0]], [1, 2, 2, 2, 79], id='opt2_3_border')
            for object_id, points in [('opt2_3_pip0', [[9.18, 0.18]]), ('opt2_3_pip1', [[9.82, 0.82]]), ('opt2_3_pip2', [[9.5, 0.5]])]:
                c.point(points, id=object_id, filled=True)
            c.path([[12, 1], [13, 1], [13, 2], [12, 2], [12, 1]], [1, 2, 2, 2, 79], id='opt3_0_border')
            c.point([[12.18, 1.18]], filled=True, id='opt3_0_pip0')
            c.point([[12.82, 1.8199999999999998]], filled=True, id='opt3_0_pip1')
            c.path([[13, 1], [14, 1], [14, 2], [13, 2], [13, 1]], [1, 2, 2, 2, 79], id='opt3_1_border')
            c.point([[13.5, 1.5]], filled=True, id='opt3_1_pip0')
            c.path([[12, 0], [13, 0], [13, 1], [12, 1], [12, 0]], [1, 2, 2, 2, 79], id='opt3_2_border')
            c.point([[12.5, 0.5]], filled=True, id='opt3_2_pip0')
            c.path([[13, 0], [14, 0], [14, 1], [13, 1], [13, 0]], [1, 2, 2, 2, 79], id='opt3_3_border')
            for object_id, points in [('opt3_3_pip0', [[13.18, 0.18]]), ('opt3_3_pip1', [[13.82, 0.82]]), ('opt3_3_pip2', [[13.5, 0.5]])]:
                c.point(points, id=object_id, filled=True)
            c.path([[16, 1], [17, 1], [17, 2], [16, 2], [16, 1]], [1, 2, 2, 2, 79], id='opt4_0_border')
            c.point([[16.18, 1.8199999999999998]], filled=True, id='opt4_0_pip0')
            c.point([[16.82, 1.18]], filled=True, id='opt4_0_pip1')
            c.path([[17, 1], [18, 1], [18, 2], [17, 2], [17, 1]], [1, 2, 2, 2, 79], id='opt4_1_border')
            c.point([[17.5, 1.5]], filled=True, id='opt4_1_pip0')
            c.path([[16, 0], [17, 0], [17, 1], [16, 1], [16, 0]], [1, 2, 2, 2, 79], id='opt4_2_border')
            c.point([[16.5, 0.5]], filled=True, id='opt4_2_pip0')
            c.path([[17, 0], [18, 0], [18, 1], [17, 1], [17, 0]], [1, 2, 2, 2, 79], id='opt4_3_border')
            for object_id, points in [('opt4_3_pip0', [[17.18, 0.18]]), ('opt4_3_pip1', [[17.82, 0.82]]), ('opt4_3_pip2', [[17.5, 0.5]])]:
                c.point(points, id=object_id, filled=True)
            for object_id, text, anchor in [('label0', '(A)', [-0.8, 0.1]), ('label1', '(B)', [3.2, 0.1]), ('label2', '(C)', [7.2, 0.1]), ('label3', '(D)', [11.2, 0.1]), ('label4', '(E)', [15.2, 0.1])]:
                c.text(text, anchor, id=object_id, offset_pt=[0, 0], vertex=False)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane199().draw(sys.argv[1] if len(sys.argv) > 1 else None))
