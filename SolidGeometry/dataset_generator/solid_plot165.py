"""Frozen question Solid165; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Solid165:

    def __init__(self):
        self.id = 'Solid165'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:1400'
        self.question = 'The diagram shows a cube and four marked angles. What is the sum of those angles?\nChoices:\nA:$315^{\\circ}$\nB:$330^{\\circ}$\nC:$345^{\\circ}$\nD:$360^{\\circ}$\nE:$375^{\\circ}$'
        self.answer = 'B'
        self.answer_type = 'choice'
        self.choices = {'A': '$315^{\\circ}$', 'B': '$330^{\\circ}$', 'C': '$345^{\\circ}$', 'D': '$360^{\\circ}$', 'E': '$375^{\\circ}$'}
        self.query = self.question
        self.points = {'cube000': [0, 0, 0],
         'cube001': [0, 0, 1],
         'cube010': [0, 1, 0],
         'cube011': [0, 1, 1],
         'cube100': [1, 0, 0],
         'cube101': [1, 0, 1],
         'cube110': [1, 1, 0],
         'cube111': [1, 1, 1],
         'P': [0, 0, 0],
         'Q': [0, 1, 1],
         'R': [1, 1, 1],
         'S': [1, 1, 0]}
        self.subject = 'SolidGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'SolidGeometry' / 'dataset_generator/scenes/Solid165.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('SolidGeometry', self.id, variant, output_path)
        with Canvas(SOLID, xlim=[-0.03362196403009343, 1.3856659320533493], ylim=[-0.035665932053349225, 1.3836219640300935], projection=[[1, 0.35, 0], [0, 0.35, 1]], origin=[0, 0, 0], offset=[0, 0]) as c:
            c.line(c.project([self.points['cube000'], self.points['cube100']]), id='cube000_cube100', clip_on=False, zorder=3)
            c.line(c.project([self.points['cube000'], self.points['cube010']]), id='cube000_cube010', linestyle=(0, [4, 3]), clip_on=False)
            for object_id, points in [('cube000_cube001', c.project([self.points['cube000'], self.points['cube001']])), ('cube001_cube101', c.project([self.points['cube001'], self.points['cube101']])), ('cube001_cube011', c.project([self.points['cube001'], self.points['cube011']]))]:
                c.line(points, id=object_id, clip_on=False, zorder=3)
            c.line(c.project([self.points['cube010'], self.points['cube110']]), id='cube010_cube110', linestyle=(0, [4, 3]), clip_on=False)
            c.line(c.project([self.points['cube010'], self.points['cube011']]), id='cube010_cube011', linestyle=(0, [4, 3]), clip_on=False)
            for object_id, points in [('cube011_cube111', c.project([self.points['cube011'], self.points['cube111']])), ('cube100_cube110', c.project([self.points['cube100'], self.points['cube110']])), ('cube100_cube101', c.project([self.points['cube100'], self.points['cube101']])), ('cube101_cube111', c.project([self.points['cube101'], self.points['cube111']])), ('cube110_cube111', c.project([self.points['cube110'], self.points['cube111']])), ('diagPQ', c.project([self.points['P'], self.points['Q']])), ('diagPS', c.project([self.points['P'], self.points['S']]))]:
                c.line(points, id=object_id, clip_on=False, zorder=3)
            t = np.radians(np.linspace(0, 60.00000000000001, 65))
            xyz = np.asarray(self.points['P']) + 0.2 * (np.cos(t)[:, None] * np.array([0.7071067811865475, 0.7071067811865475, 0.0]) + np.sin(t)[:, None] * np.array([-0.4082482904638629, 0.408248290463863, 0.8164965809277259]))
            c.line(c.project(xyz), clip_on=False, zorder=3, id='angleP')
            t = np.radians(np.linspace(0, 90.0, 65))
            xyz = np.asarray(self.points['Q']) + 0.2 * (np.cos(t)[:, None] * np.array([0.0, -0.7071067811865475, -0.7071067811865475]) + np.sin(t)[:, None] * np.array([1.0, 4.329780281177466e-17, 4.329780281177466e-17]))
            c.line(c.project(xyz), clip_on=False, zorder=3, id='angleQ')
            t = np.radians(np.linspace(0, 90.0, 65))
            xyz = np.asarray(self.points['R']) + 0.2 * (np.cos(t)[:, None] * np.array([-1.0, 0.0, 0.0]) + np.sin(t)[:, None] * np.array([6.123233995736766e-17, 0.0, -1.0]))
            c.line(c.project(xyz), clip_on=False, zorder=3, id='angleR')
            t = np.radians(np.linspace(0, 90.0, 65))
            xyz = np.asarray(self.points['S']) + 0.2 * (np.cos(t)[:, None] * np.array([0.0, 0.0, 1.0]) + np.sin(t)[:, None] * np.array([-0.7071067811865475, -0.7071067811865475, -6.123233995736766e-17]))
            c.line(c.project(xyz), clip_on=False, zorder=3, id='angleS')
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Solid165().draw(sys.argv[1] if len(sys.argv) > 1 else None))
