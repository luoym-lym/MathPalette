"""Frozen question Solid31; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Solid31:

    def __init__(self):
        self.id = 'Solid31'
        self.source_dataset = 'MathVerse'
        self.source_key = 'testmini:599'
        self.question = 'Find the area of the circular base of the cone shown. All lengths shown are in centimetres.\nChoices:\nA:3πcm^{2}\nB:9πcm^{2}\nC:16πcm^{2}\nD:25πcm^{2}'
        self.answer = 'B'
        self.answer_type = 'choice'
        self.choices = {'A': '3πcm^{2}', 'B': '9πcm^{2}', 'C': '16πcm^{2}', 'D': '25πcm^{2}'}
        self.query = self.question
        self.points = {'T': [0.0, 0.0, 4.0],
         'O': [0.0, 0.0, 0.0],
         'R': [3.0, 0.0, 0.0],
         'L': [-3.0, 0.0, 0.0],
         'TR': [2.9444740698111005, 0.5745193227473316, 0.0],
         'TL': [-2.9444740698111005, 0.574519322747332, 0.0],
         'height_value_anchor': [0.0, 0.0, 2.0],
         'slant_value_anchor': [1.4722370349055502, 0.2872596613736658, 2.0]}
        self.subject = 'SolidGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'SolidGeometry' / 'dataset_generator/scenes/Solid31.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('SolidGeometry', self.id, variant, output_path)
        with Canvas(SOLID, xlim=[-3.1485909270146926, 3.1485909270146926], ylim=[-1.5818856795597471, 4.715296174469638], projection=[[1, 0, 0], [0, 0.24740395925452294, 0.9689124217106447]], origin=[0, 0, 0], offset=[0, 0]) as c:
            c.line(c.project([self.points['T'], self.points['TR']]), id='silhouette_TR', clip_on=False, zorder=3)
            c.line(c.project([self.points['T'], self.points['TL']]), id='silhouette_TL', clip_on=False, zorder=3)
            t = np.radians(np.linspace(11.040711432694145, 168.95928856730586, 317))
            xyz = np.asarray(self.points['O']) + 3.0 * (np.cos(t)[:, None] * np.array([1.0, 0.0, 0.0]) + np.sin(t)[:, None] * np.array([0.0, 1.0, 0.0]))
            c.line(c.project(xyz), linestyle=(0, [4, 3]), clip_on=False, id='base_rim')
            t = np.radians(np.linspace(168.95928856730586, 371.04071143269414, 406))
            xyz = np.asarray(self.points['O']) + 3.0 * (np.cos(t)[:, None] * np.array([1.0, 0.0, 0.0]) + np.sin(t)[:, None] * np.array([0.0, 1.0, 0.0]))
            c.line(c.project(xyz), clip_on=False, zorder=3, id='base_rim')
            c.line(c.project([self.points['O'], self.points['T']]), id='axis', linestyle=(0, [4, 3]), clip_on=False)
            c.line(c.project([self.points['O'], self.points['R']]), id='radius', linestyle=(0, [4, 3]), clip_on=False)
            c.text('4', c.project(self.points['height_value_anchor']), offset_pt=[-12, 0], vertex=False, ha='right', id='height_value')
            c.text('5', c.project(self.points['slant_value_anchor']), offset_pt=[18, 0], vertex=False, ha='left', id='slant_value')
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Solid31().draw(sys.argv[1] if len(sys.argv) > 1 else None))
