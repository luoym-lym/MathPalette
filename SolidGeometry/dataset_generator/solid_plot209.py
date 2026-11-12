"""Frozen question Solid209; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Solid209:

    def __init__(self):
        self.id = 'Solid209'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:2098'
        self.question = 'Two spheres with radii $36$ and one sphere with radius $13$ are each externally tangent to the other two spheres and to two different planes $\\mathcal{P}$ and $\\mathcal{Q}$. The intersection of planes $\\mathcal{P}$ and $\\mathcal{Q}$ is the line $\\ell$. The distance from line $\\ell$ to the point where the sphere with radius $13$ is tangent to plane $\\mathcal{P}$ is $\\frac{m}{n}$, where $m$ and $n$ are relatively prime positive integers. Find $m + n$.'
        self.answer = '335'
        self.answer_type = 'number'
        self.query = self.question
        self.points = {'rear': [-36.0, 37.56521739130435, 36.0],
         'front': [36.0, 37.56521739130435, 36.0],
         'small': [0.0, 13.565217391304348, 13.0],
         'planeP0_0a': [-100.0, -0.4253393665158366, -9.990950226244344],
         'planeP0_0b': [100.0, -0.4253393665158366, -9.990950226244344],
         'planeP1_0a': [100.0, -0.4253393665158366, -9.990950226244344],
         'planeP1_0b': [100.0, 5.529411764705875, 129.88235294117646],
         'planeP2_0a': [100.0, 5.529411764705875, 129.88235294117646],
         'planeP2_0b': [-100.0, 5.529411764705875, 129.88235294117646],
         'planeP3_0a': [-100.0, 5.529411764705875, 129.88235294117646],
         'planeP3_0b': [-100.0, -0.4253393665158365, -9.990950226244337],
         'planeQ0_0a': [-130, -30, 0],
         'planeQ0_0b': [100, -30, 0],
         'planeQ1_0a': [100, -30, 0],
         'planeQ1_0b': [100, 150, 0],
         'planeQ2_0a': [100, 150, 0],
         'planeQ2_0b': [-130, 150, 0],
         'planeQ3_0a': [-130, 150, 0],
         'planeQ3_0b': [-130.0, 126.73050469821682, 0.0],
         'planeQ3_1a': [-130.0, 49.199930084391895, 0.0],
         'planeQ3_1b': [-130, -30, 0],
         'ell0a': [-100.0, 0.0, 0.0],
         'ell0b': [100.0, 0.0, 0.0],
         'pLabel': [-83.0, 4.891402714932121, 114.89592760180996],
         'qLabel': [77, 130, 0],
         'ellLabel': [-30, 0, 0]}
        self.subject = 'SolidGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'SolidGeometry' / 'dataset_generator/scenes/Solid209.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('SolidGeometry', self.id, variant, output_path)
        with Canvas(SOLID, xlim=[-96.59926610432012, 186.4804933702893], ylim=[-86.08584851140029, 196.99391096320915], projection=[[0.4902612396325589, 0.8715755371245493, 0.0], [-0.34819524248474293, 0.19585982389766787, 0.9167327868543622]], origin=[0, 0, 0], offset=[0, 0]) as c:
            for object_id, points in [('line_0', c.project([self.points['planeP0_0a'], self.points['planeP0_0b']])), ('line_1', c.project([self.points['planeP1_0a'], self.points['planeP1_0b']])), ('line_2', c.project([self.points['planeP2_0a'], self.points['planeP2_0b']])), ('line_3', c.project([self.points['planeP3_0a'], self.points['planeP3_0b']])), ('line_4', c.project([self.points['planeQ0_0a'], self.points['planeQ0_0b']])), ('line_5', c.project([self.points['planeQ1_0a'], self.points['planeQ1_0b']])), ('line_6', c.project([self.points['planeQ2_0a'], self.points['planeQ2_0b']])), ('line_7', c.project([self.points['planeQ3_0a'], self.points['planeQ3_0b']])), ('line_8', c.project([self.points['planeQ3_1a'], self.points['planeQ3_1b']])), ('line_9', c.project([self.points['ell0a'], self.points['ell0b']]))]:
                c.line(points, id=object_id, clip_on=False, zorder=3)
            t = np.radians(np.linspace(17.651614069550792, 245.37123396197666, 716))
            xyz = np.asarray(self.points['rear']) + 36 * (np.cos(t)[:, None] * np.array([0.4902612396325589, 0.8715755371245493, 0.0]) + np.sin(t)[:, None] * np.array([-0.34819524248474293, 0.19585982389766787, 0.9167327868543622]))
            c.line(c.project(xyz), clip_on=False, zorder=3, id='rear_silhouette0')
            t = np.radians(np.linspace(240.64224643984758, 332.1121323445899, 288))
            xyz = np.asarray(self.points['rear']) + 36 * (np.cos(t)[:, None] * np.array([1, 0, 0]) + np.sin(t)[:, None] * np.array([0, 1, 0]))
            c.line(c.project(xyz), clip_on=False, zorder=3, id='rear_equator0')
            t = np.radians(np.linspace(0.0, 360.0, 1131))
            xyz = np.asarray(self.points['front']) + 36 * (np.cos(t)[:, None] * np.array([0.4902612396325589, 0.8715755371245493, 0.0]) + np.sin(t)[:, None] * np.array([-0.34819524248474293, 0.19585982389766787, 0.9167327868543622]))
            c.line(c.project(xyz), clip_on=False, zorder=3, id='front_silhouette0')
            t = np.radians(np.linspace(0.0, 60.64224647456982, 191))
            xyz = np.asarray(self.points['front']) + 36 * (np.cos(t)[:, None] * np.array([1, 0, 0]) + np.sin(t)[:, None] * np.array([0, 1, 0]))
            c.line(c.project(xyz), clip_on=False, zorder=3, id='front_equator0')
            t = np.radians(np.linspace(240.64224643984758, 360.0, 375))
            xyz = np.asarray(self.points['front']) + 36 * (np.cos(t)[:, None] * np.array([1, 0, 0]) + np.sin(t)[:, None] * np.array([0, 1, 0]))
            c.line(c.project(xyz), clip_on=False, zorder=3, id='front_equator1')
            t = np.radians(np.linspace(78.59440220744605, 319.32775894545887, 757))
            xyz = np.asarray(self.points['small']) + 13 * (np.cos(t)[:, None] * np.array([0.4902612396325589, 0.8715755371245493, 0.0]) + np.sin(t)[:, None] * np.array([-0.34819524248474293, 0.19585982389766787, 0.9167327868543622]))
            c.line(c.project(xyz), clip_on=False, zorder=3, id='small_silhouette0')
            t = np.radians(np.linspace(0.0, 4.036770367295132, 13))
            xyz = np.asarray(self.points['small']) + 13 * (np.cos(t)[:, None] * np.array([1, 0, 0]) + np.sin(t)[:, None] * np.array([0, 1, 0]))
            c.line(c.project(xyz), clip_on=False, zorder=3, id='small_equator0')
            t = np.radians(np.linspace(240.64224640913187, 360.0, 375))
            xyz = np.asarray(self.points['small']) + 13 * (np.cos(t)[:, None] * np.array([1, 0, 0]) + np.sin(t)[:, None] * np.array([0, 1, 0]))
            c.line(c.project(xyz), clip_on=False, zorder=3, id='small_equator1')
            c.text('P', c.project(self.points['pLabel']), offset_pt=[0, 0], vertex=True, id='label_0')
            c.text('Q', c.project(self.points['qLabel']), offset_pt=[0, 0], vertex=True, id='label_1')
            c.text('ℓ', c.project(self.points['ellLabel']), offset_pt=[0, 20], vertex=True, id='label_2')
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Solid209().draw(sys.argv[1] if len(sys.argv) > 1 else None))
