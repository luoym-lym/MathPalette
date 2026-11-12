"""Frozen question Plane211; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane211:

    def __init__(self):
        self.id = 'Plane211'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:533'
        self.question = 'Nine points numbered 1 to 9 are marked on a circle. Join point 1 to point 3, then point 3 to point 5, and continue by joining every second point until returning to point 1. Which drawing results?\nChoices:\nA:(A)\nB:(B)\nC:(C)\nD:(D)\nE:(E)'
        self.answer = 'E'
        self.answer_type = 'choice'
        self.choices = {'A': '(A)', 'B': '(B)', 'C': '(C)', 'D': '(D)', 'E': '(E)'}
        self.query = self.question
        self.points = {'p0_1': [9.606969024216347, 10.915111107797445],
         'p0_2': [10.46201938253052, 9.434120444167325],
         'p0_3': [10.165063509461097, 7.75],
         'p0_4': [8.855050358314172, 6.65076844803523],
         'p0_5': [7.1449496416858285, 6.650768448035229],
         'p0_6': [5.834936490538903, 7.75],
         'p0_7': [5.53798061746948, 9.434120444167327],
         'p0_8': [6.393030975783651, 10.915111107797445],
         'p0_9': [7.999999999999999, 11.5],
         'p1_1': [1.6069690242163484, 1.915111107797445],
         'p1_2': [2.46201938253052, 0.4341204441673258],
         'p1_3': [2.165063509461097, -1.2499999999999998],
         'p1_4': [0.8550503583141721, -2.349231551964771],
         'p1_5': [-0.8550503583141718, -2.3492315519647713],
         'p1_6': [-2.165063509461097, -1.2499999999999998],
         'p1_7': [-2.46201938253052, 0.4341204441673262],
         'p1_8': [-1.6069690242163488, 1.9151111077974448],
         'p1_9': [-4.592425496802574e-16, 2.5],
         'p2_1': [9.606969024216347, 1.915111107797445],
         'p2_2': [10.46201938253052, 0.4341204441673258],
         'p2_3': [10.165063509461097, -1.2499999999999998],
         'p2_4': [8.855050358314172, -2.349231551964771],
         'p2_5': [7.1449496416858285, -2.3492315519647713],
         'p2_6': [5.834936490538903, -1.2499999999999998],
         'p2_7': [5.53798061746948, 0.4341204441673262],
         'p2_8': [6.393030975783651, 1.9151111077974448],
         'p2_9': [7.999999999999999, 2.5],
         'p3_1': [17.606969024216347, 1.915111107797445],
         'p3_2': [18.46201938253052, 0.4341204441673258],
         'p3_3': [18.165063509461095, -1.2499999999999998],
         'p3_4': [16.855050358314173, -2.349231551964771],
         'p3_5': [15.144949641685828, -2.3492315519647713],
         'p3_6': [13.834936490538903, -1.2499999999999998],
         'p3_7': [13.53798061746948, 0.4341204441673262],
         'p3_8': [14.39303097578365, 1.9151111077974448],
         'p3_9': [16.0, 2.5],
         'p4_1': [1.6069690242163484, -7.084888892202555],
         'p4_2': [2.46201938253052, -8.565879555832675],
         'p4_3': [2.165063509461097, -10.25],
         'p4_4': [0.8550503583141721, -11.34923155196477],
         'p4_5': [-0.8550503583141718, -11.34923155196477],
         'p4_6': [-2.165063509461097, -10.25],
         'p4_7': [-2.46201938253052, -8.565879555832673],
         'p4_8': [-1.6069690242163488, -7.084888892202555],
         'p4_9': [-4.592425496802574e-16, -6.5],
         'p5_1': [9.606969024216347, -7.084888892202555],
         'p5_2': [10.46201938253052, -8.565879555832675],
         'p5_3': [10.165063509461097, -10.25],
         'p5_4': [8.855050358314172, -11.34923155196477],
         'p5_5': [7.1449496416858285, -11.34923155196477],
         'p5_6': [5.834936490538903, -10.25],
         'p5_7': [5.53798061746948, -8.565879555832673],
         'p5_8': [6.393030975783651, -7.084888892202555],
         'p5_9': [7.999999999999999, -6.5]}
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane211.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-5.316008267806673, 20.575452060892534], ylim=[-12.769582167182557, 13.12187816151665]) as c:
            c.circle([8, 9], 2.5, id='circle0')
            for object_id, points in [('p0_1dot', [self.points['p0_1']]), ('p0_2dot', [self.points['p0_2']]), ('p0_3dot', [self.points['p0_3']]), ('p0_4dot', [self.points['p0_4']]), ('p0_5dot', [self.points['p0_5']]), ('p0_6dot', [self.points['p0_6']]), ('p0_7dot', [self.points['p0_7']]), ('p0_8dot', [self.points['p0_8']]), ('p0_9dot', [self.points['p0_9']])]:
                c.point(points, id=object_id, filled=True)
            c.line([self.points['p0_1'], self.points['p0_3']], id='edge0_0')
            c.line([self.points['p0_3'], self.points['p0_5']], id='edge0_1')
            c.circle([0, 0], 2.5, id='circle1')
            for object_id, points in [('p1_1dot', [self.points['p1_1']]), ('p1_2dot', [self.points['p1_2']]), ('p1_3dot', [self.points['p1_3']]), ('p1_4dot', [self.points['p1_4']]), ('p1_5dot', [self.points['p1_5']]), ('p1_6dot', [self.points['p1_6']]), ('p1_7dot', [self.points['p1_7']]), ('p1_8dot', [self.points['p1_8']]), ('p1_9dot', [self.points['p1_9']])]:
                c.point(points, id=object_id, filled=True)
            for object_id, points in [('edge1_0', [self.points['p1_1'], self.points['p1_3']]), ('edge1_1', [self.points['p1_3'], self.points['p1_5']]), ('edge1_2', [self.points['p1_5'], self.points['p1_6']]), ('edge1_3', [self.points['p1_6'], self.points['p1_8']]), ('edge1_4', [self.points['p1_8'], self.points['p1_1']])]:
                c.line(points, id=object_id)
            c.circle([8, 0], 2.5, id='circle2')
            for object_id, points in [('p2_1dot', [self.points['p2_1']]), ('p2_2dot', [self.points['p2_2']]), ('p2_3dot', [self.points['p2_3']]), ('p2_4dot', [self.points['p2_4']]), ('p2_5dot', [self.points['p2_5']]), ('p2_6dot', [self.points['p2_6']]), ('p2_7dot', [self.points['p2_7']]), ('p2_8dot', [self.points['p2_8']]), ('p2_9dot', [self.points['p2_9']])]:
                c.point(points, id=object_id, filled=True)
            for object_id, points in [('edge2_0', [self.points['p2_1'], self.points['p2_3']]), ('edge2_1', [self.points['p2_3'], self.points['p2_5']]), ('edge2_2', [self.points['p2_5'], self.points['p2_7']]), ('edge2_3', [self.points['p2_7'], self.points['p2_9']]), ('edge2_4', [self.points['p2_9'], self.points['p2_1']])]:
                c.line(points, id=object_id)
            c.circle([16, 0], 2.5, id='circle3')
            for object_id, points in [('p3_1dot', [self.points['p3_1']]), ('p3_2dot', [self.points['p3_2']]), ('p3_3dot', [self.points['p3_3']]), ('p3_4dot', [self.points['p3_4']]), ('p3_5dot', [self.points['p3_5']]), ('p3_6dot', [self.points['p3_6']]), ('p3_7dot', [self.points['p3_7']]), ('p3_8dot', [self.points['p3_8']]), ('p3_9dot', [self.points['p3_9']])]:
                c.point(points, id=object_id, filled=True)
            for object_id, points in [('edge3_0', [self.points['p3_1'], self.points['p3_8']]), ('edge3_1', [self.points['p3_8'], self.points['p3_6']]), ('edge3_2', [self.points['p3_6'], self.points['p3_4']]), ('edge3_3', [self.points['p3_4'], self.points['p3_2']]), ('edge3_4', [self.points['p3_2'], self.points['p3_9']])]:
                c.line(points, id=object_id)
            c.circle([0, -9], 2.5, id='circle4')
            for object_id, points in [('p4_1dot', [self.points['p4_1']]), ('p4_2dot', [self.points['p4_2']]), ('p4_3dot', [self.points['p4_3']]), ('p4_4dot', [self.points['p4_4']]), ('p4_5dot', [self.points['p4_5']]), ('p4_6dot', [self.points['p4_6']]), ('p4_7dot', [self.points['p4_7']]), ('p4_8dot', [self.points['p4_8']]), ('p4_9dot', [self.points['p4_9']])]:
                c.point(points, id=object_id, filled=True)
            for object_id, points in [('edge4_0', [self.points['p4_8'], self.points['p4_6']]), ('edge4_1', [self.points['p4_6'], self.points['p4_4']]), ('edge4_2', [self.points['p4_4'], self.points['p4_2']]), ('edge4_3', [self.points['p4_2'], self.points['p4_9']]), ('edge4_4', [self.points['p4_9'], self.points['p4_4']]), ('edge4_5', [self.points['p4_4'], self.points['p4_8']])]:
                c.line(points, id=object_id)
            c.circle([8, -9], 2.5, id='circle5')
            for object_id, points in [('p5_1dot', [self.points['p5_1']]), ('p5_2dot', [self.points['p5_2']]), ('p5_3dot', [self.points['p5_3']]), ('p5_4dot', [self.points['p5_4']]), ('p5_5dot', [self.points['p5_5']]), ('p5_6dot', [self.points['p5_6']]), ('p5_7dot', [self.points['p5_7']]), ('p5_8dot', [self.points['p5_8']]), ('p5_9dot', [self.points['p5_9']])]:
                c.point(points, id=object_id, filled=True)
            for object_id, points in [('edge5_0', [self.points['p5_1'], self.points['p5_3']]), ('edge5_1', [self.points['p5_3'], self.points['p5_5']]), ('edge5_2', [self.points['p5_5'], self.points['p5_7']]), ('edge5_3', [self.points['p5_7'], self.points['p5_9']]), ('edge5_4', [self.points['p5_9'], self.points['p5_2']]), ('edge5_5', [self.points['p5_2'], self.points['p5_4']]), ('edge5_6', [self.points['p5_4'], self.points['p5_6']]), ('edge5_7', [self.points['p5_6'], self.points['p5_8']]), ('edge5_8', [self.points['p5_8'], self.points['p5_1']])]:
                c.line(points, id=object_id)
            c.text('1', self.points['p0_1'], offset_pt=[8.356238925925012, 9.958577760546714], vertex=False, id='p0_1label')
            c.text('2', self.points['p0_2'], offset_pt=[12.802500789158705, 2.257426309670094], vertex=False, id='p0_2label')
            c.text('3', self.points['p0_3'], offset_pt=[11.258330249197703, -6.499999999999999], vertex=False, id='p0_3label')
            c.text('4', self.points['p0_4'], offset_pt=[4.446261863233695, -12.216004070216808], vertex=False, id='p0_4label')
            c.text('5', self.points['p0_5'], offset_pt=[-4.446261863233693, -12.21600407021681], vertex=False, id='p0_5label')
            c.text('6', self.points['p0_6'], offset_pt=[-11.258330249197703, -6.499999999999999], vertex=False, id='p0_6label')
            c.text('7', self.points['p0_7'], offset_pt=[-12.802500789158705, 2.257426309670096], vertex=False, id='p0_7label')
            c.text('8', self.points['p0_8'], offset_pt=[-8.356238925925012, 9.958577760546714], vertex=False, id='p0_8label')
            c.text('9', self.points['p0_9'], offset_pt=[-2.3880612583373385e-15, 13.0], vertex=False, id='p0_9label')
            c.text('1', self.points['p1_1'], offset_pt=[8.356238925925012, 9.958577760546714], vertex=False, id='p1_1label')
            c.text('2', self.points['p1_2'], offset_pt=[12.802500789158705, 2.257426309670094], vertex=False, id='p1_2label')
            c.text('3', self.points['p1_3'], offset_pt=[11.258330249197703, -6.499999999999999], vertex=False, id='p1_3label')
            c.text('4', self.points['p1_4'], offset_pt=[4.446261863233695, -12.216004070216808], vertex=False, id='p1_4label')
            c.text('5', self.points['p1_5'], offset_pt=[-4.446261863233693, -12.21600407021681], vertex=False, id='p1_5label')
            c.text('6', self.points['p1_6'], offset_pt=[-11.258330249197703, -6.499999999999999], vertex=False, id='p1_6label')
            c.text('7', self.points['p1_7'], offset_pt=[-12.802500789158705, 2.257426309670096], vertex=False, id='p1_7label')
            c.text('8', self.points['p1_8'], offset_pt=[-8.356238925925012, 9.958577760546714], vertex=False, id='p1_8label')
            c.text('9', self.points['p1_9'], offset_pt=[-2.3880612583373385e-15, 13.0], vertex=False, id='p1_9label')
            c.text('(A)', [-3.5, -2.2], offset_pt=[0, 0], vertex=False, id='label18')
            c.text('1', self.points['p2_1'], offset_pt=[8.356238925925012, 9.958577760546714], vertex=False, id='p2_1label')
            c.text('2', self.points['p2_2'], offset_pt=[12.802500789158705, 2.257426309670094], vertex=False, id='p2_2label')
            c.text('3', self.points['p2_3'], offset_pt=[11.258330249197703, -6.499999999999999], vertex=False, id='p2_3label')
            c.text('4', self.points['p2_4'], offset_pt=[4.446261863233695, -12.216004070216808], vertex=False, id='p2_4label')
            c.text('5', self.points['p2_5'], offset_pt=[-4.446261863233693, -12.21600407021681], vertex=False, id='p2_5label')
            c.text('6', self.points['p2_6'], offset_pt=[-11.258330249197703, -6.499999999999999], vertex=False, id='p2_6label')
            c.text('7', self.points['p2_7'], offset_pt=[-12.802500789158705, 2.257426309670096], vertex=False, id='p2_7label')
            c.text('8', self.points['p2_8'], offset_pt=[-8.356238925925012, 9.958577760546714], vertex=False, id='p2_8label')
            c.text('9', self.points['p2_9'], offset_pt=[-2.3880612583373385e-15, 13.0], vertex=False, id='p2_9label')
            c.text('(B)', [4.5, -2.2], offset_pt=[0, 0], vertex=False, id='label28')
            c.text('1', self.points['p3_1'], offset_pt=[8.356238925925012, 9.958577760546714], vertex=False, id='p3_1label')
            c.text('2', self.points['p3_2'], offset_pt=[12.802500789158705, 2.257426309670094], vertex=False, id='p3_2label')
            c.text('3', self.points['p3_3'], offset_pt=[11.258330249197703, -6.499999999999999], vertex=False, id='p3_3label')
            c.text('4', self.points['p3_4'], offset_pt=[4.446261863233695, -12.216004070216808], vertex=False, id='p3_4label')
            c.text('5', self.points['p3_5'], offset_pt=[-4.446261863233693, -12.21600407021681], vertex=False, id='p3_5label')
            c.text('6', self.points['p3_6'], offset_pt=[-11.258330249197703, -6.499999999999999], vertex=False, id='p3_6label')
            c.text('7', self.points['p3_7'], offset_pt=[-12.802500789158705, 2.257426309670096], vertex=False, id='p3_7label')
            c.text('8', self.points['p3_8'], offset_pt=[-8.356238925925012, 9.958577760546714], vertex=False, id='p3_8label')
            c.text('9', self.points['p3_9'], offset_pt=[-2.3880612583373385e-15, 13.0], vertex=False, id='p3_9label')
            c.text('(C)', [12.5, -2.2], offset_pt=[0, 0], vertex=False, id='label38')
            c.text('1', self.points['p4_1'], offset_pt=[8.356238925925012, 9.958577760546714], vertex=False, id='p4_1label')
            c.text('2', self.points['p4_2'], offset_pt=[12.802500789158705, 2.257426309670094], vertex=False, id='p4_2label')
            c.text('3', self.points['p4_3'], offset_pt=[11.258330249197703, -6.499999999999999], vertex=False, id='p4_3label')
            c.text('4', self.points['p4_4'], offset_pt=[4.446261863233695, -12.216004070216808], vertex=False, id='p4_4label')
            c.text('5', self.points['p4_5'], offset_pt=[-4.446261863233693, -12.21600407021681], vertex=False, id='p4_5label')
            c.text('6', self.points['p4_6'], offset_pt=[-11.258330249197703, -6.499999999999999], vertex=False, id='p4_6label')
            c.text('7', self.points['p4_7'], offset_pt=[-12.802500789158705, 2.257426309670096], vertex=False, id='p4_7label')
            c.text('8', self.points['p4_8'], offset_pt=[-8.356238925925012, 9.958577760546714], vertex=False, id='p4_8label')
            c.text('9', self.points['p4_9'], offset_pt=[-2.3880612583373385e-15, 13.0], vertex=False, id='p4_9label')
            c.text('(D)', [-3.5, -11.2], offset_pt=[0, 0], vertex=False, id='label48')
            c.text('1', self.points['p5_1'], offset_pt=[8.356238925925012, 9.958577760546714], vertex=False, id='p5_1label')
            c.text('2', self.points['p5_2'], offset_pt=[12.802500789158705, 2.257426309670094], vertex=False, id='p5_2label')
            c.text('3', self.points['p5_3'], offset_pt=[11.258330249197703, -6.499999999999999], vertex=False, id='p5_3label')
            c.text('4', self.points['p5_4'], offset_pt=[4.446261863233695, -12.216004070216808], vertex=False, id='p5_4label')
            c.text('5', self.points['p5_5'], offset_pt=[-4.446261863233693, -12.21600407021681], vertex=False, id='p5_5label')
            c.text('6', self.points['p5_6'], offset_pt=[-11.258330249197703, -6.499999999999999], vertex=False, id='p5_6label')
            c.text('7', self.points['p5_7'], offset_pt=[-12.802500789158705, 2.257426309670096], vertex=False, id='p5_7label')
            c.text('8', self.points['p5_8'], offset_pt=[-8.356238925925012, 9.958577760546714], vertex=False, id='p5_8label')
            c.text('9', self.points['p5_9'], offset_pt=[-2.3880612583373385e-15, 13.0], vertex=False, id='p5_9label')
            c.text('(E)', [4.5, -11.2], offset_pt=[0, 0], vertex=False, id='label58')
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane211().draw(sys.argv[1] if len(sys.argv) > 1 else None))
