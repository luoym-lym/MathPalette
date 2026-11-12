"""Frozen question Plane356; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane356:

    def __init__(self):
        self.id = 'Plane356'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:1239'
        self.question = 'The diagram shows a grid made of vertical and horizontal lines. Which part was cut from the grid?\nChoices:\nA:A\nB:B\nC:C\nD:D\nE:E'
        self.answer = 'E'
        self.answer_type = 'choice'
        self.choices = {'A': 'A', 'B': 'B', 'C': 'C', 'D': 'D', 'E': 'E'}
        self.query = self.question
        self.points = {'mainv0a': [8, 8],
         'mainv0b': [8, 16],
         'mainv1a': [10.2, 8],
         'mainv1b': [10.2, 16],
         'mainv2aa': [11.8, 8],
         'mainv2ab': [11.8, 9.6],
         'mainv2ba': [11.8, 12.4],
         'mainv2bb': [11.8, 16],
         'mainv3aa': [13.5, 8],
         'mainv3ab': [13.5, 9.6],
         'mainv3ba': [13.5, 12.4],
         'mainv3bb': [13.5, 16],
         'mainv4aa': [14.2, 8],
         'mainv4ab': [14.2, 9.6],
         'mainv4ba': [14.2, 12.4],
         'mainv4bb': [14.2, 16],
         'mainv5a': [15, 8],
         'mainv5b': [15, 16],
         'mainv6a': [15.35, 8],
         'mainv6b': [15.35, 16],
         'mainh0a': [6, 8.8],
         'mainh0b': [16, 8.8],
         'mainh1aa': [6, 9.8],
         'mainh1ab': [10.9, 9.8],
         'mainh1ba': [14.7, 9.8],
         'mainh1bb': [16, 9.8],
         'mainh2aa': [6, 10.8],
         'mainh2ab': [10.9, 10.8],
         'mainh2ba': [14.7, 10.8],
         'mainh2bb': [16, 10.8],
         'mainh3aa': [6, 11.8],
         'mainh3ab': [10.9, 11.8],
         'mainh3ba': [14.7, 11.8],
         'mainh3bb': [16, 11.8],
         'mainh4a': [6, 12.8],
         'mainh4b': [16, 12.8],
         'mainh5a': [6, 13.8],
         'mainh5b': [16, 13.8],
         'mainh6a': [6, 14.8],
         'mainh6b': [16, 14.8],
         'mainh7a': [6, 15.8],
         'mainh7b': [16, 15.8],
         'opt0v0a': [0.7, 0],
         'opt0v0b': [0.7, 2.3],
         'opt0v1a': [2.3, 0],
         'opt0v1b': [2.3, 2.3],
         'opt0h0a': [0.0, 0.5],
         'opt0h0b': [3.5, 0.5],
         'opt0h1a': [0.0, 1.2],
         'opt0h1b': [3.5, 1.2],
         'opt0h2a': [0.0, 1.9],
         'opt0h2b': [3.5, 1.9],
         'label0': [1.75, -0.6],
         'opt1v0a': [5.2, 0],
         'opt1v0b': [5.2, 2.3],
         'opt1v1a': [6.8, 0],
         'opt1v1b': [6.8, 2.3],
         'opt1v2a': [7.4, 0],
         'opt1v2b': [7.4, 2.3],
         'opt1h0a': [4.5, 0.5],
         'opt1h0b': [8.0, 0.5],
         'opt1h1a': [4.5, 1.2],
         'opt1h1b': [8.0, 1.2],
         'label1': [6.25, -0.6],
         'opt2v0a': [10.2, 0],
         'opt2v0b': [10.2, 2.3],
         'opt2v1a': [10.7, 0],
         'opt2v1b': [10.7, 2.3],
         'opt2v2a': [11.2, 0],
         'opt2v2b': [11.2, 2.3],
         'opt2h0a': [9.0, 0.5],
         'opt2h0b': [12.5, 0.5],
         'opt2h1a': [9.0, 1.2],
         'opt2h1b': [12.5, 1.2],
         'opt2h2a': [9.0, 1.9],
         'opt2h2b': [12.5, 1.9],
         'label2': [10.75, -0.6],
         'opt3v0a': [14.2, 0],
         'opt3v0b': [14.2, 2.3],
         'opt3v1a': [15.8, 0],
         'opt3v1b': [15.8, 2.3],
         'opt3v2a': [16.4, 0],
         'opt3v2b': [16.4, 2.3],
         'opt3h0a': [13.5, 0.5],
         'opt3h0b': [17.0, 0.5],
         'opt3h1a': [13.5, 0.75],
         'opt3h1b': [17.0, 0.75],
         'opt3h2a': [13.5, 1.9],
         'opt3h2b': [17.0, 1.9],
         'label3': [15.25, -0.6],
         'opt4v0a': [18.7, 0],
         'opt4v0b': [18.7, 2.3],
         'opt4v1a': [20.3, 0],
         'opt4v1b': [20.3, 2.3],
         'opt4v2a': [20.9, 0],
         'opt4v2b': [20.9, 2.3],
         'opt4h0a': [18.0, 0.5],
         'opt4h0b': [21.5, 0.5],
         'opt4h1a': [18.0, 1.2],
         'opt4h1b': [21.5, 1.2],
         'opt4h2a': [18.0, 1.9],
         'opt4h2b': [21.5, 1.9],
         'label4': [19.75, -0.6]}
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane356.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-0.5328421672137136, 22.068639012151785], ylim=[-3.7274537952981825, 18.874027384067315]) as c:
            for object_id, points in [('mainv0', [self.points['mainv0a'], self.points['mainv0b']]), ('mainv1', [self.points['mainv1a'], self.points['mainv1b']]), ('mainv2a', [self.points['mainv2aa'], self.points['mainv2ab']]), ('mainv2b', [self.points['mainv2ba'], self.points['mainv2bb']]), ('mainv3a', [self.points['mainv3aa'], self.points['mainv3ab']]), ('mainv3b', [self.points['mainv3ba'], self.points['mainv3bb']]), ('mainv4a', [self.points['mainv4aa'], self.points['mainv4ab']]), ('mainv4b', [self.points['mainv4ba'], self.points['mainv4bb']]), ('mainv5', [self.points['mainv5a'], self.points['mainv5b']]), ('mainv6', [self.points['mainv6a'], self.points['mainv6b']]), ('mainh0', [self.points['mainh0a'], self.points['mainh0b']]), ('mainh1a', [self.points['mainh1aa'], self.points['mainh1ab']]), ('mainh1b', [self.points['mainh1ba'], self.points['mainh1bb']]), ('mainh2a', [self.points['mainh2aa'], self.points['mainh2ab']]), ('mainh2b', [self.points['mainh2ba'], self.points['mainh2bb']]), ('mainh3a', [self.points['mainh3aa'], self.points['mainh3ab']]), ('mainh3b', [self.points['mainh3ba'], self.points['mainh3bb']]), ('mainh4', [self.points['mainh4a'], self.points['mainh4b']]), ('mainh5', [self.points['mainh5a'], self.points['mainh5b']]), ('mainh6', [self.points['mainh6a'], self.points['mainh6b']]), ('mainh7', [self.points['mainh7a'], self.points['mainh7b']]), ('opt0v0', [self.points['opt0v0a'], self.points['opt0v0b']]), ('opt0v1', [self.points['opt0v1a'], self.points['opt0v1b']]), ('opt0h0', [self.points['opt0h0a'], self.points['opt0h0b']]), ('opt0h1', [self.points['opt0h1a'], self.points['opt0h1b']]), ('opt0h2', [self.points['opt0h2a'], self.points['opt0h2b']]), ('opt1v0', [self.points['opt1v0a'], self.points['opt1v0b']]), ('opt1v1', [self.points['opt1v1a'], self.points['opt1v1b']]), ('opt1v2', [self.points['opt1v2a'], self.points['opt1v2b']]), ('opt1h0', [self.points['opt1h0a'], self.points['opt1h0b']]), ('opt1h1', [self.points['opt1h1a'], self.points['opt1h1b']]), ('opt2v0', [self.points['opt2v0a'], self.points['opt2v0b']]), ('opt2v1', [self.points['opt2v1a'], self.points['opt2v1b']]), ('opt2v2', [self.points['opt2v2a'], self.points['opt2v2b']]), ('opt2h0', [self.points['opt2h0a'], self.points['opt2h0b']]), ('opt2h1', [self.points['opt2h1a'], self.points['opt2h1b']]), ('opt2h2', [self.points['opt2h2a'], self.points['opt2h2b']]), ('opt3v0', [self.points['opt3v0a'], self.points['opt3v0b']]), ('opt3v1', [self.points['opt3v1a'], self.points['opt3v1b']]), ('opt3v2', [self.points['opt3v2a'], self.points['opt3v2b']]), ('opt3h0', [self.points['opt3h0a'], self.points['opt3h0b']]), ('opt3h1', [self.points['opt3h1a'], self.points['opt3h1b']]), ('opt3h2', [self.points['opt3h2a'], self.points['opt3h2b']]), ('opt4v0', [self.points['opt4v0a'], self.points['opt4v0b']]), ('opt4v1', [self.points['opt4v1a'], self.points['opt4v1b']]), ('opt4v2', [self.points['opt4v2a'], self.points['opt4v2b']]), ('opt4h0', [self.points['opt4h0a'], self.points['opt4h0b']]), ('opt4h1', [self.points['opt4h1a'], self.points['opt4h1b']]), ('opt4h2', [self.points['opt4h2a'], self.points['opt4h2b']])]:
                c.line(points, id=object_id)
            for object_id, text, anchor in [('label0', '(A)', self.points['label0']), ('label1', '(B)', self.points['label1']), ('label2', '(C)', self.points['label2']), ('label3', '(D)', self.points['label3']), ('label4', '(E)', self.points['label4'])]:
                c.text(text, anchor, id=object_id, offset_pt=[0, 0], vertex=False)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane356().draw(sys.argv[1] if len(sys.argv) > 1 else None))
