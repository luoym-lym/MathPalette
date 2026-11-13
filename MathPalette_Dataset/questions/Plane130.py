"""Collected question Plane130; construction on the shared drawing protocol."""
from pathlib import Path
import sys
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from MathPalette_Dataset.drawing import Canvas, PLANE
import numpy as np

class Plane130:
    variants = ('C01', 'C02', 'C03', 'C04', 'C05', 'C06')

    def __init__(self):
        _t = np.radians(np.linspace(80.0, 140.0, 241))
        self._samples_001 = [[0.0, 0.0], *np.column_stack([3.0 * np.cos(_t), 3.0 * np.sin(_t)]).tolist(), [0.0, 0.0]]
        self._samples_002 = [1] + [2] * 241 + [79]
        self._samples_003 = [
            [2.5980750550924734, 1.499999093062551], [2.468096171106242, 1.7251503096689924],
            [2.308325615682859, 1.9343150714364268], [2.121320343559643, 2.121320343559643],
            [1.5587396123545605, 2.683901074764725], [0.7956093000000001, 3.0], [0.0, 3.0],
            [-0.7956093000000001, 3.0], [-1.5587396123545605, 2.683901074764725],
            [-2.121320343559643, 2.121320343559643], [-2.183280586500995, 2.0593601006182904],
            [-2.2422510346240068, 1.9949672152505251], [-2.2981386841006213, 1.9283662185593937]
        ]
        self._samples_004 = [
            [-2.2981386841006213, 1.9283662185593937], [-2.7496944082345247, 1.3902498087524704],
            [-3.0, 0.707984284104408], [-3.0, 0.0], [-3.0, -0.7956093000000001],
            [-2.683901074764725, -1.5587396123545605], [-2.121320343559643, -2.121320343559643],
            [-1.5587396123545605, -2.683901074764725], [-0.7956093000000001, -3.0], [0.0, -3.0]
        ]
        self._samples_005 = self._samples_001[:-1]
        self._samples_006 = [1] + [2] * 241
        self._samples_007 = [
            [0.0, -3.0], [0.7956093000000001, -3.0], [1.5587396123545605, -2.683901074764725],
            [2.121320343559643, -2.121320343559643], [2.683901074764725, -1.5587396123545605],
            [3.0, -0.7956093000000001], [3.0, 0.0], [3.0, 0.7956093000000001],
            [2.683901074764725, 1.5587396123545605], [2.121320343559643, 2.121320343559643],
            [1.5587396123545605, 2.683901074764725], [0.7956093000000001, 3.0], [0.0, 3.0],
            [-0.7956093000000001, 3.0], [-1.5587396123545605, 2.683901074764725],
            [-2.121320343559643, 2.121320343559643], [-2.183280586500995, 2.0593601006182904],
            [-2.2422510346240068, 1.9949672152505251], [-2.2981386841006213, 1.9283662185593937]
        ]

    def _draw_base(self, c, custom=None):
        c.path(self._samples_001, self._samples_002, alpha=0.45, zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), capstyle='butt')
        if custom and 1 in custom:
            custom[1](c)
        else:
            c.path(self._samples_001, self._samples_002, id='shade', capstyle='butt', fill=False)
            c.path([[0.0, -3.0], [0.7956093000000001, -3.0], [1.5587396123545605, -2.683901074764725], [2.121320343559643, -2.121320343559643], [2.683901074764725, -1.5587396123545605], [3.0, -0.7956093000000001], [3.0, 0.0], [3.0, 0.5311439079280766], [2.859120524398346, 1.04781252858918], [2.5980750550924734, 1.499999093062551]], [1, 4, 4, 4, 4, 4, 4, 4, 4, 4], id='circle_boundary', capstyle='butt', fill=False)
            c.path(self._samples_003, [1] + [4] * 12, id='circle_boundary', edgecolor='#DC2626', linewidth=1.5, capstyle='butt', fill=False)
            c.path(self._samples_004, [1, 4, 4, 4, 4, 4, 4, 4, 4, 4], id='circle_boundary', capstyle='butt', fill=False)
            c.line([[3.0, 0.0], [-3.0, 3.6739403974420594e-16]], id='diameter')
            c.line([[0.0, 0.0], [2.598076211353316, 1.4999999999999998]], id='radius_1', color='#DC2626', linewidth=1.5)
            c.line([[0.0, 0.0], [0.5209445330007912, 2.954423259036624]], id='radius_2')
            c.line([[0.0, 0.0], [-2.2981333293569337, 1.9283628290596184]], id='radius_3', color='#DC2626', linewidth=1.5)
        c.point([[0.0, 0.0]], id='center_dot')
        for object_id, vertices, codes in [('angle_arc_0', [[0.5897957822723641, 0.0], [0.5897957822723641, 0.05154277326842139], [0.5830392296925092, 0.10286388531469748], [0.5696989783332407, 0.1526503811732275], [0.5563587269739722, 0.20243687703175753], [0.5365495171269937, 0.2502605401042276], [0.510778130492783, 0.294897891136182]], [1, 4, 4, 4, 4, 4, 4]), ('angle_arc_1', [[0.7175216595017665, 0.4142613232627318], [0.6570318305351064, 0.5190327803741388], [0.5743218011436751, 0.6092949385726969], [0.47522106703021283, 0.6786860196410593], [0.37612033291675057, 0.7480771007094218], [0.2630131528144279, 0.7949276287095801], [0.1438714477249291, 0.8159355258444698]], [1, 4, 4, 4, 4, 4, 4]), ('angle_arc_3', [[-0.6454425451210786, 0.5415906015572222], [-0.7086190071946068, 0.4662998259137033], [-0.7581369986188315, 0.380532148878186], [-0.7917524919599895, 0.28817433997952707], [-0.8253679853011476, 0.19581653108086813], [-0.8425654032462343, 0.09828512734453093], [-0.8425654032462343, 1.0318450241577997e-16]], [1, 4, 4, 4, 4, 4, 4])]:
            c.path(vertices, codes, id=object_id, zorder=3, capstyle='butt', fill=False)
        c.text('B', (3.0, 0.0), id='label_B', fontsize=18.0, fontstyle='italic', offset_pt=(18.0, 0.0))
        c.text('A', (-3.0, 3.6739403974420594e-16), id='label_A', fontsize=18.0, fontstyle='italic', offset_pt=(-18.0, 2.204364238465236e-15))
        c.text('O', (0.0, 0.0), id='label_O', fontsize=18.0, fontstyle='italic', offset_pt=(8.572527594031472e-16, -14.0))
        c.text('30°', (0.0, 0.0), id='angle_label_0', offset_pt=(79.2059177557036, 21.223161698406695))
        c.text('50°', (0.0, 0.0), id='angle_label_1', offset_pt=(55.063337889700435, 78.63859625174321))
        c.text('40°', (0.0, 0.0), id='angle_label_3', offset_pt=(-92.08987683701902, 33.51797404591555))

    def draw(self, output_path=None, *, variant=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / (self.__class__.__name__ + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if variant not in self.variants:
                raise ValueError('Unknown Special variant: ' + str(variant))
            return getattr(self, 'draw_' + variant)(output_path)
        with Canvas(PLANE, xlim=(-3.4942872403427834, 3.4942872403427825), ylim=(-3.4942872403427834, 3.4942872403427825)) as c:

            def _slot_1(c):
                c.path(self._samples_001, self._samples_002, id='shade', capstyle='butt', fill=False)
                c.circle([0.0, 0.0], 3.0, id='circle_boundary', fill=False)
                for object_id, points in [('diameter', [[3.0, 0.0], [-3.0, 3.6739403974420594e-16]]), ('radius_1', [[0.0, 0.0], [2.598076211353316, 1.4999999999999998]]), ('radius_2', [[0.0, 0.0], [0.5209445330007912, 2.954423259036624]]), ('radius_3', [[0.0, 0.0], [-2.2981333293569337, 1.9283628290596184]])]:
                    c.line(points, id=object_id)
            self._draw_base(c, custom={1: _slot_1})
            return c.save(output_path)

    def draw_C01(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane130_C01.png'
        with Canvas(PLANE, xlim=(-3.4942872403427834, 3.4942872403427825), ylim=(-3.4942872403427834, 3.4942872403427825)) as c:
            self._draw_base(c)
            return c.save(output_path)

    def draw_C02(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane130_C02.png'
        with Canvas(PLANE, xlim=(-3.4942872403427834, 3.4942872403427825), ylim=(-3.4942872403427834, 3.4942872403427825)) as c:

            def _slot_1(c):
                c.path(self._samples_005, self._samples_006, id='shade', edgecolor='#DC2626', linewidth=1.5, capstyle='butt', fill=False, simplify=True)
                c.path([[-2.2981333293569337, 1.9283628290596184], [0.0, 0.0]], [1, 2], id='shade', capstyle='butt', fill=False)
                c.path(self._samples_007, [1] + [4] * 18, id='circle_boundary', capstyle='butt', fill=False)
                c.path([[-2.2981386841006213, 1.9283662185593937], [-2.7496944082345247, 1.3902498087524704], [-3.0, 0.707984284104408], [-3.0, 0.0]], [1, 4, 4, 4], id='circle_boundary', edgecolor='#DC2626', linewidth=1.5, capstyle='butt', fill=False)
                c.path([[-3.0, 0.0], [-3.0, -0.7956093000000001], [-2.683901074764725, -1.5587396123545605], [-2.121320343559643, -2.121320343559643], [-1.5587396123545605, -2.683901074764725], [-0.7956093000000001, -3.0], [0.0, -3.0]], [1, 4, 4, 4, 4, 4, 4], id='circle_boundary', capstyle='butt', fill=False)
                c.path([[3.0, 0.0], [0.0, 1.8369701987210297e-16]], [1, 2], id='diameter', joinstyle='round', fill=False)
                c.path([[0.0, 1.8369701987210297e-16], [-3.0, 3.6739403974420594e-16]], [1, 2], id='diameter', edgecolor='#DC2626', linewidth=1.5, joinstyle='round', fill=False)
                for object_id, points in [('radius_1', [[0.0, 0.0], [2.598076211353316, 1.4999999999999998]]), ('radius_2', [[0.0, 0.0], [0.5209445330007912, 2.954423259036624]]), ('radius_3', [[0.0, 0.0], [-2.2981333293569337, 1.9283628290596184]])]:
                    c.line(points, id=object_id)
            self._draw_base(c, custom={1: _slot_1})
            return c.save(output_path)

    def draw_C03(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane130_C03.png'
        with Canvas(PLANE, xlim=(-3.4942872403427834, 3.4942872403427825), ylim=(-3.4942872403427834, 3.4942872403427825)) as c:

            def _slot_1(c):
                c.path(self._samples_001, self._samples_002, id='shade', capstyle='butt', fill=False)
                c.path([[0.0, -3.0], [0.7956093000000001, -3.0], [1.5587396123545605, -2.683901074764725], [2.121320343559643, -2.121320343559643], [2.683901074764725, -1.5587396123545605], [3.0, -0.7956093000000001], [3.0, 0.0], [3.0, 0.5311439079280766], [2.859120524398346, 1.04781252858918], [2.5980750550924734, 1.499999093062551]], [1, 4, 4, 4, 4, 4, 4, 4, 4, 4], id='circle_boundary', capstyle='butt', fill=False)
                c.path(self._samples_003, [1] + [4] * 12, id='circle_boundary', edgecolor='#2563EB', linewidth=2.0, capstyle='butt', fill=False)
                c.path(self._samples_004, [1, 4, 4, 4, 4, 4, 4, 4, 4, 4], id='circle_boundary', capstyle='butt', fill=False)
                c.line([[3.0, 0.0], [-3.0, 3.6739403974420594e-16]], id='diameter')
                c.line([[0.0, 0.0], [2.598076211353316, 1.4999999999999998]], id='radius_1', color='#2563EB', linewidth=2.0)
                c.line([[0.0, 0.0], [0.5209445330007912, 2.954423259036624]], id='radius_2')
                c.line([[0.0, 0.0], [-2.2981333293569337, 1.9283628290596184]], id='radius_3', color='#2563EB', linewidth=2.0)
            self._draw_base(c, custom={1: _slot_1})
            return c.save(output_path)

    def draw_C04(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane130_C04.png'
        with Canvas(PLANE, xlim=(-3.4942872403427834, 3.4942872403427825), ylim=(-3.4942872403427834, 3.4942872403427825)) as c:

            def _slot_1(c):
                c.path(self._samples_001, self._samples_002, id='shade', capstyle='butt', fill=False)
                c.path([[0.0, -3.0], [0.7956093000000001, -3.0], [1.5587396123545605, -2.683901074764725], [2.121320343559643, -2.121320343559643], [2.683901074764725, -1.5587396123545605], [3.0, -0.7956093000000001], [3.0, 0.0], [3.0, 0.5311439079280766], [2.859120524398346, 1.04781252858918], [2.5980750550924734, 1.499999093062551]], [1, 4, 4, 4, 4, 4, 4, 4, 4, 4], id='circle_boundary', capstyle='butt', fill=False)
                c.path(self._samples_003, [1] + [4] * 12, id='circle_boundary', edgecolor='#16A34A', linewidth=3.0, capstyle='butt', fill=False)
                c.path(self._samples_004, [1, 4, 4, 4, 4, 4, 4, 4, 4, 4], id='circle_boundary', capstyle='butt', fill=False)
                c.line([[3.0, 0.0], [-3.0, 3.6739403974420594e-16]], id='diameter')
                c.line([[0.0, 0.0], [2.598076211353316, 1.4999999999999998]], id='radius_1', color='#16A34A', linewidth=3.0)
                c.line([[0.0, 0.0], [0.5209445330007912, 2.954423259036624]], id='radius_2')
                c.line([[0.0, 0.0], [-2.2981333293569337, 1.9283628290596184]], id='radius_3', color='#16A34A', linewidth=3.0)
            self._draw_base(c, custom={1: _slot_1})
            return c.save(output_path)

    def draw_C05(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane130_C05.png'
        with Canvas(PLANE, xlim=(-3.4942872403427834, 3.4942872403427825), ylim=(-3.4942872403427834, 3.4942872403427825)) as c:

            def _slot_1(c):
                c.path(self._samples_001, self._samples_002, id='shade', capstyle='butt', fill=False)
                c.path([[0.0, -3.0], [0.7956093000000001, -3.0], [1.5587396123545605, -2.683901074764725], [2.121320343559643, -2.121320343559643], [2.683901074764725, -1.5587396123545605], [3.0, -0.7956093000000001], [3.0, 0.0], [3.0, 0.5311439079280766], [2.859120524398346, 1.04781252858918], [2.5980750550924734, 1.499999093062551]], [1, 4, 4, 4, 4, 4, 4, 4, 4, 4], id='circle_boundary', capstyle='butt', fill=False)
                c.path(self._samples_003, [1] + [4] * 12, id='circle_boundary', edgecolor='#2563EB', linewidth=3.0, capstyle='butt', fill=False)
                c.path(self._samples_004, [1, 4, 4, 4, 4, 4, 4, 4, 4, 4], id='circle_boundary', capstyle='butt', fill=False)
                c.line([[3.0, 0.0], [-3.0, 3.6739403974420594e-16]], id='diameter')
                c.line([[0.0, 0.0], [2.598076211353316, 1.4999999999999998]], id='radius_1', color='#2563EB', linewidth=3.0)
                c.line([[0.0, 0.0], [0.5209445330007912, 2.954423259036624]], id='radius_2')
                c.line([[0.0, 0.0], [-2.2981333293569337, 1.9283628290596184]], id='radius_3', color='#2563EB', linewidth=3.0)
            self._draw_base(c, custom={1: _slot_1})
            return c.save(output_path)

    def draw_C06(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane130_C06.png'
        with Canvas(PLANE, xlim=(-3.4942872403427834, 3.4942872403427825), ylim=(-3.4942872403427834, 3.4942872403427825)) as c:

            def _slot_1(c):
                c.path(self._samples_005, self._samples_006, id='shade', edgecolor='#DC2626', linewidth=3.0, capstyle='butt', fill=False, simplify=True)
                c.path([[-2.2981333293569337, 1.9283628290596184], [0.0, 0.0]], [1, 2], id='shade', capstyle='butt', fill=False)
                c.path(self._samples_007, [1] + [4] * 18, id='circle_boundary', capstyle='butt', fill=False)
                c.path([[-2.2981386841006213, 1.9283662185593937], [-2.7496944082345247, 1.3902498087524704], [-3.0, 0.707984284104408], [-3.0, 0.0]], [1, 4, 4, 4], id='circle_boundary', edgecolor='#DC2626', linewidth=3.0, capstyle='butt', fill=False)
                c.path([[-3.0, 0.0], [-3.0, -0.7956093000000001], [-2.683901074764725, -1.5587396123545605], [-2.121320343559643, -2.121320343559643], [-1.5587396123545605, -2.683901074764725], [-0.7956093000000001, -3.0], [0.0, -3.0]], [1, 4, 4, 4, 4, 4, 4], id='circle_boundary', capstyle='butt', fill=False)
                c.path([[3.0, 0.0], [0.0, 1.8369701987210297e-16]], [1, 2], id='diameter', joinstyle='round', fill=False)
                c.path([[0.0, 1.8369701987210297e-16], [-3.0, 3.6739403974420594e-16]], [1, 2], id='diameter', edgecolor='#DC2626', linewidth=3.0, joinstyle='round', fill=False)
                for object_id, points in [('radius_1', [[0.0, 0.0], [2.598076211353316, 1.4999999999999998]]), ('radius_2', [[0.0, 0.0], [0.5209445330007912, 2.954423259036624]]), ('radius_3', [[0.0, 0.0], [-2.2981333293569337, 1.9283628290596184]])]:
                    c.line(points, id=object_id)
            self._draw_base(c, custom={1: _slot_1})
            return c.save(output_path)
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Plane130')
    parser.add_argument('output', nargs='?')
    parser.add_argument('--variant', choices=('C01', 'C02', 'C03', 'C04', 'C05', 'C06'))
    args = parser.parse_args()
    print(Plane130().draw(args.output, variant=args.variant))
