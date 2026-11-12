"""Frozen question Solid228; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Solid228:

    def __init__(self):
        self.id = 'Solid228'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:2560'
        self.question = 'Which pattern of identical squares could NOT be folded along the lines shown to form a cube?\n\nChoices:\nA:A\nB:B\nC:C\nD:D\nE:E'
        self.answer = 'D'
        self.answer_type = 'choice'
        self.choices = {'A': 'A', 'B': 'B', 'C': 'C', 'D': 'D', 'E': 'E'}
        self.query = self.question
        self.points = {'Ac0_2': [0.5, 2.5, 0],
         'Ac1_2': [1.5, 2.5, 0],
         'Ac1_1': [1.5, 1.5, 0],
         'Ac2_1': [2.5, 1.5, 0],
         'Ac2_0': [2.5, 0.5, 0],
         'Ac3_0': [3.5, 0.5, 0],
         'Av0_2': [0, 2, 0],
         'Av1_2': [1, 2, 0],
         'Av1_3': [1, 3, 0],
         'Av0_3': [0, 3, 0],
         'Av2_2': [2, 2, 0],
         'Av2_3': [2, 3, 0],
         'Av1_1': [1, 1, 0],
         'Av2_1': [2, 1, 0],
         'Av3_1': [3, 1, 0],
         'Av3_2': [3, 2, 0],
         'Av2_0': [2, 0, 0],
         'Av3_0': [3, 0, 0],
         'Av4_0': [4, 0, 0],
         'Av4_1': [4, 1, 0],
         'Alabel': [-0.95, 2.5, 0],
         'Bc0_0': [6.5, 0.5, 0],
         'Bc0_1': [6.5, 1.5, 0],
         'Bc0_2': [6.5, 2.5, 0],
         'Bc1_1': [7.5, 1.5, 0],
         'Bc2_1': [8.5, 1.5, 0],
         'Bc3_1': [9.5, 1.5, 0],
         'Bv0_0': [6, 0, 0],
         'Bv1_0': [7, 0, 0],
         'Bv1_1': [7, 1, 0],
         'Bv0_1': [6, 1, 0],
         'Bv1_2': [7, 2, 0],
         'Bv0_2': [6, 2, 0],
         'Bv1_3': [7, 3, 0],
         'Bv0_3': [6, 3, 0],
         'Bv2_1': [8, 1, 0],
         'Bv2_2': [8, 2, 0],
         'Bv3_1': [9, 1, 0],
         'Bv3_2': [9, 2, 0],
         'Bv4_1': [10, 1, 0],
         'Bv4_2': [10, 2, 0],
         'Blabel': [5.05, 2.5, 0],
         'Cc0_1': [12.5, 1.5, 0],
         'Cc1_1': [13.5, 1.5, 0],
         'Cc2_1': [14.5, 1.5, 0],
         'Cc3_1': [15.5, 1.5, 0],
         'Cc1_2': [13.5, 2.5, 0],
         'Cc2_0': [14.5, 0.5, 0],
         'Cv0_1': [12, 1, 0],
         'Cv1_1': [13, 1, 0],
         'Cv1_2': [13, 2, 0],
         'Cv0_2': [12, 2, 0],
         'Cv2_1': [14, 1, 0],
         'Cv2_2': [14, 2, 0],
         'Cv3_1': [15, 1, 0],
         'Cv3_2': [15, 2, 0],
         'Cv4_1': [16, 1, 0],
         'Cv4_2': [16, 2, 0],
         'Cv2_3': [14, 3, 0],
         'Cv1_3': [13, 3, 0],
         'Cv2_0': [14, 0, 0],
         'Cv3_0': [15, 0, 0],
         'Clabel': [11.05, 2.5, 0],
         'Dc1_2': [19.5, 2.5, 0],
         'Dc0_1': [18.5, 1.5, 0],
         'Dc1_1': [19.5, 1.5, 0],
         'Dc1_0': [19.5, 0.5, 0],
         'Dc2_0': [20.5, 0.5, 0],
         'Dc3_0': [21.5, 0.5, 0],
         'Dv1_2': [19, 2, 0],
         'Dv2_2': [20, 2, 0],
         'Dv2_3': [20, 3, 0],
         'Dv1_3': [19, 3, 0],
         'Dv0_1': [18, 1, 0],
         'Dv1_1': [19, 1, 0],
         'Dv0_2': [18, 2, 0],
         'Dv2_1': [20, 1, 0],
         'Dv1_0': [19, 0, 0],
         'Dv2_0': [20, 0, 0],
         'Dv3_0': [21, 0, 0],
         'Dv3_1': [21, 1, 0],
         'Dv4_0': [22, 0, 0],
         'Dv4_1': [22, 1, 0],
         'Dlabel': [17.05, 2.5, 0],
         'Ec0_1': [24.5, 1.5, 0],
         'Ec1_1': [25.5, 1.5, 0],
         'Ec2_1': [26.5, 1.5, 0],
         'Ec3_1': [27.5, 1.5, 0],
         'Ec3_2': [27.5, 2.5, 0],
         'Ec2_0': [26.5, 0.5, 0],
         'Ev0_1': [24, 1, 0],
         'Ev1_1': [25, 1, 0],
         'Ev1_2': [25, 2, 0],
         'Ev0_2': [24, 2, 0],
         'Ev2_1': [26, 1, 0],
         'Ev2_2': [26, 2, 0],
         'Ev3_1': [27, 1, 0],
         'Ev3_2': [27, 2, 0],
         'Ev4_1': [28, 1, 0],
         'Ev4_2': [28, 2, 0],
         'Ev4_3': [28, 3, 0],
         'Ev3_3': [27, 3, 0],
         'Ev2_0': [26, 0, 0],
         'Ev3_0': [27, 0, 0],
         'Elabel': [23.05, 2.5, 0]}
        self.subject = 'SolidGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'SolidGeometry' / 'dataset_generator/scenes/Solid228.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('SolidGeometry', self.id, variant, output_path)
        with Canvas(SOLID, xlim=[-2.3014758016887473, 28.783627410740408], ylim=[-14.049231383611318, 17.035871828817836], projection=[[1, 0, 0], [0, 1, 0]], origin=[0, 0, 0], offset=[0, 0]) as c:
            for object_id, points in [('line_0', c.project([self.points['Av0_2'], self.points['Av1_2']])), ('line_1', c.project([self.points['Av1_2'], self.points['Av1_3']])), ('line_2', c.project([self.points['Av0_3'], self.points['Av1_3']])), ('line_3', c.project([self.points['Av0_2'], self.points['Av0_3']])), ('line_4', c.project([self.points['Av1_2'], self.points['Av2_2']])), ('line_5', c.project([self.points['Av2_2'], self.points['Av2_3']])), ('line_6', c.project([self.points['Av1_3'], self.points['Av2_3']])), ('line_7', c.project([self.points['Av1_1'], self.points['Av2_1']])), ('line_8', c.project([self.points['Av2_1'], self.points['Av2_2']])), ('line_9', c.project([self.points['Av1_1'], self.points['Av1_2']])), ('line_10', c.project([self.points['Av2_1'], self.points['Av3_1']])), ('line_11', c.project([self.points['Av3_1'], self.points['Av3_2']])), ('line_12', c.project([self.points['Av2_2'], self.points['Av3_2']])), ('line_13', c.project([self.points['Av2_0'], self.points['Av3_0']])), ('line_14', c.project([self.points['Av3_0'], self.points['Av3_1']])), ('line_15', c.project([self.points['Av2_0'], self.points['Av2_1']])), ('line_16', c.project([self.points['Av3_0'], self.points['Av4_0']])), ('line_17', c.project([self.points['Av4_0'], self.points['Av4_1']])), ('line_18', c.project([self.points['Av3_1'], self.points['Av4_1']])), ('line_19', c.project([self.points['Bv0_0'], self.points['Bv1_0']])), ('line_20', c.project([self.points['Bv1_0'], self.points['Bv1_1']])), ('line_21', c.project([self.points['Bv0_1'], self.points['Bv1_1']])), ('line_22', c.project([self.points['Bv0_0'], self.points['Bv0_1']])), ('line_23', c.project([self.points['Bv1_1'], self.points['Bv1_2']])), ('line_24', c.project([self.points['Bv0_2'], self.points['Bv1_2']])), ('line_25', c.project([self.points['Bv0_1'], self.points['Bv0_2']])), ('line_26', c.project([self.points['Bv1_2'], self.points['Bv1_3']])), ('line_27', c.project([self.points['Bv0_3'], self.points['Bv1_3']])), ('line_28', c.project([self.points['Bv0_2'], self.points['Bv0_3']])), ('line_29', c.project([self.points['Bv1_1'], self.points['Bv2_1']])), ('line_30', c.project([self.points['Bv2_1'], self.points['Bv2_2']])), ('line_31', c.project([self.points['Bv1_2'], self.points['Bv2_2']])), ('line_32', c.project([self.points['Bv2_1'], self.points['Bv3_1']])), ('line_33', c.project([self.points['Bv3_1'], self.points['Bv3_2']])), ('line_34', c.project([self.points['Bv2_2'], self.points['Bv3_2']])), ('line_35', c.project([self.points['Bv3_1'], self.points['Bv4_1']])), ('line_36', c.project([self.points['Bv4_1'], self.points['Bv4_2']])), ('line_37', c.project([self.points['Bv3_2'], self.points['Bv4_2']])), ('line_38', c.project([self.points['Cv0_1'], self.points['Cv1_1']])), ('line_39', c.project([self.points['Cv1_1'], self.points['Cv1_2']])), ('line_40', c.project([self.points['Cv0_2'], self.points['Cv1_2']])), ('line_41', c.project([self.points['Cv0_1'], self.points['Cv0_2']])), ('line_42', c.project([self.points['Cv1_1'], self.points['Cv2_1']])), ('line_43', c.project([self.points['Cv2_1'], self.points['Cv2_2']])), ('line_44', c.project([self.points['Cv1_2'], self.points['Cv2_2']])), ('line_45', c.project([self.points['Cv2_1'], self.points['Cv3_1']])), ('line_46', c.project([self.points['Cv3_1'], self.points['Cv3_2']])), ('line_47', c.project([self.points['Cv2_2'], self.points['Cv3_2']])), ('line_48', c.project([self.points['Cv3_1'], self.points['Cv4_1']])), ('line_49', c.project([self.points['Cv4_1'], self.points['Cv4_2']])), ('line_50', c.project([self.points['Cv3_2'], self.points['Cv4_2']])), ('line_51', c.project([self.points['Cv2_2'], self.points['Cv2_3']])), ('line_52', c.project([self.points['Cv1_3'], self.points['Cv2_3']])), ('line_53', c.project([self.points['Cv1_2'], self.points['Cv1_3']])), ('line_54', c.project([self.points['Cv2_0'], self.points['Cv3_0']])), ('line_55', c.project([self.points['Cv3_0'], self.points['Cv3_1']])), ('line_56', c.project([self.points['Cv2_0'], self.points['Cv2_1']])), ('line_57', c.project([self.points['Dv1_2'], self.points['Dv2_2']])), ('line_58', c.project([self.points['Dv2_2'], self.points['Dv2_3']])), ('line_59', c.project([self.points['Dv1_3'], self.points['Dv2_3']])), ('line_60', c.project([self.points['Dv1_2'], self.points['Dv1_3']])), ('line_61', c.project([self.points['Dv0_1'], self.points['Dv1_1']])), ('line_62', c.project([self.points['Dv1_1'], self.points['Dv1_2']])), ('line_63', c.project([self.points['Dv0_2'], self.points['Dv1_2']])), ('line_64', c.project([self.points['Dv0_1'], self.points['Dv0_2']])), ('line_65', c.project([self.points['Dv1_1'], self.points['Dv2_1']])), ('line_66', c.project([self.points['Dv2_1'], self.points['Dv2_2']])), ('line_67', c.project([self.points['Dv1_0'], self.points['Dv2_0']])), ('line_68', c.project([self.points['Dv2_0'], self.points['Dv2_1']])), ('line_69', c.project([self.points['Dv1_0'], self.points['Dv1_1']])), ('line_70', c.project([self.points['Dv2_0'], self.points['Dv3_0']])), ('line_71', c.project([self.points['Dv3_0'], self.points['Dv3_1']])), ('line_72', c.project([self.points['Dv2_1'], self.points['Dv3_1']])), ('line_73', c.project([self.points['Dv3_0'], self.points['Dv4_0']])), ('line_74', c.project([self.points['Dv4_0'], self.points['Dv4_1']])), ('line_75', c.project([self.points['Dv3_1'], self.points['Dv4_1']])), ('line_76', c.project([self.points['Ev0_1'], self.points['Ev1_1']])), ('line_77', c.project([self.points['Ev1_1'], self.points['Ev1_2']])), ('line_78', c.project([self.points['Ev0_2'], self.points['Ev1_2']])), ('line_79', c.project([self.points['Ev0_1'], self.points['Ev0_2']])), ('line_80', c.project([self.points['Ev1_1'], self.points['Ev2_1']])), ('line_81', c.project([self.points['Ev2_1'], self.points['Ev2_2']])), ('line_82', c.project([self.points['Ev1_2'], self.points['Ev2_2']])), ('line_83', c.project([self.points['Ev2_1'], self.points['Ev3_1']])), ('line_84', c.project([self.points['Ev3_1'], self.points['Ev3_2']])), ('line_85', c.project([self.points['Ev2_2'], self.points['Ev3_2']])), ('line_86', c.project([self.points['Ev3_1'], self.points['Ev4_1']])), ('line_87', c.project([self.points['Ev4_1'], self.points['Ev4_2']])), ('line_88', c.project([self.points['Ev3_2'], self.points['Ev4_2']])), ('line_89', c.project([self.points['Ev4_2'], self.points['Ev4_3']])), ('line_90', c.project([self.points['Ev3_3'], self.points['Ev4_3']])), ('line_91', c.project([self.points['Ev3_2'], self.points['Ev3_3']])), ('line_92', c.project([self.points['Ev2_0'], self.points['Ev3_0']])), ('line_93', c.project([self.points['Ev3_0'], self.points['Ev3_1']])), ('line_94', c.project([self.points['Ev2_0'], self.points['Ev2_1']]))]:
                c.line(points, id=object_id, clip_on=False, zorder=3)
            for object_id, text, anchor in [('label_0', '(A)', c.project(self.points['Alabel'])), ('label_1', '(B)', c.project(self.points['Blabel'])), ('label_2', '(C)', c.project(self.points['Clabel'])), ('label_3', '(D)', c.project(self.points['Dlabel'])), ('label_4', '(E)', c.project(self.points['Elabel']))]:
                c.text(text, anchor, id=object_id, offset_pt=[0, 0], vertex=False)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Solid228().draw(sys.argv[1] if len(sys.argv) > 1 else None))
