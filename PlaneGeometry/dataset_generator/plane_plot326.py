"""Frozen question Plane326; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane326:

    def __init__(self):
        self.id = 'Plane326'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:1038'
        self.question = 'In the picture there is a square tile with two fourths of a circle. The radius of every fourth is half the side of the tile and its length equals $5 \\mathrm{dm}$. A large square is formed from 16 such tiles. What is the maximum possible length of an unbroken continuous curve consisting of the fourths?\nChoices:\nA:$75 \\mathrm{dm}$\nB:$100 \\mathrm{dm}$\nC:$105 \\mathrm{dm}$\nD:$110 \\mathrm{dm}$\nE:$80 \\mathrm{dm}$'
        self.answer = 'D'
        self.answer_type = 'choice'
        self.choices = {'A': '$75 \\mathrm{dm}$', 'B': '$100 \\mathrm{dm}$', 'C': '$105 \\mathrm{dm}$', 'D': '$110 \\mathrm{dm}$', 'E': '$80 \\mathrm{dm}$'}
        self.query = self.question
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane326.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-0.04970267776152659, 2.0524268469403957], ylim=[-0.053291720352341976, 2.04883780434958]) as c:
            c.path([[0, 0], [2, 0], [2, 2], [0, 2], [0, 0]], [1, 2, 2, 2, 79], id='tile')
            c.arc([0, 0], 1, 0, 90, id='lower_left_quarter')
            c.arc([2, 2], 1, 180, 270, id='upper_right_quarter')
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane326().draw(sys.argv[1] if len(sys.argv) > 1 else None))
