"""Frozen question Ana564; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[3]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Ana564:

    def __init__(self):
        self.id = 'Ana564'
        self.source_dataset = 'Author Designed'
        self.source_key = 'author_special20_20261111/Ana564'
        self.question = 'Read the query point Q and sites A, B, C from the unit grid. Define d_1((x,y),(u,v))=|x-u|+|y-v|. Which site uniquely minimizes d_1(Q,site)? Answer with its letter.'
        self.answer = 'B'
        self.answer_type = 'text'
        self.query = self.question
        self.subject = 'Analytics'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'Analytics' / 'dataset_generator/scenes/Ana564.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Analytics' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('Analytics', self.id, variant, output_path)
        with Canvas(ANALYTICS, xlim=[-8, 8], ylim=[-8, 8]) as c:
            c.point([[-1, -1], [2, 2], [-1, 4], [-6, -3]], filled=True, id='object_000')
            for object_id, text, anchor in [(None, 'Q', [-1.5, -1.5]), (None, 'A', [2.4, 2.4]), (None, 'B', [-1.5, 4.5]), (None, 'C', [-6.4, -3.5])]:
                c.text(text, anchor, id=object_id)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Ana564().draw(sys.argv[1] if len(sys.argv) > 1 else None))
