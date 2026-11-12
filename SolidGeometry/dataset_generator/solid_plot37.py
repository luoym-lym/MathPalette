"""Frozen question Solid37; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Solid37:

    def __init__(self):
        self.id = 'Solid37'
        self.source_dataset = 'MathVerse'
        self.source_key = 'testmini:3179'
        self.question = 'The radius of the base of the cone is denoted by $r$.\n\nFind the value of $r$.'
        self.answer = '5 m'
        self.answer_type = 'number'
        self.query = self.question
        self.points = {'T': [0.0, 0.0, 12.0],
         'O': [0.0, 0.0, 0.0],
         'R': [5.0, 0.0, 0.0],
         'L': [-5.0, 0.0, 0.0],
         'TR': [4.971621070959463, 0.5319623358771589, 0.0],
         'TL': [-4.971621070959463, 0.5319623358771597, 0.0],
         'right_angle0': [0.6, 0.0, 0.0],
         'right_angle1': [0.6, 0.0, 0.6],
         'right_angle2': [0.0, 0.0, 0.6],
         'radius_value_anchor': [2.5, 0.0, 0.0],
         'height_value_anchor': [0.0, 0.0, 6.0],
         'slant_value_anchor': [2.4858105354797315, 0.26598116793857945, 6.0]}
        self.subject = 'SolidGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'SolidGeometry' / 'dataset_generator/scenes/Solid37.json'

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
            c.line(c.project([self.points['O'], self.points['R']]), id='radius', linestyle=(0, [4, 3]), clip_on=False)
            c.line(c.project([self.points['right_angle0'], self.points['right_angle1'], self.points['right_angle2']]), id='right_angle', clip_on=False, zorder=3)
            c.point(c.project([self.points['O']]), filled=True, id='origin_marker')
            c.line(c.project([self.points['L'], self.points['O']]), id='source_left_radius', linestyle=(0, [4, 3]), clip_on=False)
            c.text('r', c.project(self.points['radius_value_anchor']), offset_pt=[0, -16], vertex=False, id='radius_value')
            c.text('12 m', c.project(self.points['height_value_anchor']), offset_pt=[-12, 0], vertex=False, ha='right', id='height_value')
            c.text('13 m', c.project(self.points['slant_value_anchor']), offset_pt=[18, 0], vertex=False, ha='left', id='slant_value')
            c.text('O', c.project(self.points['O']), offset_pt=[-12, -15], vertex=True, id='origin_name')
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Solid37().draw(sys.argv[1] if len(sys.argv) > 1 else None))
