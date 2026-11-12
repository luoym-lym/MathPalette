"""Frozen question Solid02; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Solid02:

    def __init__(self):
        self.id = 'Solid02'
        self.source_dataset = 'MathVerse'
        self.source_key = 's3209'
        self.question = 'Find the volume of the cylinder shown, correct to two decimal places.'
        self.answer = 'Volume $=883.57 \\mathrm{~cm}^{3}$'
        self.answer_type = 'number'
        self.query = self.question
        self.points = {'O0': [0, 0, 0],
         'O1': [0, 15, 0],
         'U0': [3.061616997868383e-16, 0, 5.0],
         'R0': [5.0, 0, 0.0],
         'U1': [3.061616997868383e-16, 15, 5.0],
         'R1': [5.0, 15, 0.0],
         'T0': [2.236067977499789, 0, -4.47213595499958],
         'T1': [2.236067977499789, 15, -4.47213595499958],
         'M_R': [2.5, 0.0, 0.0],
         'M_L': [2.236067977499789, 7.5, -4.47213595499958]}
        self.subject = 'SolidGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'SolidGeometry' / 'dataset_generator/scenes/Solid02.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('SolidGeometry', self.id, variant, output_path)
        with Canvas(SOLID, xlim=[-5.5560676141905665, 17.874137968710446], ylim=[-8.654713602040424, 14.77549198086059], projection=[[1, 0.82, 0], [0, 0.41, 1]], origin=[0, 0, 0], offset=[0, 0]) as c:
            t = np.radians(np.linspace(90, 360, 361))
            xyz = np.asarray(self.points['O0']) + 5 * (np.cos(t)[:, None] * np.array([1, 0, 0]) + np.sin(t)[:, None] * np.array([0, 0, 1]))
            c.line(c.project(xyz), clip_on=False, zorder=3, id='front_sector_outline')
            t = np.radians(np.linspace(90, 116.56505117707798, 361))
            xyz = np.asarray(self.points['O1']) + 5 * (np.cos(t)[:, None] * np.array([1, 0, 0]) + np.sin(t)[:, None] * np.array([0, 0, 1]))
            c.line(c.project(xyz), clip_on=False, zorder=3, id='back_exposed_upper')
            t = np.radians(np.linspace(116.56505117707798, 296.565051177078, 361))
            xyz = np.asarray(self.points['O1']) + 5 * (np.cos(t)[:, None] * np.array([1, 0, 0]) + np.sin(t)[:, None] * np.array([0, 0, 1]))
            c.line(c.project(xyz), linestyle=(0, [4, 3]), clip_on=False, id='back_occluded')
            t = np.radians(np.linspace(296.565051177078, 360, 361))
            xyz = np.asarray(self.points['O1']) + 5 * (np.cos(t)[:, None] * np.array([1, 0, 0]) + np.sin(t)[:, None] * np.array([0, 0, 1]))
            for object_id, points in [('back_exposed_lower', c.project(xyz)), ('radial_top_front', c.project([self.points['O0'], self.points['U0']])), ('radial_side_front', c.project([self.points['O0'], self.points['R0']])), ('radial_top_back', c.project([self.points['O1'], self.points['U1']])), ('radial_side_back', c.project([self.points['O1'], self.points['R1']])), ('top_generator', c.project([self.points['U0'], self.points['U1']])), ('side_generator', c.project([self.points['R0'], self.points['R1']])), ('center_cut_edge', c.project([self.points['O0'], self.points['O1']])), ('curved_surface_tangent', c.project([self.points['T0'], self.points['T1']]))]:
                c.line(points, id=object_id, clip_on=False, zorder=3)
            c.text('5 cm', c.project(self.points['M_R']), offset_pt=[0, -15], vertex=False, id='radius_text')
            c.text('15 cm', c.project(self.points['M_L']), offset_pt=[8, -18], vertex=False, id='length_text')
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Solid02().draw(sys.argv[1] if len(sys.argv) > 1 else None))
