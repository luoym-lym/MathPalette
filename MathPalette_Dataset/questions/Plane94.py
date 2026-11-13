"""Collected question Plane94; construction on the shared drawing protocol."""
from pathlib import Path
import sys
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from MathPalette_Dataset.drawing import Canvas, PLANE

class Plane94:
    variants = ('C01', 'C02', 'C03', 'C04', 'C05')

    def __init__(self):
        self.points = {
            'C': [-1.0, 0.45], 'B': [1.0, 0.45], 'A': [-1.0, -0.45], 'D': [1.0, -0.45],
            'J01': [-0.7071067811865475, 0.0], 'J02': [0.7071067811865476, 0.0]
        }

    def draw(self, output_path=None, *, variant=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / (self.__class__.__name__ + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if variant not in self.variants:
                raise ValueError('Unknown Special variant: ' + str(variant))
            return getattr(self, 'draw_' + variant)(output_path)
        with Canvas(PLANE, xlim=(-1.1497850639678173, 1.1497902978469967), ylim=(-1.1411083357346676, 1.1584670260801464)) as c:
            for object_id, vertices, codes in [('CB_s01_C_J01', [[-1.0, 0.45], [-0.9023689270621824, 0.27426406871192854], [-0.8047378541243649, 0.12426406871192855], [-0.7071067811865475, 0.0]], [1, 4, 4, 4]), ('CB_s02_J01_J02', [[-0.7071067811865475, 0.0], [-0.23570226039551587, -0.6], [0.2357022603955159, -0.5999999999999999], [0.7071067811865476, 0.0]], [1, 4, 4, 4]), ('CB_s03_J02_B', [[0.7071067811865476, 0.0], [0.804737854124365, 0.12426406871192856], [0.9023689270621825, 0.27426406871192854], [1.0, 0.45]], [1, 4, 4, 4]), ('AD_s01_A_J01', [[-1.0, -0.45], [-0.9023689270621824, -0.27426406871192854], [-0.8047378541243649, -0.12426406871192855], [-0.7071067811865475, 0.0]], [1, 4, 4, 4]), ('AD_s02_J01_J02', [[-0.7071067811865475, 0.0], [-0.23570226039551587, 0.6], [0.2357022603955159, 0.5999999999999999], [0.7071067811865476, 0.0]], [1, 4, 4, 4]), ('AD_s03_J02_D', [[0.7071067811865476, 0.0], [0.804737854124365, -0.12426406871192856], [0.9023689270621825, -0.27426406871192854], [1.0, -0.45]], [1, 4, 4, 4])]:
                c.path(vertices, codes, id=object_id, capstyle='butt', zorder=1)
            c.text('C', self.points['C'], offset_pt=(-8.0, -0.0), vertex=True, ha='right')
            c.text('B', self.points['B'], offset_pt=(8.0, 0.0), vertex=True, ha='left')
            c.text('A', self.points['A'], offset_pt=(-8.0, -0.0), vertex=True, ha='right')
            c.text('D', self.points['D'], offset_pt=(8.0, 0.0), vertex=True, ha='left')
            return c.save(output_path)

    def _draw_choices(self, c, hi=None):
        _hi = hi or {}
        _defs = [{}, {}, {}, {}, {}, {'edgecolor': '#DC2626'}]
        _ov = {j: s for idxs, s in _hi.get(0, ()) for j in idxs}
        for i, (object_id, vertices, codes) in enumerate([('CB_s01_C_J01', [[-1.0, 0.45], [-0.9023689270621824, 0.27426406871192854], [-0.8047378541243649, 0.12426406871192855], [-0.7071067811865475, 0.0]], [1, 4, 4, 4]), ('CB_s02_J01_J02', [[-0.7071067811865475, 0.0], [-0.23570226039551587, -0.6], [0.2357022603955159, -0.5999999999999999], [0.7071067811865476, 0.0]], [1, 4, 4, 4]), ('CB_s03_J02_B', [[0.7071067811865476, 0.0], [0.804737854124365, 0.12426406871192856], [0.9023689270621825, 0.27426406871192854], [1.0, 0.45]], [1, 4, 4, 4]), ('AD_s01_A_J01', [[-1.0, -0.45], [-0.9023689270621824, -0.27426406871192854], [-0.8047378541243649, -0.12426406871192855], [-0.7071067811865475, 0.0]], [1, 4, 4, 4]), ('AD_s02_J01_J02', [[-0.7071067811865475, 0.0], [-0.23570226039551587, 0.6], [0.2357022603955159, 0.5999999999999999], [0.7071067811865476, 0.0]], [1, 4, 4, 4]), ('AD_s03_J02_D', [[0.7071067811865476, 0.0], [0.804737854124365, -0.12426406871192856], [0.9023689270621825, -0.27426406871192854], [1.0, -0.45]], [1, 4, 4, 4])]):
            c.path(vertices, codes, id=object_id, zorder=1, capstyle='butt', **_ov.get(i, _defs[i]))
        c.text('C', (-1.0, 0.45), zorder=3, clip_on=True, fontsize=18.0, fontstyle='italic', ha='right', offset_pt=(-8.0, -0.0), annotation_clip=False)
        c.text('B', (1.0, 0.45), zorder=3, clip_on=True, fontsize=18.0, fontstyle='italic', ha='left', offset_pt=(8.0, 0.0), annotation_clip=False)
        c.text('A', (-1.0, -0.45), zorder=3, clip_on=True, fontsize=18.0, fontstyle='italic', ha='right', offset_pt=(-8.0, -0.0), annotation_clip=False)
        c.text('D', (1.0, -0.45), zorder=3, clip_on=True, fontsize=18.0, fontstyle='italic', ha='left', offset_pt=(8.0, 0.0), annotation_clip=False)

    def draw_C01(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane94_C01.png'
        with Canvas(PLANE, xlim=(-1.1497850639678173, 1.1497902978469967), ylim=(-1.1411083357346676, 1.1584670260801464)) as c:
            self._draw_choices(c, hi={0: [({0, 4}, {'edgecolor': '#DC2626'})]})
            return c.save(output_path)

    def draw_C02(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane94_C02.png'
        with Canvas(PLANE, xlim=(-1.1497850639678173, 1.1497902978469967), ylim=(-1.1411083357346676, 1.1584670260801464)) as c:
            self._draw_choices(c, hi={0: [({1, 2, 3}, {'edgecolor': '#2563EB'}), ({5}, {})]})
            return c.save(output_path)

    def draw_C03(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane94_C03.png'
        with Canvas(PLANE, xlim=(-1.1497850639678173, 1.1497902978469967), ylim=(-1.1411083357346676, 1.1584670260801464)) as c:
            self._draw_choices(c, hi={0: [({1, 2, 3}, {'linestyle': (0, [3.7, 1.6])}), ({5}, {})]})
            return c.save(output_path)

    def draw_C04(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane94_C04.png'
        with Canvas(PLANE, xlim=(-1.1497850639678173, 1.1497902978469967), ylim=(-1.1411083357346676, 1.1584670260801464)) as c:
            self._draw_choices(c, hi={0: [({2}, {'edgecolor': '#DC2626'})]})
            return c.save(output_path)

    def draw_C05(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane94_C05.png'
        with Canvas(PLANE, xlim=(-1.1497850639678173, 1.1497902978469967), ylim=(-1.1411083357346676, 1.1584670260801464)) as c:
            self._draw_choices(c, hi={0: [({0, 3}, {'edgecolor': '#16A34A'}), ({2, 5}, {'edgecolor': '#EA580C'})]})
            return c.save(output_path)
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Plane94')
    parser.add_argument('output', nargs='?')
    parser.add_argument('--variant', choices=('C01', 'C02', 'C03', 'C04', 'C05'))
    args = parser.parse_args()
    print(Plane94().draw(args.output, variant=args.variant))
