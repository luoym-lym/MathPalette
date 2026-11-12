"""Frozen question Solid24; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Solid24:

    def __init__(self):
        self.id = 'Solid24'
        self.source_dataset = 'SOLIDGEO'
        self.source_key = '2072'
        self.question = 'Two cubes with equal edge lengths are placed as shown in the figure. Each face is labeled with a number, and the numbers on opposite faces of each cube sum to 10. Find the sum of the numbers on all faces that are not visible in the figure.'
        self.answer = '50'
        self.answer_type = 'number'
        self.query = self.question
        self.points = {'p0': [0.0, 0.0, 0.0],
         'p0b': [1.0, 0.0, 0.0],
         'p2': [0.0, 0.0, 0.0],
         'p2b': [0.0, 0.0, 1.0],
         'p4': [1.0, 0.0, 0.0],
         'p4b': [1.0, 0.0, 0.35],
         'p6': [1.0, 0.0, 0.35],
         'p6b': [1.0, 0.0, 1.0],
         'p8': [0.0, 0.0, 1.0],
         'p8b': [0.45, 0.0, 1.0],
         'p10': [0.45, 0.0, 1.0],
         'p10b': [1.0, 0.0, 1.0],
         'p12': [0.0, 0.0, 1.0],
         'p12b': [0.0, 1.0, 1.0],
         'p14': [1.0, 0.0, 1.0],
         'p14b': [1.0, 1.0, 1.0],
         'p16': [0.0, 1.0, 1.0],
         'p16b': [1.0, 1.0, 1.0],
         'p18': [1.0, 0.0, 0.0],
         'p18b': [2.0, 0.0, 0.0],
         'p20': [2.0, 0.0, 0.0],
         'p20b': [2.0, 1.0, 0.0],
         'p22': [2.0, 0.0, 0.0],
         'p22b': [2.0, 0.0, 0.35],
         'p24': [2.0, 0.0, 0.35],
         'p24b': [2.0, 0.0, 1.0],
         'p26': [2.0, 1.0, 0.0],
         'p26b': [2.0, 1.0, 1.0],
         'p28': [1.0, 0.0, 1.0],
         'p28b': [1.45, 0.0, 1.0],
         'p30': [1.45, 0.0, 1.0],
         'p30b': [2.0, 0.0, 1.0],
         'p32': [2.0, 0.0, 1.0],
         'p32b': [2.0, 1.0, 1.0],
         'p34': [1.0, 1.0, 1.0],
         'p34b': [2.0, 1.0, 1.0],
         'textanchor0': [0.5, 0.5, 1.0],
         'textanchor1': [0.5, 0.0, 0.5],
         'textanchor2': [1.5, 0.5, 1.0],
         'textanchor3': [1.5, 0.0, 0.5],
         'textanchor4': [2.0, 0.5, 0.5]}
        self.subject = 'SolidGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'SolidGeometry' / 'dataset_generator/scenes/Solid24.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('SolidGeometry', self.id, variant, output_path)
        with Canvas(SOLID, xlim=[-0.0638646640826872, 2.520982719638243], ylim=[-0.6209827196382427, 1.9638646640826873], projection=[[1, 0.45, 0], [0, 0.35, 1]], origin=[0, 0, 0], offset=[0, 0]) as c:
            for object_id, points in [('edge0', c.project([self.points['p0'], self.points['p0b']])), ('edge1', c.project([self.points['p2'], self.points['p2b']])), ('edge2', c.project([self.points['p4'], self.points['p4b']])), ('edge3', c.project([self.points['p6'], self.points['p6b']])), ('edge4', c.project([self.points['p8'], self.points['p8b']])), ('edge5', c.project([self.points['p10'], self.points['p10b']])), ('edge6', c.project([self.points['p12'], self.points['p12b']])), ('edge7', c.project([self.points['p14'], self.points['p14b']])), ('edge8', c.project([self.points['p16'], self.points['p16b']])), ('edge9', c.project([self.points['p18'], self.points['p18b']])), ('edge10', c.project([self.points['p20'], self.points['p20b']])), ('edge11', c.project([self.points['p22'], self.points['p22b']])), ('edge12', c.project([self.points['p24'], self.points['p24b']])), ('edge13', c.project([self.points['p26'], self.points['p26b']])), ('edge14', c.project([self.points['p28'], self.points['p28b']])), ('edge15', c.project([self.points['p30'], self.points['p30b']])), ('edge16', c.project([self.points['p32'], self.points['p32b']])), ('edge17', c.project([self.points['p34'], self.points['p34b']]))]:
                c.line(points, id=object_id, clip_on=False, zorder=3)
            for object_id, text, anchor in [('label0', '2', c.project(self.points['textanchor0'])), ('label1', '-5', c.project(self.points['textanchor1'])), ('label2', '4', c.project(self.points['textanchor2'])), ('label3', '3', c.project(self.points['textanchor3'])), ('label4', '6', c.project(self.points['textanchor4']))]:
                c.text(text, anchor, id=object_id, offset_pt=[0, 0], vertex=False)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Solid24().draw(sys.argv[1] if len(sys.argv) > 1 else None))
