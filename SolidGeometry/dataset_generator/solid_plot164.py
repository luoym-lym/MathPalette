"""Frozen question Solid164; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Solid164:

    def __init__(self):
        self.id = 'Solid164'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:1389'
        self.question = 'The diagram shows a decision-die in three different positions. What is the probability of obtaining a "YES" when this die is rolled once?\nChoices:\nA:$\\frac{1}{3}$\nB:$\\frac{1}{2}$\nC:$\\frac{5}{9}$\nD:$\\frac{2}{3}$\nE:$\\frac{5}{6}$'
        self.answer = 'B'
        self.answer_type = 'choice'
        self.choices = {'A': '$\\frac{1}{3}$', 'B': '$\\frac{1}{2}$', 'C': '$\\frac{5}{9}$', 'D': '$\\frac{2}{3}$', 'E': '$\\frac{5}{6}$'}
        self.query = self.question
        self._geometry_01 = [('cube0_(np.float64(0.0), np.float64(0.0), np.float64(0.0))_0', [[0.0, 0.0], [1.0, 0.3]]),
         ('cube0_(np.float64(0.0), np.float64(0.0), np.float64(0.0))_1', [[0.0, 0.0], [-0.6, 0.4]]),
         ('cube0_(np.float64(0.0), np.float64(0.0), np.float64(0.0))_2', [[0.0, 0.0], [0.0, 1.0]]),
         ('cube0_(np.float64(0.0), np.float64(0.0), np.float64(1.0))_0', [[0.0, 1.0], [1.0, 1.3]]),
         ('cube0_(np.float64(0.0), np.float64(0.0), np.float64(1.0))_1', [[0.0, 1.0], [-0.6, 1.4]]),
         ('cube0_(np.float64(0.0), np.float64(1.0), np.float64(0.0))_2', [[-0.6, 0.4], [-0.6, 1.4]]),
         ('cube0_(np.float64(0.0), np.float64(1.0), np.float64(1.0))_0', [[-0.6, 1.4], [0.4, 1.7]]),
         ('cube0_(np.float64(1.0), np.float64(0.0), np.float64(0.0))_2', [[1.0, 0.3], [1.0, 1.3]]),
         ('cube0_(np.float64(1.0), np.float64(0.0), np.float64(1.0))_1', [[1.0, 1.3], [0.4, 1.7]]),
         ('cube1_(np.float64(0.0), np.float64(0.0), np.float64(0.0))_0',
          [[2.1, 5.551115123125783e-17], [3.1000000000000005, 0.3000000000000001]]),
         ('cube1_(np.float64(0.0), np.float64(0.0), np.float64(0.0))_1',
          [[2.1, 5.551115123125783e-17], [1.5000000000000002, 0.4000000000000001]]),
         ('cube1_(np.float64(0.0), np.float64(0.0), np.float64(0.0))_2',
          [[2.1, 5.551115123125783e-17], [2.1, 1.0]]),
         ('cube1_(np.float64(0.0), np.float64(0.0), np.float64(1.0))_0',
          [[2.1, 1.0], [3.1000000000000005, 1.3]]),
         ('cube1_(np.float64(0.0), np.float64(0.0), np.float64(1.0))_1',
          [[2.1, 1.0], [1.5000000000000002, 1.4000000000000001]]),
         ('cube1_(np.float64(0.0), np.float64(1.0), np.float64(0.0))_2',
          [[1.5000000000000002, 0.4000000000000001], [1.5000000000000002, 1.4000000000000001]]),
         ('cube1_(np.float64(0.0), np.float64(1.0), np.float64(1.0))_0',
          [[1.5000000000000002, 1.4000000000000001], [2.5000000000000004, 1.7000000000000002]]),
         ('cube1_(np.float64(1.0), np.float64(0.0), np.float64(0.0))_2',
          [[3.1000000000000005, 0.3000000000000001], [3.1000000000000005, 1.3]]),
         ('cube1_(np.float64(1.0), np.float64(0.0), np.float64(1.0))_1',
          [[3.1000000000000005, 1.3], [2.5000000000000004, 1.7000000000000002]]),
         ('cube2_(np.float64(0.0), np.float64(0.0), np.float64(0.0))_0',
          [[4.2, 1.1102230246251565e-16], [5.200000000000001, 0.30000000000000016]]),
         ('cube2_(np.float64(0.0), np.float64(0.0), np.float64(0.0))_1',
          [[4.2, 1.1102230246251565e-16], [3.6000000000000005, 0.40000000000000013]]),
         ('cube2_(np.float64(0.0), np.float64(0.0), np.float64(0.0))_2',
          [[4.2, 1.1102230246251565e-16], [4.2, 1.0000000000000002]]),
         ('cube2_(np.float64(0.0), np.float64(0.0), np.float64(1.0))_0',
          [[4.2, 1.0000000000000002], [5.200000000000001, 1.3000000000000003]]),
         ('cube2_(np.float64(0.0), np.float64(0.0), np.float64(1.0))_1',
          [[4.2, 1.0000000000000002], [3.6000000000000005, 1.4000000000000001]]),
         ('cube2_(np.float64(0.0), np.float64(1.0), np.float64(0.0))_2',
          [[3.6000000000000005, 0.40000000000000013], [3.6000000000000005, 1.4000000000000001]]),
         ('cube2_(np.float64(0.0), np.float64(1.0), np.float64(1.0))_0',
          [[3.6000000000000005, 1.4000000000000001], [4.6000000000000005, 1.7000000000000002]]),
         ('cube2_(np.float64(1.0), np.float64(0.0), np.float64(0.0))_2',
          [[5.200000000000001, 0.30000000000000016], [5.200000000000001, 1.3000000000000003]]),
         ('cube2_(np.float64(1.0), np.float64(0.0), np.float64(1.0))_1',
          [[5.200000000000001, 1.3000000000000003], [4.6000000000000005, 1.7000000000000002]])]
        self.subject = 'SolidGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'SolidGeometry' / 'dataset_generator/scenes/Solid164.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('SolidGeometry', self.id, variant, output_path)
        with Canvas(SOLID, xlim=[-0.7444499195366978, 5.353231411784761], ylim=[-2.2032314117847607, 3.894449919536698], axes_position=[0.05, 0.05, 0.9, 0.9], coordinate_axes=False) as c:
            for object_id, points in self._geometry_01:
                c.line(points, id=object_id, zorder=3, clip_on=False)
            c.text('no', [0.2, 1.35], id='word0_0', rotation=326.30993247402023, rotation_mode='anchor', offset_pt=[0, 0], annotation_clip=None)
            c.text('YES', [-0.3, 0.7], id='word0_1', rotation=326.30993247402023, rotation_mode='anchor', offset_pt=[0, 0], annotation_clip=None)
            c.text('YES', [0.5, 0.65], id='word0_2', rotation=90.0, rotation_mode='anchor', offset_pt=[0, 0], annotation_clip=None)
            c.text('YES', [2.3000000000000003, 1.35], id='word1_0', rotation=146.30993247402023, rotation_mode='anchor', offset_pt=[0, 0], annotation_clip=None)
            c.text('YES', [1.8000000000000003, 0.7000000000000001], id='word1_1', rotation=90.0, rotation_mode='anchor', offset_pt=[0, 0], annotation_clip=None)
            c.text('maybe', [2.6000000000000005, 0.6500000000000001], id='word1_2', rotation=52.43140797117251, rotation_mode='anchor', offset_pt=[0, 0], annotation_clip=None)
            c.text('no', [4.4, 1.35], id='word2_0', rotation=326.30993247402023, rotation_mode='anchor', offset_pt=[0, 0], annotation_clip=None)
            c.text('YES', [3.9000000000000004, 0.7000000000000002], id='word2_1', rotation=146.30993247402023, rotation_mode='anchor', offset_pt=[0, 0], annotation_clip=None)
            c.text('no', [4.7, 0.65], id='word2_2', rotation=16.69924423399362, rotation_mode='anchor', offset_pt=[0, 0], annotation_clip=None)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Solid164().draw(sys.argv[1] if len(sys.argv) > 1 else None))
