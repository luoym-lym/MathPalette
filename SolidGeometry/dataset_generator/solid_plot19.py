"""Frozen question Solid19; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Solid19:

    def __init__(self):
        self.id = 'Solid19'
        self.source_dataset = 'SOLIDGEO'
        self.source_key = '1878'
        self.question = 'As shown in the figure, an ant crawls from point $A$ to point $B$ along the surface of a rectangular prism with length, width, and height of 2, 3, and 1 decimeters, respectively. Find the shortest distance the ant can crawl, in decimeters. Give your answer in radical form.'
        self.answer = '3√2 dm'
        self.answer_type = 'number'
        self.query = self.question
        self.points = {'0': [0.0, 0.0, 0.0],
         '1': [2.0, 0.0, 0.0],
         '2': [0.0, 3.0, 0.0],
         '3': [2.0, 3.0, 0.0],
         '4': [0.0, 0.0, 1.0],
         '5': [2.0, 0.0, 1.0],
         '6': [0.0, 3.0, 1.0],
         '7': [2.0, 3.0, 1.0],
         'textanchor2': [1.0, 0.0, 0.0],
         'textanchor3': [2.0, 1.5, 0.0],
         'textanchor4': [2.0, 0.0, 0.5]}
        self.subject = 'SolidGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'SolidGeometry' / 'dataset_generator/scenes/Solid19.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('SolidGeometry', self.id, variant, output_path)
        with Canvas(SOLID, xlim=[-0.23194934906323006, 3.5532033676053003], ylim=[-0.8792009267934437, 2.9059517898750866], projection=[[1, 0.45, 0], [0, 0.35, 1]], origin=[0, 0, 0], offset=[0, 0]) as c:
            for object_id, points in [('edge0', c.project([self.points['0'], self.points['1']])), ('edge1', c.project([self.points['0'], self.points['4']])), ('edge2', c.project([self.points['1'], self.points['3']])), ('edge3', c.project([self.points['1'], self.points['5']])), ('edge4', c.project([self.points['3'], self.points['7']])), ('edge5', c.project([self.points['4'], self.points['5']])), ('edge6', c.project([self.points['4'], self.points['6']])), ('edge7', c.project([self.points['5'], self.points['7']])), ('edge8', c.project([self.points['6'], self.points['7']]))]:
                c.line(points, id=object_id, clip_on=False, zorder=3)
            c.text('A', c.project(self.points['0']), offset_pt=[-12, -12], vertex=True, id='label0')
            c.text('B', c.project(self.points['7']), offset_pt=[10, 10], vertex=True, id='label1')
            c.text('2', c.project(self.points['textanchor2']), offset_pt=[0, -17], vertex=False, id='label2')
            c.text('3', c.project(self.points['textanchor3']), offset_pt=[12, -10], vertex=False, id='label3')
            c.text('1', c.project(self.points['textanchor4']), offset_pt=[-14, 0], vertex=False, id='label4')
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Solid19().draw(sys.argv[1] if len(sys.argv) > 1 else None))
