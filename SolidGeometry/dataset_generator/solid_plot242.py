"""Frozen question Solid242; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Solid242:

    def __init__(self):
        self.id = 'Solid242'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:2965'
        self.question = 'The solid shown was formed by cutting a right circular cylinder in half. If the base has a radius of 6 cm and the height is 10 cm, what is the total surface area, in terms of $\\pi$, of the solid?'
        self.answer = '96\\pi+120'
        self.answer_type = 'number'
        self.query = self.question
        self.points = {'B': [0, 0, 0],
         'T': [0, 0, 10],
         'A': [-6, 0, 10],
         'C': [6, 0, 10],
         'a': [-6, 0, 0],
         'c': [6, 0, 0],
         'R': [1.9821025483686363, 5.663150138196105, 10],
         'r': [1.9821025483686363, 5.663150138196105, 0]}
        self.subject = 'SolidGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'SolidGeometry' / 'dataset_generator/scenes/Solid242.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('SolidGeometry', self.id, variant, output_path)
        with Canvas(SOLID, xlim=[-8.181493209080664, 12.478078313279866], ylim=[-5.329752224343463, 15.329819298017068], projection=[[0.35, 1, 0], [-0.8, 0.1, 1]], origin=[0, 0, 0], offset=[0, 0]) as c:
            t = np.radians(np.linspace(0, 180, 721))
            xyz = np.asarray(self.points['T']) + 6 * (np.cos(t)[:, None] * np.array([1, 0, 0]) + np.sin(t)[:, None] * np.array([0, 1, 0]))
            c.line(c.project(xyz), clip_on=False, zorder=3, id='arc_0')
            t = np.radians(np.linspace(0, 180, 721))
            xyz = np.asarray(self.points['B']) + 6 * (np.cos(t)[:, None] * np.array([1, 0, 0]) + np.sin(t)[:, None] * np.array([0, 1, 0]))
            c.line(c.project(xyz), linestyle=(0, [4, 3]), clip_on=False, id='arc_1')
            for object_id, points in [('line_2', c.project([self.points['A'], self.points['C']])), ('line_3', c.project([self.points['a'], self.points['c']])), ('line_4', c.project([self.points['A'], self.points['a']])), ('line_5', c.project([self.points['C'], self.points['c']])), ('line_6', c.project([self.points['R'], self.points['r']]))]:
                c.line(points, id=object_id, clip_on=False, zorder=3)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Solid242().draw(sys.argv[1] if len(sys.argv) > 1 else None))
