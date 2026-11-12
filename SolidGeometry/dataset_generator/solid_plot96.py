"""Frozen question Solid96; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Solid96:

    def __init__(self):
        self.id = 'Solid96'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:264'
        self.question = 'The curved surfaces of two identical cylinders are cut open along the vertical dotted line, as shown and then stuck together to create the curved surface of one big cylinder. What can be said about the volume of the resulting cylinder compared to the volume of one of the small cylinders?\nChoices:\nA:It is 2-times as big.\nB:It is 3-times as big.\nC:It is $\\pi$-times as big.\nD:It is 4-times as big.\nE:It is 8-times as big.'
        self.answer = 'D'
        self.answer_type = 'choice'
        self.choices = {'A': 'It is 2-times as big.', 'B': 'It is 3-times as big.', 'C': 'It is $\\pi$-times as big.', 'D': 'It is 4-times as big.', 'E': 'It is 8-times as big.'}
        self.query = self.question
        self.points = {'small1bottom': [0, 0, 0],
         'small1top': [0, 0, 3],
         'small1left0': [-1, 0, 0],
         'small1left1': [-1, 0, 3],
         'small1right0': [1, 0, 0],
         'small1right1': [1, 0, 3],
         'small1front0': [-0.35, -0.9367496997597597, 0],
         'small1front1': [-0.35, -0.9367496997597597, 3],
         'small2bottom': [2.6, 0, 0],
         'small2top': [2.6, 0, 3],
         'small2left0': [1.6, 0, 0],
         'small2left1': [1.6, 0, 3],
         'small2right0': [3.6, 0, 0],
         'small2right1': [3.6, 0, 3],
         'small2front0': [2.25, -0.9367496997597597, 0],
         'small2front1': [2.25, -0.9367496997597597, 3],
         'largebottom': [8.3, 0, 0],
         'largetop': [8.3, 0, 3],
         'largeleft0': [6.300000000000001, 0, 0],
         'largeleft1': [6.300000000000001, 0, 3],
         'largeright0': [10.3, 0, 0],
         'largeright1': [10.3, 0, 3],
         'largefront0': [7.6000000000000005, -1.8734993995195195, 0],
         'largefront1': [7.6000000000000005, -1.8734993995195195, 3],
         'largeback0': [9.0, 1.8734993995195195, 0],
         'largeback1': [9.0, 1.8734993995195195, 3],
         'arr0': [4, 0, 1.5],
         'arr1': [5.5, 0, 1.5],
         'arr2': [5.25, 0, 1.62],
         'arr3': [5.25, 0, 1.38]}
        self.subject = 'SolidGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'SolidGeometry' / 'dataset_generator/scenes/Solid96.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('SolidGeometry', self.id, variant, output_path)
        with Canvas(SOLID, xlim=[-1.2900559771921118, 10.589990700274058], ylim=[-4.440023338733085, 7.440023338733085], projection=[[1, 0, 0], [0, 0.25, 1]], origin=[0, 0, 0], offset=[0, 0]) as c:
            t = np.radians(np.linspace(0, 180, 121))
            xyz = np.asarray(self.points['small1bottom']) + 1 * (np.cos(t)[:, None] * np.array([1, 0, 0]) + np.sin(t)[:, None] * np.array([0, 1, 0]))
            c.line(c.project(xyz), linestyle=(0, [4, 3]), clip_on=False, id='small1bottomrim')
            t = np.radians(np.linspace(180, 360, 121))
            xyz = np.asarray(self.points['small1bottom']) + 1 * (np.cos(t)[:, None] * np.array([1, 0, 0]) + np.sin(t)[:, None] * np.array([0, 1, 0]))
            c.line(c.project(xyz), clip_on=False, zorder=3, id='small1bottomrim')
            t = np.radians(np.linspace(0, 180, 121))
            xyz = np.asarray(self.points['small1top']) + 1 * (np.cos(t)[:, None] * np.array([1, 0, 0]) + np.sin(t)[:, None] * np.array([0, 1, 0]))
            c.line(c.project(xyz), clip_on=False, zorder=3, id='small1toprim')
            t = np.radians(np.linspace(180, 360, 121))
            xyz = np.asarray(self.points['small1top']) + 1 * (np.cos(t)[:, None] * np.array([1, 0, 0]) + np.sin(t)[:, None] * np.array([0, 1, 0]))
            for object_id, points in [('small1toprim', c.project(xyz)), ('small1left', c.project([self.points['small1left0'], self.points['small1left1']])), ('small1right', c.project([self.points['small1right0'], self.points['small1right1']]))]:
                c.line(points, id=object_id, clip_on=False, zorder=3)
            c.line(c.project([self.points['small1front0'], self.points['small1front1']]), id='small1frontseam', linestyle=(0, [4, 3]), clip_on=False, zorder=3)
            t = np.radians(np.linspace(0, 180, 121))
            xyz = np.asarray(self.points['small2bottom']) + 1 * (np.cos(t)[:, None] * np.array([1, 0, 0]) + np.sin(t)[:, None] * np.array([0, 1, 0]))
            c.line(c.project(xyz), linestyle=(0, [4, 3]), clip_on=False, id='small2bottomrim')
            t = np.radians(np.linspace(180, 360, 121))
            xyz = np.asarray(self.points['small2bottom']) + 1 * (np.cos(t)[:, None] * np.array([1, 0, 0]) + np.sin(t)[:, None] * np.array([0, 1, 0]))
            c.line(c.project(xyz), clip_on=False, zorder=3, id='small2bottomrim')
            t = np.radians(np.linspace(0, 180, 121))
            xyz = np.asarray(self.points['small2top']) + 1 * (np.cos(t)[:, None] * np.array([1, 0, 0]) + np.sin(t)[:, None] * np.array([0, 1, 0]))
            c.line(c.project(xyz), clip_on=False, zorder=3, id='small2toprim')
            t = np.radians(np.linspace(180, 360, 121))
            xyz = np.asarray(self.points['small2top']) + 1 * (np.cos(t)[:, None] * np.array([1, 0, 0]) + np.sin(t)[:, None] * np.array([0, 1, 0]))
            for object_id, points in [('small2toprim', c.project(xyz)), ('small2left', c.project([self.points['small2left0'], self.points['small2left1']])), ('small2right', c.project([self.points['small2right0'], self.points['small2right1']]))]:
                c.line(points, id=object_id, clip_on=False, zorder=3)
            c.line(c.project([self.points['small2front0'], self.points['small2front1']]), id='small2frontseam', linestyle=(0, [4, 3]), clip_on=False, zorder=3)
            t = np.radians(np.linspace(0, 180, 121))
            xyz = np.asarray(self.points['largebottom']) + 2 * (np.cos(t)[:, None] * np.array([1, 0, 0]) + np.sin(t)[:, None] * np.array([0, 1, 0]))
            c.line(c.project(xyz), linestyle=(0, [4, 3]), clip_on=False, id='largebottomrim')
            t = np.radians(np.linspace(180, 360, 121))
            xyz = np.asarray(self.points['largebottom']) + 2 * (np.cos(t)[:, None] * np.array([1, 0, 0]) + np.sin(t)[:, None] * np.array([0, 1, 0]))
            c.line(c.project(xyz), clip_on=False, zorder=3, id='largebottomrim')
            t = np.radians(np.linspace(0, 180, 121))
            xyz = np.asarray(self.points['largetop']) + 2 * (np.cos(t)[:, None] * np.array([1, 0, 0]) + np.sin(t)[:, None] * np.array([0, 1, 0]))
            c.line(c.project(xyz), clip_on=False, zorder=3, id='largetoprim')
            t = np.radians(np.linspace(180, 360, 121))
            xyz = np.asarray(self.points['largetop']) + 2 * (np.cos(t)[:, None] * np.array([1, 0, 0]) + np.sin(t)[:, None] * np.array([0, 1, 0]))
            for object_id, points in [('largetoprim', c.project(xyz)), ('largeleft', c.project([self.points['largeleft0'], self.points['largeleft1']])), ('largeright', c.project([self.points['largeright0'], self.points['largeright1']]))]:
                c.line(points, id=object_id, clip_on=False, zorder=3)
            c.line(c.project([self.points['largefront0'], self.points['largefront1']]), id='largefrontseam', linestyle=(0, [4, 3]), clip_on=False, zorder=3)
            c.line(c.project([self.points['largeback0'], self.points['largeback1']]), id='largebackseam', linestyle=(0, [4, 3]), clip_on=False)
            for object_id, points in [('assembly_arrow0', c.project([self.points['arr0'], self.points['arr1']])), ('assembly_arrow1', c.project([self.points['arr1'], self.points['arr2']])), ('assembly_arrow2', c.project([self.points['arr1'], self.points['arr3']]))]:
                c.line(points, id=object_id, clip_on=False, zorder=3)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Solid96().draw(sys.argv[1] if len(sys.argv) > 1 else None))
