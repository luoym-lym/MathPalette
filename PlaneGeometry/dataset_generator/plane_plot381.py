"""Frozen question Plane381; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane381:

    def __init__(self):
        self.id = 'Plane381'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:1509'
        self.question = 'The large shape of squares is to be divided into smaller pieces using only copies of the T-piece and the F-piece shown on the right. Pieces may be turned over or around. What is the smallest possible number of T-pieces?'
        self.answer = '2'
        self.answer_type = 'number'
        self.query = self.question
        self.points = {'board0_0': [0, 1],
         'board0_1': [1, 1],
         'board0_2': [1, 2],
         'board0_3': [0, 2],
         'board1_0': [2, 4],
         'board1_1': [3, 4],
         'board1_2': [3, 5],
         'board1_3': [2, 5],
         'board2_0': [1, 2],
         'board2_1': [2, 2],
         'board2_2': [2, 3],
         'board2_3': [1, 3],
         'board3_0': [0, 4],
         'board3_1': [1, 4],
         'board3_2': [1, 5],
         'board3_3': [0, 5],
         'board4_0': [3, 4],
         'board4_1': [4, 4],
         'board4_2': [4, 5],
         'board4_3': [3, 5],
         'board5_0': [2, 1],
         'board5_1': [3, 1],
         'board5_2': [3, 2],
         'board5_3': [2, 2],
         'board6_0': [4, 0],
         'board6_1': [5, 0],
         'board6_2': [5, 1],
         'board6_3': [4, 1],
         'board7_0': [3, 1],
         'board7_1': [4, 1],
         'board7_2': [4, 2],
         'board7_3': [3, 2],
         'board8_0': [0, 2],
         'board8_1': [1, 2],
         'board8_2': [1, 3],
         'board8_3': [0, 3],
         'board9_0': [2, 2],
         'board9_1': [3, 2],
         'board9_2': [3, 3],
         'board9_3': [2, 3],
         'board10_0': [1, 0],
         'board10_1': [2, 0],
         'board10_2': [2, 1],
         'board10_3': [1, 1],
         'board11_0': [3, 2],
         'board11_1': [4, 2],
         'board11_2': [4, 3],
         'board11_3': [3, 3],
         'board12_0': [1, 3],
         'board12_1': [2, 3],
         'board12_2': [2, 4],
         'board12_3': [1, 4],
         'board13_0': [4, 1],
         'board13_1': [5, 1],
         'board13_2': [5, 2],
         'board13_3': [4, 2],
         'board14_0': [0, 0],
         'board14_1': [1, 0],
         'board14_2': [1, 1],
         'board14_3': [0, 1],
         'board15_0': [1, 1],
         'board15_1': [2, 1],
         'board15_2': [2, 2],
         'board15_3': [1, 2],
         'board16_0': [0, 3],
         'board16_1': [1, 3],
         'board16_2': [1, 4],
         'board16_3': [0, 4],
         'board17_0': [2, 0],
         'board17_1': [3, 0],
         'board17_2': [3, 1],
         'board17_3': [2, 1],
         'board18_0': [1, 4],
         'board18_1': [2, 4],
         'board18_2': [2, 5],
         'board18_3': [1, 5],
         'board19_0': [3, 0],
         'board19_1': [4, 0],
         'board19_2': [4, 1],
         'board19_3': [3, 1],
         'board20_0': [2, 3],
         'board20_1': [3, 3],
         'board20_2': [3, 4],
         'board20_3': [2, 4],
         'board21_0': [3, 3],
         'board21_1': [4, 3],
         'board21_2': [4, 4],
         'board21_3': [3, 4],
         'T0_0': [7, 4],
         'T0_1': [8, 4],
         'T0_2': [8, 5],
         'T0_3': [7, 5],
         'T1_0': [8, 4],
         'T1_1': [9, 4],
         'T1_2': [9, 5],
         'T1_3': [8, 5],
         'T2_0': [7, 3],
         'T2_1': [8, 3],
         'T2_2': [8, 4],
         'T2_3': [7, 4],
         'F0_0': [7, 1],
         'F0_1': [8, 1],
         'F0_2': [8, 2],
         'F0_3': [7, 2],
         'F1_0': [8, 1],
         'F1_1': [9, 1],
         'F1_2': [9, 2],
         'F1_3': [8, 2],
         'F2_0': [9, 1],
         'F2_1': [10, 1],
         'F2_2': [10, 2],
         'F2_3': [9, 2],
         'F3_0': [7, 0],
         'F3_1': [8, 0],
         'F3_2': [8, 1],
         'F3_3': [7, 1],
         'Tlabel': [10.3, 4],
         'Flabel': [11.3, 1]}
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane381.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-0.2813101156616593, 11.656511625234957], ylim=[-3.4783111887353453, 8.459510552161271]) as c:
            for object_id, vertices, codes in [('board0', [self.points['board0_0'], self.points['board0_1'], self.points['board0_2'], self.points['board0_3'], self.points['board0_0']], [1, 2, 2, 2, 79]), ('board1', [self.points['board1_0'], self.points['board1_1'], self.points['board1_2'], self.points['board1_3'], self.points['board1_0']], [1, 2, 2, 2, 79]), ('board2', [self.points['board2_0'], self.points['board2_1'], self.points['board2_2'], self.points['board2_3'], self.points['board2_0']], [1, 2, 2, 2, 79]), ('board3', [self.points['board3_0'], self.points['board3_1'], self.points['board3_2'], self.points['board3_3'], self.points['board3_0']], [1, 2, 2, 2, 79]), ('board4', [self.points['board4_0'], self.points['board4_1'], self.points['board4_2'], self.points['board4_3'], self.points['board4_0']], [1, 2, 2, 2, 79]), ('board5', [self.points['board5_0'], self.points['board5_1'], self.points['board5_2'], self.points['board5_3'], self.points['board5_0']], [1, 2, 2, 2, 79]), ('board6', [self.points['board6_0'], self.points['board6_1'], self.points['board6_2'], self.points['board6_3'], self.points['board6_0']], [1, 2, 2, 2, 79]), ('board7', [self.points['board7_0'], self.points['board7_1'], self.points['board7_2'], self.points['board7_3'], self.points['board7_0']], [1, 2, 2, 2, 79]), ('board8', [self.points['board8_0'], self.points['board8_1'], self.points['board8_2'], self.points['board8_3'], self.points['board8_0']], [1, 2, 2, 2, 79]), ('board9', [self.points['board9_0'], self.points['board9_1'], self.points['board9_2'], self.points['board9_3'], self.points['board9_0']], [1, 2, 2, 2, 79]), ('board10', [self.points['board10_0'], self.points['board10_1'], self.points['board10_2'], self.points['board10_3'], self.points['board10_0']], [1, 2, 2, 2, 79]), ('board11', [self.points['board11_0'], self.points['board11_1'], self.points['board11_2'], self.points['board11_3'], self.points['board11_0']], [1, 2, 2, 2, 79]), ('board12', [self.points['board12_0'], self.points['board12_1'], self.points['board12_2'], self.points['board12_3'], self.points['board12_0']], [1, 2, 2, 2, 79]), ('board13', [self.points['board13_0'], self.points['board13_1'], self.points['board13_2'], self.points['board13_3'], self.points['board13_0']], [1, 2, 2, 2, 79]), ('board14', [self.points['board14_0'], self.points['board14_1'], self.points['board14_2'], self.points['board14_3'], self.points['board14_0']], [1, 2, 2, 2, 79]), ('board15', [self.points['board15_0'], self.points['board15_1'], self.points['board15_2'], self.points['board15_3'], self.points['board15_0']], [1, 2, 2, 2, 79]), ('board16', [self.points['board16_0'], self.points['board16_1'], self.points['board16_2'], self.points['board16_3'], self.points['board16_0']], [1, 2, 2, 2, 79]), ('board17', [self.points['board17_0'], self.points['board17_1'], self.points['board17_2'], self.points['board17_3'], self.points['board17_0']], [1, 2, 2, 2, 79]), ('board18', [self.points['board18_0'], self.points['board18_1'], self.points['board18_2'], self.points['board18_3'], self.points['board18_0']], [1, 2, 2, 2, 79]), ('board19', [self.points['board19_0'], self.points['board19_1'], self.points['board19_2'], self.points['board19_3'], self.points['board19_0']], [1, 2, 2, 2, 79]), ('board20', [self.points['board20_0'], self.points['board20_1'], self.points['board20_2'], self.points['board20_3'], self.points['board20_0']], [1, 2, 2, 2, 79]), ('board21', [self.points['board21_0'], self.points['board21_1'], self.points['board21_2'], self.points['board21_3'], self.points['board21_0']], [1, 2, 2, 2, 79]), ('T0', [self.points['T0_0'], self.points['T0_1'], self.points['T0_2'], self.points['T0_3'], self.points['T0_0']], [1, 2, 2, 2, 79]), ('T1', [self.points['T1_0'], self.points['T1_1'], self.points['T1_2'], self.points['T1_3'], self.points['T1_0']], [1, 2, 2, 2, 79]), ('T2', [self.points['T2_0'], self.points['T2_1'], self.points['T2_2'], self.points['T2_3'], self.points['T2_0']], [1, 2, 2, 2, 79]), ('F0', [self.points['F0_0'], self.points['F0_1'], self.points['F0_2'], self.points['F0_3'], self.points['F0_0']], [1, 2, 2, 2, 79]), ('F1', [self.points['F1_0'], self.points['F1_1'], self.points['F1_2'], self.points['F1_3'], self.points['F1_0']], [1, 2, 2, 2, 79]), ('F2', [self.points['F2_0'], self.points['F2_1'], self.points['F2_2'], self.points['F2_3'], self.points['F2_0']], [1, 2, 2, 2, 79]), ('F3', [self.points['F3_0'], self.points['F3_1'], self.points['F3_2'], self.points['F3_3'], self.points['F3_0']], [1, 2, 2, 2, 79])]:
                c.path(vertices, codes, id=object_id)
            c.text('T', self.points['Tlabel'], offset_pt=[0, 0], vertex=False, id='Tname')
            c.text('F', self.points['Flabel'], offset_pt=[0, 0], vertex=False, id='Fname')
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane381().draw(sys.argv[1] if len(sys.argv) > 1 else None))
