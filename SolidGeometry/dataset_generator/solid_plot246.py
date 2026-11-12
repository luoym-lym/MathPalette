"""Frozen question Solid246; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Solid246:

    def __init__(self):
        self.id = 'Solid246'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:3008'
        self.question = 'A card is 6 inches wide and 8 inches tall. Point A is 3 inches from the fold, as shown. As the card is opened to an angle of 45 degrees, how many more inches does point B travel than point A? Give the answer as a common fraction in terms of $\\pi$.'
        self.answer = '\\frac{3}{4}\\pi{inches}'
        self.answer_type = 'number'
        self.query = self.question
        self.points = {'O': [0, 0, 0],
         'T': [0, 0, 8],
         'U': [6, 0, 8],
         'V': [6, 0, 0],
         'B': [4.242640687119286, 4.242640687119286, 8],
         'W': [4.242640687119286, 4.242640687119286, 0],
         'A': [2.121320343559643, 2.121320343559643, 8],
         'K': [5.091168824543143, 0, 0],
         'height': [0, 0, 4],
         'width': [2.121320343559643, 2.121320343559643, 0],
         'greeting': [2.121320343559643, 2.121320343559643, 3.7]}
        self.subject = 'SolidGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'SolidGeometry' / 'dataset_generator/scenes/Solid246.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('SolidGeometry', self.id, variant, output_path)
        with Canvas(SOLID, xlim=[-1.9144760926778313, 7.39343005598518], ylim=[-1.090335883360658, 8.217570265302353], projection=[[1, 0.2, 0], [0, -0.2, 1]], origin=[0, 0, 0], offset=[0, 0]) as c:
            for object_id, points in [('line_0', c.project([self.points['O'], self.points['T']])), ('line_1', c.project([self.points['T'], self.points['U']])), ('line_2', c.project([self.points['U'], self.points['V']])), ('line_3', c.project([self.points['K'], self.points['V']])), ('line_4', c.project([self.points['T'], self.points['B']])), ('line_5', c.project([self.points['B'], self.points['W']])), ('line_6', c.project([self.points['W'], self.points['O']]))]:
                c.line(points, id=object_id, clip_on=False, zorder=3)
            c.point(c.project([self.points['A']]), filled=True, id='dot_A')
            c.point(c.project([self.points['B']]), filled=True, id='dot_B')
            c.text('A', c.project(self.points['A']), offset_pt=[-8, -17], vertex=True, id='label_0')
            c.text('B', c.project(self.points['B']), offset_pt=[-15, -15], vertex=True, id='label_1')
            c.text('8″', c.project(self.points['height']), offset_pt=[-22, 0], vertex=False, id='label_2')
            c.text('6″', c.project(self.points['width']), offset_pt=[0, -20], vertex=False, id='label_3')
            c.text('Happy Birthday!', c.project(self.points['greeting']), offset_pt=[0, 0], vertex=False, id='label_4')
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Solid246().draw(sys.argv[1] if len(sys.argv) > 1 else None))
