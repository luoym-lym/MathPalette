"""Frozen question Ana101; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[3]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Ana101:

    def __init__(self):
        self.id = 'Ana101'
        self.source_dataset = 'MathVista'
        self.source_key = 'testmini/452'
        self.question = 'The graph shows marked population observations with horizontal coordinate t and vertical coordinate p. To the nearest integer, what is the p-coordinate of the rightmost marked point?\nChoices:\nA: 2\nB: 3\nC: 4\nD: 5'
        self.answer = 'C'
        self.answer_type = 'choice'
        self.choices = {'A': '2', 'B': '3', 'C': '4', 'D': '5'}
        self.query = self.question
        self.subject = 'Analytics'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'Analytics' / 'dataset_generator/scenes/Ana101.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Analytics' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('Analytics', self.id, variant, output_path)
        with Canvas(ANALYTICS, xlim=[-8, 8], ylim=[-8, 8], xlabel='$t$', ylabel='$p$') as c:
            c.point([[0.0, 0.5], [0.6, 1.025], [1.2, 1.525], [1.8, 2.15], [2.4, 2.8], [3.0, 3.375], [3.6, 3.7], [4.2, 3.85], [4.8, 3.94], [5.4, 3.975], [5.8, 3.9799999999999995], [6.2, 3.9899999999999998]], filled=True, id='object_000')
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Ana101().draw(sys.argv[1] if len(sys.argv) > 1 else None))
