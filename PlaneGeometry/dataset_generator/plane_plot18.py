"""Frozen question Plane18; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane18:

    def __init__(self):
        self.id = 'Plane18'
        self.source_dataset = 'MathVista'
        self.source_key = 'testmini/30'
        self.question = 'As shown in the figure, the two chords AB and CD in the circle intersect at E, ∠D = 35.0, ∠AEC = 105.0, then ∠C = ()\nChoices:\nA: 60°\nB: 70°\nC: 80°\nD: 85°'
        self.answer = 'B'
        self.answer_type = 'choice'
        self.choices = {'A': '60°', 'B': '70°', 'C': '80°', 'D': '85°'}
        self.query = self.question
        self.points = {'O': [0.0, 0.0],
         'A': [3.064177772475912, 2.571150438746157],
         'B': [-3.984778792366982, 0.3486229709906328],
         'C': [-1.3680805733026749, 3.7587704831436337],
         'D': [2.8284271247461894, -2.8284271247461907],
         'E': [0.0033396779489303086, 1.6060718945871442]}
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane18.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-4.511386812220768, 4.2121897075337165], ylim=[-4.292611210049283, 4.4309653097052015]) as c:
            c.circle(self.points['O'], 4, id='o1')
            for object_id, points in [('o2', [self.points['A'], self.points['B']]), ('o3', [self.points['C'], self.points['D']]), ('o4', [self.points['B'], self.points['C']]), ('o5', [self.points['A'], self.points['D']])]:
                c.line(points, id=object_id)
            c.text('A', self.points['A'], offset_pt=[12, 9], vertex=True, id='l1')
            c.text('B', self.points['B'], offset_pt=[-13, -3], vertex=True, id='l2')
            c.text('C', self.points['C'], offset_pt=[-2, 14], vertex=True, id='l3')
            c.text('D', self.points['D'], offset_pt=[10, -10], vertex=True, id='l4')
            c.text('E', self.points['E'], offset_pt=[8, 12], vertex=True, id='l5')
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane18().draw(sys.argv[1] if len(sys.argv) > 1 else None))
