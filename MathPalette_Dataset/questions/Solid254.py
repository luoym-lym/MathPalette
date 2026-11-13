"""Collected question Solid254; construction on the shared drawing protocol."""
from pathlib import Path
import sys
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from MathPalette_Dataset.drawing import Canvas, SOLID

class Solid254:
    variants = ('C01',)

    def _draw_base(self, c, hi=None, kw=None):
        _hi = hi or {}
        _kw = kw or {}
        c.line([[-1.5, 0.8660254037844386], [-1.0, 0.0]], id='edge00', zorder=1, **_kw.get(0, {}))
        c.text('x', (-1.4145448267190432, 0.3380127018922193), zorder=2)
        for object_id, points in [('edge01', [[-1.5, 0.8660254037844386], [-0.5, 0.8660254037844386]]), ('edge02', [[-1.0, 0.0], [-0.5, 0.8660254037844386]]), ('edge03', [[-1.0, 0.0], [0.0, 0.0]])]:
            c.line(points, id=object_id, zorder=1)
        c.text('C', (-0.5, -0.19), zorder=2)
        _ov = {j: s for idxs, s in _hi.get(4, ()) for j in idxs}
        for i, (object_id, points) in enumerate([('edge04', [[-0.5, 0.8660254037844386], [0.0, 1.7320508075688772]]), ('edge05', [[-0.5, 0.8660254037844386], [0.0, 0.0]]), ('edge06', [[-0.5, 0.8660254037844386], [0.5, 0.8660254037844386]]), ('edge07', [[0.0, 1.7320508075688772], [0.5, 0.8660254037844386]]), ('edge08', [[0.0, 0.0], [0.5, 0.8660254037844386]]), ('edge09', [[0.0, 0.0], [0.5, -0.8660254037844386]]), ('edge10', [[0.0, 0.0], [1.0, 0.0]]), ('edge11', [[0.5, 0.8660254037844386], [1.0, 0.0]]), ('edge12', [[0.5, 0.8660254037844386], [1.5, 0.8660254037844386]])]):
            c.line(points, id=object_id, zorder=1, **_ov[i]) if i in _ov else c.line(points, id=object_id, zorder=1)
        c.text('E', (1.0, 1.0560254037844385), zorder=2)
        c.line([[0.5, -0.8660254037844386], [1.0, 0.0]], id='edge13', zorder=1)
        c.text('D', (0.9145448267190434, -0.5280127018922193), zorder=2)
        c.line([[1.0, 0.0], [1.5, 0.8660254037844386]], id='edge14', zorder=1)
        c.line([[1.0, 0.0], [2.0, 0.0]], id='edge15', zorder=1)
        c.text('A', (1.5, -0.19), zorder=2)
        c.line([[1.5, 0.8660254037844386], [2.0, 0.0]], id='edge16', zorder=1)
        c.text('B', (1.9145448267190432, 0.5280127018922193), zorder=2)

    def draw(self, output_path=None, *, variant=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / (self.__class__.__name__ + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if variant not in self.variants:
                raise ValueError('Unknown Special variant: ' + str(variant))
            return getattr(self, 'draw_' + variant)(output_path)
        with Canvas(SOLID, xlim=(-2.025, 2.525), ylim=(-1.8419872981077807, 2.708012701892219)) as c:
            self._draw_base(c)
            return c.save(output_path)

    def draw_C01(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Solid254_C01.png'
        with Canvas(SOLID, xlim=(-2.025, 2.525), ylim=(-1.8419872981077807, 2.708012701892219)) as c:
            self._draw_base(c, hi={4: [({8}, {'color': '#DC2626', 'linewidth': 3.0})]}, kw={0: {'color': '#DC2626', 'linewidth': 3.0}})
            c.point([[-1.5, 0.8660254037844386]], zorder=10, s=50, facecolors='#2563EB', edgecolors='#2563EB')
            c.point([[1.5, 0.8660254037844386]], zorder=10, s=50, facecolors='#2563EB', edgecolors='#2563EB')
            return c.save(output_path)
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Solid254')
    parser.add_argument('output', nargs='?')
    parser.add_argument('--variant', choices=('C01',))
    args = parser.parse_args()
    print(Solid254().draw(args.output, variant=args.variant))
