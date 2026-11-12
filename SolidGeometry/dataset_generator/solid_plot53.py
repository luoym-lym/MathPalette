"""Frozen question Solid53; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Solid53:

    def __init__(self):
        self.id = 'Solid53'
        self.source_dataset = 'MathVerse'
        self.source_key = 'testmini:3359'
        self.question = 'Find the surface area of the composite figure shown, consisting of a cone and a hemisphere joined at their bases.\n\nRound your answer to two decimal places.'
        self.answer = '235.87 cm²'
        self.answer_type = 'number'
        self.query = self.question
        self.points = {'O': [0.0, 0.0, 0.0],
         'T': [0.0, 0.0, 10.0],
         'R': [-4.0, 0.0, 0.0],
         'right': [3.9790814628961675, 0.408547073953658, 0.0],
         'left': [-3.9790814628961675, 0.4085470739536575, 0.0],
         'hemisphere_O': [0.0, 0.0, 0.0],
         'right_angle0': [-0.48, 0.0, 0.0],
         'right_angle1': [-0.48, 0.0, 0.48],
         'right_angle2': [0.0, 0.0, 0.48],
         'height_value_anchor': [0.0, 0.0, 5.0],
         'radius_value_anchor': [-2.0, 0.0, 0.0]}
        self.subject = 'SolidGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'SolidGeometry' / 'dataset_generator/scenes/Solid53.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('SolidGeometry', self.id, variant, output_path)
        with Canvas(SOLID, xlim=[-7.182772192211794, 7.182772192211794], ylim=[-4.338182969929025, 10.027361414494564], projection=[[1, 0, 0], [0, 0.24740395925452294, 0.9689124217106447]], origin=[0, 0, 0], offset=[0, 0]) as c:
            c.line(c.project([self.points['right'], self.points['T']]), id='right_cone_contour_0', clip_on=False, zorder=3)
            c.line(c.project([self.points['left'], self.points['T']]), id='left_cone_contour_0', clip_on=False, zorder=3)
            t = np.radians(np.linspace(0.0, 5.866279861802582, 13))
            xyz = np.asarray(self.points['O']) + 4.0 * (np.cos(t)[:, None] * np.array([1.0, 0.0, 0.0]) + np.sin(t)[:, None] * np.array([0.0, 1.0, 0.0]))
            c.line(c.project(xyz), clip_on=False, zorder=3, id='join_circle_part0')
            t = np.radians(np.linspace(5.866279861802582, 174.1337201381756, 338))
            xyz = np.asarray(self.points['O']) + 4.0 * (np.cos(t)[:, None] * np.array([1.0, 0.0, 0.0]) + np.sin(t)[:, None] * np.array([0.0, 1.0, 0.0]))
            c.line(c.project(xyz), linestyle=(0, [4, 3]), clip_on=False, id='join_circle_part1')
            t = np.radians(np.linspace(174.1337201381756, 360.0, 373))
            xyz = np.asarray(self.points['O']) + 4.0 * (np.cos(t)[:, None] * np.array([1.0, 0.0, 0.0]) + np.sin(t)[:, None] * np.array([0.0, 1.0, 0.0]))
            c.line(c.project(xyz), clip_on=False, zorder=3, id='join_circle_part2')
            t = np.radians(np.linspace(180.0, 360.0, 362))
            xyz = np.asarray(self.points['hemisphere_O']) + 4.0 * (np.cos(t)[:, None] * np.array([1.0, 0.0, 0.0]) + np.sin(t)[:, None] * np.array([-0.0, 0.24740395925452296, 0.9689124217106448]))
            c.line(c.project(xyz), clip_on=False, zorder=3, id='hemisphere_contour_part0')
            c.line(c.project([self.points['O'], self.points['T']]), id='height', linestyle=(0, [4, 3]), clip_on=False)
            c.line(c.project([self.points['O'], self.points['R']]), id='radius', linestyle=(0, [4, 3]), clip_on=False)
            c.line(c.project([self.points['right_angle0'], self.points['right_angle1'], self.points['right_angle2']]), id='right_angle', clip_on=False, zorder=3)
            c.text('10 cm', c.project(self.points['height_value_anchor']), offset_pt=[32.5, 0.0], vertex=False, id='height_value')
            c.text('4 cm', c.project(self.points['radius_value_anchor']), offset_pt=[0.0, 51.40980000000001], vertex=False, id='radius_value')
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Solid53().draw(sys.argv[1] if len(sys.argv) > 1 else None))
