"""Frozen question Solid34; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Solid34:

    def __init__(self):
        self.id = 'Solid34'
        self.source_dataset = 'MathVerse'
        self.source_key = 'testmini:639'
        self.question = 'As shown in the figure, If OA and OB are overlapped to form a cone side, the diameter of the bottom of the cone is ()\nChoices:\nA:2cm\nB:4cm\nC:3cm\nD:5cm'
        self.answer = 'B'
        self.answer_type = 'choice'
        self.choices = {'A': '2cm', 'B': '4cm', 'C': '3cm', 'D': '5cm'}
        self.query = self.question
        self.points = {'T': [0.0, 0.0, 5.656854249492381],
         'O': [0.0, 0.0, 0.0],
         'R': [2.0, 0.0, 0.0],
         'L': [-2.0, 0.0, 0.0],
         'TR': [1.9918333895267382, 0.18055400401659594, 0.0],
         'TL': [-1.9918333895267382, 0.18055400401659627, 0.0],
         'net_end': [3.905557553998407, -0.14530638840727558, 10.209381706399588],
         'angle_anchor': [1.5234926604106627, 0.009105634032407751, 5.371569828074544],
         'net_radius_measure_anchor': [1.9527787769992035, -0.07265319420363779, 7.933117977945985]}
        self.subject = 'SolidGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'SolidGeometry' / 'dataset_generator/scenes/Solid34.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('SolidGeometry', self.id, variant, output_path)
        with Canvas(SOLID, xlim=[-3.709604423380655, 7.709596362339006], ylim=[-0.7749975495092354, 10.644203236210426], projection=[[1, 0, 0], [0, 0.24740395925452294, 0.9689124217106447]], origin=[0, 0, 0], offset=[0, 0]) as c:
            c.line(c.project([self.points['T'], self.points['TR']]), id='silhouette_TR', clip_on=False, zorder=3)
            c.line(c.project([self.points['T'], self.points['TL']]), id='silhouette_TL', clip_on=False, zorder=3)
            t = np.radians(np.linspace(5.179543008189399, 174.8204569918106, 341))
            xyz = np.asarray(self.points['O']) + 2.0 * (np.cos(t)[:, None] * np.array([1.0, 0.0, 0.0]) + np.sin(t)[:, None] * np.array([0.0, 1.0, 0.0]))
            c.line(c.project(xyz), linestyle=(0, [4, 3]), clip_on=False, id='base_rim')
            t = np.radians(np.linspace(174.8204569918106, 365.1795430081894, 382))
            xyz = np.asarray(self.points['O']) + 2.0 * (np.cos(t)[:, None] * np.array([1.0, 0.0, 0.0]) + np.sin(t)[:, None] * np.array([0.0, 1.0, 0.0]))
            c.line(c.project(xyz), clip_on=False, zorder=3, id='base_rim')
            c.line(c.project([self.points['T'], self.points['net_end']]), id='net_second_radius', clip_on=False, zorder=3)
            t = np.radians(np.linspace(0.0, 120.0, 242))
            xyz = np.asarray(self.points['T']) + 6.0 * (np.cos(t)[:, None] * np.array([0.3319722315877897, 0.03009233400276599, -0.9428090415820635]) + np.sin(t)[:, None] * np.array([0.9432891589828767, -0.010590410350263224, 0.3318032636276957]))
            c.line(c.project(xyz), clip_on=False, zorder=3, id='net_boundary')
            t = np.radians(np.linspace(0.0, 120.0, 242))
            xyz = np.asarray(self.points['T']) + 0.65 * (np.cos(t)[:, None] * np.array([0.3319722315877897, 0.03009233400276599, -0.9428090415820635]) + np.sin(t)[:, None] * np.array([0.9432891589828767, -0.010590410350263224, 0.3318032636276957]))
            c.line(c.project(xyz), clip_on=False, zorder=3, id='net_angle_arc')
            c.text('120°', c.project(self.points['angle_anchor']), offset_pt=[10, 1], vertex=False, id='sector_angle')
            c.text('6', c.project(self.points['net_radius_measure_anchor']), offset_pt=[0, 18], vertex=False, id='net_radius_measure')
            c.text('O', c.project(self.points['T']), offset_pt=[-16, 0], vertex=True, id='name_O')
            c.text('A', c.project(self.points['TR']), offset_pt=[16.900000000000002, -9.1], vertex=True, id='name_A')
            c.text('B', c.project(self.points['net_end']), offset_pt=[0, 15], vertex=True, id='name_B')
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Solid34().draw(sys.argv[1] if len(sys.argv) > 1 else None))
