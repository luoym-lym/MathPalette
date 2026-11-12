"""Frozen question Plane201; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane201:

    def __init__(self):
        self.id = 'Plane201'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:470'
        self.question = 'Tiles have the shape shown.\nWhich of the following patterns cannot be made with these tiles?\nChoices:\nA:A\nB:B\nC:C\nD:D\nE:E'
        self.answer = 'B'
        self.answer_type = 'choice'
        self.choices = {'A': 'A', 'B': 'B', 'C': 'C', 'D': 'D', 'E': 'E'}
        self.query = self.question
        self._geometry_01 = [('source0grid0_0', [[8.0, 5.0], [8.0, 6.0]]),
         ('source0grid0_1', [[8.0, 5.0], [9.0, 5.0]]),
         ('source0grid1_0', [[9.0, 5.0], [9.0, 6.0]]),
         ('source0grid1_1', [[8.0, 6.0], [9.0, 6.0]]),
         ('source0stroke0', [[8.0, 6.0], [9.0, 5.0]]),
         ('source1grid0_0', [[10.0, 5.0], [10.0, 6.0]]),
         ('source1grid0_1', [[10.0, 5.0], [11.0, 5.0]]),
         ('source1grid1_0', [[11.0, 5.0], [11.0, 6.0]]),
         ('source1grid1_1', [[10.0, 6.0], [11.0, 6.0]]),
         ('source1stroke0', [[10.0, 5.0], [11.0, 6.0]]),
         ('source2grid0_0', [[12.0, 5.0], [11.292893218813452, 5.707106781186548]]),
         ('source2grid0_1', [[12.0, 5.0], [12.707106781186548, 5.707106781186548]]),
         ('source2grid1_0', [[12.707106781186548, 5.707106781186548], [12.0, 6.414213562373096]]),
         ('source2grid1_1', [[11.292893218813452, 5.707106781186548], [12.0, 6.414213562373096]]),
         ('source2stroke0',
          [[11.292893218813452, 5.707106781186548], [12.707106781186548, 5.707106781186548]]),
         ('Agrid0_0', [[0.0, 0.0], [0.0, 2.0]]),
         ('Agrid0_1', [[0.0, 0.0], [2.0, 0.0]]),
         ('Agrid1_0', [[1.0, 0.0], [1.0, 2.0]]),
         ('Agrid1_1', [[0.0, 1.0], [2.0, 1.0]]),
         ('Agrid2_0', [[2.0, 0.0], [2.0, 2.0]]),
         ('Agrid2_1', [[0.0, 2.0], [2.0, 2.0]]),
         ('Astroke0', [[0.0, 0.0], [2.0, 2.0]]),
         ('Astroke1', [[0.0, 2.0], [2.0, 0.0]]),
         ('Bgrid0_0', [[6.4, 0.0], [4.985786437626905, 1.4142135623730951]]),
         ('Bgrid0_1', [[6.4, 0.0], [7.814213562373095, 1.414213562373095]]),
         ('Bgrid1_0', [[7.107106781186548, 0.7071067811865475], [5.692893218813453, 2.121320343559643]]),
         ('Bgrid1_1', [[5.6928932188134524, 0.7071067811865476], [7.107106781186548, 2.1213203435596424]]),
         ('Bgrid2_0', [[7.814213562373095, 1.414213562373095], [6.4, 2.82842712474619]]),
         ('Bgrid2_1', [[4.985786437626905, 1.4142135623730951], [6.4, 2.82842712474619]]),
         ('Bstroke0', [[6.046446609406726, 0.3535533905932738], [7.460660171779821, 1.7677669529663687]]),
         ('Bstroke1', [[5.339339828220179, 1.0606601717798214], [6.753553390593274, 2.4748737341529163]]),
         ('Cgrid0_0', [[10.0, 0.0], [10.0, 2.0]]),
         ('Cgrid0_1', [[10.0, 0.0], [12.0, 0.0]]),
         ('Cgrid1_0', [[11.0, 0.0], [11.0, 2.0]]),
         ('Cgrid1_1', [[10.0, 1.0], [12.0, 1.0]]),
         ('Cgrid2_0', [[12.0, 0.0], [12.0, 2.0]]),
         ('Cgrid2_1', [[10.0, 2.0], [12.0, 2.0]]),
         ('Cstroke0', [[10.0, 1.0], [11.0, 2.0]]),
         ('Cstroke1', [[11.0, 2.0], [12.0, 1.0]]),
         ('Cstroke2', [[12.0, 1.0], [11.0, 0.0]]),
         ('Cstroke3', [[11.0, 0.0], [10.0, 1.0]]),
         ('Dgrid0_0', [[16.4, 0.0], [14.985786437626903, 1.4142135623730951]]),
         ('Dgrid0_1', [[16.4, 0.0], [17.814213562373094, 1.414213562373095]]),
         ('Dgrid1_0', [[17.107106781186545, 0.7071067811865475], [15.692893218813449, 2.121320343559643]]),
         ('Dgrid1_1', [[15.69289321881345, 0.7071067811865476], [17.10710678118655, 2.1213203435596424]]),
         ('Dgrid2_0', [[17.814213562373094, 1.414213562373095], [16.4, 2.82842712474619]]),
         ('Dgrid2_1', [[14.985786437626903, 1.4142135623730951], [16.4, 2.82842712474619]]),
         ('Dstroke0', [[15.69289321881345, 0.7071067811865476], [17.107106781186545, 0.7071067811865475]]),
         ('Dstroke1', [[14.985786437626903, 1.4142135623730951], [17.814213562373094, 1.414213562373095]]),
         ('Dstroke2', [[15.692893218813449, 2.121320343559643], [17.10710678118655, 2.1213203435596424]]),
         ('Egrid0_0', [[20.0, 0.0], [20.0, 2.0]]),
         ('Egrid0_1', [[20.0, 0.0], [22.0, 0.0]]),
         ('Egrid1_0', [[21.0, 0.0], [21.0, 2.0]]),
         ('Egrid1_1', [[20.0, 1.0], [22.0, 1.0]]),
         ('Egrid2_0', [[22.0, 0.0], [22.0, 2.0]]),
         ('Egrid2_1', [[20.0, 2.0], [22.0, 2.0]]),
         ('Estroke0', [[20.0, 0.0], [21.0, 1.0]]),
         ('Estroke1', [[21.0, 1.0], [22.0, 0.0]]),
         ('Estroke2', [[20.0, 1.0], [21.0, 2.0]]),
         ('Estroke3', [[21.0, 2.0], [22.0, 1.0]])]
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane201.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-0.5484123633595761, 22.59427275740987], ylim=[-8.891464597826982, 14.251220522942464]) as c:
            for object_id, points in self._geometry_01:
                c.line(points, id=object_id)
            for object_id, text, anchor in [('label0', 'A)', [1, -0.8]), ('label1', 'B)', [6, -0.8]), ('label2', 'C)', [11, -0.8]), ('label3', 'D)', [16, -0.8]), ('label4', 'E)', [21, -0.8])]:
                c.text(text, anchor, id=object_id, offset_pt=[0, 0], vertex=False)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane201().draw(sys.argv[1] if len(sys.argv) > 1 else None))
