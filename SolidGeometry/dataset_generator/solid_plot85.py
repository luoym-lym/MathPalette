"""Frozen question Solid85; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Solid85:

    def __init__(self):
        self.id = 'Solid85'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:96'
        self.question = 'Each figure is made up of 4 equally big cubes and coloured in. Which figure needs the least amount of colour?\nChoices:\nA:A\nB:B\nC:C\nD:D\nE:E'
        self.answer = 'B'
        self.answer_type = 'choice'
        self.choices = {'A': 'A', 'B': 'B', 'C': 'C', 'D': 'D', 'E': 'E'}
        self.query = self.question
        self.subject = 'SolidGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'SolidGeometry' / 'dataset_generator/scenes/Solid85.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('SolidGeometry', self.id, variant, output_path)
        with Canvas(SOLID, xlim=[-0.5403255150348656, 21.590203915112294], ylim=[-10.460397211305278, 11.670132218841882], projection=[[1, 0.35, 0], [0, 0.35, 1]], origin=[0, 0, 0], offset=[0, 0]) as c:
            for object_id, points in [('Ae0', c.project([[0.0, 0.0, 0.0], [1.0, 0.0, 0.0]])), ('Ae1', c.project([[0.0, 0.0, 1.0], [1.0, 0.0, 1.0]])), ('Ae2', c.project([[0.0, 1.0, 1.0], [1.0, 1.0, 1.0]])), ('Ae3', c.project([[0.0, 0.0, 1.0], [0.0, 1.0, 1.0]])), ('Ae4', c.project([[1.0, 0.0, 1.0], [1.0, 1.0, 1.0]])), ('Ae5', c.project([[0.0, 0.0, 0.0], [0.0, 0.0, 1.0]])), ('Ae6', c.project([[1.0, 0.0, 0.0], [1.0, 0.0, 1.0]])), ('Ae7', c.project([[1.0, 0.0, 0.0], [2.0, 0.0, 0.0]])), ('Ae8', c.project([[1.0, 0.0, 1.0], [2.0, 0.0, 1.0]])), ('Ae9', c.project([[1.0, 1.0, 1.0], [2.0, 1.0, 1.0]])), ('Ae10', c.project([[2.0, 0.0, 1.0], [2.0, 1.0, 1.0]])), ('Ae11', c.project([[2.0, 0.0, 0.0], [2.0, 0.0, 1.0]])), ('Ae12', c.project([[2.0, 0.0, 0.0], [3.0, 0.0, 0.0]])), ('Ae13', c.project([[2.0, 0.0, 1.0], [3.0, 0.0, 1.0]])), ('Ae14', c.project([[2.0, 1.0, 1.0], [3.0, 1.0, 1.0]])), ('Ae15', c.project([[3.0, 0.0, 1.0], [3.0, 1.0, 1.0]])), ('Ae16', c.project([[3.0, 0.0, 0.0], [3.0, 0.0, 1.0]])), ('Ae17', c.project([[3.0, 0.0, 0.0], [4.0, 0.0, 0.0]])), ('Ae18', c.project([[3.0, 0.0, 1.0], [4.0, 0.0, 1.0]])), ('Ae19', c.project([[3.0, 1.0, 1.0], [4.0, 1.0, 1.0]])), ('Ae20', c.project([[4.0, 0.0, 0.0], [4.0, 1.0, 0.0]])), ('Ae21', c.project([[4.0, 0.0, 1.0], [4.0, 1.0, 1.0]])), ('Ae22', c.project([[4.0, 0.0, 0.0], [4.0, 0.0, 1.0]])), ('Ae23', c.project([[4.0, 1.0, 0.0], [4.0, 1.0, 1.0]])), ('Be0', c.project([[5.3, 0.0, 0.0], [6.3, 0.0, 0.0]])), ('Be1', c.project([[5.3, 0.0, 1.0], [6.3, 0.0, 1.0]])), ('Be2', c.project([[5.3, 0.0, 0.0], [5.3, 0.0, 1.0]])), ('Be3', c.project([[6.3, 0.0, 0.0], [6.3, 0.0, 1.0]])), ('Be4', c.project([[5.3, 0.0, 2.0], [6.3, 0.0, 2.0]])), ('Be5', c.project([[5.3, 1.0, 2.0], [6.3, 1.0, 2.0]])), ('Be6', c.project([[5.3, 0.0, 2.0], [5.3, 1.0, 2.0]])), ('Be7', c.project([[6.3, 0.0, 2.0], [6.3, 1.0, 2.0]])), ('Be8', c.project([[5.3, 0.0, 1.0], [5.3, 0.0, 2.0]])), ('Be9', c.project([[6.3, 0.0, 1.0], [6.3, 0.0, 2.0]])), ('Be10', c.project([[6.3, 0.0, 0.0], [7.3, 0.0, 0.0]])), ('Be11', c.project([[6.3, 0.0, 1.0], [7.3, 0.0, 1.0]])), ('Be12', c.project([[7.3, 0.0, 0.0], [7.3, 1.0, 0.0]])), ('Be13', c.project([[7.3, 0.0, 1.0], [7.3, 1.0, 1.0]])), ('Be14', c.project([[7.3, 0.0, 0.0], [7.3, 0.0, 1.0]])), ('Be15', c.project([[7.3, 1.0, 0.0], [7.3, 1.0, 1.0]])), ('Be16', c.project([[6.3, 0.0, 2.0], [7.3, 0.0, 2.0]])), ('Be17', c.project([[6.3, 1.0, 2.0], [7.3, 1.0, 2.0]])), ('Be18', c.project([[7.3, 0.0, 2.0], [7.3, 1.0, 2.0]])), ('Be19', c.project([[7.3, 0.0, 1.0], [7.3, 0.0, 2.0]])), ('Be20', c.project([[7.3, 1.0, 1.0], [7.3, 1.0, 2.0]])), ('Ce0', c.project([[9.0, 1.0, 0.0], [10.0, 1.0, 0.0]])), ('Ce1', c.project([[9.0, 1.0, 1.0], [10.0, 1.0, 1.0]])), ('Ce2', c.project([[9.0, 2.0, 1.0], [10.0, 2.0, 1.0]])), ('Ce3', c.project([[9.0, 1.0, 1.0], [9.0, 2.0, 1.0]])), ('Ce4', c.project([[10.0, 1.0, 1.0], [10.0, 2.0, 1.0]])), ('Ce5', c.project([[9.0, 1.0, 0.0], [9.0, 1.0, 1.0]])), ('Ce6', c.project([[10.0, 1.0, 0.0], [10.0, 1.0, 1.0]])), ('Ce7', c.project([[10.0, 1.0, 0.0], [10.65, 1.0, 0.0]])), ('Ce8', c.project([[10.0, 1.0, 1.0], [11.0, 1.0, 1.0]])), ('Ce9', c.project([[10.0, 2.0, 1.0], [11.0, 2.0, 1.0]])), ('Ce10', c.project([[11.0, 1.0, 1.0], [11.0, 2.0, 1.0]])), ('Ce11', c.project([[11.0, 1.0, 1.0], [12.0, 1.0, 1.0]])), ('Ce12', c.project([[11.0, 2.0, 1.0], [12.0, 2.0, 1.0]])), ('Ce13', c.project([[12.0, 1.0, 0.0], [12.0, 2.0, 0.0]])), ('Ce14', c.project([[12.0, 1.0, 1.0], [12.0, 2.0, 1.0]])), ('Ce15', c.project([[12.0, 1.0, 0.0], [12.0, 1.0, 1.0]])), ('Ce16', c.project([[12.0, 2.0, 0.0], [12.0, 2.0, 1.0]])), ('Ce17', c.project([[11.0, 0.0, 0.0], [12.0, 0.0, 0.0]])), ('Ce18', c.project([[11.0, 0.0, 1.0], [12.0, 0.0, 1.0]])), ('Ce19', c.project([[11.0, 0.0, 1.0], [11.0, 1.0, 1.0]])), ('Ce20', c.project([[12.0, 0.0, 0.0], [12.0, 1.0, 0.0]])), ('Ce21', c.project([[12.0, 0.0, 1.0], [12.0, 1.0, 1.0]])), ('Ce22', c.project([[11.0, 0.0, 0.0], [11.0, 0.0, 1.0]])), ('Ce23', c.project([[12.0, 0.0, 0.0], [12.0, 0.0, 1.0]])), ('De0', c.project([[13.4, 1.0, 0.0], [14.05, 1.0, 0.0]])), ('De1', c.project([[13.4, 1.0, 1.0], [14.4, 1.0, 1.0]])), ('De2', c.project([[13.4, 2.0, 1.0], [14.4, 2.0, 1.0]])), ('De3', c.project([[13.4, 1.0, 1.0], [13.4, 2.0, 1.0]])), ('De4', c.project([[14.4, 1.0, 1.0], [14.4, 2.0, 1.0]])), ('De5', c.project([[13.4, 1.0, 0.0], [13.4, 1.0, 1.0]])), ('De6', c.project([[14.4, 1.0, 1.0], [15.4, 1.0, 1.0]])), ('De7', c.project([[14.4, 2.0, 1.0], [15.4, 2.0, 1.0]])), ('De8', c.project([[15.4, 1.0, 1.0], [15.4, 2.0, 1.0]])), ('De9', c.project([[15.4, 2.0, 0.65], [15.4, 2.0, 1.0]])), ('De10', c.project([[14.4, 0.0, 0.0], [15.4, 0.0, 0.0]])), ('De11', c.project([[14.4, 0.0, 1.0], [15.4, 0.0, 1.0]])), ('De12', c.project([[14.4, 0.0, 1.0], [14.4, 1.0, 1.0]])), ('De13', c.project([[15.4, 0.0, 1.0], [15.4, 1.0, 1.0]])), ('De14', c.project([[14.4, 0.0, 0.0], [14.4, 0.0, 1.0]])), ('De15', c.project([[15.4, 0.0, 0.0], [15.4, 0.0, 1.0]])), ('De16', c.project([[15.4, 0.0, 0.0], [16.4, 0.0, 0.0]])), ('De17', c.project([[15.4, 0.0, 1.0], [16.4, 0.0, 1.0]])), ('De18', c.project([[15.4, 1.0, 1.0], [16.4, 1.0, 1.0]])), ('De19', c.project([[16.4, 0.0, 0.0], [16.4, 1.0, 0.0]])), ('De20', c.project([[16.4, 0.0, 1.0], [16.4, 1.0, 1.0]])), ('De21', c.project([[16.4, 0.0, 0.0], [16.4, 0.0, 1.0]])), ('De22', c.project([[16.4, 1.0, 0.0], [16.4, 1.0, 1.0]])), ('Ee0', c.project([[17.7, 0.0, 0.0], [18.7, 0.0, 0.0]])), ('Ee1', c.project([[17.7, 0.0, 1.0], [18.7, 0.0, 1.0]])), ('Ee2', c.project([[17.7, 1.0, 1.0], [18.349999999999998, 1.0, 1.0]])), ('Ee3', c.project([[17.7, 0.0, 1.0], [17.7, 1.0, 1.0]])), ('Ee4', c.project([[17.7, 0.0, 0.0], [17.7, 0.0, 1.0]])), ('Ee5', c.project([[18.7, 0.0, 0.0], [18.7, 0.0, 1.0]])), ('Ee6', c.project([[18.7, 0.0, 0.0], [19.7, 0.0, 0.0]])), ('Ee7', c.project([[18.7, 0.0, 1.0], [19.7, 0.0, 1.0]])), ('Ee8', c.project([[19.7, 0.0, 1.0], [19.7, 1.0, 1.0]])), ('Ee9', c.project([[19.7, 0.0, 0.0], [19.7, 0.0, 1.0]])), ('Ee10', c.project([[19.7, 0.0, 0.0], [20.7, 0.0, 0.0]])), ('Ee11', c.project([[19.7, 0.0, 1.0], [20.7, 0.0, 1.0]])), ('Ee12', c.project([[19.7, 1.0, 1.0], [20.7, 1.0, 1.0]])), ('Ee13', c.project([[20.7, 0.0, 0.0], [20.7, 1.0, 0.0]])), ('Ee14', c.project([[20.7, 0.0, 1.0], [20.7, 1.0, 1.0]])), ('Ee15', c.project([[20.7, 0.0, 0.0], [20.7, 0.0, 1.0]])), ('Ee16', c.project([[20.7, 1.0, 0.0], [20.7, 1.0, 1.0]])), ('Ee17', c.project([[18.7, 0.0, 2.0], [19.7, 0.0, 2.0]])), ('Ee18', c.project([[18.7, 1.0, 2.0], [19.7, 1.0, 2.0]])), ('Ee19', c.project([[18.7, 0.0, 2.0], [18.7, 1.0, 2.0]])), ('Ee20', c.project([[19.7, 0.0, 2.0], [19.7, 1.0, 2.0]])), ('Ee21', c.project([[18.7, 0.0, 1.0], [18.7, 0.0, 2.0]])), ('Ee22', c.project([[19.7, 0.0, 1.0], [19.7, 0.0, 2.0]])), ('Ee23', c.project([[19.7, 1.0, 1.0], [19.7, 1.0, 2.0]]))]:
                c.line(points, id=object_id, clip_on=False, zorder=3)
            for object_id, text, anchor in [('optionA', '(A)', c.project([1, 0, 0])), ('optionB', '(B)', c.project([6.3, 0, 0])), ('optionC', '(C)', c.project([10, 0, 0])), ('optionD', '(D)', c.project([14.4, 0, 0])), ('optionE', '(E)', c.project([18.7, 0, 0]))]:
                c.text(text, anchor, id=object_id, offset_pt=[0, -20], vertex=False)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Solid85().draw(sys.argv[1] if len(sys.argv) > 1 else None))
