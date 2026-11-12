"""Frozen question Plane450; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane450:

    def __init__(self):
        self.id = 'Plane450'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:2453'
        self.question = 'Several figures can be made by attaching two equilateral triangles to the regular pentagon $ ABCDE$ in two of the five positions shown. How many non-congruent figures can be constructed in this way?'
        self.answer = '2'
        self.answer_type = 'number'
        self.query = self.question
        self.points = {'A': [0.5877852522924731, -0.8090169943749475],
         'B': [-0.587785252292473, -0.8090169943749475],
         'C': [-0.9510565162951535, 0.3090169943749475],
         'D': [6.123233995736766e-17, 1.0],
         'E': [0.9510565162951535, 0.3090169943749474],
         'tipA': [5.551115123125783e-17, -1.8270909152852017],
         'tipB': [-1.7376667208456675, -0.5646021430912047],
         'tipC': [-1.073937094602198, 1.4781476007338057],
         'tipD': [1.073937094602198, 1.4781476007338055],
         'tipE': [1.7376667208456675, -0.5646021430912047]}
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane450.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-1.8235998292828883, 1.8235998292828883], ylim=[-1.9980535643478374, 1.6491460942179392]) as c:
            c.path([self.points['A'], self.points['B'], self.points['C'], self.points['D'], self.points['E'], self.points['A']], [1, 2, 2, 2, 2, 79], id='pentagon')
            for object_id, points in [('dashA0', [self.points['A'], self.points['tipA']]), ('dashA1', [self.points['B'], self.points['tipA']]), ('dashB0', [self.points['B'], self.points['tipB']]), ('dashB1', [self.points['C'], self.points['tipB']]), ('dashC0', [self.points['C'], self.points['tipC']]), ('dashC1', [self.points['D'], self.points['tipC']]), ('dashD0', [self.points['D'], self.points['tipD']]), ('dashD1', [self.points['E'], self.points['tipD']]), ('dashE0', [self.points['E'], self.points['tipE']]), ('dashE1', [self.points['A'], self.points['tipE']])]:
                c.line(points, id=object_id, linestyle=(0, [4, 3]))
            c.text('A', self.points['A'], offset_pt=[9.40456403667957, -12.94427190999916], vertex=True, id='nameA')
            c.text('B', self.points['B'], offset_pt=[-9.404564036679568, -12.94427190999916], vertex=True, id='nameB')
            c.text('C', self.points['C'], offset_pt=[-15.216904260722456, 4.94427190999916], vertex=True, id='nameC')
            c.text('D', self.points['D'], offset_pt=[9.797174393178826e-16, 16.0], vertex=True, id='nameD')
            c.text('E', self.points['E'], offset_pt=[15.216904260722456, 4.944271909999158], vertex=True, id='nameE')
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane450().draw(sys.argv[1] if len(sys.argv) > 1 else None))
