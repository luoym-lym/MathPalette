"""Frozen question Solid192; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Solid192:

    def __init__(self):
        self.id = 'Solid192'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:1833'
        self.question = 'The diagram shows two ordinary dice. What is the total number of spots on all the faces that cannot be seen in the diagram?'
        self.answer = '27'
        self.answer_type = 'number'
        self.query = self.question
        self.subject = 'SolidGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'SolidGeometry' / 'dataset_generator/scenes/Solid192.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('SolidGeometry', self.id, variant, output_path)
        with Canvas(SOLID, xlim=[-0.062262896352024644, 2.566048022321017], ylim=[-0.5660480223210169, 2.0622628963520246], projection=[[1, 0.5, 0], [0, 0.5, 1]], origin=[0, 0, 0], offset=[0, 0]) as c:
            for object_id, points in [('dicee0', c.project([[0.0, 0.0, 0.0], [1.0, 0.0, 0.0]])), ('dicee1', c.project([[0.0, 0.0, 1.0], [1.0, 0.0, 1.0]])), ('dicee2', c.project([[0.0, 1.0, 1.0], [1.0, 1.0, 1.0]])), ('dicee3', c.project([[0.0, 0.0, 1.0], [0.0, 1.0, 1.0]])), ('dicee4', c.project([[1.0, 0.0, 1.0], [1.0, 1.0, 1.0]])), ('dicee5', c.project([[0.0, 0.0, 0.0], [0.0, 0.0, 1.0]])), ('dicee6', c.project([[1.0, 0.0, 0.0], [1.0, 0.0, 1.0]])), ('dicee7', c.project([[1.0, 0.0, 0.0], [2.0, 0.0, 0.0]])), ('dicee8', c.project([[1.0, 0.0, 1.0], [2.0, 0.0, 1.0]])), ('dicee9', c.project([[1.0, 1.0, 1.0], [2.0, 1.0, 1.0]])), ('dicee10', c.project([[2.0, 0.0, 0.0], [2.0, 1.0, 0.0]])), ('dicee11', c.project([[2.0, 0.0, 1.0], [2.0, 1.0, 1.0]])), ('dicee12', c.project([[2.0, 0.0, 0.0], [2.0, 0.0, 1.0]])), ('dicee13', c.project([[2.0, 1.0, 0.0], [2.0, 1.0, 1.0]]))]:
                c.line(points, id=object_id, clip_on=False, zorder=3)
            for object_id, points in [('die0toppip0', c.project([[0.5, 0.5, 1.0]])), ('die0frontpip0', c.project([[0.25, 0.0, 0.25]])), ('die0frontpip1', c.project([[0.75, 0.0, 0.75]])), ('die1toppip0', c.project([[1.25, 0.25, 1.0]])), ('die1toppip1', c.project([[1.25, 0.75, 1.0]])), ('die1toppip2', c.project([[1.75, 0.25, 1.0]])), ('die1toppip3', c.project([[1.75, 0.75, 1.0]])), ('die1frontpip0', c.project([[1.25, 0.0, 0.25]])), ('die1frontpip1', c.project([[1.25, 0.0, 0.5]])), ('die1frontpip2', c.project([[1.25, 0.0, 0.75]])), ('die1frontpip3', c.project([[1.75, 0.0, 0.25]])), ('die1frontpip4', c.project([[1.75, 0.0, 0.5]])), ('die1frontpip5', c.project([[1.75, 0.0, 0.75]])), ('right2pip0', c.project([[2, 0.25, 0.25]])), ('right2pip1', c.project([[2, 0.75, 0.75]]))]:
                c.point(points, id=object_id, filled=True)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Solid192().draw(sys.argv[1] if len(sys.argv) > 1 else None))
