"""Frozen question Solid20; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Solid20:

    def __init__(self):
        self.id = 'Solid20'
        self.source_dataset = 'SOLIDGEO'
        self.source_key = '1892'
        self.question = 'As shown in the figure, a cuboid has length 3, width 2, and height 4. Point $B$ lies on an edge, with $BC = 1$. Find the shortest distance an ant can crawl from point $A$ to point $B$ along the surface of the cuboid.'
        self.answer = '5'
        self.answer_type = 'number'
        self.query = self.question
        self.points = {'0': [0.0, 0.0, 0.0],
         '1': [3.0, 0.0, 0.0],
         '2': [0.0, 2.0, 0.0],
         '3': [3.0, 2.0, 0.0],
         '4': [0.0, 0.0, 4.0],
         '5': [3.0, 0.0, 4.0],
         '6': [0.0, 2.0, 4.0],
         '7': [3.0, 2.0, 4.0],
         'B': [2.0, 0.0, 4.0],
         'textanchor3': [1.5, 0.0, 0.0],
         'textanchor4': [3.0, 1.0, 0.0],
         'textanchor5': [3.0, 0.0, 2.0],
         'textanchor6': [2.5, 0.0, 4.0]}
        self.subject = 'SolidGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'SolidGeometry' / 'dataset_generator/scenes/Solid20.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('SolidGeometry', self.id, variant, output_path)
        with Canvas(SOLID, xlim=[-0.542739971411442, 4.623237362197941], ylim=[-0.34404560855749056, 4.821931725051892], projection=[[1, 0.45, 0], [0, 0.35, 1]], origin=[0, 0, 0], offset=[0, 0]) as c:
            for object_id, points in [('edge0', c.project([self.points['0'], self.points['1']])), ('edge1', c.project([self.points['0'], self.points['4']])), ('edge2', c.project([self.points['1'], self.points['3']])), ('edge3', c.project([self.points['1'], self.points['5']])), ('edge4', c.project([self.points['3'], self.points['7']])), ('edge5', c.project([self.points['4'], self.points['5']])), ('edge6', c.project([self.points['4'], self.points['6']])), ('edge7', c.project([self.points['5'], self.points['7']])), ('edge8', c.project([self.points['6'], self.points['7']]))]:
                c.line(points, id=object_id, clip_on=False, zorder=3)
            c.point(c.project([self.points['B']]), filled=True, id='dotB')
            c.text('B', c.project(self.points['B']), offset_pt=[0, 16], vertex=True, id='label0')
            c.text('C', c.project(self.points['5']), offset_pt=[13, -5], vertex=True, id='label1')
            c.text('A', c.project(self.points['3']), offset_pt=[12, -5], vertex=True, id='label2')
            c.text('3', c.project(self.points['textanchor3']), offset_pt=[0, -17], vertex=False, id='label3')
            c.text('2', c.project(self.points['textanchor4']), offset_pt=[12, -9], vertex=False, id='label4')
            c.text('4', c.project(self.points['textanchor5']), offset_pt=[-20, 0], vertex=False, id='label5')
            c.text('1', c.project(self.points['textanchor6']), offset_pt=[0, 15], vertex=False, id='label6')
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Solid20().draw(sys.argv[1] if len(sys.argv) > 1 else None))
