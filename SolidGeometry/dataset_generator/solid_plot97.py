"""Frozen question Solid97; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Solid97:

    def __init__(self):
        self.id = 'Solid97'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:278'
        self.question = 'On a standard die the sum of the numbers on opposite faces is always 7. Two identical standard dice are shown in the figure. How many dots could there be on the non-visible right-hand face (marked with "?")?\nChoices:\nA:only 5\nB:only 2\nC:either 2 or 5\nD:either 1, 2, 3 or 5\nE:either 2,3 or 5'
        self.answer = 'A'
        self.answer_type = 'choice'
        self.choices = {'A': 'only 5', 'B': 'only 2', 'C': 'either 2 or 5', 'D': 'either 1, 2, 3 or 5', 'E': 'either 2,3 or 5'}
        self.query = self.question
        self.subject = 'SolidGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'SolidGeometry' / 'dataset_generator/scenes/Solid97.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('SolidGeometry', self.id, variant, output_path)
        with Canvas(SOLID, xlim=[-0.4851998797849886, 3.110520492979205], ylim=[-1.1004571723507344, 2.4952632004134596], projection=[[1, -0.4, 0], [0, 0.4, 1]], origin=[0, 0, 0], offset=[0, 0]) as c:
            for object_id, points in [('dicee0', c.project([[0.0, 0.0, 0.0], [1.0, 0.0, 0.0]])), ('dicee1', c.project([[0.0, 0.0, 1.0], [1.0, 0.0, 1.0]])), ('dicee2', c.project([[0.0, 1.0, 1.0], [1.0, 1.0, 1.0]])), ('dicee3', c.project([[0.0, 0.0, 0.0], [0.0, 1.0, 0.0]])), ('dicee4', c.project([[0.0, 0.0, 1.0], [0.0, 1.0, 1.0]])), ('dicee5', c.project([[1.0, 0.0, 1.0], [1.0, 1.0, 1.0]])), ('dicee6', c.project([[0.0, 0.0, 0.0], [0.0, 0.0, 1.0]])), ('dicee7', c.project([[0.0, 1.0, 0.0], [0.0, 1.0, 1.0]])), ('dicee8', c.project([[1.0, 0.0, 0.0], [1.0, 0.0, 1.0]])), ('dicee9', c.project([[1.0, 0.0, 0.0], [2.0, 0.0, 0.0]])), ('dicee10', c.project([[1.0, 0.0, 1.0], [2.0, 0.0, 1.0]])), ('dicee11', c.project([[1.0, 1.0, 1.0], [2.0, 1.0, 1.0]])), ('dicee12', c.project([[2.0, 0.0, 1.0], [2.0, 1.0, 1.0]])), ('dicee13', c.project([[2.0, 0.0, 0.0], [2.0, 0.0, 1.0]]))]:
                c.line(points, id=object_id, clip_on=False, zorder=3)
            for object_id, points in [('die0toppip0', c.project([[0.25, 0.75, 1.0]])), ('die0toppip1', c.project([[0.75, 0.25, 1.0]])), ('die0frontpip0', c.project([[0.5, 0.0, 0.5]])), ('die1frontpip0', c.project([[1.25, 0.0, 0.25]])), ('die1frontpip1', c.project([[1.25, 0.0, 0.75]])), ('die1frontpip2', c.project([[1.75, 0.0, 0.25]])), ('die1frontpip3', c.project([[1.75, 0.0, 0.75]]))]:
                c.point(points, id=object_id, filled=True)
            for object_id, points in [('questionarrow0', c.project([[2.1, 0, 0.55], [2.8, 0, 0.55]])), ('questionarrow1', c.project([[2.1, 0, 0.55], [2.25, 0, 0.62]])), ('questionarrow2', c.project([[2.1, 0, 0.55], [2.25, 0, 0.48]]))]:
                c.line(points, id=object_id, clip_on=False, zorder=3)
            for object_id, points in [('die0leftpip0', c.project([[0.0, 0.25, 0.75]])), ('die0leftpip1', c.project([[0.0, 0.5, 0.5]])), ('die0leftpip2', c.project([[0.0, 0.75, 0.25]])), ('die1toppip0', c.project([[1.2, 0.25, 1.0]])), ('die1toppip1', c.project([[1.2, 0.75, 1.0]])), ('die1toppip2', c.project([[1.5, 0.25, 1.0]])), ('die1toppip3', c.project([[1.5, 0.75, 1.0]])), ('die1toppip4', c.project([[1.8, 0.25, 1.0]])), ('die1toppip5', c.project([[1.8, 0.75, 1.0]]))]:
                c.point(points, id=object_id, filled=True)
            c.text('?', c.project([3, 0, 0.55]), offset_pt=[0, 0], vertex=False, id='unknown')
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Solid97().draw(sys.argv[1] if len(sys.argv) > 1 else None))
