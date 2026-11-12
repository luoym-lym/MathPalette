"""Collected question Plane507; construction on the shared drawing protocol."""
from pathlib import Path
import sys
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from MathPalette_Dataset.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane507:
    variants = ('C01', 'C02')

    def __init__(self):
        self.id = 'Plane507'
        self.source_dataset = 'Author Designed'
        self.source_key = 'author-promote15:Plane511'
        self.question = 'Six points are numbered as shown. Draw one triangle by connecting the three odd-numbered points, and a second triangle by connecting the three even-numbered points. Which choice shows the resulting two triangles? All choices preserve the source points’ relative positions and orientation.\nChoices:\nA: A\nB: B\nC: C\nD: D\nE: E'
        self.answer = 'C'
        self.answer_type = 'choice'
        self.choices = {'A': 'A', 'B': 'B', 'C': 'C', 'D': 'D', 'E': 'E'}
        self.query = self.question

    def draw(self, output_path=None, *, variant=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if variant not in self.variants:
                raise ValueError('Unknown Special variant: ' + str(variant))
            return getattr(self, 'draw_' + variant)(output_path)
        with Canvas(PLANE, xlim=[0.0, 8.0], ylim=[0.0, 8.0], axes_position=[0.05, 0.05, 0.9, 0.9], coordinate_axes=False) as c:
            for object_id, points in [('source_dot1', [[3.0455, 7.166]]), ('source_dot2', [[4.0575, 7.6145]]), ('source_dot5', [[5.058, 6.9245]]), ('source_dot4', [[4.966, 5.7515]]), ('source_dot3', [[3.9195, 5.257]]), ('source_dot6', [[2.896, 6.0735]])]:
                c.point(points, id=object_id, zorder=3, linewidths=[0])
            c.line([[0.6611, 4.2512], [1.3915, 4.5749], [2.1136, 4.0769], [0.6611, 4.2512]], id='option0_0', solid_capstyle='projecting')
            c.line([[2.0472, 3.2303], [1.2919, 2.8734], [0.5532, 3.4627], [2.0472, 3.2303]], id='option0_1', solid_capstyle='projecting')
            for object_id, points in [('option0_dot0', [[0.6611, 4.2512]]), ('option0_dot1', [[1.3915, 4.5749]]), ('option0_dot2', [[2.1136, 4.0769]]), ('option0_dot3', [[2.0472, 3.2303]]), ('option0_dot4', [[1.2919, 2.8734]]), ('option0_dot5', [[0.5532, 3.4627]])]:
                c.point(points, id=object_id, zorder=3, s=[12], linewidths=[0])
            c.line([[3.3111, 4.2512], [4.0415, 4.5749], [4.6972, 3.2303], [3.3111, 4.2512]], id='option1_0', solid_capstyle='projecting')
            c.line([[4.7636, 4.0769], [3.9419, 2.8734], [3.2032, 3.4627], [4.7636, 4.0769]], id='option1_1', solid_capstyle='projecting')
            for object_id, points in [('option1_dot0', [[3.3111, 4.2512]]), ('option1_dot1', [[4.0415, 4.5749]]), ('option1_dot2', [[4.7636, 4.0769]]), ('option1_dot3', [[4.6972, 3.2303]]), ('option1_dot4', [[3.9419, 2.8734]]), ('option1_dot5', [[3.2032, 3.4627]])]:
                c.point(points, id=object_id, zorder=3, s=[12], linewidths=[0])
            c.line([[5.9611, 4.2512], [7.4136, 4.0769], [6.5919, 2.8734], [5.9611, 4.2512]], id='option2_0', solid_capstyle='projecting')
            c.line([[6.6915, 4.5749], [7.3472, 3.2303], [5.8532, 3.4627], [6.6915, 4.5749]], id='option2_1', solid_capstyle='projecting')
            for object_id, points in [('option2_dot0', [[5.9611, 4.2512]]), ('option2_dot1', [[6.6915, 4.5749]]), ('option2_dot2', [[7.4136, 4.0769]]), ('option2_dot3', [[7.3472, 3.2303]]), ('option2_dot4', [[6.5919, 2.8734]]), ('option2_dot5', [[5.8532, 3.4627]])]:
                c.point(points, id=object_id, zorder=3, s=[12], linewidths=[0])
            c.line([[1.9611, 1.9712], [2.6915, 2.2949], [2.5919, 0.5934], [1.9611, 1.9712]], id='option3_0', solid_capstyle='projecting')
            c.line([[3.4136, 1.7969], [3.3472, 0.9503], [1.8532, 1.1827], [3.4136, 1.7969]], id='option3_1', solid_capstyle='projecting')
            for object_id, points in [('option3_dot0', [[1.9611, 1.9712]]), ('option3_dot1', [[2.6915, 2.2949]]), ('option3_dot2', [[3.4136, 1.7969]]), ('option3_dot3', [[3.3472, 0.9503]]), ('option3_dot4', [[2.5919, 0.5934]]), ('option3_dot5', [[1.8532, 1.1827]])]:
                c.point(points, id=object_id, zorder=3, s=[12], linewidths=[0])
            c.line([[4.6611, 1.9712], [5.3915, 2.2949], [4.5532, 1.1827], [4.6611, 1.9712]], id='option4_0', solid_capstyle='projecting')
            c.line([[6.1136, 1.7969], [6.0472, 0.9503], [5.2919, 0.5934], [6.1136, 1.7969]], id='option4_1', solid_capstyle='projecting')
            for object_id, points in [('option4_dot0', [[4.6611, 1.9712]]), ('option4_dot1', [[5.3915, 2.2949]]), ('option4_dot2', [[6.1136, 1.7969]]), ('option4_dot3', [[6.0472, 0.9503]]), ('option4_dot4', [[5.2919, 0.5934]]), ('option4_dot5', [[4.5532, 1.1827]])]:
                c.point(points, id=object_id, zorder=3, s=[12], linewidths=[0])
            for object_id, text, anchor in [(None, '1', [2.80001, 7.3553]), (None, '2', [4.07253, 7.92414]), (None, '5', [5.33884, 7.05576]), (None, '4', [5.21968, 5.57332]), (None, '3', [3.89828, 4.94773]), (None, '6', [2.601, 5.97824]), (None, '(A)', [1.35, 2.6]), (None, '(B)', [4, 2.6]), (None, '(C)', [6.65, 2.6]), (None, '(D)', [2.65, 0.31999999999999984]), (None, '(E)', [5.35, 0.31999999999999984])]:
                c.text(text, anchor, id=object_id, zorder=3, rotation_mode='default')
            return c.save(output_path)

    def draw_C01(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane507_C01.png'
        with Canvas(PLANE, xlim=(0.0, 8.0), ylim=(0.0, 8.0), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
            for object_id, points in [('source_dot1', [[3.0455, 7.166]]), ('source_dot2', [[4.0575, 7.6145]]), ('source_dot5', [[5.058, 6.9245]]), ('source_dot4', [[4.966, 5.7515]]), ('source_dot3', [[3.9195, 5.257]]), ('source_dot6', [[2.896, 6.0735]])]:
                c.point(points, id=object_id, zorder=3, linewidths=[0])
            c.line([[0.6611, 4.2512], [1.3915, 4.5749], [2.1136, 4.0769], [0.6611, 4.2512]], id='option0_0', solid_capstyle='projecting')
            c.line([[2.0472, 3.2303], [1.2919, 2.8734], [0.5532, 3.4627], [2.0472, 3.2303]], id='option0_1', solid_capstyle='projecting')
            for object_id, points in [('option0_dot0', [[0.6611, 4.2512]]), ('option0_dot1', [[1.3915, 4.5749]]), ('option0_dot2', [[2.1136, 4.0769]]), ('option0_dot3', [[2.0472, 3.2303]]), ('option0_dot4', [[1.2919, 2.8734]]), ('option0_dot5', [[0.5532, 3.4627]])]:
                c.point(points, id=object_id, zorder=3, s=[12], linewidths=[0])
            c.line([[3.3111, 4.2512], [4.0415, 4.5749], [4.6972, 3.2303], [3.3111, 4.2512]], id='option1_0', color='#DC2626', linewidth=1.5, solid_capstyle='projecting')
            c.line([[4.7636, 4.0769], [3.9419, 2.8734], [3.2032, 3.4627], [4.7636, 4.0769]], id='option1_1', color='#2563EB', linewidth=1.5, solid_capstyle='projecting')
            for object_id, points in [('option1_dot0', [[3.3111, 4.2512]]), ('option1_dot1', [[4.0415, 4.5749]]), ('option1_dot2', [[4.7636, 4.0769]]), ('option1_dot3', [[4.6972, 3.2303]]), ('option1_dot4', [[3.9419, 2.8734]]), ('option1_dot5', [[3.2032, 3.4627]])]:
                c.point(points, id=object_id, zorder=3, s=[12], linewidths=[0])
            c.line([[5.9611, 4.2512], [7.4136, 4.0769], [6.5919, 2.8734], [5.9611, 4.2512]], id='option2_0', solid_capstyle='projecting')
            c.line([[6.6915, 4.5749], [7.3472, 3.2303], [5.8532, 3.4627], [6.6915, 4.5749]], id='option2_1', solid_capstyle='projecting')
            for object_id, points in [('option2_dot0', [[5.9611, 4.2512]]), ('option2_dot1', [[6.6915, 4.5749]]), ('option2_dot2', [[7.4136, 4.0769]]), ('option2_dot3', [[7.3472, 3.2303]]), ('option2_dot4', [[6.5919, 2.8734]]), ('option2_dot5', [[5.8532, 3.4627]])]:
                c.point(points, id=object_id, zorder=3, s=[12], linewidths=[0])
            c.line([[1.9611, 1.9712], [2.6915, 2.2949], [2.5919, 0.5934], [1.9611, 1.9712]], id='option3_0', solid_capstyle='projecting')
            c.line([[3.4136, 1.7969], [3.3472, 0.9503], [1.8532, 1.1827], [3.4136, 1.7969]], id='option3_1', solid_capstyle='projecting')
            for object_id, points in [('option3_dot0', [[1.9611, 1.9712]]), ('option3_dot1', [[2.6915, 2.2949]]), ('option3_dot2', [[3.4136, 1.7969]]), ('option3_dot3', [[3.3472, 0.9503]]), ('option3_dot4', [[2.5919, 0.5934]]), ('option3_dot5', [[1.8532, 1.1827]])]:
                c.point(points, id=object_id, zorder=3, s=[12], linewidths=[0])
            c.line([[4.6611, 1.9712], [5.3915, 2.2949], [4.5532, 1.1827], [4.6611, 1.9712]], id='option4_0', solid_capstyle='projecting')
            c.line([[6.1136, 1.7969], [6.0472, 0.9503], [5.2919, 0.5934], [6.1136, 1.7969]], id='option4_1', solid_capstyle='projecting')
            for object_id, points in [('option4_dot0', [[4.6611, 1.9712]]), ('option4_dot1', [[5.3915, 2.2949]]), ('option4_dot2', [[6.1136, 1.7969]]), ('option4_dot3', [[6.0472, 0.9503]]), ('option4_dot4', [[5.2919, 0.5934]]), ('option4_dot5', [[4.5532, 1.1827]])]:
                c.point(points, id=object_id, zorder=3, s=[12], linewidths=[0])
            for object_id, text, anchor in [(None, '1', (2.80001, 7.3553)), (None, '2', (4.07253, 7.92414)), (None, '5', (5.33884, 7.05576)), (None, '4', (5.21968, 5.57332)), (None, '3', (3.89828, 4.94773)), (None, '6', (2.601, 5.97824)), (None, '(A)', (1.35, 2.6)), (None, '(B)', (4, 2.6)), (None, '(C)', (6.65, 2.6)), (None, '(D)', (2.65, 0.31999999999999984)), (None, '(E)', (5.35, 0.31999999999999984))]:
                c.text(text, anchor, id=object_id, zorder=3, rotation_mode='default')
            for object_id, points in [(None, [[3.0455, 7.166], [4.0575, 7.6145]]), (None, [[3.0455, 7.166], [4.966, 5.7515]]), (None, [[4.0575, 7.6145], [4.966, 5.7515]])]:
                c.line(points, id=object_id, zorder=9, color='#DC2626', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            for object_id, points in [(None, [[5.058, 6.9245], [3.9195, 5.257]]), (None, [[5.058, 6.9245], [2.896, 6.0735]]), (None, [[3.9195, 5.257], [2.896, 6.0735]])]:
                c.line(points, id=object_id, zorder=9, color='#2563EB', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            return c.save(output_path)

    def draw_C02(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane507_C02.png'
        with Canvas(PLANE, xlim=(0.0, 8.0), ylim=(0.0, 8.0), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
            for object_id, points in [('source_dot1', [[3.0455, 7.166]]), ('source_dot2', [[4.0575, 7.6145]]), ('source_dot5', [[5.058, 6.9245]]), ('source_dot4', [[4.966, 5.7515]]), ('source_dot3', [[3.9195, 5.257]]), ('source_dot6', [[2.896, 6.0735]])]:
                c.point(points, id=object_id, zorder=3, linewidths=[0])
            c.line([[0.6611, 4.2512], [1.3915, 4.5749], [2.1136, 4.0769], [0.6611, 4.2512]], id='option0_0', solid_capstyle='projecting')
            c.line([[2.0472, 3.2303], [1.2919, 2.8734], [0.5532, 3.4627], [2.0472, 3.2303]], id='option0_1', solid_capstyle='projecting')
            for object_id, points in [('option0_dot0', [[0.6611, 4.2512]]), ('option0_dot1', [[1.3915, 4.5749]]), ('option0_dot2', [[2.1136, 4.0769]]), ('option0_dot3', [[2.0472, 3.2303]]), ('option0_dot4', [[1.2919, 2.8734]]), ('option0_dot5', [[0.5532, 3.4627]])]:
                c.point(points, id=object_id, zorder=3, s=[12], linewidths=[0])
            c.line([[3.3111, 4.2512], [4.0415, 4.5749], [4.6972, 3.2303], [3.3111, 4.2512]], id='option1_0', solid_capstyle='projecting')
            c.line([[4.7636, 4.0769], [3.9419, 2.8734], [3.2032, 3.4627], [4.7636, 4.0769]], id='option1_1', solid_capstyle='projecting')
            for object_id, points in [('option1_dot0', [[3.3111, 4.2512]]), ('option1_dot1', [[4.0415, 4.5749]]), ('option1_dot2', [[4.7636, 4.0769]]), ('option1_dot3', [[4.6972, 3.2303]]), ('option1_dot4', [[3.9419, 2.8734]]), ('option1_dot5', [[3.2032, 3.4627]])]:
                c.point(points, id=object_id, zorder=3, s=[12], linewidths=[0])
            c.line([[5.9611, 4.2512], [7.4136, 4.0769], [6.5919, 2.8734], [5.9611, 4.2512]], id='option2_0', linewidth=0.5, linestyle=(0.0, [3.7, 1.6]), solid_capstyle='projecting')
            c.line([[6.6915, 4.5749], [7.3472, 3.2303], [5.8532, 3.4627], [6.6915, 4.5749]], id='option2_1', linewidth=0.5, linestyle=(0.0, [3.7, 1.6]), solid_capstyle='projecting')
            for object_id, points in [('option2_dot0', [[5.9611, 4.2512]]), ('option2_dot1', [[6.6915, 4.5749]]), ('option2_dot2', [[7.4136, 4.0769]]), ('option2_dot3', [[7.3472, 3.2303]]), ('option2_dot4', [[6.5919, 2.8734]]), ('option2_dot5', [[5.8532, 3.4627]])]:
                c.point(points, id=object_id, zorder=3, s=[12], linewidths=[0])
            c.line([[1.9611, 1.9712], [2.6915, 2.2949], [2.5919, 0.5934], [1.9611, 1.9712]], id='option3_0', color='#DC2626', linewidth=1.5, solid_capstyle='projecting')
            c.line([[3.4136, 1.7969], [3.3472, 0.9503], [1.8532, 1.1827], [3.4136, 1.7969]], id='option3_1', color='#2563EB', linewidth=1.5, solid_capstyle='projecting')
            for object_id, points in [('option3_dot0', [[1.9611, 1.9712]]), ('option3_dot1', [[2.6915, 2.2949]]), ('option3_dot2', [[3.4136, 1.7969]]), ('option3_dot3', [[3.3472, 0.9503]]), ('option3_dot4', [[2.5919, 0.5934]]), ('option3_dot5', [[1.8532, 1.1827]])]:
                c.point(points, id=object_id, zorder=3, s=[12], linewidths=[0])
            c.line([[4.6611, 1.9712], [5.3915, 2.2949], [4.5532, 1.1827], [4.6611, 1.9712]], id='option4_0', solid_capstyle='projecting')
            c.line([[6.1136, 1.7969], [6.0472, 0.9503], [5.2919, 0.5934], [6.1136, 1.7969]], id='option4_1', solid_capstyle='projecting')
            for object_id, points in [('option4_dot0', [[4.6611, 1.9712]]), ('option4_dot1', [[5.3915, 2.2949]]), ('option4_dot2', [[6.1136, 1.7969]]), ('option4_dot3', [[6.0472, 0.9503]]), ('option4_dot4', [[5.2919, 0.5934]]), ('option4_dot5', [[4.5532, 1.1827]])]:
                c.point(points, id=object_id, zorder=3, s=[12], linewidths=[0])
            for object_id, text, anchor in [(None, '1', (2.80001, 7.3553)), (None, '2', (4.07253, 7.92414)), (None, '5', (5.33884, 7.05576)), (None, '4', (5.21968, 5.57332)), (None, '3', (3.89828, 4.94773)), (None, '6', (2.601, 5.97824)), (None, '(A)', (1.35, 2.6)), (None, '(B)', (4, 2.6)), (None, '(C)', (6.65, 2.6)), (None, '(D)', (2.65, 0.31999999999999984)), (None, '(E)', (5.35, 0.31999999999999984))]:
                c.text(text, anchor, id=object_id, zorder=3, rotation_mode='default')
            for object_id, points in [(None, [[3.0455, 7.166], [4.0575, 7.6145]]), (None, [[3.0455, 7.166], [3.9195, 5.257]]), (None, [[4.0575, 7.6145], [3.9195, 5.257]])]:
                c.line(points, id=object_id, zorder=9, color='#DC2626', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            for object_id, points in [(None, [[5.058, 6.9245], [4.966, 5.7515]]), (None, [[5.058, 6.9245], [2.896, 6.0735]]), (None, [[4.966, 5.7515], [2.896, 6.0735]])]:
                c.line(points, id=object_id, zorder=9, color='#2563EB', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            return c.save(output_path)
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Plane507')
    parser.add_argument('output', nargs='?')
    parser.add_argument('--variant', choices=('C01', 'C02'))
    args = parser.parse_args()
    print(Plane507().draw(args.output, variant=args.variant))
