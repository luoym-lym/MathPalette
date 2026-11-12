"""Frozen question Plane465; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane465:

    def __init__(self):
        self.id = 'Plane465'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:2643'
        self.question = 'A portion of a corner of a tiled floor is shown.  If the entire floor is tiled in this way and each of the four corners  looks like this one, then what fraction of the tiled floor is made of darker tiles?\n\nChoices:\nA:$\\frac{1}{3}$\nB:$\\frac{4}{9}$\nC:$\\frac{1}{2}$\nD:$\\frac{5}{9}$\nE:$\\frac{5}{8}$'
        self.answer = 'B'
        self.answer_type = 'choice'
        self.choices = {'A': '$\\frac{1}{3}$', 'B': '$\\frac{4}{9}$', 'C': '$\\frac{1}{2}$', 'D': '$\\frac{5}{9}$', 'E': '$\\frac{5}{8}$'}
        self.query = self.question
        self.points = {'f0_0': [3.0, 11.0],
         'f0_1': [4.0, 10.0],
         'f0_2': [4.0, 9.0],
         'f0_3': [5.0, 9.0],
         'f0_4': [6.0, 8.0],
         'f0_5': [5.0, 7.0],
         'f0_6': [4.0, 7.0],
         'f0_7': [4.0, 6.0],
         'f0_8': [3.0, 5.0],
         'f0_9': [2.0, 6.0],
         'f0_10': [2.0, 7.0],
         'f0_11': [1.0, 7.0],
         'f0_12': [0.0, 8.0],
         'f0_13': [1.0, 9.0],
         'f0_14': [2.0, 9.0],
         'f0_15': [2.0, 10.0],
         'f1_0': [9.0, 11.0],
         'f1_1': [10.0, 10.0],
         'f1_2': [10.0, 9.0],
         'f1_3': [11.0, 9.0],
         'f1_4': [11.0, 7.0],
         'f1_5': [10.0, 7.0],
         'f1_6': [10.0, 6.0],
         'f1_7': [9.0, 5.0],
         'f1_8': [8.0, 6.0],
         'f1_9': [8.0, 7.0],
         'f1_10': [7.0, 7.0],
         'f1_11': [6.0, 8.0],
         'f1_12': [7.0, 9.0],
         'f1_13': [8.0, 9.0],
         'f1_14': [8.0, 10.0],
         'f2_0': [3.0, 5.0],
         'f2_1': [4.0, 4.0],
         'f2_2': [4.0, 3.0],
         'f2_3': [5.0, 3.0],
         'f2_4': [5.909090909090909, 2.090909090909091],
         'f2_5': [4.0, 1.0],
         'f2_6': [2.0, 0.5],
         'f2_7': [2.0, 1.0],
         'f2_8': [1.0, 1.0],
         'f2_9': [0.0, 2.0],
         'f2_10': [1.0, 3.0],
         'f2_11': [2.0, 3.0],
         'f2_12': [2.0, 4.0],
         'f3_0': [9.0, 5.0],
         'f3_1': [9.727272727272727, 4.2727272727272725],
         'f3_2': [6.333333333333333, 2.3333333333333335],
         'f3_3': [7.0, 3.0],
         'f3_4': [7.5, 3.0],
         'f3_5': [8.0, 3.2857142857142856],
         'f3_6': [8.0, 4.0],
         'grid0_0a': [0.0, 0.0],
         'grid0_0b': [0.0, 11.0],
         'grid0_1a': [1.0, 0.25],
         'grid0_1b': [1.0, 11.0],
         'grid0_2a': [2.0, 0.5],
         'grid0_2b': [2.0, 11.0],
         'grid0_3a': [3.0, 0.75],
         'grid0_3b': [3.0, 11.0],
         'grid0_4a': [4.0, 1.0],
         'grid0_4b': [4.0, 11.0],
         'grid0_5a': [5.0, 1.5714285714285714],
         'grid0_5b': [5.0, 11.0],
         'grid0_6a': [6.0, 2.142857142857143],
         'grid0_6b': [6.0, 11.0],
         'grid0_7a': [7.0, 2.7142857142857144],
         'grid0_7b': [7.0, 11.0],
         'grid0_8a': [8.0, 3.2857142857142856],
         'grid0_8b': [8.0, 11.0],
         'grid0_9a': [9.0, 3.857142857142857],
         'grid0_9b': [9.0, 11.0],
         'grid0_10a': [10.0, 4.428571428571429],
         'grid0_10b': [10.0, 11.0],
         'grid1_1a': [0.0, 1.0],
         'grid1_1b': [4.0, 1.0],
         'grid1_2a': [0.0, 2.0],
         'grid1_2b': [5.75, 2.0],
         'grid1_3a': [0.0, 3.0],
         'grid1_3b': [7.499999999999999, 3.0],
         'grid1_4a': [0.0, 4.0],
         'grid1_4b': [9.25, 4.0],
         'grid1_5a': [0.0, 5.0],
         'grid1_5b': [11.0, 5.0],
         'grid1_6a': [0.0, 6.0],
         'grid1_6b': [11.0, 6.0],
         'grid1_7a': [0.0, 7.0],
         'grid1_7b': [11.0, 7.0],
         'grid1_8a': [0.0, 8.0],
         'grid1_8b': [11.0, 8.0],
         'grid1_9a': [0.0, 9.0],
         'grid1_9b': [11.0, 9.0],
         'grid1_10a': [0.0, 10.0],
         'grid1_10b': [11.0, 10.0],
         'grid1_11a': [0.0, 11.0],
         'grid1_11b': [11.0, 11.0]}
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane465.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-0.27261692276050464, 11.29093158761254], ylim=[-0.29093158761253957, 11.272616922760506]) as c:
            for object_id, points in [('gray0', [self.points['f0_0'], self.points['f0_1'], self.points['f0_2'], self.points['f0_3'], self.points['f0_4'], self.points['f0_5'], self.points['f0_6'], self.points['f0_7'], self.points['f0_8'], self.points['f0_9'], self.points['f0_10'], self.points['f0_11'], self.points['f0_12'], self.points['f0_13'], self.points['f0_14'], self.points['f0_15']]), ('gray1', [self.points['f1_0'], self.points['f1_1'], self.points['f1_2'], self.points['f1_3'], self.points['f1_4'], self.points['f1_5'], self.points['f1_6'], self.points['f1_7'], self.points['f1_8'], self.points['f1_9'], self.points['f1_10'], self.points['f1_11'], self.points['f1_12'], self.points['f1_13'], self.points['f1_14']]), ('gray2', [self.points['f2_0'], self.points['f2_1'], self.points['f2_2'], self.points['f2_3'], self.points['f2_4'], self.points['f2_5'], self.points['f2_6'], self.points['f2_7'], self.points['f2_8'], self.points['f2_9'], self.points['f2_10'], self.points['f2_11'], self.points['f2_12']]), ('gray3', [self.points['f3_0'], self.points['f3_1'], self.points['f3_2'], self.points['f3_3'], self.points['f3_4'], self.points['f3_5'], self.points['f3_6']])]:
                c.fill(points, id=object_id, facecolor='#D0D0D0')
            c.line([self.points['grid0_0a'], self.points['grid0_0b']], id='grid0_0')
            for object_id, points in [('grid0_1', [self.points['grid0_1a'], self.points['grid0_1b']]), ('grid0_2', [self.points['grid0_2a'], self.points['grid0_2b']]), ('grid0_3', [self.points['grid0_3a'], self.points['grid0_3b']]), ('grid0_4', [self.points['grid0_4a'], self.points['grid0_4b']]), ('grid0_5', [self.points['grid0_5a'], self.points['grid0_5b']]), ('grid0_6', [self.points['grid0_6a'], self.points['grid0_6b']]), ('grid0_7', [self.points['grid0_7a'], self.points['grid0_7b']]), ('grid0_8', [self.points['grid0_8a'], self.points['grid0_8b']]), ('grid0_9', [self.points['grid0_9a'], self.points['grid0_9b']]), ('grid0_10', [self.points['grid0_10a'], self.points['grid0_10b']]), ('grid1_1', [self.points['grid1_1a'], self.points['grid1_1b']]), ('grid1_2', [self.points['grid1_2a'], self.points['grid1_2b']]), ('grid1_3', [self.points['grid1_3a'], self.points['grid1_3b']]), ('grid1_4', [self.points['grid1_4a'], self.points['grid1_4b']]), ('grid1_5', [self.points['grid1_5a'], self.points['grid1_5b']]), ('grid1_6', [self.points['grid1_6a'], self.points['grid1_6b']]), ('grid1_7', [self.points['grid1_7a'], self.points['grid1_7b']]), ('grid1_8', [self.points['grid1_8a'], self.points['grid1_8b']]), ('grid1_9', [self.points['grid1_9a'], self.points['grid1_9b']]), ('grid1_10', [self.points['grid1_10a'], self.points['grid1_10b']])]:
                c.line(points, id=object_id, linestyle=(0, [4, 3]))
            c.line([self.points['grid1_11a'], self.points['grid1_11b']], id='grid1_11')
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane465().draw(sys.argv[1] if len(sys.argv) > 1 else None))
