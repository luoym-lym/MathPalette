"""Collected question Plane135; construction on the shared drawing protocol."""
from pathlib import Path
import sys
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from MathPalette_Dataset.drawing import Canvas, PLANE
import numpy as np

class Plane135:
    variants = ('C01', 'C02', 'C03', 'C04', 'C05', 'C06')

    def __init__(self):
        _t = np.radians(np.linspace(130.0, 195.0, 261))
        self._samples_001 = [[0.0, 0.0], *np.column_stack([3.0 * np.cos(_t), 3.0 * np.sin(_t)]).tolist(), [0.0, 0.0]]
        self._samples_002 = [1] + [2] * 261 + [79]
        self._samples_003 = [
            [4.440892098500626e-16, -2.9999999999999996], [0.7956093000000005, -2.9999999999999996],
            [1.558739612354561, -2.6839010747647247], [2.1213203435596433, -2.1213203435596424],
            [2.6839010747647256, -1.55873961235456], [3.0000000000000004, -0.7956092999999996],
            [3.0000000000000004, 4.440892098500626e-16], [3.0000000000000004, 0.7956093000000005],
            [2.6839010747647256, 1.558739612354561], [2.1213203435596433, 2.1213203435596433],
            [1.558739612354561, 2.6839010747647256], [0.7956093000000005, 3.0000000000000004],
            [4.440892098500626e-16, 3.0000000000000004]
        ]
        self._samples_004 = [
            [4.440892098500626e-16, 3.0000000000000004], [-0.7956092999999996, 3.0000000000000004],
            [-1.55873961235456, 2.6839010747647256], [-2.1213203435596424, 2.1213203435596433],
            [-2.6839010747647247, 1.558739612354561], [-2.9999999999999996, 0.7956093000000005],
            [-2.9999999999999996, 4.440892098500626e-16], [-2.9999999999999996, -0.2644653217785484],
            [-2.9650730403095693, -0.5253419179977367], [-2.897776073627158, -0.776456758774623]
        ]
        self._samples_005 = [
            [4.440892098500626e-16, -2.9999999999999996], [0.7956093000000005, -2.9999999999999996],
            [1.558739612354561, -2.6839010747647247], [2.1213203435596433, -2.1213203435596424],
            [2.6839010747647256, -1.55873961235456], [3.0000000000000004, -0.7956092999999996],
            [3.0000000000000004, 4.440892098500626e-16], [3.0000000000000004, 0.7956093000000005],
            [2.6839010747647256, 1.558739612354561], [2.1213203435596433, 2.1213203435596433],
            [1.558739612354561, 2.6839010747647256], [0.7956093000000005, 3.0000000000000004],
            [4.440892098500626e-16, 3.0000000000000004], [-0.7079845681328844, 3.0000000000000004],
            [-1.3902503561737636, 2.749694207399756], [-1.928366866202447, 2.2981381406364076]
        ]
        self._samples_006 = [
            [-1.928366866202447, 2.2981381406364076], [-1.9949676326977994, 2.2422506523293446],
            [-2.0593603014567523, 2.1832803856625334], [-2.1213203435596424, 2.1213203435596433],
            [-2.6839010747647247, 1.558739612354561], [-2.9999999999999996, 0.7956093000000005],
            [-2.9999999999999996, 4.440892098500626e-16], [-2.9999999999999996, -0.7956092999999996],
            [-2.6839010747647247, -1.55873961235456], [-2.1213203435596424, -2.1213203435596424]
        ]

    def _draw_base(self, c, custom=None):
        c.path(self._samples_001, self._samples_002, alpha=0.45, zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), capstyle='butt')
        c.path(self._samples_001, self._samples_002, id='shade', capstyle='butt', fill=False)
        if custom and 2 in custom:
            custom[2](c)
        else:
            c.path(self._samples_003, [1] + [4] * 12, id='circle_boundary', capstyle='butt', fill=False)
            c.path(self._samples_004, [1, 4, 4, 4, 4, 4, 4, 4, 4, 4], id='circle_boundary', edgecolor='#DC2626', linewidth=3.0, capstyle='butt', fill=False)
            c.path([[-2.897776073627158, -0.776456758774623], [-2.7626189257427063, -1.2807880435861962], [-2.4968958523464306, -1.7457448347728541], [-2.1213203435596424, -2.1213203435596424], [-1.55873961235456, -2.6839010747647247], [-0.7956092999999996, -2.9999999999999996], [4.440892098500626e-16, -2.9999999999999996]], [1, 4, 4, 4, 4, 4, 4], id='circle_boundary', capstyle='butt', fill=False)
            c.path([[6.277862297221655e-16, 3.0000000000000004], [2.603921899779596e-16, 4.440892098500626e-16]], [1, 2], id='diameter', edgecolor='#DC2626', linewidth=3.0, joinstyle='round', fill=False)
            c.path([[2.603921899779596e-16, 4.440892098500626e-16], [-1.0700184976624634e-16, -2.9999999999999996]], [1, 2], id='diameter', joinstyle='round', fill=False)
            c.line([[0.0, 0.0], [-1.9283628290596182, 2.298133329356934]], id='radius_1')
            c.line([[0.0, 0.0], [-2.897777478867205, -0.7764571353075624]], id='radius_2', color='#DC2626', linewidth=3.0)
            c.line([[0.0, 0.0], [-2.121320343559643, -2.1213203435596424]], id='radius_3')
        c.point([[0.0, 0.0]], id='center_dot')
        for object_id, vertices, codes in [('angle_arc_0', [[3.6608607428365405e-17, 0.5978639302998014], [-0.06974073739299393, 0.5978639302998014], [-0.13894665083402138, 0.5856610605355738], [-0.2044815071303857, 0.5618083235367841], [-0.27001636342675, 0.5379555865379945], [-0.33087502233628624, 0.5028188234340542], [-0.38429952667520917, 0.4579903415474349]], [1, 4, 4, 4, 4, 4, 4]), ('angle_arc_2', [[-0.6049918399729449, -0.16210707494816964], [-0.5908251598093998, -0.21497784509309834], [-0.5697887690670531, -0.2657641849266513], [-0.5424208445815626, -0.31316682063322937], [-0.515052920096072, -0.3605694563398074], [-0.48158885500615894, -0.4041806750433917], [-0.4428847650247754, -0.44288476502477525]], [1, 4, 4, 4, 4, 4, 4]), ('angle_arc_3', [[-0.6039337704883301, -0.6039337704883299], [-0.5246259143964549, -0.6832416265802053], [-0.43046730892826257, -0.7461563953303225], [-0.32684660133487303, -0.7890774977582014], [-0.22322589374148352, -0.8319986001860801], [-0.11215824568786383, -0.8540913289997163], [-1.5689403183585173e-16, -0.8540913289997163]], [1, 4, 4, 4, 4, 4, 4])]:
            c.path(vertices, codes, id=object_id, zorder=3, capstyle='butt', fill=False)
        c.text('B', (1.8369701987210297e-16, 3.0), id='label_B', fontsize=18.0, fontstyle='italic', offset_pt=(1.102182119232618e-15, 18.0))
        c.text('A', (-5.51091059616309e-16, -3.0), id='label_A', fontsize=18.0, fontstyle='italic', offset_pt=(-3.3065463576978533e-15, -18.0))
        c.text('O', (0.0, 0.0), id='label_O', fontsize=18.0, fontstyle='italic', offset_pt=(14.0, 0.0))
        c.text('40°', (0.0, 0.0), id='angle_label_0', offset_pt=(-28.04565175270483, 77.05479490444449))
        c.text('30°', (0.0, 0.0), id='angle_label_2', offset_pt=(-71.01408311032397, -41.0))
        c.text('45°', (0.0, 0.0), id='angle_label_3', offset_pt=(-37.50297637177881, -90.54019418610609))

    def draw(self, output_path=None, *, variant=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / (self.__class__.__name__ + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if variant not in self.variants:
                raise ValueError('Unknown Special variant: ' + str(variant))
            return getattr(self, 'draw_' + variant)(output_path)
        with Canvas(PLANE, xlim=(-3.5420875596276233, 3.5420875596276242), ylim=(-3.5420875596276233, 3.5420875596276242)) as c:

            def _slot_2(c):
                c.circle([0.0, 0.0], 3.0, id='circle_boundary', fill=False)
                for object_id, points in [('diameter', [[1.8369701987210297e-16, 3.0], [-5.51091059616309e-16, -3.0]]), ('radius_1', [[0.0, 0.0], [-1.9283628290596182, 2.298133329356934]]), ('radius_2', [[0.0, 0.0], [-2.897777478867205, -0.7764571353075624]]), ('radius_3', [[0.0, 0.0], [-2.121320343559643, -2.1213203435596424]])]:
                    c.line(points, id=object_id)
            self._draw_base(c, custom={2: _slot_2})
            return c.save(output_path)

    def draw_C01(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane135_C01.png'
        with Canvas(PLANE, xlim=(-3.5420875596276233, 3.5420875596276242), ylim=(-3.5420875596276233, 3.5420875596276242)) as c:
            self._draw_base(c)
            return c.save(output_path)

    def draw_C02(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane135_C02.png'
        with Canvas(PLANE, xlim=(-3.5420875596276233, 3.5420875596276242), ylim=(-3.5420875596276233, 3.5420875596276242)) as c:

            def _slot_2(c):
                c.path(self._samples_003, [1] + [4] * 12, id='circle_boundary', capstyle='butt', fill=False)
                c.path(self._samples_004, [1, 4, 4, 4, 4, 4, 4, 4, 4, 4], id='circle_boundary', edgecolor='#2563EB', linewidth=3.0, capstyle='butt', fill=False)
                c.path([[-2.897776073627158, -0.776456758774623], [-2.7626189257427063, -1.2807880435861962], [-2.4968958523464306, -1.7457448347728541], [-2.1213203435596424, -2.1213203435596424], [-1.55873961235456, -2.6839010747647247], [-0.7956092999999996, -2.9999999999999996], [4.440892098500626e-16, -2.9999999999999996]], [1, 4, 4, 4, 4, 4, 4], id='circle_boundary', capstyle='butt', fill=False)
                c.path([[6.277862297221655e-16, 3.0000000000000004], [2.603921899779596e-16, 4.440892098500626e-16]], [1, 2], id='diameter', edgecolor='#2563EB', linewidth=3.0, joinstyle='round', fill=False)
                c.path([[2.603921899779596e-16, 4.440892098500626e-16], [-1.0700184976624634e-16, -2.9999999999999996]], [1, 2], id='diameter', joinstyle='round', fill=False)
                c.line([[0.0, 0.0], [-1.9283628290596182, 2.298133329356934]], id='radius_1')
                c.line([[0.0, 0.0], [-2.897777478867205, -0.7764571353075624]], id='radius_2', color='#2563EB', linewidth=3.0)
                c.line([[0.0, 0.0], [-2.121320343559643, -2.1213203435596424]], id='radius_3')
            self._draw_base(c, custom={2: _slot_2})
            return c.save(output_path)

    def draw_C03(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane135_C03.png'
        with Canvas(PLANE, xlim=(-3.5420875596276233, 3.5420875596276242), ylim=(-3.5420875596276233, 3.5420875596276242)) as c:

            def _slot_2(c):
                c.path(self._samples_003, [1] + [4] * 12, id='circle_boundary', capstyle='butt', fill=False)
                c.path(self._samples_004, [1, 4, 4, 4, 4, 4, 4, 4, 4, 4], id='circle_boundary', edgecolor='#16A34A', linewidth=3.0, capstyle='butt', fill=False)
                c.path([[-2.897776073627158, -0.776456758774623], [-2.7626189257427063, -1.2807880435861962], [-2.4968958523464306, -1.7457448347728541], [-2.1213203435596424, -2.1213203435596424], [-1.55873961235456, -2.6839010747647247], [-0.7956092999999996, -2.9999999999999996], [4.440892098500626e-16, -2.9999999999999996]], [1, 4, 4, 4, 4, 4, 4], id='circle_boundary', capstyle='butt', fill=False)
                c.path([[6.277862297221655e-16, 3.0000000000000004], [2.603921899779596e-16, 4.440892098500626e-16]], [1, 2], id='diameter', edgecolor='#16A34A', linewidth=3.0, joinstyle='round', fill=False)
                c.path([[2.603921899779596e-16, 4.440892098500626e-16], [-1.0700184976624634e-16, -2.9999999999999996]], [1, 2], id='diameter', joinstyle='round', fill=False)
                c.line([[0.0, 0.0], [-1.9283628290596182, 2.298133329356934]], id='radius_1')
                c.line([[0.0, 0.0], [-2.897777478867205, -0.7764571353075624]], id='radius_2', color='#16A34A', linewidth=3.0)
                c.line([[0.0, 0.0], [-2.121320343559643, -2.1213203435596424]], id='radius_3')
            self._draw_base(c, custom={2: _slot_2})
            return c.save(output_path)

    def draw_C04(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane135_C04.png'
        with Canvas(PLANE, xlim=(-3.5420875596276233, 3.5420875596276242), ylim=(-3.5420875596276233, 3.5420875596276242)) as c:

            def _slot_2(c):
                c.path(self._samples_003, [1] + [4] * 12, id='circle_boundary', capstyle='butt', fill=False)
                c.path(self._samples_004, [1, 4, 4, 4, 4, 4, 4, 4, 4, 4], id='circle_boundary', edgecolor='#EA580C', linewidth=3.0, capstyle='butt', fill=False)
                c.path([[-2.897776073627158, -0.776456758774623], [-2.7626189257427063, -1.2807880435861962], [-2.4968958523464306, -1.7457448347728541], [-2.1213203435596424, -2.1213203435596424], [-1.55873961235456, -2.6839010747647247], [-0.7956092999999996, -2.9999999999999996], [4.440892098500626e-16, -2.9999999999999996]], [1, 4, 4, 4, 4, 4, 4], id='circle_boundary', capstyle='butt', fill=False)
                c.path([[6.277862297221655e-16, 3.0000000000000004], [2.603921899779596e-16, 4.440892098500626e-16]], [1, 2], id='diameter', edgecolor='#EA580C', linewidth=3.0, joinstyle='round', fill=False)
                c.path([[2.603921899779596e-16, 4.440892098500626e-16], [-1.0700184976624634e-16, -2.9999999999999996]], [1, 2], id='diameter', joinstyle='round', fill=False)
                c.line([[0.0, 0.0], [-1.9283628290596182, 2.298133329356934]], id='radius_1')
                c.line([[0.0, 0.0], [-2.897777478867205, -0.7764571353075624]], id='radius_2', color='#EA580C', linewidth=3.0)
                c.line([[0.0, 0.0], [-2.121320343559643, -2.1213203435596424]], id='radius_3')
            self._draw_base(c, custom={2: _slot_2})
            return c.save(output_path)

    def draw_C05(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane135_C05.png'
        with Canvas(PLANE, xlim=(-3.5420875596276233, 3.5420875596276242), ylim=(-3.5420875596276233, 3.5420875596276242)) as c:

            def _slot_2(c):
                c.path(self._samples_005, [1] + [4] * 15, id='circle_boundary', capstyle='butt', fill=False)
                c.path(self._samples_006, [1, 4, 4, 4, 4, 4, 4, 4, 4, 4], id='circle_boundary', edgecolor='#DC2626', linewidth=3.0, capstyle='butt', fill=False)
                c.path([[-2.1213203435596424, -2.1213203435596424], [-1.55873961235456, -2.6839010747647247], [-0.7956092999999996, -2.9999999999999996], [4.440892098500626e-16, -2.9999999999999996]], [1, 4, 4, 4], id='circle_boundary', capstyle='butt', fill=False)
                c.line([[1.8369701987210297e-16, 3.0], [-5.51091059616309e-16, -3.0]], id='diameter')
                c.line([[0.0, 0.0], [-1.9283628290596182, 2.298133329356934]], id='radius_1', color='#DC2626', linewidth=3.0)
                c.line([[0.0, 0.0], [-2.897777478867205, -0.7764571353075624]], id='radius_2')
                c.line([[0.0, 0.0], [-2.121320343559643, -2.1213203435596424]], id='radius_3', color='#DC2626', linewidth=3.0)
            self._draw_base(c, custom={2: _slot_2})
            return c.save(output_path)

    def draw_C06(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane135_C06.png'
        with Canvas(PLANE, xlim=(-3.5420875596276233, 3.5420875596276242), ylim=(-3.5420875596276233, 3.5420875596276242)) as c:

            def _slot_2(c):
                c.path(self._samples_005, [1] + [4] * 15, id='circle_boundary', capstyle='butt', fill=False)
                c.path(self._samples_006, [1, 4, 4, 4, 4, 4, 4, 4, 4, 4], id='circle_boundary', edgecolor='#2563EB', linewidth=3.0, capstyle='butt', fill=False)
                c.path([[-2.1213203435596424, -2.1213203435596424], [-1.55873961235456, -2.6839010747647247], [-0.7956092999999996, -2.9999999999999996], [4.440892098500626e-16, -2.9999999999999996]], [1, 4, 4, 4], id='circle_boundary', capstyle='butt', fill=False)
                c.line([[1.8369701987210297e-16, 3.0], [-5.51091059616309e-16, -3.0]], id='diameter')
                c.line([[0.0, 0.0], [-1.9283628290596182, 2.298133329356934]], id='radius_1', color='#2563EB', linewidth=3.0)
                c.line([[0.0, 0.0], [-2.897777478867205, -0.7764571353075624]], id='radius_2')
                c.line([[0.0, 0.0], [-2.121320343559643, -2.1213203435596424]], id='radius_3', color='#2563EB', linewidth=3.0)
            self._draw_base(c, custom={2: _slot_2})
            return c.save(output_path)
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Plane135')
    parser.add_argument('output', nargs='?')
    parser.add_argument('--variant', choices=('C01', 'C02', 'C03', 'C04', 'C05', 'C06'))
    args = parser.parse_args()
    print(Plane135().draw(args.output, variant=args.variant))
