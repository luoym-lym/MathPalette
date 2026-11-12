"""Frozen question Plane67; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane67:

    def __init__(self):
        self.id = 'Plane67'
        self.source_dataset = 'MathVista'
        self.source_key = 'testmini/866'
        self.question = 'For trapezoid $Q R S T, A$ and $B$ are midpoints of the legs. Find $m \\angle S$\nChoices:\nA: 45\nB: 60\nC: 120\nD: 135'
        self.answer = 'D'
        self.answer_type = 'choice'
        self.choices = {'A': '45', 'B': '60', 'C': '120', 'D': '135'}
        self.query = self.question
        self.points = {'Q': [0.0, 0.0],
         'R': [20.0, 0.0],
         'T': [2.9282032302755097, 5.071796769724491],
         'S': [14.928203230275509, 5.071796769724491],
         'A': [1.4641016151377548, 2.5358983848622456],
         'B': [17.464101615137753, 2.5358983848622456],
         'anchor16': [8.928203230275509, 5.071796769724491],
         'anchor18': [10.0, 0.0]}
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane67.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-1.340261720334471, 21.37932422033447], ylim=[-8.742886975476464, 13.976698965192478]) as c:
            for object_id, points in [('segment11', [self.points['Q'], self.points['R']]), ('segment12', [self.points['R'], self.points['S']]), ('segment13', [self.points['S'], self.points['T']]), ('segment14', [self.points['T'], self.points['Q']]), ('segment15', [self.points['A'], self.points['B']])]:
                c.line(points, id=object_id)
            center, direction, start, end = self._angle(self.points['Q'], self.points['T'], self.points['S'], reflex=False)
            c.arc(center, 16, start, end, radius_pt=True, id='angle_arc20')
            center, direction, start, end = self._angle(self.points['Q'], self.points['R'], self.points['S'], reflex=False)
            c.arc(center, 16, start, end, radius_pt=True, id='angle_arc22')
            c.text('Q', self.points['Q'], offset_pt=[-12, -9], vertex=True, id='label1')
            c.text('R', self.points['R'], offset_pt=[14, -9], vertex=True, id='label2')
            c.text('T', self.points['T'], offset_pt=[-5, 15], vertex=True, id='label3')
            c.text('S', self.points['S'], offset_pt=[6, 15], vertex=True, id='label4')
            c.text('A', self.points['A'], offset_pt=[-14, 0], vertex=True, id='label5')
            c.text('B', self.points['B'], offset_pt=[14, 0], vertex=True, id='label8')
            c.text('12', self.points['anchor16'], offset_pt=[0, 15], vertex=False, id='text17')
            c.text('20', self.points['anchor18'], offset_pt=[0, -15], vertex=False, id='text19')
            center, direction, start, end = self._angle(self.points['Q'], self.points['T'], self.points['S'], reflex=False)
            offset = direction * 35 + np.array([0, 0])
            c.text('120°', center, offset_pt=offset, id='anglelabel21')
            center, direction, start, end = self._angle(self.points['Q'], self.points['R'], self.points['S'], reflex=False)
            offset = direction * 38 + np.array([0, 0])
            c.text('45°', center, offset_pt=offset, id='anglelabel23')
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
    print(Plane67().draw(sys.argv[1] if len(sys.argv) > 1 else None))
