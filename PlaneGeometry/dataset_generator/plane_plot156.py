"""Frozen question Plane156; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane156:

    def __init__(self):
        self.id = 'Plane156'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:86'
        self.question = 'Which of the 5 pictures shows a part of this chain?\nChoices:\nA:A\nB:B\nC:C\nD:D\nE:E'
        self.answer = 'C'
        self.answer_type = 'choice'
        self.choices = {'A': 'A', 'B': 'B', 'C': 'C', 'D': 'D', 'E': 'E'}
        self.query = self.question
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane156.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-3.1106738912081173, 32.192634087199224], ylim=[-13.254408317067817, 22.048899661339522], axes_position=[0.05, 0.05, 0.9, 0.9], coordinate_axes=False) as c:
            for object_id, points in [('thread0', [[13.453204411711791, 8.811971798460293], [14.041679691311995, 8.844578911756129]]), ('thread1', [[14.981288836526858, 8.735182083779115], [15.468018525533553, 8.591437088870139]]), ('thread2', [[16.284347492802798, 8.133498542887521], [16.463093198614548, 7.971824171357308]]), ('thread3', [[16.88476131416617, 7.174353588907699], [16.88873980722818, 7.1455531458439046]]), ('thread4', [[16.6698297468181, 6.283537049992492], [16.582726841575457, 6.165234954035916]]), ('thread5', [[15.8593443940904, 5.584116105496371], [15.46484936524354, 5.409171456605979]]), ('thread6', [[14.546795588288209, 5.188028201539707], [13.958320308688007, 5.155421088243872]]), ('thread7', [[13.018711163473144, 5.264817916220886], [12.531981474466447, 5.40856291112986]]), ('thread8', [[11.7156525071972, 5.866501457112479], [11.536906801385456, 6.028175828642691]]), ('thread9', [[11.11523868583383, 6.825646411092301], [11.111260192771821, 6.8544468541560954]]), ('thread10', [[11.330170253181901, 7.716462950007508], [11.41727315842454, 7.834765045964084]]), ('thread11', [[12.140655605909599, 8.41588389450363], [12.53515063475646, 8.590828543394021]])]:
                c.line(points, id=object_id)
            c.circle([12.973939570022994, 8.785415979493227], 0.48, id='bead0', facecolor=[1.0, 1.0, 1.0, 1.0])
            c.circle([14.520944533000792, 8.871134730723195], 0.48, id='bead1', facecolor=[1.0, 1.0, 1.0, 1.0])
            c.circle([15.928362829059619, 8.455484441926059], 0.48, id='bead2', facecolor=[0.0, 0.0, 0.0, 1.0])
            c.circle([16.819077862357727, 7.649838272318771], 0.48, id='bead3', facecolor=[0.6, 0.6, 0.6, 1.0])
            c.circle([16.954423259036624, 6.670068462432832], 0.48, id='bead4', facecolor=[0.6, 0.6, 0.6, 1.0])
            c.circle([16.298133329356933, 5.778703541595576], 0.48, id='bead5', facecolor=[0.0, 0.0, 0.0, 1.0])
            c.circle([15.026060429977006, 5.214584020506774], 0.48, id='bead6', facecolor=[1.0, 1.0, 1.0, 1.0])
            c.circle([13.47905546699921, 5.128865269276805], 0.48, id='bead7', facecolor=[1.0, 1.0, 1.0, 1.0])
            c.circle([12.071637170940381, 5.544515558073941], 0.48, id='bead8', facecolor=[0.0, 0.0, 0.0, 1.0])
            c.circle([11.180922137642275, 6.350161727681229], 0.48, id='bead9', facecolor=[0.6, 0.6, 0.6, 1.0])
            c.circle([11.045576740963376, 7.329931537567168], 0.48, id='bead10', facecolor=[0.6, 0.6, 0.6, 1.0])
            c.circle([11.701866670643065, 8.221296458404424], 0.48, id='bead11', facecolor=[0.0, 0.0, 0.0, 1.0])
            for object_id, points in [('opt0gap0', [[-0.7, 0.0], [-0.48, 0.0]]), ('opt0gap1', [[0.48, 0.0], [0.82, 0.0]]), ('opt0gap2', [[1.78, 0.0], [2.12, 0.0]]), ('opt0gap3', [[3.08, 0.0], [3.3, 0.0]])]:
                c.line(points, id=object_id)
            c.circle([0.0, 0.0], 0.48, id='opt0bead0', facecolor=[0.6, 0.6, 0.6, 1.0])
            c.circle([1.3, 0.0], 0.48, id='opt0bead1', facecolor=[1.0, 1.0, 1.0, 1.0])
            c.circle([2.6, 0.0], 0.48, id='opt0bead2', facecolor=[0.0, 0.0, 0.0, 1.0])
            for object_id, points in [('opt1gap0', [[6.3, 0.0], [6.52, 0.0]]), ('opt1gap1', [[7.48, 0.0], [7.82, 0.0]]), ('opt1gap2', [[8.78, 0.0], [9.120000000000001, 0.0]]), ('opt1gap3', [[10.08, 0.0], [10.3, 0.0]])]:
                c.line(points, id=object_id)
            c.circle([7.0, 0.0], 0.48, id='opt1bead0', facecolor=[1.0, 1.0, 1.0, 1.0])
            c.circle([8.3, 0.0], 0.48, id='opt1bead1', facecolor=[0.0, 0.0, 0.0, 1.0])
            c.circle([9.6, 0.0], 0.48, id='opt1bead2', facecolor=[1.0, 1.0, 1.0, 1.0])
            for object_id, points in [('opt2gap0', [[13.3, 0.0], [13.52, 0.0]]), ('opt2gap1', [[14.48, 0.0], [14.82, 0.0]]), ('opt2gap2', [[15.78, 0.0], [16.12, 0.0]]), ('opt2gap3', [[17.08, 0.0], [17.3, 0.0]])]:
                c.line(points, id=object_id)
            c.circle([14.0, 0.0], 0.48, id='opt2bead0', facecolor=[1.0, 1.0, 1.0, 1.0])
            c.circle([15.3, 0.0], 0.48, id='opt2bead1', facecolor=[0.0, 0.0, 0.0, 1.0])
            c.circle([16.6, 0.0], 0.48, id='opt2bead2', facecolor=[0.6, 0.6, 0.6, 1.0])
            for object_id, points in [('opt3gap0', [[20.3, 0.0], [20.52, 0.0]]), ('opt3gap1', [[21.48, 0.0], [21.82, 0.0]]), ('opt3gap2', [[22.78, 0.0], [23.12, 0.0]]), ('opt3gap3', [[24.08, 0.0], [24.3, 0.0]])]:
                c.line(points, id=object_id)
            c.circle([21.0, 0.0], 0.48, id='opt3bead0', facecolor=[0.6, 0.6, 0.6, 1.0])
            c.circle([22.3, 0.0], 0.48, id='opt3bead1', facecolor=[0.0, 0.0, 0.0, 1.0])
            c.circle([23.6, 0.0], 0.48, id='opt3bead2', facecolor=[0.6, 0.6, 0.6, 1.0])
            for object_id, points in [('opt4gap0', [[27.3, 0.0], [27.52, 0.0]]), ('opt4gap1', [[28.48, 0.0], [28.82, 0.0]]), ('opt4gap2', [[29.78, 0.0], [30.12, 0.0]]), ('opt4gap3', [[31.08, 0.0], [31.3, 0.0]])]:
                c.line(points, id=object_id)
            c.circle([28.0, 0.0], 0.48, id='opt4bead0', facecolor=[0.0, 0.0, 0.0, 1.0])
            c.circle([29.3, 0.0], 0.48, id='opt4bead1', facecolor=[1.0, 1.0, 1.0, 1.0])
            c.circle([30.6, 0.0], 0.48, id='opt4bead2', facecolor=[0.0, 0.0, 0.0, 1.0])
            for object_id, text, anchor in [('label0', '(A)', [-1.6, -0.2]), ('label1', '(B)', [5.4, -0.2]), ('label2', '(C)', [12.4, -0.2]), ('label3', '(D)', [19.4, -0.2]), ('label4', '(E)', [26.4, -0.2])]:
                c.text(text, anchor, id=object_id, rotation_mode='default', offset_pt=[0, 0], annotation_clip=None)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane156().draw(sys.argv[1] if len(sys.argv) > 1 else None))
