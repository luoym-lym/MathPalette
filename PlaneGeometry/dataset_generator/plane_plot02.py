"""Frozen question Plane02; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane02:

    def __init__(self):
        self.id = 'Plane02'
        self.source_dataset = 'MathVerse'
        self.source_key = 's209'
        self.question = 'It is known that BC parallel PQ, AB:AP = 2.0:5.0, then the length of CQ is ()\nChoices:\nA:8cm\nB:12cm\nC:30cm\nD:50cm'
        self.answer = 'B'
        self.answer_type = 'choice'
        self.choices = {'A': '8cm', 'B': '12cm', 'C': '30cm', 'D': '50cm'}
        self.query = self.question
        self.points = {'A': [0, 17.3205080757],
         'P': [-10, 0],
         'Q': [10, 0],
         'B': [-4, 10.3923048454],
         'C': [4, 10.3923048454],
         'aqm': [5, 8.66025403785],
         'aq1': [10.9, 0.52],
         'aq2': [0.9, 17.84],
         'aqdim_mid': [5.9, 9.18],
         'P_extension': [-10.7, -1.2124355653],
         'Q_extension': [10.7, -1.2124355653]}
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane02.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-11.31325316834279, 11.457544132938683], ylim=[-3.5915734191592565, 19.179223882122216]) as c:
            for object_id, points in [('AP', [self.points['A'], self.points['P']]), ('AQ', [self.points['A'], self.points['Q']]), ('AP_extension_beyond_P', [self.points['P'], self.points['P_extension']]), ('AQ_extension_beyond_Q', [self.points['Q'], self.points['Q_extension']]), ('BC', [self.points['B'], self.points['C']]), ('PQ', [self.points['P'], self.points['Q']])]:
                c.line(points, id=object_id)
            c.line([self.points['aq1'], self.points['aq2']], id='AQ_dimension', linestyle=(0, [4, 3]))
            c.line([self.points['aq1'], self.points['Q']], id='AQ_tick_top')
            c.line([self.points['aq2'], self.points['A']], id='AQ_tick_bottom')
            c.text('A', self.points['A'], offset_pt=[0.0, 15.0], vertex=True, id='label_A')
            c.text('B', self.points['B'], offset_pt=[-15.0, 9.0], vertex=True, id='label_B')
            c.text('C', self.points['C'], offset_pt=[0, -24], vertex=True, id='label_C')
            c.text('P', self.points['P'], offset_pt=[-24, -12], vertex=True, id='label_P')
            c.text('Q', self.points['Q'], offset_pt=[24, -12], vertex=True, id='label_Q')
            c.text('20', self.points['aqdim_mid'], offset_pt=[20, 18], vertex=False, id='AQval')
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane02().draw(sys.argv[1] if len(sys.argv) > 1 else None))
