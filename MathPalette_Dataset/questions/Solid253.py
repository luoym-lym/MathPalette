"""Collected question Solid253; construction on the shared drawing protocol."""
from pathlib import Path
import sys
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from MathPalette_Dataset.drawing import Canvas, SOLID

class Solid253:
    variants = ('C01', 'C02')

    def _draw_base(self, c, kw=None, custom=None):
        _kw = kw or {}
        if custom and 0 in custom:
            custom[0](c)
        else:
            c.line([[-1.0, 0.0], [-0.5, 0.8660254037844386]], id='edge00', zorder=1)
        c.text('D', (-0.9145448267190434, 0.5280127018922193), zorder=2)
        c.line([[-1.0, 0.0], [0.0, 0.0]], id='edge01', zorder=1)
        c.text('C', (-0.5, -0.19), zorder=2)
        if custom and 4 in custom:
            custom[4](c)
        else:
            for object_id, points in [('edge02', [[-0.5, 0.8660254037844386], [0.0, 0.0]]), ('edge03', [[-0.5, 0.8660254037844386], [0.5, 0.8660254037844386]]), ('edge04', [[0.0, 0.0], [0.5, 0.8660254037844386]]), ('edge05', [[0.0, 0.0], [0.5, -0.8660254037844386]])]:
                c.line(points, id=object_id, zorder=1)
        c.text('x', (0.08545517328095664, -0.5280127018922193), zorder=2)
        for object_id, points in [('edge06', [[0.0, 0.0], [1.0, 0.0]]), ('edge07', [[0.5, 0.8660254037844386], [1.0, 1.7320508075688772]]), ('edge08', [[0.5, 0.8660254037844386], [1.0, 0.0]]), ('edge09', [[0.5, 0.8660254037844386], [1.5, 0.8660254037844386]]), ('edge10', [[1.0, 1.7320508075688772], [1.5, 0.8660254037844386]])]:
            c.line(points, id=object_id, zorder=1)
        c.text('E', (1.4145448267190432, 1.394038105676658), zorder=2)
        for object_id, points in [('edge11', [[0.5, -0.8660254037844386], [1.0, 0.0]]), ('edge12', [[0.5, -0.8660254037844386], [1.0, -1.7320508075688772]]), ('edge13', [[0.5, -0.8660254037844386], [1.5, -0.8660254037844386]]), ('edge14', [[1.0, 0.0], [1.5, 0.8660254037844386]])]:
            c.line(points, id=object_id, zorder=1)
        c.text('B', (1.4145448267190432, 0.3380127018922193), zorder=2)
        c.line([[1.0, 0.0], [1.5, -0.8660254037844386]], id='edge15', zorder=1)
        c.line([[1.0, -1.7320508075688772], [1.5, -0.8660254037844386]], id='edge16', zorder=1, **_kw.get(11, {}))
        c.text('A', (1.4145448267190432, -1.394038105676658), zorder=2)

    def draw(self, output_path=None, *, variant=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / (self.__class__.__name__ + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if variant not in self.variants:
                raise ValueError('Unknown Special variant: ' + str(variant))
            return getattr(self, 'draw_' + variant)(output_path)
        with Canvas(SOLID, xlim=(-2.007050807568877, 2.507050807568877), ylim=(-2.257050807568877, 2.257050807568877)) as c:
            self._draw_base(c)
            return c.save(output_path)

    def draw_C01(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Solid253_C01.png'
        with Canvas(SOLID, xlim=(-2.007050807568877, 2.507050807568877), ylim=(-2.257050807568877, 2.257050807568877)) as c:

            def _slot_4(c):
                for object_id, points in [('edge02', [[-0.5, 0.8660254037844386], [0.0, 0.0]]), ('edge03', [[-0.5, 0.8660254037844386], [0.5, 0.8660254037844386]]), ('edge04', [[0.0, 0.0], [0.5, 0.8660254037844386]])]:
                    c.line(points, id=object_id, zorder=1)
                c.line([[0.0, 0.0], [0.5, -0.8660254037844386]], id='edge05', zorder=1, color='#2563EB', linewidth=2.0)
            self._draw_base(c, custom={4: _slot_4}, kw={11: {'color': '#2563EB', 'linewidth': 2.0}})
            return c.save(output_path)

    def draw_C02(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Solid253_C02.png'
        with Canvas(SOLID, xlim=(-2.007050807568877, 2.507050807568877), ylim=(-2.257050807568877, 2.257050807568877)) as c:

            def _slot_0(c):
                c.path([[-0.9999999999999994, -4.440892098500626e-16], [-0.8349999999999994, 0.2857883832488643]], [1, 2], id='edge00', zorder=1, edgecolor='#DC2626', linewidth=3.0, joinstyle='round', fill=False)
                c.path([[-0.8349999999999994, 0.2857883832488643], [-0.4999999999999995, 0.866025403784438]], [1, 2], id='edge00', zorder=1, joinstyle='round', fill=False)

            def _slot_4(c):
                for object_id, points in [('edge02', [[-0.5, 0.8660254037844386], [0.0, 0.0]]), ('edge03', [[-0.5, 0.8660254037844386], [0.5, 0.8660254037844386]]), ('edge04', [[0.0, 0.0], [0.5, 0.8660254037844386]])]:
                    c.line(points, id=object_id, zorder=1)
                c.path([[4.440892098500626e-16, -4.440892098500626e-16], [0.33500000000000046, -0.5802370205355742]], [1, 2], id='edge05', zorder=1, joinstyle='round', fill=False)
                c.path([[0.33500000000000046, -0.5802370205355742], [0.5000000000000004, -0.8660254037844389]], [1, 2], id='edge05', zorder=1, edgecolor='#DC2626', linewidth=3.0, joinstyle='round', fill=False)
            self._draw_base(c, custom={0: _slot_0, 4: _slot_4})
            return c.save(output_path)
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Solid253')
    parser.add_argument('output', nargs='?')
    parser.add_argument('--variant', choices=('C01', 'C02'))
    args = parser.parse_args()
    print(Solid253().draw(args.output, variant=args.variant))
