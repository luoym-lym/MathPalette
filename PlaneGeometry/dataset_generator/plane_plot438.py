"""Frozen question Plane438; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane438:

    def __init__(self):
        self.id = 'Plane438'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:2060'
        self.question = 'The two squares shown share the same center $O$ and have sides of length 1. The length of $\\overline{AB}$ is $43/99$ and the area of octagon $ABCDEFGH$ is $m/n,$ where $m$ and $n$ are relatively prime positive integers.  Find $m+n$.'
        self.answer = '185'
        self.answer_type = 'number'
        self.query = self.question
        self.points = {'A': [-0.09744172130172023, 0.5],
         'B': [0.33690171304171407, 0.5],
         'C': [0.5, 0.09744172130172023],
         'D': [0.5, -0.33690171304171407],
         'E': [0.09744172130172023, -0.5],
         'F': [-0.33690171304171407, -0.5],
         'G': [-0.5, -0.09744172130172023],
         'H': [-0.5, 0.33690171304171407],
         'O': [0, 0]}
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane438.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-0.683134462189062, 0.683134462189062], ylim=[-0.683134462189062, 0.683134462189062]) as c:
            c.path([[-0.5, -0.5], [0.5, -0.5], [0.5, 0.5], [-0.5, 0.5], [-0.5, -0.5]], [1, 2, 2, 2, 79], id='o0')
            c.path([[-0.2756574323518534, -0.6511627906976745], [0.6511627906976745, -0.2756574323518534], [0.2756574323518534, 0.6511627906976745], [-0.6511627906976745, 0.2756574323518534], [-0.2756574323518534, -0.6511627906976745]], [1, 2, 2, 2, 79], id='o1')
            c.point([self.points['O']], filled=True, id='o2')
            c.text('A', self.points['A'], offset_pt=[0, 15], vertex=True, id='lA')
            c.text('B', self.points['B'], offset_pt=[7, 16], vertex=True, id='lB')
            c.text('C', self.points['C'], offset_pt=[17, 0], vertex=True, id='lC')
            c.text('D', self.points['D'], offset_pt=[15, -8], vertex=True, id='lD')
            c.text('E', self.points['E'], offset_pt=[2, -18], vertex=True, id='lE')
            c.text('F', self.points['F'], offset_pt=[-7, -18], vertex=True, id='lF')
            c.text('G', self.points['G'], offset_pt=[-17, -4], vertex=True, id='lG')
            c.text('H', self.points['H'], offset_pt=[-17, 5], vertex=True, id='lH')
            c.text('O', self.points['O'], offset_pt=[15, -10], vertex=True, id='lO')
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane438().draw(sys.argv[1] if len(sys.argv) > 1 else None))
