"""Frozen question Solid41; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Solid41:

    def __init__(self):
        self.id = 'Solid41'
        self.source_dataset = 'MathVerse'
        self.source_key = 'testmini:3219'
        self.question = 'Find the volume of the cone shown. \n\nRound your answer to two decimal places.'
        self.answer = '32.45 cm³'
        self.answer_type = 'number'
        self.query = self.question
        self.points = {'T': [0.0, 0.0, 7.745966692414834],
         'O': [0.0, 0.0, 0.0],
         'R': [2.0, 0.0, 0.0],
         'L': [-2.0, 0.0, 0.0],
         'TR': [1.9956486332864076, 0.13185800113035728, 0.0],
         'TL': [-1.9956486332864076, 0.1318580011303568, 0.0],
         'radius_value_anchor': [1.0, 0.0, 0.0],
         'slant_value_anchor': [0.9978243166432038, 0.06592900056517864, 3.872983346207417]}
        self.subject = 'SolidGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'SolidGeometry' / 'dataset_generator/scenes/Solid41.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('SolidGeometry', self.id, variant, output_path)
        with Canvas(SOLID, xlim=[-4.3316089758671135, 4.3410059411480395], ylim=[-0.9663798130047088, 7.706235104010444], projection=[[1, 0, 0], [0, 0.24740395925452294, 0.9689124217106447]], origin=[0, 0, 0], offset=[0, 0]) as c:
            c.line(c.project([self.points['T'], self.points['TR']]), id='silhouette_TR', clip_on=False, zorder=3)
            c.line(c.project([self.points['T'], self.points['TL']]), id='silhouette_TL', clip_on=False, zorder=3)
            t = np.radians(np.linspace(3.7801953804741815, 176.21980461952583, 346))
            xyz = np.asarray(self.points['O']) + 2.0 * (np.cos(t)[:, None] * np.array([1.0, 0.0, 0.0]) + np.sin(t)[:, None] * np.array([0.0, 1.0, 0.0]))
            c.line(c.project(xyz), linestyle=(0, [4, 3]), clip_on=False, id='base_rim')
            t = np.radians(np.linspace(176.21980461952583, 363.7801953804742, 377))
            xyz = np.asarray(self.points['O']) + 2.0 * (np.cos(t)[:, None] * np.array([1.0, 0.0, 0.0]) + np.sin(t)[:, None] * np.array([0.0, 1.0, 0.0]))
            c.line(c.project(xyz), clip_on=False, zorder=3, id='base_rim')
            c.line(c.project([self.points['O'], self.points['R']]), id='radius', linestyle=(0, [4, 3]), clip_on=False)
            c.text('2 cm', c.project(self.points['radius_value_anchor']), offset_pt=[0, -40], vertex=False, id='radius_value')
            c.text('8 cm', c.project(self.points['slant_value_anchor']), offset_pt=[18, 0], vertex=False, ha='left', id='slant_value')
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Solid41().draw(sys.argv[1] if len(sys.argv) > 1 else None))
