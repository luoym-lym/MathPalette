"""Frozen question Solid80; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Solid80:

    def __init__(self):
        self.id = 'Solid80'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:25'
        self.question = 'A wooden block has 8 vertices. One vertex is cut off now (see the picture).\nHow many vertices has the block now?'
        self.answer = '10'
        self.answer_type = 'number'
        self.query = self.question
        self.points = {'p000': [0, 0, 0],
         'p001': [0, 0, 1],
         'p010': [0, 1, 0],
         'p011': [0, 1, 1],
         'p100': [1, 0, 0],
         'p101': [1, 0, 1],
         'p110': [1, 1, 0],
         'p111': [1, 1, 1],
         'U': [0.8, 0, 1],
         'V': [1, 0, 0.8],
         'W': [1, 0.2, 1]}
        self.subject = 'SolidGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'SolidGeometry' / 'dataset_generator/scenes/Solid80.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('SolidGeometry', self.id, variant, output_path)
        with Canvas(SOLID, xlim=[-0.0346527052397656, 1.3846449066699096], ylim=[-0.03464490666990949, 1.3846527052397657], projection=[[1, 0.35, 0], [0, 0.35, 1]], origin=[0, 0, 0], offset=[0, 0]) as c:
            for object_id, points in [('edge0', c.project([self.points['p000'], self.points['p100']])), ('edge1', c.project([self.points['p000'], self.points['p001']])), ('edge2', c.project([self.points['p001'], self.points['p011']])), ('edge3', c.project([self.points['p011'], self.points['p111']])), ('edge4', c.project([self.points['p111'], self.points['p110']])), ('edge5', c.project([self.points['p110'], self.points['p100']])), ('edge6', c.project([self.points['p001'], self.points['U']])), ('edge7', c.project([self.points['V'], self.points['p100']])), ('edge8', c.project([self.points['W'], self.points['p111']])), ('edge9', c.project([self.points['U'], self.points['V']])), ('edge10', c.project([self.points['V'], self.points['W']])), ('edge11', c.project([self.points['W'], self.points['U']]))]:
                c.line(points, id=object_id, clip_on=False, zorder=3)
            for object_id, points in [('removed_U', c.project([self.points['U'], self.points['p101']])), ('removed_V', c.project([self.points['V'], self.points['p101']])), ('removed_W', c.project([self.points['W'], self.points['p101']]))]:
                c.line(points, id=object_id, linestyle=(0, [4, 3]), clip_on=False)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Solid80().draw(sys.argv[1] if len(sys.argv) > 1 else None))
