"""Frozen question Solid244; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Solid244:

    def __init__(self):
        self.id = 'Solid244'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:2995'
        self.question = '$ABCDEFGH$ shown below is a right rectangular prism.  If the volume of pyramid $ABCH$ is 20, then what is the volume of $ABCDEFGH$?'
        self.answer = '120'
        self.answer_type = 'number'
        self.query = self.question
        self.points = {'A': [0, 0, 0], 'B': [0, 1, 0], 'C': [2, 1, 0], 'D': [2, 0, 0], 'E': [0, 0, 1.5], 'F': [0, 1, 1.5], 'G': [2, 1, 1.5], 'H': [2, 0, 1.5]}
        self.subject = 'SolidGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'SolidGeometry' / 'dataset_generator/scenes/Solid244.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('SolidGeometry', self.id, variant, output_path)
        with Canvas(SOLID, xlim=[-1.5690708249356673, 2.2968601649934284], ylim=[-1.4191123764261282, 2.4468186135029675], projection=[[1, -1.3, 0], [-0.08, -0.3, 1]], origin=[0, 0, 0], offset=[0, 0]) as c:
            for object_id, points in [('line_0', c.project([self.points['A'], self.points['B']])), ('line_1', c.project([self.points['A'], self.points['D']])), ('line_2', c.project([self.points['A'], self.points['E']]))]:
                c.line(points, id=object_id, linestyle=(0, [4, 3]), clip_on=False)
            for object_id, points in [('line_3', c.project([self.points['B'], self.points['C']])), ('line_4', c.project([self.points['C'], self.points['D']])), ('line_5', c.project([self.points['B'], self.points['F']])), ('line_6', c.project([self.points['C'], self.points['G']])), ('line_7', c.project([self.points['D'], self.points['H']])), ('line_8', c.project([self.points['E'], self.points['F']])), ('line_9', c.project([self.points['F'], self.points['G']])), ('line_10', c.project([self.points['G'], self.points['H']])), ('line_11', c.project([self.points['H'], self.points['E']]))]:
                c.line(points, id=object_id, clip_on=False, zorder=3)
            c.text('A', c.project(self.points['A']), offset_pt=[0, -17], vertex=True, id='label_0')
            c.text('B', c.project(self.points['B']), offset_pt=[-18, 0], vertex=True, id='label_1')
            c.text('C', c.project(self.points['C']), offset_pt=[0, -22], vertex=True, id='label_2')
            c.text('D', c.project(self.points['D']), offset_pt=[18, 0], vertex=True, id='label_3')
            c.text('E', c.project(self.points['E']), offset_pt=[0, 18], vertex=True, id='label_4')
            c.text('F', c.project(self.points['F']), offset_pt=[-18, 0], vertex=True, id='label_5')
            c.text('G', c.project(self.points['G']), offset_pt=[-20, -20], vertex=True, id='label_6')
            c.text('H', c.project(self.points['H']), offset_pt=[20, 0], vertex=True, id='label_7')
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Solid244().draw(sys.argv[1] if len(sys.argv) > 1 else None))
