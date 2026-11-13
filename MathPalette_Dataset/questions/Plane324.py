"""Collected question Plane324; construction on the shared drawing protocol."""
from pathlib import Path
import sys
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from MathPalette_Dataset.drawing import Canvas, PLANE

class Plane324:
    variants = ('C01',)

    def draw(self, output_path=None, *, variant=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / (self.__class__.__name__ + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if variant not in self.variants:
                raise ValueError('Unknown Special variant: ' + str(variant))
            return getattr(self, 'draw_' + variant)(output_path)
        with Canvas(PLANE, xlim=(-0.16814956219310906, 3.172145258471985), ylim=(-0.3707154221712696, 2.9695793984938246)) as c:
            for object_id, center, radius in [('dot0', [0.0, 0.0], 0.09), ('dot1', [1.0, 0.0], 0.09), ('dot2', [2.0, 0.0], 0.09), ('dot3', [3.0, 0.0], 0.09), ('dot4', [0.5, 0.8660254037844386], 0.09), ('dot5', [1.5, 0.8660254037844386], 0.09), ('dot6', [2.5, 0.8660254037844386], 0.09), ('dot7', [1.0, 1.7320508075688772], 0.09), ('dot8', [2.0, 1.7320508075688772], 0.09), ('dot9', [1.5, 2.598076211353316], 0.09)]:
                c.circle(center, radius, id=object_id, facecolor='black')
            return c.save(output_path)

    def draw_C01(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane324_C01.png'
        with Canvas(PLANE, xlim=(-0.16814956219310906, 3.172145258471985), ylim=(-0.3707154221712696, 2.9695793984938246)) as c:
            for object_id, center, radius in [('dot0', [0.0, 0.0], 0.09), ('dot1', [1.0, 0.0], 0.09), ('dot2', [2.0, 0.0], 0.09), ('dot3', [3.0, 0.0], 0.09), ('dot4', [0.5, 0.8660254037844386], 0.09), ('dot5', [1.5, 0.8660254037844386], 0.09), ('dot6', [2.5, 0.8660254037844386], 0.09), ('dot7', [1.0, 1.7320508075688772], 0.09), ('dot8', [2.0, 1.7320508075688772], 0.09), ('dot9', [1.5, 2.598076211353316], 0.09)]:
                c.circle(center, radius, id=object_id, facecolor='black')
            for object_id, points in [(None, [[1.5019978481394378, 2.6059402768813866], [0.9834880312061307, 1.7258380876130102]]), (None, [[0.9971330263885863, 1.7326605852042378], [2.0136851674815173, 1.7258380876130102]]), (None, [[1.4917641017525962, 2.6059402768813866], [2.0102739186859035, 1.7258380876130102]])]:
                c.line(points, id=object_id, zorder=9, color='#2563EB', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            for object_id, points in [(None, [[0.4990907022289624, 0.8764371375051585], [-0.01941911470434471, 0.009979943419236914]]), (None, [[-0.0057741195218892205, -0.00025380296760468823], [1.0141892703666555, 0.006568694623623639]]), (None, [[0.49226820463773474, 0.8696146399139306], [1.0141892703666555, -0.010487549354445402]])]:
                c.line(points, id=object_id, zorder=9, color='#DC2626', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            for object_id, points in [(None, [[2.494671247663072, 0.8798483863007722], [1.9932176747078338, 0.02021368980607896]]), (None, [[2.0034514210946757, 0.0031574458280094753], [2.999536069413924, 0.0031574458280094753]]), (None, [[2.498082496458686, 0.8832596350963859], [3.0268260597788346, 0.013391192214851078]])]:
                c.line(points, id=object_id, zorder=9, color='#16A34A', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            return c.save(output_path)

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Plane324')
    parser.add_argument('output', nargs='?')
    parser.add_argument('--variant', choices=('C01',))
    args = parser.parse_args()
    print(Plane324().draw(args.output, variant=args.variant))
