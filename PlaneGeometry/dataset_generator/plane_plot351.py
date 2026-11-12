"""Frozen question Plane351; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane351:

    def __init__(self):
        self.id = 'Plane351'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:1194'
        self.question = 'The figure of side 1 is formed by six equal triangles, made with 12 sticks. How many matchsticks are needed to complete the figure of side 2, partially represented?'
        self.answer = '36'
        self.answer_type = 'number'
        self.query = self.question
        self.points = {'O': [0, 0],
         'V0': [1.0, 0.0],
         'V1': [0.5000000000000001, 0.8660254037844386],
         'V2': [-0.4999999999999998, 0.8660254037844387],
         'V3': [-1.0, 1.2246467991473532e-16],
         'V4': [-0.5000000000000004, -0.8660254037844384],
         'V5': [0.5000000000000001, -0.8660254037844386],
         'P0': [2, 1.7320508075688772],
         'P1': [2.5, 0.8660254037844386],
         'P2': [3, 0],
         'P3': [3.5, 0.8660254037844386],
         'P4': [4, 0],
         'P5': [5, 0],
         'label1': [0, -1.25],
         'label2': [3.5, -1.25],
         'side0gapA': [0.9875, 0.021650635094610966],
         'side0gapB': [0.5125000000000001, 0.8443747686898276],
         'spoke0gapA': [0.025, 0.0],
         'spoke0gapB': [0.975, 0.0],
         'side1gapA': [0.4750000000000001, 0.8660254037844386],
         'side1gapB': [-0.47499999999999976, 0.8660254037844387],
         'spoke1gapA': [0.012500000000000004, 0.021650635094610966],
         'spoke1gapB': [0.4875000000000001, 0.8443747686898276],
         'side2gapA': [-0.5124999999999997, 0.8443747686898277],
         'side2gapB': [-0.9875, 0.021650635094611088],
         'spoke2gapA': [-0.012499999999999995, 0.02165063509461097],
         'spoke2gapB': [-0.48749999999999977, 0.8443747686898277],
         'side3gapA': [-0.9875, -0.02165063509461084],
         'side3gapB': [-0.5125000000000004, -0.8443747686898274],
         'spoke3gapA': [-0.025, 3.061616997868383e-18],
         'spoke3gapB': [-0.975, 1.1940306291686693e-16],
         'side4gapA': [-0.4750000000000004, -0.8660254037844384],
         'side4gapB': [0.4750000000000001, -0.8660254037844386],
         'spoke4gapA': [-0.012500000000000011, -0.02165063509461096],
         'spoke4gapB': [-0.48750000000000043, -0.8443747686898274],
         'side5gapA': [0.5125000000000001, -0.8443747686898276],
         'side5gapB': [0.9875, -0.021650635094610966],
         'spoke5gapA': [0.012500000000000004, -0.021650635094610966],
         'spoke5gapB': [0.4875000000000001, -0.8443747686898276],
         'partial0gapA': [2.0125, 1.7104001724742661],
         'partial0gapB': [2.4875, 0.8876760388790496],
         'partial1gapA': [2.5125, 0.8443747686898276],
         'partial1gapB': [2.9875, 0.021650635094610966],
         'partial2gapA': [3.0125, 0.021650635094610966],
         'partial2gapB': [3.4875, 0.8443747686898276],
         'partial3gapA': [3.5125, 0.8443747686898276],
         'partial3gapB': [3.9875, 0.021650635094610966],
         'partial4gapA': [3.975, 0.0],
         'partial4gapB': [3.025, 0.0],
         'partial5gapA': [4.025, 0.0],
         'partial5gapB': [4.975, 0.0]}
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane351.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-1.1369015302412477, 5.127839046514371], ylim=[-2.926277524815745, 3.338463051939874]) as c:
            for object_id, points in [('side0', [self.points['side0gapA'], self.points['side0gapB']]), ('spoke0', [self.points['spoke0gapA'], self.points['spoke0gapB']]), ('side1', [self.points['side1gapA'], self.points['side1gapB']]), ('spoke1', [self.points['spoke1gapA'], self.points['spoke1gapB']]), ('side2', [self.points['side2gapA'], self.points['side2gapB']]), ('spoke2', [self.points['spoke2gapA'], self.points['spoke2gapB']]), ('side3', [self.points['side3gapA'], self.points['side3gapB']]), ('spoke3', [self.points['spoke3gapA'], self.points['spoke3gapB']]), ('side4', [self.points['side4gapA'], self.points['side4gapB']]), ('spoke4', [self.points['spoke4gapA'], self.points['spoke4gapB']]), ('side5', [self.points['side5gapA'], self.points['side5gapB']]), ('spoke5', [self.points['spoke5gapA'], self.points['spoke5gapB']]), ('partial0', [self.points['partial0gapA'], self.points['partial0gapB']]), ('partial1', [self.points['partial1gapA'], self.points['partial1gapB']]), ('partial2', [self.points['partial2gapA'], self.points['partial2gapB']]), ('partial3', [self.points['partial3gapA'], self.points['partial3gapB']]), ('partial4', [self.points['partial4gapA'], self.points['partial4gapB']]), ('partial5', [self.points['partial5gapA'], self.points['partial5gapB']])]:
                c.line(points, id=object_id)
            c.text('side 1', self.points['label1'], offset_pt=[0, 0], vertex=False, id='label1')
            c.text('side 2', self.points['label2'], offset_pt=[0, 0], vertex=False, id='label2')
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane351().draw(sys.argv[1] if len(sys.argv) > 1 else None))
