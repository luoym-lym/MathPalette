"""Frozen question Solid28; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Solid28:

    def __init__(self):
        self.id = 'Solid28'
        self.source_dataset = 'MathVerse'
        self.source_key = 'testmini:579'
        self.question = 'The area of paper required to make this paper cap is (the seams are ignored) ()\nChoices:\nA:60π\nB:65π\nC:78π\nD:156π'
        self.answer = 'B'
        self.answer_type = 'choice'
        self.choices = {'A': '60π', 'B': '65π', 'C': '78π', 'D': '156π'}
        self.query = self.question
        self.points = {'T': [0.0, 0.0, 12.0],
         'O': [0.0, 0.0, 0.0],
         'R': [5.0, 0.0, 0.0],
         'L': [-5.0, 0.0, 0.0],
         'TR': [4.971621070959463, 0.5319623358771589, 0.0],
         'TL': [-4.971621070959463, 0.5319623358771597, 0.0],
         'height_value_anchor': [0.0, 0.0, 6.0],
         'slant_value_anchor': [2.4858105354797315, 0.26598116793857945, 6.0]}
        self.subject = 'SolidGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'SolidGeometry' / 'dataset_generator/scenes/Solid28.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('SolidGeometry', self.id, variant, output_path)
        with Canvas(SOLID, xlim=[-6.75665721146275, 6.75665721146275], ylim=[-1.5616790212056086, 11.95163540171989], projection=[[1, 0, 0], [0, 0.24740395925452294, 0.9689124217106447]], origin=[0, 0, 0], offset=[0, 0]) as c:
            c.line(c.project([self.points['T'], self.points['TR']]), id='silhouette_TR', clip_on=False, zorder=3)
            c.line(c.project([self.points['T'], self.points['TL']]), id='silhouette_TL', clip_on=False, zorder=3)
            t = np.radians(np.linspace(6.107398481086494, 173.8926015189135, 337))
            xyz = np.asarray(self.points['O']) + 5.0 * (np.cos(t)[:, None] * np.array([1.0, 0.0, 0.0]) + np.sin(t)[:, None] * np.array([0.0, 1.0, 0.0]))
            c.line(c.project(xyz), linestyle=(0, [4, 3]), clip_on=False, id='base_rim')
            t = np.radians(np.linspace(173.8926015189135, 366.1073984810865, 386))
            xyz = np.asarray(self.points['O']) + 5.0 * (np.cos(t)[:, None] * np.array([1.0, 0.0, 0.0]) + np.sin(t)[:, None] * np.array([0.0, 1.0, 0.0]))
            c.line(c.project(xyz), clip_on=False, zorder=3, id='base_rim')
            c.line(c.project([self.points['O'], self.points['T']]), id='axis', linestyle=(0, [4, 3]), clip_on=False)
            c.line(c.project([self.points['L'], self.points['R']]), id='base_diameter', linestyle=(0, [4, 3]), clip_on=False)
            c.text('12', c.project(self.points['height_value_anchor']), offset_pt=[-12, 0], vertex=False, ha='right', id='height_value')
            c.text('13', c.project(self.points['slant_value_anchor']), offset_pt=[18, 0], vertex=False, ha='left', id='slant_value')
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Solid28().draw(sys.argv[1] if len(sys.argv) > 1 else None))
