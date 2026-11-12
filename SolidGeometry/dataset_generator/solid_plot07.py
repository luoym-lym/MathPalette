"""Frozen question Solid07; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Solid07:

    def __init__(self):
        self.id = 'Solid07'
        self.source_dataset = 'MathVerse'
        self.source_key = 's3419'
        self.question = 'Calculate the area of the divider correct to two decimal places, using your rounded answer from the previous part.'
        self.answer = '\\[94.59 \\mathrm{cm}^2\\]'
        self.answer_type = 'number'
        self.query = self.question
        self.points = {'A': [0, 0, 0],
         'B': [19, 0, 0],
         'C': [19, 9, 0],
         'D': [19, 9, 9],
         'E': [0, 9, 0],
         'F': [0, 9, 9],
         'G': [0, 0, 9],
         'H': [19, 0, 9],
         'MAB': [9.5, 0.0, 0.0],
         'MBC': [19.0, 4.5, 0.0],
         'MCD': [19.0, 9.0, 4.5],
         'MZ': [12.666666666666666, 6.0, 3.0],
         'M_AB': [9.5, 0.0, 0.0],
         'M_BC': [19.0, 4.5, 0.0],
         'M_CD': [19.0, 9.0, 4.5],
         'M_AC': [9.5, 4.5, 0.0]}
        self.subject = 'SolidGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'SolidGeometry' / 'dataset_generator/scenes/Solid07.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('SolidGeometry', self.id, variant, output_path)
        with Canvas(SOLID, xlim=[-1.6776574894475011, 28.82701179210117], ylim=[-8.694102509840484, 21.81056677170819], projection=[[1.0, 0.69, 0.0], [0.0, 0.4, 1.1]], origin=[0, 0, 0], offset=[0, 0]) as c:
            c.fill(c.project([self.points['A'], self.points['C'], self.points['D']]), facecolor='#E6E6E6', alpha=1, id='divider')
            for object_id, points in [('A_B', c.project([self.points['A'], self.points['B']])), ('B_C', c.project([self.points['B'], self.points['C']])), ('C_D', c.project([self.points['C'], self.points['D']])), ('D_H', c.project([self.points['D'], self.points['H']])), ('H_G', c.project([self.points['H'], self.points['G']])), ('G_A', c.project([self.points['G'], self.points['A']])), ('G_F', c.project([self.points['G'], self.points['F']])), ('F_D', c.project([self.points['F'], self.points['D']])), ('B_H', c.project([self.points['B'], self.points['H']]))]:
                c.line(points, id=object_id, clip_on=False, zorder=3)
            for object_id, points in [('A_E', c.project([self.points['A'], self.points['E']])), ('E_F', c.project([self.points['E'], self.points['F']])), ('E_C', c.project([self.points['E'], self.points['C']]))]:
                c.line(points, id=object_id, linestyle=(0, [4, 3]), clip_on=False)
            c.text('A', c.project(self.points['A']), offset_pt=[-9, -9], vertex=True, id='vertexA')
            c.text('B', c.project(self.points['B']), offset_pt=[-3, -13], vertex=True, id='vertexB')
            c.text('C', c.project(self.points['C']), offset_pt=[8, -4], vertex=True, id='vertexC')
            c.text('D', c.project(self.points['D']), offset_pt=[8, 6], vertex=True, id='vertexD')
            c.text('19 cm', c.project(self.points['M_AB']), offset_pt=[0, -16], vertex=False, id='ab')
            c.text('9 cm', c.project(self.points['M_BC']), offset_pt=[18, -28], vertex=False, id='bc')
            c.text('9 cm', c.project(self.points['M_CD']), offset_pt=[29, 0], vertex=False, id='cd')
            c.text('z cm', c.project(self.points['M_AC']), offset_pt=[0, -4], vertex=False, id='z')
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Solid07().draw(sys.argv[1] if len(sys.argv) > 1 else None))
