"""Frozen question Solid213; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Solid213:

    def __init__(self):
        self.id = 'Solid213'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:2195'
        self.question = 'Four cubes with edge lengths $1$, $2$, $3$, and $4$ are stacked as shown. What is the length of the portion of $\\overline{XY}$ contained in the cube with edge length $3$?\nChoices:\nA:$\\frac{3\\sqrt{33}}5$\nB:$2\\sqrt{3}$\nC:$\\frac{2\\sqrt{33}}3$\nD:$4$\nE:$3\\sqrt{2} $'
        self.answer = 'A'
        self.answer_type = 'choice'
        self.choices = {'A': '$\\frac{3\\sqrt{33}}5$', 'B': '$2\\sqrt{3}$', 'C': '$\\frac{2\\sqrt{33}}3$', 'D': '$4$', 'E': '$3\\sqrt{2} $'}
        self.query = self.question
        self.points = {'blockp0': [0.0, 0.0, 0.0],
         'blockp1': [4.0, 0.0, 0.0],
         'blockp2': [0.0, 0.0, 4.0],
         'blockp3': [4.0, 0.0, 4.0],
         'blockp4': [2.5, 4.0, 4.0],
         'blockp5': [4.0, 4.0, 4.0],
         'blockp6': [4.0, 0.0, 0.0],
         'blockp7': [4.0, 4.0, 0.0],
         'blockp8': [4.0, 0.0, 4.0],
         'blockp9': [4.0, 4.0, 4.0],
         'blockp10': [0.0, 0.0, 0.0],
         'blockp11': [0.0, 0.0, 10.0],
         'blockp12': [4.0, 0.0, 0.0],
         'blockp13': [4.0, 0.0, 4.0],
         'blockp14': [4.0, 4.0, 0.0],
         'blockp15': [4.0, 4.0, 4.0],
         'blockp16': [0.0, 0.0, 7.0],
         'blockp17': [3.0, 0.0, 7.0],
         'blockp18': [1.5, 3.0, 7.0],
         'blockp19': [3.0, 3.0, 7.0],
         'blockp20': [3.0, 0.0, 4.0],
         'blockp21': [3.0, 3.0, 4.0],
         'blockp22': [3.0, 0.0, 7.0],
         'blockp23': [3.0, 3.0, 7.0],
         'blockp24': [3.0, 0.0, 4.0],
         'blockp25': [3.0, 0.0, 7.0],
         'blockp26': [3.0, 3.0, 4.0],
         'blockp27': [3.0, 3.0, 7.0],
         'blockp28': [0.0, 0.0, 9.0],
         'blockp29': [2.0, 0.0, 9.0],
         'blockp30': [0.5, 2.0, 9.0],
         'blockp31': [2.0, 2.0, 9.0],
         'blockp32': [2.0, 0.0, 7.0],
         'blockp33': [2.0, 2.0, 7.0],
         'blockp34': [2.0, 0.0, 9.0],
         'blockp35': [2.0, 2.0, 9.0],
         'blockp36': [2.0, 0.0, 7.0],
         'blockp37': [2.0, 0.0, 9.0],
         'blockp38': [2.0, 2.0, 7.0],
         'blockp39': [2.0, 2.0, 9.0],
         'blockp40': [0.0, 0.0, 10.0],
         'blockp41': [1.0, 0.0, 10.0],
         'blockp42': [0.0, 1.0, 10.0],
         'blockp43': [1.0, 1.0, 10.0],
         'blockp44': [0.0, 0.0, 10.0],
         'blockp45': [0.0, 1.0, 10.0],
         'blockp46': [1.0, 0.0, 9.0],
         'blockp47': [1.0, 1.0, 9.0],
         'blockp48': [1.0, 0.0, 10.0],
         'blockp49': [1.0, 1.0, 10.0],
         'blockp50': [1.0, 0.0, 9.0],
         'blockp51': [1.0, 0.0, 10.0],
         'blockp52': [1.0, 1.0, 9.0],
         'blockp53': [1.0, 1.0, 10.0],
         'X': [0, 0, 10],
         'Y': [4, 4, 0],
         'dim1': [1, 0, 9.5],
         'dim2': [2, 0, 8],
         'dim3': [3, 0, 5.5],
         'dim4': [4, 0, 2]}
        self.subject = 'SolidGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'SolidGeometry' / 'dataset_generator/scenes/Solid213.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('SolidGeometry', self.id, variant, output_path)
        with Canvas(SOLID, xlim=[-2.5120680441718446, 8.533335405282955], ylim=[-0.28331747519701356, 10.762085974257786], projection=[[1, 0.5, 0], [0, 0.5, 1]], origin=[0, 0, 0], offset=[0, 0]) as c:
            for object_id, points in [('line_0', c.project([self.points['blockp0'], self.points['blockp1']])), ('line_1', c.project([self.points['blockp2'], self.points['blockp3']])), ('line_2', c.project([self.points['blockp4'], self.points['blockp5']])), ('line_3', c.project([self.points['blockp6'], self.points['blockp7']])), ('line_4', c.project([self.points['blockp8'], self.points['blockp9']])), ('line_5', c.project([self.points['blockp10'], self.points['blockp11']])), ('line_6', c.project([self.points['blockp12'], self.points['blockp13']])), ('line_7', c.project([self.points['blockp14'], self.points['blockp15']])), ('line_8', c.project([self.points['blockp16'], self.points['blockp17']])), ('line_9', c.project([self.points['blockp18'], self.points['blockp19']])), ('line_10', c.project([self.points['blockp20'], self.points['blockp21']])), ('line_11', c.project([self.points['blockp22'], self.points['blockp23']])), ('line_12', c.project([self.points['blockp24'], self.points['blockp25']])), ('line_13', c.project([self.points['blockp26'], self.points['blockp27']])), ('line_14', c.project([self.points['blockp28'], self.points['blockp29']])), ('line_15', c.project([self.points['blockp30'], self.points['blockp31']])), ('line_16', c.project([self.points['blockp32'], self.points['blockp33']])), ('line_17', c.project([self.points['blockp34'], self.points['blockp35']])), ('line_18', c.project([self.points['blockp36'], self.points['blockp37']])), ('line_19', c.project([self.points['blockp38'], self.points['blockp39']])), ('line_20', c.project([self.points['blockp40'], self.points['blockp41']])), ('line_21', c.project([self.points['blockp42'], self.points['blockp43']])), ('line_22', c.project([self.points['blockp44'], self.points['blockp45']])), ('line_23', c.project([self.points['blockp46'], self.points['blockp47']])), ('line_24', c.project([self.points['blockp48'], self.points['blockp49']])), ('line_25', c.project([self.points['blockp50'], self.points['blockp51']])), ('line_26', c.project([self.points['blockp52'], self.points['blockp53']]))]:
                c.line(points, id=object_id, clip_on=False, zorder=3)
            c.text('X', c.project(self.points['X']), offset_pt=[-18, 0], vertex=True, id='label_0')
            c.text('Y', c.project(self.points['Y']), offset_pt=[18, 0], vertex=True, id='label_1')
            for object_id, text, anchor in [('label_2', '1', c.project(self.points['dim1'])), ('label_3', '2', c.project(self.points['dim2'])), ('label_4', '3', c.project(self.points['dim3'])), ('label_5', '4', c.project(self.points['dim4']))]:
                c.text(text, anchor, id=object_id, offset_pt=[-12, 0], vertex=False)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Solid213().draw(sys.argv[1] if len(sys.argv) > 1 else None))
