"""Frozen question Plane476; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane476:

    def __init__(self):
        self.id = 'Plane476'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:2706'
        self.question = 'The diagram shows an octagon consisting of $10$ unit squares. The portion below $\\overline{PQ}$ is a unit square and a triangle with base $5$. If $\\overline{PQ}$ bisects the area of the octagon, what is the ratio $\\frac{XQ}{QY}$?\n\nChoices:\nA:$\\frac{2}{5}$\nB:$\\frac{1}{2}$\nC:$\\frac{3}{5}$\nD:$\\frac{2}{3}$\nE:$\\frac{3}{4}$'
        self.answer = 'D'
        self.answer_type = 'choice'
        self.choices = {'A': '$\\frac{2}{5}$', 'B': '$\\frac{1}{2}$', 'C': '$\\frac{3}{5}$', 'D': '$\\frac{2}{3}$', 'E': '$\\frac{3}{4}$'}
        self.query = self.question
        self.points = {'lower00': [0, 0],
         'lower01': [1, 0],
         'lower02': [1, 1],
         'lower03': [0, 1],
         'lower10': [1, 0],
         'lower11': [2, 0],
         'lower12': [2, 1],
         'lower13': [1, 1],
         'lower20': [2, 0],
         'lower21': [3, 0],
         'lower22': [3, 1],
         'lower23': [2, 1],
         'lower30': [3, 0],
         'lower31': [4, 0],
         'lower32': [4, 1],
         'lower33': [3, 1],
         'lower40': [4, 0],
         'lower41': [5, 0],
         'lower42': [5, 1],
         'lower43': [4, 1],
         'lower50': [5, 0],
         'lower51': [6, 0],
         'lower52': [6, 1],
         'lower53': [5, 1],
         'upper10': [1, 1],
         'upper11': [2, 1],
         'upper12': [2, 2],
         'upper13': [1, 2],
         'upper20': [2, 1],
         'upper21': [3, 1],
         'upper22': [3, 2],
         'upper23': [2, 2],
         'upper30': [3, 1],
         'upper31': [4, 1],
         'upper32': [4, 2],
         'upper33': [3, 2],
         'upper40': [4, 1],
         'upper41': [5, 1],
         'upper42': [5, 2],
         'upper43': [4, 2],
         'd00': [0, 0],
         'd01': [0, 1],
         'd10': [1, 0],
         'd11': [1, 1],
         'd12': [1, 2],
         'd20': [2, 0],
         'd21': [2, 1],
         'd22': [2, 2],
         'd30': [3, 0],
         'd31': [3, 1],
         'd32': [3, 2],
         'd40': [4, 0],
         'd41': [4, 1],
         'd42': [4, 2],
         'd50': [5, 0],
         'd51': [5, 1],
         'd52': [5, 2],
         'd60': [6, 0],
         'd61': [6, 1],
         'P': [0, 0],
         'X': [5, 2],
         'Y': [5, 1],
         'Q': [5, 1.6]}
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane476.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-0.37406298002810034, 6.20434315721525], ylim=[-2.274451893865774, 4.303954243377577]) as c:
            for object_id, vertices, codes in [('lower0', [self.points['lower00'], self.points['lower01'], self.points['lower02'], self.points['lower03'], self.points['lower00']], [1, 2, 2, 2, 79]), ('lower1', [self.points['lower10'], self.points['lower11'], self.points['lower12'], self.points['lower13'], self.points['lower10']], [1, 2, 2, 2, 79]), ('lower2', [self.points['lower20'], self.points['lower21'], self.points['lower22'], self.points['lower23'], self.points['lower20']], [1, 2, 2, 2, 79]), ('lower3', [self.points['lower30'], self.points['lower31'], self.points['lower32'], self.points['lower33'], self.points['lower30']], [1, 2, 2, 2, 79]), ('lower4', [self.points['lower40'], self.points['lower41'], self.points['lower42'], self.points['lower43'], self.points['lower40']], [1, 2, 2, 2, 79]), ('lower5', [self.points['lower50'], self.points['lower51'], self.points['lower52'], self.points['lower53'], self.points['lower50']], [1, 2, 2, 2, 79]), ('upper1', [self.points['upper10'], self.points['upper11'], self.points['upper12'], self.points['upper13'], self.points['upper10']], [1, 2, 2, 2, 79]), ('upper2', [self.points['upper20'], self.points['upper21'], self.points['upper22'], self.points['upper23'], self.points['upper20']], [1, 2, 2, 2, 79]), ('upper3', [self.points['upper30'], self.points['upper31'], self.points['upper32'], self.points['upper33'], self.points['upper30']], [1, 2, 2, 2, 79]), ('upper4', [self.points['upper40'], self.points['upper41'], self.points['upper42'], self.points['upper43'], self.points['upper40']], [1, 2, 2, 2, 79])]:
                c.path(vertices, codes, id=object_id)
            for object_id, points in [('d00', [self.points['d00']]), ('d01', [self.points['d01']]), ('d10', [self.points['d10']]), ('d11', [self.points['d11']]), ('d12', [self.points['d12']]), ('d20', [self.points['d20']]), ('d22', [self.points['d22']]), ('d30', [self.points['d30']]), ('d32', [self.points['d32']]), ('d40', [self.points['d40']]), ('d42', [self.points['d42']]), ('d50', [self.points['d50']]), ('d51', [self.points['d51']]), ('d52', [self.points['d52']]), ('d60', [self.points['d60']]), ('d61', [self.points['d61']])]:
                c.point(points, id=object_id, filled=True)
            c.line([self.points['P'], self.points['Q']], id='PQ')
            c.point([self.points['Q']], filled=True, id='Qdot')
            c.text('P', self.points['P'], offset_pt=[-12, -14], vertex=True, id='nameP')
            c.text('Q', self.points['Q'], offset_pt=[16, 4], vertex=True, id='nameQ')
            c.text('X', self.points['X'], offset_pt=[16, 13], vertex=True, id='nameX')
            c.text('Y', self.points['Y'], offset_pt=[16, 13], vertex=True, id='nameY')
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane476().draw(sys.argv[1] if len(sys.argv) > 1 else None))
