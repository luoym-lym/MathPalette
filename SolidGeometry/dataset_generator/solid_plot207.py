"""Frozen question Solid207; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Solid207:

    def __init__(self):
        self.id = 'Solid207'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:2042'
        self.question = 'Three 12 cm $\\times$ 12 cm squares are each cut into two pieces $A$ and $B$, as shown in the first figure below, by joining the midpoints of two adjacent sides.  These six pieces are then attached to a regular hexagon, as shown in the second figure, so as to fold into a polyhedron.  What is the volume (in $\\text{cm}^3$) of this polyhedron?'
        self.answer = '864'
        self.answer_type = 'number'
        self.query = self.question
        self.points = {'h0': [8.485281374238571, 0.0, 0],
         'h1': [4.2426406871192865, 7.3484692283495345, 0],
         'h2': [-4.242640687119284, 7.348469228349535, 0],
         'h3': [-8.485281374238571, 1.039147267482592e-15, 0],
         'h4': [-4.242640687119289, -7.348469228349533, 0],
         'h5': [4.2426406871192865, -7.3484692283495345, 0],
         'f0_0': [8.485281374238571, 0.0, 0.0],
         'f0_1': [10.038195644853698, 5.79555495773441, 0.0],
         'f0_2': [4.242640687119287, 7.3484692283495345, 0.0],
         'label0': [7.833654876348836, 4.522762751598624, 0.0],
         'f1_0': [4.242640687119287, 7.3484692283495345, 0.0],
         'f1_1': [8.485281374238573, 11.59110991546882, 0.0],
         'f1_2': [2.6645352591003757e-15, 20.07639128970739, 0.0],
         'f1_3': [-8.48528137423857, 11.59110991546882, 0.0],
         'f1_4': [-4.242640687119284, 7.3484692283495345, 0.0],
         'label1': [1.7763568394002505e-15, 11.59110991546882, 0.0],
         'f2_0': [-4.242640687119284, 7.348469228349535, 0.0],
         'f2_1': [-10.038195644853694, 5.795554957734412, 0.0],
         'f2_2': [-8.485281374238571, 8.881784197001252e-16, 0.0],
         'label2': [-7.8336548763488345, 4.522762751598625, 0.0],
         'f3_0': [-8.485281374238571, 8.881784197001252e-16, 0.0],
         'f3_1': [-14.28083633197298, 1.5529142706151267, 0.0],
         'f3_2': [-17.38666487320323, -10.038195644853689, 0.0],
         'f3_3': [-5.795554957734415, -13.14402418608394, 0.0],
         'f3_4': [-4.242640687119289, -7.348469228349533, 0.0],
         'label3': [-10.038195644853698, -5.7955549577344065, 0.0],
         'f4_0': [-4.242640687119289, -7.348469228349533, 0.0],
         'f4_1': [-2.220446049250313e-15, -11.59110991546882, 0.0],
         'f4_2': [4.242640687119286, -7.3484692283495345, 0.0],
         'label4': [-1.6875389974302379e-15, -9.045525503197249, 0.0],
         'f5_0': [4.242640687119287, -7.3484692283495345, 0.0],
         'f5_1': [5.795554957734412, -13.144024186083943, 0.0],
         'f5_2': [17.38666487320323, -10.038195644853694, 0.0],
         'f5_3': [14.280836331972981, 1.5529142706151249, 0.0],
         'f5_4': [8.485281374238571, 0.0, 0.0],
         'label5': [10.038195644853698, -5.79555495773441, 0.0],
         's0': [-39.032294321497425, -5.939696961967, 0],
         's1': [-27.032294321497425, -5.939696961967, 0],
         's2': [-27.032294321497425, 6.060303038033, 0],
         's3': [-39.032294321497425, 6.060303038033, 0],
         'sm': [-33.032294321497425, 6.060303038033, 0],
         'sn': [-27.032294321497425, 0.06030303803300008, 0],
         'sa': [-34.032294321497425, -0.9396969619669999, 0],
         'sb': [-29.032294321497425, 4.060303038033, 0]}
        self.subject = 'SolidGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'SolidGeometry' / 'dataset_generator/scenes/Solid207.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('SolidGeometry', self.id, variant, output_path)
        with Canvas(SOLID, xlim=[-40.43794475825942, 18.792315309965222], ylim=[-26.148946482300595, 33.08131358592404], projection=[[1, 0, 0], [0, 1, 0]], origin=[0, 0, 0], offset=[0, 0]) as c:
            for object_id, points in [('line_0', c.project([self.points['h0'], self.points['h1']])), ('line_1', c.project([self.points['h1'], self.points['h2']])), ('line_2', c.project([self.points['h2'], self.points['h3']])), ('line_3', c.project([self.points['h3'], self.points['h4']])), ('line_4', c.project([self.points['h4'], self.points['h5']])), ('line_5', c.project([self.points['h5'], self.points['h0']])), ('line_6', c.project([self.points['f0_0'], self.points['f0_1']])), ('line_7', c.project([self.points['f0_1'], self.points['f0_2']])), ('line_8', c.project([self.points['f1_0'], self.points['f1_1']])), ('line_9', c.project([self.points['f1_1'], self.points['f1_2']])), ('line_10', c.project([self.points['f1_2'], self.points['f1_3']])), ('line_11', c.project([self.points['f1_3'], self.points['f1_4']])), ('line_12', c.project([self.points['f2_0'], self.points['f2_1']])), ('line_13', c.project([self.points['f2_1'], self.points['f2_2']])), ('line_14', c.project([self.points['f3_0'], self.points['f3_1']])), ('line_15', c.project([self.points['f3_1'], self.points['f3_2']])), ('line_16', c.project([self.points['f3_2'], self.points['f3_3']])), ('line_17', c.project([self.points['f3_3'], self.points['f3_4']])), ('line_18', c.project([self.points['f4_0'], self.points['f4_1']])), ('line_19', c.project([self.points['f4_1'], self.points['f4_2']])), ('line_20', c.project([self.points['f5_0'], self.points['f5_1']])), ('line_21', c.project([self.points['f5_1'], self.points['f5_2']])), ('line_22', c.project([self.points['f5_2'], self.points['f5_3']])), ('line_23', c.project([self.points['f5_3'], self.points['f5_4']])), ('line_24', c.project([self.points['s0'], self.points['s1']])), ('line_25', c.project([self.points['s1'], self.points['s2']])), ('line_26', c.project([self.points['s2'], self.points['s3']])), ('line_27', c.project([self.points['s3'], self.points['s0']])), ('line_28', c.project([self.points['sm'], self.points['sn']]))]:
                c.line(points, id=object_id, clip_on=False, zorder=3)
            for object_id, text, anchor in [('label_0', 'B', c.project(self.points['label0'])), ('label_1', 'A', c.project(self.points['label1'])), ('label_2', 'B', c.project(self.points['label2'])), ('label_3', 'A', c.project(self.points['label3'])), ('label_4', 'B', c.project(self.points['label4'])), ('label_5', 'A', c.project(self.points['label5'])), ('label_6', 'A', c.project(self.points['sa'])), ('label_7', 'B', c.project(self.points['sb']))]:
                c.text(text, anchor, id=object_id, offset_pt=[0, 0], vertex=False)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Solid207().draw(sys.argv[1] if len(sys.argv) > 1 else None))
