"""Frozen question Solid92; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Solid92:

    def __init__(self):
        self.id = 'Solid92'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:209'
        self.question = 'Each of the cubes in the figure has the length of an edge equal to 1. What is the length of the segment $A B$?\nChoices:\nA:$\\sqrt{17}$\nB:7\nC:$\\sqrt{13}$\nD:$\\sqrt{7}$\nE:$\\sqrt{14}$'
        self.answer = 'A'
        self.answer_type = 'choice'
        self.choices = {'A': '$\\sqrt{17}$', 'B': '7', 'C': '$\\sqrt{13}$', 'D': '$\\sqrt{7}$', 'E': '$\\sqrt{14}$'}
        self.query = self.question
        self.points = {'A': [0, 0, 0], 'B': [3, 2, 2]}
        self.subject = 'SolidGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'SolidGeometry' / 'dataset_generator/scenes/Solid92.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('SolidGeometry', self.id, variant, output_path)
        with Canvas(SOLID, xlim=[-0.23662675813098089, 3.9246050661864618], ylim=[-0.7352996670287992, 3.4259321572886434], projection=[[1, 0.35, 0], [0, 0.35, 1]], origin=[0, 0, 0], offset=[0, 0]) as c:
            c.line(c.project([[0.0, 0.0, 0.0], [1.0, 0.0, 0.0]]), id='stepse0', clip_on=False, zorder=3)
            c.line(c.project([[0.0, 0.0, 1.0], [1.0, 0.0, 1.0]]), id='stepse1', clip_on=False, zorder=3)
            c.line(c.project([[0.0, 1.0, 0.0], [1.0, 1.0, 0.0]]), id='stepse2', linestyle=(0, [4, 3]), clip_on=False)
            c.line(c.project([[0.0, 1.0, 1.0], [1.0, 1.0, 1.0]]), id='stepse3', clip_on=False, zorder=3)
            c.line(c.project([[0.0, 0.0, 0.0], [0.0, 1.0, 0.0]]), id='stepse4', linestyle=(0, [4, 3]), clip_on=False)
            c.line(c.project([[0.0, 0.0, 1.0], [0.0, 1.0, 1.0]]), id='stepse5', clip_on=False, zorder=3)
            c.line(c.project([[1.0, 0.0, 0.0], [1.0, 1.0, 0.0]]), id='stepse6', linestyle=(0, [4, 3]), clip_on=False)
            c.line(c.project([[1.0, 0.0, 1.0], [1.0, 1.0, 1.0]]), id='stepse7', clip_on=False, zorder=3)
            c.line(c.project([[0.0, 0.0, 0.0], [0.0, 0.0, 1.0]]), id='stepse8', clip_on=False, zorder=3)
            c.line(c.project([[0.0, 1.0, 0.0], [0.0, 1.0, 1.0]]), id='stepse9', linestyle=(0, [4, 3]), clip_on=False)
            c.line(c.project([[1.0, 0.0, 0.0], [1.0, 0.0, 1.0]]), id='stepse10', clip_on=False, zorder=3)
            c.line(c.project([[1.0, 1.0, 0.0], [1.0, 1.0, 1.0]]), id='stepse11', linestyle=(0, [4, 3]), clip_on=False)
            c.line(c.project([[1.0, 0.0, 0.0], [2.0, 0.0, 0.0]]), id='stepse12', clip_on=False, zorder=3)
            c.line(c.project([[1.0, 0.0, 1.0], [2.0, 0.0, 1.0]]), id='stepse13', clip_on=False, zorder=3)
            c.line(c.project([[1.0, 1.0, 0.0], [2.0, 1.0, 0.0]]), id='stepse14', linestyle=(0, [4, 3]), clip_on=False)
            c.line(c.project([[1.0, 1.0, 1.0], [2.0, 1.0, 1.0]]), id='stepse15', clip_on=False, zorder=3)
            c.line(c.project([[2.0, 0.0, 0.0], [2.0, 1.0, 0.0]]), id='stepse16', linestyle=(0, [4, 3]), clip_on=False)
            c.line(c.project([[2.0, 0.0, 1.0], [2.0, 1.0, 1.0]]), id='stepse17', clip_on=False, zorder=3)
            c.line(c.project([[2.0, 0.0, 0.0], [2.0, 0.0, 1.0]]), id='stepse18', clip_on=False, zorder=3)
            c.line(c.project([[2.0, 1.0, 0.0], [2.0, 1.0, 1.0]]), id='stepse19', linestyle=(0, [4, 3]), clip_on=False)
            c.line(c.project([[2.0, 0.0, 0.0], [3.0, 0.0, 0.0]]), id='stepse20', clip_on=False, zorder=3)
            c.line(c.project([[2.0, 0.0, 1.0], [3.0, 0.0, 1.0]]), id='stepse21', clip_on=False, zorder=3)
            c.line(c.project([[2.0, 1.0, 0.0], [3.0, 1.0, 0.0]]), id='stepse22', linestyle=(0, [4, 3]), clip_on=False)
            for object_id, points in [('stepse23', c.project([[2.0, 1.0, 1.0], [3.0, 1.0, 1.0]])), ('stepse24', c.project([[3.0, 0.0, 0.0], [3.0, 1.0, 0.0]])), ('stepse25', c.project([[3.0, 0.0, 1.0], [3.0, 1.0, 1.0]])), ('stepse26', c.project([[3.0, 0.0, 0.0], [3.0, 0.0, 1.0]])), ('stepse27', c.project([[3.0, 1.0, 0.0], [3.0, 1.0, 1.0]])), ('stepse28', c.project([[2.0, 1.0, 2.0], [3.0, 1.0, 2.0]]))]:
                c.line(points, id=object_id, clip_on=False, zorder=3)
            c.line(c.project([[2.0, 2.0, 1.0], [3.0, 2.0, 1.0]]), id='stepse29', linestyle=(0, [4, 3]), clip_on=False)
            c.line(c.project([[2.0, 2.0, 2.0], [3.0, 2.0, 2.0]]), id='stepse30', clip_on=False, zorder=3)
            c.line(c.project([[2.0, 1.0, 1.0], [2.0, 2.0, 1.0]]), id='stepse31', linestyle=(0, [4, 3]), clip_on=False)
            for object_id, points in [('stepse32', c.project([[2.0, 1.0, 2.0], [2.0, 2.0, 2.0]])), ('stepse33', c.project([[3.0, 1.0, 1.0], [3.0, 2.0, 1.0]])), ('stepse34', c.project([[3.0, 1.0, 2.0], [3.0, 2.0, 2.0]])), ('stepse35', c.project([[2.0, 1.0, 1.0], [2.0, 1.0, 2.0]]))]:
                c.line(points, id=object_id, clip_on=False, zorder=3)
            c.line(c.project([[2.0, 2.0, 1.0], [2.0, 2.0, 2.0]]), id='stepse36', linestyle=(0, [4, 3]), clip_on=False)
            for object_id, points in [('stepse37', c.project([[3.0, 1.0, 1.0], [3.0, 1.0, 2.0]])), ('stepse38', c.project([[3.0, 2.0, 1.0], [3.0, 2.0, 2.0]])), ('AB', c.project([self.points['A'], self.points['B']]))]:
                c.line(points, id=object_id, clip_on=False, zorder=3)
            c.text('A', c.project(self.points['A']), offset_pt=[-10, -14], vertex=True, id='labelA')
            c.text('B', c.project(self.points['B']), offset_pt=[10, 10], vertex=True, id='labelB')
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Solid92().draw(sys.argv[1] if len(sys.argv) > 1 else None))
