"""Frozen question Solid237; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Solid237:

    def __init__(self):
        self.id = 'Solid237'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:2760'
        self.question = 'The faces of a cube are painted in six different colors: red (R), white (W), green (G), brown (B), aqua (A), and purple (P). Three views of the cube are shown below. What is the color of the face opposite the aqua face?\nChoices:\nA:$\\text{red}$\nB:$\\text{white}$\nC:$\\text{green}$\nD:$\\text{brown}$\nE:$\\text{purple}\n$'
        self.answer = 'A'
        self.answer_type = 'choice'
        self.choices = {'A': '$\\text{red}$', 'B': '$\\text{white}$', 'C': '$\\text{green}$', 'D': '$\\text{brown}$', 'E': '$\\text{purple}\n$'}
        self.query = self.question
        self.points = {'0blockp0': [0.0, 0.0, 0.0],
         '0blockp1': [1.0, 0.0, 0.0],
         '0blockp2': [0.0, 0.0, 1.0],
         '0blockp3': [1.0, 0.0, 1.0],
         '0blockp4': [0.0, 1.0, 1.0],
         '0blockp5': [1.0, 1.0, 1.0],
         '0blockp6': [0.0, 0.0, 1.0],
         '0blockp7': [0.0, 1.0, 1.0],
         '0blockp8': [1.0, 0.0, 0.0],
         '0blockp9': [1.0, 1.0, 0.0],
         '0blockp10': [1.0, 0.0, 1.0],
         '0blockp11': [1.0, 1.0, 1.0],
         '0blockp12': [0.0, 0.0, 0.0],
         '0blockp13': [0.0, 0.0, 1.0],
         '0blockp14': [1.0, 0.0, 0.0],
         '0blockp15': [1.0, 0.0, 1.0],
         '0blockp16': [1.0, 1.0, 0.0],
         '0blockp17': [1.0, 1.0, 1.0],
         '0top': [0.5, 0.5, 1.0],
         '0front': [0.5, 0, 0.5],
         '0right': [1.0, 0.5, 0.5],
         '1blockp0': [2.15, 0.0, 0.172],
         '1blockp1': [3.15, 0.0, 0.172],
         '1blockp2': [2.15, 0.0, 1.172],
         '1blockp3': [3.15, 0.0, 1.172],
         '1blockp4': [2.15, 1.0, 1.172],
         '1blockp5': [3.15, 1.0, 1.172],
         '1blockp6': [2.15, 0.0, 1.172],
         '1blockp7': [2.15, 1.0, 1.172],
         '1blockp8': [3.15, 0.0, 0.172],
         '1blockp9': [3.15, 1.0, 0.172],
         '1blockp10': [3.15, 0.0, 1.172],
         '1blockp11': [3.15, 1.0, 1.172],
         '1blockp12': [2.15, 0.0, 0.172],
         '1blockp13': [2.15, 0.0, 1.172],
         '1blockp14': [3.15, 0.0, 0.172],
         '1blockp15': [3.15, 0.0, 1.172],
         '1blockp16': [3.15, 1.0, 0.172],
         '1blockp17': [3.15, 1.0, 1.172],
         '1top': [2.65, 0.5, 1.172],
         '1front': [2.65, 0, 0.6719999999999999],
         '1right': [3.15, 0.5, 0.6719999999999999],
         '2blockp0': [4.3, 0.0, 0.344],
         '2blockp1': [5.3, 0.0, 0.344],
         '2blockp2': [4.3, 0.0, 1.3439999999999999],
         '2blockp3': [5.3, 0.0, 1.3439999999999999],
         '2blockp4': [4.3, 1.0, 1.3439999999999999],
         '2blockp5': [5.3, 1.0, 1.3439999999999999],
         '2blockp6': [4.3, 0.0, 1.3439999999999999],
         '2blockp7': [4.3, 1.0, 1.3439999999999999],
         '2blockp8': [5.3, 0.0, 0.344],
         '2blockp9': [5.3, 1.0, 0.344],
         '2blockp10': [5.3, 0.0, 1.3439999999999999],
         '2blockp11': [5.3, 1.0, 1.3439999999999999],
         '2blockp12': [4.3, 0.0, 0.344],
         '2blockp13': [4.3, 0.0, 1.3439999999999999],
         '2blockp14': [5.3, 0.0, 0.344],
         '2blockp15': [5.3, 0.0, 1.3439999999999999],
         '2blockp16': [5.3, 1.0, 0.344],
         '2blockp17': [5.3, 1.0, 1.3439999999999999],
         '2top': [4.8, 0.5, 1.3439999999999999],
         '2front': [4.8, 0, 0.844],
         '2right': [5.3, 0.5, 0.844]}
        self.subject = 'SolidGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'SolidGeometry' / 'dataset_generator/scenes/Solid237.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('SolidGeometry', self.id, variant, output_path)
        with Canvas(SOLID, xlim=[-0.1472673569638987, 6.059197438444036], ylim=[-2.3991974384440367, 3.807267356963898], projection=[[1, 0.6, 0], [-0.08, 0.5, 1]], origin=[0, 0, 0], offset=[0, 0]) as c:
            for object_id, points in [('0line_0', c.project([self.points['0blockp0'], self.points['0blockp1']])), ('0line_1', c.project([self.points['0blockp2'], self.points['0blockp3']])), ('0line_2', c.project([self.points['0blockp4'], self.points['0blockp5']])), ('0line_3', c.project([self.points['0blockp6'], self.points['0blockp7']])), ('0line_4', c.project([self.points['0blockp8'], self.points['0blockp9']])), ('0line_5', c.project([self.points['0blockp10'], self.points['0blockp11']])), ('0line_6', c.project([self.points['0blockp12'], self.points['0blockp13']])), ('0line_7', c.project([self.points['0blockp14'], self.points['0blockp15']])), ('0line_8', c.project([self.points['0blockp16'], self.points['0blockp17']])), ('1line_0', c.project([self.points['1blockp0'], self.points['1blockp1']])), ('1line_1', c.project([self.points['1blockp2'], self.points['1blockp3']])), ('1line_2', c.project([self.points['1blockp4'], self.points['1blockp5']])), ('1line_3', c.project([self.points['1blockp6'], self.points['1blockp7']])), ('1line_4', c.project([self.points['1blockp8'], self.points['1blockp9']])), ('1line_5', c.project([self.points['1blockp10'], self.points['1blockp11']])), ('1line_6', c.project([self.points['1blockp12'], self.points['1blockp13']])), ('1line_7', c.project([self.points['1blockp14'], self.points['1blockp15']])), ('1line_8', c.project([self.points['1blockp16'], self.points['1blockp17']])), ('2line_0', c.project([self.points['2blockp0'], self.points['2blockp1']])), ('2line_1', c.project([self.points['2blockp2'], self.points['2blockp3']])), ('2line_2', c.project([self.points['2blockp4'], self.points['2blockp5']])), ('2line_3', c.project([self.points['2blockp6'], self.points['2blockp7']])), ('2line_4', c.project([self.points['2blockp8'], self.points['2blockp9']])), ('2line_5', c.project([self.points['2blockp10'], self.points['2blockp11']])), ('2line_6', c.project([self.points['2blockp12'], self.points['2blockp13']])), ('2line_7', c.project([self.points['2blockp14'], self.points['2blockp15']])), ('2line_8', c.project([self.points['2blockp16'], self.points['2blockp17']]))]:
                c.line(points, id=object_id, clip_on=False, zorder=3)
            for object_id, text, anchor in [('label_0', 'B', c.project(self.points['0top'])), ('label_1', 'R', c.project(self.points['0front'])), ('label_2', 'G', c.project(self.points['0right'])), ('label_3', 'B', c.project(self.points['1top'])), ('label_4', 'W', c.project(self.points['1front'])), ('label_5', 'R', c.project(self.points['1right'])), ('label_6', 'R', c.project(self.points['2top'])), ('label_7', 'P', c.project(self.points['2front'])), ('label_8', 'G', c.project(self.points['2right']))]:
                c.text(text, anchor, id=object_id, offset_pt=[0, 0], vertex=False)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Solid237().draw(sys.argv[1] if len(sys.argv) > 1 else None))
