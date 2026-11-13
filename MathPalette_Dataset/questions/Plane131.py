"""Collected question Plane131; construction on the shared drawing protocol."""
from pathlib import Path
import sys
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from MathPalette_Dataset.drawing import Canvas, PLANE
import numpy as np

class Plane131:
    variants = ('C01', 'C02', 'C03', 'C04', 'C05', 'C06')

    def __init__(self):
        _t = np.radians(np.linspace(70.0, 140.0, 281))
        self._samples_001 = [[0.0, 0.0], *np.column_stack([3.0 * np.cos(_t), 3.0 * np.sin(_t)]).tolist(), [0.0, 0.0]]
        self._samples_002 = [1] + [2] * 281 + [79]
        self._samples_003 = [
            [2.7189141236784002, 1.267850477737024], [2.572394095047459, 1.5820800908876425],
            [2.3711636092619344, 1.8714770778573513], [2.121320343559643, 2.121320343559643],
            [1.5587396123545605, 2.683901074764725], [0.7956093000000001, 3.0], [0.0, 3.0],
            [-0.7956093000000001, 3.0], [-1.5587396123545605, 2.683901074764725],
            [-2.121320343559643, 2.121320343559643], [-2.183280385662532, 2.0593603014567536],
            [-2.2422506523293424, 1.9949676326978019], [-2.2981381406364045, 1.9283668662024505]
        ]
        self._samples_004 = [
            [-2.2981381406364045, 1.9283668662024505], [-2.749694207399754, 1.3902503561737667],
            [-3.0, 0.7079845681328862], [-3.0, 0.0], [-3.0, -0.7956093000000001],
            [-2.683901074764725, -1.5587396123545605], [-2.121320343559643, -2.121320343559643],
            [-1.5587396123545605, -2.683901074764725], [-0.7956093000000001, -3.0], [0.0, -3.0]
        ]
        self._samples_005 = [
            [0.0, -3.0], [0.7956093000000001, -3.0], [1.5587396123545605, -2.683901074764725],
            [2.121320343559643, -2.121320343559643], [2.683901074764725, -1.5587396123545605],
            [3.0, -0.7956093000000001], [3.0, 0.0], [3.0, 0.7956093000000001],
            [2.683901074764725, 1.5587396123545605], [2.121320343559643, 2.121320343559643],
            [1.808582878056852, 2.4340578090624336], [1.433871077271473, 2.670626847801744],
            [1.0260569439784224, 2.819068284655329]
        ]
        self._samples_006 = [
            [1.0260569439784224, 2.819068284655329], [0.7002577478454088, 2.9376568691391713],
            [0.35333173482376534, 3.0], [0.0, 3.0], [-0.7956093000000001, 3.0],
            [-1.5587396123545605, 2.683901074764725], [-2.121320343559643, 2.121320343559643],
            [-2.683901074764724, 1.5587396123545616], [-2.999999999999999, 0.7956093000000027],
            [-3.0, 4.2398580646363365e-15]
        ]

    def _draw_base(self, c, custom=None):
        c.path(self._samples_001, self._samples_002, alpha=0.45, zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), capstyle='butt')
        c.path(self._samples_001, self._samples_002, id='shade', capstyle='butt', fill=False)
        if custom and 2 in custom:
            custom[2](c)
        else:
            c.path([[0.0, -3.0], [0.7956093000000001, -3.0], [1.5587396123545605, -2.683901074764725], [2.121320343559643, -2.121320343559643], [2.683901074764725, -1.5587396123545605], [3.0, -0.7956093000000001], [3.0, 0.0], [3.0, 0.44227756517623473], [2.9023183161853856, 0.8745183920135485], [2.7189141236784002, 1.267850477737024]], [1, 4, 4, 4, 4, 4, 4, 4, 4, 4], id='circle_boundary', capstyle='butt', fill=False)
            c.path(self._samples_003, [1] + [4] * 12, id='circle_boundary', edgecolor='#DC2626', linewidth=3.0, capstyle='butt', fill=False)
            c.path(self._samples_004, [1, 4, 4, 4, 4, 4, 4, 4, 4, 4], id='circle_boundary', capstyle='butt', fill=False)
            c.line([[3.0, 0.0], [-3.0, 3.6739403974420594e-16]], id='diameter')
            c.line([[0.0, 0.0], [2.7189233611099497, 1.2678547852220983]], id='radius_1', color='#DC2626', linewidth=3.0)
            c.line([[0.0, 0.0], [1.0260604299770064, 2.819077862357725]], id='radius_2')
            c.line([[0.0, 0.0], [-2.2981333293569337, 1.9283628290596184]], id='radius_3', color='#DC2626', linewidth=3.0)
        c.point([[0.0, 0.0]], id='center_dot')
        for object_id, vertices, codes in [('angle_arc_0', [[0.5897957822723641, 0.0], [0.5897957822723641, 0.042933645676274064], [0.5851078089438146, 0.08573922457250352], [0.5758152672486866, 0.1276551714173519], [0.5665227255535585, 0.16957111826220025], [0.5526810529407141, 0.21034737088366298], [0.5345365102348161, 0.24925846828594256]], [1, 4, 4, 4, 4, 4, 4]), ('angle_arc_1', [[0.7508965262822416, 0.35014880068739546], [0.7049154070724237, 0.44875562904562477], [0.639958001231089, 0.5373463523543495], [0.5597417867804143, 0.6108509703171696], [0.4795255723297395, 0.6843555882799898], [0.3856105525164127, 0.741344621290397], [0.28337143431320155, 0.7785566170939897]], [1, 4, 4, 4, 4, 4, 4]), ('angle_arc_3', [[-0.6454425451210786, 0.5415906015572222], [-0.7086190071946068, 0.4662998259137033], [-0.7581369986188315, 0.380532148878186], [-0.7917524919599895, 0.28817433997952707], [-0.8253679853011476, 0.19581653108086813], [-0.8425654032462343, 0.09828512734453093], [-0.8425654032462343, 1.0318450241577997e-16]], [1, 4, 4, 4, 4, 4, 4])]:
            c.path(vertices, codes, id=object_id, zorder=3, capstyle='butt', fill=False)
        c.text('B', (3.0, 0.0), id='label_B', fontsize=18.0, fontstyle='italic', offset_pt=(18.0, 0.0))
        c.text('A', (-3.0, 3.6739403974420594e-16), id='label_A', fontsize=18.0, fontstyle='italic', offset_pt=(-18.0, 2.204364238465236e-15))
        c.text('O', (0.0, 0.0), id='label_O', fontsize=18.0, fontstyle='italic', offset_pt=(8.572527594031472e-16, -14.0))
        c.text('25°', (0.0, 0.0), id='angle_label_0', offset_pt=(80.05627258383453, 17.748048342924434))
        c.text('45°', (0.0, 0.0), id='angle_label_1', offset_pt=(64.8566599311034, 70.7786243337719))
        c.text('40°', (0.0, 0.0), id='angle_label_3', offset_pt=(-92.08987683701902, 33.51797404591555))

    def draw(self, output_path=None, *, variant=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / (self.__class__.__name__ + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if variant not in self.variants:
                raise ValueError('Unknown Special variant: ' + str(variant))
            return getattr(self, 'draw_' + variant)(output_path)
        with Canvas(PLANE, xlim=(-3.4942872403427834, 3.4942872403427825), ylim=(-3.4942872403427834, 3.4942872403427825)) as c:

            def _slot_2(c):
                c.circle([0.0, 0.0], 3.0, id='circle_boundary', fill=False)
                for object_id, points in [('diameter', [[3.0, 0.0], [-3.0, 3.6739403974420594e-16]]), ('radius_1', [[0.0, 0.0], [2.7189233611099497, 1.2678547852220983]]), ('radius_2', [[0.0, 0.0], [1.0260604299770064, 2.819077862357725]]), ('radius_3', [[0.0, 0.0], [-2.2981333293569337, 1.9283628290596184]])]:
                    c.line(points, id=object_id)
            self._draw_base(c, custom={2: _slot_2})
            return c.save(output_path)

    def draw_C01(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane131_C01.png'
        with Canvas(PLANE, xlim=(-3.4942872403427834, 3.4942872403427825), ylim=(-3.4942872403427834, 3.4942872403427825)) as c:
            self._draw_base(c)
            return c.save(output_path)

    def draw_C02(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane131_C02.png'
        with Canvas(PLANE, xlim=(-3.4942872403427834, 3.4942872403427825), ylim=(-3.4942872403427834, 3.4942872403427825)) as c:

            def _slot_2(c):
                c.path([[0.0, -3.0], [0.7956093000000001, -3.0], [1.5587396123545605, -2.683901074764725], [2.121320343559643, -2.121320343559643], [2.683901074764725, -1.5587396123545605], [3.0, -0.7956093000000001], [3.0, 0.0], [3.0, 0.44227756517623473], [2.9023183161853856, 0.8745183920135485], [2.7189141236784002, 1.267850477737024]], [1, 4, 4, 4, 4, 4, 4, 4, 4, 4], id='circle_boundary', capstyle='butt', fill=False)
                c.path(self._samples_003, [1] + [4] * 12, id='circle_boundary', edgecolor='#2563EB', linewidth=3.0, capstyle='butt', fill=False)
                c.path(self._samples_004, [1, 4, 4, 4, 4, 4, 4, 4, 4, 4], id='circle_boundary', capstyle='butt', fill=False)
                c.line([[3.0, 0.0], [-3.0, 3.6739403974420594e-16]], id='diameter')
                c.line([[0.0, 0.0], [2.7189233611099497, 1.2678547852220983]], id='radius_1', color='#2563EB', linewidth=3.0)
                c.line([[0.0, 0.0], [1.0260604299770064, 2.819077862357725]], id='radius_2')
                c.line([[0.0, 0.0], [-2.2981333293569337, 1.9283628290596184]], id='radius_3', color='#2563EB', linewidth=3.0)
            self._draw_base(c, custom={2: _slot_2})
            return c.save(output_path)

    def draw_C03(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane131_C03.png'
        with Canvas(PLANE, xlim=(-3.4942872403427834, 3.4942872403427825), ylim=(-3.4942872403427834, 3.4942872403427825)) as c:

            def _slot_2(c):
                c.path([[0.0, -3.0], [0.7956093000000001, -3.0], [1.5587396123545605, -2.683901074764725], [2.121320343559643, -2.121320343559643], [2.683901074764725, -1.5587396123545605], [3.0, -0.7956093000000001], [3.0, 0.0], [3.0, 0.44227756517623473], [2.9023183161853856, 0.8745183920135485], [2.7189141236784002, 1.267850477737024]], [1, 4, 4, 4, 4, 4, 4, 4, 4, 4], id='circle_boundary', capstyle='butt', fill=False)
                c.path(self._samples_003, [1] + [4] * 12, id='circle_boundary', edgecolor='#16A34A', linewidth=3.0, capstyle='butt', fill=False)
                c.path(self._samples_004, [1, 4, 4, 4, 4, 4, 4, 4, 4, 4], id='circle_boundary', capstyle='butt', fill=False)
                c.line([[3.0, 0.0], [-3.0, 3.6739403974420594e-16]], id='diameter')
                c.line([[0.0, 0.0], [2.7189233611099497, 1.2678547852220983]], id='radius_1', color='#16A34A', linewidth=3.0)
                c.line([[0.0, 0.0], [1.0260604299770064, 2.819077862357725]], id='radius_2')
                c.line([[0.0, 0.0], [-2.2981333293569337, 1.9283628290596184]], id='radius_3', color='#16A34A', linewidth=3.0)
            self._draw_base(c, custom={2: _slot_2})
            return c.save(output_path)

    def draw_C04(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane131_C04.png'
        with Canvas(PLANE, xlim=(-3.4942872403427834, 3.4942872403427825), ylim=(-3.4942872403427834, 3.4942872403427825)) as c:

            def _slot_2(c):
                c.path(self._samples_005, [1] + [4] * 12, id='circle_boundary', capstyle='butt', fill=False)
                c.path(self._samples_006, [1, 4, 4, 4, 4, 4, 4, 4, 4, 4], id='circle_boundary', edgecolor='#DC2626', linewidth=3.0, capstyle='butt', fill=False)
                c.path([[-3.0, 4.2398580646363365e-15], [-3.0, 2.8265720430908913e-15], [-3.0, 1.4132860215454458e-15], [-3.0, 0.0], [-3.0, -0.7956093000000001], [-2.683901074764725, -1.5587396123545605], [-2.121320343559643, -2.121320343559643], [-1.5587396123545605, -2.683901074764725], [-0.7956093000000001, -3.0], [0.0, -3.0]], [1, 4, 4, 4, 4, 4, 4, 4, 4, 4], id='circle_boundary', capstyle='butt', fill=False)
                c.path([[3.0, 0.0], [0.0, 1.8369701987210297e-16]], [1, 2], id='diameter', joinstyle='round', fill=False)
                c.path([[0.0, 1.8369701987210297e-16], [-3.0, 3.6739403974420594e-16]], [1, 2], id='diameter', edgecolor='#DC2626', linewidth=3.0, joinstyle='round', fill=False)
                c.line([[0.0, 0.0], [2.7189233611099497, 1.2678547852220983]], id='radius_1')
                c.line([[0.0, 0.0], [1.0260604299770064, 2.819077862357725]], id='radius_2', color='#DC2626', linewidth=3.0)
                c.line([[0.0, 0.0], [-2.2981333293569337, 1.9283628290596184]], id='radius_3')
            self._draw_base(c, custom={2: _slot_2})
            return c.save(output_path)

    def draw_C05(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane131_C05.png'
        with Canvas(PLANE, xlim=(-3.4942872403427834, 3.4942872403427825), ylim=(-3.4942872403427834, 3.4942872403427825)) as c:

            def _slot_2(c):
                c.path(self._samples_005, [1] + [4] * 12, id='circle_boundary', capstyle='butt', fill=False)
                c.path(self._samples_006, [1, 4, 4, 4, 4, 4, 4, 4, 4, 4], id='circle_boundary', edgecolor='#2563EB', linewidth=3.0, capstyle='butt', fill=False)
                c.path([[-3.0, 4.2398580646363365e-15], [-3.0, 2.8265720430908913e-15], [-3.0, 1.4132860215454458e-15], [-3.0, 0.0], [-3.0, -0.7956093000000001], [-2.683901074764725, -1.5587396123545605], [-2.121320343559643, -2.121320343559643], [-1.5587396123545605, -2.683901074764725], [-0.7956093000000001, -3.0], [0.0, -3.0]], [1, 4, 4, 4, 4, 4, 4, 4, 4, 4], id='circle_boundary', capstyle='butt', fill=False)
                c.path([[3.0, 0.0], [0.0, 1.8369701987210297e-16]], [1, 2], id='diameter', joinstyle='round', fill=False)
                c.path([[0.0, 1.8369701987210297e-16], [-3.0, 3.6739403974420594e-16]], [1, 2], id='diameter', edgecolor='#2563EB', linewidth=3.0, joinstyle='round', fill=False)
                c.line([[0.0, 0.0], [2.7189233611099497, 1.2678547852220983]], id='radius_1')
                c.line([[0.0, 0.0], [1.0260604299770064, 2.819077862357725]], id='radius_2', color='#2563EB', linewidth=3.0)
                c.line([[0.0, 0.0], [-2.2981333293569337, 1.9283628290596184]], id='radius_3')
            self._draw_base(c, custom={2: _slot_2})
            return c.save(output_path)

    def draw_C06(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane131_C06.png'
        with Canvas(PLANE, xlim=(-3.4942872403427834, 3.4942872403427825), ylim=(-3.4942872403427834, 3.4942872403427825)) as c:

            def _slot_2(c):
                c.path(self._samples_005, [1] + [4] * 12, id='circle_boundary', capstyle='butt', fill=False)
                c.path(self._samples_006, [1, 4, 4, 4, 4, 4, 4, 4, 4, 4], id='circle_boundary', edgecolor='#16A34A', linewidth=3.0, capstyle='butt', fill=False)
                c.path([[-3.0, 4.2398580646363365e-15], [-3.0, 2.8265720430908913e-15], [-3.0, 1.4132860215454458e-15], [-3.0, 0.0], [-3.0, -0.7956093000000001], [-2.683901074764725, -1.5587396123545605], [-2.121320343559643, -2.121320343559643], [-1.5587396123545605, -2.683901074764725], [-0.7956093000000001, -3.0], [0.0, -3.0]], [1, 4, 4, 4, 4, 4, 4, 4, 4, 4], id='circle_boundary', capstyle='butt', fill=False)
                c.path([[3.0, 0.0], [0.0, 1.8369701987210297e-16]], [1, 2], id='diameter', joinstyle='round', fill=False)
                c.path([[0.0, 1.8369701987210297e-16], [-3.0, 3.6739403974420594e-16]], [1, 2], id='diameter', edgecolor='#16A34A', linewidth=3.0, joinstyle='round', fill=False)
                c.line([[0.0, 0.0], [2.7189233611099497, 1.2678547852220983]], id='radius_1')
                c.line([[0.0, 0.0], [1.0260604299770064, 2.819077862357725]], id='radius_2', color='#16A34A', linewidth=3.0)
                c.line([[0.0, 0.0], [-2.2981333293569337, 1.9283628290596184]], id='radius_3')
            self._draw_base(c, custom={2: _slot_2})
            return c.save(output_path)
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Plane131')
    parser.add_argument('output', nargs='?')
    parser.add_argument('--variant', choices=('C01', 'C02', 'C03', 'C04', 'C05', 'C06'))
    args = parser.parse_args()
    print(Plane131().draw(args.output, variant=args.variant))
