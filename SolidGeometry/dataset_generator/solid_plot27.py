"""Frozen question Solid27; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Solid27:

    def __init__(self):
        self.id = 'Solid27'
        self.source_dataset = 'MathVerse'
        self.source_key = 'testmini:574'
        self.question = 'The sector shown is folded into an open conical paper cap without overlap. Find the circumference of the cap’s circular base. All lengths shown are in centimetres.\nChoices:\nA:2π cm\nB:3π cm\nC:4π cm\nD:5π cm'
        self.answer = 'C'
        self.answer_type = 'choice'
        self.choices = {'A': '2π cm', 'B': '3π cm', 'C': '4π cm', 'D': '5π cm'}
        self.query = self.question
        self.points = {'T': [7.5, 0.0, 5.656854249492381],
         'O': [7.5, 0.0, 0.0],
         'R': [9.5, 0.0, 0.0],
         'L': [5.5, 0.0, 0.0],
         'TR': [9.491833389526738, 0.18055400401659594, 0.0],
         'TL': [5.508166610473262, 0.18055400401659627, 0.0],
         'sector_O': [-7.199999999999999, 0.0, 0.0],
         'sector_A': [-2.0038475772933673, 0.7422118777635687, 2.906737265131934],
         'sector_B': [-12.396152422706631, 0.7422118777635687, 2.906737265131934],
         'sector_radius_label_anchor': [-9.798076211353315, 0.37110593888178434, 1.453368632565967],
         'sector_angle_label_anchor': [-7.199999999999999, 0.3711059388817844, 1.4533686325659672]}
        self.subject = 'SolidGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'SolidGeometry' / 'dataset_generator/scenes/Solid27.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('SolidGeometry', self.id, variant, output_path)
        with Canvas(SOLID, xlim=[-12.946987571037448, 10.050808978120136], ylim=[-8.74632820354417, 14.251468345613414], projection=[[1, 0, 0], [0, 0.24740395925452294, 0.9689124217106447]], origin=[0, 0, 0], offset=[0, 0]) as c:
            c.line(c.project([self.points['T'], self.points['TR']]), id='silhouette_TR', clip_on=False, zorder=3)
            c.line(c.project([self.points['T'], self.points['TL']]), id='silhouette_TL', clip_on=False, zorder=3)
            t = np.radians(np.linspace(5.179543008189399, 174.8204569918106, 341))
            xyz = np.asarray(self.points['O']) + 2.0 * (np.cos(t)[:, None] * np.array([1.0, 0.0, 0.0]) + np.sin(t)[:, None] * np.array([0.0, 1.0, 0.0]))
            c.line(c.project(xyz), linestyle=(0, [4, 3]), clip_on=False, id='base_rim')
            t = np.radians(np.linspace(174.8204569918106, 365.1795430081894, 382))
            xyz = np.asarray(self.points['O']) + 2.0 * (np.cos(t)[:, None] * np.array([1.0, 0.0, 0.0]) + np.sin(t)[:, None] * np.array([0.0, 1.0, 0.0]))
            c.line(c.project(xyz), clip_on=False, zorder=3, id='base_rim')
            c.line(c.project([self.points['O'], self.points['T']]), id='axis', linestyle=(0, [4, 3]), clip_on=False)
            c.line(c.project([self.points['O'], self.points['R']]), id='radius', linestyle=(0, [4, 3]), clip_on=False)
            c.line(c.project([self.points['sector_O'], self.points['sector_A']]), id='sector_first', clip_on=False, zorder=3)
            c.line(c.project([self.points['sector_O'], self.points['sector_B']]), id='sector_second', clip_on=False, zorder=3)
            t = np.radians(np.linspace(30.0, 150.0, 242))
            xyz = np.asarray(self.points['sector_O']) + 6.0 * (np.cos(t)[:, None] * np.array([1.0, 0.0, 0.0]) + np.sin(t)[:, None] * np.array([0.0, 0.24740395925452294, 0.9689124217106447]))
            c.line(c.project(xyz), clip_on=False, zorder=3, id='sector_arc')
            t = np.radians(np.linspace(30.0, 150.0, 242))
            xyz = np.asarray(self.points['sector_O']) + 0.72 * (np.cos(t)[:, None] * np.array([1.0, 0.0, 0.0]) + np.sin(t)[:, None] * np.array([0.0, 0.24740395925452294, 0.9689124217106447]))
            c.line(c.project(xyz), clip_on=False, zorder=3, id='sector_angle_arc')
            c.text('6', c.project(self.points['sector_radius_label_anchor']), offset_pt=[-26.364, 30.758000000000003], vertex=False, id='sector_radius_label')
            c.text('120°', c.project(self.points['sector_angle_label_anchor']), offset_pt=[0, 0], vertex=False, id='sector_angle_label')
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Solid27().draw(sys.argv[1] if len(sys.argv) > 1 else None))
