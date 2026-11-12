"""Frozen question Plane227; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane227:

    def __init__(self):
        self.id = 'Plane227'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:606'
        self.question = 'Which of the following shapes cannot be formed using the connected sticks shown?\nChoices:\nA:A\nB:B\nC:C\nD:D\nE:E'
        self.answer = 'D'
        self.answer_type = 'choice'
        self.choices = {'A': 'A', 'B': 'B', 'C': 'C', 'D': 'D', 'E': 'E'}
        self.query = self.question
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane227.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-2.355082151757445, 28.964429629998804], ylim=[-11.455980970730264, 19.86353081102599]) as c:
            for object_id, points in [('source0', [[14.0, 7.5], [13.803883864861817, 8.48058067569092]]), ('source1', [[13.803883864861817, 8.48058067569092], [12.823303189170897, 8.284464540552737]]), ('source2', [[12.823303189170897, 8.284464540552737], [12.168372650753055, 7.528775457762919]]), ('source3', [[12.168372650753055, 7.528775457762919], [11.822667291925699, 8.467118574580029]]), ('source4', [[11.822667291925699, 8.467118574580029], [11.476961933098343, 7.528775457762919]]), ('source5', [[11.476961933098343, 7.528775457762919], [12.253075933214609, 6.898182832668453]]), ('source6', [[12.253075933214609, 6.898182832668453], [13.253075933214609, 6.898182832668453]]), ('source7', [[13.253075933214609, 6.898182832668453], [14.206658598348751, 6.597051464731355]]), ('source8', [[14.206658598348751, 6.597051464731355], [15.145001715165861, 6.942756823558711]]), ('source9', [[15.145001715165861, 6.942756823558711], [15.341117850304046, 7.923337499249631]])]:
                c.line(points, id=object_id)
            for object_id, points in [('sourcepin0', [[14.0, 7.5]]), ('sourcepin1', [[13.803883864861817, 8.48058067569092]]), ('sourcepin2', [[12.823303189170897, 8.284464540552737]]), ('sourcepin3', [[12.168372650753055, 7.528775457762919]]), ('sourcepin4', [[11.822667291925699, 8.467118574580029]]), ('sourcepin5', [[11.476961933098343, 7.528775457762919]]), ('sourcepin6', [[12.253075933214609, 6.898182832668453]]), ('sourcepin7', [[13.253075933214609, 6.898182832668453]]), ('sourcepin8', [[14.206658598348751, 6.597051464731355]]), ('sourcepin9', [[15.145001715165861, 6.942756823558711]]), ('sourcepin10', [[15.341117850304046, 7.923337499249631]])]:
                c.point(points, id=object_id, filled=True)
            c.line([[0.0, 0.0], [1.0, 0.0]], id='opt0_0')
            c.point([[0.0, 0.0]], filled=True, id='opt0pin0')
            c.line([[1.0, 0.0], [2.0, 0.0]], id='opt0_1')
            c.point([[1.0, 0.0]], filled=True, id='opt0pin1')
            c.line([[2.0, 0.0], [3.0, 0.0]], id='opt0_2')
            c.point([[2.0, 0.0]], filled=True, id='opt0pin2')
            c.line([[3.0, 0.0], [3.0, 1.0]], id='opt0_3')
            c.point([[3.0, 0.0]], filled=True, id='opt0pin3')
            c.line([[3.0, 1.0], [2.0, 1.0]], id='opt0_4')
            c.point([[3.0, 1.0]], filled=True, id='opt0pin4')
            c.line([[2.0, 1.0], [2.0, 2.0]], id='opt0_5')
            c.point([[2.0, 1.0]], filled=True, id='opt0pin5')
            c.line([[2.0, 2.0], [1.0, 2.0]], id='opt0_6')
            c.point([[2.0, 2.0]], filled=True, id='opt0pin6')
            c.line([[1.0, 2.0], [1.0, 1.0]], id='opt0_7')
            c.point([[1.0, 2.0]], filled=True, id='opt0pin7')
            c.line([[1.0, 1.0], [0.0, 1.0]], id='opt0_8')
            c.point([[1.0, 1.0]], filled=True, id='opt0pin8')
            c.line([[0.0, 1.0], [0.0, 0.0]], id='opt0_9')
            c.point([[0.0, 1.0]], filled=True, id='opt0pin9')
            c.line([[6.0, 0.0], [7.0, 0.0]], id='opt1_0')
            c.point([[6.0, 0.0]], filled=True, id='opt1pin0')
            c.line([[7.0, 0.0], [8.0, 0.0]], id='opt1_1')
            c.point([[7.0, 0.0]], filled=True, id='opt1pin1')
            c.line([[8.0, 0.0], [8.0, 1.0]], id='opt1_2')
            c.point([[8.0, 0.0]], filled=True, id='opt1pin2')
            c.line([[8.0, 1.0], [8.0, 2.0]], id='opt1_3')
            c.point([[8.0, 1.0]], filled=True, id='opt1pin3')
            c.line([[8.0, 2.0], [8.0, 3.0]], id='opt1_4')
            c.point([[8.0, 2.0]], filled=True, id='opt1pin4')
            c.line([[8.0, 3.0], [7.0, 3.0]], id='opt1_5')
            c.point([[8.0, 3.0]], filled=True, id='opt1pin5')
            c.line([[7.0, 3.0], [6.0, 3.0]], id='opt1_6')
            c.point([[7.0, 3.0]], filled=True, id='opt1pin6')
            c.line([[6.0, 3.0], [6.0, 2.0]], id='opt1_7')
            c.point([[6.0, 3.0]], filled=True, id='opt1pin7')
            c.line([[6.0, 2.0], [6.0, 1.0]], id='opt1_8')
            c.point([[6.0, 2.0]], filled=True, id='opt1pin8')
            c.line([[6.0, 1.0], [6.0, 0.0]], id='opt1_9')
            c.point([[6.0, 1.0]], filled=True, id='opt1pin9')
            c.line([[12.0, 0.0], [13.0, 0.0]], id='opt2_0')
            c.point([[12.0, 0.0]], filled=True, id='opt2pin0')
            c.line([[13.0, 0.0], [14.0, 0.0]], id='opt2_1')
            c.point([[13.0, 0.0]], filled=True, id='opt2pin1')
            c.line([[14.0, 0.0], [14.0, 1.0]], id='opt2_2')
            c.point([[14.0, 0.0]], filled=True, id='opt2pin2')
            c.line([[14.0, 1.0], [15.0, 1.0]], id='opt2_3')
            c.point([[14.0, 1.0]], filled=True, id='opt2pin3')
            c.line([[15.0, 1.0], [15.0, 2.0]], id='opt2_4')
            c.point([[15.0, 1.0]], filled=True, id='opt2pin4')
            c.line([[15.0, 2.0], [14.0, 2.0]], id='opt2_5')
            c.point([[15.0, 2.0]], filled=True, id='opt2pin5')
            c.line([[14.0, 2.0], [13.0, 2.0]], id='opt2_6')
            c.point([[14.0, 2.0]], filled=True, id='opt2pin6')
            c.line([[13.0, 2.0], [13.0, 1.0]], id='opt2_7')
            c.point([[13.0, 2.0]], filled=True, id='opt2pin7')
            c.line([[13.0, 1.0], [12.0, 1.0]], id='opt2_8')
            c.point([[13.0, 1.0]], filled=True, id='opt2pin8')
            c.line([[12.0, 1.0], [12.0, 0.0]], id='opt2_9')
            c.point([[12.0, 1.0]], filled=True, id='opt2pin9')
            c.line([[19.0, 0.0], [20.0, 0.0]], id='opt3_0')
            c.point([[19.0, 0.0]], filled=True, id='opt3pin0')
            c.line([[20.0, 0.0], [20.0, 1.0]], id='opt3_1')
            c.point([[20.0, 0.0]], filled=True, id='opt3pin1')
            c.line([[20.0, 1.0], [21.0, 1.0]], id='opt3_2')
            c.point([[20.0, 1.0]], filled=True, id='opt3pin2')
            c.line([[21.0, 1.0], [21.0, 2.0]], id='opt3_3')
            c.point([[21.0, 1.0]], filled=True, id='opt3pin3')
            c.line([[21.0, 2.0], [20.0, 2.0]], id='opt3_4')
            c.point([[21.0, 2.0]], filled=True, id='opt3pin4')
            c.line([[20.0, 2.0], [20.0, 3.0]], id='opt3_5')
            c.point([[20.0, 2.0]], filled=True, id='opt3pin5')
            c.line([[20.0, 3.0], [19.0, 3.0]], id='opt3_6')
            c.point([[20.0, 3.0]], filled=True, id='opt3pin6')
            c.line([[19.0, 3.0], [19.0, 2.0]], id='opt3_7')
            c.point([[19.0, 3.0]], filled=True, id='opt3pin7')
            c.line([[19.0, 2.0], [18.0, 2.0]], id='opt3_8')
            c.point([[19.0, 2.0]], filled=True, id='opt3pin8')
            c.line([[18.0, 2.0], [18.0, 1.0]], id='opt3_9')
            c.point([[18.0, 2.0]], filled=True, id='opt3pin9')
            c.line([[18.0, 1.0], [19.0, 1.0]], id='opt3_10')
            c.point([[18.0, 1.0]], filled=True, id='opt3pin10')
            c.line([[19.0, 1.0], [19.0, 0.0]], id='opt3_11')
            c.point([[19.0, 1.0]], filled=True, id='opt3pin11')
            c.line([[24.0, 0.0], [25.0, 0.0]], id='opt4_0')
            c.point([[24.0, 0.0]], filled=True, id='opt4pin0')
            c.line([[25.0, 0.0], [26.0, 0.0]], id='opt4_1')
            c.point([[25.0, 0.0]], filled=True, id='opt4pin1')
            c.line([[26.0, 0.0], [27.0, 0.0]], id='opt4_2')
            c.point([[26.0, 0.0]], filled=True, id='opt4pin2')
            c.line([[27.0, 0.0], [28.0, 0.0]], id='opt4_3')
            c.point([[27.0, 0.0]], filled=True, id='opt4pin3')
            c.line([[28.0, 0.0], [28.0, 1.0]], id='opt4_4')
            c.point([[28.0, 0.0]], filled=True, id='opt4pin4')
            c.line([[28.0, 1.0], [27.0, 1.0]], id='opt4_5')
            c.point([[28.0, 1.0]], filled=True, id='opt4pin5')
            c.line([[27.0, 1.0], [26.0, 1.0]], id='opt4_6')
            c.point([[27.0, 1.0]], filled=True, id='opt4pin6')
            c.line([[26.0, 1.0], [25.0, 1.0]], id='opt4_7')
            c.point([[26.0, 1.0]], filled=True, id='opt4pin7')
            c.line([[25.0, 1.0], [24.0, 1.0]], id='opt4_8')
            c.point([[25.0, 1.0]], filled=True, id='opt4pin8')
            c.line([[24.0, 1.0], [24.0, 0.0]], id='opt4_9')
            c.point([[24.0, 1.0]], filled=True, id='opt4pin9')
            for object_id, text, anchor in [('label0', '(A)', [-1, 0.2]), ('label1', '(B)', [5, 0.2]), ('label2', '(C)', [11, 0.2]), ('label3', '(D)', [17, 0.2]), ('label4', '(E)', [23, 0.2])]:
                c.text(text, anchor, id=object_id, offset_pt=[0, 0], vertex=False)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane227().draw(sys.argv[1] if len(sys.argv) > 1 else None))
