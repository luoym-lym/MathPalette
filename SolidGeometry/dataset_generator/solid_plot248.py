"""Frozen question Solid248; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Solid248:

    def __init__(self):
        self.id = 'Solid248'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:3039'
        self.question = 'The volume of the cylinder shown is $45\\pi$ cubic cm. What is the height in centimeters of the cylinder?'
        self.answer = '5'
        self.answer_type = 'number'
        self.query = self.question
        self.points = {'O': [0, 0, 5], 'B': [0, 0, 0], 'R': [3, 0, 5], 'L': [-3, 0, 5], 'r': [3, 0, 0], 'l': [-3, 0, 0], 'labelr': [1.5, 0, 5], 'labelh': [3, 0, 2.5]}
        self.subject = 'SolidGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'SolidGeometry' / 'dataset_generator/scenes/Solid248.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('SolidGeometry', self.id, variant, output_path)
        with Canvas(SOLID, xlim=[-3.4147053983556352, 3.7172517181351097], ylim=[-1.0659785582453725, 6.065978558245373], projection=[[1, 0, 0], [0, 0.3, 1]], origin=[0, 0, 0], offset=[0, 0]) as c:
            t = np.radians(np.linspace(0, 360, 721))
            xyz = np.asarray(self.points['O']) + 3 * (np.cos(t)[:, None] * np.array([1, 0, 0]) + np.sin(t)[:, None] * np.array([0, 1, 0]))
            c.line(c.project(xyz), clip_on=False, zorder=3, id='arc_0')
            t = np.radians(np.linspace(180, 360, 721))
            xyz = np.asarray(self.points['B']) + 3 * (np.cos(t)[:, None] * np.array([1, 0, 0]) + np.sin(t)[:, None] * np.array([0, 1, 0]))
            for object_id, points in [('arc_1', c.project(xyz)), ('line_2', c.project([self.points['L'], self.points['l']])), ('line_3', c.project([self.points['R'], self.points['r']])), ('line_4', c.project([self.points['O'], self.points['R']]))]:
                c.line(points, id=object_id, clip_on=False, zorder=3)
            c.text('r = 3', c.project(self.points['labelr']), offset_pt=[0, 16], vertex=False, id='label_0')
            c.text('h', c.project(self.points['labelh']), offset_pt=[18, 0], vertex=False, id='label_1')
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Solid248().draw(sys.argv[1] if len(sys.argv) > 1 else None))
