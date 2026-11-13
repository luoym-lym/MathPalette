"""Collected question Plane112; construction on the shared drawing protocol."""
from pathlib import Path
import sys
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from MathPalette_Dataset.drawing import Canvas, PLANE

class Plane112:
    variants = ('C01', 'C02', 'C03', 'C04', 'C05', 'C06', 'C07', 'C08')

    def __init__(self):
        self.points = {
            'left_circle_center': [-0.9, 0.25], 'right_circle_center': [1.0, 0.05], 'line_a': [-3.0, -1.08],
            'line_b': [3.0, -0.12], 'crossing_1': [-1.9926368849521967, -0.9188219015923516],
            'crossing_2': [-0.3255463966993375, -0.6520874234718941],
            'crossing_3': [0.0030760337958954387, -1.0707776789389936],
            'crossing_4': [0.25829382921780325, 1.3537913775691304],
            'crossing_5': [0.5027772905684218, -0.5195556335090525],
            'crossing_6': [2.4784325121439554, -0.20345079805696709]
        }

    def draw(self, output_path=None, *, variant=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / (self.__class__.__name__ + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if variant not in self.variants:
                raise ValueError('Unknown Special variant: ' + str(variant))
            return getattr(self, 'draw_' + variant)(output_path)
        with Canvas(PLANE, xlim=(-3.1395348837209305, 3.1395348837209305), ylim=(-2.9395348837209303, 3.3395348837209307)) as c:
            c.circle(self.points['left_circle_center'], 1.6, id='left_circle')
            c.circle(self.points['right_circle_center'], 1.5, id='right_circle')
            c.line([self.points['line_a'], self.points['line_b']], id='line')
            return c.save(output_path)

    def draw_C01(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane112_C01.png'
        with Canvas(PLANE, xlim=(-3.1395348837209305, 3.1395348837209305), ylim=(-2.9395348837209303, 3.3395348837209307)) as c:
            c.circle([-0.9, 0.25], 1.6, id='left_circle', fill=False)
            c.circle([1.0, 0.05], 1.5, id='right_circle', fill=False)
            c.line([[-3.0, -1.08], [3.0, -0.12]], id='line')
            for object_id, points in [(None, [[-0.3255463966993375, -0.6520874234718941]]), (None, [[0.0030760337958954387, -1.0707776789389936]]), (None, [[0.25829382921780325, 1.3537913775691304]]), (None, [[0.5027772905684218, -0.5195556335090525]]), (None, [[2.4784325121439554, -0.20345079805696709]])]:
                c.point(points, id=object_id, zorder=10, s=50, facecolors='#DC2626', edgecolors='#DC2626')
            return c.save(output_path)

    def draw_C02(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane112_C02.png'
        with Canvas(PLANE, xlim=(-3.1395348837209305, 3.1395348837209305), ylim=(-2.9395348837209303, 3.3395348837209307)) as c:
            c.circle([-0.9, 0.25], 1.6, id='left_circle', fill=False)
            c.circle([1.0, 0.05], 1.5, id='right_circle', fill=False)
            c.line([[-3.0, -1.08], [3.0, -0.12]], id='line')
            for object_id, points in [(None, [[-1.9926368849521967, -0.9188219015923516]]), (None, [[-0.3255463966993375, -0.6520874234718941]]), (None, [[0.25829382921780325, 1.3537913775691304]]), (None, [[0.5027772905684218, -0.5195556335090525]]), (None, [[2.4784325121439554, -0.20345079805696709]])]:
                c.point(points, id=object_id, zorder=10, s=50, facecolors='#2563EB', edgecolors='#2563EB')
            return c.save(output_path)

    def draw_C03(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane112_C03.png'
        with Canvas(PLANE, xlim=(-3.1395348837209305, 3.1395348837209305), ylim=(-2.9395348837209303, 3.3395348837209307)) as c:
            c.circle([-0.9, 0.25], 1.6, id='left_circle', fill=False)
            c.circle([1.0, 0.05], 1.5, id='right_circle', fill=False)
            c.line([[-3.0, -1.08], [3.0, -0.12]], id='line')
            for object_id, points in [(None, [[-1.9926368849521967, -0.9188219015923516]]), (None, [[-0.3255463966993375, -0.6520874234718941]]), (None, [[0.0030760337958954387, -1.0707776789389936]]), (None, [[0.5027772905684218, -0.5195556335090525]]), (None, [[2.4784325121439554, -0.20345079805696709]])]:
                c.point(points, id=object_id, zorder=10, s=50, facecolors='#16A34A', edgecolors='#16A34A')
            return c.save(output_path)

    def draw_C04(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane112_C04.png'
        with Canvas(PLANE, xlim=(-3.1395348837209305, 3.1395348837209305), ylim=(-2.9395348837209303, 3.3395348837209307)) as c:
            c.circle([-0.9, 0.25], 1.6, id='left_circle', fill=False)
            c.circle([1.0, 0.05], 1.5, id='right_circle', fill=False)
            c.line([[-3.0, -1.08], [3.0, -0.12]], id='line')
            for object_id, points in [(None, [[-1.9926368849521967, -0.9188219015923516]]), (None, [[-0.3255463966993375, -0.6520874234718941]]), (None, [[0.0030760337958954387, -1.0707776789389936]]), (None, [[0.25829382921780325, 1.3537913775691304]]), (None, [[2.4784325121439554, -0.20345079805696709]])]:
                c.point(points, id=object_id, zorder=10, s=50, facecolors='#DC2626', edgecolors='#DC2626')
            return c.save(output_path)

    def draw_C05(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane112_C05.png'
        with Canvas(PLANE, xlim=(-3.1395348837209305, 3.1395348837209305), ylim=(-2.9395348837209303, 3.3395348837209307)) as c:
            c.circle([-0.9, 0.25], 1.6, id='left_circle', fill=False)
            c.circle([1.0, 0.05], 1.5, id='right_circle', fill=False)
            c.line([[-3.0, -1.08], [3.0, -0.12]], id='line')
            for object_id, points in [(None, [[-0.3255463966993375, -0.6520874234718941]]), (None, [[0.25829382921780325, 1.3537913775691304]]), (None, [[0.5027772905684218, -0.5195556335090525]]), (None, [[2.4784325121439554, -0.20345079805696709]])]:
                c.point(points, id=object_id, zorder=10, s=50, facecolors='#DC2626', edgecolors='#DC2626')
            return c.save(output_path)

    def draw_C06(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane112_C06.png'
        with Canvas(PLANE, xlim=(-3.1395348837209305, 3.1395348837209305), ylim=(-2.9395348837209303, 3.3395348837209307)) as c:
            c.circle([-0.9, 0.25], 1.6, id='left_circle', fill=False)
            c.circle([1.0, 0.05], 1.5, id='right_circle', fill=False)
            c.line([[-3.0, -1.08], [3.0, -0.12]], id='line')
            for object_id, points in [(None, [[-0.3255463966993375, -0.6520874234718941]]), (None, [[0.0030760337958954387, -1.0707776789389936]]), (None, [[0.5027772905684218, -0.5195556335090525]]), (None, [[2.4784325121439554, -0.20345079805696709]])]:
                c.point(points, id=object_id, zorder=10, s=50, facecolors='#DC2626', edgecolors='#DC2626')
            return c.save(output_path)

    def draw_C07(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane112_C07.png'
        with Canvas(PLANE, xlim=(-3.1395348837209305, 3.1395348837209305), ylim=(-2.9395348837209303, 3.3395348837209307)) as c:
            c.circle([-0.9, 0.25], 1.6, id='left_circle', fill=False)
            c.circle([1.0, 0.05], 1.5, id='right_circle', fill=False)
            c.line([[-3.0, -1.08], [3.0, -0.12]], id='line')
            for object_id, points in [(None, [[-1.9926368849521967, -0.9188219015923516]]), (None, [[-0.3255463966993375, -0.6520874234718941]]), (None, [[0.0030760337958954387, -1.0707776789389936]]), (None, [[0.25829382921780325, 1.3537913775691304]]), (None, [[0.5027772905684218, -0.5195556335090525]]), (None, [[2.4784325121439554, -0.20345079805696709]]), (None, [[0.7000000000000001, 0.25]])]:
                c.point(points, id=object_id, zorder=10, s=50, facecolors='#DC2626', edgecolors='#DC2626')
            return c.save(output_path)

    def draw_C08(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane112_C08.png'
        with Canvas(PLANE, xlim=(-3.1395348837209305, 3.1395348837209305), ylim=(-2.9395348837209303, 3.3395348837209307)) as c:
            c.circle([-0.9, 0.25], 1.6, id='left_circle', fill=False)
            c.circle([1.0, 0.05], 1.5, id='right_circle', fill=False)
            c.line([[-3.0, -1.08], [3.0, -0.12]], id='line')
            for object_id, points in [(None, [[-1.9926368849521967, -0.9188219015923516]]), (None, [[-0.3255463966993375, -0.6520874234718941]]), (None, [[0.0030760337958954387, -1.0707776789389936]]), (None, [[0.25829382921780325, 1.3537913775691304]]), (None, [[0.5027772905684218, -0.5195556335090525]]), (None, [[2.4784325121439554, -0.20345079805696709]]), (None, [[-0.8999999999999999, 1.85]])]:
                c.point(points, id=object_id, zorder=10, s=50, facecolors='#EA580C', edgecolors='#EA580C')
            return c.save(output_path)

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Plane112')
    parser.add_argument('output', nargs='?')
    parser.add_argument('--variant', choices=('C01', 'C02', 'C03', 'C04', 'C05', 'C06', 'C07', 'C08'))
    args = parser.parse_args()
    print(Plane112().draw(args.output, variant=args.variant))
