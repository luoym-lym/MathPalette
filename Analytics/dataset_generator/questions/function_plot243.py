"""Frozen question Ana243; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[3]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Ana243:

    def __init__(self):
        self.id = 'Ana243'
        self.source_dataset = 'We-Math2.0-Standard'
        self.source_key = 'standard/3870'
        self.question = 'Read the unit grid. Find the inclination of line AB, measured counterclockwise from the positive x-axis in [0°, 180°).'
        self.answer = '135°'
        self.answer_type = 'number'
        self.query = self.question
        self.subject = 'Analytics'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'Analytics' / 'dataset_generator/scenes/Ana243.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Analytics' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('Analytics', self.id, variant, output_path)
        with Canvas(ANALYTICS, xlim=[-8, 8], ylim=[-8, 8], xlabel='x', ylabel='y') as c:
            c.line([[-7.5, 7.5], [7.5, -7.5]], id='object_000', solid_capstyle='butt')
            c.point([[-3, 3]], filled=True, id='object_001')
            c.point([[3, -3]], filled=True, id='object_002')
            c.text('A', [-2.77, 3.37], ha='left', va='bottom')
            c.text('B', [3.23, -2.63], ha='left', va='bottom')
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Ana243().draw(sys.argv[1] if len(sys.argv) > 1 else None))
