"""Collected question Plane200; construction on the shared drawing protocol."""
from pathlib import Path
import sys
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from MathPalette_Dataset.drawing import Canvas, PLANE

class Plane200:
    variants = ('C01', 'C02', 'C03', 'C04', 'C05', 'C06')

    def draw(self, output_path=None, *, variant=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / (self.__class__.__name__ + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if variant not in self.variants:
                raise ValueError('Unknown Special variant: ' + str(variant))
            return getattr(self, 'draw_' + variant)(output_path)
        with Canvas(PLANE, xlim=(-1.4878458591050734, 18.994709910248375), ylim=(-8.505176642386582, 11.977379126966868)) as c:
            for object_id, center, radius in [('tri0', [0.0, 0.0], 1), ('tri1', [2.0, 0.0], 1), ('tri2', [4.0, 0.0], 1), ('tri3', [1.0, 1.7320508075688772], 1), ('tri4', [3.0, 1.7320508075688772], 1), ('tri5', [2.0, 3.4641016151377544], 1), ('hex0', [17.5, 1.7320508075688772], 1), ('hex1', [16.5, 3.4641016151377544], 1), ('hex2', [14.5, 3.4641016151377544], 1), ('hex3', [13.5, 1.7320508075688774], 1), ('hex4', [14.5, 4.440892098500626e-16], 1), ('hex5', [16.5, 0.0], 1)]:
                c.circle(center, radius, id=object_id)
            c.path([[6.5, 1.2320508075688772], [10.5, 1.2320508075688772], [10.5, 0.7320508075688772], [11.5, 1.7320508075688772], [10.5, 2.732050807568877], [10.5, 2.232050807568877], [6.5, 2.232050807568877], [6.5, 1.2320508075688772]], [1, 2, 2, 2, 2, 2, 2, 79], id='transformation_arrow')
            return c.save(output_path)

    def draw_C01(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane200_C01.png'
        with Canvas(PLANE, xlim=(-1.4878458591050734, 18.994709910248375), ylim=(-8.505176642386582, 11.977379126966868)) as c:
            c.circle([0.0, 0.0], 1.0, id='tri0', edgecolor='#DC2626')
            c.circle([2.0, 0.0], 1.0, id='tri1')
            c.circle([4.0, 0.0], 1.0, id='tri2', edgecolor='#DC2626')
            c.circle([1.0, 1.7320508075688772], 1.0, id='tri3')
            c.circle([3.0, 1.7320508075688772], 1.0, id='tri4')
            c.circle([2.0, 3.4641016151377544], 1.0, id='tri5', edgecolor='#DC2626')
            for object_id, center, radius in [('hex0', [17.5, 1.7320508075688772], 1.0), ('hex1', [16.5, 3.4641016151377544], 1.0), ('hex2', [14.5, 3.4641016151377544], 1.0), ('hex3', [13.5, 1.7320508075688774], 1.0), ('hex4', [14.5, 4.440892098500626e-16], 1.0), ('hex5', [16.5, 0.0], 1.0)]:
                c.circle(center, radius, id=object_id)
            c.path([[6.5, 1.2320508075688772], [10.5, 1.2320508075688772], [10.5, 0.7320508075688772], [11.5, 1.7320508075688772], [10.5, 2.732050807568877], [10.5, 2.232050807568877], [6.5, 2.232050807568877], [6.5, 1.2320508075688772]], [1, 2, 2, 2, 2, 2, 2, 79], id='transformation_arrow', capstyle='butt')
            return c.save(output_path)

    def draw_C02(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane200_C02.png'
        with Canvas(PLANE, xlim=(-1.4878458591050734, 18.994709910248375), ylim=(-8.505176642386582, 11.977379126966868)) as c:
            c.circle([0.0, 0.0], 1.0, id='tri0')
            c.circle([2.0, 0.0], 1.0, id='tri1', edgecolor='#DC2626')
            c.circle([4.0, 0.0], 1.0, id='tri2')
            c.circle([1.0, 1.7320508075688772], 1.0, id='tri3', edgecolor='#DC2626')
            c.circle([3.0, 1.7320508075688772], 1.0, id='tri4', edgecolor='#DC2626')
            for object_id, center, radius in [('tri5', [2.0, 3.4641016151377544], 1.0), ('hex0', [17.5, 1.7320508075688772], 1.0), ('hex1', [16.5, 3.4641016151377544], 1.0), ('hex2', [14.5, 3.4641016151377544], 1.0), ('hex3', [13.5, 1.7320508075688774], 1.0), ('hex4', [14.5, 4.440892098500626e-16], 1.0), ('hex5', [16.5, 0.0], 1.0)]:
                c.circle(center, radius, id=object_id)
            c.path([[6.5, 1.2320508075688772], [10.5, 1.2320508075688772], [10.5, 0.7320508075688772], [11.5, 1.7320508075688772], [10.5, 2.732050807568877], [10.5, 2.232050807568877], [6.5, 2.232050807568877], [6.5, 1.2320508075688772]], [1, 2, 2, 2, 2, 2, 2, 79], id='transformation_arrow', capstyle='butt')
            return c.save(output_path)

    def draw_C03(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane200_C03.png'
        with Canvas(PLANE, xlim=(-1.4878458591050734, 18.994709910248375), ylim=(-8.505176642386582, 11.977379126966868)) as c:
            for object_id, center, radius in [('tri0', [0.0, 0.0], 1.0), ('tri1', [2.0, 0.0], 1.0), ('tri2', [4.0, 0.0], 1.0), ('tri3', [1.0, 1.7320508075688772], 1.0), ('tri4', [3.0, 1.7320508075688772], 1.0), ('tri5', [2.0, 3.4641016151377544], 1.0), ('hex0', [17.5, 1.7320508075688772], 1.0)]:
                c.circle(center, radius, id=object_id)
            c.circle([16.5, 3.4641016151377544], 1.0, id='hex1', edgecolor='#DC2626')
            c.circle([14.5, 3.4641016151377544], 1.0, id='hex2', edgecolor='#DC2626')
            c.circle([13.5, 1.7320508075688774], 1.0, id='hex3')
            c.circle([14.5, 4.440892098500626e-16], 1.0, id='hex4', edgecolor='#DC2626')
            c.circle([16.5, 0.0], 1.0, id='hex5', edgecolor='#DC2626')
            c.path([[6.5, 1.2320508075688772], [10.5, 1.2320508075688772], [10.5, 0.7320508075688772], [11.5, 1.7320508075688772], [10.5, 2.732050807568877], [10.5, 2.232050807568877], [6.5, 2.232050807568877], [6.5, 1.2320508075688772]], [1, 2, 2, 2, 2, 2, 2, 79], id='transformation_arrow', capstyle='butt')
            return c.save(output_path)

    def draw_C04(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane200_C04.png'
        with Canvas(PLANE, xlim=(-1.4878458591050734, 18.994709910248375), ylim=(-8.505176642386582, 11.977379126966868)) as c:
            c.circle([0.0, 0.0], 1.0, id='tri0')
            c.circle([2.0, 0.0], 1.0, id='tri1', edgecolor='#2563EB')
            c.circle([4.0, 0.0], 1.0, id='tri2')
            c.circle([1.0, 1.7320508075688772], 1.0, id='tri3', edgecolor='#2563EB')
            c.circle([3.0, 1.7320508075688772], 1.0, id='tri4', edgecolor='#2563EB')
            for object_id, center, radius in [('tri5', [2.0, 3.4641016151377544], 1.0), ('hex0', [17.5, 1.7320508075688772], 1.0), ('hex1', [16.5, 3.4641016151377544], 1.0), ('hex2', [14.5, 3.4641016151377544], 1.0), ('hex3', [13.5, 1.7320508075688774], 1.0), ('hex4', [14.5, 4.440892098500626e-16], 1.0), ('hex5', [16.5, 0.0], 1.0)]:
                c.circle(center, radius, id=object_id)
            c.path([[6.5, 1.2320508075688772], [10.5, 1.2320508075688772], [10.5, 0.7320508075688772], [11.5, 1.7320508075688772], [10.5, 2.732050807568877], [10.5, 2.232050807568877], [6.5, 2.232050807568877], [6.5, 1.2320508075688772]], [1, 2, 2, 2, 2, 2, 2, 79], id='transformation_arrow', capstyle='butt')
            return c.save(output_path)

    def draw_C05(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane200_C05.png'
        with Canvas(PLANE, xlim=(-1.4878458591050734, 18.994709910248375), ylim=(-8.505176642386582, 11.977379126966868)) as c:
            c.circle([0.0, 0.0], 1.0, id='tri0', edgecolor='#16A34A')
            c.circle([2.0, 0.0], 1.0, id='tri1')
            c.circle([4.0, 0.0], 1.0, id='tri2', edgecolor='#16A34A')
            c.circle([1.0, 1.7320508075688772], 1.0, id='tri3')
            c.circle([3.0, 1.7320508075688772], 1.0, id='tri4')
            c.circle([2.0, 3.4641016151377544], 1.0, id='tri5', edgecolor='#16A34A')
            for object_id, center, radius in [('hex0', [17.5, 1.7320508075688772], 1.0), ('hex1', [16.5, 3.4641016151377544], 1.0), ('hex2', [14.5, 3.4641016151377544], 1.0), ('hex3', [13.5, 1.7320508075688774], 1.0), ('hex4', [14.5, 4.440892098500626e-16], 1.0), ('hex5', [16.5, 0.0], 1.0)]:
                c.circle(center, radius, id=object_id)
            c.path([[6.5, 1.2320508075688772], [10.5, 1.2320508075688772], [10.5, 0.7320508075688772], [11.5, 1.7320508075688772], [10.5, 2.732050807568877], [10.5, 2.232050807568877], [6.5, 2.232050807568877], [6.5, 1.2320508075688772]], [1, 2, 2, 2, 2, 2, 2, 79], id='transformation_arrow', capstyle='butt')
            return c.save(output_path)

    def draw_C06(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane200_C06.png'
        with Canvas(PLANE, xlim=(-1.4878458591050734, 18.994709910248375), ylim=(-8.505176642386582, 11.977379126966868)) as c:
            c.circle([0.0, 0.0], 1.0, id='tri0')
            for object_id, center, radius in [('tri1', [2.0, 0.0], 1.0), ('tri2', [4.0, 0.0], 1.0), ('tri3', [1.0, 1.7320508075688772], 1.0), ('tri4', [3.0, 1.7320508075688772], 1.0)]:
                c.circle(center, radius, id=object_id, edgecolor='#DC2626')
            for object_id, center, radius in [('tri5', [2.0, 3.4641016151377544], 1.0), ('hex0', [17.5, 1.7320508075688772], 1.0), ('hex1', [16.5, 3.4641016151377544], 1.0), ('hex2', [14.5, 3.4641016151377544], 1.0), ('hex3', [13.5, 1.7320508075688774], 1.0), ('hex4', [14.5, 4.440892098500626e-16], 1.0), ('hex5', [16.5, 0.0], 1.0)]:
                c.circle(center, radius, id=object_id)
            c.path([[6.5, 1.2320508075688772], [10.5, 1.2320508075688772], [10.5, 0.7320508075688772], [11.5, 1.7320508075688772], [10.5, 2.732050807568877], [10.5, 2.232050807568877], [6.5, 2.232050807568877], [6.5, 1.2320508075688772]], [1, 2, 2, 2, 2, 2, 2, 79], id='transformation_arrow', capstyle='butt')
            return c.save(output_path)

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Plane200')
    parser.add_argument('output', nargs='?')
    parser.add_argument('--variant', choices=('C01', 'C02', 'C03', 'C04', 'C05', 'C06'))
    args = parser.parse_args()
    print(Plane200().draw(args.output, variant=args.variant))
