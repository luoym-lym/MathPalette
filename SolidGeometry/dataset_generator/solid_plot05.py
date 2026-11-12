"""Frozen question Solid05; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Solid05:

    def __init__(self):
        self.id = 'Solid05'
        self.source_dataset = 'MathVerse'
        self.source_key = 's3404'
        self.question = 'Calculate the area of the divider correct to two decimal places, using your rounded answer from the previous part.'
        self.answer = '\\[75.15 \\mathrm{cm}^2\\]'
        self.answer_type = 'number'
        self.query = self.question
        self.points = {'A': [0, 0, 0],
         'B': [19, 0, 0],
         'C': [19, 10, 0],
         'D': [19, 10, 7],
         'E': [0, 10, 0],
         'F': [0, 10, 7],
         'G': [0, 0, 7],
         'H': [19, 0, 7],
         'MAB': [9.5, 0.0, 0.0],
         'MBC': [19.0, 5.0, 0.0],
         'MCD': [19.0, 10.0, 3.5],
         'MZ': [12.666666666666666, 6.666666666666667, 2.3333333333333335],
         'M_AB': [9.5, 0.0, 0.0],
         'M_BC': [19.0, 5.0, 0.0],
         'M_CD': [19.0, 10.0, 3.5],
         'M_AC': [9.5, 5.0, 0.0]}
        self.subject = 'SolidGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'SolidGeometry' / 'dataset_generator/scenes/Solid05.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('SolidGeometry', self.id, variant, output_path)
        with Canvas(SOLID, xlim=[-1.4636181458786375, 29.381503546674594], ylim=[-8.587257409985629, 22.257864282567603], projection=[[1, 0.6820512820512821, 0], [0, 0.38974358974358975, 1.415140415140415]], origin=[0, 0, 0], offset=[0, 0]) as c:
            for object_id, points in [('AB', c.project([self.points['A'], self.points['B']])), ('BC', c.project([self.points['B'], self.points['C']])), ('CD', c.project([self.points['C'], self.points['D']])), ('DH', c.project([self.points['D'], self.points['H']])), ('HG', c.project([self.points['H'], self.points['G']])), ('GA', c.project([self.points['G'], self.points['A']]))]:
                c.line(points, id=object_id, clip_on=False, zorder=3)
            for object_id, points in [('AE', c.project([self.points['A'], self.points['E']])), ('EF', c.project([self.points['E'], self.points['F']])), ('EC', c.project([self.points['E'], self.points['C']]))]:
                c.line(points, id=object_id, linestyle=(0, [4, 3]), clip_on=False)
            for object_id, points in [('FD', c.project([self.points['F'], self.points['D']])), ('FG', c.project([self.points['F'], self.points['G']])), ('BH', c.project([self.points['B'], self.points['H']]))]:
                c.line(points, id=object_id, clip_on=False, zorder=3)
            c.fill(c.project([self.points['A'], self.points['C'], self.points['D']]), facecolor='#E6E6E6', alpha=1, id='divider')
            c.text('A', c.project(self.points['A']), offset_pt=[-5, -13], vertex=True, id='vertex_A')
            c.text('B', c.project(self.points['B']), offset_pt=[-2, -13], vertex=True, id='vertex_B')
            c.text('C', c.project(self.points['C']), offset_pt=[8, -6], vertex=True, id='vertex_C')
            c.text('D', c.project(self.points['D']), offset_pt=[9, 8], vertex=True, id='vertex_D')
            c.text('19 cm', c.project(self.points['M_AB']), offset_pt=[0, -14], vertex=False, id='AB_length')
            c.text('10 cm', c.project(self.points['M_BC']), offset_pt=[25, -23], vertex=False, id='BC_length')
            c.text('7 cm', c.project(self.points['M_CD']), offset_pt=[27, 0], vertex=False, id='CD_length')
            c.text('z cm', c.project(self.points['M_AC']), offset_pt=[0, -12], vertex=False, id='unknown_z')
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Solid05().draw(sys.argv[1] if len(sys.argv) > 1 else None))
