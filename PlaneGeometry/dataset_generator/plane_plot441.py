"""Frozen question Plane441; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane441:

    def __init__(self):
        self.id = 'Plane441'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:2150'
        self.question = 'The $ 8\\times 18$ rectangle $ ABCD$ is cut into two congruent hexagons, as shown, in such a way that the two hexagons can be repositioned without overlap to form a square. What is $ y$?'
        self.answer = '6'
        self.answer_type = 'number'
        self.query = self.question
        self.points = {'A': [0, 0], 'B': [18, 0], 'C': [18, 8], 'D': [0, 8], 'U': [6, 8], 'V': [6, 4], 'W': [12, 4], 'X': [12, 0], 'Y': [9, 4]}
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane441.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-1.289047828263227, 19.25930126349521], ylim=[-6.229153780070223, 14.319195311688212]) as c:
            c.path([self.points['A'], self.points['B'], self.points['C'], self.points['D'], self.points['A']], [1, 2, 2, 2, 79], id='outer')
            for object_id, points in [('cut1', [self.points['U'], self.points['V']]), ('cut2', [self.points['V'], self.points['W']]), ('cut3', [self.points['W'], self.points['X']])]:
                c.line(points, id=object_id)
            c.text('A', self.points['A'], offset_pt=[-13, -13], vertex=True, id='nameA')
            c.text('B', self.points['B'], offset_pt=[13, -13], vertex=True, id='nameB')
            c.text('C', self.points['C'], offset_pt=[13, 13], vertex=True, id='nameC')
            c.text('D', self.points['D'], offset_pt=[-13, 13], vertex=True, id='nameD')
            c.text('y', self.points['Y'], offset_pt=[0, 12], vertex=False, id='y')
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane441().draw(sys.argv[1] if len(sys.argv) > 1 else None))
