"""Frozen question Plane505; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane505:

    def __init__(self):
        self.id = 'Plane505'
        self.source_dataset = 'Author Designed'
        self.source_key = 'authored-extension:Plane356:ext04'
        self.question = 'Which rectangular piece was cut from the nonuniform grid? Each candidate is shown at the same reduced scale and in the original orientation; the correct piece must restore every broken vertical and horizontal line.\nChoices:\nA:A\nB:B\nC:C\nD:D\nE:E'
        self.answer = 'E'
        self.answer_type = 'choice'
        self.choices = {'A': 'A', 'B': 'B', 'C': 'C', 'D': 'D', 'E': 'E'}
        self.query = self.question
        self.points = {'P0001': [6.2, 8.6],
         'P0002': [6.2, 21.6],
         'P0003': [8.1, 8.6],
         'P0004': [8.1, 21.6],
         'P0005': [10.4, 8.6],
         'P0006': [10.4, 21.6],
         'P0007': [12.7, 8.6],
         'P0008': [12.7, 11.5],
         'P0009': [12.7, 18.7],
         'P0010': [12.7, 21.6],
         'P0011': [14, 8.6],
         'P0012': [14, 11.5],
         'P0013': [14, 18.7],
         'P0014': [14, 21.6],
         'P0015': [15.8, 8.6],
         'P0016': [15.8, 11.5],
         'P0017': [15.8, 18.7],
         'P0018': [15.8, 21.6],
         'P0019': [18.6, 8.6],
         'P0020': [18.6, 11.5],
         'P0021': [18.6, 18.7],
         'P0022': [18.6, 21.6],
         'P0023': [20.8, 8.6],
         'P0024': [20.8, 21.6],
         'P0025': [5.6, 9.2],
         'P0026': [21.4, 9.2],
         'P0027': [5.6, 10.6],
         'P0028': [21.4, 10.6],
         'P0029': [5.6, 12.4],
         'P0030': [10.9, 12.4],
         'P0031': [19.5, 12.4],
         'P0032': [21.4, 12.4],
         'P0033': [5.6, 14.2],
         'P0034': [10.9, 14.2],
         'P0035': [19.5, 14.2],
         'P0036': [21.4, 14.2],
         'P0037': [5.6, 15.1],
         'P0038': [10.9, 15.1],
         'P0039': [19.5, 15.1],
         'P0040': [21.4, 15.1],
         'P0041': [5.6, 17.8],
         'P0042': [10.9, 17.8],
         'P0043': [19.5, 17.8],
         'P0044': [21.4, 17.8],
         'P0045': [5.6, 19.4],
         'P0046': [21.4, 19.4],
         'P0047': [5.6, 21],
         'P0048': [21.4, 21],
         'P0049': [1.2872093023255808, 0],
         'P0050': [1.2872093023255808, 3.3488372093023253],
         'P0051': [1.541860465116279, 0],
         'P0052': [1.541860465116279, 3.3488372093023253],
         'P0053': [2.3790697674418606, 0],
         'P0054': [2.3790697674418606, 3.3488372093023253],
         'P0055': [3.68139534883721, 0],
         'P0056': [3.68139534883721, 3.3488372093023253],
         'P0057': [0.1, 0.4186046511627909],
         'P0058': [4.1, 0.4186046511627909],
         'P0059': [0.1, 1.2558139534883719],
         'P0060': [4.1, 1.2558139534883719],
         'P0061': [0.1, 1.6744186046511627],
         'P0062': [4.1, 1.6744186046511627],
         'P0063': [0.1, 2.930232558139535],
         'P0064': [4.1, 2.930232558139535],
         'P0065': [6.53720930232558, 0],
         'P0066': [6.53720930232558, 3.3488372093023253],
         'P0067': [7.141860465116278, 0],
         'P0068': [7.141860465116278, 3.3488372093023253],
         'P0069': [7.97906976744186, 0],
         'P0070': [7.97906976744186, 3.3488372093023253],
         'P0071': [9.28139534883721, 0],
         'P0072': [9.28139534883721, 3.3488372093023253],
         'P0073': [5.699999999999999, 0.4186046511627909],
         'P0074': [9.7, 0.4186046511627909],
         'P0075': [5.699999999999999, 1.655813953488372],
         'P0076': [9.7, 1.655813953488372],
         'P0077': [5.699999999999999, 1.6744186046511627],
         'P0078': [9.7, 1.6744186046511627],
         'P0079': [5.699999999999999, 2.930232558139535],
         'P0080': [9.7, 2.930232558139535],
         'P0081': [12.13720930232558, 0],
         'P0082': [12.13720930232558, 3.3488372093023253],
         'P0083': [12.741860465116279, 0],
         'P0084': [12.741860465116279, 3.3488372093023253],
         'P0085': [13.57906976744186, 0],
         'P0086': [13.57906976744186, 3.3488372093023253],
         'P0087': [14.581395348837209, 0],
         'P0088': [14.581395348837209, 3.3488372093023253],
         'P0089': [11.299999999999999, 0.4186046511627909],
         'P0090': [15.299999999999999, 0.4186046511627909],
         'P0091': [11.299999999999999, 1.2558139534883719],
         'P0092': [15.299999999999999, 1.2558139534883719],
         'P0093': [11.299999999999999, 1.6744186046511627],
         'P0094': [15.299999999999999, 1.6744186046511627],
         'P0095': [11.299999999999999, 2.930232558139535],
         'P0096': [15.299999999999999, 2.930232558139535],
         'P0097': [17.737209302325578, 0],
         'P0098': [17.737209302325578, 3.3488372093023253],
         'P0099': [18.341860465116277, 0],
         'P0100': [18.341860465116277, 3.3488372093023253],
         'P0101': [19.17906976744186, 0],
         'P0102': [19.17906976744186, 3.3488372093023253],
         'P0103': [20.481395348837207, 0],
         'P0104': [20.481395348837207, 3.3488372093023253],
         'P0105': [16.9, 0.4186046511627909],
         'P0106': [20.9, 0.4186046511627909],
         'P0107': [16.9, 1.6744186046511627],
         'P0108': [20.9, 1.6744186046511627],
         'P0109': [16.9, 2.930232558139535],
         'P0110': [20.9, 2.930232558139535],
         'P0111': [23.33720930232558, 0],
         'P0112': [23.33720930232558, 3.3488372093023253],
         'P0113': [23.941860465116278, 0],
         'P0114': [23.941860465116278, 3.3488372093023253],
         'P0115': [24.77906976744186, 0],
         'P0116': [24.77906976744186, 3.3488372093023253],
         'P0117': [26.08139534883721, 0],
         'P0118': [26.08139534883721, 3.3488372093023253],
         'P0119': [22.5, 0.4186046511627909],
         'P0120': [26.5, 0.4186046511627909],
         'P0121': [22.5, 1.2558139534883719],
         'P0122': [26.5, 1.2558139534883719],
         'P0123': [22.5, 1.6744186046511627],
         'P0124': [26.5, 1.6744186046511627],
         'P0125': [22.5, 2.930232558139535],
         'P0126': [26.5, 2.930232558139535]}
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane505.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-0.5490148578811365, 27.203528746770026], ylim=[-3.704396802325581, 24.048146802325583]) as c:
            for object_id, points in [('mainv0', [self.points['P0001'], self.points['P0002']]), ('mainv1', [self.points['P0003'], self.points['P0004']]), ('mainv2', [self.points['P0005'], self.points['P0006']]), ('mainv3a', [self.points['P0007'], self.points['P0008']]), ('mainv3b', [self.points['P0009'], self.points['P0010']]), ('mainv4a', [self.points['P0011'], self.points['P0012']]), ('mainv4b', [self.points['P0013'], self.points['P0014']]), ('mainv5a', [self.points['P0015'], self.points['P0016']]), ('mainv5b', [self.points['P0017'], self.points['P0018']]), ('mainv6a', [self.points['P0019'], self.points['P0020']]), ('mainv6b', [self.points['P0021'], self.points['P0022']]), ('mainv7', [self.points['P0023'], self.points['P0024']]), ('mainh0', [self.points['P0025'], self.points['P0026']]), ('mainh1', [self.points['P0027'], self.points['P0028']]), ('mainh2a', [self.points['P0029'], self.points['P0030']]), ('mainh2b', [self.points['P0031'], self.points['P0032']]), ('mainh3a', [self.points['P0033'], self.points['P0034']]), ('mainh3b', [self.points['P0035'], self.points['P0036']]), ('mainh4a', [self.points['P0037'], self.points['P0038']]), ('mainh4b', [self.points['P0039'], self.points['P0040']]), ('mainh5a', [self.points['P0041'], self.points['P0042']]), ('mainh5b', [self.points['P0043'], self.points['P0044']]), ('mainh6', [self.points['P0045'], self.points['P0046']]), ('mainh7', [self.points['P0047'], self.points['P0048']]), ('opt0v0', [self.points['P0049'], self.points['P0050']]), ('opt0v1', [self.points['P0051'], self.points['P0052']]), ('opt0v2', [self.points['P0053'], self.points['P0054']]), ('opt0v3', [self.points['P0055'], self.points['P0056']]), ('opt0h0', [self.points['P0057'], self.points['P0058']]), ('opt0h1', [self.points['P0059'], self.points['P0060']]), ('opt0h2', [self.points['P0061'], self.points['P0062']]), ('opt0h3', [self.points['P0063'], self.points['P0064']]), ('opt1v0', [self.points['P0065'], self.points['P0066']]), ('opt1v1', [self.points['P0067'], self.points['P0068']]), ('opt1v2', [self.points['P0069'], self.points['P0070']]), ('opt1v3', [self.points['P0071'], self.points['P0072']]), ('opt1h0', [self.points['P0073'], self.points['P0074']]), ('opt1h1', [self.points['P0075'], self.points['P0076']]), ('opt1h2', [self.points['P0077'], self.points['P0078']]), ('opt1h3', [self.points['P0079'], self.points['P0080']]), ('opt2v0', [self.points['P0081'], self.points['P0082']]), ('opt2v1', [self.points['P0083'], self.points['P0084']]), ('opt2v2', [self.points['P0085'], self.points['P0086']]), ('opt2v3', [self.points['P0087'], self.points['P0088']]), ('opt2h0', [self.points['P0089'], self.points['P0090']]), ('opt2h1', [self.points['P0091'], self.points['P0092']]), ('opt2h2', [self.points['P0093'], self.points['P0094']]), ('opt2h3', [self.points['P0095'], self.points['P0096']]), ('opt3v0', [self.points['P0097'], self.points['P0098']]), ('opt3v1', [self.points['P0099'], self.points['P0100']]), ('opt3v2', [self.points['P0101'], self.points['P0102']]), ('opt3v3', [self.points['P0103'], self.points['P0104']]), ('opt3h0', [self.points['P0105'], self.points['P0106']]), ('opt3h1', [self.points['P0107'], self.points['P0108']]), ('opt3h2', [self.points['P0109'], self.points['P0110']]), ('opt4v0', [self.points['P0111'], self.points['P0112']]), ('opt4v1', [self.points['P0113'], self.points['P0114']]), ('opt4v2', [self.points['P0115'], self.points['P0116']]), ('opt4v3', [self.points['P0117'], self.points['P0118']]), ('opt4h0', [self.points['P0119'], self.points['P0120']]), ('opt4h1', [self.points['P0121'], self.points['P0122']]), ('opt4h2', [self.points['P0123'], self.points['P0124']]), ('opt4h3', [self.points['P0125'], self.points['P0126']])]:
                c.line(points, id=object_id)
            for object_id, text, anchor in [('label0', 'A', [2.1, -1]), ('label1', 'B', [7.699999999999999, -1]), ('label2', 'C', [13.299999999999999, -1]), ('label3', 'D', [18.9, -1]), ('label4', 'E', [24.5, -1])]:
                c.text(text, anchor, id=object_id, offset_pt=[0, 0], vertex=False)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane505().draw(sys.argv[1] if len(sys.argv) > 1 else None))
