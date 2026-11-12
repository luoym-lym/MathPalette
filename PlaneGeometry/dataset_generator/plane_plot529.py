"""Frozen question Plane529; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane529:

    def __init__(self):
        self.id = 'Plane529'
        self.source_dataset = 'Author Designed'
        self.source_key = 'author-expand24:Plane385/extension_03'
        self.question = 'The diagram shows a truncated diamond of 12 dots, in centered rows of 3, 5, 3, and 1 from top to bottom on a square lattice. How many different squares can be drawn by joining the shown dots with line segments? Every vertex must be one of the shown dots; count squares of every size and orientation.'
        self.answer = '9'
        self.answer_type = 'number'
        self.query = self.question
        self.points = {'P02': [0, 2],
         'P11': [1, 1],
         'P12': [1, 2],
         'P13': [1, 3],
         'P20': [2, 0],
         'P21': [2, 1],
         'P22': [2, 2],
         'P23': [2, 3],
         'P31': [3, 1],
         'P32': [3, 2],
         'P33': [3, 3],
         'P42': [4, 2]}
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane529.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-0.11764705882352944, 4.117647058823529], ylim=[-0.6176470588235294, 3.6176470588235294]) as c:
            for object_id, points in [('dotP02', [self.points['P02']]), ('dotP11', [self.points['P11']]), ('dotP12', [self.points['P12']]), ('dotP13', [self.points['P13']]), ('dotP20', [self.points['P20']]), ('dotP21', [self.points['P21']]), ('dotP22', [self.points['P22']]), ('dotP23', [self.points['P23']]), ('dotP31', [self.points['P31']]), ('dotP32', [self.points['P32']]), ('dotP33', [self.points['P33']]), ('dotP42', [self.points['P42']])]:
                c.point(points, id=object_id, filled=True)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane529().draw(sys.argv[1] if len(sys.argv) > 1 else None))
