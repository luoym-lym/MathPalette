"""Frozen question Solid26; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Solid26:

    def __init__(self):
        self.id = 'Solid26'
        self.source_dataset = 'MathVerse'
        self.source_key = 'testmini:559'
        self.question = 'As shown in the figure, AO is the height of the cone, then the length of AO is ()\nChoices:\nA:2.4\nB:2.2\nC:1.8\nD:1.6'
        self.answer = 'A'
        self.answer_type = 'choice'
        self.choices = {'A': '2.4', 'B': '2.2', 'C': '1.8', 'D': '1.6'}
        self.query = self.question
        self.points = {'T': [0.0, 0.0, 2.4],
         'O': [0.0, 0.0, 0.0],
         'R': [0.7, 0.0, 0.0],
         'L': [-0.7, 0.0, 0.0],
         'TR': [0.698056030965345, 0.052132308915961566, 0.0],
         'TL': [-0.698056030965345, 0.05213230891596165, 0.0],
         'slant_value_anchor': [0.3490280154826725, 0.026066154457980783, 1.2],
         'source_right_angle0': [0.06980560309653451, 0.005213230891596157, 0.0],
         'source_right_angle1': [0.06980560309653451, 0.005213230891596157, 0.07],
         'source_right_angle2': [0.0, 0.0, 0.07],
         'radius_measure_anchor': [0.3490280154826725, 0.026066154457980783, 0.0]}
        self.subject = 'SolidGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'SolidGeometry' / 'dataset_generator/scenes/Solid26.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('SolidGeometry', self.id, variant, output_path)
        with Canvas(SOLID, xlim=[-1.3685749389739248, 1.4629605034771698], ylim=[-0.30796273444041056, 2.523572708010684], projection=[[1, 0, 0], [0, 0.24740395925452294, 0.9689124217106447]], origin=[0, 0, 0], offset=[0, 0]) as c:
            c.line(c.project([self.points['T'], self.points['TR']]), id='silhouette_TR', clip_on=False, zorder=3)
            c.line(c.project([self.points['T'], self.points['TL']]), id='silhouette_TL', clip_on=False, zorder=3)
            t = np.radians(np.linspace(4.271041972858761, 175.72895802714123, 344))
            xyz = np.asarray(self.points['O']) + 0.7 * (np.cos(t)[:, None] * np.array([1.0, 0.0, 0.0]) + np.sin(t)[:, None] * np.array([0.0, 1.0, 0.0]))
            c.line(c.project(xyz), linestyle=(0, [4, 3]), clip_on=False, id='base_rim')
            t = np.radians(np.linspace(175.72895802714123, 364.27104197285877, 379))
            xyz = np.asarray(self.points['O']) + 0.7 * (np.cos(t)[:, None] * np.array([1.0, 0.0, 0.0]) + np.sin(t)[:, None] * np.array([0.0, 1.0, 0.0]))
            c.line(c.project(xyz), clip_on=False, zorder=3, id='base_rim')
            c.line(c.project([self.points['O'], self.points['T']]), id='axis', linestyle=(0, [4, 3]), clip_on=False)
            c.line(c.project([self.points['O'], self.points['TR']]), id='source_radius', linestyle=(0, [4, 3]), clip_on=False)
            c.line(c.project([self.points['source_right_angle0'], self.points['source_right_angle1'], self.points['source_right_angle2']]), id='source_right_angle', clip_on=False, zorder=3)
            c.text('2.5', c.project(self.points['slant_value_anchor']), offset_pt=[18, 0], vertex=False, ha='left', id='slant_value')
            c.text('0.7', c.project(self.points['radius_measure_anchor']), offset_pt=[0.0, -39.54600000000001], vertex=False, id='radius_measure')
            c.text('A', c.project(self.points['T']), offset_pt=[0, 15], vertex=True, id='vertex_A')
            c.text('O', c.project(self.points['O']), offset_pt=[-12, -10], vertex=True, id='vertex_O')
            c.text('B', c.project(self.points['TR']), offset_pt=[12, -10], vertex=True, id='vertex_B')
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Solid26().draw(sys.argv[1] if len(sys.argv) > 1 else None))
