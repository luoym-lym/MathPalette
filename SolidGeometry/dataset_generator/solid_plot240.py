"""Frozen question Solid240; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Solid240:

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
        self.subject = 'SolidGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'SolidGeometry' / 'dataset_generator/scenes/Solid240.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('SolidGeometry', self.id, variant, output_path)
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
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Solid240().draw(sys.argv[1] if len(sys.argv) > 1 else None))
