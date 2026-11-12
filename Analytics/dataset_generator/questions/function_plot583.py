"""Frozen question Ana583; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[3]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Ana583:

    def __init__(self):
        self.id = 'Ana583'
        self.source_dataset = 'Author Designed'
        self.source_key = 'author_extensions12_20261111/Ana583'
        self.question = 'The closed polygonal curve C is shown on a unit grid. The horizontal line y=2 meets C at P and Q. Find the length of the chord PQ.'
        self.answer = '9'
        self.answer_type = 'number'
        self.query = self.question
        self.subject = 'Analytics'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'Analytics' / 'dataset_generator/scenes/Ana583.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Analytics' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('Analytics', self.id, variant, output_path)
        with Canvas(ANALYTICS, xlim=[-8, 8], ylim=[-8, 8]) as c:
            c.line([[-5, 2], [-3, 5], [2, 5], [4, 2], [2, -3], [-3, -3], [-5, 2]], id='object_000', solid_capstyle='butt')
            c.text('$C$', [2.6, 5.4])
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Ana583().draw(sys.argv[1] if len(sys.argv) > 1 else None))
