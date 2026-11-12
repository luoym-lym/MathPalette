"""Frozen question Plane458; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane458:

    def __init__(self):
        self.id = 'Plane458'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:2589'
        self.question = 'The horizontal and vertical distances between adjacent points equal $1$ unit.  The area of triangle $ABC$ is\n\nChoices:\nA:1/4\nB:1/2\nC:3/4\nD:1\nE:5/4'
        self.answer = 'B'
        self.answer_type = 'choice'
        self.choices = {'A': '1/4', 'B': '1/2', 'C': '3/4', 'D': '1', 'E': '5/4'}
        self.query = self.question
        self.points = {'p00': [0, 0],
         'p01': [0, 1],
         'p02': [0, 2],
         'p03': [0, 3],
         'p10': [1, 0],
         'p11': [1, 1],
         'p12': [1, 2],
         'p13': [1, 3],
         'p20': [2, 0],
         'p21': [2, 1],
         'p22': [2, 2],
         'p23': [2, 3],
         'p30': [3, 0],
         'p31': [3, 1],
         'p32': [3, 2],
         'p33': [3, 3],
         'p40': [4, 0],
         'p41': [4, 1],
         'p42': [4, 2],
         'p43': [4, 3],
         'A': [0, 0],
         'B': [3, 2],
         'C': [4, 3]}
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane458.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-0.28628250514176745, 4.272972319956582], ylim=[-0.762959818437829, 3.7962950066605208]) as c:
            for object_id, points in [('p00', [self.points['p00']]), ('p01', [self.points['p01']]), ('p02', [self.points['p02']]), ('p03', [self.points['p03']]), ('p10', [self.points['p10']]), ('p11', [self.points['p11']]), ('p12', [self.points['p12']]), ('p13', [self.points['p13']]), ('p20', [self.points['p20']]), ('p21', [self.points['p21']]), ('p22', [self.points['p22']]), ('p23', [self.points['p23']]), ('p30', [self.points['p30']]), ('p31', [self.points['p31']]), ('p32', [self.points['p32']]), ('p33', [self.points['p33']]), ('p40', [self.points['p40']]), ('p41', [self.points['p41']]), ('p42', [self.points['p42']]), ('p43', [self.points['p43']])]:
                c.point(points, id=object_id, filled=True)
            c.path([self.points['p00'], self.points['p32'], self.points['p43'], self.points['p00']], [1, 2, 2, 79], id='triangle')
            c.text('A', self.points['A'], offset_pt=[-13, -13], vertex=True, id='nameA')
            c.text('B', self.points['B'], offset_pt=[14, -13], vertex=True, id='nameB')
            c.text('C', self.points['C'], offset_pt=[12, 14], vertex=True, id='nameC')
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane458().draw(sys.argv[1] if len(sys.argv) > 1 else None))
