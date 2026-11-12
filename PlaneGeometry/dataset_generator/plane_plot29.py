"""Frozen question Plane29; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane29:

    def __init__(self):
        self.id = 'Plane29'
        self.source_dataset = 'MathVista'
        self.source_key = 'testmini/234'
        self.question = 'In the figure shown above, AC = 6. What is the length of segment AB?\nChoices:\nA: 3\nB: 5\nC: 6\nD: 7\nE: It cannot be determined from the information given'
        self.answer = 'C'
        self.answer_type = 'choice'
        self.choices = {'A': '3', 'B': '5', 'C': '6', 'D': '7', 'E': 'It cannot be determined from the information given'}
        self.query = self.question
        self.points = {'A': [0.0, 0.0], 'C': [6.0, 0.0], 'B': [3.0, 5.196152422706632]}
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane29.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-0.37877084051291154, 6.37279749116429], ylim=[-0.7243938243577013, 6.027174507319501]) as c:
            c.path([self.points['A'], self.points['B'], self.points['C'], self.points['A']], [1, 2, 2, 79], id='o1')
            center, direction, start, end = self._angle(self.points['B'], self.points['A'], self.points['C'], reflex=False)
            c.arc(center, 16, start, end, radius_pt=True, id='o2')
            center, direction, start, end = self._angle(self.points['A'], self.points['B'], self.points['C'], reflex=False)
            c.arc(center, 16, start, end, radius_pt=True, id='o3')
            c.text('A', self.points['A'], offset_pt=[-10, -10], vertex=True, id='l1')
            c.text('C', self.points['C'], offset_pt=[10, -10], vertex=True, id='l2')
            c.text('B', self.points['B'], offset_pt=[0, 15], vertex=True, id='l3')
            center, direction, start, end = self._angle(self.points['B'], self.points['A'], self.points['C'], reflex=False)
            offset = direction * 40 + np.array([0, 0])
            c.text('60°', center, offset_pt=offset, id='l4')
            center, direction, start, end = self._angle(self.points['A'], self.points['B'], self.points['C'], reflex=False)
            offset = direction * 40 + np.array([0, 0])
            c.text('60°', center, offset_pt=offset, id='l5')
            return c if _canvas else c.save(output_path)

    @staticmethod
    def _angle(a, vertex, b, reflex=False):
        center = np.asarray(vertex, dtype=float)
        u, v = (np.asarray(a) - center, np.asarray(b) - center)
        u, v = (u / np.linalg.norm(u), v / np.linalg.norm(v))
        start, end = (np.degrees(np.arctan2(u[1], u[0])), np.degrees(np.arctan2(v[1], v[0])))
        sweep = (end - start) % 360
        if sweep > 180:
            start, sweep = (end, 360 - sweep)
        if reflex:
            start, sweep = (start + sweep, 360 - sweep)
        middle = np.radians(start + sweep / 2)
        return (center, np.array([np.cos(middle), np.sin(middle)]), start, start + sweep)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane29().draw(sys.argv[1] if len(sys.argv) > 1 else None))
