"""Frozen question Plane375; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane375:

    def __init__(self):
        self.id = 'Plane375'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:1431'
        self.question = 'A $3 \\times 2$ rectangle can be covered in two ways by two of the L-shaped figures as shown:\nIn how many ways can the diagram below be covered by these L-shaped figures?'
        self.answer = '2'
        self.answer_type = 'number'
        self.query = self.question
        self.points = {'piece0_0': [0, 7],
         'piece0_1': [1, 7],
         'piece0_2': [1, 8],
         'piece0_3': [0, 8],
         'piece1_0': [0, 8],
         'piece1_1': [1, 8],
         'piece1_2': [1, 9],
         'piece1_3': [0, 9],
         'piece2_0': [1, 7],
         'piece2_1': [2, 7],
         'piece2_2': [2, 8],
         'piece2_3': [1, 8],
         'pieceL0': [0.5, 8.5],
         'pieceL1': [0.5, 7.5],
         'pieceL2': [1.5, 7.5],
         'demo00_0': [4.5, 7],
         'demo00_1': [5.5, 7],
         'demo00_2': [5.5, 8],
         'demo00_3': [4.5, 8],
         'demo01_0': [4.5, 8],
         'demo01_1': [5.5, 8],
         'demo01_2': [5.5, 9],
         'demo01_3': [4.5, 9],
         'demo02_0': [5.5, 7],
         'demo02_1': [6.5, 7],
         'demo02_2': [6.5, 8],
         'demo02_3': [5.5, 8],
         'demo03_0': [5.5, 8],
         'demo03_1': [6.5, 8],
         'demo03_2': [6.5, 9],
         'demo03_3': [5.5, 9],
         'demo04_0': [6.5, 7],
         'demo04_1': [7.5, 7],
         'demo04_2': [7.5, 8],
         'demo04_3': [6.5, 8],
         'demo05_0': [6.5, 8],
         'demo05_1': [7.5, 8],
         'demo05_2': [7.5, 9],
         'demo05_3': [6.5, 9],
         'demol00': [5.0, 7.5],
         'demol01': [5.0, 8.5],
         'demol02': [6.0, 8.5],
         'demol10': [6.0, 7.5],
         'demol11': [7.0, 7.5],
         'demol12': [7.0, 8.5],
         'demo10_0': [9, 7],
         'demo10_1': [10, 7],
         'demo10_2': [10, 8],
         'demo10_3': [9, 8],
         'demo11_0': [9, 8],
         'demo11_1': [10, 8],
         'demo11_2': [10, 9],
         'demo11_3': [9, 9],
         'demo12_0': [10, 7],
         'demo12_1': [11, 7],
         'demo12_2': [11, 8],
         'demo12_3': [10, 8],
         'demo13_0': [10, 8],
         'demo13_1': [11, 8],
         'demo13_2': [11, 9],
         'demo13_3': [10, 9],
         'demo14_0': [11, 7],
         'demo14_1': [12, 7],
         'demo14_2': [12, 8],
         'demo14_3': [11, 8],
         'demo15_0': [11, 8],
         'demo15_1': [12, 8],
         'demo15_2': [12, 9],
         'demo15_3': [11, 9],
         'demol20': [9.5, 8.5],
         'demol21': [9.5, 7.5],
         'demol22': [10.5, 7.5],
         'demol30': [10.5, 8.5],
         'demol31': [11.5, 8.5],
         'demol32': [11.5, 7.5],
         'target0_0': [4, 1],
         'target0_1': [5, 1],
         'target0_2': [5, 2],
         'target0_3': [4, 2],
         'target1_0': [5, 2],
         'target1_1': [6, 2],
         'target1_2': [6, 3],
         'target1_3': [5, 3],
         'target2_0': [6, 1],
         'target2_1': [7, 1],
         'target2_2': [7, 2],
         'target2_3': [6, 2],
         'target3_0': [7, 1],
         'target3_1': [8, 1],
         'target3_2': [8, 2],
         'target3_3': [7, 2],
         'target4_0': [5, 1],
         'target4_1': [6, 1],
         'target4_2': [6, 2],
         'target4_3': [5, 2],
         'target5_0': [6, 0],
         'target5_1': [7, 0],
         'target5_2': [7, 1],
         'target5_3': [6, 1],
         'target6_0': [7, 0],
         'target6_1': [8, 0],
         'target6_2': [8, 1],
         'target6_3': [7, 1],
         'target7_0': [6, 3],
         'target7_1': [7, 3],
         'target7_2': [7, 4],
         'target7_3': [6, 4],
         'target8_0': [4, 2],
         'target8_1': [5, 2],
         'target8_2': [5, 3],
         'target8_3': [4, 3],
         'target9_0': [7, 3],
         'target9_1': [8, 3],
         'target9_2': [8, 4],
         'target9_3': [7, 4],
         'target10_0': [6, 2],
         'target10_1': [7, 2],
         'target10_2': [7, 3],
         'target10_3': [6, 3],
         'target11_0': [7, 2],
         'target11_1': [8, 2],
         'target11_2': [8, 3],
         'target11_3': [7, 3]}
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane375.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-0.2974002793750987, 12.317379913759137], ylim=[-1.817372735456007, 10.79740745767823]) as c:
            for object_id, vertices, codes in [('cellpiece0', [self.points['piece0_0'], self.points['piece0_1'], self.points['piece0_2'], self.points['piece0_3'], self.points['piece0_0']], [1, 2, 2, 2, 79]), ('cellpiece1', [self.points['piece1_0'], self.points['piece1_1'], self.points['piece1_2'], self.points['piece1_3'], self.points['piece1_0']], [1, 2, 2, 2, 79]), ('cellpiece2', [self.points['piece2_0'], self.points['piece2_1'], self.points['piece2_2'], self.points['piece2_3'], self.points['piece2_0']], [1, 2, 2, 2, 79])]:
                c.path(vertices, codes, id=object_id)
            c.line([self.points['pieceL0'], self.points['pieceL1']], id='pieceL0')
            c.line([self.points['pieceL1'], self.points['pieceL2']], id='pieceL1')
            for object_id, vertices, codes in [('celldemo00', [self.points['demo00_0'], self.points['demo00_1'], self.points['demo00_2'], self.points['demo00_3'], self.points['demo00_0']], [1, 2, 2, 2, 79]), ('celldemo01', [self.points['demo01_0'], self.points['demo01_1'], self.points['demo01_2'], self.points['demo01_3'], self.points['demo01_0']], [1, 2, 2, 2, 79]), ('celldemo02', [self.points['demo02_0'], self.points['demo02_1'], self.points['demo02_2'], self.points['demo02_3'], self.points['demo02_0']], [1, 2, 2, 2, 79]), ('celldemo03', [self.points['demo03_0'], self.points['demo03_1'], self.points['demo03_2'], self.points['demo03_3'], self.points['demo03_0']], [1, 2, 2, 2, 79]), ('celldemo04', [self.points['demo04_0'], self.points['demo04_1'], self.points['demo04_2'], self.points['demo04_3'], self.points['demo04_0']], [1, 2, 2, 2, 79]), ('celldemo05', [self.points['demo05_0'], self.points['demo05_1'], self.points['demo05_2'], self.points['demo05_3'], self.points['demo05_0']], [1, 2, 2, 2, 79])]:
                c.path(vertices, codes, id=object_id)
            for object_id, points in [('demol00', [self.points['demol00'], self.points['demol01']]), ('demol01', [self.points['demol01'], self.points['demol02']]), ('demol10', [self.points['demol10'], self.points['demol11']]), ('demol11', [self.points['demol11'], self.points['demol12']])]:
                c.line(points, id=object_id)
            for object_id, vertices, codes in [('celldemo10', [self.points['demo10_0'], self.points['demo10_1'], self.points['demo10_2'], self.points['demo10_3'], self.points['demo10_0']], [1, 2, 2, 2, 79]), ('celldemo11', [self.points['demo11_0'], self.points['demo11_1'], self.points['demo11_2'], self.points['demo11_3'], self.points['demo11_0']], [1, 2, 2, 2, 79]), ('celldemo12', [self.points['demo12_0'], self.points['demo12_1'], self.points['demo12_2'], self.points['demo12_3'], self.points['demo12_0']], [1, 2, 2, 2, 79]), ('celldemo13', [self.points['demo13_0'], self.points['demo13_1'], self.points['demo13_2'], self.points['demo13_3'], self.points['demo13_0']], [1, 2, 2, 2, 79]), ('celldemo14', [self.points['demo14_0'], self.points['demo14_1'], self.points['demo14_2'], self.points['demo14_3'], self.points['demo14_0']], [1, 2, 2, 2, 79]), ('celldemo15', [self.points['demo15_0'], self.points['demo15_1'], self.points['demo15_2'], self.points['demo15_3'], self.points['demo15_0']], [1, 2, 2, 2, 79])]:
                c.path(vertices, codes, id=object_id)
            for object_id, points in [('demol20', [self.points['demol20'], self.points['demol21']]), ('demol21', [self.points['demol21'], self.points['demol22']]), ('demol30', [self.points['demol30'], self.points['demol31']]), ('demol31', [self.points['demol31'], self.points['demol32']])]:
                c.line(points, id=object_id)
            for object_id, vertices, codes in [('celltarget0', [self.points['target0_0'], self.points['target0_1'], self.points['target0_2'], self.points['target0_3'], self.points['target0_0']], [1, 2, 2, 2, 79]), ('celltarget1', [self.points['target1_0'], self.points['target1_1'], self.points['target1_2'], self.points['target1_3'], self.points['target1_0']], [1, 2, 2, 2, 79]), ('celltarget2', [self.points['target2_0'], self.points['target2_1'], self.points['target2_2'], self.points['target2_3'], self.points['target2_0']], [1, 2, 2, 2, 79]), ('celltarget3', [self.points['target3_0'], self.points['target3_1'], self.points['target3_2'], self.points['target3_3'], self.points['target3_0']], [1, 2, 2, 2, 79]), ('celltarget4', [self.points['target4_0'], self.points['target4_1'], self.points['target4_2'], self.points['target4_3'], self.points['target4_0']], [1, 2, 2, 2, 79]), ('celltarget5', [self.points['target5_0'], self.points['target5_1'], self.points['target5_2'], self.points['target5_3'], self.points['target5_0']], [1, 2, 2, 2, 79]), ('celltarget6', [self.points['target6_0'], self.points['target6_1'], self.points['target6_2'], self.points['target6_3'], self.points['target6_0']], [1, 2, 2, 2, 79]), ('celltarget7', [self.points['target7_0'], self.points['target7_1'], self.points['target7_2'], self.points['target7_3'], self.points['target7_0']], [1, 2, 2, 2, 79]), ('celltarget8', [self.points['target8_0'], self.points['target8_1'], self.points['target8_2'], self.points['target8_3'], self.points['target8_0']], [1, 2, 2, 2, 79]), ('celltarget9', [self.points['target9_0'], self.points['target9_1'], self.points['target9_2'], self.points['target9_3'], self.points['target9_0']], [1, 2, 2, 2, 79]), ('celltarget10', [self.points['target10_0'], self.points['target10_1'], self.points['target10_2'], self.points['target10_3'], self.points['target10_0']], [1, 2, 2, 2, 79]), ('celltarget11', [self.points['target11_0'], self.points['target11_1'], self.points['target11_2'], self.points['target11_3'], self.points['target11_0']], [1, 2, 2, 2, 79])]:
                c.path(vertices, codes, id=object_id)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane375().draw(sys.argv[1] if len(sys.argv) > 1 else None))
