"""Frozen question Solid291; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Solid291:

    def __init__(self):
        self.id = 'Solid291'
        self.source_dataset = 'We-Math2.0-Standard'
        self.source_key = 'standard/5415'
        self.question = 'The figure is an oblique drawing of a cube; the named points are vertices. Vectors AB and AC are normal vectors of two planes. Find the cosine of the smaller angle between the planes.'
        self.answer = '1/2'
        self.answer_type = 'number'
        self.query = self.question
        self.points = {'v000': [0, 0, 0],
         'v001': [0, 0, 4],
         'v010': [0, 4, 0],
         'v011': [0, 4, 4],
         'v100': [4, 0, 0],
         'v101': [4, 0, 4],
         'v110': [4, 4, 0],
         'v111': [4, 4, 4],
         'A': [0, 0, 0],
         'B': [4, 4, 0],
         'C': [0, 4, 4]}
        self.subject = 'SolidGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'SolidGeometry' / 'dataset_generator/scenes/Solid291.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('SolidGeometry', self.id, variant, output_path)
        with Canvas(SOLID, xlim=[-0.4094781999452133, 6.022402342750617], ylim=[-0.5836299143344066, 5.8482506283614235], projection=[[1, 0.4, 0], [0, 0.3, 1]], origin=[0, 0, 0], offset=[0, 0]) as c:
            c.line(c.project([self.points['v000'], self.points['v001']]), id='edge0', clip_on=False, zorder=3)
            c.line(c.project([self.points['v000'], self.points['v010']]), id='edge1', linestyle=(0, [4, 3]), clip_on=False)
            for object_id, points in [('edge2', c.project([self.points['v000'], self.points['v100']])), ('edge3', c.project([self.points['v001'], self.points['v011']])), ('edge4', c.project([self.points['v001'], self.points['v101']]))]:
                c.line(points, id=object_id, clip_on=False, zorder=3)
            c.line(c.project([self.points['v010'], self.points['v011']]), id='edge5', linestyle=(0, [4, 3]), clip_on=False)
            c.line(c.project([self.points['v010'], self.points['v110']]), id='edge6', linestyle=(0, [4, 3]), clip_on=False)
            for object_id, points in [('edge7', c.project([self.points['v011'], self.points['v111']])), ('edge8', c.project([self.points['v100'], self.points['v101']])), ('edge9', c.project([self.points['v100'], self.points['v110']])), ('edge10', c.project([self.points['v101'], self.points['v111']])), ('edge11', c.project([self.points['v110'], self.points['v111']]))]:
                c.line(points, id=object_id, clip_on=False, zorder=3)
            c.text('A', c.project(self.points['A']), offset_pt=[-14, -12], vertex=True, id='labelA')
            c.text('B', c.project(self.points['B']), offset_pt=[15, -5], vertex=True, id='labelB')
            c.text('C', c.project(self.points['C']), offset_pt=[0, 17], vertex=True, id='labelC')
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Solid291().draw(sys.argv[1] if len(sys.argv) > 1 else None))
