"""Frozen question Plane524; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane524:

    def __init__(self):
        self.id = 'Plane524'
        self.source_dataset = 'Author Designed'
        self.source_key = 'author-expand24:Plane363/extension_01'
        self.question = 'The diagram consists of all 12 points in a rectangular array of 4 columns and 3 rows, with equal spacing horizontally and vertically. What is the minimum number of points that must be removed so that no three of the remaining points lie on one straight line?'
        self.answer = '6'
        self.answer_type = 'number'
        self.query = self.question
        self.points = {'P00': [0, 0],
         'P01': [0, 1],
         'P02': [0, 2],
         'P10': [1, 0],
         'P11': [1, 1],
         'P12': [1, 2],
         'P20': [2, 0],
         'P21': [2, 1],
         'P22': [2, 2],
         'P30': [3, 0],
         'P31': [3, 1],
         'P32': [3, 2]}
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane524.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-0.09262672811059947, 3.0926267281105995], ylim=[-0.5926267281105995, 2.5926267281105995]) as c:
            for object_id, points in [('dotP00', [self.points['P00']]), ('dotP01', [self.points['P01']]), ('dotP02', [self.points['P02']]), ('dotP10', [self.points['P10']]), ('dotP11', [self.points['P11']]), ('dotP12', [self.points['P12']]), ('dotP20', [self.points['P20']]), ('dotP21', [self.points['P21']]), ('dotP22', [self.points['P22']]), ('dotP30', [self.points['P30']]), ('dotP31', [self.points['P31']]), ('dotP32', [self.points['P32']])]:
                c.point(points, id=object_id, filled=True)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane524().draw(sys.argv[1] if len(sys.argv) > 1 else None))
