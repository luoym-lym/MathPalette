"""Frozen question Solid66; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Solid66:

    def __init__(self):
        self.id = 'Solid66'
        self.source_dataset = 'MathVerse'
        self.source_key = 'testmini:3754'
        self.question = 'In the cylindrical tube shown above, the circumference of the circular base is 32 . If the tube is cut along $\\overline{A B}$ and laid out flat to make a rectangle, what is the length of $\\overline{A C}$ to the nearest whole number?\nChoices:\nA:24\nB:30\nC:34\nD:38'
        self.answer = 'C'
        self.answer_type = 'choice'
        self.choices = {'A': '24', 'B': '30', 'C': '34', 'D': '38'}
        self.query = self.question
        self.points = {'O': [0.0, 0.0, 0.0],
         'Q': [0.0, 0.0, 30.0],
         'L': [-5.092958178940651, 0.0, 0.0],
         'Ltop': [-5.092958178940651, 0.0, 30.0],
         'R': [5.092958178940651, 0.0, 0.0],
         'Rtop': [5.092958178940651, 0.0, 30.0],
         'length_value_anchor': [5.092958178940651, 0.0, 15.0]}
        self.subject = 'SolidGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'SolidGeometry' / 'dataset_generator/scenes/Solid66.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('SolidGeometry', self.id, variant, output_path)
        with Canvas(SOLID, xlim=[-31.135636312654945, 2.0199995930078654], ylim=[-16.279349541608347, 16.876286364054465], projection=[[6.123233995736766e-17, -0.23770262642713458, -0.9713379748520297], [1.0, 1.455508803014547e-17, 5.947729708964052e-17]], origin=[0, 0, 0], offset=[0, 0]) as c:
            c.line(c.project([self.points['L'], self.points['Ltop']]), id='silhouette_L', clip_on=False, zorder=3)
            c.line(c.project([self.points['R'], self.points['Rtop']]), id='silhouette_R', clip_on=False, zorder=3)
            t = np.radians(np.linspace(0.0, 360.0, 722))
            xyz = np.asarray(self.points['Q']) + 5.092958178940651 * (np.cos(t)[:, None] * np.array([1.0, 0.0, 0.0]) + np.sin(t)[:, None] * np.array([0.0, 1.0, 0.0]))
            c.line(c.project(xyz), clip_on=False, zorder=3, id='upper_rim')
            t = np.radians(np.linspace(0.0, 180.0, 362))
            xyz = np.asarray(self.points['O']) + 5.092958178940651 * (np.cos(t)[:, None] * np.array([1.0, 0.0, 0.0]) + np.sin(t)[:, None] * np.array([0.0, 1.0, 0.0]))
            c.line(c.project(xyz), linestyle=(0, [4, 3]), clip_on=False, id='lower_rim')
            t = np.radians(np.linspace(180.0, 360.0, 362))
            xyz = np.asarray(self.points['O']) + 5.092958178940651 * (np.cos(t)[:, None] * np.array([1.0, 0.0, 0.0]) + np.sin(t)[:, None] * np.array([0.0, 1.0, 0.0]))
            c.line(c.project(xyz), clip_on=False, zorder=3, id='lower_rim')
            c.line(c.project([self.points['Ltop'], self.points['Rtop']]), id='front_diameter', clip_on=False, zorder=3)
            c.line(c.project([self.points['L'], self.points['R']]), id='rear_diameter', linestyle=(0, [4, 3]), clip_on=False)
            c.text('30', c.project(self.points['length_value_anchor']), offset_pt=[1.102182119232618e-15, 18.0], vertex=False, id='length_value')
            c.text('A', c.project(self.points['Rtop']), offset_pt=[-10, 12], vertex=True, id='name_A')
            c.text('B', c.project(self.points['R']), offset_pt=[10, 12], vertex=True, id='name_B')
            c.text('C', c.project(self.points['L']), offset_pt=[10, -12], vertex=True, id='name_C')
            c.text('D', c.project(self.points['Ltop']), offset_pt=[-10, -12], vertex=True, id='name_D')
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Solid66().draw(sys.argv[1] if len(sys.argv) > 1 else None))
