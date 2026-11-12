"""Frozen question Plane449; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane449:

    def __init__(self):
        self.id = 'Plane449'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:2434'
        self.question = 'Each of the sides of the five congruent rectangles is labeled with an integer, as shown above. These five rectangles are placed, without rotating or reflecting, in positions $I$ through $V$ so that the labels on coincident sides are equal.\nWhich of the rectangles is in position $I$?\nChoices:\nA:A\nB:B\nC:C\nD:D\nE:E'
        self.answer = 'E'
        self.answer_type = 'choice'
        self.choices = {'A': 'A', 'B': 'B', 'C': 'C', 'D': 'D', 'E': 'E'}
        self.query = self.question
        self.points = {'A_0': [0, 3],
         'A_1': [2, 3],
         'A_2': [2, 4.2],
         'A_3': [0, 4.2],
         'A0': [1, 3.95],
         'A1': [1.78, 3.6],
         'A2': [1, 3.25],
         'A3': [0.22, 3.6],
         'labelA': [1, 4.6],
         'B_0': [3, 3],
         'B_1': [5, 3],
         'B_2': [5, 4.2],
         'B_3': [3, 4.2],
         'B0': [4, 3.95],
         'B1': [4.78, 3.6],
         'B2': [4, 3.25],
         'B3': [3.22, 3.6],
         'labelB': [4, 4.6],
         'C_0': [6, 3],
         'C_1': [8, 3],
         'C_2': [8, 4.2],
         'C_3': [6, 4.2],
         'C0': [7, 3.95],
         'C1': [7.78, 3.6],
         'C2': [7, 3.25],
         'C3': [6.22, 3.6],
         'labelC': [7, 4.6],
         'D_0': [9, 3],
         'D_1': [11, 3],
         'D_2': [11, 4.2],
         'D_3': [9, 4.2],
         'D0': [10, 3.95],
         'D1': [10.78, 3.6],
         'D2': [10, 3.25],
         'D3': [9.22, 3.6],
         'labelD': [10, 4.6],
         'E_0': [12, 3],
         'E_1': [14, 3],
         'E_2': [14, 4.2],
         'E_3': [12, 4.2],
         'E0': [13, 3.95],
         'E1': [13.78, 3.6],
         'E2': [13, 3.25],
         'E3': [12.22, 3.6],
         'labelE': [13, 4.6],
         'slotI_0': [4, 0],
         'slotI_1': [6, 0],
         'slotI_2': [6, 1.2],
         'slotI_3': [4, 1.2],
         'slotlabelI': [5, 0.6],
         'slotII_0': [6, 0],
         'slotII_1': [8, 0],
         'slotII_2': [8, 1.2],
         'slotII_3': [6, 1.2],
         'slotlabelII': [7, 0.6],
         'slotIII_0': [8, 0],
         'slotIII_1': [10, 0],
         'slotIII_2': [10, 1.2],
         'slotIII_3': [8, 1.2],
         'slotlabelIII': [9, 0.6],
         'slotIV_0': [4, -1.2],
         'slotIV_1': [6, -1.2],
         'slotIV_2': [6, 0.0],
         'slotIV_3': [4, 0.0],
         'slotlabelIV': [5, -0.6],
         'slotV_0': [6, -1.2],
         'slotV_1': [8, -1.2],
         'slotV_2': [8, 0.0],
         'slotV_3': [6, 0.0],
         'slotlabelV': [7, -0.6]}
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane449.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-0.34696699260427977, 14.370276566052326], ylim=[-5.576095360019281, 9.141148198637325]) as c:
            for object_id, vertices, codes in [('A', [self.points['A_0'], self.points['A_1'], self.points['A_2'], self.points['A_3'], self.points['A_0']], [1, 2, 2, 2, 79]), ('B', [self.points['B_0'], self.points['B_1'], self.points['B_2'], self.points['B_3'], self.points['B_0']], [1, 2, 2, 2, 79]), ('C', [self.points['C_0'], self.points['C_1'], self.points['C_2'], self.points['C_3'], self.points['C_0']], [1, 2, 2, 2, 79]), ('D', [self.points['D_0'], self.points['D_1'], self.points['D_2'], self.points['D_3'], self.points['D_0']], [1, 2, 2, 2, 79]), ('E', [self.points['E_0'], self.points['E_1'], self.points['E_2'], self.points['E_3'], self.points['E_0']], [1, 2, 2, 2, 79]), ('slotI', [self.points['slotI_0'], self.points['slotI_1'], self.points['slotI_2'], self.points['slotI_3'], self.points['slotI_0']], [1, 2, 2, 2, 79]), ('slotII', [self.points['slotII_0'], self.points['slotII_1'], self.points['slotII_2'], self.points['slotII_3'], self.points['slotII_0']], [1, 2, 2, 2, 79]), ('slotIII', [self.points['slotIII_0'], self.points['slotIII_1'], self.points['slotIII_2'], self.points['slotIII_3'], self.points['slotIII_0']], [1, 2, 2, 2, 79]), ('slotIV', [self.points['slotIV_0'], self.points['slotIV_1'], self.points['slotIV_2'], self.points['slotIV_3'], self.points['slotIV_0']], [1, 2, 2, 2, 79]), ('slotV', [self.points['slotV_0'], self.points['slotV_1'], self.points['slotV_2'], self.points['slotV_3'], self.points['slotV_0']], [1, 2, 2, 2, 79])]:
                c.path(vertices, codes, id=object_id)
            for object_id, text, anchor in [('A0', '1', self.points['A0']), ('A1', '6', self.points['A1']), ('A2', '9', self.points['A2']), ('A3', '4', self.points['A3']), ('labelA', 'A', self.points['labelA']), ('B0', '0', self.points['B0']), ('B1', '3', self.points['B1']), ('B2', '6', self.points['B2']), ('B3', '1', self.points['B3']), ('labelB', 'B', self.points['labelB']), ('C0', '8', self.points['C0']), ('C1', '5', self.points['C1']), ('C2', '2', self.points['C2']), ('C3', '3', self.points['C3']), ('labelC', 'C', self.points['labelC']), ('D0', '5', self.points['D0']), ('D1', '4', self.points['D1']), ('D2', '8', self.points['D2']), ('D3', '7', self.points['D3']), ('labelD', 'D', self.points['labelD']), ('E0', '2', self.points['E0']), ('E1', '7', self.points['E1']), ('E2', '0', self.points['E2']), ('E3', '9', self.points['E3']), ('labelE', 'E', self.points['labelE']), ('slotlabelI', 'I', self.points['slotlabelI']), ('slotlabelII', 'II', self.points['slotlabelII']), ('slotlabelIII', 'III', self.points['slotlabelIII']), ('slotlabelIV', 'IV', self.points['slotlabelIV']), ('slotlabelV', 'V', self.points['slotlabelV'])]:
                c.text(text, anchor, id=object_id, offset_pt=[0, 0], vertex=False)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane449().draw(sys.argv[1] if len(sys.argv) > 1 else None))
