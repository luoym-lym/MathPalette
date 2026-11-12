"""Frozen question Solid245; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Solid245:

    def __init__(self):
        self.id = 'Solid245'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:3004'
        self.question = 'The lateral surface area of the frustum of a solid right cone is the product of one-half the slant height ($L$) and the sum of the circumferences of the two circular faces. What is the number of square centimeters in the total surface area of the frustum shown here? Express your answer in terms of $\\pi$.'
        self.answer = '256\\pi'
        self.answer_type = 'number'
        self.query = self.question
        self.points = {'B': [0, 0, 0],
         'T': [0, 0, 8],
         'tl': [-4, 0, 8],
         'tr': [4, 0, 8],
         'bl': [-10, 0, 0],
         'br': [10, 0, 0],
         'height': [0, 0, 4],
         'l0': [-9.886859966642593, 1.5000000000000004, 0],
         'l1': [-3.9547439866570375, 0.6000000000000002, 8],
         'r0': [9.886859966642593, 1.5000000000000002, 0],
         'r1': [3.9547439866570375, 0.6000000000000001, 8],
         'slant': [6.920801976649815, 1.0500000000000003, 4.0]}
        self.subject = 'SolidGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'SolidGeometry' / 'dataset_generator/scenes/Solid245.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('SolidGeometry', self.id, variant, output_path)
        with Canvas(SOLID, xlim=[-10.490660527222452, 10.490660527222452], ylim=[-6.53232620695257, 14.448994847492335], projection=[[1, 0, 0], [0, 0.2, 1]], origin=[0, 0, 0], offset=[0, 0]) as c:
            t = np.radians(np.linspace(0, 360, 721))
            xyz = np.asarray(self.points['T']) + 4 * (np.cos(t)[:, None] * np.array([1, 0, 0]) + np.sin(t)[:, None] * np.array([0, 1, 0]))
            c.line(c.project(xyz), clip_on=False, zorder=3, id='arc_0')
            t = np.radians(np.linspace(0, 180, 721))
            xyz = np.asarray(self.points['B']) + 10 * (np.cos(t)[:, None] * np.array([1, 0, 0]) + np.sin(t)[:, None] * np.array([0, 1, 0]))
            c.line(c.project(xyz), linestyle=(0, [4, 3]), clip_on=False, id='arc_1')
            t = np.radians(np.linspace(180, 360, 721))
            xyz = np.asarray(self.points['B']) + 10 * (np.cos(t)[:, None] * np.array([1, 0, 0]) + np.sin(t)[:, None] * np.array([0, 1, 0]))
            for object_id, points in [('arc_2', c.project(xyz)), ('line_3', c.project([self.points['l0'], self.points['l1']])), ('line_4', c.project([self.points['r0'], self.points['r1']]))]:
                c.line(points, id=object_id, clip_on=False, zorder=3)
            c.line(c.project([self.points['tl'], self.points['tr']]), id='line_5', linestyle=(0, [4, 3]), clip_on=False, zorder=3)
            c.line(c.project([self.points['bl'], self.points['br']]), id='line_6', linestyle=(0, [4, 3]), clip_on=False, zorder=3)
            c.line(c.project([self.points['T'], self.points['B']]), id='line_7', clip_on=False, zorder=3)
            c.text('8cm', c.project(self.points['T']), offset_pt=[0, 39], vertex=False, id='label_0')
            c.text('20cm', c.project(self.points['B']), offset_pt=[0, -20], vertex=False, id='label_1')
            c.text('8cm', c.project(self.points['height']), offset_pt=[29, 0], vertex=False, id='label_2')
            c.text('L', c.project(self.points['slant']), offset_pt=[-25, 0], vertex=False, id='label_3')
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Solid245().draw(sys.argv[1] if len(sys.argv) > 1 else None))
