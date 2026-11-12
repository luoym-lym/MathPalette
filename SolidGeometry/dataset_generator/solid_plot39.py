"""Frozen question Solid39; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Solid39:

    def __init__(self):
        self.id = 'Solid39'
        self.source_dataset = 'MathVerse'
        self.source_key = 'testmini:3204'
        self.question = 'Find the volume of the cylinder, rounding your answer to two decimal places.'
        self.answer = '904.78 cm³'
        self.answer_type = 'number'
        self.query = self.question
        self.points = {'O': [0.0, 0.0, 0.0],
         'Q': [0.0, 0.0, 8.0],
         'L': [-6.0, 0.0, 0.0],
         'Ltop': [-6.0, 0.0, 8.0],
         'R': [6.0, 0.0, 0.0],
         'Rtop': [6.0, 0.0, 8.0],
         'radius_value_anchor': [3.0, 0.0, 8.0],
         'height_value_anchor': [6.0, 0.0, 4.0]}
        self.subject = 'SolidGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'SolidGeometry' / 'dataset_generator/scenes/Solid39.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('SolidGeometry', self.id, variant, output_path)
        with Canvas(SOLID, xlim=[-6.345808964098487, 7.727327384843764], ylim=[-3.151211216711973, 10.921925132230278], projection=[[1, 0, 0], [0, 0.23770262642713458, 0.9713379748520297]], origin=[0, 0, 0], offset=[0, 0]) as c:
            c.line(c.project([self.points['L'], self.points['Ltop']]), id='silhouette_L', clip_on=False, zorder=3)
            c.line(c.project([self.points['R'], self.points['Rtop']]), id='silhouette_R', clip_on=False, zorder=3)
            t = np.radians(np.linspace(0.0, 360.0, 722))
            xyz = np.asarray(self.points['Q']) + 6.0 * (np.cos(t)[:, None] * np.array([1.0, 0.0, 0.0]) + np.sin(t)[:, None] * np.array([0.0, 1.0, 0.0]))
            c.line(c.project(xyz), clip_on=False, zorder=3, id='upper_rim')
            t = np.radians(np.linspace(180.0, 360.0, 362))
            xyz = np.asarray(self.points['O']) + 6.0 * (np.cos(t)[:, None] * np.array([1.0, 0.0, 0.0]) + np.sin(t)[:, None] * np.array([0.0, 1.0, 0.0]))
            c.line(c.project(xyz), clip_on=False, zorder=3, id='lower_rim')
            c.line(c.project([self.points['Q'], self.points['Rtop']]), id='radius', clip_on=False, zorder=3)
            c.text('6 cm', c.project(self.points['radius_value_anchor']), offset_pt=[0, 15], vertex=False, id='radius_value')
            c.text('8 cm', c.project(self.points['height_value_anchor']), offset_pt=[12, 0], vertex=False, ha='left', id='height_value')
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Solid39().draw(sys.argv[1] if len(sys.argv) > 1 else None))
