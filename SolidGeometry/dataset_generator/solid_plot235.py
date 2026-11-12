"""Frozen question Solid235; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Solid235:

    def __init__(self):
        self.id = 'Solid235'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:2704'
        self.question = 'A one-cubic-foot cube is cut into four pieces by three cuts parallel to the top face of the cube. The first cut is $\\frac{1}{2}$ foot from the top face. The second cut is $\\frac{1}{3}$ foot below the first cut, and the third cut is $\\frac{1}{17}$ foot below the second cut. From the top to the bottom the pieces are labeled A, B, C, and D. The pieces are then glued together end to end as shown in the second diagram. What is the total surface area of this solid in square feet?\n\nChoices:\nA:6$\nB:$7$\nC:$\\frac{419}{51}$\nD:$\\frac{158}{17}$\nE:$11$'
        self.answer = 'E'
        self.answer_type = 'choice'
        self.choices = {'A': '6$', 'B': '$7$', 'C': '$\\frac{419}{51}$', 'D': '$\\frac{158}{17}$', 'E': '$11$'}
        self.query = self.question
        self.points = {'blockp0': [0.0, 0.0, 2.2],
         'blockp1': [1.0, 0.0, 2.2],
         'blockp2': [0.0, 0.0, 3.2],
         'blockp3': [1.0, 0.0, 3.2],
         'blockp4': [0.0, 1.0, 3.2],
         'blockp5': [1.0, 1.0, 3.2],
         'blockp6': [0.0, 0.0, 3.2],
         'blockp7': [0.0, 1.0, 3.2],
         'blockp8': [1.0, 0.0, 2.2],
         'blockp9': [1.0, 1.0, 2.2],
         'blockp10': [1.0, 0.0, 3.2],
         'blockp11': [1.0, 1.0, 3.2],
         'blockp12': [0.0, 0.0, 2.2],
         'blockp13': [0.0, 0.0, 3.2],
         'blockp14': [1.0, 0.0, 2.2],
         'blockp15': [1.0, 0.0, 3.2],
         'blockp16': [1.0, 1.0, 2.2],
         'blockp17': [1.0, 1.0, 3.2],
         'a0': [0, 0, 2.307843137254902],
         'b0': [1, 0, 2.307843137254902],
         'c0': [1, 1, 2.307843137254902],
         'a1': [0, 0, 2.3666666666666667],
         'b1': [1, 0, 2.3666666666666667],
         'c1': [1, 1, 2.3666666666666667],
         'a2': [0, 0, 2.7],
         'b2': [1, 0, 2.7],
         'c2': [1, 1, 2.7],
         'Atop': [0, 0, 2.95],
         'Afraction': [1, 0, 2.95],
         'Btop': [0, 0, 2.5333333333333337],
         'Bfraction': [1, 0, 2.5333333333333337],
         'Ctop': [0, 0, 2.3372549019607844],
         'Cfraction': [1, 1, 2.3372549019607844],
         'Dtop': [0, 0, 2.2539215686274514],
         'Cbottom': [0.4, 0.5, 0],
         'Bbottom': [0.4, 1.5, 0],
         'Abottom': [0.4, 2.5, 0],
         'Dbottom': [0.4, 3.5, 0],
         'lowerblockp0': [-0.6, 0.0, 0.0],
         'lowerblockp1': [0.4, 0.0, 0.0],
         'lowerblockp2': [-0.6, 0.0, 0.05882353],
         'lowerblockp3': [0.4, 0.0, 0.05882353],
         'lowerblockp4': [-0.6, 1.0, 0.05882353],
         'lowerblockp5': [0.4, 1.0, 0.05882353],
         'lowerblockp6': [-0.6, 0.0, 0.05882353],
         'lowerblockp7': [-0.6, 1.0, 0.05882353],
         'lowerblockp8': [0.4, 0.0, 0.0],
         'lowerblockp9': [0.4, 4.0, 0.0],
         'lowerblockp10': [0.4, 0.0, 0.05882353],
         'lowerblockp11': [0.4, 1.0, 0.05882353],
         'lowerblockp12': [-0.6, 0.0, 0.0],
         'lowerblockp13': [-0.6, 0.0, 0.058823529411764705],
         'lowerblockp14': [0.4, 0.0, 0.0],
         'lowerblockp15': [0.4, 0.0, 0.058823529411764705],
         'lowerblockp16': [0.4, 1.0, 0.0],
         'lowerblockp17': [0.4, 1.0, 0.3333333333333333],
         'lowerblockp18': [-0.6, 1.0, 0.33333333],
         'lowerblockp19': [0.4, 1.0, 0.33333333],
         'lowerblockp20': [-0.6, 2.0, 0.33333333],
         'lowerblockp21': [0.4, 2.0, 0.33333333],
         'lowerblockp22': [-0.6, 1.0, 0.33333333],
         'lowerblockp23': [-0.6, 2.0, 0.33333333],
         'lowerblockp24': [0.4, 1.0, 0.33333333],
         'lowerblockp25': [0.4, 2.0, 0.33333333],
         'lowerblockp26': [-0.6, 1.0, 0.058823529411764705],
         'lowerblockp27': [-0.6, 1.0, 0.3333333333333333],
         'lowerblockp28': [0.4, 2.0, 0.0],
         'lowerblockp29': [0.4, 2.0, 0.5],
         'lowerblockp30': [-0.6, 2.0, 0.5],
         'lowerblockp31': [0.4, 2.0, 0.5],
         'lowerblockp32': [-0.6, 3.0, 0.5],
         'lowerblockp33': [0.4, 3.0, 0.5],
         'lowerblockp34': [-0.6, 2.0, 0.5],
         'lowerblockp35': [-0.6, 3.0, 0.5],
         'lowerblockp36': [0.4, 2.0, 0.5],
         'lowerblockp37': [0.4, 3.0, 0.5],
         'lowerblockp38': [-0.6, 2.0, 0.3333333333333333],
         'lowerblockp39': [-0.6, 2.0, 0.5],
         'lowerblockp40': [0.4, 3.0, 0.0],
         'lowerblockp41': [0.4, 3.0, 0.5],
         'lowerblockp42': [-0.6, 4.0, 0.10784314],
         'lowerblockp43': [0.4, 4.0, 0.10784314],
         'lowerblockp44': [-0.6, 3.8003201280512204, 0.10784314],
         'lowerblockp45': [-0.6, 4.0, 0.10784314],
         'lowerblockp46': [0.4, 3.0, 0.10784314],
         'lowerblockp47': [0.4, 4.0, 0.10784314],
         'lowerblockp48': [0.4, 4.0, 0.0],
         'lowerblockp49': [0.4, 4.0, 0.10784313725490197]}
        self.subject = 'SolidGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'SolidGeometry' / 'dataset_generator/scenes/Solid235.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('SolidGeometry', self.id, variant, output_path)
        with Canvas(SOLID, xlim=[-0.8213494325399004, 3.028762626984345], ylim=[-0.1587563770686744, 3.691355682455571], projection=[[1, 0.6, 0], [-0.15, 0.4, 1]], origin=[0, 0, 0], offset=[0, 0]) as c:
            for object_id, points in [('line_0', c.project([self.points['blockp0'], self.points['blockp1']])), ('line_1', c.project([self.points['blockp2'], self.points['blockp3']])), ('line_2', c.project([self.points['blockp4'], self.points['blockp5']])), ('line_3', c.project([self.points['blockp6'], self.points['blockp7']])), ('line_4', c.project([self.points['blockp8'], self.points['blockp9']])), ('line_5', c.project([self.points['blockp10'], self.points['blockp11']])), ('line_6', c.project([self.points['blockp12'], self.points['blockp13']])), ('line_7', c.project([self.points['blockp14'], self.points['blockp15']])), ('line_8', c.project([self.points['blockp16'], self.points['blockp17']])), ('line_9', c.project([self.points['a0'], self.points['b0']])), ('line_10', c.project([self.points['b0'], self.points['c0']])), ('line_11', c.project([self.points['a1'], self.points['b1']])), ('line_12', c.project([self.points['b1'], self.points['c1']])), ('line_13', c.project([self.points['a2'], self.points['b2']])), ('line_14', c.project([self.points['b2'], self.points['c2']])), ('lowerline_0', c.project([self.points['lowerblockp0'], self.points['lowerblockp1']])), ('lowerline_1', c.project([self.points['lowerblockp2'], self.points['lowerblockp3']])), ('lowerline_2', c.project([self.points['lowerblockp4'], self.points['lowerblockp5']])), ('lowerline_3', c.project([self.points['lowerblockp6'], self.points['lowerblockp7']])), ('lowerline_4', c.project([self.points['lowerblockp8'], self.points['lowerblockp9']])), ('lowerline_5', c.project([self.points['lowerblockp10'], self.points['lowerblockp11']])), ('lowerline_6', c.project([self.points['lowerblockp12'], self.points['lowerblockp13']])), ('lowerline_7', c.project([self.points['lowerblockp14'], self.points['lowerblockp15']])), ('lowerline_8', c.project([self.points['lowerblockp16'], self.points['lowerblockp17']])), ('lowerline_9', c.project([self.points['lowerblockp18'], self.points['lowerblockp19']])), ('lowerline_10', c.project([self.points['lowerblockp20'], self.points['lowerblockp21']])), ('lowerline_11', c.project([self.points['lowerblockp22'], self.points['lowerblockp23']])), ('lowerline_12', c.project([self.points['lowerblockp24'], self.points['lowerblockp25']])), ('lowerline_13', c.project([self.points['lowerblockp26'], self.points['lowerblockp27']])), ('lowerline_14', c.project([self.points['lowerblockp28'], self.points['lowerblockp29']])), ('lowerline_15', c.project([self.points['lowerblockp30'], self.points['lowerblockp31']])), ('lowerline_16', c.project([self.points['lowerblockp32'], self.points['lowerblockp33']])), ('lowerline_17', c.project([self.points['lowerblockp34'], self.points['lowerblockp35']])), ('lowerline_18', c.project([self.points['lowerblockp36'], self.points['lowerblockp37']])), ('lowerline_19', c.project([self.points['lowerblockp38'], self.points['lowerblockp39']])), ('lowerline_20', c.project([self.points['lowerblockp40'], self.points['lowerblockp41']])), ('lowerline_21', c.project([self.points['lowerblockp42'], self.points['lowerblockp43']])), ('lowerline_22', c.project([self.points['lowerblockp44'], self.points['lowerblockp45']])), ('lowerline_23', c.project([self.points['lowerblockp46'], self.points['lowerblockp47']])), ('lowerline_24', c.project([self.points['lowerblockp48'], self.points['lowerblockp49']]))]:
                c.line(points, id=object_id, clip_on=False, zorder=3)
            c.text('A', c.project(self.points['Atop']), offset_pt=[-15, 0], vertex=True, id='label_0')
            c.text('1/2', c.project(self.points['Afraction']), offset_pt=[18, 0], vertex=False, id='label_1')
            c.text('B', c.project(self.points['Btop']), offset_pt=[-15, 0], vertex=True, id='label_2')
            c.text('1/3', c.project(self.points['Bfraction']), offset_pt=[18, 15], vertex=False, id='label_3')
            c.text('C', c.project(self.points['Ctop']), offset_pt=[-35, 0], vertex=True, id='label_4')
            c.text('1/17', c.project(self.points['Cfraction']), offset_pt=[22, 0], vertex=False, id='label_5')
            c.text('D', c.project(self.points['Dtop']), offset_pt=[-15, -7], vertex=True, id='label_6')
            for object_id, text, anchor in [('label_7', 'C', c.project(self.points['Cbottom'])), ('label_8', 'B', c.project(self.points['Bbottom'])), ('label_9', 'A', c.project(self.points['Abottom'])), ('label_10', 'D', c.project(self.points['Dbottom']))]:
                c.text(text, anchor, id=object_id, offset_pt=[12, -15], vertex=True)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Solid235().draw(sys.argv[1] if len(sys.argv) > 1 else None))
