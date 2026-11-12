"""Frozen question Solid84; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Solid84:

    def __init__(self):
        self.id = 'Solid84'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:59'
        self.question = 'The cube is shown above in two different orientations.\nIts six faces are shown in a row.\nWhich face is opposite to the face shown by itself below the row of six faces?'
        self.answer = 'C'
        self.answer_type = 'text'
        self.query = self.question
        self.points = {'cube0000': [1.4, 0, 7],
         'cube0001': [1.4, 0, 9],
         'cube0010': [1.4, 2, 7],
         'cube0011': [1.4, 2, 9],
         'cube0100': [3.4, 0, 7],
         'cube0101': [3.4, 0, 9],
         'cube0110': [3.4, 2, 7],
         'cube0111': [3.4, 2, 9],
         'cube1000': [7, 0, 7],
         'cube1001': [7, 0, 9],
         'cube1010': [7, 2, 7],
         'cube1011': [7, 2, 9],
         'cube1100': [9, 0, 7],
         'cube1101': [9, 0, 9],
         'cube1110': [9, 2, 7],
         'cube1111': [9, 2, 9]}
        self.subject = 'SolidGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'SolidGeometry' / 'dataset_generator/scenes/Solid84.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('SolidGeometry', self.id, variant, output_path)
        with Canvas(SOLID, xlim=[-0.28640932321931345, 11.803820902676676], ylim=[-1.482406173994507, 10.607824051901483], projection=[[1, 0.35, 0], [0, 0.35, 1]], origin=[0, 0, 0], offset=[0, 0]) as c:
            for object_id, points in [('cube0000_cube0100', c.project([self.points['cube0000'], self.points['cube0100']])), ('cube0000_cube0001', c.project([self.points['cube0000'], self.points['cube0001']])), ('cube0001_cube0101', c.project([self.points['cube0001'], self.points['cube0101']])), ('cube0001_cube0011', c.project([self.points['cube0001'], self.points['cube0011']])), ('cube0011_cube0111', c.project([self.points['cube0011'], self.points['cube0111']])), ('cube0100_cube0110', c.project([self.points['cube0100'], self.points['cube0110']])), ('cube0100_cube0101', c.project([self.points['cube0100'], self.points['cube0101']])), ('cube0101_cube0111', c.project([self.points['cube0101'], self.points['cube0111']])), ('cube0110_cube0111', c.project([self.points['cube0110'], self.points['cube0111']])), ('cube0topline0', c.project([[1.9, 0.5, 9], [2.9, 0.5, 9]])), ('cube0topline1', c.project([[2.9, 0.5, 9], [2.9, 1.5, 9]])), ('cube0topline2', c.project([[2.9, 1.5, 9], [1.9, 1.5, 9]])), ('cube0topline3', c.project([[1.9, 1.5, 9], [1.9, 0.5, 9]])), ('cube0frontline0', c.project([[1.4, 0, 8.0], [3.4, 0, 8.0]])), ('cube0rightline0', c.project([[3.4, 0.4, 8.0], [3.4, 1.0, 8.6]])), ('cube0rightline1', c.project([[3.4, 1.0, 8.6], [3.4, 1.6, 8.0]])), ('cube0rightline2', c.project([[3.4, 1.6, 8.0], [3.4, 1.0, 7.4]])), ('cube0rightline3', c.project([[3.4, 1.0, 7.4], [3.4, 0.4, 8.0]])), ('cube1000_cube1100', c.project([self.points['cube1000'], self.points['cube1100']])), ('cube1000_cube1001', c.project([self.points['cube1000'], self.points['cube1001']])), ('cube1001_cube1101', c.project([self.points['cube1001'], self.points['cube1101']])), ('cube1001_cube1011', c.project([self.points['cube1001'], self.points['cube1011']])), ('cube1011_cube1111', c.project([self.points['cube1011'], self.points['cube1111']])), ('cube1100_cube1110', c.project([self.points['cube1100'], self.points['cube1110']])), ('cube1100_cube1101', c.project([self.points['cube1100'], self.points['cube1101']])), ('cube1101_cube1111', c.project([self.points['cube1101'], self.points['cube1111']])), ('cube1110_cube1111', c.project([self.points['cube1110'], self.points['cube1111']])), ('cube1topline0', c.project([[7, 1.0, 9], [9, 1.0, 9]])), ('cube1topline1', c.project([[8.0, 0, 9], [8.0, 2, 9]])), ('cube1frontline0', c.project([[7.5, 0, 7.5], [8.5, 0, 7.5]])), ('cube1frontline1', c.project([[8.5, 0, 7.5], [8.5, 0, 8.5]])), ('cube1frontline2', c.project([[8.5, 0, 8.5], [7.5, 0, 8.5]])), ('cube1frontline3', c.project([[7.5, 0, 8.5], [7.5, 0, 7.5]])), ('cube1rightline0', c.project([[9, 0, 7], [9, 2, 9]])), ('cube1rightline1', c.project([[9, 0, 9], [9, 2, 7]])), ('face0line0', c.project([[0.0, 0, 4.8], [1.0, 0, 4.8]])), ('face0line1', c.project([[1.0, 0, 4.8], [1.0, 0, 5.8]])), ('face0line2', c.project([[1.0, 0, 5.8], [0.0, 0, 5.8]])), ('face0line3', c.project([[0.0, 0, 5.8], [0.0, 0, 4.8]])), ('face0line4', c.project([[0.0, 0, 5.3], [0.5, 0, 5.8]])), ('face0line5', c.project([[0.5, 0, 5.8], [1.0, 0, 5.3]])), ('face0line6', c.project([[1.0, 0, 5.3], [0.5, 0, 4.8]])), ('face0line7', c.project([[0.5, 0, 4.8], [0.0, 0, 5.3]])), ('face1line0', c.project([[2.1, 0, 4.8], [3.1, 0, 4.8]])), ('face1line1', c.project([[3.1, 0, 4.8], [3.1, 0, 5.8]])), ('face1line2', c.project([[3.1, 0, 5.8], [2.1, 0, 5.8]])), ('face1line3', c.project([[2.1, 0, 5.8], [2.1, 0, 4.8]])), ('face1line4', c.project([[2.3000000000000003, 0, 5.3], [2.6, 0, 5.6]])), ('face1line5', c.project([[2.6, 0, 5.6], [2.9000000000000004, 0, 5.3]])), ('face1line6', c.project([[2.9000000000000004, 0, 5.3], [2.6, 0, 5.0]])), ('face1line7', c.project([[2.6, 0, 5.0], [2.3000000000000003, 0, 5.3]])), ('face2line0', c.project([[4.2, 0, 4.8], [5.2, 0, 4.8]])), ('face2line1', c.project([[5.2, 0, 4.8], [5.2, 0, 5.8]])), ('face2line2', c.project([[5.2, 0, 5.8], [4.2, 0, 5.8]])), ('face2line3', c.project([[4.2, 0, 5.8], [4.2, 0, 4.8]])), ('face2line4', c.project([[4.2, 0, 5.3], [5.2, 0, 5.3]])), ('face3line0', c.project([[6.300000000000001, 0, 4.8], [7.300000000000001, 0, 4.8]])), ('face3line1', c.project([[7.300000000000001, 0, 4.8], [7.300000000000001, 0, 5.8]])), ('face3line2', c.project([[7.300000000000001, 0, 5.8], [6.300000000000001, 0, 5.8]])), ('face3line3', c.project([[6.300000000000001, 0, 5.8], [6.300000000000001, 0, 4.8]])), ('face3line4', c.project([[6.550000000000001, 0, 5.05], [7.050000000000001, 0, 5.05]])), ('face3line5', c.project([[7.050000000000001, 0, 5.05], [7.050000000000001, 0, 5.55]])), ('face3line6', c.project([[7.050000000000001, 0, 5.55], [6.550000000000001, 0, 5.55]])), ('face3line7', c.project([[6.550000000000001, 0, 5.55], [6.550000000000001, 0, 5.05]])), ('face4line0', c.project([[8.4, 0, 4.8], [9.4, 0, 4.8]])), ('face4line1', c.project([[9.4, 0, 4.8], [9.4, 0, 5.8]])), ('face4line2', c.project([[9.4, 0, 5.8], [8.4, 0, 5.8]])), ('face4line3', c.project([[8.4, 0, 5.8], [8.4, 0, 4.8]])), ('face4line4', c.project([[8.4, 0, 5.3], [9.4, 0, 5.3]])), ('face4line5', c.project([[8.9, 0, 4.8], [8.9, 0, 5.8]])), ('face5line0', c.project([[10.5, 0, 4.8], [11.5, 0, 4.8]])), ('face5line1', c.project([[11.5, 0, 4.8], [11.5, 0, 5.8]])), ('face5line2', c.project([[11.5, 0, 5.8], [10.5, 0, 5.8]])), ('face5line3', c.project([[10.5, 0, 5.8], [10.5, 0, 4.8]])), ('face5line4', c.project([[10.5, 0, 4.8], [11.5, 0, 5.8]])), ('face5line5', c.project([[10.5, 0, 5.8], [11.5, 0, 4.8]])), ('targetline0', c.project([[5.25, 0, 2.4], [6.25, 0, 2.4]])), ('targetline1', c.project([[6.25, 0, 2.4], [6.25, 0, 3.4]])), ('targetline2', c.project([[6.25, 0, 3.4], [5.25, 0, 3.4]])), ('targetline3', c.project([[5.25, 0, 3.4], [5.25, 0, 2.4]])), ('targetline4', c.project([[5.25, 0, 2.9], [5.75, 0, 3.4]])), ('targetline5', c.project([[5.75, 0, 3.4], [6.25, 0, 2.9]])), ('targetline6', c.project([[6.25, 0, 2.9], [5.75, 0, 2.4]])), ('targetline7', c.project([[5.75, 0, 2.4], [5.25, 0, 2.9]])), ('option0line0', c.project([[0.6, 0, 0], [1.6, 0, 0]])), ('option0line1', c.project([[1.6, 0, 0], [1.6, 0, 1]])), ('option0line2', c.project([[1.6, 0, 1], [0.6, 0, 1]])), ('option0line3', c.project([[0.6, 0, 1], [0.6, 0, 0]])), ('option0line4', c.project([[0.8, 0, 0.5], [1.1, 0, 0.8]])), ('option0line5', c.project([[1.1, 0, 0.8], [1.4, 0, 0.5]])), ('option0line6', c.project([[1.4, 0, 0.5], [1.1, 0, 0.2]])), ('option0line7', c.project([[1.1, 0, 0.2], [0.8, 0, 0.5]])), ('option1line0', c.project([[2.95, 0, 0], [3.95, 0, 0]])), ('option1line1', c.project([[3.95, 0, 0], [3.95, 0, 1]])), ('option1line2', c.project([[3.95, 0, 1], [2.95, 0, 1]])), ('option1line3', c.project([[2.95, 0, 1], [2.95, 0, 0]])), ('option1line4', c.project([[2.95, 0, 0.5], [3.95, 0, 0.5]])), ('option2line0', c.project([[5.3, 0, 0], [6.3, 0, 0]])), ('option2line1', c.project([[6.3, 0, 0], [6.3, 0, 1]])), ('option2line2', c.project([[6.3, 0, 1], [5.3, 0, 1]])), ('option2line3', c.project([[5.3, 0, 1], [5.3, 0, 0]])), ('option2line4', c.project([[5.55, 0, 0.25], [6.05, 0, 0.25]])), ('option2line5', c.project([[6.05, 0, 0.25], [6.05, 0, 0.75]])), ('option2line6', c.project([[6.05, 0, 0.75], [5.55, 0, 0.75]])), ('option2line7', c.project([[5.55, 0, 0.75], [5.55, 0, 0.25]])), ('option3line0', c.project([[7.65, 0, 0], [8.65, 0, 0]])), ('option3line1', c.project([[8.65, 0, 0], [8.65, 0, 1]])), ('option3line2', c.project([[8.65, 0, 1], [7.65, 0, 1]])), ('option3line3', c.project([[7.65, 0, 1], [7.65, 0, 0]])), ('option3line4', c.project([[7.65, 0, 0.5], [8.65, 0, 0.5]])), ('option3line5', c.project([[8.15, 0, 0], [8.15, 0, 1]])), ('option4line0', c.project([[10.0, 0, 0], [11.0, 0, 0]])), ('option4line1', c.project([[11.0, 0, 0], [11.0, 0, 1]])), ('option4line2', c.project([[11.0, 0, 1], [10.0, 0, 1]])), ('option4line3', c.project([[10.0, 0, 1], [10.0, 0, 0]])), ('option4line4', c.project([[10.0, 0, 0], [11.0, 0, 1]])), ('option4line5', c.project([[10.0, 0, 1], [11.0, 0, 0]]))]:
                c.line(points, id=object_id, clip_on=False, zorder=3)
            for object_id, text, anchor in [('optionlabel0', '(A)', c.project([1.1, 0, 0])), ('optionlabel1', '(B)', c.project([3.45, 0, 0])), ('optionlabel2', '(C)', c.project([5.8, 0, 0])), ('optionlabel3', '(D)', c.project([8.15, 0, 0])), ('optionlabel4', '(E)', c.project([10.5, 0, 0]))]:
                c.text(text, anchor, id=object_id, offset_pt=[0, -18], vertex=False)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Solid84().draw(sys.argv[1] if len(sys.argv) > 1 else None))
