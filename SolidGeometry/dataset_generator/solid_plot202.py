"""Frozen question Solid202; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Solid202:

    def __init__(self):
        self.id = 'Solid202'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:1917'
        self.question = 'The picture shows a cube with four marked angles, $\\angle W X Y$, $\\angle X Y Z, \\angle Y Z W$ and $\\angle Z W X$. What is the sum of these angles?\nChoices:\nA:$315^{\\circ}$\nB:$330^{\\circ}$\nC:$345^{\\circ}$\nD:$360^{\\circ}$\nE:$375^{\\circ}$'
        self.answer = 'B'
        self.answer_type = 'choice'
        self.choices = {'A': '$315^{\\circ}$', 'B': '$330^{\\circ}$', 'C': '$345^{\\circ}$', 'D': '$360^{\\circ}$', 'E': '$375^{\\circ}$'}
        self.query = self.question
        self.points = {'p000': [0, 0, 0],
         'p001': [0, 0, 1],
         'p010': [0, 1, 0],
         'p011': [0, 1, 1],
         'p100': [1, 0, 0],
         'p101': [1, 0, 1],
         'p110': [1, 1, 0],
         'p111': [1, 1, 1],
         'W': [0, 0, 0],
         'X': [1, 1, 0],
         'Y': [1, 1, 1],
         'Z': [0, 1, 1]}
        self.subject = 'SolidGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'SolidGeometry' / 'dataset_generator/scenes/Solid202.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('SolidGeometry', self.id, variant, output_path)
        with Canvas(SOLID, xlim=[-0.1072029816224731, 1.459508004808125], ylim=[-0.0956265404082497, 1.4710844460223484], projection=[[1, 0.35, 0], [0, 0.35, 1]], origin=[0, 0, 0], offset=[0, 0]) as c:
            c.line(c.project([self.points['p000'], self.points['p100']]), id='line_0', clip_on=False, zorder=3)
            c.line(c.project([self.points['p000'], self.points['p010']]), id='line_1', linestyle=(0, [4, 3]), clip_on=False)
            for object_id, points in [('line_2', c.project([self.points['p000'], self.points['p001']])), ('line_3', c.project([self.points['p001'], self.points['p101']])), ('line_4', c.project([self.points['p001'], self.points['p011']]))]:
                c.line(points, id=object_id, clip_on=False, zorder=3)
            c.line(c.project([self.points['p010'], self.points['p110']]), id='line_5', linestyle=(0, [4, 3]), clip_on=False)
            c.line(c.project([self.points['p010'], self.points['p011']]), id='line_6', linestyle=(0, [4, 3]), clip_on=False)
            for object_id, points in [('line_7', c.project([self.points['p011'], self.points['p111']])), ('line_8', c.project([self.points['p100'], self.points['p110']])), ('line_9', c.project([self.points['p100'], self.points['p101']])), ('line_10', c.project([self.points['p101'], self.points['p111']])), ('line_11', c.project([self.points['p110'], self.points['p111']])), ('line_12', c.project([self.points['W'], self.points['X']])), ('line_13', c.project([self.points['W'], self.points['Z']]))]:
                c.line(points, id=object_id, clip_on=False, zorder=3)
            t = np.radians(np.linspace(0, 90.0, 100))
            xyz = np.asarray(self.points['X']) + 0.1 * (np.cos(t)[:, None] * np.array([-0.7071067811865475, -0.7071067811865475, 0.0]) + np.sin(t)[:, None] * np.array([0.0, 0.0, 1.0]))
            c.line(c.project(xyz), clip_on=False, zorder=3, id='angle14')
            t = np.radians(np.linspace(0, 90.0, 100))
            xyz = np.asarray(self.points['Y']) + 0.1 * (np.cos(t)[:, None] * np.array([0.0, 0.0, -1.0]) + np.sin(t)[:, None] * np.array([-1.0, 0.0, 0.0]))
            c.line(c.project(xyz), clip_on=False, zorder=3, id='angle15')
            t = np.radians(np.linspace(0, 90.0, 100))
            xyz = np.asarray(self.points['Z']) + 0.1 * (np.cos(t)[:, None] * np.array([1.0, 0.0, 0.0]) + np.sin(t)[:, None] * np.array([0.0, -0.7071067811865476, -0.7071067811865476]))
            c.line(c.project(xyz), clip_on=False, zorder=3, id='angle16')
            t = np.radians(np.linspace(0, 60.00000000000001, 100))
            xyz = np.asarray(self.points['W']) + 0.1 * (np.cos(t)[:, None] * np.array([0.0, 0.7071067811865475, 0.7071067811865475]) + np.sin(t)[:, None] * np.array([0.8164965809277261, 0.40824829046386313, -0.408248290463863]))
            c.line(c.project(xyz), clip_on=False, zorder=3, id='angle17')
            c.text('W', c.project(self.points['W']), offset_pt=[-16, -14], vertex=True, id='label_0')
            c.text('X', c.project(self.points['X']), offset_pt=[16, 0], vertex=True, id='label_1')
            c.text('Y', c.project(self.points['Y']), offset_pt=[16, 14], vertex=True, id='label_2')
            c.text('Z', c.project(self.points['Z']), offset_pt=[-2, 19], vertex=True, id='label_3')
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Solid202().draw(sys.argv[1] if len(sys.argv) > 1 else None))
