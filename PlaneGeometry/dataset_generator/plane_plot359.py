"""Frozen question Plane359; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane359:

    def __init__(self):
        self.id = 'Plane359'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:1243'
        self.question = 'A $4\\times 6$ grid should be cut along the black lines into several identical shapes. No piece is to be left over. Into which of the following shapes is it not possible to cut this grid in this way?\nChoices:\nA:A\nB:B\nC:C\nD:D\nE:E'
        self.answer = 'D'
        self.answer_type = 'choice'
        self.choices = {'A': 'A', 'B': 'B', 'C': 'C', 'D': 'D', 'E': 'E'}
        self.query = self.question
        self.points = {'board0_0': [7, 6],
         'board0_1': [8, 6],
         'board0_2': [8, 7],
         'board0_3': [7, 7],
         'board1_0': [7, 7],
         'board1_1': [8, 7],
         'board1_2': [8, 8],
         'board1_3': [7, 8],
         'board2_0': [7, 8],
         'board2_1': [8, 8],
         'board2_2': [8, 9],
         'board2_3': [7, 9],
         'board3_0': [7, 9],
         'board3_1': [8, 9],
         'board3_2': [8, 10],
         'board3_3': [7, 10],
         'board4_0': [8, 6],
         'board4_1': [9, 6],
         'board4_2': [9, 7],
         'board4_3': [8, 7],
         'board5_0': [8, 7],
         'board5_1': [9, 7],
         'board5_2': [9, 8],
         'board5_3': [8, 8],
         'board6_0': [8, 8],
         'board6_1': [9, 8],
         'board6_2': [9, 9],
         'board6_3': [8, 9],
         'board7_0': [8, 9],
         'board7_1': [9, 9],
         'board7_2': [9, 10],
         'board7_3': [8, 10],
         'board8_0': [9, 6],
         'board8_1': [10, 6],
         'board8_2': [10, 7],
         'board8_3': [9, 7],
         'board9_0': [9, 7],
         'board9_1': [10, 7],
         'board9_2': [10, 8],
         'board9_3': [9, 8],
         'board10_0': [9, 8],
         'board10_1': [10, 8],
         'board10_2': [10, 9],
         'board10_3': [9, 9],
         'board11_0': [9, 9],
         'board11_1': [10, 9],
         'board11_2': [10, 10],
         'board11_3': [9, 10],
         'board12_0': [10, 6],
         'board12_1': [11, 6],
         'board12_2': [11, 7],
         'board12_3': [10, 7],
         'board13_0': [10, 7],
         'board13_1': [11, 7],
         'board13_2': [11, 8],
         'board13_3': [10, 8],
         'board14_0': [10, 8],
         'board14_1': [11, 8],
         'board14_2': [11, 9],
         'board14_3': [10, 9],
         'board15_0': [10, 9],
         'board15_1': [11, 9],
         'board15_2': [11, 10],
         'board15_3': [10, 10],
         'board16_0': [11, 6],
         'board16_1': [12, 6],
         'board16_2': [12, 7],
         'board16_3': [11, 7],
         'board17_0': [11, 7],
         'board17_1': [12, 7],
         'board17_2': [12, 8],
         'board17_3': [11, 8],
         'board18_0': [11, 8],
         'board18_1': [12, 8],
         'board18_2': [12, 9],
         'board18_3': [11, 9],
         'board19_0': [11, 9],
         'board19_1': [12, 9],
         'board19_2': [12, 10],
         'board19_3': [11, 10],
         'board20_0': [12, 6],
         'board20_1': [13, 6],
         'board20_2': [13, 7],
         'board20_3': [12, 7],
         'board21_0': [12, 7],
         'board21_1': [13, 7],
         'board21_2': [13, 8],
         'board21_3': [12, 8],
         'board22_0': [12, 8],
         'board22_1': [13, 8],
         'board22_2': [13, 9],
         'board22_3': [12, 9],
         'board23_0': [12, 9],
         'board23_1': [13, 9],
         'board23_2': [13, 10],
         'board23_3': [12, 10],
         'A0_0': [0, 0],
         'A0_1': [1, 0],
         'A0_2': [1, 1],
         'A0_3': [0, 1],
         'A1_0': [1, 0],
         'A1_1': [2, 0],
         'A1_2': [2, 1],
         'A1_3': [1, 1],
         'A2_0': [0, 1],
         'A2_1': [1, 1],
         'A2_2': [1, 2],
         'A2_3': [0, 2],
         'A3_0': [1, 1],
         'A3_1': [2, 1],
         'A3_2': [2, 2],
         'A3_3': [1, 2],
         'label0': [1, -0.8],
         'B0_0': [5, 0],
         'B0_1': [6, 0],
         'B0_2': [6, 1],
         'B0_3': [5, 1],
         'B1_0': [6, 0],
         'B1_1': [7, 0],
         'B1_2': [7, 1],
         'B1_3': [6, 1],
         'B2_0': [7, 0],
         'B2_1': [8, 0],
         'B2_2': [8, 1],
         'B2_3': [7, 1],
         'B3_0': [5, 1],
         'B3_1': [6, 1],
         'B3_2': [6, 2],
         'B3_3': [5, 2],
         'label1': [6, -0.8],
         'C0_0': [10, 0],
         'C0_1': [11, 0],
         'C0_2': [11, 1],
         'C0_3': [10, 1],
         'C1_0': [11, 0],
         'C1_1': [12, 0],
         'C1_2': [12, 1],
         'C1_3': [11, 1],
         'C2_0': [10, 1],
         'C2_1': [11, 1],
         'C2_2': [11, 2],
         'C2_3': [10, 2],
         'label2': [11, -0.8],
         'D0_0': [15, 0],
         'D0_1': [16, 0],
         'D0_2': [16, 1],
         'D0_3': [15, 1],
         'D1_0': [16, 0],
         'D1_1': [17, 0],
         'D1_2': [17, 1],
         'D1_3': [16, 1],
         'D2_0': [17, 0],
         'D2_1': [18, 0],
         'D2_2': [18, 1],
         'D2_3': [17, 1],
         'D3_0': [16, 1],
         'D3_1': [17, 1],
         'D3_2': [17, 2],
         'D3_3': [16, 2],
         'D4_0': [17, 1],
         'D4_1': [18, 1],
         'D4_2': [18, 2],
         'D4_3': [17, 2],
         'label3': [16, -0.8],
         'E0_0': [20, 0],
         'E0_1': [21, 0],
         'E0_2': [21, 1],
         'E0_3': [20, 1],
         'E1_0': [21, 0],
         'E1_1': [22, 0],
         'E1_2': [22, 1],
         'E1_3': [21, 1],
         'E2_0': [22, 0],
         'E2_1': [23, 0],
         'E2_2': [23, 1],
         'E2_3': [22, 1],
         'E3_0': [23, 0],
         'E3_1': [24, 0],
         'E3_2': [24, 1],
         'E3_3': [23, 1],
         'label4': [21, -0.8]}
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane359.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-0.5948005587501974, 24.634759827518273], ylim=[-8.156214211238911, 17.07334617502956]) as c:
            for object_id, vertices, codes in [('cellboard0', [self.points['board0_0'], self.points['board0_1'], self.points['board0_2'], self.points['board0_3'], self.points['board0_0']], [1, 2, 2, 2, 79]), ('cellboard1', [self.points['board1_0'], self.points['board1_1'], self.points['board1_2'], self.points['board1_3'], self.points['board1_0']], [1, 2, 2, 2, 79]), ('cellboard2', [self.points['board2_0'], self.points['board2_1'], self.points['board2_2'], self.points['board2_3'], self.points['board2_0']], [1, 2, 2, 2, 79]), ('cellboard3', [self.points['board3_0'], self.points['board3_1'], self.points['board3_2'], self.points['board3_3'], self.points['board3_0']], [1, 2, 2, 2, 79]), ('cellboard4', [self.points['board4_0'], self.points['board4_1'], self.points['board4_2'], self.points['board4_3'], self.points['board4_0']], [1, 2, 2, 2, 79]), ('cellboard5', [self.points['board5_0'], self.points['board5_1'], self.points['board5_2'], self.points['board5_3'], self.points['board5_0']], [1, 2, 2, 2, 79]), ('cellboard6', [self.points['board6_0'], self.points['board6_1'], self.points['board6_2'], self.points['board6_3'], self.points['board6_0']], [1, 2, 2, 2, 79]), ('cellboard7', [self.points['board7_0'], self.points['board7_1'], self.points['board7_2'], self.points['board7_3'], self.points['board7_0']], [1, 2, 2, 2, 79]), ('cellboard8', [self.points['board8_0'], self.points['board8_1'], self.points['board8_2'], self.points['board8_3'], self.points['board8_0']], [1, 2, 2, 2, 79]), ('cellboard9', [self.points['board9_0'], self.points['board9_1'], self.points['board9_2'], self.points['board9_3'], self.points['board9_0']], [1, 2, 2, 2, 79]), ('cellboard10', [self.points['board10_0'], self.points['board10_1'], self.points['board10_2'], self.points['board10_3'], self.points['board10_0']], [1, 2, 2, 2, 79]), ('cellboard11', [self.points['board11_0'], self.points['board11_1'], self.points['board11_2'], self.points['board11_3'], self.points['board11_0']], [1, 2, 2, 2, 79]), ('cellboard12', [self.points['board12_0'], self.points['board12_1'], self.points['board12_2'], self.points['board12_3'], self.points['board12_0']], [1, 2, 2, 2, 79]), ('cellboard13', [self.points['board13_0'], self.points['board13_1'], self.points['board13_2'], self.points['board13_3'], self.points['board13_0']], [1, 2, 2, 2, 79]), ('cellboard14', [self.points['board14_0'], self.points['board14_1'], self.points['board14_2'], self.points['board14_3'], self.points['board14_0']], [1, 2, 2, 2, 79]), ('cellboard15', [self.points['board15_0'], self.points['board15_1'], self.points['board15_2'], self.points['board15_3'], self.points['board15_0']], [1, 2, 2, 2, 79]), ('cellboard16', [self.points['board16_0'], self.points['board16_1'], self.points['board16_2'], self.points['board16_3'], self.points['board16_0']], [1, 2, 2, 2, 79]), ('cellboard17', [self.points['board17_0'], self.points['board17_1'], self.points['board17_2'], self.points['board17_3'], self.points['board17_0']], [1, 2, 2, 2, 79]), ('cellboard18', [self.points['board18_0'], self.points['board18_1'], self.points['board18_2'], self.points['board18_3'], self.points['board18_0']], [1, 2, 2, 2, 79]), ('cellboard19', [self.points['board19_0'], self.points['board19_1'], self.points['board19_2'], self.points['board19_3'], self.points['board19_0']], [1, 2, 2, 2, 79]), ('cellboard20', [self.points['board20_0'], self.points['board20_1'], self.points['board20_2'], self.points['board20_3'], self.points['board20_0']], [1, 2, 2, 2, 79]), ('cellboard21', [self.points['board21_0'], self.points['board21_1'], self.points['board21_2'], self.points['board21_3'], self.points['board21_0']], [1, 2, 2, 2, 79]), ('cellboard22', [self.points['board22_0'], self.points['board22_1'], self.points['board22_2'], self.points['board22_3'], self.points['board22_0']], [1, 2, 2, 2, 79]), ('cellboard23', [self.points['board23_0'], self.points['board23_1'], self.points['board23_2'], self.points['board23_3'], self.points['board23_0']], [1, 2, 2, 2, 79]), ('cellA0', [self.points['A0_0'], self.points['A0_1'], self.points['A0_2'], self.points['A0_3'], self.points['A0_0']], [1, 2, 2, 2, 79]), ('cellA1', [self.points['A1_0'], self.points['A1_1'], self.points['A1_2'], self.points['A1_3'], self.points['A1_0']], [1, 2, 2, 2, 79]), ('cellA2', [self.points['A2_0'], self.points['A2_1'], self.points['A2_2'], self.points['A2_3'], self.points['A2_0']], [1, 2, 2, 2, 79]), ('cellA3', [self.points['A3_0'], self.points['A3_1'], self.points['A3_2'], self.points['A3_3'], self.points['A3_0']], [1, 2, 2, 2, 79]), ('cellB0', [self.points['B0_0'], self.points['B0_1'], self.points['B0_2'], self.points['B0_3'], self.points['B0_0']], [1, 2, 2, 2, 79]), ('cellB1', [self.points['B1_0'], self.points['B1_1'], self.points['B1_2'], self.points['B1_3'], self.points['B1_0']], [1, 2, 2, 2, 79]), ('cellB2', [self.points['B2_0'], self.points['B2_1'], self.points['B2_2'], self.points['B2_3'], self.points['B2_0']], [1, 2, 2, 2, 79]), ('cellB3', [self.points['B3_0'], self.points['B3_1'], self.points['B3_2'], self.points['B3_3'], self.points['B3_0']], [1, 2, 2, 2, 79]), ('cellC0', [self.points['C0_0'], self.points['C0_1'], self.points['C0_2'], self.points['C0_3'], self.points['C0_0']], [1, 2, 2, 2, 79]), ('cellC1', [self.points['C1_0'], self.points['C1_1'], self.points['C1_2'], self.points['C1_3'], self.points['C1_0']], [1, 2, 2, 2, 79]), ('cellC2', [self.points['C2_0'], self.points['C2_1'], self.points['C2_2'], self.points['C2_3'], self.points['C2_0']], [1, 2, 2, 2, 79]), ('cellD0', [self.points['D0_0'], self.points['D0_1'], self.points['D0_2'], self.points['D0_3'], self.points['D0_0']], [1, 2, 2, 2, 79]), ('cellD1', [self.points['D1_0'], self.points['D1_1'], self.points['D1_2'], self.points['D1_3'], self.points['D1_0']], [1, 2, 2, 2, 79]), ('cellD2', [self.points['D2_0'], self.points['D2_1'], self.points['D2_2'], self.points['D2_3'], self.points['D2_0']], [1, 2, 2, 2, 79]), ('cellD3', [self.points['D3_0'], self.points['D3_1'], self.points['D3_2'], self.points['D3_3'], self.points['D3_0']], [1, 2, 2, 2, 79]), ('cellD4', [self.points['D4_0'], self.points['D4_1'], self.points['D4_2'], self.points['D4_3'], self.points['D4_0']], [1, 2, 2, 2, 79]), ('cellE0', [self.points['E0_0'], self.points['E0_1'], self.points['E0_2'], self.points['E0_3'], self.points['E0_0']], [1, 2, 2, 2, 79]), ('cellE1', [self.points['E1_0'], self.points['E1_1'], self.points['E1_2'], self.points['E1_3'], self.points['E1_0']], [1, 2, 2, 2, 79]), ('cellE2', [self.points['E2_0'], self.points['E2_1'], self.points['E2_2'], self.points['E2_3'], self.points['E2_0']], [1, 2, 2, 2, 79]), ('cellE3', [self.points['E3_0'], self.points['E3_1'], self.points['E3_2'], self.points['E3_3'], self.points['E3_0']], [1, 2, 2, 2, 79])]:
                c.path(vertices, codes, id=object_id)
            for object_id, text, anchor in [('label0', '(A)', self.points['label0']), ('label1', '(B)', self.points['label1']), ('label2', '(C)', self.points['label2']), ('label3', '(D)', self.points['label3']), ('label4', '(E)', self.points['label4'])]:
                c.text(text, anchor, id=object_id, offset_pt=[0, 0], vertex=False)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane359().draw(sys.argv[1] if len(sys.argv) > 1 else None))
