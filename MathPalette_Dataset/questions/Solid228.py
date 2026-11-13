"""Collected question Solid228; construction on the shared drawing protocol."""
from pathlib import Path
import sys
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from MathPalette_Dataset.drawing import Canvas, SOLID

class Solid228:
    variants = ('C01', 'C02')

    def __init__(self):
        self.points = {
            'Ac0_2': [0.5, 2.5, 0], 'Ac1_2': [1.5, 2.5, 0], 'Ac1_1': [1.5, 1.5, 0], 'Ac2_1': [2.5, 1.5, 0],
            'Ac2_0': [2.5, 0.5, 0], 'Ac3_0': [3.5, 0.5, 0], 'Av0_2': [0, 2, 0], 'Av1_2': [1, 2, 0],
            'Av1_3': [1, 3, 0], 'Av0_3': [0, 3, 0], 'Av2_2': [2, 2, 0], 'Av2_3': [2, 3, 0],
            'Av1_1': [1, 1, 0], 'Av2_1': [2, 1, 0], 'Av3_1': [3, 1, 0], 'Av3_2': [3, 2, 0],
            'Av2_0': [2, 0, 0], 'Av3_0': [3, 0, 0], 'Av4_0': [4, 0, 0], 'Av4_1': [4, 1, 0],
            'Alabel': [-0.95, 2.5, 0], 'Bc0_0': [6.5, 0.5, 0], 'Bc0_1': [6.5, 1.5, 0], 'Bc0_2': [6.5, 2.5, 0],
            'Bc1_1': [7.5, 1.5, 0], 'Bc2_1': [8.5, 1.5, 0], 'Bc3_1': [9.5, 1.5, 0], 'Bv0_0': [6, 0, 0],
            'Bv1_0': [7, 0, 0], 'Bv1_1': [7, 1, 0], 'Bv0_1': [6, 1, 0], 'Bv1_2': [7, 2, 0],
            'Bv0_2': [6, 2, 0], 'Bv1_3': [7, 3, 0], 'Bv0_3': [6, 3, 0], 'Bv2_1': [8, 1, 0],
            'Bv2_2': [8, 2, 0], 'Bv3_1': [9, 1, 0], 'Bv3_2': [9, 2, 0], 'Bv4_1': [10, 1, 0],
            'Bv4_2': [10, 2, 0], 'Blabel': [5.05, 2.5, 0], 'Cc0_1': [12.5, 1.5, 0], 'Cc1_1': [13.5, 1.5, 0],
            'Cc2_1': [14.5, 1.5, 0], 'Cc3_1': [15.5, 1.5, 0], 'Cc1_2': [13.5, 2.5, 0],
            'Cc2_0': [14.5, 0.5, 0], 'Cv0_1': [12, 1, 0], 'Cv1_1': [13, 1, 0], 'Cv1_2': [13, 2, 0],
            'Cv0_2': [12, 2, 0], 'Cv2_1': [14, 1, 0], 'Cv2_2': [14, 2, 0], 'Cv3_1': [15, 1, 0],
            'Cv3_2': [15, 2, 0], 'Cv4_1': [16, 1, 0], 'Cv4_2': [16, 2, 0], 'Cv2_3': [14, 3, 0],
            'Cv1_3': [13, 3, 0], 'Cv2_0': [14, 0, 0], 'Cv3_0': [15, 0, 0], 'Clabel': [11.05, 2.5, 0],
            'Dc1_2': [19.5, 2.5, 0], 'Dc0_1': [18.5, 1.5, 0], 'Dc1_1': [19.5, 1.5, 0],
            'Dc1_0': [19.5, 0.5, 0], 'Dc2_0': [20.5, 0.5, 0], 'Dc3_0': [21.5, 0.5, 0], 'Dv1_2': [19, 2, 0],
            'Dv2_2': [20, 2, 0], 'Dv2_3': [20, 3, 0], 'Dv1_3': [19, 3, 0], 'Dv0_1': [18, 1, 0],
            'Dv1_1': [19, 1, 0], 'Dv0_2': [18, 2, 0], 'Dv2_1': [20, 1, 0], 'Dv1_0': [19, 0, 0],
            'Dv2_0': [20, 0, 0], 'Dv3_0': [21, 0, 0], 'Dv3_1': [21, 1, 0], 'Dv4_0': [22, 0, 0],
            'Dv4_1': [22, 1, 0], 'Dlabel': [17.05, 2.5, 0], 'Ec0_1': [24.5, 1.5, 0], 'Ec1_1': [25.5, 1.5, 0],
            'Ec2_1': [26.5, 1.5, 0], 'Ec3_1': [27.5, 1.5, 0], 'Ec3_2': [27.5, 2.5, 0],
            'Ec2_0': [26.5, 0.5, 0], 'Ev0_1': [24, 1, 0], 'Ev1_1': [25, 1, 0], 'Ev1_2': [25, 2, 0],
            'Ev0_2': [24, 2, 0], 'Ev2_1': [26, 1, 0], 'Ev2_2': [26, 2, 0], 'Ev3_1': [27, 1, 0],
            'Ev3_2': [27, 2, 0], 'Ev4_1': [28, 1, 0], 'Ev4_2': [28, 2, 0], 'Ev4_3': [28, 3, 0],
            'Ev3_3': [27, 3, 0], 'Ev2_0': [26, 0, 0], 'Ev3_0': [27, 0, 0], 'Elabel': [23.05, 2.5, 0]
        }
        self._g01 = [
            ('line_18', [[3.0, 1.0], [4.0, 1.0]]), ('line_19', [[6.0, 0.0], [7.0, 0.0]]),
            ('line_20', [[7.0, 0.0], [7.0, 1.0]]), ('line_21', [[6.0, 1.0], [7.0, 1.0]]),
            ('line_22', [[6.0, 0.0], [6.0, 1.0]]), ('line_23', [[7.0, 1.0], [7.0, 2.0]]),
            ('line_24', [[6.0, 2.0], [7.0, 2.0]]), ('line_25', [[6.0, 1.0], [6.0, 2.0]]),
            ('line_26', [[7.0, 2.0], [7.0, 3.0]]), ('line_27', [[6.0, 3.0], [7.0, 3.0]]),
            ('line_28', [[6.0, 2.0], [6.0, 3.0]]), ('line_29', [[7.0, 1.0], [8.0, 1.0]]),
            ('line_30', [[8.0, 1.0], [8.0, 2.0]]), ('line_31', [[7.0, 2.0], [8.0, 2.0]]),
            ('line_32', [[8.0, 1.0], [9.0, 1.0]]), ('line_33', [[9.0, 1.0], [9.0, 2.0]]),
            ('line_34', [[8.0, 2.0], [9.0, 2.0]]), ('line_35', [[9.0, 1.0], [10.0, 1.0]]),
            ('line_36', [[10.0, 1.0], [10.0, 2.0]]), ('line_37', [[9.0, 2.0], [10.0, 2.0]]),
            ('line_38', [[12.0, 1.0], [13.0, 1.0]]), ('line_39', [[13.0, 1.0], [13.0, 2.0]]),
            ('line_40', [[12.0, 2.0], [13.0, 2.0]]), ('line_41', [[12.0, 1.0], [12.0, 2.0]]),
            ('line_42', [[13.0, 1.0], [14.0, 1.0]]), ('line_43', [[14.0, 1.0], [14.0, 2.0]]),
            ('line_44', [[13.0, 2.0], [14.0, 2.0]]), ('line_45', [[14.0, 1.0], [15.0, 1.0]]),
            ('line_46', [[15.0, 1.0], [15.0, 2.0]]), ('line_47', [[14.0, 2.0], [15.0, 2.0]]),
            ('line_48', [[15.0, 1.0], [16.0, 1.0]]), ('line_49', [[16.0, 1.0], [16.0, 2.0]]),
            ('line_50', [[15.0, 2.0], [16.0, 2.0]]), ('line_51', [[14.0, 2.0], [14.0, 3.0]]),
            ('line_52', [[13.0, 3.0], [14.0, 3.0]]), ('line_53', [[13.0, 2.0], [13.0, 3.0]]),
            ('line_54', [[14.0, 0.0], [15.0, 0.0]]), ('line_55', [[15.0, 0.0], [15.0, 1.0]]),
            ('line_56', [[14.0, 0.0], [14.0, 1.0]]), ('line_57', [[19.0, 2.0], [20.0, 2.0]]),
            ('line_58', [[20.0, 2.0], [20.0, 3.0]]), ('line_59', [[19.0, 3.0], [20.0, 3.0]]),
            ('line_60', [[19.0, 2.0], [19.0, 3.0]]), ('line_61', [[18.0, 1.0], [19.0, 1.0]]),
            ('line_62', [[19.0, 1.0], [19.0, 2.0]]), ('line_63', [[18.0, 2.0], [19.0, 2.0]]),
            ('line_64', [[18.0, 1.0], [18.0, 2.0]]), ('line_65', [[19.0, 1.0], [20.0, 1.0]]),
            ('line_66', [[20.0, 1.0], [20.0, 2.0]]), ('line_67', [[19.0, 0.0], [20.0, 0.0]]),
            ('line_68', [[20.0, 0.0], [20.0, 1.0]]), ('line_69', [[19.0, 0.0], [19.0, 1.0]]),
            ('line_70', [[20.0, 0.0], [21.0, 0.0]]), ('line_71', [[21.0, 0.0], [21.0, 1.0]]),
            ('line_72', [[20.0, 1.0], [21.0, 1.0]]), ('line_73', [[21.0, 0.0], [22.0, 0.0]]),
            ('line_74', [[22.0, 0.0], [22.0, 1.0]]), ('line_75', [[21.0, 1.0], [22.0, 1.0]]),
            ('line_76', [[24.0, 1.0], [25.0, 1.0]]), ('line_77', [[25.0, 1.0], [25.0, 2.0]]),
            ('line_78', [[24.0, 2.0], [25.0, 2.0]]), ('line_79', [[24.0, 1.0], [24.0, 2.0]]),
            ('line_80', [[25.0, 1.0], [26.0, 1.0]]), ('line_81', [[26.0, 1.0], [26.0, 2.0]]),
            ('line_82', [[25.0, 2.0], [26.0, 2.0]]), ('line_83', [[26.0, 1.0], [27.0, 1.0]]),
            ('line_84', [[27.0, 1.0], [27.0, 2.0]]), ('line_85', [[26.0, 2.0], [27.0, 2.0]]),
            ('line_86', [[27.0, 1.0], [28.0, 1.0]]), ('line_87', [[28.0, 1.0], [28.0, 2.0]]),
            ('line_88', [[27.0, 2.0], [28.0, 2.0]]), ('line_89', [[28.0, 2.0], [28.0, 3.0]]),
            ('line_90', [[27.0, 3.0], [28.0, 3.0]]), ('line_91', [[27.0, 2.0], [27.0, 3.0]]),
            ('line_92', [[26.0, 0.0], [27.0, 0.0]]), ('line_93', [[27.0, 0.0], [27.0, 1.0]]),
            ('line_94', [[26.0, 0.0], [26.0, 1.0]])
        ]

    def draw(self, output_path=None, *, variant=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / (self.__class__.__name__ + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if variant not in self.variants:
                raise ValueError('Unknown Special variant: ' + str(variant))
            return getattr(self, 'draw_' + variant)(output_path)
        with Canvas(SOLID, xlim=(-2.3014758016887473, 28.783627410740408), ylim=(-14.049231383611318, 17.035871828817836), projection=[[1, 0, 0], [0, 1, 0]]) as c:
            for object_id, points in [('line_0', c.project([self.points['Av0_2'], self.points['Av1_2']])), ('line_1', c.project([self.points['Av1_2'], self.points['Av1_3']])), ('line_2', c.project([self.points['Av0_3'], self.points['Av1_3']])), ('line_3', c.project([self.points['Av0_2'], self.points['Av0_3']])), ('line_4', c.project([self.points['Av1_2'], self.points['Av2_2']])), ('line_5', c.project([self.points['Av2_2'], self.points['Av2_3']])), ('line_6', c.project([self.points['Av1_3'], self.points['Av2_3']])), ('line_7', c.project([self.points['Av1_1'], self.points['Av2_1']])), ('line_8', c.project([self.points['Av2_1'], self.points['Av2_2']])), ('line_9', c.project([self.points['Av1_1'], self.points['Av1_2']])), ('line_10', c.project([self.points['Av2_1'], self.points['Av3_1']])), ('line_11', c.project([self.points['Av3_1'], self.points['Av3_2']])), ('line_12', c.project([self.points['Av2_2'], self.points['Av3_2']])), ('line_13', c.project([self.points['Av2_0'], self.points['Av3_0']])), ('line_14', c.project([self.points['Av3_0'], self.points['Av3_1']])), ('line_15', c.project([self.points['Av2_0'], self.points['Av2_1']])), ('line_16', c.project([self.points['Av3_0'], self.points['Av4_0']])), ('line_17', c.project([self.points['Av4_0'], self.points['Av4_1']])), ('line_18', c.project([self.points['Av3_1'], self.points['Av4_1']])), ('line_19', c.project([self.points['Bv0_0'], self.points['Bv1_0']])), ('line_20', c.project([self.points['Bv1_0'], self.points['Bv1_1']])), ('line_21', c.project([self.points['Bv0_1'], self.points['Bv1_1']])), ('line_22', c.project([self.points['Bv0_0'], self.points['Bv0_1']])), ('line_23', c.project([self.points['Bv1_1'], self.points['Bv1_2']])), ('line_24', c.project([self.points['Bv0_2'], self.points['Bv1_2']])), ('line_25', c.project([self.points['Bv0_1'], self.points['Bv0_2']])), ('line_26', c.project([self.points['Bv1_2'], self.points['Bv1_3']])), ('line_27', c.project([self.points['Bv0_3'], self.points['Bv1_3']])), ('line_28', c.project([self.points['Bv0_2'], self.points['Bv0_3']])), ('line_29', c.project([self.points['Bv1_1'], self.points['Bv2_1']])), ('line_30', c.project([self.points['Bv2_1'], self.points['Bv2_2']])), ('line_31', c.project([self.points['Bv1_2'], self.points['Bv2_2']])), ('line_32', c.project([self.points['Bv2_1'], self.points['Bv3_1']])), ('line_33', c.project([self.points['Bv3_1'], self.points['Bv3_2']])), ('line_34', c.project([self.points['Bv2_2'], self.points['Bv3_2']])), ('line_35', c.project([self.points['Bv3_1'], self.points['Bv4_1']])), ('line_36', c.project([self.points['Bv4_1'], self.points['Bv4_2']])), ('line_37', c.project([self.points['Bv3_2'], self.points['Bv4_2']])), ('line_38', c.project([self.points['Cv0_1'], self.points['Cv1_1']])), ('line_39', c.project([self.points['Cv1_1'], self.points['Cv1_2']])), ('line_40', c.project([self.points['Cv0_2'], self.points['Cv1_2']])), ('line_41', c.project([self.points['Cv0_1'], self.points['Cv0_2']])), ('line_42', c.project([self.points['Cv1_1'], self.points['Cv2_1']])), ('line_43', c.project([self.points['Cv2_1'], self.points['Cv2_2']])), ('line_44', c.project([self.points['Cv1_2'], self.points['Cv2_2']])), ('line_45', c.project([self.points['Cv2_1'], self.points['Cv3_1']])), ('line_46', c.project([self.points['Cv3_1'], self.points['Cv3_2']])), ('line_47', c.project([self.points['Cv2_2'], self.points['Cv3_2']])), ('line_48', c.project([self.points['Cv3_1'], self.points['Cv4_1']])), ('line_49', c.project([self.points['Cv4_1'], self.points['Cv4_2']])), ('line_50', c.project([self.points['Cv3_2'], self.points['Cv4_2']])), ('line_51', c.project([self.points['Cv2_2'], self.points['Cv2_3']])), ('line_52', c.project([self.points['Cv1_3'], self.points['Cv2_3']])), ('line_53', c.project([self.points['Cv1_2'], self.points['Cv1_3']])), ('line_54', c.project([self.points['Cv2_0'], self.points['Cv3_0']])), ('line_55', c.project([self.points['Cv3_0'], self.points['Cv3_1']])), ('line_56', c.project([self.points['Cv2_0'], self.points['Cv2_1']])), ('line_57', c.project([self.points['Dv1_2'], self.points['Dv2_2']])), ('line_58', c.project([self.points['Dv2_2'], self.points['Dv2_3']])), ('line_59', c.project([self.points['Dv1_3'], self.points['Dv2_3']])), ('line_60', c.project([self.points['Dv1_2'], self.points['Dv1_3']])), ('line_61', c.project([self.points['Dv0_1'], self.points['Dv1_1']])), ('line_62', c.project([self.points['Dv1_1'], self.points['Dv1_2']])), ('line_63', c.project([self.points['Dv0_2'], self.points['Dv1_2']])), ('line_64', c.project([self.points['Dv0_1'], self.points['Dv0_2']])), ('line_65', c.project([self.points['Dv1_1'], self.points['Dv2_1']])), ('line_66', c.project([self.points['Dv2_1'], self.points['Dv2_2']])), ('line_67', c.project([self.points['Dv1_0'], self.points['Dv2_0']])), ('line_68', c.project([self.points['Dv2_0'], self.points['Dv2_1']])), ('line_69', c.project([self.points['Dv1_0'], self.points['Dv1_1']])), ('line_70', c.project([self.points['Dv2_0'], self.points['Dv3_0']])), ('line_71', c.project([self.points['Dv3_0'], self.points['Dv3_1']])), ('line_72', c.project([self.points['Dv2_1'], self.points['Dv3_1']])), ('line_73', c.project([self.points['Dv3_0'], self.points['Dv4_0']])), ('line_74', c.project([self.points['Dv4_0'], self.points['Dv4_1']])), ('line_75', c.project([self.points['Dv3_1'], self.points['Dv4_1']])), ('line_76', c.project([self.points['Ev0_1'], self.points['Ev1_1']])), ('line_77', c.project([self.points['Ev1_1'], self.points['Ev1_2']])), ('line_78', c.project([self.points['Ev0_2'], self.points['Ev1_2']])), ('line_79', c.project([self.points['Ev0_1'], self.points['Ev0_2']])), ('line_80', c.project([self.points['Ev1_1'], self.points['Ev2_1']])), ('line_81', c.project([self.points['Ev2_1'], self.points['Ev2_2']])), ('line_82', c.project([self.points['Ev1_2'], self.points['Ev2_2']])), ('line_83', c.project([self.points['Ev2_1'], self.points['Ev3_1']])), ('line_84', c.project([self.points['Ev3_1'], self.points['Ev3_2']])), ('line_85', c.project([self.points['Ev2_2'], self.points['Ev3_2']])), ('line_86', c.project([self.points['Ev3_1'], self.points['Ev4_1']])), ('line_87', c.project([self.points['Ev4_1'], self.points['Ev4_2']])), ('line_88', c.project([self.points['Ev3_2'], self.points['Ev4_2']])), ('line_89', c.project([self.points['Ev4_2'], self.points['Ev4_3']])), ('line_90', c.project([self.points['Ev3_3'], self.points['Ev4_3']])), ('line_91', c.project([self.points['Ev3_2'], self.points['Ev3_3']])), ('line_92', c.project([self.points['Ev2_0'], self.points['Ev3_0']])), ('line_93', c.project([self.points['Ev3_0'], self.points['Ev3_1']])), ('line_94', c.project([self.points['Ev2_0'], self.points['Ev2_1']]))]:
                c.line(points, id=object_id, clip_on=False, zorder=3)
            for object_id, text, anchor in [('label_0', '(A)', c.project(self.points['Alabel'])), ('label_1', '(B)', c.project(self.points['Blabel'])), ('label_2', '(C)', c.project(self.points['Clabel'])), ('label_3', '(D)', c.project(self.points['Dlabel'])), ('label_4', '(E)', c.project(self.points['Elabel']))]:
                c.text(text, anchor, id=object_id)
            return c.save(output_path)

    def _draw_choices(self, c, kw=None):
        _kw = kw or {}
        for object_id, points in [('line_0', [[0.0, 2.0], [1.0, 2.0]]), ('line_1', [[1.0, 2.0], [1.0, 3.0]]), ('line_2', [[0.0, 3.0], [1.0, 3.0]])]:
            c.line(points, id=object_id, zorder=3, clip_on=False)
        c.line([[0.0, 2.0], [0.0, 3.0]], id='line_3', zorder=3, clip_on=False, linewidth=2.0, solid_capstyle='butt', **_kw.get(1, {'color': '#DC2626'}))
        c.line([[1.0, 2.0], [2.0, 2.0]], id='line_4', zorder=3, clip_on=False)
        c.line([[2.0, 2.0], [2.0, 3.0]], id='line_5', zorder=3, clip_on=False)
        c.line([[1.0, 3.0], [2.0, 3.0]], id='line_6', zorder=3, clip_on=False, linewidth=2.0, solid_capstyle='butt', **_kw.get(4, {'color': '#16A34A'}))
        for object_id, points in [('line_7', [[1.0, 1.0], [2.0, 1.0]]), ('line_8', [[2.0, 1.0], [2.0, 2.0]]), ('line_9', [[1.0, 1.0], [1.0, 2.0]]), ('line_10', [[2.0, 1.0], [3.0, 1.0]]), ('line_11', [[3.0, 1.0], [3.0, 2.0]]), ('line_12', [[2.0, 2.0], [3.0, 2.0]])]:
            c.line(points, id=object_id, zorder=3, clip_on=False)
        c.line([[2.0, 0.0], [3.0, 0.0]], id='line_13', zorder=3, clip_on=False, linewidth=2.0, solid_capstyle='butt', **_kw.get(6, {'color': '#16A34A'}))
        for object_id, points in [('line_14', [[3.0, 0.0], [3.0, 1.0]]), ('line_15', [[2.0, 0.0], [2.0, 1.0]]), ('line_16', [[3.0, 0.0], [4.0, 0.0]])]:
            c.line(points, id=object_id, zorder=3, clip_on=False)
        c.line([[4.0, 0.0], [4.0, 1.0]], id='line_17', zorder=3, clip_on=False, linewidth=2.0, solid_capstyle='butt', **_kw.get(8, {'color': '#DC2626'}))
        for object_id, points in self._g01:
            c.line(points, id=object_id, zorder=3, clip_on=False)
        for object_id, text, anchor in [('label_0', '(A)', (-0.95, 2.5)), ('label_1', '(B)', (5.05, 2.5)), ('label_2', '(C)', (11.05, 2.5)), ('label_3', '(D)', (17.05, 2.5)), ('label_4', '(E)', (23.05, 2.5))]:
            c.text(text, anchor, id=object_id)

    def draw_C01(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Solid228_C01.png'
        with Canvas(SOLID, xlim=(-2.3014758016887473, 28.783627410740408), ylim=(-14.049231383611318, 17.035871828817836)) as c:
            self._draw_choices(c)
            return c.save(output_path)

    def draw_C02(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Solid228_C02.png'
        with Canvas(SOLID, xlim=(-2.3014758016887473, 28.783627410740408), ylim=(-14.049231383611318, 17.035871828817836)) as c:
            self._draw_choices(c, kw={1: {'color': '#2563EB'}, 4: {'color': '#DC2626'}, 6: {'color': '#DC2626'}, 8: {'color': '#2563EB'}})
            return c.save(output_path)
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Solid228')
    parser.add_argument('output', nargs='?')
    parser.add_argument('--variant', choices=('C01', 'C02'))
    args = parser.parse_args()
    print(Solid228().draw(args.output, variant=args.variant))
