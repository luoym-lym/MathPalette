"""Frozen question Solid58; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Solid58:

    def __init__(self):
        self.id = 'Solid58'
        self.source_dataset = 'MathVerse'
        self.source_key = 'testmini:3474'
        self.question = 'All lengths are in cm. Find the volume of the sector-shaped prism, correct to one decimal place.'
        self.answer = '89.1 cm³'
        self.answer_type = 'number'
        self.query = self.question
        self.points = {'O': [0.0, 0.0, 0.0],
         'Q': [0.0, 3.0, 0.0],
         'A': [9.0, 0.0, 0.0],
         'Afar': [9.0, 3.0, 0.0],
         'B': [6.688303429296548, 0.0, 6.022175457229724],
         'Bfar': [6.688303429296548, 3.0, 6.022175457229724],
         'axis_corner_0_end': [0.0, 1.0145664191441033e-07, 0.0],
         'radius_value_anchor': [4.5, 0.0, 0.0],
         'sector_angle_anchor': [2.2219214150633397, 0.0, 0.8529157199178147],
         'length_value_anchor': [9.0, 1.5, 0.0]}
        self.subject = 'SolidGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'SolidGeometry' / 'dataset_generator/scenes/Solid58.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('SolidGeometry', self.id, variant, output_path)
        with Canvas(SOLID, xlim=[-0.24525086623724324, 10.212716331159715], ylim=[-0.47119733311354395, 9.986769864283414], projection=[[0.9396926207859084, 0.5013537576466265, -0.3420201433256687], [0.3420201433256687, 0.5230147318131754, 0.9396926207859084]], origin=[0, 0, 0], offset=[0, 0]) as c:
            t = np.radians(np.linspace(0.0, 42.0, 86))
            xyz = np.asarray(self.points['O']) + 9.0 * (np.cos(t)[:, None] * np.array([1.0, 0.0, 0.0]) + np.sin(t)[:, None] * np.array([0.0, 0.0, 1.0]))
            c.line(c.project(xyz), clip_on=False, zorder=3, id='front_curve_part0')
            t = np.radians(np.linspace(0.0, 42.0, 86))
            xyz = np.asarray(self.points['Q']) + 9.0 * (np.cos(t)[:, None] * np.array([1.0, 0.0, 0.0]) + np.sin(t)[:, None] * np.array([0.0, 0.0, 1.0]))
            for object_id, points in [('back_curve_part0', c.project(xyz)), ('side_A_0', c.project([self.points['A'], self.points['Afar']])), ('side_B_0', c.project([self.points['B'], self.points['Bfar']])), ('front_radius_A', c.project([self.points['O'], self.points['A']])), ('front_radius_B', c.project([self.points['O'], self.points['B']])), ('axis_corner_0', c.project([self.points['O'], self.points['axis_corner_0_end']]))]:
                c.line(points, id=object_id, clip_on=False, zorder=3)
            t = np.radians(np.linspace(0.0, 42.0, 86))
            xyz = np.asarray(self.points['O']) + 1.4 * (np.cos(t)[:, None] * np.array([1.0, 0.0, 0.0]) + np.sin(t)[:, None] * np.array([0.0, 0.0, 1.0]))
            c.line(c.project(xyz), clip_on=False, zorder=3, id='sector_angle')
            c.text('9', c.project(self.points['radius_value_anchor']), offset_pt=[6.156362579862037, -16.914467174146353], vertex=False, id='radius_value')
            c.text('42°', c.project(self.points['sector_angle_anchor']), offset_pt=[3.8416871988960093, 9.91168196956695], vertex=False, id='sector_angle_label')
            c.text('3', c.project(self.points['length_value_anchor']), offset_pt=[27.68292504874683, -5.886905871972576], vertex=False, id='length_value')
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Solid58().draw(sys.argv[1] if len(sys.argv) > 1 else None))
