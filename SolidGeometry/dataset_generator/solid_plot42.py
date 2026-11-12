"""Frozen question Solid42; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Solid42:

    def __init__(self):
        self.id = 'Solid42'
        self.source_dataset = 'MathVerse'
        self.source_key = 'testmini:3224'
        self.question = 'Find the volume of the half cone, correct to two decimal places.'
        self.answer = '10.45 cm³'
        self.answer_type = 'number'
        self.query = self.question
        self.points = {'O': [0.0, 0.0, 0.0],
         'T': [0.0, 0.0, 8.874119674649425],
         'A': [-1.5, 0.0, 0.0],
         'B': [1.5, 0.0, 0.0],
         'right_angle0': [0.18, 0.0, 0.0],
         'right_angle1': [0.18, 0.0, 0.18],
         'right_angle2': [0.0, 0.0, 0.18],
         'slant_anchor': [-0.75, 0.0, 4.437059837324712],
         'diameter_value_anchor': [0.0, 0.0, 0.0]}
        self.subject = 'SolidGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'SolidGeometry' / 'dataset_generator/scenes/Solid42.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('SolidGeometry', self.id, variant, output_path)
        with Canvas(SOLID, xlim=[-2.3360590780080237, 6.020311156141352], ylim=[-1.1173054801529774, 7.239064753996399], projection=[[0.8191520442889918, 0.14190508128834867, 0.5557453339810535], [-0.573576436351046, 0.20266145898853288, 0.7936865909812724]], origin=[0, 0, 0], offset=[0, 0]) as c:
            t = np.radians(np.linspace(180.0, 360.0, 362))
            xyz = np.asarray(self.points['O']) + 1.5 * (np.cos(t)[:, None] * np.array([1.0, 0.0, 0.0]) + np.sin(t)[:, None] * np.array([0.0, 1.0, 0.0]))
            for object_id, points in [('base_semicircle_part0', c.project(xyz)), ('cut_left', c.project([self.points['A'], self.points['T']])), ('cut_right', c.project([self.points['B'], self.points['T']])), ('diameter', c.project([self.points['A'], self.points['B']]))]:
                c.line(points, id=object_id, clip_on=False, zorder=3)
            c.line(c.project([self.points['O'], self.points['T']]), id='axis', linestyle=(0, [4, 3]), clip_on=False, zorder=3)
            c.line(c.project([self.points['right_angle0'], self.points['right_angle1'], self.points['right_angle2']]), id='right_angle', clip_on=False, zorder=3)
            c.text('9 cm', c.project(self.points['slant_anchor']), offset_pt=[-18.02134497435782, 12.618681599723013], vertex=False, id='slant')
            c.text('3 cm', c.project(self.points['diameter_value_anchor']), offset_pt=[-27.72324347459146, -39.592894908664135], vertex=False, id='diameter_value')
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Solid42().draw(sys.argv[1] if len(sys.argv) > 1 else None))
