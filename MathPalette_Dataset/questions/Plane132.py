"""Collected question Plane132; construction on the shared drawing protocol."""
from pathlib import Path
import sys
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from MathPalette_Dataset.drawing import Canvas, PLANE
import numpy as np

class Plane132:
    variants = ('C01', 'C02', 'C03', 'C04', 'C05', 'C06')

    def __init__(self):
        _t = np.radians(np.linspace(130.0, 180.0, 201))
        self._samples_001 = [[0.0, 0.0], *np.column_stack([3.0 * np.cos(_t), 3.0 * np.sin(_t)]).tolist(), [0.0, 0.0]]
        self._samples_002 = [1] + [2] * 201 + [79]
        self._samples_003 = [
            [0.0, -3.0], [0.7956093000000001, -3.0], [1.5587396123545605, -2.683901074764725],
            [2.121320343559643, -2.121320343559643], [2.683901074764725, -1.5587396123545605],
            [3.0, -0.7956093000000001], [3.0, 0.0], [3.0, 0.7956093000000001],
            [2.683901074764725, 1.5587396123545605], [2.121320343559643, 2.121320343559643],
            [1.558739612354561, 2.6839010747647247], [0.7956093000000014, 2.999999999999999],
            [2.1199290323181686e-15, 3.0]
        ]
        self._samples_004 = [
            [2.1199290323181686e-15, 3.0], [1.4132860215454458e-15, 3.0], [7.066430107727229e-16, 3.0],
            [0.0, 3.0], [-0.7956093000000001, 3.0], [-1.5587396123545605, 2.683901074764725],
            [-2.121320343559643, 2.121320343559643], [-2.683901074764724, 1.5587396123545616],
            [-2.999999999999999, 0.7956093000000027], [-3.0, 4.2398580646363365e-15]
        ]

    def draw(self, output_path=None, *, variant=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / (self.__class__.__name__ + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if variant not in self.variants:
                raise ValueError('Unknown Special variant: ' + str(variant))
            return getattr(self, 'draw_' + variant)(output_path)
        with Canvas(PLANE, xlim=(-3.4942872403427834, 3.4942872403427825), ylim=(-3.4942872403427834, 3.4942872403427825)) as c:
            c.path(self._samples_001, self._samples_002, alpha=0.45, zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), capstyle='butt')
            c.path(self._samples_001, self._samples_002, id='shade', capstyle='butt', fill=False)
            c.circle([0.0, 0.0], 3.0, id='circle_boundary', fill=False)
            for object_id, points in [('diameter', [[3.0, 0.0], [-3.0, 3.6739403974420594e-16]]), ('radius_1', [[0.0, 0.0], [2.4574561328669753, 1.7207293090531381]]), ('radius_2', [[0.0, 0.0], [1.8369701987210297e-16, 3.0]]), ('radius_3', [[0.0, 0.0], [-1.9283628290596182, 2.298133329356934]])]:
                c.line(points, id=object_id)
            c.point([[0.0, 0.0]], id='center_dot')
            for object_id, vertices, codes in [('angle_arc_0', [[0.5897957822723641, 0.0], [0.5897957822723641, 0.060164086425230384], [0.5805899247429073, 0.11997550320243593], [0.5624982350329643, 0.17735501225245942], [0.5444065453230211, 0.23473452130248293], [0.5176411230495321, 0.289009428582653], [0.48313242076143215, 0.33829296297066]], [1, 4, 4, 4, 4, 4, 4]), ('angle_arc_1', [[0.6786860196410593, 0.47522106703021283], [0.6022931087503933, 0.5843214504479455], [0.500707473351541, 0.673409661670903], [0.38256918306695303, 0.7349085630015768], [0.2644308927823652, 0.7964074643322507], [0.13318697570049975, 0.8285226465254637], [5.073238035442515e-17, 0.8285226465254637]], [1, 4, 4, 4, 4, 4, 4]), ('angle_arc_2', [[3.783431755245266e-17, 0.6178812957139052], [-0.0720757600526559, 0.6178812957139052], [-0.14359878945930318, 0.6052698558875084], [-0.21132784931831974, 0.5806184941039925], [-0.2790569091773363, 0.5559671323204765], [-0.341953205670049, 0.5196539386093783], [-0.39716644114196287, 0.4733245330887911]], [1, 4, 4, 4, 4, 4, 4])]:
                c.path(vertices, codes, id=object_id, zorder=3, capstyle='butt', fill=False)
            c.text('B', (3.0, 0.0), id='label_B', fontsize=18.0, fontstyle='italic', offset_pt=(18.0, 0.0))
            c.text('A', (-3.0, 3.6739403974420594e-16), id='label_A', fontsize=18.0, fontstyle='italic', offset_pt=(-18.0, 2.204364238465236e-15))
            c.text('O', (0.0, 0.0), id='label_O', fontsize=18.0, fontstyle='italic', offset_pt=(8.572527594031472e-16, -14.0))
            c.text('35°', (0.0, 0.0), id='angle_label_0', offset_pt=(78.2047899613546, 24.657875559350394))
            c.text('55°', (0.0, 0.0), id='angle_label_1', offset_pt=(44.32786687056326, 85.15303998510929))
            c.text('40°', (0.0, 0.0), id='angle_label_2', offset_pt=(-28.04565175270483, 77.05479490444449))
            return c.save(output_path)

    def _draw_choices(self, c, kw=None):
        _kw = kw or {}
        c.path(self._samples_001, self._samples_002, alpha=0.45, zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), capstyle='butt')
        c.path(self._samples_001, self._samples_002, id='shade', capstyle='butt', fill=False)
        c.path(self._samples_003, [1] + [4] * 12, id='circle_boundary', capstyle='butt', fill=False)
        c.path(self._samples_004, [1, 4, 4, 4, 4, 4, 4, 4, 4, 4], id='circle_boundary', capstyle='butt', fill=False, **_kw.get(3, {'edgecolor': '#DC2626', 'linewidth': 3.0}))
        c.path([[-3.0, 4.2398580646363365e-15], [-3.0, 2.8265720430908913e-15], [-3.0, 1.4132860215454458e-15], [-3.0, 0.0], [-3.0, -0.7956093000000001], [-2.683901074764725, -1.5587396123545605], [-2.121320343559643, -2.121320343559643], [-1.5587396123545605, -2.683901074764725], [-0.7956093000000001, -3.0], [0.0, -3.0]], [1, 4, 4, 4, 4, 4, 4, 4, 4, 4], id='circle_boundary', capstyle='butt', fill=False)
        c.path([[3.0, 0.0], [0.0, 1.8369701987210297e-16]], [1, 2], id='diameter', joinstyle='round', fill=False)
        c.path([[0.0, 1.8369701987210297e-16], [-3.0, 3.6739403974420594e-16]], [1, 2], id='diameter', joinstyle='round', fill=False, **_kw.get(6, {'edgecolor': '#DC2626', 'linewidth': 3.0}))
        c.line([[0.0, 0.0], [2.4574561328669753, 1.7207293090531381]], id='radius_1')
        c.line([[0.0, 0.0], [1.8369701987210297e-16, 3.0]], id='radius_2', **_kw.get(8, {'color': '#DC2626', 'linewidth': 3.0}))
        c.line([[0.0, 0.0], [-1.9283628290596182, 2.298133329356934]], id='radius_3')
        c.point([[0.0, 0.0]], id='center_dot')
        for object_id, vertices, codes in [('angle_arc_0', [[0.5897957822723641, 0.0], [0.5897957822723641, 0.060164086425230384], [0.5805899247429073, 0.11997550320243593], [0.5624982350329643, 0.17735501225245942], [0.5444065453230211, 0.23473452130248293], [0.5176411230495321, 0.289009428582653], [0.48313242076143215, 0.33829296297066]], [1, 4, 4, 4, 4, 4, 4]), ('angle_arc_1', [[0.6786860196410593, 0.47522106703021283], [0.6022931087503933, 0.5843214504479455], [0.500707473351541, 0.673409661670903], [0.38256918306695303, 0.7349085630015768], [0.2644308927823652, 0.7964074643322507], [0.13318697570049975, 0.8285226465254637], [5.073238035442515e-17, 0.8285226465254637]], [1, 4, 4, 4, 4, 4, 4]), ('angle_arc_2', [[3.783431755245266e-17, 0.6178812957139052], [-0.0720757600526559, 0.6178812957139052], [-0.14359878945930318, 0.6052698558875084], [-0.21132784931831974, 0.5806184941039925], [-0.2790569091773363, 0.5559671323204765], [-0.341953205670049, 0.5196539386093783], [-0.39716644114196287, 0.4733245330887911]], [1, 4, 4, 4, 4, 4, 4])]:
            c.path(vertices, codes, id=object_id, zorder=3, capstyle='butt', fill=False)
        c.text('B', (3.0, 0.0), id='label_B', fontsize=18.0, fontstyle='italic', offset_pt=(18.0, 0.0))
        c.text('A', (-3.0, 3.6739403974420594e-16), id='label_A', fontsize=18.0, fontstyle='italic', offset_pt=(-18.0, 2.204364238465236e-15))
        c.text('O', (0.0, 0.0), id='label_O', fontsize=18.0, fontstyle='italic', offset_pt=(8.572527594031472e-16, -14.0))
        c.text('35°', (0.0, 0.0), id='angle_label_0', offset_pt=(78.2047899613546, 24.657875559350394))
        c.text('55°', (0.0, 0.0), id='angle_label_1', offset_pt=(44.32786687056326, 85.15303998510929))
        c.text('40°', (0.0, 0.0), id='angle_label_2', offset_pt=(-28.04565175270483, 77.05479490444449))

    def draw_C01(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane132_C01.png'
        with Canvas(PLANE, xlim=(-3.4942872403427834, 3.4942872403427825), ylim=(-3.4942872403427834, 3.4942872403427825)) as c:
            self._draw_choices(c)
            return c.save(output_path)

    def draw_C02(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane132_C02.png'
        with Canvas(PLANE, xlim=(-3.4942872403427834, 3.4942872403427825), ylim=(-3.4942872403427834, 3.4942872403427825)) as c:
            self._draw_choices(c, kw={3: {'edgecolor': '#2563EB', 'linewidth': 3.0}, 6: {'edgecolor': '#2563EB', 'linewidth': 3.0}, 8: {'color': '#2563EB', 'linewidth': 3.0}})
            return c.save(output_path)

    def draw_C03(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane132_C03.png'
        with Canvas(PLANE, xlim=(-3.4942872403427834, 3.4942872403427825), ylim=(-3.4942872403427834, 3.4942872403427825)) as c:
            self._draw_choices(c, kw={3: {'edgecolor': '#16A34A', 'linewidth': 3.0}, 6: {'edgecolor': '#16A34A', 'linewidth': 3.0}, 8: {'color': '#16A34A', 'linewidth': 3.0}})
            return c.save(output_path)

    def draw_C04(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane132_C04.png'
        with Canvas(PLANE, xlim=(-3.4942872403427834, 3.4942872403427825), ylim=(-3.4942872403427834, 3.4942872403427825)) as c:
            self._draw_choices(c, kw={3: {'edgecolor': '#EA580C', 'linewidth': 3.0}, 6: {'edgecolor': '#EA580C', 'linewidth': 3.0}, 8: {'color': '#EA580C', 'linewidth': 3.0}})
            return c.save(output_path)

    def draw_C05(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane132_C05.png'
        with Canvas(PLANE, xlim=(-3.4942872403427834, 3.4942872403427825), ylim=(-3.4942872403427834, 3.4942872403427825)) as c:
            self._draw_choices(c, kw={3: {'edgecolor': '#DC2626', 'linewidth': 2.0}, 6: {'edgecolor': '#DC2626', 'linewidth': 2.0}, 8: {'color': '#DC2626', 'linewidth': 2.0}})
            return c.save(output_path)

    def draw_C06(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane132_C06.png'
        with Canvas(PLANE, xlim=(-3.4942872403427834, 3.4942872403427825), ylim=(-3.4942872403427834, 3.4942872403427825)) as c:
            self._draw_choices(c, kw={3: {'edgecolor': '#2563EB', 'linewidth': 2.0}, 6: {'edgecolor': '#2563EB', 'linewidth': 2.0}, 8: {'color': '#2563EB', 'linewidth': 2.0}})
            return c.save(output_path)
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Plane132')
    parser.add_argument('output', nargs='?')
    parser.add_argument('--variant', choices=('C01', 'C02', 'C03', 'C04', 'C05', 'C06'))
    args = parser.parse_args()
    print(Plane132().draw(args.output, variant=args.variant))
