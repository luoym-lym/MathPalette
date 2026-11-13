"""Collected question Plane133; construction on the shared drawing protocol."""
from pathlib import Path
import sys
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from MathPalette_Dataset.drawing import Canvas, PLANE
import numpy as np

class Plane133:
    variants = ('C01', 'C02', 'C03', 'C04', 'C05', 'C06')

    def __init__(self):
        _t = np.radians(np.linspace(-150.0, -105.0, 181))
        self._samples_001 = [[0.0, 0.0], *np.column_stack([3.0 * np.cos(_t), 3.0 * np.sin(_t)]).tolist(), [0.0, 0.0]]
        self._samples_002 = [1] + [2] * 181 + [79]
        self._samples_003 = [
            [0.0, -3.0], [0.7956093000000001, -3.0], [1.5587396123545605, -2.683901074764725],
            [2.121320343559643, -2.121320343559643], [2.683901074764725, -1.5587396123545605],
            [3.0, -0.7956093000000001], [3.0, 0.0], [3.0, 0.7956093000000001],
            [2.683901074764725, 1.5587396123545605], [2.121320343559643, 2.121320343559643],
            [1.5587396123545605, 2.683901074764725], [0.7956093000000001, 3.0], [0.0, 3.0],
            [-0.7956093000000001, 3.0], [-1.5587396123545605, 2.683901074764725],
            [-2.121320343559643, 2.121320343559643], [-2.683901074764724, 1.5587396123545616],
            [-2.999999999999999, 0.7956093000000027], [-3.0, 4.2398580646363365e-15]
        ]
        self._samples_004 = [
            [-3.0, 4.2398580646363365e-15], [-3.0, 2.8265720430908913e-15], [-3.0, 1.4132860215454458e-15],
            [-3.0, 0.0], [-3.0, -0.7956093000000001], [-2.683901074764725, -1.5587396123545605],
            [-2.121320343559643, -2.121320343559643], [-1.7457448347728557, -2.49689585234643],
            [-1.2807880435861994, -2.7626189257427054], [-0.7764567587746274, -2.897776073627157]
        ]
        self._samples_005 = [
            [2.298138140636405, -1.9283668662024498], [2.7496942073997546, -1.3902503561737662],
            [3.0, -0.7079845681328858], [3.0, 0.0], [3.0, 0.7956093000000001],
            [2.683901074764725, 1.5587396123545605], [2.121320343559643, 2.121320343559643],
            [1.5587396123545605, 2.683901074764725], [0.7956093000000001, 3.0], [0.0, 3.0],
            [-0.7956093000000001, 3.0], [-1.5587396123545605, 2.683901074764725],
            [-2.121320343559643, 2.121320343559643], [-2.683901074764725, 1.5587396123545605],
            [-3.0, 0.7956093000000001], [-3.0, 0.0], [-3.0, -0.5311439782214498],
            [-2.859120487109415, -1.0478126653445095], [-2.598074951449558, -1.4999992725942253]
        ]

    def _draw_base(self, c, custom=None):
        c.path(self._samples_001, self._samples_002, alpha=0.45, zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), capstyle='butt')
        c.path(self._samples_001, self._samples_002, id='shade', capstyle='butt', fill=False)
        if custom and 2 in custom:
            custom[2](c)
        else:
            c.path(self._samples_003, [1] + [4] * 18, id='circle_boundary', capstyle='butt', fill=False)
            c.path(self._samples_004, [1, 4, 4, 4, 4, 4, 4, 4, 4, 4], id='circle_boundary', edgecolor='#2563EB', linewidth=3.0, capstyle='butt', fill=False)
            c.path([[-0.7764567587746274, -2.897776073627157], [-0.5253419179977399, -2.9650730403095693], [-0.26446532177855026, -3.0], [0.0, -3.0]], [1, 4, 4, 4], id='circle_boundary', capstyle='butt', fill=False)
            c.path([[-3.0, 3.6739403974420594e-16], [0.0, -1.8369701987210297e-16]], [1, 2], id='diameter', edgecolor='#2563EB', linewidth=3.0, joinstyle='round', fill=False)
            c.path([[0.0, -1.8369701987210297e-16], [3.0, -7.347880794884119e-16]], [1, 2], id='diameter', joinstyle='round', fill=False)
            c.line([[0.0, 0.0], [-2.598076211353316, -1.5000000000000004]], id='radius_1')
            c.line([[0.0, 0.0], [-0.7764571353075619, -2.897777478867205]], id='radius_2', color='#2563EB', linewidth=3.0)
            c.line([[0.0, 0.0], [2.2981333293569333, -1.9283628290596186]], id='radius_3')
        c.point([[0.0, 0.0]], id='center_dot')
        for object_id, vertices, codes in [('angle_arc_0', [[-0.5897957822723641, 7.222915169104599e-17], [-0.5897957822723641, -0.05154277326842135], [-0.5830392296925092, -0.10286388531469748], [-0.5696989783332407, -0.15265038117322752], [-0.5563587269739722, -0.20243687703175758], [-0.5365495171269936, -0.25026054010422766], [-0.5107781304927829, -0.2948978911361821]], [1, 4, 4, 4, 4, 4, 4]), ('angle_arc_2', [[-0.15991944694338112, -0.596827501111014], [-0.04632200724613436, -0.6272658433401344], [0.07363887076105025, -0.6246482876703965], [0.18580048902638627, -0.5892838652726291], [0.2979621072917223, -0.5539194428748617], [0.3977296739990082, -0.4872568860438646], [0.4733245330887909, -0.39716644114196303]], [1, 4, 4, 4, 4, 4, 4]), ('angle_arc_3', [[0.6454425451210786, -0.5415906015572223], [0.7086190071946067, -0.46629982591370334], [0.7581369986188317, -0.38053214887818576], [0.7917524919599896, -0.2881743399795268], [0.8253679853011476, -0.19581653108086788], [0.8425654032462343, -0.09828512734453103], [0.8425654032462343, -2.0636900483155995e-16]], [1, 4, 4, 4, 4, 4, 4])]:
            c.path(vertices, codes, id=object_id, zorder=3, capstyle='butt', fill=False)
        c.text('B', (-3.0, 3.6739403974420594e-16), id='label_B', fontsize=18.0, fontstyle='italic', offset_pt=(-18.0, 2.204364238465236e-15))
        c.text('A', (3.0, -7.347880794884119e-16), id='label_A', fontsize=18.0, fontstyle='italic', offset_pt=(18.0, -4.408728476930472e-15))
        c.text('O', (0.0, 0.0), id='label_O', fontsize=18.0, fontstyle='italic', offset_pt=(8.572527594031472e-16, 14.0))
        c.text('30°', (0.0, 0.0), id='angle_label_0', offset_pt=(-79.2059177557036, -21.2231616984067))
        c.text('65°', (0.0, 0.0), id='angle_label_2', offset_pt=(24.657875559350394, -78.2047899613546))
        c.text('40°', (0.0, 0.0), id='angle_label_3', offset_pt=(92.08987683701902, -33.517974045915565))

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
                for object_id, points in [('diameter', [[-3.0, 3.6739403974420594e-16], [3.0, -7.347880794884119e-16]]), ('radius_1', [[0.0, 0.0], [-2.598076211353316, -1.5000000000000004]]), ('radius_2', [[0.0, 0.0], [-0.7764571353075619, -2.897777478867205]]), ('radius_3', [[0.0, 0.0], [2.2981333293569333, -1.9283628290596186]])]:
                    c.line(points, id=object_id)
            self._draw_base(c, custom={2: _slot_2})
            return c.save(output_path)

    def draw_C01(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane133_C01.png'
        with Canvas(PLANE, xlim=(-3.4942872403427834, 3.4942872403427825), ylim=(-3.4942872403427834, 3.4942872403427825)) as c:
            self._draw_base(c)
            return c.save(output_path)

    def draw_C02(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane133_C02.png'
        with Canvas(PLANE, xlim=(-3.4942872403427834, 3.4942872403427825), ylim=(-3.4942872403427834, 3.4942872403427825)) as c:

            def _slot_2(c):
                c.path(self._samples_003, [1] + [4] * 18, id='circle_boundary', capstyle='butt', fill=False)
                c.path(self._samples_004, [1, 4, 4, 4, 4, 4, 4, 4, 4, 4], id='circle_boundary', edgecolor='#16A34A', linewidth=3.0, capstyle='butt', fill=False)
                c.path([[-0.7764567587746274, -2.897776073627157], [-0.5253419179977399, -2.9650730403095693], [-0.26446532177855026, -3.0], [0.0, -3.0]], [1, 4, 4, 4], id='circle_boundary', capstyle='butt', fill=False)
                c.path([[-3.0, 3.6739403974420594e-16], [0.0, -1.8369701987210297e-16]], [1, 2], id='diameter', edgecolor='#16A34A', linewidth=3.0, joinstyle='round', fill=False)
                c.path([[0.0, -1.8369701987210297e-16], [3.0, -7.347880794884119e-16]], [1, 2], id='diameter', joinstyle='round', fill=False)
                c.line([[0.0, 0.0], [-2.598076211353316, -1.5000000000000004]], id='radius_1')
                c.line([[0.0, 0.0], [-0.7764571353075619, -2.897777478867205]], id='radius_2', color='#16A34A', linewidth=3.0)
                c.line([[0.0, 0.0], [2.2981333293569333, -1.9283628290596186]], id='radius_3')
            self._draw_base(c, custom={2: _slot_2})
            return c.save(output_path)

    def draw_C03(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane133_C03.png'
        with Canvas(PLANE, xlim=(-3.4942872403427834, 3.4942872403427825), ylim=(-3.4942872403427834, 3.4942872403427825)) as c:

            def _slot_2(c):
                c.path(self._samples_003, [1] + [4] * 18, id='circle_boundary', capstyle='butt', fill=False)
                c.path(self._samples_004, [1, 4, 4, 4, 4, 4, 4, 4, 4, 4], id='circle_boundary', edgecolor='#EA580C', linewidth=3.0, capstyle='butt', fill=False)
                c.path([[-0.7764567587746274, -2.897776073627157], [-0.5253419179977399, -2.9650730403095693], [-0.26446532177855026, -3.0], [0.0, -3.0]], [1, 4, 4, 4], id='circle_boundary', capstyle='butt', fill=False)
                c.path([[-3.0, 3.6739403974420594e-16], [0.0, -1.8369701987210297e-16]], [1, 2], id='diameter', edgecolor='#EA580C', linewidth=3.0, joinstyle='round', fill=False)
                c.path([[0.0, -1.8369701987210297e-16], [3.0, -7.347880794884119e-16]], [1, 2], id='diameter', joinstyle='round', fill=False)
                c.line([[0.0, 0.0], [-2.598076211353316, -1.5000000000000004]], id='radius_1')
                c.line([[0.0, 0.0], [-0.7764571353075619, -2.897777478867205]], id='radius_2', color='#EA580C', linewidth=3.0)
                c.line([[0.0, 0.0], [2.2981333293569333, -1.9283628290596186]], id='radius_3')
            self._draw_base(c, custom={2: _slot_2})
            return c.save(output_path)

    def draw_C04(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane133_C04.png'
        with Canvas(PLANE, xlim=(-3.4942872403427834, 3.4942872403427825), ylim=(-3.4942872403427834, 3.4942872403427825)) as c:

            def _slot_2(c):
                c.path(self._samples_003, [1] + [4] * 18, id='circle_boundary', capstyle='butt', fill=False)
                c.path(self._samples_004, [1, 4, 4, 4, 4, 4, 4, 4, 4, 4], id='circle_boundary', edgecolor='#DC2626', linewidth=3.0, capstyle='butt', fill=False)
                c.path([[-0.7764567587746274, -2.897776073627157], [-0.5253419179977399, -2.9650730403095693], [-0.26446532177855026, -3.0], [0.0, -3.0]], [1, 4, 4, 4], id='circle_boundary', capstyle='butt', fill=False)
                c.path([[-3.0, 3.6739403974420594e-16], [0.0, -1.8369701987210297e-16]], [1, 2], id='diameter', edgecolor='#DC2626', linewidth=3.0, joinstyle='round', fill=False)
                c.path([[0.0, -1.8369701987210297e-16], [3.0, -7.347880794884119e-16]], [1, 2], id='diameter', joinstyle='round', fill=False)
                c.line([[0.0, 0.0], [-2.598076211353316, -1.5000000000000004]], id='radius_1')
                c.line([[0.0, 0.0], [-0.7764571353075619, -2.897777478867205]], id='radius_2', color='#DC2626', linewidth=3.0)
                c.line([[0.0, 0.0], [2.2981333293569333, -1.9283628290596186]], id='radius_3')
            self._draw_base(c, custom={2: _slot_2})
            return c.save(output_path)

    def draw_C05(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane133_C05.png'
        with Canvas(PLANE, xlim=(-3.4942872403427834, 3.4942872403427825), ylim=(-3.4942872403427834, 3.4942872403427825)) as c:

            def _slot_2(c):
                c.path([[0.0, -3.0], [0.7956093000000001, -3.0], [1.5587396123545605, -2.683901074764725], [2.121320343559643, -2.121320343559643], [2.1832803856625325, -2.0593603014567536], [2.242250652329343, -1.9949676326978014], [2.298138140636405, -1.9283668662024498]], [1, 4, 4, 4, 4, 4, 4], id='circle_boundary', edgecolor='#16A34A', linewidth=3.0, capstyle='butt', fill=False)
                c.path(self._samples_005, [1] + [4] * 18, id='circle_boundary', capstyle='butt', fill=False)
                c.path([[-2.598074951449558, -1.4999992725942253], [-2.4680960861740595, -1.7251504208585613], [-2.3083255659779383, -1.9343151211413476], [-2.121320343559643, -2.121320343559643], [-1.5587396123545605, -2.683901074764725], [-0.7956093000000001, -3.0], [0.0, -3.0]], [1, 4, 4, 4, 4, 4, 4], id='circle_boundary', edgecolor='#16A34A', linewidth=3.0, capstyle='butt', fill=False)
                c.line([[-3.0, 3.6739403974420594e-16], [3.0, -7.347880794884119e-16]], id='diameter')
                c.line([[0.0, 0.0], [-2.598076211353316, -1.5000000000000004]], id='radius_1', color='#16A34A', linewidth=3.0)
                c.line([[0.0, 0.0], [-0.7764571353075619, -2.897777478867205]], id='radius_2')
                c.line([[0.0, 0.0], [2.2981333293569333, -1.9283628290596186]], id='radius_3', color='#16A34A', linewidth=3.0)
            self._draw_base(c, custom={2: _slot_2})
            return c.save(output_path)

    def draw_C06(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane133_C06.png'
        with Canvas(PLANE, xlim=(-3.4942872403427834, 3.4942872403427825), ylim=(-3.4942872403427834, 3.4942872403427825)) as c:

            def _slot_2(c):
                c.path([[0.0, -3.0], [0.7956093000000001, -3.0], [1.5587396123545605, -2.683901074764725], [2.121320343559643, -2.121320343559643], [2.1832803856625325, -2.0593603014567536], [2.242250652329343, -1.9949676326978014], [2.298138140636405, -1.9283668662024498]], [1, 4, 4, 4, 4, 4, 4], id='circle_boundary', edgecolor='#EA580C', linewidth=3.0, capstyle='butt', fill=False)
                c.path(self._samples_005, [1] + [4] * 18, id='circle_boundary', capstyle='butt', fill=False)
                c.path([[-2.598074951449558, -1.4999992725942253], [-2.4680960861740595, -1.7251504208585613], [-2.3083255659779383, -1.9343151211413476], [-2.121320343559643, -2.121320343559643], [-1.5587396123545605, -2.683901074764725], [-0.7956093000000001, -3.0], [0.0, -3.0]], [1, 4, 4, 4, 4, 4, 4], id='circle_boundary', edgecolor='#EA580C', linewidth=3.0, capstyle='butt', fill=False)
                c.line([[-3.0, 3.6739403974420594e-16], [3.0, -7.347880794884119e-16]], id='diameter')
                c.line([[0.0, 0.0], [-2.598076211353316, -1.5000000000000004]], id='radius_1', color='#EA580C', linewidth=3.0)
                c.line([[0.0, 0.0], [-0.7764571353075619, -2.897777478867205]], id='radius_2')
                c.line([[0.0, 0.0], [2.2981333293569333, -1.9283628290596186]], id='radius_3', color='#EA580C', linewidth=3.0)
            self._draw_base(c, custom={2: _slot_2})
            return c.save(output_path)
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Plane133')
    parser.add_argument('output', nargs='?')
    parser.add_argument('--variant', choices=('C01', 'C02', 'C03', 'C04', 'C05', 'C06'))
    args = parser.parse_args()
    print(Plane133().draw(args.output, variant=args.variant))
