"""Frozen question Ana562; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[3]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Ana562:

    def __init__(self):
        self.id = 'Ana562'
        self.source_dataset = 'Author Designed'
        self.source_key = 'author_special20_20261111/Ana562'
        self.question = 'Read A, B and P from the unit grid. Among all points X on the closed segment AB whose two coordinates are integers, find the coordinates of the unique point minimizing the Euclidean distance PX.'
        self.answer = '(3, 2)'
        self.answer_type = 'expression'
        self.query = self.question
        self.subject = 'Analytics'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'Analytics' / 'dataset_generator/scenes/Ana562.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Analytics' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('Analytics', self.id, variant, output_path)
        with Canvas(ANALYTICS, xlim=[-8, 8], ylim=[-8, 8]) as c:
            c.line([[-3, -2], [6, 4]], id='object_000', solid_capstyle='butt')
            c.point([[-3, -2], [6, 4], [1, 3]], filled=True, id='object_001')
            for object_id, text, anchor in [(None, 'A', [-3.4, -2.5]), (None, 'B', [6.4, 4.4]), (None, 'P', [0.5, 3.5])]:
                c.text(text, anchor, id=object_id)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Ana562().draw(sys.argv[1] if len(sys.argv) > 1 else None))
