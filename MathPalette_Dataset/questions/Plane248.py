"""Collected question Plane248; construction on the shared drawing protocol."""
from pathlib import Path
import sys
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from MathPalette_Dataset.drawing import Canvas, PLANE

class Plane248:
    variants = ('C01', 'C02', 'C03', 'C04', 'C05')

    def draw(self, output_path=None, *, variant=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / (self.__class__.__name__ + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if variant not in self.variants:
                raise ValueError('Unknown Special variant: ' + str(variant))
            return getattr(self, 'draw_' + variant)(output_path)
        with Canvas(PLANE, xlim=(-1.3532246852867402, 27.67854144687496), ylim=(-11.02219427296967, 18.00957185919203)) as c:
            for object_id, vertices, codes in [('source0', [[8, 6], [9, 7], [10, 6], [10, 5], [9, 5], [9, 6], [8, 6]], [1, 2, 2, 2, 2, 2, 79]), ('source1', [[11, 6], [12, 7], [13, 6], [13, 5], [12, 5], [12, 6], [11, 6]], [1, 2, 2, 2, 2, 2, 79]), ('option0', [[0, 2], [1, 2], [1, 1], [2, 2], [3, 1], [3, 0], [2, 0], [2, 1], [1, 0], [0, 1], [0, 2]], [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 79]), ('option1', [[6, 1], [7, 2], [8, 2], [9, 1], [8, 0], [7, 0], [6, 1]], [1, 2, 2, 2, 2, 2, 79]), ('option2', [[12, 1], [13, 2], [15, 2], [15, 3], [16, 2], [15, 1], [13, 1], [13, 0], [12, 1]], [1, 2, 2, 2, 2, 2, 2, 2, 79]), ('option3', [[18, 0], [19, 0], [21, 2], [21, 3], [20, 3], [20, 2], [19, 2], [19, 1], [18, 1], [18, 0]], [1, 2, 2, 2, 2, 2, 2, 2, 2, 79]), ('option4', [[24, 1], [25, 1], [26, 0], [26, 1], [27, 1], [27, 2], [26, 2], [25, 3], [25, 2], [24, 2], [24, 1]], [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 79])]:
                c.path(vertices, codes, id=object_id)
            for object_id, text, anchor in [('label0', 'A', (-0.4, 3.3)), ('label1', 'B', (5.6, 3.3)), ('label2', 'C', (11.6, 3.3)), ('label3', 'D', (17.6, 3.3)), ('label4', 'E', (23.6, 3.3))]:
                c.text(text, anchor, id=object_id)
            return c.save(output_path)

    def draw_C01(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane248_C01.png'
        with Canvas(PLANE, xlim=(-1.3532246852867402, 27.67854144687496), ylim=(-11.02219427296967, 18.00957185919203)) as c:
            for object_id, vertices, codes in [('source0', [[8.0, 6.0], [9.0, 7.0], [10.0, 6.0], [10.0, 5.0], [9.0, 5.0], [9.0, 6.0], [8.0, 6.0]], [1, 2, 2, 2, 2, 2, 79]), ('source1', [[11.0, 6.0], [12.0, 7.0], [13.0, 6.0], [13.0, 5.0], [12.0, 5.0], [12.0, 6.0], [11.0, 6.0]], [1, 2, 2, 2, 2, 2, 79]), ('option0', [[0.0, 2.0], [1.0, 2.0], [1.0, 1.0], [2.0, 2.0], [3.0, 1.0], [3.0, 0.0], [2.0, 0.0], [2.0, 1.0], [1.0, 0.0], [0.0, 1.0], [0.0, 2.0]], [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 79])]:
                c.path(vertices, codes, id=object_id, capstyle='butt')
            c.path([[6.0, 1.0], [7.0, 2.0], [8.0, 2.0], [9.0, 1.0], [8.0, 0.0], [7.0, 0.0], [6.0, 1.0]], [1, 2, 2, 2, 2, 2, 79], id='option1', edgecolor='#16A34A', capstyle='butt')
            for object_id, vertices, codes in [('option2', [[12.0, 1.0], [13.0, 2.0], [15.0, 2.0], [15.0, 3.0], [16.0, 2.0], [15.0, 1.0], [13.0, 1.0], [13.0, 0.0], [12.0, 1.0]], [1, 2, 2, 2, 2, 2, 2, 2, 79]), ('option3', [[18.0, 0.0], [19.0, 0.0], [21.0, 2.0], [21.0, 3.0], [20.0, 3.0], [20.0, 2.0], [19.0, 2.0], [19.0, 1.0], [18.0, 1.0], [18.0, 0.0]], [1, 2, 2, 2, 2, 2, 2, 2, 2, 79]), ('option4', [[24.0, 1.0], [25.0, 1.0], [26.0, 0.0], [26.0, 1.0], [27.0, 1.0], [27.0, 2.0], [26.0, 2.0], [25.0, 3.0], [25.0, 2.0], [24.0, 2.0], [24.0, 1.0]], [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 79])]:
                c.path(vertices, codes, id=object_id, capstyle='butt')
            for object_id, text, anchor in [('label0', 'A', (-0.4, 3.3)), ('label1', 'B', (5.6, 3.3)), ('label2', 'C', (11.6, 3.3)), ('label3', 'D', (17.6, 3.3)), ('label4', 'E', (23.6, 3.3))]:
                c.text(text, anchor, id=object_id)
            c.line([[6, 1], [9, 1]], zorder=9, color='#2563EB', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            c.line([[6, 1], [9, 1]], zorder=9, color='#DC2626', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            return c.save(output_path)

    def draw_C02(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane248_C02.png'
        with Canvas(PLANE, xlim=(-1.3532246852867402, 27.67854144687496), ylim=(-11.02219427296967, 18.00957185919203)) as c:
            for object_id, vertices, codes in [('source0', [[8.0, 6.0], [9.0, 7.0], [10.0, 6.0], [10.0, 5.0], [9.0, 5.0], [9.0, 6.0], [8.0, 6.0]], [1, 2, 2, 2, 2, 2, 79]), ('source1', [[11.0, 6.0], [12.0, 7.0], [13.0, 6.0], [13.0, 5.0], [12.0, 5.0], [12.0, 6.0], [11.0, 6.0]], [1, 2, 2, 2, 2, 2, 79]), ('option0', [[0.0, 2.0], [1.0, 2.0], [1.0, 1.0], [2.0, 2.0], [3.0, 1.0], [3.0, 0.0], [2.0, 0.0], [2.0, 1.0], [1.0, 0.0], [0.0, 1.0], [0.0, 2.0]], [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 79]), ('option1', [[6.0, 1.0], [7.0, 2.0], [8.0, 2.0], [9.0, 1.0], [8.0, 0.0], [7.0, 0.0], [6.0, 1.0]], [1, 2, 2, 2, 2, 2, 79])]:
                c.path(vertices, codes, id=object_id, capstyle='butt')
            c.path([[12.0, 1.0], [13.0, 2.0], [15.0, 2.0], [15.0, 3.0], [16.0, 2.0], [15.0, 1.0], [13.0, 1.0], [13.0, 0.0], [12.0, 1.0]], [1, 2, 2, 2, 2, 2, 2, 2, 79], id='option2', edgecolor='#16A34A', capstyle='butt')
            c.path([[18.0, 0.0], [19.0, 0.0], [21.0, 2.0], [21.0, 3.0], [20.0, 3.0], [20.0, 2.0], [19.0, 2.0], [19.0, 1.0], [18.0, 1.0], [18.0, 0.0]], [1, 2, 2, 2, 2, 2, 2, 2, 2, 79], id='option3', capstyle='butt')
            c.path([[24.0, 1.0], [25.0, 1.0], [26.0, 0.0], [26.0, 1.0], [27.0, 1.0], [27.0, 2.0], [26.0, 2.0], [25.0, 3.0], [25.0, 2.0], [24.0, 2.0], [24.0, 1.0]], [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 79], id='option4', capstyle='butt')
            for object_id, text, anchor in [('label0', 'A', (-0.4, 3.3)), ('label1', 'B', (5.6, 3.3)), ('label2', 'C', (11.6, 3.3)), ('label3', 'D', (17.6, 3.3)), ('label4', 'E', (23.6, 3.3))]:
                c.text(text, anchor, id=object_id)
            c.line([[13, 1], [15, 2]], zorder=9, color='#DC2626', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            return c.save(output_path)

    def draw_C03(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane248_C03.png'
        with Canvas(PLANE, xlim=(-1.3532246852867402, 27.67854144687496), ylim=(-11.02219427296967, 18.00957185919203)) as c:
            for object_id, vertices, codes in [('source0', [[8.0, 6.0], [9.0, 7.0], [10.0, 6.0], [10.0, 5.0], [9.0, 5.0], [9.0, 6.0], [8.0, 6.0]], [1, 2, 2, 2, 2, 2, 79]), ('source1', [[11.0, 6.0], [12.0, 7.0], [13.0, 6.0], [13.0, 5.0], [12.0, 5.0], [12.0, 6.0], [11.0, 6.0]], [1, 2, 2, 2, 2, 2, 79]), ('option0', [[0.0, 2.0], [1.0, 2.0], [1.0, 1.0], [2.0, 2.0], [3.0, 1.0], [3.0, 0.0], [2.0, 0.0], [2.0, 1.0], [1.0, 0.0], [0.0, 1.0], [0.0, 2.0]], [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 79]), ('option1', [[6.0, 1.0], [7.0, 2.0], [8.0, 2.0], [9.0, 1.0], [8.0, 0.0], [7.0, 0.0], [6.0, 1.0]], [1, 2, 2, 2, 2, 2, 79])]:
                c.path(vertices, codes, id=object_id, capstyle='butt')
            c.path([[12.0, 1.0], [13.0, 2.0], [15.0, 2.0], [15.0, 3.0], [16.0, 2.0], [15.0, 1.0], [13.0, 1.0], [13.0, 0.0], [12.0, 1.0]], [1, 2, 2, 2, 2, 2, 2, 2, 79], id='option2', edgecolor='#16A34A', capstyle='butt')
            c.path([[18.0, 0.0], [19.0, 0.0], [21.0, 2.0], [21.0, 3.0], [20.0, 3.0], [20.0, 2.0], [19.0, 2.0], [19.0, 1.0], [18.0, 1.0], [18.0, 0.0]], [1, 2, 2, 2, 2, 2, 2, 2, 2, 79], id='option3', capstyle='butt')
            c.path([[24.0, 1.0], [25.0, 1.0], [26.0, 0.0], [26.0, 1.0], [27.0, 1.0], [27.0, 2.0], [26.0, 2.0], [25.0, 3.0], [25.0, 2.0], [24.0, 2.0], [24.0, 1.0]], [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 79], id='option4', capstyle='butt')
            for object_id, text, anchor in [('label0', 'A', (-0.4, 3.3)), ('label1', 'B', (5.6, 3.3)), ('label2', 'C', (11.6, 3.3)), ('label3', 'D', (17.6, 3.3)), ('label4', 'E', (23.6, 3.3))]:
                c.text(text, anchor, id=object_id)
            c.line([[13, 1], [15, 2]], zorder=9, color='#DC2626', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            c.line([[13, 2], [15, 1]], zorder=9, color='#2563EB', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            return c.save(output_path)

    def draw_C04(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane248_C04.png'
        with Canvas(PLANE, xlim=(-1.3532246852867402, 27.67854144687496), ylim=(-11.02219427296967, 18.00957185919203)) as c:
            c.path([[8.0, 6.0], [9.0, 7.0], [10.0, 6.0], [10.0, 5.0], [9.0, 5.0], [9.0, 6.0], [8.0, 6.0]], [1, 2, 2, 2, 2, 2, 79], id='source0', capstyle='butt')
            c.path([[11.0, 6.0], [12.0, 7.0], [13.0, 6.0], [13.0, 5.0], [12.0, 5.0], [12.0, 6.0], [11.0, 6.0]], [1, 2, 2, 2, 2, 2, 79], id='source1', edgecolor='#16A34A', capstyle='butt')
            c.path([[0.0, 2.0], [1.0, 2.0], [1.0, 1.0], [2.0, 2.0], [3.0, 1.0], [3.0, 0.0], [2.0, 0.0], [2.0, 1.0], [1.0, 0.0], [0.0, 1.0], [0.0, 2.0]], [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 79], id='option0', capstyle='butt')
            c.path([[6.0, 1.0], [7.0, 2.0], [8.0, 2.0], [9.0, 1.0], [8.0, 0.0], [7.0, 0.0], [6.0, 1.0]], [1, 2, 2, 2, 2, 2, 79], id='option1', edgecolor='#16A34A', capstyle='butt')
            for object_id, vertices, codes in [('option2', [[12.0, 1.0], [13.0, 2.0], [15.0, 2.0], [15.0, 3.0], [16.0, 2.0], [15.0, 1.0], [13.0, 1.0], [13.0, 0.0], [12.0, 1.0]], [1, 2, 2, 2, 2, 2, 2, 2, 79]), ('option3', [[18.0, 0.0], [19.0, 0.0], [21.0, 2.0], [21.0, 3.0], [20.0, 3.0], [20.0, 2.0], [19.0, 2.0], [19.0, 1.0], [18.0, 1.0], [18.0, 0.0]], [1, 2, 2, 2, 2, 2, 2, 2, 2, 79]), ('option4', [[24.0, 1.0], [25.0, 1.0], [26.0, 0.0], [26.0, 1.0], [27.0, 1.0], [27.0, 2.0], [26.0, 2.0], [25.0, 3.0], [25.0, 2.0], [24.0, 2.0], [24.0, 1.0]], [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 79])]:
                c.path(vertices, codes, id=object_id, capstyle='butt')
            for object_id, text, anchor in [('label0', 'A', (-0.4, 3.3)), ('label1', 'B', (5.6, 3.3)), ('label2', 'C', (11.6, 3.3)), ('label3', 'D', (17.6, 3.3)), ('label4', 'E', (23.6, 3.3))]:
                c.text(text, anchor, id=object_id)
            c.line([[7, 2], [8, 0]], zorder=9, color='#DC2626', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            return c.save(output_path)

    def draw_C05(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane248_C05.png'
        with Canvas(PLANE, xlim=(-1.3532246852867402, 27.67854144687496), ylim=(-11.02219427296967, 18.00957185919203)) as c:
            c.path([[8.0, 6.0], [9.0, 7.0], [10.0, 6.0], [10.0, 5.0], [9.0, 5.0], [9.0, 6.0], [8.0, 6.0]], [1, 2, 2, 2, 2, 2, 79], id='source0', capstyle='butt')
            c.path([[11.0, 6.0], [12.0, 7.0], [13.0, 6.0], [13.0, 5.0], [12.0, 5.0], [12.0, 6.0], [11.0, 6.0]], [1, 2, 2, 2, 2, 2, 79], id='source1', edgecolor='#16A34A', capstyle='butt')
            c.path([[0.0, 2.0], [1.0, 2.0], [1.0, 1.0], [2.0, 2.0], [3.0, 1.0], [3.0, 0.0], [2.0, 0.0], [2.0, 1.0], [1.0, 0.0], [0.0, 1.0], [0.0, 2.0]], [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 79], id='option0', capstyle='butt')
            c.path([[6.0, 1.0], [7.0, 2.0], [8.0, 2.0], [9.0, 1.0], [8.0, 0.0], [7.0, 0.0], [6.0, 1.0]], [1, 2, 2, 2, 2, 2, 79], id='option1', edgecolor='#16A34A', capstyle='butt')
            for object_id, vertices, codes in [('option2', [[12.0, 1.0], [13.0, 2.0], [15.0, 2.0], [15.0, 3.0], [16.0, 2.0], [15.0, 1.0], [13.0, 1.0], [13.0, 0.0], [12.0, 1.0]], [1, 2, 2, 2, 2, 2, 2, 2, 79]), ('option3', [[18.0, 0.0], [19.0, 0.0], [21.0, 2.0], [21.0, 3.0], [20.0, 3.0], [20.0, 2.0], [19.0, 2.0], [19.0, 1.0], [18.0, 1.0], [18.0, 0.0]], [1, 2, 2, 2, 2, 2, 2, 2, 2, 79]), ('option4', [[24.0, 1.0], [25.0, 1.0], [26.0, 0.0], [26.0, 1.0], [27.0, 1.0], [27.0, 2.0], [26.0, 2.0], [25.0, 3.0], [25.0, 2.0], [24.0, 2.0], [24.0, 1.0]], [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 79])]:
                c.path(vertices, codes, id=object_id, capstyle='butt')
            for object_id, text, anchor in [('label0', 'A', (-0.4, 3.3)), ('label1', 'B', (5.6, 3.3)), ('label2', 'C', (11.6, 3.3)), ('label3', 'D', (17.6, 3.3)), ('label4', 'E', (23.6, 3.3))]:
                c.text(text, anchor, id=object_id)
            c.line([[7.0, 2.0], [7.5, 1.0]], zorder=9, color='#DC2626', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            return c.save(output_path)
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Plane248')
    parser.add_argument('output', nargs='?')
    parser.add_argument('--variant', choices=('C01', 'C02', 'C03', 'C04', 'C05'))
    args = parser.parse_args()
    print(Plane248().draw(args.output, variant=args.variant))
