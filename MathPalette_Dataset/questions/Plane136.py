"""Collected question Plane136; construction on the shared drawing protocol."""
from pathlib import Path
import sys
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from MathPalette_Dataset.drawing import Canvas, PLANE
import numpy as np

class Plane136:
    variants = ('C01', 'C02', 'C03', 'C04', 'C05', 'C06')

    def __init__(self):
        _t = np.radians(np.linspace(50.0, 90.0, 161))
        self._samples_001 = [[0.0, 0.0], *np.column_stack([3.0 * np.cos(_t), 3.0 * np.sin(_t)]).tolist(), [0.0, 0.0]]
        self._samples_002 = [1] + [2] * 161 + [79]
        self._samples_003 = [
            [4.440892098500626e-16, -3.0000000000000004], [0.7956093000000006, -3.0000000000000004],
            [1.5587396123545612, -2.6839010747647256], [2.1213203435596433, -2.121320343559643],
            [2.683901074764726, -1.5587396123545607], [3.000000000000001, -0.7956093000000002],
            [3.000000000000001, 0.0], [3.000000000000001, 0.4422775651762348],
            [2.9023183161853865, 0.8745183920135485], [2.7189141236784007, 1.267850477737024]
        ]
        self._samples_004 = [
            [4.440892098500626e-16, 3.0000000000000004], [-0.7956092999999997, 3.0000000000000004],
            [-1.5587396123545603, 2.6839010747647256], [-2.1213203435596424, 2.121320343559643],
            [-2.683901074764725, 1.5587396123545607], [-3.0, 0.7956093000000002], [-3.0, 0.0],
            [-3.0, -0.7956093000000002], [-2.683901074764725, -1.5587396123545607],
            [-2.1213203435596424, -2.121320343559643], [-1.5587396123545603, -2.6839010747647256],
            [-0.7956092999999997, -3.0000000000000004], [4.440892098500626e-16, -3.0000000000000004]
        ]
        self._samples_005 = [
            [4.440892098500626e-16, -3.0000000000000004], [0.7956093000000006, -3.0000000000000004],
            [1.5587396123545612, -2.6839010747647256], [2.1213203435596433, -2.121320343559643],
            [2.683901074764726, -1.5587396123545607], [3.000000000000001, -0.7956093000000002],
            [3.000000000000001, 0.0], [3.000000000000001, 0.7956093000000002],
            [2.683901074764726, 1.5587396123545607], [2.1213203435596433, 2.121320343559643],
            [2.0593603014567536, 2.1832803856625325], [1.9949676326978012, 2.2422506523293433],
            [1.9283668662024493, 2.298138140636406]
        ]
        self._samples_006 = [
            [-2.1213203435596424, 2.121320343559643], [-2.683901074764725, 1.5587396123545607],
            [-3.0, 0.7956093000000002], [-3.0, 0.0], [-3.0, -0.7956093000000002],
            [-2.683901074764725, -1.5587396123545607], [-2.1213203435596424, -2.121320343559643],
            [-1.5587396123545603, -2.6839010747647256], [-0.7956092999999997, -3.0000000000000004],
            [4.440892098500626e-16, -3.0000000000000004]
        ]

    def _draw_base(self, c, custom=None):
        c.path(self._samples_001, self._samples_002, alpha=0.45, zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), capstyle='butt')
        c.path(self._samples_001, self._samples_002, id='shade', capstyle='butt', fill=False)
        if custom and 2 in custom:
            custom[2](c)
        else:
            c.path(self._samples_003, [1, 4, 4, 4, 4, 4, 4, 4, 4, 4], id='circle_boundary', capstyle='butt', fill=False)
            c.path([[2.7189141236784007, 1.267850477737024], [2.5723940950474593, 1.5820800908876425], [2.371163609261935, 1.8714770778573513], [2.1213203435596433, 2.121320343559643], [1.5587396123545612, 2.6839010747647256], [0.7956093000000006, 3.0000000000000004], [4.440892098500626e-16, 3.0000000000000004]], [1, 4, 4, 4, 4, 4, 4], id='circle_boundary', edgecolor='#DC2626', linewidth=3.0, capstyle='butt', fill=False)
            c.path(self._samples_004, [1] + [4] * 12, id='circle_boundary', capstyle='butt', fill=False)
            c.path([[2.7189233611099506, 1.2678547852220985], [2.220446049250313e-16, 2.220446049250313e-16]], [1, 2], id='diameter', edgecolor='#DC2626', linewidth=3.0, joinstyle='round', fill=False)
            c.path([[2.220446049250313e-16, 2.220446049250313e-16], [-2.71892336110995, -1.267854785222098]], [1, 2], id='diameter', joinstyle='round', fill=False)
            c.line([[0.0, 0.0], [1.9283628290596182, 2.298133329356934]], id='radius_1')
            c.line([[0.0, 0.0], [1.8369701987210297e-16, 3.0]], id='radius_2', color='#DC2626', linewidth=3.0)
            c.line([[0.0, 0.0], [-2.1213203435596424, 2.121320343559643]], id='radius_3')
            c.line([[0.0, 0.0], [-2.954423259036624, 0.5209445330007908]], id='radius_4')
        c.point([[0.0, 0.0]], id='center_dot')
        for object_id, vertices, codes in [('angle_arc_0', [[0.4807011460373026, 0.22415462568107858], [0.4643840146420749, 0.25914682688100815], [0.4442947175967112, 0.2922529638057495], [0.4207906688493419, 0.32288403649781766], [0.39728662010197263, 0.3535151091898858], [0.3705080401157647, 0.3814883787838902], [0.34093135362457466, 0.40630616551009385]], [1, 4, 4, 4, 4, 4, 4]), ('angle_arc_2', [[3.402386826488966e-17, 0.5556519363555011], [-0.07296754372589838, 0.5556519363555011], [-0.14522557001885167, 0.5412789212833882], [-0.21263879020483156, 0.5133554511991116], [-0.28005201039081146, 0.4854319811148351], [-0.3413094072013021, 0.4445010971515195], [-0.39290525217641076, 0.3929052521764108]], [1, 4, 4, 4, 4, 4, 4]), ('angle_arc_3', [[-0.5357798893314691, 0.5357798893314693], [-0.5904339043914704, 0.48112587427146825], [-0.636404801010726, 0.41842948222960896], [-0.6720944823051618, 0.34987024234570085], [-0.7077841635995975, 0.28131100246179275], [-0.7327742182514954, 0.20769267539889377], [-0.7461959112261047, 0.13157447204350076]], [1, 4, 4, 4, 4, 4, 4]), ('angle_arc_4', [[-0.5472103348991435, 0.0964879461652339], [-0.5570529097471904, 0.04066793037127908], [-0.558296629018141, -0.016330916859590823], [-0.5508982570120692, -0.07252713145218187], [-0.5434998850059973, -0.1287233460447729], [-0.5275461572292945, -0.18345810641969226], [-0.5035916768009838, -0.23482865547541534]], [1, 4, 4, 4, 4, 4, 4])]:
            c.path(vertices, codes, id=object_id, zorder=3, capstyle='butt', fill=False)
        c.text('B', (2.7189233611099497, 1.2678547852220983), id='label_B', fontsize=18.0, fontstyle='italic', offset_pt=(16.3135401666597, 7.60712871133259))
        c.text('A', (-2.71892336110995, -1.2678547852220978), id='label_A', fontsize=18.0, fontstyle='italic', offset_pt=(-16.3135401666597, -7.607128711332587))
        c.text('O', (0.0, 0.0), id='label_O', fontsize=18.0, fontstyle='italic', offset_pt=(5.9166556643697925, -12.688309018513099))
        c.text('25°', (0.0, 0.0), id='angle_label_0', offset_pt=(87.26886743203586, 66.96375719095927))
        c.text('45°', (0.0, 0.0), id='angle_label_2', offset_pt=(-31.380041453937352, 75.75812166592551))
        c.text('35°', (0.0, 0.0), id='angle_label_3', offset_pt=(-86.92706165146573, 45.251364097033324))
        c.text('35°', (0.0, 0.0), id='angle_label_4', offset_pt=(-89.23003752364295, -11.747357299804637))

    def draw(self, output_path=None, *, variant=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / (self.__class__.__name__ + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if variant not in self.variants:
                raise ValueError('Unknown Special variant: ' + str(variant))
            return getattr(self, 'draw_' + variant)(output_path)
        with Canvas(PLANE, xlim=(-3.1423632415275478, 3.142363241527546), ylim=(-3.142363241527547, 3.142363241527547)) as c:

            def _slot_2(c):
                c.circle([0.0, 0.0], 3.0, id='circle_boundary', fill=False)
                for object_id, points in [('diameter', [[2.7189233611099497, 1.2678547852220983], [-2.71892336110995, -1.2678547852220978]]), ('radius_1', [[0.0, 0.0], [1.9283628290596182, 2.298133329356934]]), ('radius_2', [[0.0, 0.0], [1.8369701987210297e-16, 3.0]]), ('radius_3', [[0.0, 0.0], [-2.1213203435596424, 2.121320343559643]]), ('radius_4', [[0.0, 0.0], [-2.954423259036624, 0.5209445330007908]])]:
                    c.line(points, id=object_id)
            self._draw_base(c, custom={2: _slot_2})
            return c.save(output_path)

    def draw_C01(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane136_C01.png'
        with Canvas(PLANE, xlim=(-3.1423632415275478, 3.142363241527546), ylim=(-3.142363241527547, 3.142363241527547)) as c:
            self._draw_base(c)
            return c.save(output_path)

    def draw_C02(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane136_C02.png'
        with Canvas(PLANE, xlim=(-3.1423632415275478, 3.142363241527546), ylim=(-3.142363241527547, 3.142363241527547)) as c:

            def _slot_2(c):
                c.path(self._samples_003, [1, 4, 4, 4, 4, 4, 4, 4, 4, 4], id='circle_boundary', capstyle='butt', fill=False)
                c.path([[2.7189141236784007, 1.267850477737024], [2.5723940950474593, 1.5820800908876425], [2.371163609261935, 1.8714770778573513], [2.1213203435596433, 2.121320343559643], [1.5587396123545612, 2.6839010747647256], [0.7956093000000006, 3.0000000000000004], [4.440892098500626e-16, 3.0000000000000004]], [1, 4, 4, 4, 4, 4, 4], id='circle_boundary', edgecolor='#2563EB', linewidth=3.0, capstyle='butt', fill=False)
                c.path(self._samples_004, [1] + [4] * 12, id='circle_boundary', capstyle='butt', fill=False)
                c.path([[2.7189233611099506, 1.2678547852220985], [2.220446049250313e-16, 2.220446049250313e-16]], [1, 2], id='diameter', edgecolor='#2563EB', linewidth=3.0, joinstyle='round', fill=False)
                c.path([[2.220446049250313e-16, 2.220446049250313e-16], [-2.71892336110995, -1.267854785222098]], [1, 2], id='diameter', joinstyle='round', fill=False)
                c.line([[0.0, 0.0], [1.9283628290596182, 2.298133329356934]], id='radius_1')
                c.line([[0.0, 0.0], [1.8369701987210297e-16, 3.0]], id='radius_2', color='#2563EB', linewidth=3.0)
                c.line([[0.0, 0.0], [-2.1213203435596424, 2.121320343559643]], id='radius_3')
                c.line([[0.0, 0.0], [-2.954423259036624, 0.5209445330007908]], id='radius_4')
            self._draw_base(c, custom={2: _slot_2})
            return c.save(output_path)

    def draw_C03(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane136_C03.png'
        with Canvas(PLANE, xlim=(-3.1423632415275478, 3.142363241527546), ylim=(-3.142363241527547, 3.142363241527547)) as c:

            def _slot_2(c):
                c.path(self._samples_003, [1, 4, 4, 4, 4, 4, 4, 4, 4, 4], id='circle_boundary', capstyle='butt', fill=False)
                c.path([[2.7189141236784007, 1.267850477737024], [2.5723940950474593, 1.5820800908876425], [2.371163609261935, 1.8714770778573513], [2.1213203435596433, 2.121320343559643], [1.5587396123545612, 2.6839010747647256], [0.7956093000000006, 3.0000000000000004], [4.440892098500626e-16, 3.0000000000000004]], [1, 4, 4, 4, 4, 4, 4], id='circle_boundary', edgecolor='#16A34A', linewidth=3.0, capstyle='butt', fill=False)
                c.path(self._samples_004, [1] + [4] * 12, id='circle_boundary', capstyle='butt', fill=False)
                c.path([[2.7189233611099506, 1.2678547852220985], [2.220446049250313e-16, 2.220446049250313e-16]], [1, 2], id='diameter', edgecolor='#16A34A', linewidth=3.0, joinstyle='round', fill=False)
                c.path([[2.220446049250313e-16, 2.220446049250313e-16], [-2.71892336110995, -1.267854785222098]], [1, 2], id='diameter', joinstyle='round', fill=False)
                c.line([[0.0, 0.0], [1.9283628290596182, 2.298133329356934]], id='radius_1')
                c.line([[0.0, 0.0], [1.8369701987210297e-16, 3.0]], id='radius_2', color='#16A34A', linewidth=3.0)
                c.line([[0.0, 0.0], [-2.1213203435596424, 2.121320343559643]], id='radius_3')
                c.line([[0.0, 0.0], [-2.954423259036624, 0.5209445330007908]], id='radius_4')
            self._draw_base(c, custom={2: _slot_2})
            return c.save(output_path)

    def draw_C04(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane136_C04.png'
        with Canvas(PLANE, xlim=(-3.1423632415275478, 3.142363241527546), ylim=(-3.142363241527547, 3.142363241527547)) as c:

            def _slot_2(c):
                c.path(self._samples_003, [1, 4, 4, 4, 4, 4, 4, 4, 4, 4], id='circle_boundary', capstyle='butt', fill=False)
                c.path([[2.7189141236784007, 1.267850477737024], [2.5723940950474593, 1.5820800908876425], [2.371163609261935, 1.8714770778573513], [2.1213203435596433, 2.121320343559643], [1.5587396123545612, 2.6839010747647256], [0.7956093000000006, 3.0000000000000004], [4.440892098500626e-16, 3.0000000000000004]], [1, 4, 4, 4, 4, 4, 4], id='circle_boundary', edgecolor='#EA580C', linewidth=3.0, capstyle='butt', fill=False)
                c.path(self._samples_004, [1] + [4] * 12, id='circle_boundary', capstyle='butt', fill=False)
                c.path([[2.7189233611099506, 1.2678547852220985], [2.220446049250313e-16, 2.220446049250313e-16]], [1, 2], id='diameter', edgecolor='#EA580C', linewidth=3.0, joinstyle='round', fill=False)
                c.path([[2.220446049250313e-16, 2.220446049250313e-16], [-2.71892336110995, -1.267854785222098]], [1, 2], id='diameter', joinstyle='round', fill=False)
                c.line([[0.0, 0.0], [1.9283628290596182, 2.298133329356934]], id='radius_1')
                c.line([[0.0, 0.0], [1.8369701987210297e-16, 3.0]], id='radius_2', color='#EA580C', linewidth=3.0)
                c.line([[0.0, 0.0], [-2.1213203435596424, 2.121320343559643]], id='radius_3')
                c.line([[0.0, 0.0], [-2.954423259036624, 0.5209445330007908]], id='radius_4')
            self._draw_base(c, custom={2: _slot_2})
            return c.save(output_path)

    def draw_C05(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane136_C05.png'
        with Canvas(PLANE, xlim=(-3.1423632415275478, 3.142363241527546), ylim=(-3.142363241527547, 3.142363241527547)) as c:

            def _slot_2(c):
                c.path(self._samples_005, [1] + [4] * 12, id='circle_boundary', capstyle='butt', fill=False)
                c.path([[1.9283668662024493, 2.298138140636406], [1.390250356173766, 2.7496942073997555], [0.707984568132886, 3.0000000000000004], [4.440892098500626e-16, 3.0000000000000004], [-0.7956092999999997, 3.0000000000000004], [-1.5587396123545603, 2.6839010747647256], [-2.1213203435596424, 2.121320343559643]], [1, 4, 4, 4, 4, 4, 4], id='circle_boundary', edgecolor='#DC2626', linewidth=3.0, capstyle='butt', fill=False)
                c.path(self._samples_006, [1, 4, 4, 4, 4, 4, 4, 4, 4, 4], id='circle_boundary', capstyle='butt', fill=False)
                c.line([[2.7189233611099497, 1.2678547852220983], [-2.71892336110995, -1.2678547852220978]], id='diameter')
                c.line([[0.0, 0.0], [1.9283628290596182, 2.298133329356934]], id='radius_1', color='#DC2626', linewidth=3.0)
                c.line([[0.0, 0.0], [1.8369701987210297e-16, 3.0]], id='radius_2')
                c.line([[0.0, 0.0], [-2.1213203435596424, 2.121320343559643]], id='radius_3', color='#DC2626', linewidth=3.0)
                c.line([[0.0, 0.0], [-2.954423259036624, 0.5209445330007908]], id='radius_4')
            self._draw_base(c, custom={2: _slot_2})
            return c.save(output_path)

    def draw_C06(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane136_C06.png'
        with Canvas(PLANE, xlim=(-3.1423632415275478, 3.142363241527546), ylim=(-3.142363241527547, 3.142363241527547)) as c:

            def _slot_2(c):
                c.path(self._samples_005, [1] + [4] * 12, id='circle_boundary', capstyle='butt', fill=False)
                c.path([[1.9283668662024493, 2.298138140636406], [1.390250356173766, 2.7496942073997555], [0.707984568132886, 3.0000000000000004], [4.440892098500626e-16, 3.0000000000000004], [-0.7956092999999997, 3.0000000000000004], [-1.5587396123545603, 2.6839010747647256], [-2.1213203435596424, 2.121320343559643]], [1, 4, 4, 4, 4, 4, 4], id='circle_boundary', edgecolor='#2563EB', linewidth=3.0, capstyle='butt', fill=False)
                c.path(self._samples_006, [1, 4, 4, 4, 4, 4, 4, 4, 4, 4], id='circle_boundary', capstyle='butt', fill=False)
                c.line([[2.7189233611099497, 1.2678547852220983], [-2.71892336110995, -1.2678547852220978]], id='diameter')
                c.line([[0.0, 0.0], [1.9283628290596182, 2.298133329356934]], id='radius_1', color='#2563EB', linewidth=3.0)
                c.line([[0.0, 0.0], [1.8369701987210297e-16, 3.0]], id='radius_2')
                c.line([[0.0, 0.0], [-2.1213203435596424, 2.121320343559643]], id='radius_3', color='#2563EB', linewidth=3.0)
                c.line([[0.0, 0.0], [-2.954423259036624, 0.5209445330007908]], id='radius_4')
            self._draw_base(c, custom={2: _slot_2})
            return c.save(output_path)
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Plane136')
    parser.add_argument('output', nargs='?')
    parser.add_argument('--variant', choices=('C01', 'C02', 'C03', 'C04', 'C05', 'C06'))
    args = parser.parse_args()
    print(Plane136().draw(args.output, variant=args.variant))
