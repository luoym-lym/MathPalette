"""Frozen question Plane426; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane426:

    def __init__(self):
        self.id = 'Plane426'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:1878'
        self.question = 'In triangle $P Q R$, a point $S$ is chosen on the line segment $Q R$, then a point $T$ is chosen on the line segment $P S$. Considering the nine marked angles, what is the smallest number of different values that these nine angles could take?'
        self.answer = '3'
        self.answer_type = 'number'
        self.query = self.question
        self.points = {'P': [0, 0],
         'Q': [6.2, 0],
         'R': [3.2, 3.6],
         'S': [4.7, 1.8],
         'T': [3.478, 1.332],
         'dot0': [0.49351810117750183, 0.34123288793748036],
         'dot1': [0.5899950976959975, 0.1091136320295975],
         'dot2': [3.196012161073516, 3.3500318077420723],
         'dot3': [4.409712772561456, 1.8757187267856716],
         'dot4': [4.624281273214328, 1.5097127725614563],
         'dot5': [3.777700732440231, 1.3186033222480642],
         'dot6': [3.4646033222480646, 1.0322992675597693],
         'dot7': [5.80671849750435, 0.3087550158212231],
         'dot8': [5.712888325697245, 0.11279280454872036]}
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane426.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-0.36981449888709816, 6.621391466479691], ylim=[-1.6904452859241352, 5.300760679442654]) as c:
            c.path([self.points['P'], self.points['Q'], self.points['R'], self.points['P']], [1, 2, 2, 79], id='triangle')
            c.line([self.points['P'], self.points['S']], id='PS')
            c.line([self.points['T'], self.points['Q']], id='TQ')
            for object_id, points in [('anglemark0', [self.points['dot0']]), ('anglemark1', [self.points['dot1']]), ('anglemark2', [self.points['dot2']]), ('anglemark3', [self.points['dot3']]), ('anglemark4', [self.points['dot4']]), ('anglemark5', [self.points['dot5']]), ('anglemark6', [self.points['dot6']]), ('anglemark7', [self.points['dot7']]), ('anglemark8', [self.points['dot8']])]:
                c.point(points, id=object_id, filled=True)
            c.text('P', self.points['P'], offset_pt=[-10, -15], vertex=True, id='nameP')
            c.text('Q', self.points['Q'], offset_pt=[12, -15], vertex=True, id='nameQ')
            c.text('R', self.points['R'], offset_pt=[0, 15], vertex=True, id='nameR')
            c.text('S', self.points['S'], offset_pt=[15, 0], vertex=True, id='nameS')
            c.text('T', self.points['T'], offset_pt=[-10, 12], vertex=True, id='nameT')
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane426().draw(sys.argv[1] if len(sys.argv) > 1 else None))
