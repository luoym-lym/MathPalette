"""Frozen question Solid107; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Solid107:

    def __init__(self):
        self.id = 'Solid107'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:387'
        self.question = 'In a three-sided pyramid all side lengths are integers. Four of the side lengths can be seen in the diagram. What is the sum of the two remaining side lengths?'
        self.answer = '11'
        self.answer_type = 'number'
        self.query = self.question
        self.points = {'A': [0, 0, 0], 'B': [2, 0, 0], 'C': [3.25, 3.799671038392666, 0.0], 'D': [4.25, 4.918188919824273, 2.5978679236862194]}
        self.subject = 'SolidGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'SolidGeometry' / 'dataset_generator/scenes/Solid107.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('SolidGeometry', self.id, variant, output_path)
        with Canvas(SOLID, xlim=[-0.5671152833794044, 3.3671152833794045], ylim=[-0.24096622624224362, 3.6932643405165653], projection=[[1.0, -0.11843130509275848, -0.949829837396501], [0.0, 0.6842697627581598, 0.09031715295945672]], origin=[0, 0, 0], offset=[0, 0]) as c:
            for object_id, points in [('AB', c.project([self.points['A'], self.points['B']])), ('AD', c.project([self.points['A'], self.points['D']])), ('DC', c.project([self.points['D'], self.points['C']])), ('CB', c.project([self.points['C'], self.points['B']])), ('DB', c.project([self.points['D'], self.points['B']]))]:
                c.line(points, id=object_id, clip_on=False, zorder=3)
            c.line(c.project([self.points['A'], self.points['C']]), id='AC', linestyle=(0, [4, 3]), clip_on=False)
            c.text('2', c.project([1.0, 0.0, 0.0]), offset_pt=[0, -15], vertex=False, id='labelAB')
            c.text('7', c.project([2.125, 2.4590944599121367, 1.2989339618431097]), offset_pt=[-20, 0], vertex=False, id='labelAD')
            c.text('3', c.project([3.75, 4.35892997910847, 1.2989339618431097]), offset_pt=[10, 17], vertex=False, id='labelDC')
            c.text('4', c.project([2.625, 1.899835519196333, 0.0]), offset_pt=[22, 0], vertex=False, id='labelBC')
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Solid107().draw(sys.argv[1] if len(sys.argv) > 1 else None))
