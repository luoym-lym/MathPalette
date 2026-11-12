"""Frozen question Plane86; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane86:

    def __init__(self):
        self.id = 'Plane86'
        self.source_dataset = 'MathVerse'
        self.source_key = 'testmini:194'
        self.question = 'A rectangular strip is folded along the segment joining its upper and lower edges, as shown. The dashed edges show the original position. Find angle 2.\nChoices:\nA:100°\nB:110°\nC:120°\nD:140°'
        self.answer = 'B'
        self.answer_type = 'choice'
        self.choices = {'A': '100°', 'B': '110°', 'C': '120°', 'D': '140°'}
        self.query = self.question
        self.points = {'Q': [0.0, 2.0],
         'R': [0.7279404685324049, 0.0],
         'T': [-3.8302222155948895, -1.2139380484326971],
         'U': [-2.5446469962218106, -2.7460269346706525],
         'P': [-2.3835071851884195, -4.440892098500626e-16],
         'L': [-6.0, 2.0],
         'M': [-6.0, 0.0],
         'V': [5.0, 2.0],
         'W': [5.0, 0.0]}
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane86.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-6.281708977942342, 5.298398927328188], ylim=[-6.16306741997059, 5.417040485299941]) as c:
            for object_id, points in [('segment_0', [self.points['Q'], self.points['L']]), ('segment_1', [self.points['L'], self.points['M']]), ('segment_2', [self.points['M'], self.points['R']]), ('segment_3', [self.points['R'], self.points['Q']]), ('segment_4', [self.points['Q'], self.points['T']]), ('segment_5', [self.points['T'], self.points['U']]), ('segment_6', [self.points['U'], self.points['R']])]:
                c.line(points, id=object_id)
            for object_id, points in [('segment_7', [self.points['Q'], self.points['V']]), ('segment_8', [self.points['V'], self.points['W']]), ('segment_9', [self.points['R'], self.points['W']])]:
                c.line(points, id=object_id, linestyle=(0, [4, 3]))
            center, direction, start, end = self._angle(self.points['M'], self.points['P'], self.points['Q'], reflex=False)
            c.arc(center, 24, start, end, radius_pt=True, id='angle_arc_10')
            center, direction, start, end = self._angle(self.points['Q'], self.points['R'], self.points['W'], reflex=False)
            c.arc(center, 24, start, end, radius_pt=True, id='angle_arc_11')
            center, direction, start, end = self._angle(self.points['M'], self.points['P'], self.points['Q'], reflex=False)
            offset = direction * 70 + np.array([0, 0])
            c.text('1: 140°', center, offset_pt=offset, id='label_0')
            center, direction, start, end = self._angle(self.points['Q'], self.points['R'], self.points['W'], reflex=False)
            offset = direction * 40 + np.array([0, 0])
            c.text('2', center, offset_pt=offset, id='label_1')
            return c if _canvas else c.save(output_path)

    @staticmethod
    def _angle(a, vertex, b, reflex=False):
        center = np.asarray(vertex, dtype=float)
        u, v = (np.asarray(a) - center, np.asarray(b) - center)
        u, v = (u / np.linalg.norm(u), v / np.linalg.norm(v))
        start, end = (np.degrees(np.arctan2(u[1], u[0])), np.degrees(np.arctan2(v[1], v[0])))
        sweep = (end - start) % 360
        if sweep > 180:
            start, sweep = (end, 360 - sweep)
        if reflex:
            start, sweep = (start + sweep, 360 - sweep)
        middle = np.radians(start + sweep / 2)
        return (center, np.array([np.cos(middle), np.sin(middle)]), start, start + sweep)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane86().draw(sys.argv[1] if len(sys.argv) > 1 else None))
