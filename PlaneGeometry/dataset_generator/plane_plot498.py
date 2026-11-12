"""Frozen question Plane498; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane498:

    def __init__(self):
        self.id = 'Plane498'
        self.source_dataset = 'Author Designed'
        self.source_key = 'authored-extension:Plane157:ext02'
        self.question = 'The floor of a rectangular room is covered completely with congruent rectangular tiles, as shown. The marked short side of one tile is 3 m. How long is the room in the direction indicated by the question mark? Give the length in metres.\nChoices:\nA:12\nB:15'
        self.answer = 'B'
        self.answer_type = 'choice'
        self.choices = {'A': '12', 'B': '15'}
        self.query = self.question
        self.points = {'P0001': [0, 1],
         'P0002': [1, 1],
         'P0003': [1, 4],
         'P0004': [0, 4],
         'P0005': [2, 1],
         'P0006': [2, 4],
         'P0007': [3, 1],
         'P0008': [3, 4],
         'P0009': [3, 5],
         'P0010': [0, 5],
         'P0011': [3, 0],
         'P0012': [3.6, 0],
         'P0013': [3.6, 5],
         'P0014': [0, 0]}
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane498.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-1.0022065146362111, 4.285460870388693], ylim=[-0.1493653140954483, 5.138302070929456]) as c:
            for object_id, vertices, codes in [('tile_0', [self.points['P0001'], self.points['P0002'], self.points['P0003'], self.points['P0004'], self.points['P0001']], [1, 2, 2, 2, 79]), ('tile_1', [self.points['P0002'], self.points['P0005'], self.points['P0006'], self.points['P0003'], self.points['P0002']], [1, 2, 2, 2, 79]), ('tile_2', [self.points['P0005'], self.points['P0007'], self.points['P0008'], self.points['P0006'], self.points['P0005']], [1, 2, 2, 2, 79]), ('tile_3', [self.points['P0004'], self.points['P0008'], self.points['P0009'], self.points['P0010'], self.points['P0004']], [1, 2, 2, 2, 79])]:
                c.path(vertices, codes, id=object_id)
            c.line([self.points['P0011'], self.points['P0012']], id='dimension_0')
            c.line([self.points['P0009'], self.points['P0013']], id='dimension_1')
            c.line([self.points['P0012'], self.points['P0013']], id='dimension_2', linestyle=(0, [4, 3]))
            c.path([self.points['P0014'], self.points['P0011'], self.points['P0007'], self.points['P0001'], self.points['P0014']], [1, 2, 2, 2, 79], id='tile_4')
            c.text('3 m', [-0.6, 0.5], offset_pt=[0, 0], vertex=False, id='label000')
            c.text('?', [4.0, 2.5], offset_pt=[0, 0], vertex=False, id='label001')
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane498().draw(sys.argv[1] if len(sys.argv) > 1 else None))
