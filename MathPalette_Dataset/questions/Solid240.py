"""Collected question Solid240; construction on the shared drawing protocol."""
from pathlib import Path
import sys
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from MathPalette_Dataset.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Solid240:
    variants = ('C01', 'C02')

    def __init__(self):
        self.id = 'Solid240'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:2790'
        self.question = 'A regular octahedron has eight equilateral triangle faces with four faces meeting at each vertex. The regular octahedron shown on the right is formed by folding the piece of paper shown on the left. Which numbered face will end up to the right of $Q$?'
        self.answer = '1'
        self.answer_type = 'number'
        self.query = self.question
        self.points = {'net(0, 0.8660254037844386)': [0, 0.8660254037844386, 0],
         'net(1, 0.8660254037844386)': [1, 0.8660254037844386, 0],
         'net(0.5, 0)': [0.5, 0, 0],
         'label1': [0.5, 0.5773502691896257, 0],
         'net(1.5, 0)': [1.5, 0, 0],
         'label3': [1.0, 0.28867513459481287, 0],
         'net(2, 0.8660254037844386)': [2, 0.8660254037844386, 0],
         'label4': [1.5, 0.5773502691896257, 0],
         'net(2.5, 0)': [2.5, 0, 0],
         'label5': [2.0, 0.28867513459481287, 0],
         'net(3, 0.8660254037844386)': [3, 0.8660254037844386, 0],
         'label6': [2.5, 0.5773502691896257, 0],
         'net(3.5, 0)': [3.5, 0, 0],
         'labelQ': [3.0, 0.28867513459481287, 0],
         'net(1, -0.8660254037844386)': [1, -0.8660254037844386, 0],
         'label2': [1.0, -0.28867513459481287, 0],
         'net(2.5, 1.7320508075688772)': [2.5, 1.7320508075688772, 0],
         'label7': [2.5, 1.1547005383792515, 0],
         'T': [6.1, 1.417333478872227, 0.25350727928987515],
         'Z': [6.1, -0.5173334788722268, -0.25350727928987515],
         'L': [5.111063647131703, 0.4123946153690259, 0.14349468639049534],
         'R': [7.088936352868297, 0.48760538463097414, -0.14349468639049534],
         'F': [6.248340452930244, 0.199297435793506, 0.9566312426033023],
         'H': [5.951659547069755, 0.700702564206494, -0.9566312426033023],
         'q': [5.7209077314004855, 0.843476886149249, -0.186543092307644],
         'unknown': [6.380198633312684, 0.8685471425698983, -0.2822062165679742],
         'arrowA': [3.75, 0.55, 0],
         'arrowB': [4.8, 0.55, 0],
         'tipup': [4.67, 0.61, 0],
         'tipdown': [4.67, 0.49, 0]}

    def draw(self, output_path=None, *, variant=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if variant not in self.variants:
                raise ValueError('Unknown Special variant: ' + str(variant))
            return getattr(self, 'draw_' + variant)(output_path)
        with Canvas(SOLID, xlim=[-0.17661733968185622, 7.265553692550153], ylim=[-3.2880728142237854, 4.154098218008224], projection=[[1, 0, 0], [0, 1, 0]], origin=[0, 0, 0], offset=[0, 0]) as c:
            for object_id, points in [('line_0', c.project([self.points['net(0, 0.8660254037844386)'], self.points['net(0.5, 0)']])), ('line_1', c.project([self.points['net(0, 0.8660254037844386)'], self.points['net(1, 0.8660254037844386)']])), ('line_2', c.project([self.points['net(0.5, 0)'], self.points['net(1, -0.8660254037844386)']])), ('line_3', c.project([self.points['net(0.5, 0)'], self.points['net(1, 0.8660254037844386)']])), ('line_4', c.project([self.points['net(0.5, 0)'], self.points['net(1.5, 0)']])), ('line_5', c.project([self.points['net(1, -0.8660254037844386)'], self.points['net(1.5, 0)']])), ('line_6', c.project([self.points['net(1, 0.8660254037844386)'], self.points['net(1.5, 0)']])), ('line_7', c.project([self.points['net(1, 0.8660254037844386)'], self.points['net(2, 0.8660254037844386)']])), ('line_8', c.project([self.points['net(1.5, 0)'], self.points['net(2, 0.8660254037844386)']])), ('line_9', c.project([self.points['net(1.5, 0)'], self.points['net(2.5, 0)']])), ('line_10', c.project([self.points['net(2, 0.8660254037844386)'], self.points['net(2.5, 0)']])), ('line_11', c.project([self.points['net(2, 0.8660254037844386)'], self.points['net(2.5, 1.7320508075688772)']])), ('line_12', c.project([self.points['net(2, 0.8660254037844386)'], self.points['net(3, 0.8660254037844386)']])), ('line_13', c.project([self.points['net(2.5, 0)'], self.points['net(3, 0.8660254037844386)']])), ('line_14', c.project([self.points['net(2.5, 0)'], self.points['net(3.5, 0)']])), ('line_15', c.project([self.points['net(2.5, 1.7320508075688772)'], self.points['net(3, 0.8660254037844386)']])), ('line_16', c.project([self.points['net(3, 0.8660254037844386)'], self.points['net(3.5, 0)']])), ('line_17', c.project([self.points['T'], self.points['L']])), ('line_18', c.project([self.points['T'], self.points['R']])), ('line_19', c.project([self.points['T'], self.points['F']]))]:
                c.line(points, id=object_id, clip_on=False, zorder=3)
            c.line(c.project([self.points['T'], self.points['H']]), id='line_20', linestyle=(0, [4, 3]), clip_on=False)
            for object_id, points in [('line_21', c.project([self.points['Z'], self.points['L']])), ('line_22', c.project([self.points['Z'], self.points['R']])), ('line_23', c.project([self.points['Z'], self.points['F']]))]:
                c.line(points, id=object_id, clip_on=False, zorder=3)
            c.line(c.project([self.points['Z'], self.points['H']]), id='line_24', linestyle=(0, [4, 3]), clip_on=False)
            c.line(c.project([self.points['L'], self.points['F']]), id='line_25', clip_on=False, zorder=3)
            c.line(c.project([self.points['L'], self.points['H']]), id='line_26', linestyle=(0, [4, 3]), clip_on=False)
            c.line(c.project([self.points['R'], self.points['F']]), id='line_27', clip_on=False, zorder=3)
            c.line(c.project([self.points['R'], self.points['H']]), id='line_28', linestyle=(0, [4, 3]), clip_on=False)
            for object_id, points in [('line_29', c.project([self.points['arrowA'], self.points['arrowB']])), ('line_30', c.project([self.points['arrowB'], self.points['tipup']])), ('line_31', c.project([self.points['arrowB'], self.points['tipdown']]))]:
                c.line(points, id=object_id, clip_on=False, zorder=3)
            for object_id, text, anchor in [('label_0', '1', c.project(self.points['label1'])), ('label_1', '3', c.project(self.points['label3'])), ('label_2', '4', c.project(self.points['label4'])), ('label_3', '5', c.project(self.points['label5'])), ('label_4', '6', c.project(self.points['label6']))]:
                c.text(text, anchor, id=object_id, offset_pt=[0, 0], vertex=False)
            c.text('Q', c.project(self.points['labelQ']), offset_pt=[0, 0], vertex=True, id='label_5')
            c.text('2', c.project(self.points['label2']), offset_pt=[0, 0], vertex=False, id='label_6')
            c.text('7', c.project(self.points['label7']), offset_pt=[0, 0], vertex=False, id='label_7')
            c.text('Q', c.project(self.points['q']), offset_pt=[6, 1], vertex=True, id='label_8')
            c.text('?', c.project(self.points['unknown']), offset_pt=[0, 0], vertex=True, id='label_9')
            return c.save(output_path)

    def draw_C01(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Solid240_C01.png'
        with Canvas(SOLID, xlim=(-0.17661733968185622, 7.265553692550153), ylim=(-3.2880728142237854, 4.154098218008224), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
            for object_id, points in [('line_0', [[0.0, 0.8660254037844386], [0.5, 0.0]]), ('line_1', [[0.0, 0.8660254037844386], [1.0, 0.8660254037844386]]), ('line_2', [[0.5, 0.0], [1.0, -0.8660254037844386]]), ('line_3', [[0.5, 0.0], [1.0, 0.8660254037844386]]), ('line_4', [[0.5, 0.0], [1.5, 0.0]]), ('line_5', [[1.0, -0.8660254037844386], [1.5, 0.0]]), ('line_6', [[1.0, 0.8660254037844386], [1.5, 0.0]]), ('line_7', [[1.0, 0.8660254037844386], [2.0, 0.8660254037844386]]), ('line_8', [[1.5, 0.0], [2.0, 0.8660254037844386]]), ('line_9', [[1.5, 0.0], [2.5, 0.0]])]:
                c.line(points, id=object_id, zorder=3, clip_on=False)
            c.line([[2.0, 0.8660254037844386], [2.5, 0.0]], id='line_10', zorder=3, clip_on=False, color='#16A34A')
            c.line([[2.0, 0.8660254037844386], [2.5, 1.7320508075688772]], id='line_11', zorder=3, clip_on=False)
            c.line([[2.0, 0.8660254037844386], [3.0, 0.8660254037844386]], id='line_12', zorder=3, clip_on=False, color='#DC2626')
            c.line([[2.5, 0.0], [3.0, 0.8660254037844386]], id='line_13', zorder=3, clip_on=False, color='#2563EB')
            c.line([[2.5, 0.0], [3.5, 0.0]], id='line_14', zorder=3, clip_on=False, color='#16A34A')
            c.line([[2.5, 1.7320508075688772], [3.0, 0.8660254037844386]], id='line_15', zorder=3, clip_on=False)
            c.line([[3.0, 0.8660254037844386], [3.5, 0.0]], id='line_16', zorder=3, clip_on=False, color='#DC2626')
            for object_id, points in [('line_17', [[6.1, 1.417333478872227], [5.111063647131703, 0.4123946153690259]]), ('line_18', [[6.1, 1.417333478872227], [7.088936352868297, 0.48760538463097414]]), ('line_19', [[6.1, 1.417333478872227], [6.248340452930244, 0.199297435793506]])]:
                c.line(points, id=object_id, zorder=3, clip_on=False)
            c.line([[6.1, 1.417333478872227], [5.951659547069755, 0.700702564206494]], id='line_20', clip_on=False, linestyle=(0.0, [4.0, 3.0]))
            for object_id, points in [('line_21', [[6.1, -0.5173334788722268], [5.111063647131703, 0.4123946153690259]]), ('line_22', [[6.1, -0.5173334788722268], [7.088936352868297, 0.48760538463097414]]), ('line_23', [[6.1, -0.5173334788722268], [6.248340452930244, 0.199297435793506]])]:
                c.line(points, id=object_id, zorder=3, clip_on=False)
            c.line([[6.1, -0.5173334788722268], [5.951659547069755, 0.700702564206494]], id='line_24', clip_on=False, linestyle=(0.0, [4.0, 3.0]))
            c.line([[5.111063647131703, 0.4123946153690259], [6.248340452930244, 0.199297435793506]], id='line_25', zorder=3, clip_on=False)
            c.line([[5.111063647131703, 0.4123946153690259], [5.951659547069755, 0.700702564206494]], id='line_26', clip_on=False, linestyle=(0.0, [4.0, 3.0]))
            c.line([[7.088936352868297, 0.48760538463097414], [6.248340452930244, 0.199297435793506]], id='line_27', zorder=3, clip_on=False)
            c.line([[7.088936352868297, 0.48760538463097414], [5.951659547069755, 0.700702564206494]], id='line_28', clip_on=False, linestyle=(0.0, [4.0, 3.0]))
            for object_id, points in [('line_29', [[3.75, 0.55], [4.8, 0.55]]), ('line_30', [[4.8, 0.55], [4.67, 0.61]]), ('line_31', [[4.8, 0.55], [4.67, 0.49]])]:
                c.line(points, id=object_id, zorder=3, clip_on=False)
            for object_id, text, anchor in [('label_0', '1', (0.5, 0.5773502691896257)), ('label_1', '3', (1.0, 0.28867513459481287)), ('label_2', '4', (1.5, 0.5773502691896257)), ('label_3', '5', (2.0, 0.28867513459481287)), ('label_4', '6', (2.5, 0.5773502691896257))]:
                c.text(text, anchor, id=object_id, rotation_mode='default', offset_pt=(0, 0), annotation_clip=None)
            c.text('Q', (3.0, 0.28867513459481287), id='label_5', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(0, 0), annotation_clip=None)
            c.text('2', (1.0, -0.28867513459481287), id='label_6', rotation_mode='default', offset_pt=(0, 0), annotation_clip=None)
            c.text('7', (2.5, 1.1547005383792515), id='label_7', rotation_mode='default', offset_pt=(0, 0), annotation_clip=None)
            c.text('Q', (5.7209077314004855, 0.843476886149249), id='label_8', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(6, 1), annotation_clip=None)
            c.text('?', (6.380198633312684, 0.8685471425698983), id='label_9', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(0, 0), annotation_clip=None)
            return c.save(output_path)

    def draw_C02(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Solid240_C02.png'
        with Canvas(SOLID, xlim=(-0.17661733968185622, 7.265553692550153), ylim=(-3.2880728142237854, 4.154098218008224), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
            for object_id, points in [('line_0', [[0.0, 0.8660254037844386], [0.5, 0.0]]), ('line_1', [[0.0, 0.8660254037844386], [1.0, 0.8660254037844386]]), ('line_2', [[0.5, 0.0], [1.0, -0.8660254037844386]])]:
                c.line(points, id=object_id, zorder=3, clip_on=False)
            c.line([[0.5, 0.0], [1.0, 0.8660254037844386]], id='line_3', zorder=3, clip_on=False, color='#2563EB')
            c.line([[0.5, 0.0], [1.5, 0.0]], id='line_4', zorder=3, clip_on=False, color='#DC2626')
            c.line([[1.0, -0.8660254037844386], [1.5, 0.0]], id='line_5', zorder=3, clip_on=False)
            c.line([[1.0, 0.8660254037844386], [1.5, 0.0]], id='line_6', zorder=3, clip_on=False, color='#16A34A')
            for object_id, points in [('line_7', [[1.0, 0.8660254037844386], [2.0, 0.8660254037844386]]), ('line_8', [[1.5, 0.0], [2.0, 0.8660254037844386]]), ('line_9', [[1.5, 0.0], [2.5, 0.0]]), ('line_10', [[2.0, 0.8660254037844386], [2.5, 0.0]]), ('line_11', [[2.0, 0.8660254037844386], [2.5, 1.7320508075688772]]), ('line_12', [[2.0, 0.8660254037844386], [3.0, 0.8660254037844386]])]:
                c.line(points, id=object_id, zorder=3, clip_on=False)
            c.line([[2.5, 0.0], [3.0, 0.8660254037844386]], id='line_13', zorder=3, clip_on=False, color='#DC2626')
            c.line([[2.5, 0.0], [3.5, 0.0]], id='line_14', zorder=3, clip_on=False, color='#16A34A')
            c.line([[2.5, 1.7320508075688772], [3.0, 0.8660254037844386]], id='line_15', zorder=3, clip_on=False)
            c.line([[3.0, 0.8660254037844386], [3.5, 0.0]], id='line_16', zorder=3, clip_on=False, color='#2563EB')
            for object_id, points in [('line_17', [[6.1, 1.417333478872227], [5.111063647131703, 0.4123946153690259]]), ('line_18', [[6.1, 1.417333478872227], [7.088936352868297, 0.48760538463097414]]), ('line_19', [[6.1, 1.417333478872227], [6.248340452930244, 0.199297435793506]])]:
                c.line(points, id=object_id, zorder=3, clip_on=False)
            c.line([[6.1, 1.417333478872227], [5.951659547069755, 0.700702564206494]], id='line_20', clip_on=False, linestyle=(0.0, [4.0, 3.0]))
            for object_id, points in [('line_21', [[6.1, -0.5173334788722268], [5.111063647131703, 0.4123946153690259]]), ('line_22', [[6.1, -0.5173334788722268], [7.088936352868297, 0.48760538463097414]]), ('line_23', [[6.1, -0.5173334788722268], [6.248340452930244, 0.199297435793506]])]:
                c.line(points, id=object_id, zorder=3, clip_on=False)
            c.line([[6.1, -0.5173334788722268], [5.951659547069755, 0.700702564206494]], id='line_24', clip_on=False, linestyle=(0.0, [4.0, 3.0]))
            c.line([[5.111063647131703, 0.4123946153690259], [6.248340452930244, 0.199297435793506]], id='line_25', zorder=3, clip_on=False)
            c.line([[5.111063647131703, 0.4123946153690259], [5.951659547069755, 0.700702564206494]], id='line_26', clip_on=False, linestyle=(0.0, [4.0, 3.0]))
            c.line([[7.088936352868297, 0.48760538463097414], [6.248340452930244, 0.199297435793506]], id='line_27', zorder=3, clip_on=False)
            c.line([[7.088936352868297, 0.48760538463097414], [5.951659547069755, 0.700702564206494]], id='line_28', clip_on=False, linestyle=(0.0, [4.0, 3.0]))
            for object_id, points in [('line_29', [[3.75, 0.55], [4.8, 0.55]]), ('line_30', [[4.8, 0.55], [4.67, 0.61]]), ('line_31', [[4.8, 0.55], [4.67, 0.49]])]:
                c.line(points, id=object_id, zorder=3, clip_on=False)
            for object_id, text, anchor in [('label_0', '1', (0.5, 0.5773502691896257)), ('label_1', '3', (1.0, 0.28867513459481287)), ('label_2', '4', (1.5, 0.5773502691896257)), ('label_3', '5', (2.0, 0.28867513459481287)), ('label_4', '6', (2.5, 0.5773502691896257))]:
                c.text(text, anchor, id=object_id, rotation_mode='default', offset_pt=(0, 0), annotation_clip=None)
            c.text('Q', (3.0, 0.28867513459481287), id='label_5', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(0, 0), annotation_clip=None)
            c.text('2', (1.0, -0.28867513459481287), id='label_6', rotation_mode='default', offset_pt=(0, 0), annotation_clip=None)
            c.text('7', (2.5, 1.1547005383792515), id='label_7', rotation_mode='default', offset_pt=(0, 0), annotation_clip=None)
            c.text('Q', (5.7209077314004855, 0.843476886149249), id='label_8', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(6, 1), annotation_clip=None)
            c.text('?', (6.380198633312684, 0.8685471425698983), id='label_9', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(0, 0), annotation_clip=None)
            return c.save(output_path)
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Solid240')
    parser.add_argument('output', nargs='?')
    parser.add_argument('--variant', choices=('C01', 'C02'))
    args = parser.parse_args()
    print(Solid240().draw(args.output, variant=args.variant))
