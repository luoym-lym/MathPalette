"""Collected question Plane356; construction on the shared drawing protocol."""
from pathlib import Path
import sys
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from MathPalette_Dataset.drawing import Canvas, PLANE

class Plane356:
    variants = ('C01', 'C02', 'C03', 'C04', 'C05', 'C06')

    def __init__(self):
        self.points = {
            'mainv0a': [8, 8], 'mainv0b': [8, 16], 'mainv1a': [10.2, 8], 'mainv1b': [10.2, 16],
            'mainv2aa': [11.8, 8], 'mainv2ab': [11.8, 9.6], 'mainv2ba': [11.8, 12.4], 'mainv2bb': [11.8, 16],
            'mainv3aa': [13.5, 8], 'mainv3ab': [13.5, 9.6], 'mainv3ba': [13.5, 12.4], 'mainv3bb': [13.5, 16],
            'mainv4aa': [14.2, 8], 'mainv4ab': [14.2, 9.6], 'mainv4ba': [14.2, 12.4], 'mainv4bb': [14.2, 16],
            'mainv5a': [15, 8], 'mainv5b': [15, 16], 'mainv6a': [15.35, 8], 'mainv6b': [15.35, 16],
            'mainh0a': [6, 8.8], 'mainh0b': [16, 8.8], 'mainh1aa': [6, 9.8], 'mainh1ab': [10.9, 9.8],
            'mainh1ba': [14.7, 9.8], 'mainh1bb': [16, 9.8], 'mainh2aa': [6, 10.8], 'mainh2ab': [10.9, 10.8],
            'mainh2ba': [14.7, 10.8], 'mainh2bb': [16, 10.8], 'mainh3aa': [6, 11.8], 'mainh3ab': [10.9, 11.8],
            'mainh3ba': [14.7, 11.8], 'mainh3bb': [16, 11.8], 'mainh4a': [6, 12.8], 'mainh4b': [16, 12.8],
            'mainh5a': [6, 13.8], 'mainh5b': [16, 13.8], 'mainh6a': [6, 14.8], 'mainh6b': [16, 14.8],
            'mainh7a': [6, 15.8], 'mainh7b': [16, 15.8], 'opt0v0a': [0.7, 0], 'opt0v0b': [0.7, 2.3],
            'opt0v1a': [2.3, 0], 'opt0v1b': [2.3, 2.3], 'opt0h0a': [0.0, 0.5], 'opt0h0b': [3.5, 0.5],
            'opt0h1a': [0.0, 1.2], 'opt0h1b': [3.5, 1.2], 'opt0h2a': [0.0, 1.9], 'opt0h2b': [3.5, 1.9],
            'label0': [1.75, -0.6], 'opt1v0a': [5.2, 0], 'opt1v0b': [5.2, 2.3], 'opt1v1a': [6.8, 0],
            'opt1v1b': [6.8, 2.3], 'opt1v2a': [7.4, 0], 'opt1v2b': [7.4, 2.3], 'opt1h0a': [4.5, 0.5],
            'opt1h0b': [8.0, 0.5], 'opt1h1a': [4.5, 1.2], 'opt1h1b': [8.0, 1.2], 'label1': [6.25, -0.6],
            'opt2v0a': [10.2, 0], 'opt2v0b': [10.2, 2.3], 'opt2v1a': [10.7, 0], 'opt2v1b': [10.7, 2.3],
            'opt2v2a': [11.2, 0], 'opt2v2b': [11.2, 2.3], 'opt2h0a': [9.0, 0.5], 'opt2h0b': [12.5, 0.5],
            'opt2h1a': [9.0, 1.2], 'opt2h1b': [12.5, 1.2], 'opt2h2a': [9.0, 1.9], 'opt2h2b': [12.5, 1.9],
            'label2': [10.75, -0.6], 'opt3v0a': [14.2, 0], 'opt3v0b': [14.2, 2.3], 'opt3v1a': [15.8, 0],
            'opt3v1b': [15.8, 2.3], 'opt3v2a': [16.4, 0], 'opt3v2b': [16.4, 2.3], 'opt3h0a': [13.5, 0.5],
            'opt3h0b': [17.0, 0.5], 'opt3h1a': [13.5, 0.75], 'opt3h1b': [17.0, 0.75], 'opt3h2a': [13.5, 1.9],
            'opt3h2b': [17.0, 1.9], 'label3': [15.25, -0.6], 'opt4v0a': [18.7, 0], 'opt4v0b': [18.7, 2.3],
            'opt4v1a': [20.3, 0], 'opt4v1b': [20.3, 2.3], 'opt4v2a': [20.9, 0], 'opt4v2b': [20.9, 2.3],
            'opt4h0a': [18.0, 0.5], 'opt4h0b': [21.5, 0.5], 'opt4h1a': [18.0, 1.2], 'opt4h1b': [21.5, 1.2],
            'opt4h2a': [18.0, 1.9], 'opt4h2b': [21.5, 1.9], 'label4': [19.75, -0.6]
        }
        self._g01 = [
            ('mainv5', [[15.0, 8.0], [15.0, 16.0]]), ('mainv6', [[15.35, 8.0], [15.35, 16.0]]),
            ('mainh0', [[6.0, 8.8], [16.0, 8.8]]), ('mainh1a', [[6.0, 9.8], [10.9, 9.8]]),
            ('mainh1b', [[14.7, 9.8], [16.0, 9.8]]), ('mainh2a', [[6.0, 10.8], [10.9, 10.8]]),
            ('mainh2b', [[14.7, 10.8], [16.0, 10.8]]), ('mainh3a', [[6.0, 11.8], [10.9, 11.8]]),
            ('mainh3b', [[14.7, 11.8], [16.0, 11.8]]), ('mainh4', [[6.0, 12.8], [16.0, 12.8]]),
            ('mainh5', [[6.0, 13.8], [16.0, 13.8]]), ('mainh6', [[6.0, 14.8], [16.0, 14.8]]),
            ('mainh7', [[6.0, 15.8], [16.0, 15.8]]), ('opt0v0', [[0.7, 0.0], [0.7, 2.3]]),
            ('opt0v1', [[2.3, 0.0], [2.3, 2.3]]), ('opt0h0', [[0.0, 0.5], [3.5, 0.5]]),
            ('opt0h1', [[0.0, 1.2], [3.5, 1.2]]), ('opt0h2', [[0.0, 1.9], [3.5, 1.9]]),
            ('opt1v0', [[5.2, 0.0], [5.2, 2.3]]), ('opt1v1', [[6.8, 0.0], [6.8, 2.3]]),
            ('opt1v2', [[7.4, 0.0], [7.4, 2.3]]), ('opt1h0', [[4.5, 0.5], [8.0, 0.5]]),
            ('opt1h1', [[4.5, 1.2], [8.0, 1.2]]), ('opt2v0', [[10.2, 0.0], [10.2, 2.3]]),
            ('opt2v1', [[10.7, 0.0], [10.7, 2.3]]), ('opt2v2', [[11.2, 0.0], [11.2, 2.3]]),
            ('opt2h0', [[9.0, 0.5], [12.5, 0.5]]), ('opt2h1', [[9.0, 1.2], [12.5, 1.2]]),
            ('opt2h2', [[9.0, 1.9], [12.5, 1.9]])
        ]

    def draw(self, output_path=None, *, variant=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / (self.__class__.__name__ + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if variant not in self.variants:
                raise ValueError('Unknown Special variant: ' + str(variant))
            return getattr(self, 'draw_' + variant)(output_path)
        with Canvas(PLANE, xlim=(-0.5328421672137136, 22.068639012151785), ylim=(-3.7274537952981825, 18.874027384067315)) as c:
            for object_id, points in [('mainv0', [self.points['mainv0a'], self.points['mainv0b']]), ('mainv1', [self.points['mainv1a'], self.points['mainv1b']]), ('mainv2a', [self.points['mainv2aa'], self.points['mainv2ab']]), ('mainv2b', [self.points['mainv2ba'], self.points['mainv2bb']]), ('mainv3a', [self.points['mainv3aa'], self.points['mainv3ab']]), ('mainv3b', [self.points['mainv3ba'], self.points['mainv3bb']]), ('mainv4a', [self.points['mainv4aa'], self.points['mainv4ab']]), ('mainv4b', [self.points['mainv4ba'], self.points['mainv4bb']]), ('mainv5', [self.points['mainv5a'], self.points['mainv5b']]), ('mainv6', [self.points['mainv6a'], self.points['mainv6b']]), ('mainh0', [self.points['mainh0a'], self.points['mainh0b']]), ('mainh1a', [self.points['mainh1aa'], self.points['mainh1ab']]), ('mainh1b', [self.points['mainh1ba'], self.points['mainh1bb']]), ('mainh2a', [self.points['mainh2aa'], self.points['mainh2ab']]), ('mainh2b', [self.points['mainh2ba'], self.points['mainh2bb']]), ('mainh3a', [self.points['mainh3aa'], self.points['mainh3ab']]), ('mainh3b', [self.points['mainh3ba'], self.points['mainh3bb']]), ('mainh4', [self.points['mainh4a'], self.points['mainh4b']]), ('mainh5', [self.points['mainh5a'], self.points['mainh5b']]), ('mainh6', [self.points['mainh6a'], self.points['mainh6b']]), ('mainh7', [self.points['mainh7a'], self.points['mainh7b']]), ('opt0v0', [self.points['opt0v0a'], self.points['opt0v0b']]), ('opt0v1', [self.points['opt0v1a'], self.points['opt0v1b']]), ('opt0h0', [self.points['opt0h0a'], self.points['opt0h0b']]), ('opt0h1', [self.points['opt0h1a'], self.points['opt0h1b']]), ('opt0h2', [self.points['opt0h2a'], self.points['opt0h2b']]), ('opt1v0', [self.points['opt1v0a'], self.points['opt1v0b']]), ('opt1v1', [self.points['opt1v1a'], self.points['opt1v1b']]), ('opt1v2', [self.points['opt1v2a'], self.points['opt1v2b']]), ('opt1h0', [self.points['opt1h0a'], self.points['opt1h0b']]), ('opt1h1', [self.points['opt1h1a'], self.points['opt1h1b']]), ('opt2v0', [self.points['opt2v0a'], self.points['opt2v0b']]), ('opt2v1', [self.points['opt2v1a'], self.points['opt2v1b']]), ('opt2v2', [self.points['opt2v2a'], self.points['opt2v2b']]), ('opt2h0', [self.points['opt2h0a'], self.points['opt2h0b']]), ('opt2h1', [self.points['opt2h1a'], self.points['opt2h1b']]), ('opt2h2', [self.points['opt2h2a'], self.points['opt2h2b']]), ('opt3v0', [self.points['opt3v0a'], self.points['opt3v0b']]), ('opt3v1', [self.points['opt3v1a'], self.points['opt3v1b']]), ('opt3v2', [self.points['opt3v2a'], self.points['opt3v2b']]), ('opt3h0', [self.points['opt3h0a'], self.points['opt3h0b']]), ('opt3h1', [self.points['opt3h1a'], self.points['opt3h1b']]), ('opt3h2', [self.points['opt3h2a'], self.points['opt3h2b']]), ('opt4v0', [self.points['opt4v0a'], self.points['opt4v0b']]), ('opt4v1', [self.points['opt4v1a'], self.points['opt4v1b']]), ('opt4v2', [self.points['opt4v2a'], self.points['opt4v2b']]), ('opt4h0', [self.points['opt4h0a'], self.points['opt4h0b']]), ('opt4h1', [self.points['opt4h1a'], self.points['opt4h1b']]), ('opt4h2', [self.points['opt4h2a'], self.points['opt4h2b']])]:
                c.line(points, id=object_id)
            for object_id, text, anchor in [('label0', '(A)', self.points['label0']), ('label1', '(B)', self.points['label1']), ('label2', '(C)', self.points['label2']), ('label3', '(D)', self.points['label3']), ('label4', '(E)', self.points['label4'])]:
                c.text(text, anchor, id=object_id)
            return c.save(output_path)

    def draw_C01(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane356_C01.png'
        with Canvas(PLANE, xlim=(-0.5328421672137136, 22.068639012151785), ylim=(-3.7274537952981825, 18.874027384067315)) as c:
            c.line([[8.0, 8.0], [8.0, 16.0]], id='mainv0')
            c.line([[10.2, 8.0], [10.2, 16.0]], id='mainv1')
            for object_id, points in [('mainv2a', [[11.8, 8.0], [11.8, 9.6]]), ('mainv2b', [[11.8, 12.4], [11.8, 16.0]]), ('mainv3a', [[13.5, 8.0], [13.5, 9.6]]), ('mainv3b', [[13.5, 12.4], [13.5, 16.0]]), ('mainv4a', [[14.2, 8.0], [14.2, 9.6]]), ('mainv4b', [[14.2, 12.4], [14.2, 16.0]])]:
                c.line(points, id=object_id, color='#DC2626')
            for object_id, points in self._g01:
                c.line(points, id=object_id)
            for object_id, points in [('opt3v0', [[14.2, 0.0], [14.2, 2.3]]), ('opt3v1', [[15.8, 0.0], [15.8, 2.3]]), ('opt3v2', [[16.4, 0.0], [16.4, 2.3]]), ('opt3h0', [[13.5, 0.5], [17.0, 0.5]]), ('opt3h1', [[13.5, 0.75], [17.0, 0.75]]), ('opt3h2', [[13.5, 1.9], [17.0, 1.9]])]:
                c.line(points, id=object_id, color='#DC2626')
            for object_id, points in [('opt4v0', [[18.7, 0.0], [18.7, 2.3]]), ('opt4v1', [[20.3, 0.0], [20.3, 2.3]]), ('opt4v2', [[20.9, 0.0], [20.9, 2.3]]), ('opt4h0', [[18.0, 0.5], [21.5, 0.5]]), ('opt4h1', [[18.0, 1.2], [21.5, 1.2]]), ('opt4h2', [[18.0, 1.9], [21.5, 1.9]])]:
                c.line(points, id=object_id)
            for object_id, text, anchor in [('label0', '(A)', (1.75, -0.6)), ('label1', '(B)', (6.25, -0.6)), ('label2', '(C)', (10.75, -0.6)), ('label3', '(D)', (15.25, -0.6)), ('label4', '(E)', (19.75, -0.6))]:
                c.text(text, anchor, id=object_id)
            return c.save(output_path)

    def draw_C02(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane356_C02.png'
        with Canvas(PLANE, xlim=(-0.5328421672137136, 22.068639012151785), ylim=(-3.7274537952981825, 18.874027384067315)) as c:
            for object_id, points in [('mainv0', [[8.0, 8.0], [8.0, 16.0]]), ('mainv1', [[10.2, 8.0], [10.2, 16.0]]), ('mainv2a', [[11.8, 8.0], [11.8, 9.6]]), ('mainv2b', [[11.8, 12.4], [11.8, 16.0]]), ('mainv3a', [[13.5, 8.0], [13.5, 9.6]]), ('mainv3b', [[13.5, 12.4], [13.5, 16.0]]), ('mainv4a', [[14.2, 8.0], [14.2, 9.6]]), ('mainv4b', [[14.2, 12.4], [14.2, 16.0]]), ('mainv5', [[15.0, 8.0], [15.0, 16.0]]), ('mainv6', [[15.35, 8.0], [15.35, 16.0]]), ('mainh0', [[6.0, 8.8], [16.0, 8.8]]), ('mainh1a', [[6.0, 9.8], [10.9, 9.8]]), ('mainh1b', [[14.7, 9.8], [16.0, 9.8]]), ('mainh2a', [[6.0, 10.8], [10.9, 10.8]]), ('mainh2b', [[14.7, 10.8], [16.0, 10.8]]), ('mainh3a', [[6.0, 11.8], [10.9, 11.8]]), ('mainh3b', [[14.7, 11.8], [16.0, 11.8]]), ('mainh4', [[6.0, 12.8], [16.0, 12.8]]), ('mainh5', [[6.0, 13.8], [16.0, 13.8]]), ('mainh6', [[6.0, 14.8], [16.0, 14.8]]), ('mainh7', [[6.0, 15.8], [16.0, 15.8]])]:
                c.line(points, id=object_id)
            for object_id, points in [('opt0v0', [[0.7, 0.0], [0.7, 2.3]]), ('opt0v1', [[2.3, 0.0], [2.3, 2.3]]), ('opt0h0', [[0.0, 0.5], [3.5, 0.5]]), ('opt0h1', [[0.0, 1.2], [3.5, 1.2]]), ('opt0h2', [[0.0, 1.9], [3.5, 1.9]])]:
                c.line(points, id=object_id, color='#DC2626', linewidth=1.5)
            for object_id, points in [('opt1v0', [[5.2, 0.0], [5.2, 2.3]]), ('opt1v1', [[6.8, 0.0], [6.8, 2.3]]), ('opt1v2', [[7.4, 0.0], [7.4, 2.3]]), ('opt1h0', [[4.5, 0.5], [8.0, 0.5]]), ('opt1h1', [[4.5, 1.2], [8.0, 1.2]]), ('opt2v0', [[10.2, 0.0], [10.2, 2.3]]), ('opt2v1', [[10.7, 0.0], [10.7, 2.3]]), ('opt2v2', [[11.2, 0.0], [11.2, 2.3]]), ('opt2h0', [[9.0, 0.5], [12.5, 0.5]]), ('opt2h1', [[9.0, 1.2], [12.5, 1.2]]), ('opt2h2', [[9.0, 1.9], [12.5, 1.9]]), ('opt3v0', [[14.2, 0.0], [14.2, 2.3]]), ('opt3v1', [[15.8, 0.0], [15.8, 2.3]]), ('opt3v2', [[16.4, 0.0], [16.4, 2.3]]), ('opt3h0', [[13.5, 0.5], [17.0, 0.5]]), ('opt3h1', [[13.5, 0.75], [17.0, 0.75]]), ('opt3h2', [[13.5, 1.9], [17.0, 1.9]]), ('opt4v0', [[18.7, 0.0], [18.7, 2.3]]), ('opt4v1', [[20.3, 0.0], [20.3, 2.3]]), ('opt4v2', [[20.9, 0.0], [20.9, 2.3]]), ('opt4h0', [[18.0, 0.5], [21.5, 0.5]]), ('opt4h1', [[18.0, 1.2], [21.5, 1.2]]), ('opt4h2', [[18.0, 1.9], [21.5, 1.9]])]:
                c.line(points, id=object_id)
            for object_id, text, anchor in [('label0', '(A)', (1.75, -0.6)), ('label1', '(B)', (6.25, -0.6)), ('label2', '(C)', (10.75, -0.6)), ('label3', '(D)', (15.25, -0.6)), ('label4', '(E)', (19.75, -0.6))]:
                c.text(text, anchor, id=object_id)
            return c.save(output_path)

    def draw_C03(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane356_C03.png'
        _geometry_01 = [
            ('mainv0', [[8.0, 8.0], [8.0, 16.0]]), ('mainv1', [[10.2, 8.0], [10.2, 16.0]]),
            ('mainv2a', [[11.8, 8.0], [11.8, 9.6]]), ('mainv2b', [[11.8, 12.4], [11.8, 16.0]]),
            ('mainv3a', [[13.5, 8.0], [13.5, 9.6]]), ('mainv3b', [[13.5, 12.4], [13.5, 16.0]]),
            ('mainv4a', [[14.2, 8.0], [14.2, 9.6]]), ('mainv4b', [[14.2, 12.4], [14.2, 16.0]]),
            ('mainv5', [[15.0, 8.0], [15.0, 16.0]]), ('mainv6', [[15.35, 8.0], [15.35, 16.0]]),
            ('mainh0', [[6.0, 8.8], [16.0, 8.8]]), ('mainh1a', [[6.0, 9.8], [10.9, 9.8]]),
            ('mainh1b', [[14.7, 9.8], [16.0, 9.8]]), ('mainh2a', [[6.0, 10.8], [10.9, 10.8]]),
            ('mainh2b', [[14.7, 10.8], [16.0, 10.8]]), ('mainh3a', [[6.0, 11.8], [10.9, 11.8]]),
            ('mainh3b', [[14.7, 11.8], [16.0, 11.8]]), ('mainh4', [[6.0, 12.8], [16.0, 12.8]]),
            ('mainh5', [[6.0, 13.8], [16.0, 13.8]]), ('mainh6', [[6.0, 14.8], [16.0, 14.8]]),
            ('mainh7', [[6.0, 15.8], [16.0, 15.8]]), ('opt0v0', [[0.7, 0.0], [0.7, 2.3]]),
            ('opt0v1', [[2.3, 0.0], [2.3, 2.3]]), ('opt0h0', [[0.0, 0.5], [3.5, 0.5]]),
            ('opt0h1', [[0.0, 1.2], [3.5, 1.2]]), ('opt0h2', [[0.0, 1.9], [3.5, 1.9]]),
            ('opt1v0', [[5.2, 0.0], [5.2, 2.3]]), ('opt1v1', [[6.8, 0.0], [6.8, 2.3]]),
            ('opt1v2', [[7.4, 0.0], [7.4, 2.3]]), ('opt1h0', [[4.5, 0.5], [8.0, 0.5]]),
            ('opt1h1', [[4.5, 1.2], [8.0, 1.2]])
        ]
        with Canvas(PLANE, xlim=(-0.5328421672137136, 22.068639012151785), ylim=(-3.7274537952981825, 18.874027384067315)) as c:
            for object_id, points in _geometry_01:
                c.line(points, id=object_id)
            for object_id, points in [('opt2v0', [[10.2, 0.0], [10.2, 2.3]]), ('opt2v1', [[10.7, 0.0], [10.7, 2.3]]), ('opt2v2', [[11.2, 0.0], [11.2, 2.3]]), ('opt2h0', [[9.0, 0.5], [12.5, 0.5]]), ('opt2h1', [[9.0, 1.2], [12.5, 1.2]]), ('opt2h2', [[9.0, 1.9], [12.5, 1.9]])]:
                c.line(points, id=object_id, color='#EA580C', linewidth=1.5)
            for object_id, points in [('opt3v0', [[14.2, 0.0], [14.2, 2.3]]), ('opt3v1', [[15.8, 0.0], [15.8, 2.3]]), ('opt3v2', [[16.4, 0.0], [16.4, 2.3]]), ('opt3h0', [[13.5, 0.5], [17.0, 0.5]]), ('opt3h1', [[13.5, 0.75], [17.0, 0.75]]), ('opt3h2', [[13.5, 1.9], [17.0, 1.9]]), ('opt4v0', [[18.7, 0.0], [18.7, 2.3]]), ('opt4v1', [[20.3, 0.0], [20.3, 2.3]]), ('opt4v2', [[20.9, 0.0], [20.9, 2.3]]), ('opt4h0', [[18.0, 0.5], [21.5, 0.5]]), ('opt4h1', [[18.0, 1.2], [21.5, 1.2]]), ('opt4h2', [[18.0, 1.9], [21.5, 1.9]])]:
                c.line(points, id=object_id)
            for object_id, text, anchor in [('label0', '(A)', (1.75, -0.6)), ('label1', '(B)', (6.25, -0.6)), ('label2', '(C)', (10.75, -0.6)), ('label3', '(D)', (15.25, -0.6)), ('label4', '(E)', (19.75, -0.6))]:
                c.text(text, anchor, id=object_id)
            return c.save(output_path)

    def draw_C04(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane356_C04.png'
        _geometry_01 = [
            ('mainv5', [[15.0, 8.0], [15.0, 16.0]]), ('mainv6', [[15.35, 8.0], [15.35, 16.0]]),
            ('mainh0', [[6.0, 8.8], [16.0, 8.8]]), ('mainh1a', [[6.0, 9.8], [10.9, 9.8]]),
            ('mainh1b', [[14.7, 9.8], [16.0, 9.8]]), ('mainh2a', [[6.0, 10.8], [10.9, 10.8]]),
            ('mainh2b', [[14.7, 10.8], [16.0, 10.8]]), ('mainh3a', [[6.0, 11.8], [10.9, 11.8]]),
            ('mainh3b', [[14.7, 11.8], [16.0, 11.8]]), ('mainh4', [[6.0, 12.8], [16.0, 12.8]]),
            ('mainh5', [[6.0, 13.8], [16.0, 13.8]]), ('mainh6', [[6.0, 14.8], [16.0, 14.8]]),
            ('mainh7', [[6.0, 15.8], [16.0, 15.8]]), ('opt0v0', [[0.7, 0.0], [0.7, 2.3]]),
            ('opt0v1', [[2.3, 0.0], [2.3, 2.3]]), ('opt0h0', [[0.0, 0.5], [3.5, 0.5]]),
            ('opt0h1', [[0.0, 1.2], [3.5, 1.2]]), ('opt0h2', [[0.0, 1.9], [3.5, 1.9]]),
            ('opt1v0', [[5.2, 0.0], [5.2, 2.3]]), ('opt1v1', [[6.8, 0.0], [6.8, 2.3]]),
            ('opt1v2', [[7.4, 0.0], [7.4, 2.3]]), ('opt1h0', [[4.5, 0.5], [8.0, 0.5]]),
            ('opt1h1', [[4.5, 1.2], [8.0, 1.2]]), ('opt2v0', [[10.2, 0.0], [10.2, 2.3]]),
            ('opt2v1', [[10.7, 0.0], [10.7, 2.3]]), ('opt2v2', [[11.2, 0.0], [11.2, 2.3]]),
            ('opt2h0', [[9.0, 0.5], [12.5, 0.5]]), ('opt2h1', [[9.0, 1.2], [12.5, 1.2]]),
            ('opt2h2', [[9.0, 1.9], [12.5, 1.9]]), ('opt3v0', [[14.2, 0.0], [14.2, 2.3]])
        ]
        with Canvas(PLANE, xlim=(-0.5328421672137136, 22.068639012151785), ylim=(-3.7274537952981825, 18.874027384067315)) as c:
            for object_id, points in [('mainv0', [[8.0, 8.0], [8.0, 16.0]]), ('mainv1', [[10.2, 8.0], [10.2, 16.0]]), ('mainv2a', [[11.8, 8.0], [11.8, 9.6]]), ('mainv2b', [[11.8, 12.4], [11.8, 16.0]])]:
                c.line(points, id=object_id)
            for object_id, points in [('mainv3a', [[13.5, 8.0], [13.5, 9.6]]), ('mainv3b', [[13.5, 12.4], [13.5, 16.0]]), ('mainv4a', [[14.2, 8.0], [14.2, 9.6]]), ('mainv4b', [[14.2, 12.4], [14.2, 16.0]])]:
                c.line(points, id=object_id, color='#EA580C', linewidth=2.0)
            for object_id, points in _geometry_01:
                c.line(points, id=object_id)
            c.line([[15.8, 0.0], [15.8, 2.3]], id='opt3v1', color='#EA580C', linewidth=2.0)
            c.line([[16.4, 0.0], [16.4, 2.3]], id='opt3v2', color='#EA580C', linewidth=2.0)
            for object_id, points in [('opt3h0', [[13.5, 0.5], [17.0, 0.5]]), ('opt3h1', [[13.5, 0.75], [17.0, 0.75]]), ('opt3h2', [[13.5, 1.9], [17.0, 1.9]]), ('opt4v0', [[18.7, 0.0], [18.7, 2.3]]), ('opt4v1', [[20.3, 0.0], [20.3, 2.3]]), ('opt4v2', [[20.9, 0.0], [20.9, 2.3]]), ('opt4h0', [[18.0, 0.5], [21.5, 0.5]]), ('opt4h1', [[18.0, 1.2], [21.5, 1.2]]), ('opt4h2', [[18.0, 1.9], [21.5, 1.9]])]:
                c.line(points, id=object_id)
            for object_id, text, anchor in [('label0', '(A)', (1.75, -0.6)), ('label1', '(B)', (6.25, -0.6)), ('label2', '(C)', (10.75, -0.6)), ('label3', '(D)', (15.25, -0.6)), ('label4', '(E)', (19.75, -0.6))]:
                c.text(text, anchor, id=object_id)
            return c.save(output_path)

    def draw_C05(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane356_C05.png'
        with Canvas(PLANE, xlim=(-0.5328421672137136, 22.068639012151785), ylim=(-3.7274537952981825, 18.874027384067315)) as c:
            c.line([[8.0, 8.0], [8.0, 16.0]], id='mainv0')
            c.line([[10.2, 8.0], [10.2, 16.0]], id='mainv1')
            for object_id, points in [('mainv2a', [[11.8, 8.0], [11.8, 9.6]]), ('mainv2b', [[11.8, 12.4], [11.8, 16.0]]), ('mainv3a', [[13.5, 8.0], [13.5, 9.6]]), ('mainv3b', [[13.5, 12.4], [13.5, 16.0]]), ('mainv4a', [[14.2, 8.0], [14.2, 9.6]]), ('mainv4b', [[14.2, 12.4], [14.2, 16.0]])]:
                c.line(points, id=object_id, color='#DC2626', linewidth=1.5)
            for object_id, points in [('mainv5', [[15.0, 8.0], [15.0, 16.0]]), ('mainv6', [[15.35, 8.0], [15.35, 16.0]]), ('mainh0', [[6.0, 8.8], [16.0, 8.8]]), ('mainh1a', [[6.0, 9.8], [10.9, 9.8]]), ('mainh1b', [[14.7, 9.8], [16.0, 9.8]]), ('mainh2a', [[6.0, 10.8], [10.9, 10.8]]), ('mainh2b', [[14.7, 10.8], [16.0, 10.8]]), ('mainh3a', [[6.0, 11.8], [10.9, 11.8]]), ('mainh3b', [[14.7, 11.8], [16.0, 11.8]]), ('mainh4', [[6.0, 12.8], [16.0, 12.8]]), ('mainh5', [[6.0, 13.8], [16.0, 13.8]]), ('mainh6', [[6.0, 14.8], [16.0, 14.8]]), ('mainh7', [[6.0, 15.8], [16.0, 15.8]]), ('opt0v0', [[0.7, 0.0], [0.7, 2.3]]), ('opt0v1', [[2.3, 0.0], [2.3, 2.3]]), ('opt0h0', [[0.0, 0.5], [3.5, 0.5]]), ('opt0h1', [[0.0, 1.2], [3.5, 1.2]]), ('opt0h2', [[0.0, 1.9], [3.5, 1.9]]), ('opt1v0', [[5.2, 0.0], [5.2, 2.3]]), ('opt1v1', [[6.8, 0.0], [6.8, 2.3]]), ('opt1v2', [[7.4, 0.0], [7.4, 2.3]]), ('opt1h0', [[4.5, 0.5], [8.0, 0.5]]), ('opt1h1', [[4.5, 1.2], [8.0, 1.2]])]:
                c.line(points, id=object_id)
            for object_id, points in [('opt2v0', [[10.2, 0.0], [10.2, 2.3]]), ('opt2v1', [[10.7, 0.0], [10.7, 2.3]]), ('opt2v2', [[11.2, 0.0], [11.2, 2.3]])]:
                c.line(points, id=object_id, color='#DC2626', linewidth=1.5)
            for object_id, points in [('opt2h0', [[9.0, 0.5], [12.5, 0.5]]), ('opt2h1', [[9.0, 1.2], [12.5, 1.2]]), ('opt2h2', [[9.0, 1.9], [12.5, 1.9]]), ('opt3v0', [[14.2, 0.0], [14.2, 2.3]]), ('opt3v1', [[15.8, 0.0], [15.8, 2.3]]), ('opt3v2', [[16.4, 0.0], [16.4, 2.3]]), ('opt3h0', [[13.5, 0.5], [17.0, 0.5]]), ('opt3h1', [[13.5, 0.75], [17.0, 0.75]]), ('opt3h2', [[13.5, 1.9], [17.0, 1.9]]), ('opt4v0', [[18.7, 0.0], [18.7, 2.3]]), ('opt4v1', [[20.3, 0.0], [20.3, 2.3]]), ('opt4v2', [[20.9, 0.0], [20.9, 2.3]]), ('opt4h0', [[18.0, 0.5], [21.5, 0.5]]), ('opt4h1', [[18.0, 1.2], [21.5, 1.2]]), ('opt4h2', [[18.0, 1.9], [21.5, 1.9]])]:
                c.line(points, id=object_id)
            for object_id, text, anchor in [('label0', '(A)', (1.75, -0.6)), ('label1', '(B)', (6.25, -0.6)), ('label2', '(C)', (10.75, -0.6)), ('label3', '(D)', (15.25, -0.6)), ('label4', '(E)', (19.75, -0.6))]:
                c.text(text, anchor, id=object_id)
            return c.save(output_path)

    def draw_C06(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane356_C06.png'
        with Canvas(PLANE, xlim=(-0.5328421672137136, 22.068639012151785), ylim=(-3.7274537952981825, 18.874027384067315)) as c:
            c.line([[8.0, 8.0], [8.0, 16.0]], id='mainv0')
            c.line([[10.2, 8.0], [10.2, 16.0]], id='mainv1')
            for object_id, points in [('mainv2a', [[11.8, 8.0], [11.8, 9.6]]), ('mainv2b', [[11.8, 12.4], [11.8, 16.0]]), ('mainv3a', [[13.5, 8.0], [13.5, 9.6]]), ('mainv3b', [[13.5, 12.4], [13.5, 16.0]]), ('mainv4a', [[14.2, 8.0], [14.2, 9.6]]), ('mainv4b', [[14.2, 12.4], [14.2, 16.0]])]:
                c.line(points, id=object_id, color='#2563EB', linewidth=1.5)
            for object_id, points in self._g01:
                c.line(points, id=object_id)
            for object_id, points in [('opt3v0', [[14.2, 0.0], [14.2, 2.3]]), ('opt3v1', [[15.8, 0.0], [15.8, 2.3]]), ('opt3v2', [[16.4, 0.0], [16.4, 2.3]])]:
                c.line(points, id=object_id, color='#2563EB', linewidth=1.5)
            for object_id, points in [('opt3h0', [[13.5, 0.5], [17.0, 0.5]]), ('opt3h1', [[13.5, 0.75], [17.0, 0.75]]), ('opt3h2', [[13.5, 1.9], [17.0, 1.9]]), ('opt4v0', [[18.7, 0.0], [18.7, 2.3]]), ('opt4v1', [[20.3, 0.0], [20.3, 2.3]]), ('opt4v2', [[20.9, 0.0], [20.9, 2.3]]), ('opt4h0', [[18.0, 0.5], [21.5, 0.5]]), ('opt4h1', [[18.0, 1.2], [21.5, 1.2]]), ('opt4h2', [[18.0, 1.9], [21.5, 1.9]])]:
                c.line(points, id=object_id)
            for object_id, text, anchor in [('label0', '(A)', (1.75, -0.6)), ('label1', '(B)', (6.25, -0.6)), ('label2', '(C)', (10.75, -0.6)), ('label3', '(D)', (15.25, -0.6)), ('label4', '(E)', (19.75, -0.6))]:
                c.text(text, anchor, id=object_id)
            return c.save(output_path)
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Plane356')
    parser.add_argument('output', nargs='?')
    parser.add_argument('--variant', choices=('C01', 'C02', 'C03', 'C04', 'C05', 'C06'))
    args = parser.parse_args()
    print(Plane356().draw(args.output, variant=args.variant))
