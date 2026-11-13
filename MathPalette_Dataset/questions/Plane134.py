"""Collected question Plane134; construction on the shared drawing protocol."""
from pathlib import Path
import sys
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from MathPalette_Dataset.drawing import Canvas, PLANE
import numpy as np

class Plane134:
    variants = ('C01', 'C02', 'C03', 'C04', 'C05', 'C06')

    def __init__(self):
        _t = np.radians(np.linspace(85.0, 140.0, 221))
        self._samples_001 = [[0.0, 0.0], *np.column_stack([3.0 * np.cos(_t), 3.0 * np.sin(_t)]).tolist(), [0.0, 0.0]]
        self._samples_002 = [1] + [2] * 221 + [79]
        self._samples_003 = [
            [0.0, -3.0], [0.7956093000000001, -3.0], [1.5587396123545605, -2.683901074764725],
            [2.121320343559643, -2.121320343559643], [2.683901074764725, -1.5587396123545605],
            [3.0, -0.7956093000000001], [3.0, 0.0], [3.0, 0.7956093000000001],
            [2.683901074764725, 1.5587396123545605], [2.121320343559643, 2.121320343559643],
            [2.059360301456753, 2.1832803856625325], [1.9949676326978008, 2.2422506523293433],
            [1.928366866202449, 2.298138140636406]
        ]
        self._samples_004 = [
            [1.928366866202449, 2.298138140636406], [1.3902503561737656, 2.749694207399755],
            [0.7079845681328855, 3.0], [0.0, 3.0], [-0.7956093000000001, 3.0],
            [-1.5587396123545605, 2.683901074764725], [-2.121320343559643, 2.121320343559643],
            [-2.183280385662532, 2.0593603014567536], [-2.2422506523293424, 1.9949676326978019],
            [-2.2981381406364045, 1.9283668662024505]
        ]
        self._samples_005 = [
            [-2.2981381406364045, 1.9283668662024505], [-2.749694207399754, 1.3902503561737667],
            [-3.0, 0.7079845681328862], [-3.0, 0.0], [-3.0, -0.7956093000000001],
            [-2.683901074764725, -1.5587396123545605], [-2.121320343559643, -2.121320343559643],
            [-1.5587396123545605, -2.683901074764725], [-0.7956093000000001, -3.0], [0.0, -3.0]
        ]
        self._samples_006 = [
            [0.0, -3.0], [0.7956093000000001, -3.0], [1.5587396123545605, -2.683901074764725],
            [2.121320343559643, -2.121320343559643], [2.683901074764725, -1.5587396123545605],
            [3.0, -0.7956093000000001], [3.0, 0.0], [3.0, 0.7956093000000001],
            [2.683901074764725, 1.5587396123545605], [2.121320343559643, 2.121320343559643],
            [1.6206996544574506, 2.621941032661835], [0.9612719658442546, 2.927382874639217],
            [0.261467775640245, 2.9885903510546488]
        ]
        self._samples_007 = [
            [0.261467775640245, 2.9885903510546488], [0.17485550005375133, 2.9961657827103263],
            [0.0876247318671153, 3.0], [0.0, 3.0], [-0.7956093000000001, 3.0],
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
            c.path(self._samples_003, [1] + [4] * 12, id='circle_boundary', capstyle='butt', fill=False)
            c.path(self._samples_004, [1, 4, 4, 4, 4, 4, 4, 4, 4, 4], id='circle_boundary', edgecolor='#2563EB', linewidth=3.0, capstyle='butt', fill=False)
            c.path(self._samples_005, [1, 4, 4, 4, 4, 4, 4, 4, 4, 4], id='circle_boundary', capstyle='butt', fill=False)
            c.line([[3.0, 0.0], [-3.0, 3.6739403974420594e-16]], id='diameter')
            c.line([[0.0, 0.0], [2.8190778623577253, 1.0260604299770062]], id='radius_1')
            c.line([[0.0, 0.0], [1.9283628290596182, 2.298133329356934]], id='radius_2', color='#2563EB', linewidth=3.0)
            c.line([[0.0, 0.0], [0.2614672282429744, 2.988584094275237]], id='radius_3')
            c.line([[0.0, 0.0], [-2.2981333293569337, 1.9283628290596184]], id='radius_4', color='#2563EB', linewidth=3.0)
        c.point([[0.0, 0.0]], id='center_dot')
        for object_id, vertices, codes in [('angle_arc_0', [[0.5897957822723641, 0.0], [0.5897957822723641, 0.03433468880752151], [0.5867976152179116, 0.06860389505232897], [0.5808354590757243, 0.10241696278723764], [0.5748733029335371, 0.1362300305221463], [0.5659698995589836, 0.16945798427626038], [0.5542267443719928, 0.20172203798566885]], [1, 4, 4, 4, 4, 4, 4]), ('angle_arc_1', [[0.7785566170939898, 0.28337143431320144], [0.7537925376811467, 0.35141018331356877], [0.720216007556443, 0.4159100975688335], [0.6786860196410593, 0.47522106703021283], [0.6371560317256757, 0.5345320364915922], [0.5880297879043094, 0.588143923999451], [0.5325640915312684, 0.6346851693690607]], [1, 4, 4, 4, 4, 4, 4]), ('angle_arc_2', [[0.39716644114196287, 0.4733245330887911], [0.34888339305671007, 0.5138388209292416], [0.29468417774709255, 0.5467277121476796], [0.23645293503798628, 0.5708478826316308], [0.17822169232888005, 0.594968053115582], [0.11664110164219545, 0.610036727789738], [0.053851903257830805, 0.6155300708402502]], [1, 4, 4, 4, 4, 4, 4]), ('angle_arc_4', [[-0.47332453308879097, 0.3971664411419629], [-0.5196539386093783, 0.34195320567004905], [-0.5559671323204765, 0.2790569091773364], [-0.5806184941039924, 0.21132784931831983], [-0.6052698558875083, 0.1435987894593033], [-0.6178812957139052, 0.07207576005265601], [-0.6178812957139052, 7.566863510490532e-17]], [1, 4, 4, 4, 4, 4, 4])]:
            c.path(vertices, codes, id=object_id, zorder=3, capstyle='butt', fill=False)
        c.text('B', (3.0, 0.0), id='label_B', fontsize=18.0, fontstyle='italic', offset_pt=(18.0, 0.0))
        c.text('A', (-3.0, 3.6739403974420594e-16), id='label_A', fontsize=18.0, fontstyle='italic', offset_pt=(-18.0, 2.204364238465236e-15))
        c.text('O', (0.0, 0.0), id='label_O', fontsize=18.0, fontstyle='italic', offset_pt=(8.572527594031472e-16, -14.0))
        c.text('20°', (0.0, 0.0), id='angle_label_0', offset_pt=(80.75423574700106, 14.23915056868829))
        c.text('30°', (0.0, 0.0), id='angle_label_1', offset_pt=(78.63859625174321, 55.06333788970042))
        c.text('35°', (0.0, 0.0), id='angle_label_2', offset_pt=(31.38004145393736, 75.75812166592551))
        c.text('40°', (0.0, 0.0), id='angle_label_4', offset_pt=(-80.81356538758813, 29.413732326007523))

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
                for object_id, points in [('diameter', [[3.0, 0.0], [-3.0, 3.6739403974420594e-16]]), ('radius_1', [[0.0, 0.0], [2.8190778623577253, 1.0260604299770062]]), ('radius_2', [[0.0, 0.0], [1.9283628290596182, 2.298133329356934]]), ('radius_3', [[0.0, 0.0], [0.2614672282429744, 2.988584094275237]]), ('radius_4', [[0.0, 0.0], [-2.2981333293569337, 1.9283628290596184]])]:
                    c.line(points, id=object_id)
            self._draw_base(c, custom={2: _slot_2})
            return c.save(output_path)

    def draw_C01(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane134_C01.png'
        with Canvas(PLANE, xlim=(-3.4942872403427834, 3.4942872403427825), ylim=(-3.4942872403427834, 3.4942872403427825)) as c:
            self._draw_base(c)
            return c.save(output_path)

    def draw_C02(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane134_C02.png'
        with Canvas(PLANE, xlim=(-3.4942872403427834, 3.4942872403427825), ylim=(-3.4942872403427834, 3.4942872403427825)) as c:

            def _slot_2(c):
                c.path(self._samples_003, [1] + [4] * 12, id='circle_boundary', capstyle='butt', fill=False)
                c.path(self._samples_004, [1, 4, 4, 4, 4, 4, 4, 4, 4, 4], id='circle_boundary', edgecolor='#EA580C', linewidth=3.0, capstyle='butt', fill=False)
                c.path(self._samples_005, [1, 4, 4, 4, 4, 4, 4, 4, 4, 4], id='circle_boundary', capstyle='butt', fill=False)
                c.line([[3.0, 0.0], [-3.0, 3.6739403974420594e-16]], id='diameter')
                c.line([[0.0, 0.0], [2.8190778623577253, 1.0260604299770062]], id='radius_1')
                c.line([[0.0, 0.0], [1.9283628290596182, 2.298133329356934]], id='radius_2', color='#EA580C', linewidth=3.0)
                c.line([[0.0, 0.0], [0.2614672282429744, 2.988584094275237]], id='radius_3')
                c.line([[0.0, 0.0], [-2.2981333293569337, 1.9283628290596184]], id='radius_4', color='#EA580C', linewidth=3.0)
            self._draw_base(c, custom={2: _slot_2})
            return c.save(output_path)

    def draw_C03(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane134_C03.png'
        with Canvas(PLANE, xlim=(-3.4942872403427834, 3.4942872403427825), ylim=(-3.4942872403427834, 3.4942872403427825)) as c:

            def _slot_2(c):
                c.path(self._samples_003, [1] + [4] * 12, id='circle_boundary', capstyle='butt', fill=False)
                c.path(self._samples_004, [1, 4, 4, 4, 4, 4, 4, 4, 4, 4], id='circle_boundary', edgecolor='#DC2626', linewidth=3.0, capstyle='butt', fill=False)
                c.path(self._samples_005, [1, 4, 4, 4, 4, 4, 4, 4, 4, 4], id='circle_boundary', capstyle='butt', fill=False)
                c.line([[3.0, 0.0], [-3.0, 3.6739403974420594e-16]], id='diameter')
                c.line([[0.0, 0.0], [2.8190778623577253, 1.0260604299770062]], id='radius_1')
                c.line([[0.0, 0.0], [1.9283628290596182, 2.298133329356934]], id='radius_2', color='#DC2626', linewidth=3.0)
                c.line([[0.0, 0.0], [0.2614672282429744, 2.988584094275237]], id='radius_3')
                c.line([[0.0, 0.0], [-2.2981333293569337, 1.9283628290596184]], id='radius_4', color='#DC2626', linewidth=3.0)
            self._draw_base(c, custom={2: _slot_2})
            return c.save(output_path)

    def draw_C04(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane134_C04.png'
        with Canvas(PLANE, xlim=(-3.4942872403427834, 3.4942872403427825), ylim=(-3.4942872403427834, 3.4942872403427825)) as c:

            def _slot_2(c):
                c.path(self._samples_006, [1] + [4] * 12, id='circle_boundary', capstyle='butt', fill=False)
                c.path(self._samples_007, [1, 4, 4, 4, 4, 4, 4, 4, 4, 4], id='circle_boundary', edgecolor='#2563EB', linewidth=3.0, capstyle='butt', fill=False)
                c.path([[-3.0, 4.2398580646363365e-15], [-3.0, 2.8265720430908913e-15], [-3.0, 1.4132860215454458e-15], [-3.0, 0.0], [-3.0, -0.7956093000000001], [-2.683901074764725, -1.5587396123545605], [-2.121320343559643, -2.121320343559643], [-1.5587396123545605, -2.683901074764725], [-0.7956093000000001, -3.0], [0.0, -3.0]], [1, 4, 4, 4, 4, 4, 4, 4, 4, 4], id='circle_boundary', capstyle='butt', fill=False)
                c.path([[3.0, 0.0], [0.0, 1.8369701987210297e-16]], [1, 2], id='diameter', joinstyle='round', fill=False)
                c.path([[0.0, 1.8369701987210297e-16], [-3.0, 3.6739403974420594e-16]], [1, 2], id='diameter', edgecolor='#2563EB', linewidth=3.0, joinstyle='round', fill=False)
                c.line([[0.0, 0.0], [2.8190778623577253, 1.0260604299770062]], id='radius_1')
                c.line([[0.0, 0.0], [1.9283628290596182, 2.298133329356934]], id='radius_2')
                c.line([[0.0, 0.0], [0.2614672282429744, 2.988584094275237]], id='radius_3', color='#2563EB', linewidth=3.0)
                c.line([[0.0, 0.0], [-2.2981333293569337, 1.9283628290596184]], id='radius_4')
            self._draw_base(c, custom={2: _slot_2})
            return c.save(output_path)

    def draw_C05(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane134_C05.png'
        with Canvas(PLANE, xlim=(-3.4942872403427834, 3.4942872403427825), ylim=(-3.4942872403427834, 3.4942872403427825)) as c:

            def _slot_2(c):
                c.path(self._samples_006, [1] + [4] * 12, id='circle_boundary', capstyle='butt', fill=False)
                c.path(self._samples_007, [1, 4, 4, 4, 4, 4, 4, 4, 4, 4], id='circle_boundary', edgecolor='#16A34A', linewidth=3.0, capstyle='butt', fill=False)
                c.path([[-3.0, 4.2398580646363365e-15], [-3.0, 2.8265720430908913e-15], [-3.0, 1.4132860215454458e-15], [-3.0, 0.0], [-3.0, -0.7956093000000001], [-2.683901074764725, -1.5587396123545605], [-2.121320343559643, -2.121320343559643], [-1.5587396123545605, -2.683901074764725], [-0.7956093000000001, -3.0], [0.0, -3.0]], [1, 4, 4, 4, 4, 4, 4, 4, 4, 4], id='circle_boundary', capstyle='butt', fill=False)
                c.path([[3.0, 0.0], [0.0, 1.8369701987210297e-16]], [1, 2], id='diameter', joinstyle='round', fill=False)
                c.path([[0.0, 1.8369701987210297e-16], [-3.0, 3.6739403974420594e-16]], [1, 2], id='diameter', edgecolor='#16A34A', linewidth=3.0, joinstyle='round', fill=False)
                c.line([[0.0, 0.0], [2.8190778623577253, 1.0260604299770062]], id='radius_1')
                c.line([[0.0, 0.0], [1.9283628290596182, 2.298133329356934]], id='radius_2')
                c.line([[0.0, 0.0], [0.2614672282429744, 2.988584094275237]], id='radius_3', color='#16A34A', linewidth=3.0)
                c.line([[0.0, 0.0], [-2.2981333293569337, 1.9283628290596184]], id='radius_4')
            self._draw_base(c, custom={2: _slot_2})
            return c.save(output_path)

    def draw_C06(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane134_C06.png'
        with Canvas(PLANE, xlim=(-3.4942872403427834, 3.4942872403427825), ylim=(-3.4942872403427834, 3.4942872403427825)) as c:

            def _slot_2(c):
                c.path(self._samples_006, [1] + [4] * 12, id='circle_boundary', capstyle='butt', fill=False)
                c.path(self._samples_007, [1, 4, 4, 4, 4, 4, 4, 4, 4, 4], id='circle_boundary', edgecolor='#EA580C', linewidth=3.0, capstyle='butt', fill=False)
                c.path([[-3.0, 4.2398580646363365e-15], [-3.0, 2.8265720430908913e-15], [-3.0, 1.4132860215454458e-15], [-3.0, 0.0], [-3.0, -0.7956093000000001], [-2.683901074764725, -1.5587396123545605], [-2.121320343559643, -2.121320343559643], [-1.5587396123545605, -2.683901074764725], [-0.7956093000000001, -3.0], [0.0, -3.0]], [1, 4, 4, 4, 4, 4, 4, 4, 4, 4], id='circle_boundary', capstyle='butt', fill=False)
                c.path([[3.0, 0.0], [0.0, 1.8369701987210297e-16]], [1, 2], id='diameter', joinstyle='round', fill=False)
                c.path([[0.0, 1.8369701987210297e-16], [-3.0, 3.6739403974420594e-16]], [1, 2], id='diameter', edgecolor='#EA580C', linewidth=3.0, joinstyle='round', fill=False)
                c.line([[0.0, 0.0], [2.8190778623577253, 1.0260604299770062]], id='radius_1')
                c.line([[0.0, 0.0], [1.9283628290596182, 2.298133329356934]], id='radius_2')
                c.line([[0.0, 0.0], [0.2614672282429744, 2.988584094275237]], id='radius_3', color='#EA580C', linewidth=3.0)
                c.line([[0.0, 0.0], [-2.2981333293569337, 1.9283628290596184]], id='radius_4')
            self._draw_base(c, custom={2: _slot_2})
            return c.save(output_path)
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Plane134')
    parser.add_argument('output', nargs='?')
    parser.add_argument('--variant', choices=('C01', 'C02', 'C03', 'C04', 'C05', 'C06'))
    args = parser.parse_args()
    print(Plane134().draw(args.output, variant=args.variant))
