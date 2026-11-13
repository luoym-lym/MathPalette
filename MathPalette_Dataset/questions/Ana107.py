"""Collected question Ana107; construction on the shared drawing protocol."""
from pathlib import Path
import sys
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from MathPalette_Dataset.drawing import Canvas, ANALYTICS

class Ana107:
    variants = ('C01', 'C02')

    def _samples_001(self):
        x1 = np.linspace(-1.5 * np.pi + 0.001, -0.5 * np.pi - 0.001, 1801)
        return np.column_stack((x1, np.tan(x1)))

    def _samples_002(self):
        x2 = np.linspace(-0.5 * np.pi + 0.001, 0.5 * np.pi - 0.001, 1801)
        return np.column_stack((x2, np.tan(x2)))

    def _samples_003(self):
        x3 = np.linspace(0.5 * np.pi + 0.001, 1.5 * np.pi - 0.001, 1801)
        return np.column_stack((x3, np.tan(x3)))

    def draw(self, output_path=None, *, variant=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / (self.__class__.__name__ + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if variant not in self.variants:
                raise ValueError('Unknown Special variant: ' + str(variant))
            return getattr(self, 'draw_' + variant)(output_path)
        with Canvas(ANALYTICS, xlabel='$\\theta$') as c:
            for object_id, points in [('object_000', self._samples_001()), ('object_001', self._samples_002()), ('object_002', self._samples_003())]:
                c.line(points, id=object_id, solid_capstyle='butt')
            return c.save(output_path)

    def draw_C01(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Ana107_C01.png'
        with Canvas(ANALYTICS, xlabel='$\\theta$') as c:
            for object_id, points in [('curve_001', self._samples_001()), ('curve_002', self._samples_002()), ('curve_003', self._samples_003())]:
                c.line(points, id=object_id, solid_capstyle='butt', simplify=True)
            for object_id, points in [(None, [[-3.0, 0.0]]), (None, [[0.0, 0.0]]), (None, [[3.0, 0.0]]), (None, [[4.0, 0.0]])]:
                c.point(points, id=object_id, zorder=10, s=50, facecolors='#DC2626', edgecolors='#DC2626')
            return c.save(output_path)

    def draw_C02(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Ana107_C02.png'
        with Canvas(ANALYTICS, xlabel='$\\theta$') as c:
            for object_id, points in [('curve_001', self._samples_001()), ('curve_002', self._samples_002()), ('curve_003', self._samples_003())]:
                c.line(points, id=object_id, solid_capstyle='butt', simplify=True)
            for object_id, points in [(None, [[-3.0, 0.0]]), (None, [[0.0, 0.0]]), (None, [[3.0, 0.0]]), (None, [[-5.0, 0.0]])]:
                c.point(points, id=object_id, zorder=10, s=50, facecolors='#DC2626', edgecolors='#DC2626')
            return c.save(output_path)

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Ana107')
    parser.add_argument('output', nargs='?')
    parser.add_argument('--variant', choices=('C01', 'C02'))
    args = parser.parse_args()
    print(Ana107().draw(args.output, variant=args.variant))
