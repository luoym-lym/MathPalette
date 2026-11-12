"""Frozen question Solid18; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Solid18:

    def __init__(self):
        self.id = 'Solid18'
        self.source_dataset = 'SOLIDGEO'
        self.source_key = '1807'
        self.question = 'As shown in the figure, the lateral surface of a cylinder unfolds into a rectangle with length $12\\pi$ and width 8. Find the volume of the cylinder.'
        self.answer = '288π'
        self.answer_type = 'number'
        self.query = self.question
        self.points = {'L0': [-6.0, 0.0, 0.0],
         'R0': [6.0, 0.0, 0.0],
         'L1': [-6.0, 0.0, 8.0],
         'R1': [6.0, 0.0, 8.0],
         'O0': [0.0, 0.0, 0.0],
         'O1': [0.0, 0.0, 8.0],
         'netTL': [6.0, 0.0, 8.0],
         'netTR': [43.69911184307752, 0.0, 8.0],
         'netBR': [43.69911184307752, 0.0, 0.0],
         'netBL': [6.0, 0.0, 0.0],
         'label_length': [24.84955592153876, 0.0, 8.0],
         'label_width': [43.69911184307752, 0.0, 4.0]}
        self.subject = 'SolidGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'SolidGeometry' / 'dataset_generator/scenes/Solid18.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('SolidGeometry', self.id, variant, output_path)
        with Canvas(SOLID, xlim=[-7.296061635582195, 47.029217239563664], ylim=[-22.771428460257603, 31.55385041488826], projection=[[1, 0, 0], [0, 0.24192189559966773, 0.9702957262759965]], origin=[0, 0, 0], offset=[0, 0]) as c:
            t = np.radians(np.linspace(0, 180, 721))
            xyz = np.asarray(self.points['O0']) + 6 * (np.cos(t)[:, None] * np.array([1, 0, 0]) + np.sin(t)[:, None] * np.array([0, 1, 0]))
            c.line(c.project(xyz), linestyle=(0, [4, 3]), clip_on=False, id='bottom')
            t = np.radians(np.linspace(180, 360, 721))
            xyz = np.asarray(self.points['O0']) + 6 * (np.cos(t)[:, None] * np.array([1, 0, 0]) + np.sin(t)[:, None] * np.array([0, 1, 0]))
            c.line(c.project(xyz), clip_on=False, zorder=3, id='bottom')
            t = np.radians(np.linspace(0, 360, 721))
            xyz = np.asarray(self.points['O1']) + 6 * (np.cos(t)[:, None] * np.array([1, 0, 0]) + np.sin(t)[:, None] * np.array([0, 1, 0]))
            for object_id, points in [('top', c.project(xyz)), ('L_silhouette', c.project([self.points['L0'], self.points['L1']])), ('R_silhouette', c.project([self.points['R0'], self.points['R1']])), ('net_top', c.project([self.points['netTL'], self.points['netTR']])), ('net_right', c.project([self.points['netTR'], self.points['netBR']])), ('net_bottom', c.project([self.points['netBL'], self.points['netBR']]))]:
                c.line(points, id=object_id, clip_on=False, zorder=3)
            c.text('12π', c.project(self.points['label_length']), offset_pt=[0, 16], vertex=False, id='label_label_length')
            c.text('8', c.project(self.points['label_width']), offset_pt=[15, 0], vertex=False, id='label_label_width')
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Solid18().draw(sys.argv[1] if len(sys.argv) > 1 else None))
