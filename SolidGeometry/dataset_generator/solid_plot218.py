"""Frozen question Solid218; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Solid218:

    def __init__(self):
        self.id = 'Solid218'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:2432'
        self.question = 'In the figure, polygons $ A$, $ E$, and $ F$ are isosceles right triangles; $ B$, $ C$, and $ D$ are squares with sides of length $ 1$; and $ G$ is an equilateral triangle. The figure can be folded along its edges to form a polyhedron having the polygons as faces.\nThe volume of this polyhedron is\nChoices:\nA:1/2\nB:2/3\nC:3/4\nD:5/6\nE:4/3'
        self.answer = 'D'
        self.answer_type = 'choice'
        self.choices = {'A': '1/2', 'B': '2/3', 'C': '3/4', 'D': '5/6', 'E': '4/3'}
        self.query = self.question
        self.points = {'p1_2': [1, 2, 0],
         'p1_3': [1, 3, 0],
         'p2_2': [2, 2, 0],
         'labelA': [1.3333333333333333, 2.3333333333333335, 0],
         'p1_1': [1, 1, 0],
         'p2_1': [2, 1, 0],
         'labelB': [1.5, 1.5, 0],
         'p0_0': [0, 0, 0],
         'p1_0': [1, 0, 0],
         'p0_1': [0, 1, 0],
         'labelC': [0.5, 0.5, 0],
         'p2_0': [2, 0, 0],
         'labelD': [1.5, 0.5, 0],
         'p3_1': [3, 1, 0],
         'labelE': [2.3333333333333335, 0.6666666666666666, 0],
         'p1_-1': [1, -1, 0],
         'labelF': [1.3333333333333333, -0.3333333333333333, 0],
         'p2.3660254037844384_-1.3660254037844386': [2.3660254037844384, -1.3660254037844386, 0],
         'labelG': [1.7886751345948129, -0.7886751345948128, 0]}
        self.subject = 'SolidGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'SolidGeometry' / 'dataset_generator/scenes/Solid218.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('SolidGeometry', self.id, variant, output_path)
        with Canvas(SOLID, xlim=[-0.7873708650944011, 3.7962092615471], ylim=[-1.4748027652129698, 3.1087773614285314], projection=[[1, 0, 0], [0, 1, 0]], origin=[0, 0, 0], offset=[0, 0]) as c:
            for object_id, points in [('line_0', c.project([self.points['p1_-1'], self.points['p2_0']])), ('line_1', c.project([self.points['p0_1'], self.points['p1_1']])), ('line_2', c.project([self.points['p1_0'], self.points['p2_0']])), ('line_3', c.project([self.points['p1_-1'], self.points['p2.3660254037844384_-1.3660254037844386']])), ('line_4', c.project([self.points['p1_1'], self.points['p2_1']])), ('line_5', c.project([self.points['p1_2'], self.points['p2_2']])), ('line_6', c.project([self.points['p2_0'], self.points['p2_1']])), ('line_7', c.project([self.points['p1_0'], self.points['p1_1']])), ('line_8', c.project([self.points['p2_0'], self.points['p3_1']])), ('line_9', c.project([self.points['p1_1'], self.points['p1_2']])), ('line_10', c.project([self.points['p0_0'], self.points['p1_0']])), ('line_11', c.project([self.points['p1_-1'], self.points['p1_0']])), ('line_12', c.project([self.points['p1_3'], self.points['p2_2']])), ('line_13', c.project([self.points['p2.3660254037844384_-1.3660254037844386'], self.points['p2_0']])), ('line_14', c.project([self.points['p1_2'], self.points['p1_3']])), ('line_15', c.project([self.points['p0_0'], self.points['p0_1']])), ('line_16', c.project([self.points['p2_1'], self.points['p3_1']])), ('line_17', c.project([self.points['p2_1'], self.points['p2_2']]))]:
                c.line(points, id=object_id, clip_on=False, zorder=3)
            for object_id, text, anchor in [('label_0', 'A', c.project(self.points['labelA'])), ('label_1', 'B', c.project(self.points['labelB'])), ('label_2', 'C', c.project(self.points['labelC'])), ('label_3', 'D', c.project(self.points['labelD'])), ('label_4', 'E', c.project(self.points['labelE'])), ('label_5', 'F', c.project(self.points['labelF'])), ('label_6', 'G', c.project(self.points['labelG']))]:
                c.text(text, anchor, id=object_id, offset_pt=[0, 0], vertex=False)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Solid218().draw(sys.argv[1] if len(sys.argv) > 1 else None))
