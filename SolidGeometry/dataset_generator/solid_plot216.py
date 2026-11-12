"""Frozen question Solid216; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Solid216:

    def __init__(self):
        self.id = 'Solid216'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:2341'
        self.question = 'In the adjoining figure of a rectangular solid, $\\angle DHG=45^\\circ$ and $\\angle FHB=60^\\circ$. Find the cosine of $\\angle BHD$.\n\nChoices:\nA:$\\frac{\\sqrt{3}}{6}$\nB:$\\frac{\\sqrt{2}}{6}$\nC:$\\frac{\\sqrt{6}}{3}$\nD:$\\frac{\\sqrt{6}}{4}$\nE:$\\frac{\\sqrt{6}-\\sqrt{2}}{4}$'
        self.answer = 'D'
        self.answer_type = 'choice'
        self.choices = {'A': '$\\frac{\\sqrt{3}}{6}$',
         'B': '$\\frac{\\sqrt{2}}{6}$',
         'C': '$\\frac{\\sqrt{6}}{3}$',
         'D': '$\\frac{\\sqrt{6}}{4}$',
         'E': '$\\frac{\\sqrt{6}-\\sqrt{2}}{4}$'}
        self.query = self.question
        self.points = {'H': [0, 0, 0],
         'G': [1, 0, 0],
         'F': [0, 0.5773502691896258, 0],
         'E': [1, 0.5773502691896258, 0],
         'C': [0, 0, 1],
         'D': [1, 0, 1],
         'B': [0, 0.5773502691896258, 1],
         'A': [1, 0.5773502691896258, 1]}
        self.subject = 'SolidGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'SolidGeometry' / 'dataset_generator/scenes/Solid216.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('SolidGeometry', self.id, variant, output_path)
        with Canvas(SOLID, xlim=[-1.4922437818877912, 1.3575119155399378], ylim=[-0.22241390199324274, 2.627341795434486], projection=[[-1, 1.5, 0], [0.5, 0.2, 1.8]], origin=[0, 0, 0], offset=[0, 0]) as c:
            for object_id, points in [('line_0', c.project([self.points['H'], self.points['G']])), ('line_1', c.project([self.points['H'], self.points['F']])), ('line_2', c.project([self.points['H'], self.points['C']])), ('line_3', c.project([self.points['G'], self.points['D']])), ('line_4', c.project([self.points['F'], self.points['B']])), ('line_5', c.project([self.points['C'], self.points['D']])), ('line_6', c.project([self.points['C'], self.points['B']])), ('line_7', c.project([self.points['D'], self.points['A']])), ('line_8', c.project([self.points['A'], self.points['B']]))]:
                c.line(points, id=object_id, clip_on=False, zorder=3)
            for object_id, points in [('line_9', c.project([self.points['E'], self.points['G']])), ('line_10', c.project([self.points['E'], self.points['F']])), ('line_11', c.project([self.points['E'], self.points['A']]))]:
                c.line(points, id=object_id, linestyle=(0, [4, 3]), clip_on=False)
            for object_id, points in [('line_12', c.project([self.points['D'], self.points['B']])), ('line_13', c.project([self.points['D'], self.points['H']])), ('line_14', c.project([self.points['H'], self.points['B']]))]:
                c.line(points, id=object_id, clip_on=False, zorder=3)
            t = np.radians(np.linspace(0, 45, 101))
            xyz = np.asarray(self.points['H']) + 0.15 * (np.cos(t)[:, None] * np.array([1.0, 0.0, 0.0]) + np.sin(t)[:, None] * np.array([0.0, 0.0, 1.0]))
            c.line(c.project(xyz), clip_on=False, zorder=3, id='ang45')
            t = np.radians(np.linspace(0, 60, 101))
            xyz = np.asarray(self.points['H']) + 0.17 * (np.cos(t)[:, None] * np.array([0.0, 1.0, 0.0]) + np.sin(t)[:, None] * np.array([0.0, 0.0, 1.0]))
            c.line(c.project(xyz), clip_on=False, zorder=3, id='ang60')
            c.text('A', c.project(self.points['A']), offset_pt=[0, 18], vertex=True, id='label_0')
            c.text('B', c.project(self.points['B']), offset_pt=[18, 0], vertex=True, id='label_1')
            c.text('C', c.project(self.points['C']), offset_pt=[0, 19], vertex=True, id='label_2')
            c.text('D', c.project(self.points['D']), offset_pt=[-18, 0], vertex=True, id='label_3')
            c.text('E', c.project(self.points['E']), offset_pt=[-16, 14], vertex=True, id='label_4')
            c.text('F', c.project(self.points['F']), offset_pt=[18, -10], vertex=True, id='label_5')
            c.text('G', c.project(self.points['G']), offset_pt=[-18, 0], vertex=True, id='label_6')
            c.text('H', c.project(self.points['H']), offset_pt=[0, -23], vertex=True, id='label_7')
            c.text('45°', c.project(self.points['H']), offset_pt=[-50, 55], vertex=False, id='label_8')
            c.text('60°', c.project(self.points['H']), offset_pt=[55, 40], vertex=False, id='label_9')
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Solid216().draw(sys.argv[1] if len(sys.argv) > 1 else None))
