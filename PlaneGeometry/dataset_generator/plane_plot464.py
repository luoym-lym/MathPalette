"""Frozen question Plane464; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane464:

    def __init__(self):
        self.id = 'Plane464'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:2639'
        self.question = 'Which of the following polygons has the largest area?\n\nChoices:\nA:$\\text{A}$\nB:$\\text{B}$\nC:$\\text{C}$\nD:$\\text{D}$\nE:$\\text{E}$'
        self.answer = 'E'
        self.answer_type = 'choice'
        self.choices = {'A': '$\\text{A}$', 'B': '$\\text{B}$', 'C': '$\\text{C}$', 'D': '$\\text{D}$', 'E': '$\\text{E}$'}
        self.query = self.question
        self.points = {'p000': [0, 0],
         'p001': [0, 1],
         'p002': [0, 2],
         'p003': [0, 3],
         'p004': [0, 4],
         'p010': [1, 0],
         'p011': [1, 1],
         'p012': [1, 2],
         'p013': [1, 3],
         'p014': [1, 4],
         'p020': [2, 0],
         'p021': [2, 1],
         'p022': [2, 2],
         'p023': [2, 3],
         'p024': [2, 4],
         'p030': [3, 0],
         'p031': [3, 1],
         'p032': [3, 2],
         'p033': [3, 3],
         'p034': [3, 4],
         'p040': [4, 0],
         'p041': [4, 1],
         'p042': [4, 2],
         'p043': [4, 3],
         'p044': [4, 4],
         'poly00': [0, 0],
         'poly01': [1, 1],
         'poly02': [2, 1],
         'poly03': [2, 3],
         'poly04': [3, 3],
         'poly05': [3, 1],
         'poly06': [4, 0],
         'name0': [2, -0.5],
         'p100': [6, 0],
         'p101': [6, 1],
         'p102': [6, 2],
         'p103': [6, 3],
         'p104': [6, 4],
         'p110': [7, 0],
         'p111': [7, 1],
         'p112': [7, 2],
         'p113': [7, 3],
         'p114': [7, 4],
         'p120': [8, 0],
         'p121': [8, 1],
         'p122': [8, 2],
         'p123': [8, 3],
         'p124': [8, 4],
         'p130': [9, 0],
         'p131': [9, 1],
         'p132': [9, 2],
         'p133': [9, 3],
         'p134': [9, 4],
         'p140': [10, 0],
         'p141': [10, 1],
         'p142': [10, 2],
         'p143': [10, 3],
         'p144': [10, 4],
         'poly10': [6, 0],
         'poly11': [6, 2],
         'poly12': [7, 1],
         'poly13': [8, 1],
         'poly14': [9, 2],
         'poly15': [9, 1],
         'poly16': [10, 1],
         'poly17': [10, 0],
         'name1': [8, -0.5],
         'p200': [12, 0],
         'p201': [12, 1],
         'p202': [12, 2],
         'p203': [12, 3],
         'p204': [12, 4],
         'p210': [13, 0],
         'p211': [13, 1],
         'p212': [13, 2],
         'p213': [13, 3],
         'p214': [13, 4],
         'p220': [14, 0],
         'p221': [14, 1],
         'p222': [14, 2],
         'p223': [14, 3],
         'p224': [14, 4],
         'p230': [15, 0],
         'p231': [15, 1],
         'p232': [15, 2],
         'p233': [15, 3],
         'p234': [15, 4],
         'p240': [16, 0],
         'p241': [16, 1],
         'p242': [16, 2],
         'p243': [16, 3],
         'p244': [16, 4],
         'poly20': [12, 4],
         'poly21': [13, 3],
         'poly22': [13, 1],
         'poly23': [15, 3],
         'poly24': [15, 2],
         'poly25': [13, 0],
         'poly26': [12, 1],
         'name2': [14, -0.5],
         'p300': [18, 0],
         'p301': [18, 1],
         'p302': [18, 2],
         'p303': [18, 3],
         'p304': [18, 4],
         'p310': [19, 0],
         'p311': [19, 1],
         'p312': [19, 2],
         'p313': [19, 3],
         'p314': [19, 4],
         'p320': [20, 0],
         'p321': [20, 1],
         'p322': [20, 2],
         'p323': [20, 3],
         'p324': [20, 4],
         'p330': [21, 0],
         'p331': [21, 1],
         'p332': [21, 2],
         'p333': [21, 3],
         'p334': [21, 4],
         'p340': [22, 0],
         'p341': [22, 1],
         'p342': [22, 2],
         'p343': [22, 3],
         'p344': [22, 4],
         'poly30': [18, 1],
         'poly31': [18, 2],
         'poly32': [19, 2],
         'poly33': [19, 3],
         'poly34': [20, 2],
         'poly35': [21, 3],
         'poly36': [21, 0],
         'poly37': [20, 1],
         'name3': [20, -0.5],
         'p400': [24, 0],
         'p401': [24, 1],
         'p402': [24, 2],
         'p403': [24, 3],
         'p404': [24, 4],
         'p410': [25, 0],
         'p411': [25, 1],
         'p412': [25, 2],
         'p413': [25, 3],
         'p414': [25, 4],
         'p420': [26, 0],
         'p421': [26, 1],
         'p422': [26, 2],
         'p423': [26, 3],
         'p424': [26, 4],
         'p430': [27, 0],
         'p431': [27, 1],
         'p432': [27, 2],
         'p433': [27, 3],
         'p434': [27, 4],
         'p440': [28, 0],
         'p441': [28, 1],
         'p442': [28, 2],
         'p443': [28, 3],
         'p444': [28, 4],
         'poly40': [24, 4],
         'poly41': [27, 4],
         'poly42': [27, 2],
         'poly43': [26, 3],
         'poly44': [26, 1],
         'poly45': [25, 0],
         'poly46': [25, 3],
         'name4': [26, -0.5]}
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane464.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-0.8884221966597146, 28.935075674350557], ylim=[-13.444611732118823, 16.37888613889145]) as c:
            for object_id, points in [('p000', [self.points['p000']]), ('p001', [self.points['p001']]), ('p002', [self.points['p002']]), ('p003', [self.points['p003']]), ('p004', [self.points['p004']]), ('p010', [self.points['p010']]), ('p011', [self.points['p011']]), ('p012', [self.points['p012']]), ('p013', [self.points['p013']]), ('p014', [self.points['p014']]), ('p020', [self.points['p020']]), ('p021', [self.points['p021']]), ('p022', [self.points['p022']]), ('p023', [self.points['p023']]), ('p024', [self.points['p024']]), ('p030', [self.points['p030']]), ('p031', [self.points['p031']]), ('p032', [self.points['p032']]), ('p033', [self.points['p033']]), ('p034', [self.points['p034']]), ('p040', [self.points['p040']]), ('p041', [self.points['p041']]), ('p042', [self.points['p042']]), ('p043', [self.points['p043']]), ('p044', [self.points['p044']])]:
                c.point(points, id=object_id, filled=True)
            c.path([self.points['poly00'], self.points['poly01'], self.points['poly02'], self.points['poly03'], self.points['poly04'], self.points['poly05'], self.points['poly06'], self.points['poly00']], [1, 2, 2, 2, 2, 2, 2, 79], id='poly0')
            for object_id, points in [('p100', [self.points['p100']]), ('p101', [self.points['p101']]), ('p102', [self.points['p102']]), ('p103', [self.points['p103']]), ('p104', [self.points['p104']]), ('p110', [self.points['p110']]), ('p111', [self.points['p111']]), ('p112', [self.points['p112']]), ('p113', [self.points['p113']]), ('p114', [self.points['p114']]), ('p120', [self.points['p120']]), ('p121', [self.points['p121']]), ('p122', [self.points['p122']]), ('p123', [self.points['p123']]), ('p124', [self.points['p124']]), ('p130', [self.points['p130']]), ('p131', [self.points['p131']]), ('p132', [self.points['p132']]), ('p133', [self.points['p133']]), ('p134', [self.points['p134']]), ('p140', [self.points['p140']]), ('p141', [self.points['p141']]), ('p142', [self.points['p142']]), ('p143', [self.points['p143']]), ('p144', [self.points['p144']])]:
                c.point(points, id=object_id, filled=True)
            c.path([self.points['poly10'], self.points['poly11'], self.points['poly12'], self.points['poly13'], self.points['poly14'], self.points['poly15'], self.points['poly16'], self.points['poly17'], self.points['poly10']], [1, 2, 2, 2, 2, 2, 2, 2, 79], id='poly1')
            for object_id, points in [('p200', [self.points['p200']]), ('p201', [self.points['p201']]), ('p202', [self.points['p202']]), ('p203', [self.points['p203']]), ('p204', [self.points['p204']]), ('p210', [self.points['p210']]), ('p211', [self.points['p211']]), ('p212', [self.points['p212']]), ('p213', [self.points['p213']]), ('p214', [self.points['p214']]), ('p220', [self.points['p220']]), ('p221', [self.points['p221']]), ('p222', [self.points['p222']]), ('p223', [self.points['p223']]), ('p224', [self.points['p224']]), ('p230', [self.points['p230']]), ('p231', [self.points['p231']]), ('p232', [self.points['p232']]), ('p233', [self.points['p233']]), ('p234', [self.points['p234']]), ('p240', [self.points['p240']]), ('p241', [self.points['p241']]), ('p242', [self.points['p242']]), ('p243', [self.points['p243']]), ('p244', [self.points['p244']])]:
                c.point(points, id=object_id, filled=True)
            c.path([self.points['poly20'], self.points['poly21'], self.points['poly22'], self.points['poly23'], self.points['poly24'], self.points['poly25'], self.points['poly26'], self.points['poly20']], [1, 2, 2, 2, 2, 2, 2, 79], id='poly2')
            for object_id, points in [('p300', [self.points['p300']]), ('p301', [self.points['p301']]), ('p302', [self.points['p302']]), ('p303', [self.points['p303']]), ('p304', [self.points['p304']]), ('p310', [self.points['p310']]), ('p311', [self.points['p311']]), ('p312', [self.points['p312']]), ('p313', [self.points['p313']]), ('p314', [self.points['p314']]), ('p320', [self.points['p320']]), ('p321', [self.points['p321']]), ('p322', [self.points['p322']]), ('p323', [self.points['p323']]), ('p324', [self.points['p324']]), ('p330', [self.points['p330']]), ('p331', [self.points['p331']]), ('p332', [self.points['p332']]), ('p333', [self.points['p333']]), ('p334', [self.points['p334']]), ('p340', [self.points['p340']]), ('p341', [self.points['p341']]), ('p342', [self.points['p342']]), ('p343', [self.points['p343']]), ('p344', [self.points['p344']])]:
                c.point(points, id=object_id, filled=True)
            c.path([self.points['poly30'], self.points['poly31'], self.points['poly32'], self.points['poly33'], self.points['poly34'], self.points['poly35'], self.points['poly36'], self.points['poly37'], self.points['poly30']], [1, 2, 2, 2, 2, 2, 2, 2, 79], id='poly3')
            for object_id, points in [('p400', [self.points['p400']]), ('p401', [self.points['p401']]), ('p402', [self.points['p402']]), ('p403', [self.points['p403']]), ('p404', [self.points['p404']]), ('p410', [self.points['p410']]), ('p411', [self.points['p411']]), ('p412', [self.points['p412']]), ('p413', [self.points['p413']]), ('p414', [self.points['p414']]), ('p420', [self.points['p420']]), ('p421', [self.points['p421']]), ('p422', [self.points['p422']]), ('p423', [self.points['p423']]), ('p424', [self.points['p424']]), ('p430', [self.points['p430']]), ('p431', [self.points['p431']]), ('p432', [self.points['p432']]), ('p433', [self.points['p433']]), ('p434', [self.points['p434']]), ('p440', [self.points['p440']]), ('p441', [self.points['p441']]), ('p442', [self.points['p442']]), ('p443', [self.points['p443']]), ('p444', [self.points['p444']])]:
                c.point(points, id=object_id, filled=True)
            c.path([self.points['poly40'], self.points['poly41'], self.points['poly42'], self.points['poly43'], self.points['poly44'], self.points['poly45'], self.points['poly46'], self.points['poly40']], [1, 2, 2, 2, 2, 2, 2, 79], id='poly4')
            for object_id, text, anchor in [('name0', 'A', self.points['name0']), ('name1', 'B', self.points['name1']), ('name2', 'C', self.points['name2']), ('name3', 'D', self.points['name3']), ('name4', 'E', self.points['name4'])]:
                c.text(text, anchor, id=object_id, offset_pt=[0, -9], vertex=False)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane464().draw(sys.argv[1] if len(sys.argv) > 1 else None))
