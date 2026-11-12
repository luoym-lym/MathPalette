"""Frozen question Plane385; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane385:

    def __init__(self):
        self.id = 'Plane385'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:1552'
        self.question = 'How many different squares can be drawn in total by joining the dots with line segments in the part of the square lattice as shown on the right?'
        self.answer = '4'
        self.answer_type = 'number'
        self.query = self.question
        self.points = {'P01': [0, 1], 'P02': [0, 2], 'P10': [1, 0], 'P11': [1, 1], 'P12': [1, 2], 'P20': [2, 0], 'P21': [2, 1], 'P22': [2, 2]}
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane385.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-0.06345872833283672, 2.066791119596469], ylim=[-0.06679111959646866, 2.063458728332837]) as c:
            for object_id, points in [('dotP01', [self.points['P01']]), ('dotP02', [self.points['P02']]), ('dotP10', [self.points['P10']]), ('dotP11', [self.points['P11']]), ('dotP12', [self.points['P12']]), ('dotP20', [self.points['P20']]), ('dotP21', [self.points['P21']]), ('dotP22', [self.points['P22']])]:
                c.point(points, id=object_id, filled=True)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane385().draw(sys.argv[1] if len(sys.argv) > 1 else None))
