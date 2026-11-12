"""Frozen question Ana285; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[3]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Ana285:

    def __init__(self):
        self.id = 'Ana285'
        self.source_dataset = 'We-Math2.0-Standard'
        self.source_key = 'standard/5418'
        self.question = 'Read W and Z from the unit grid. Find the slope of WZ as an exact fraction.'
        self.answer = '1/2'
        self.answer_type = 'number'
        self.query = self.question
        self.subject = 'Analytics'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'Analytics' / 'dataset_generator/scenes/Ana285.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Analytics' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('Analytics', self.id, variant, output_path)
        with Canvas(ANALYTICS, xlim=[-8, 8], ylim=[-8, 8], xlabel='x', ylabel='y') as c:
            c.line([[-7.5, -4.75], [7.5, 2.75]], id='object_000', solid_capstyle='butt')
            c.point([[-4, -3]], filled=True, id='object_001')
            c.point([[2, 0]], filled=True, id='object_002')
            c.text('W', [-4.25, -2.63], ha='right', va='bottom')
            c.text('Z', [1.75, 0.37], ha='right', va='bottom')
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Ana285().draw(sys.argv[1] if len(sys.argv) > 1 else None))
