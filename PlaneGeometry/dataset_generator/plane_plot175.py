"""Frozen question Plane175; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane175:

    def __init__(self):
        self.id = 'Plane175'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:179'
        self.question = 'A square piece of paper has been cut in three pieces. Two of them are in the picture on the right. What is the third one?\nChoices:\nA:A\nB:B\nC:C\nD:D\nE:E'
        self.answer = 'A'
        self.answer_type = 'choice'
        self.choices = {'A': 'A', 'B': 'B', 'C': 'C', 'D': 'D', 'E': 'E'}
        self.query = self.question
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane175.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-0.46161278474120415, 19.297449014554005], ylim=[-6.605572173782688, 13.153489625512519]) as c:
            for object_id, vertices, codes in [('given_square', [[5, 6], [6, 6], [6, 7], [5, 7], [5, 6]], [1, 2, 2, 2, 79]), ('given_notched_piece', [[8.0, 6.0], [10.82842712474619, 6.0], [10.121320343559642, 7.414213562373095], [9.414213562373096, 6.707106781186548], [8.707106781186548, 7.414213562373095], [8.0, 7.414213562373095], [8.0, 6.0]], [1, 2, 2, 2, 2, 2, 79]), ('option0', [[0.0, 0.0], [2.8284271247461903, 0.0], [2.8284271247461903, 1.4142135623730951], [2.121320343559643, 1.4142135623730951], [1.4142135623730951, 0.7071067811865476], [0.7071067811865476, 1.4142135623730951], [0.0, 2.8284271247461903], [0.0, 0.0]], [1, 2, 2, 2, 2, 2, 2, 79]), ('option1', [[4.0, 0.0], [6.82842712474619, 0.0], [6.82842712474619, 2.8284271247461903], [5.767766952966369, 0.7071067811865476], [4.707106781186548, 0.7071067811865476], [4.707106781186548, 1.4142135623730951], [4.0, 0.0]], [1, 2, 2, 2, 2, 2, 79]), ('option2', [[8.0, 2.8284271247461903], [10.82842712474619, 2.8284271247461903], [10.82842712474619, 1.4142135623730951], [9.414213562373096, 0.3535533905932738], [8.707106781186548, 1.4142135623730951], [8.0, 1.4142135623730951], [8.0, 2.8284271247461903]], [1, 2, 2, 2, 2, 2, 79]), ('option3', [[12.0, 0.0], [14.82842712474619, 0.0], [14.82842712474619, 0.7071067811865476], [13.414213562373096, 0.7071067811865476], [12.707106781186548, 2.8284271247461903], [12.0, 2.8284271247461903], [12.0, 0.0]], [1, 2, 2, 2, 2, 2, 79]), ('option4', [[16.0, 2.8284271247461903], [17.76776695296637, 2.8284271247461903], [17.76776695296637, 1.7677669529663689], [18.82842712474619, 1.7677669529663689], [18.82842712474619, 0.0], [17.414213562373096, 0.0], [18.121320343559642, 0.3535533905932738], [16.707106781186546, 1.0606601717798214], [16.0, 1.0606601717798214], [16.0, 2.8284271247461903]], [1, 2, 2, 2, 2, 2, 2, 2, 2, 79])]:
                c.path(vertices, codes, id=object_id)
            for object_id, text, anchor in [('label0', '(A)', [1.4, -0.65]), ('label1', '(B)', [5.4, -0.65]), ('label2', '(C)', [9.4, -0.65]), ('label3', '(D)', [13.4, -0.65]), ('label4', '(E)', [17.4, -0.65])]:
                c.text(text, anchor, id=object_id, offset_pt=[0, 0], vertex=False)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane175().draw(sys.argv[1] if len(sys.argv) > 1 else None))
