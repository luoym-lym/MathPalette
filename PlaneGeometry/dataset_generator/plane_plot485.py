"""Frozen question Plane485; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane485:

    def __init__(self):
        self.id = 'Plane485'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:2845'
        self.question = 'What is the maximum number of $T$-shaped polyominos (shown below) that can be placed in a $6 \\times 6$ grid without any overlaps? The blocks can be rotated.'
        self.answer = '8'
        self.answer_type = 'number'
        self.query = self.question
        self.points = {'tile00': [0, 1],
         'tile01': [1, 1],
         'tile02': [1, 2],
         'tile03': [0, 2],
         'tile10': [1, 1],
         'tile11': [2, 1],
         'tile12': [2, 2],
         'tile13': [1, 2],
         'tile20': [2, 1],
         'tile21': [3, 1],
         'tile22': [3, 2],
         'tile23': [2, 2],
         'tile30': [1, 0],
         'tile31': [2, 0],
         'tile32': [2, 1],
         'tile33': [1, 1]}
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane485.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-0.07435006984377468, 3.079344978439784], ylim=[-0.577058547025228, 2.576636501258331]) as c:
            for object_id, vertices, codes in [('tile0', [self.points['tile00'], self.points['tile01'], self.points['tile02'], self.points['tile03'], self.points['tile00']], [1, 2, 2, 2, 79]), ('tile1', [self.points['tile10'], self.points['tile11'], self.points['tile12'], self.points['tile13'], self.points['tile10']], [1, 2, 2, 2, 79]), ('tile2', [self.points['tile20'], self.points['tile21'], self.points['tile22'], self.points['tile23'], self.points['tile20']], [1, 2, 2, 2, 79]), ('tile3', [self.points['tile30'], self.points['tile31'], self.points['tile32'], self.points['tile33'], self.points['tile30']], [1, 2, 2, 2, 79])]:
                c.path(vertices, codes, id=object_id)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane485().draw(sys.argv[1] if len(sys.argv) > 1 else None))
