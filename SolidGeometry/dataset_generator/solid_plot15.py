"""Frozen question Solid15; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Solid15:

    def __init__(self):
        self.id = 'Solid15'
        self.source_dataset = 'MathVerse'
        self.source_key = 's3589'
        self.question = 'Consider the two similar spheres shown.\n\n\nFind the volume of Sphere A, in simplest exact form.'
        self.answer = '\\[36\\pi \\mathrm{cm}^3\\]'
        self.answer_type = 'number'
        self.query = self.question
        self.points = {'Oa': [0, 0, 0],
         'Ob': [22, 0, 0],
         'Apole': [0, 0, 3],
         'Bpole': [22, 0, 12],
         'Arim': [2.673019572565104, 0, 1.3619714992186402],
         'Brim': [22, 0, 12],
         'MA': [1.336509786282552, 0, 0.6809857496093201],
         'MB': [22, 0, 6]}
        self.subject = 'SolidGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'SolidGeometry' / 'dataset_generator/scenes/Solid15.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('SolidGeometry', self.id, variant, output_path)
        with Canvas(SOLID, xlim=[-3.918404460055987, 34.93827931538006], ylim=[-18.45290966838932, 20.403774107046726], projection=[[1, 0, 0], [0, 0, 1]], origin=[0, 0, 0], offset=[0, 0]) as c:
            t = np.radians(np.linspace(0, 360, 721))
            xyz = np.asarray(self.points['Oa']) + 3 * (np.cos(t)[:, None] * np.array([1, 0, 0]) + np.sin(t)[:, None] * np.array([0, 0, 1]))
            c.line(c.project(xyz), clip_on=False, zorder=3, id='sphere_A_outline')
            t = np.radians(np.linspace(0, 360, 721))
            xyz = np.asarray(self.points['Ob']) + 12 * (np.cos(t)[:, None] * np.array([1, 0, 0]) + np.sin(t)[:, None] * np.array([0, 0, 1]))
            c.line(c.project(xyz), clip_on=False, zorder=3, id='sphere_B_outline')
            t = np.radians(np.linspace(0, 360, 721))
            xyz = np.asarray(self.points['Oa']) + 3 * (np.cos(t)[:, None] * np.array([0.8910065241883679, 0, 0.45399049973954675]) + np.sin(t)[:, None] * np.array([-0.17251638990102777, 0.9249864863877743, 0.3385824791915798]))
            c.line(c.project(xyz), clip_on=False, zorder=3, id='sphere_A_great_circle')
            t = np.radians(np.linspace(0, 360, 721))
            xyz = np.asarray(self.points['Ob']) + 12 * (np.cos(t)[:, None] * np.array([0, 0, 1]) + np.sin(t)[:, None] * np.array([0.34, 0.9404254356406998, 0]))
            for object_id, points in [('sphere_B_great_circle', c.project(xyz)), ('radius_A', c.project([self.points['Oa'], self.points['Arim']])), ('radius_B', c.project([self.points['Ob'], self.points['Brim']]))]:
                c.line(points, id=object_id, clip_on=False, zorder=3)
            c.text('A', c.project(self.points['Apole']), offset_pt=[0, 18], vertex=False, id='sphere_A')
            c.text('B', c.project(self.points['Bpole']), offset_pt=[0, 18], vertex=False, id='sphere_B')
            c.text('3', c.project(self.points['Oa']), offset_pt=[16, -20], vertex=False, id='radius_3')
            c.text('12', c.project(self.points['Ob']), offset_pt=[0, -15], vertex=False, id='radius_12')
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Solid15().draw(sys.argv[1] if len(sys.argv) > 1 else None))
