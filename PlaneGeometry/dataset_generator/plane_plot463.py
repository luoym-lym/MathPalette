"""Frozen question Plane463; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane463:

    def __init__(self):
        self.id = 'Plane463'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:2625'
        self.question = 'A small kite and a large kite have the shape shown in the diagram. The small kite is drawn on a one-inch grid. For the large kite, both the height and width of the entire grid are tripled.\n\nWhat is the area of the small kite in square inches?'
        self.answer = '21'
        self.answer_type = 'number'
        self.query = self.question
        self.points = {'p00': [0, 0],
         'p01': [0, 1],
         'p02': [0, 2],
         'p03': [0, 3],
         'p04': [0, 4],
         'p05': [0, 5],
         'p06': [0, 6],
         'p07': [0, 7],
         'p10': [1, 0],
         'p11': [1, 1],
         'p12': [1, 2],
         'p13': [1, 3],
         'p14': [1, 4],
         'p15': [1, 5],
         'p16': [1, 6],
         'p17': [1, 7],
         'p20': [2, 0],
         'p21': [2, 1],
         'p22': [2, 2],
         'p23': [2, 3],
         'p24': [2, 4],
         'p25': [2, 5],
         'p26': [2, 6],
         'p27': [2, 7],
         'p30': [3, 0],
         'p31': [3, 1],
         'p32': [3, 2],
         'p33': [3, 3],
         'p34': [3, 4],
         'p35': [3, 5],
         'p36': [3, 6],
         'p37': [3, 7],
         'p40': [4, 0],
         'p41': [4, 1],
         'p42': [4, 2],
         'p43': [4, 3],
         'p44': [4, 4],
         'p45': [4, 5],
         'p46': [4, 6],
         'p47': [4, 7],
         'p50': [5, 0],
         'p51': [5, 1],
         'p52': [5, 2],
         'p53': [5, 3],
         'p54': [5, 4],
         'p55': [5, 5],
         'p56': [5, 6],
         'p57': [5, 7],
         'p60': [6, 0],
         'p61': [6, 1],
         'p62': [6, 2],
         'p63': [6, 3],
         'p64': [6, 4],
         'p65': [6, 5],
         'p66': [6, 6],
         'p67': [6, 7]}
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane463.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-0.7221140278577654, 6.733760439894802], ylim=[-0.23376891858763882, 7.222105549164928]) as c:
            for object_id, points in [('p00', [self.points['p00']]), ('p01', [self.points['p01']]), ('p02', [self.points['p02']]), ('p03', [self.points['p03']]), ('p04', [self.points['p04']]), ('p05', [self.points['p05']]), ('p06', [self.points['p06']]), ('p07', [self.points['p07']]), ('p10', [self.points['p10']]), ('p11', [self.points['p11']]), ('p12', [self.points['p12']]), ('p13', [self.points['p13']]), ('p14', [self.points['p14']]), ('p15', [self.points['p15']]), ('p16', [self.points['p16']]), ('p17', [self.points['p17']]), ('p20', [self.points['p20']]), ('p21', [self.points['p21']]), ('p22', [self.points['p22']]), ('p23', [self.points['p23']]), ('p24', [self.points['p24']]), ('p25', [self.points['p25']]), ('p26', [self.points['p26']]), ('p27', [self.points['p27']]), ('p30', [self.points['p30']]), ('p31', [self.points['p31']]), ('p32', [self.points['p32']]), ('p33', [self.points['p33']]), ('p34', [self.points['p34']]), ('p35', [self.points['p35']]), ('p36', [self.points['p36']]), ('p37', [self.points['p37']]), ('p40', [self.points['p40']]), ('p41', [self.points['p41']]), ('p42', [self.points['p42']]), ('p43', [self.points['p43']]), ('p44', [self.points['p44']]), ('p45', [self.points['p45']]), ('p46', [self.points['p46']]), ('p47', [self.points['p47']]), ('p50', [self.points['p50']]), ('p51', [self.points['p51']]), ('p52', [self.points['p52']]), ('p53', [self.points['p53']]), ('p54', [self.points['p54']]), ('p55', [self.points['p55']]), ('p56', [self.points['p56']]), ('p57', [self.points['p57']]), ('p60', [self.points['p60']]), ('p61', [self.points['p61']]), ('p62', [self.points['p62']]), ('p63', [self.points['p63']]), ('p64', [self.points['p64']]), ('p65', [self.points['p65']]), ('p66', [self.points['p66']]), ('p67', [self.points['p67']])]:
                c.point(points, id=object_id, filled=True)
            c.path([self.points['p37'], self.points['p65'], self.points['p30'], self.points['p05'], self.points['p37']], [1, 2, 2, 2, 79], id='kite')
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane463().draw(sys.argv[1] if len(sys.argv) > 1 else None))
