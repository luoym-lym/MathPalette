"""Frozen question Plane96; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane96:

    def __init__(self):
        self.id = 'Plane96'
        self.source_dataset = 'Author Designed'
        self.source_key = 'smooth-curve:05'
        self.question = 'Starting at H, which endpoint is reached along the same smooth curve, without switching curves at any crossing?'
        self.answer = 'A'
        self.answer_type = 'text'
        self.query = self.question
        self.points = {'G': [-1.0, 1.65],
         'B': [1.0, -0.75],
         'E': [-1.0, 0.25000000000000006],
         'D': [1.0, -0.55],
         'C': [-1.0, 0.04999999999999999],
         'F': [1.0, 0.8500000000000001],
         'A': [-1.0, -1.35],
         'H': [1.0, 1.0499999999999998],
         'J01': [-0.75, 0.084375],
         'J02': [-8.326672684688674e-17, 0.30000000000000004],
         'J03': [-8.326672684688674e-17, -0.30000000000000004],
         'J04': [0.25, 0.009375000000000022],
         'J05': [0.75, -0.515625],
         'J06': [0.7500000000000003, 0.6843750000000003]}
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane96.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-1.6159419358411378, 1.615945899796933], ylim=[-1.4552622444776464, 1.7766255911604243]) as c:
            for object_id, vertices, codes in [('GB_s01_G_J02', [[-1.0, 1.65], [-0.6666666666666666, 1.15], [-0.33333333333333337, 0.7000000000000001], [-8.326672684688674e-17, 0.30000000000000004]], [1, 4, 4, 4]), ('GB_s02_J02_J04', [[-8.326672684688674e-17, 0.30000000000000004], [0.08333333333333329, 0.20000000000000007], [0.16666666666666663, 0.10312500000000005], [0.25, 0.009375000000000022]], [1, 4, 4, 4]), ('GB_s03_J04_J05', [[0.25, 0.009375000000000022], [0.41666666666666663, -0.17812499999999995], [0.5833333333333334, -0.35312499999999997], [0.75, -0.515625]], [1, 4, 4, 4]), ('GB_s04_J05_B', [[0.75, -0.515625], [0.8333333333333333, -0.596875], [0.9166666666666666, -0.675], [1.0, -0.75]], [1, 4, 4, 4]), ('ED_s01_E_J01', [[-1.0, 0.25000000000000006], [-0.9166666666666666, 0.1916666666666667], [-0.8333333333333333, 0.13645833333333335], [-0.75, 0.084375]], [1, 4, 4, 4]), ('ED_s02_J01_J03', [[-0.75, 0.084375], [-0.4999999999999999, -0.07187500000000002], [-0.24999999999999997, -0.2], [-8.326672684688674e-17, -0.30000000000000004]], [1, 4, 4, 4]), ('ED_s03_J03_J05', [[-8.326672684688674e-17, -0.30000000000000004], [0.08333333333333329, -0.33333333333333337], [0.16666666666666663, -0.3635416666666667], [0.25, -0.390625], [0.41666666666666663, -0.4447916666666667], [0.5833333333333334, -0.4864583333333334], [0.75, -0.515625]], [1, 4, 4, 4, 4, 4, 4]), ('ED_s04_J05_D', [[0.75, -0.515625], [0.8333333333333333, -0.5302083333333334], [0.9166666666666666, -0.5416666666666667], [1.0, -0.55]], [1, 4, 4, 4]), ('CF_s01_C_J01', [[-1.0, 0.04999999999999999], [-0.9166666666666666, 0.058333333333333334], [-0.8333333333333333, 0.06979166666666667], [-0.75, 0.084375]], [1, 4, 4, 4]), ('CF_s02_J01_J02', [[-0.75, 0.084375], [-0.4999999999999999, 0.12812500000000002], [-0.24999999999999997, 0.2], [-8.326672684688674e-17, 0.30000000000000004]], [1, 4, 4, 4]), ('CF_s03_J02_J06', [[-8.326672684688674e-17, 0.30000000000000004], [0.08333333333333329, 0.3333333333333333], [0.16666666666666663, 0.36979166666666663], [0.25, 0.409375], [0.41666666666666674, 0.48854166666666665], [0.5833333333333335, 0.5802083333333334], [0.7500000000000003, 0.6843750000000003]], [1, 4, 4, 4, 4, 4, 4]), ('CF_s04_J06_F', [[0.7500000000000003, 0.6843750000000003], [0.8333333333333335, 0.7364583333333335], [0.9166666666666667, 0.7916666666666669], [1.0, 0.8500000000000001]], [1, 4, 4, 4]), ('AH_s01_A_J03', [[-1.0, -1.35], [-0.6666666666666666, -1.0500000000000003], [-0.33333333333333337, -0.7000000000000002], [-8.326672684688674e-17, -0.30000000000000004]], [1, 4, 4, 4]), ('AH_s02_J03_J04', [[-8.326672684688674e-17, -0.30000000000000004], [0.08333333333333329, -0.20000000000000007], [0.16666666666666663, -0.09687500000000002], [0.25, 0.009375000000000022]], [1, 4, 4, 4]), ('AH_s03_J04_J06', [[0.25, 0.009375000000000022], [0.41666666666666674, 0.22187500000000016], [0.5833333333333335, 0.44687500000000024], [0.7500000000000003, 0.6843750000000003]], [1, 4, 4, 4]), ('AH_s04_J06_H', [[0.7500000000000003, 0.6843750000000003], [0.8333333333333335, 0.8031250000000001], [0.9166666666666667, 0.9249999999999999], [1.0, 1.0499999999999998]], [1, 4, 4, 4])]:
                c.path(vertices, codes, id=object_id, capstyle='butt', zorder=1)
            c.text('G', self.points['G'], offset_pt=[-8.0, -0.0], vertex=True, ha='right')
            c.text('B', self.points['B'], offset_pt=[8.0, 0.0], vertex=True, ha='left')
            c.text('E', self.points['E'], offset_pt=[-8.0, -0.0], vertex=True, ha='right')
            c.text('D', self.points['D'], offset_pt=[8.0, 0.0], vertex=True, ha='left')
            c.text('C', self.points['C'], offset_pt=[-8.0, -0.0], vertex=True, ha='right')
            c.text('F', self.points['F'], offset_pt=[8.0, 0.0], vertex=True, ha='left')
            c.text('A', self.points['A'], offset_pt=[-8.0, -0.0], vertex=True, ha='right')
            c.text('H', self.points['H'], offset_pt=[8.0, 0.0], vertex=True, ha='left')
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane96().draw(sys.argv[1] if len(sys.argv) > 1 else None))
