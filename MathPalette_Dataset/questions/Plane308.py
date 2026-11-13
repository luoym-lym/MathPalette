"""Collected question Plane308; construction on the shared drawing protocol."""
from pathlib import Path
import sys
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from MathPalette_Dataset.drawing import Canvas, PLANE

class Plane308:
    variants = ('C01', 'C02', 'C03', 'C04', 'C05')

    def _draw_base(self, c, hi=None, kw=None):
        _hi = hi or {}
        _kw = kw or {}
        _ov = {j: s for idxs, s in _hi.get(0, ()) for j in idxs}
        for i, (object_id, center, radius) in enumerate([('source_dot1', [9.0, 6.732050807568877], 0.04), ('source_dot2', [8.0, 5.0], 0.04), ('source_dot6', [9.0, 3.267949192431123], 0.04), ('source_dot3', [11.0, 3.267949192431123], 0.04), ('source_dot4', [12.0, 5.0], 0.04), ('source_dot5', [11.0, 6.732050807568877], 0.04)]):
            c.circle(center, radius, id=object_id, facecolor='black', **_ov[i]) if i in _ov else c.circle(center, radius, id=object_id, facecolor='black')
        c.path([[-0.5, 0.8660254037844386], [-1.0, 0.0], [0.5, -0.8660254037844386], [-0.5, 0.8660254037844386]], [1, 2, 2, 79], id='option0_0', alpha=0.5, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
        c.path([[-0.5, 0.8660254037844386], [-1.0, 0.0], [0.5, -0.8660254037844386], [-0.5, 0.8660254037844386]], [1, 2, 2, 79], id='option0_0', capstyle='butt', fill=False, **_kw.get(2, {'edgecolor': '#2563EB', 'linewidth': 1.5}))
        c.path([[0.5, 0.8660254037844386], [1.0, 0.0], [-0.5, -0.8660254037844386], [0.5, 0.8660254037844386]], [1, 2, 2, 79], id='option0_1', alpha=0.5, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
        c.path([[0.5, 0.8660254037844386], [1.0, 0.0], [-0.5, -0.8660254037844386], [0.5, 0.8660254037844386]], [1, 2, 2, 79], id='option0_1', capstyle='butt', fill=False, **_kw.get(4, {'edgecolor': '#DC2626', 'linewidth': 1.5}))
        _ov = {j: s for idxs, s in _hi.get(5, ()) for j in idxs}
        for i, (object_id, center, radius) in enumerate([('dot0_1', [-0.5, 0.8660254037844386], 0.04), ('dot0_2', [-1.0, 0.0], 0.04), ('dot0_6', [-0.5, -0.8660254037844386], 0.04), ('dot0_3', [0.5, -0.8660254037844386], 0.04), ('dot0_4', [1.0, 0.0], 0.04), ('dot0_5', [0.5, 0.8660254037844386], 0.04)]):
            c.circle(center, radius, id=object_id, facecolor='black', **_ov[i]) if i in _ov else c.circle(center, radius, id=object_id, facecolor='black')
        c.path([[4.5, 0.8660254037844386], [5.5, 0.8660254037844386], [4.5, -0.8660254037844386], [4.5, 0.8660254037844386]], [1, 2, 2, 79], id='option1_0', alpha=0.5, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
        c.path([[4.5, 0.8660254037844386], [5.5, 0.8660254037844386], [4.5, -0.8660254037844386], [4.5, 0.8660254037844386]], [1, 2, 2, 79], id='option1_0', capstyle='butt', fill=False)
        c.path([[4.0, 0.0], [6.0, 0.0], [5.5, -0.8660254037844386], [4.0, 0.0]], [1, 2, 2, 79], id='option1_1', alpha=0.5, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
        c.path([[4.0, 0.0], [6.0, 0.0], [5.5, -0.8660254037844386], [4.0, 0.0]], [1, 2, 2, 79], id='option1_1', capstyle='butt', fill=False)
        for object_id, center, radius in [('dot1_1', [4.5, 0.8660254037844386], 0.04), ('dot1_2', [4.0, 0.0], 0.04), ('dot1_6', [4.5, -0.8660254037844386], 0.04), ('dot1_3', [5.5, -0.8660254037844386], 0.04), ('dot1_4', [6.0, 0.0], 0.04), ('dot1_5', [5.5, 0.8660254037844386], 0.04)]:
            c.circle(center, radius, id=object_id, facecolor='black')
        c.path([[9.5, 0.8660254037844386], [9.0, 0.0], [11.0, 0.0], [9.5, 0.8660254037844386]], [1, 2, 2, 79], id='option2_0', alpha=0.5, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
        c.path([[9.5, 0.8660254037844386], [9.0, 0.0], [11.0, 0.0], [9.5, 0.8660254037844386]], [1, 2, 2, 79], id='option2_0', capstyle='butt', fill=False)
        c.path([[10.5, 0.8660254037844386], [9.5, -0.8660254037844386], [10.5, -0.8660254037844386], [10.5, 0.8660254037844386]], [1, 2, 2, 79], id='option2_1', alpha=0.5, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
        c.path([[10.5, 0.8660254037844386], [9.5, -0.8660254037844386], [10.5, -0.8660254037844386], [10.5, 0.8660254037844386]], [1, 2, 2, 79], id='option2_1', capstyle='butt', fill=False)
        for object_id, center, radius in [('dot2_1', [9.5, 0.8660254037844386], 0.04), ('dot2_2', [9.0, 0.0], 0.04), ('dot2_6', [9.5, -0.8660254037844386], 0.04), ('dot2_3', [10.5, -0.8660254037844386], 0.04), ('dot2_4', [11.0, 0.0], 0.04), ('dot2_5', [10.5, 0.8660254037844386], 0.04)]:
            c.circle(center, radius, id=object_id, facecolor='black')
        c.path([[14.5, 0.8660254037844386], [16.0, 0.0], [15.5, -0.8660254037844386], [14.5, 0.8660254037844386]], [1, 2, 2, 79], id='option3_0', alpha=0.5, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
        c.path([[14.5, 0.8660254037844386], [16.0, 0.0], [15.5, -0.8660254037844386], [14.5, 0.8660254037844386]], [1, 2, 2, 79], id='option3_0', capstyle='butt', fill=False)
        c.path([[15.5, 0.8660254037844386], [14.0, 0.0], [14.5, -0.8660254037844386], [15.5, 0.8660254037844386]], [1, 2, 2, 79], id='option3_1', alpha=0.5, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
        c.path([[15.5, 0.8660254037844386], [14.0, 0.0], [14.5, -0.8660254037844386], [15.5, 0.8660254037844386]], [1, 2, 2, 79], id='option3_1', capstyle='butt', fill=False)
        for object_id, center, radius in [('dot3_1', [14.5, 0.8660254037844386], 0.04), ('dot3_2', [14.0, 0.0], 0.04), ('dot3_6', [14.5, -0.8660254037844386], 0.04), ('dot3_3', [15.5, -0.8660254037844386], 0.04), ('dot3_4', [16.0, 0.0], 0.04), ('dot3_5', [15.5, 0.8660254037844386], 0.04)]:
            c.circle(center, radius, id=object_id, facecolor='black')
        c.path([[19.5, 0.8660254037844386], [20.5, 0.8660254037844386], [20.5, -0.8660254037844386], [19.5, 0.8660254037844386]], [1, 2, 2, 79], id='option4_0', alpha=0.5, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
        c.path([[19.5, 0.8660254037844386], [20.5, 0.8660254037844386], [20.5, -0.8660254037844386], [19.5, 0.8660254037844386]], [1, 2, 2, 79], id='option4_0', capstyle='butt', fill=False)
        c.path([[19.0, 0.0], [21.0, 0.0], [19.5, -0.8660254037844386], [19.0, 0.0]], [1, 2, 2, 79], id='option4_1', alpha=0.5, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
        c.path([[19.0, 0.0], [21.0, 0.0], [19.5, -0.8660254037844386], [19.0, 0.0]], [1, 2, 2, 79], id='option4_1', capstyle='butt', fill=False)
        for object_id, center, radius in [('dot4_1', [19.5, 0.8660254037844386], 0.04), ('dot4_2', [19.0, 0.0], 0.04), ('dot4_6', [19.5, -0.8660254037844386], 0.04), ('dot4_3', [20.5, -0.8660254037844386], 0.04), ('dot4_4', [21.0, 0.0], 0.04), ('dot4_5', [20.5, 0.8660254037844386], 0.04)]:
            c.circle(center, radius, id=object_id, facecolor='black')
        for object_id, text, anchor in [('label0', '1', (8.55, 7.132050807568877)), ('label1', '2', (7.55, 5.0)), ('label2', '6', (8.55, 2.867949192431123)), ('label3', '3', (11.45, 2.867949192431123)), ('label4', '4', (12.45, 5.0)), ('label5', '5', (11.45, 7.132050807568877)), ('label6', '(A)', (-1.7, -0.8)), ('label7', '(B)', (3.3, -0.8)), ('label8', '(C)', (8.3, -0.8)), ('label9', '(D)', (13.3, -0.8)), ('label10', '(E)', (18.3, -0.8))]:
            c.text(text, anchor, id=object_id)

    def draw(self, output_path=None, *, variant=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / (self.__class__.__name__ + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if variant not in self.variants:
                raise ValueError('Unknown Special variant: ' + str(variant))
            return getattr(self, 'draw_' + variant)(output_path)
        with Canvas(PLANE, xlim=(-2.741648736260336, 21.60590377298287), ylim=(-8.988760979535469, 15.358791529707736)) as c:
            self._draw_base(c, kw={2: {}, 4: {}})
            return c.save(output_path)

    def draw_C01(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane308_C01.png'
        with Canvas(PLANE, xlim=(-2.741648736260336, 21.60590377298287), ylim=(-8.988760979535469, 15.358791529707736)) as c:
            self._draw_base(c, hi={0: [({0, 3, 5}, {'edgecolor': '#DC2626'}), ({1, 2, 4}, {'edgecolor': '#2563EB'})]})
            return c.save(output_path)

    def draw_C02(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane308_C02.png'
        with Canvas(PLANE, xlim=(-2.741648736260336, 21.60590377298287), ylim=(-8.988760979535469, 15.358791529707736)) as c:
            self._draw_base(c, hi={0: [({0, 3, 5}, {'edgecolor': '#DC2626', 'linewidth': 1.5}), ({1, 2, 4}, {'edgecolor': '#2563EB', 'linewidth': 1.5})], 5: [({0, 1, 3}, {'edgecolor': '#2563EB', 'linewidth': 1.5}), ({2, 4, 5}, {'edgecolor': '#DC2626', 'linewidth': 1.5})]})
            return c.save(output_path)

    def draw_C03(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane308_C03.png'
        with Canvas(PLANE, xlim=(-2.741648736260336, 21.60590377298287), ylim=(-8.988760979535469, 15.358791529707736)) as c:
            self._draw_base(c, hi={0: [({0, 3, 5}, {'edgecolor': '#DC2626', 'linewidth': 1.5})]})
            return c.save(output_path)

    def draw_C04(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane308_C04.png'
        with Canvas(PLANE, xlim=(-2.741648736260336, 21.60590377298287), ylim=(-8.988760979535469, 15.358791529707736)) as c:
            self._draw_base(c, hi={0: [({1, 2, 4}, {'edgecolor': '#2563EB', 'linewidth': 1.5})]})
            return c.save(output_path)

    def draw_C05(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane308_C05.png'
        with Canvas(PLANE, xlim=(-2.741648736260336, 21.60590377298287), ylim=(-8.988760979535469, 15.358791529707736)) as c:
            self._draw_base(c, hi={0: [({0, 3, 5}, {'edgecolor': '#2563EB'}), ({1, 2, 4}, {'edgecolor': '#DC2626'})]}, kw={2: {'edgecolor': '#DC2626', 'linewidth': 1.5}, 4: {'edgecolor': '#2563EB', 'linewidth': 1.5}})
            return c.save(output_path)
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Plane308')
    parser.add_argument('output', nargs='?')
    parser.add_argument('--variant', choices=('C01', 'C02', 'C03', 'C04', 'C05'))
    args = parser.parse_args()
    print(Plane308().draw(args.output, variant=args.variant))
