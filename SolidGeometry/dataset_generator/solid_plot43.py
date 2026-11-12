"""Frozen question Solid43; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Solid43:

    def __init__(self):
        self.id = 'Solid43'
        self.source_dataset = 'MathVerse'
        self.source_key = 'testmini:3229'
        self.question = 'Find the volume of the cone pictured here.\n\n(Give your answer correct to 1 decimal place.)'
        self.answer = '220.0 cm³'
        self.answer_type = 'number'
        self.query = self.question
        self.points = {'T': [0.0, 0.0, 12.5],
         'O': [0.0, 0.0, 0.0],
         'R': [4.1, 0.0, 0.0],
         'L': [-4.1, 0.0, 0.0],
         'TR': [4.085595128637212, 0.34338381565804954, 0.0],
         'TL': [-4.085595128637212, 0.34338381565805076, 0.0],
         'right_angle0': [0.49199999999999994, 0.0, 0.0],
         'right_angle1': [0.49199999999999994, 0.0, 0.49199999999999994],
         'right_angle2': [0.0, 0.0, 0.49199999999999994],
         'radius_value_anchor': [2.05, 0.0, 0.0],
         'height_value_anchor': [0, 0, 3.75]}
        self.subject = 'SolidGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'SolidGeometry' / 'dataset_generator/scenes/Solid43.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('SolidGeometry', self.id, variant, output_path)
        with Canvas(SOLID, xlim=[-6.887827307435129, 6.887827307435129], ylim=[-1.3392792572773642, 12.436375357592894], projection=[[1, 0, 0], [0, 0.24740395925452294, 0.9689124217106447]], origin=[0, 0, 0], offset=[0, 0]) as c:
            c.line(c.project([self.points['T'], self.points['TR']]), id='silhouette_TR', clip_on=False, zorder=3)
            c.line(c.project([self.points['T'], self.points['TL']]), id='silhouette_TL', clip_on=False, zorder=3)
            t = np.radians(np.linspace(4.804272465113954, 175.19572753488603, 342))
            xyz = np.asarray(self.points['O']) + 4.1 * (np.cos(t)[:, None] * np.array([1.0, 0.0, 0.0]) + np.sin(t)[:, None] * np.array([0.0, 1.0, 0.0]))
            c.line(c.project(xyz), linestyle=(0, [4, 3]), clip_on=False, id='base_rim')
            t = np.radians(np.linspace(175.19572753488603, 364.80427246511397, 381))
            xyz = np.asarray(self.points['O']) + 4.1 * (np.cos(t)[:, None] * np.array([1.0, 0.0, 0.0]) + np.sin(t)[:, None] * np.array([0.0, 1.0, 0.0]))
            c.line(c.project(xyz), clip_on=False, zorder=3, id='base_rim')
            c.line(c.project([self.points['O'], self.points['T']]), id='axis', linestyle=(0, [4, 3]), clip_on=False)
            c.line(c.project([self.points['O'], self.points['R']]), id='radius', linestyle=(0, [4, 3]), clip_on=False)
            c.line(c.project([self.points['right_angle0'], self.points['right_angle1'], self.points['right_angle2']]), id='right_angle', clip_on=False, zorder=3)
            c.text('4.1 cm', c.project(self.points['radius_value_anchor']), offset_pt=[0, -16], vertex=False, id='radius_value')
            c.text('12.5 cm', c.project(self.points['height_value_anchor']), offset_pt=[-12, 0], vertex=False, ha='right', id='height_value')
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Solid43().draw(sys.argv[1] if len(sys.argv) > 1 else None))
