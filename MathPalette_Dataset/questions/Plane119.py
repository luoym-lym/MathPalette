"""Collected question Plane119; construction on the shared drawing protocol."""
from pathlib import Path
import sys
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from MathPalette_Dataset.drawing import Canvas, PLANE

class Plane119:
    variants = ('C01',)

    def __init__(self):
        self.points = {
            'V1': [1.86, 6.58], 'V2': [5.81, 7.13], 'V3': [7.12, 3.84], 'V4': [6.03, 1.1], 'V5': [2.74, 0.56],
            'V6': [0.55, 1.65]
        }

    def draw(self, output_path=None, *, variant=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / (self.__class__.__name__ + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if variant not in self.variants:
                raise ValueError('Unknown Special variant: ' + str(variant))
            return getattr(self, 'draw_' + variant)(output_path)
        with Canvas(PLANE, xlim=(0.395, 7.275), ylim=(0.405, 7.285)) as c:
            for object_id, points in [('edge_01', [self.points['V1'], self.points['V2']]), ('edge_02', [self.points['V2'], self.points['V3']]), ('edge_03', [self.points['V3'], self.points['V4']]), ('edge_04', [self.points['V4'], self.points['V5']]), ('edge_05', [self.points['V5'], self.points['V6']]), ('edge_06', [self.points['V6'], self.points['V1']])]:
                c.line(points, id=object_id)
            return c.save(output_path)

    def draw_C01(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane119_C01.png'
        with Canvas(PLANE, xlim=(0.395, 7.275), ylim=(0.405, 7.285)) as c:
            for object_id, points in [('edge_01', [[1.86, 6.58], [5.81, 7.13]]), ('edge_02', [[5.81, 7.13], [7.12, 3.84]]), ('edge_03', [[7.12, 3.84], [6.03, 1.1]]), ('edge_04', [[6.03, 1.1], [2.74, 0.56]]), ('edge_05', [[2.74, 0.56], [0.55, 1.65]]), ('edge_06', [[0.55, 1.65], [1.86, 6.58]])]:
                c.line(points, id=object_id)
            for object_id, points in [(None, [[1.86, 6.58]]), (None, [[0.55, 1.65]]), (None, [[2.74, 0.56]]), (None, [[6.03, 1.1]]), (None, [[7.12, 3.84]]), (None, [[5.81, 7.13]]), (None, [[3.870130718954248, 6.859215686274511]]), (None, [[1.172091503267974, 4.048758169934642]]), (None, [[1.5093464052287582, 1.189117647058823]]), (None, [[4.48140522875817, 0.8518627450980389]]), (None, [[6.6243790849673205, 2.55921568627451]]), (None, [[6.4768300653594775, 5.425882352941177]])]:
                c.point(points, id=object_id, zorder=10, s=50, facecolors='#DC2626', edgecolors='#DC2626')
            return c.save(output_path)

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Plane119')
    parser.add_argument('output', nargs='?')
    parser.add_argument('--variant', choices=('C01',))
    args = parser.parse_args()
    print(Plane119().draw(args.output, variant=args.variant))
