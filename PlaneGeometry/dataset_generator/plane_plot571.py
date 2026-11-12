"""Frozen question Plane571; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane571:

    def __init__(self):
        self.id = 'Plane571'
        self.source_dataset = 'Author Designed'
        self.source_key = 'author-extensions95-v1:Plane278/extension_02'
        self.question = 'A square can be made out of four of the given pieces, with both straight sides of each piece on the outside. Pieces may be rotated or turned over. Which piece will not be used?\nChoices:\nA:A\nB:B\nC:C\nD:D\nE:E'
        self.answer = 'A'
        self.answer_type = 'choice'
        self.choices = {'A': 'A', 'B': 'B', 'C': 'C', 'D': 'D', 'E': 'E'}
        self.query = self.question
        self._geometry_01 = [[0.0, 0.0],
         [400.0, 0.0],
         [800.0, 0.0],
         [1200.0, 0.0],
         [1200.0, 90.0],
         [1371.0, 180.0],
         [1371.0, 270.0],
         [1371.0, 380.0],
         [1200.0, 490.0],
         [1200.0, 600.0],
         [1200.0, 710.0],
         [1029.0, 820.0],
         [1029.0, 930.0],
         [1029.0, 1020.0],
         [1200.0, 1110.0],
         [1200.0, 1200.0],
         [1070.0, 1200.0],
         [940.0, 1083.0],
         [810.0, 1083.0],
         [740.0, 1083.0],
         [670.0, 1200.0],
         [600.0, 1200.0],
         [530.0, 1200.0],
         [460.0, 1317.0],
         [390.0, 1317.0],
         [260.0, 1317.0],
         [130.0, 1200.0],
         [0.0, 1200.0],
         [0.0, 800.0],
         [0.0, 400.0],
         [0.0, 0.0],
         [0.0, 0.0]]
        self._geometry_02 = [1, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 79]
        self._geometry_03 = [[1850.0, 0.0],
         [2250.0, 0.0],
         [2650.0, 0.0],
         [3050.0, 0.0],
         [3050.0, 80.0],
         [2966.0, 160.0],
         [2966.0, 240.0],
         [2966.0, 300.0],
         [2897.0, 360.0],
         [2897.0, 420.0],
         [2897.0, 480.0],
         [3050.0, 540.0],
         [3050.0, 600.0],
         [3050.0, 660.0],
         [3203.0, 720.0],
         [3203.0, 780.0],
         [3203.0, 840.0],
         [3134.0, 900.0],
         [3134.0, 960.0],
         [3134.0, 1040.0],
         [3050.0, 1120.0],
         [3050.0, 1200.0],
         [2960.0, 1200.0],
         [2870.0, 1371.0],
         [2780.0, 1371.0],
         [2670.0, 1371.0],
         [2560.0, 1200.0],
         [2450.0, 1200.0],
         [2340.0, 1200.0],
         [2230.0, 1029.0],
         [2120.0, 1029.0],
         [2030.0, 1029.0],
         [1940.0, 1200.0],
         [1850.0, 1200.0],
         [1850.0, 800.0],
         [1850.0, 400.0],
         [1850.0, 0.0],
         [1850.0, 0.0]]
        self._geometry_04 = [1, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 79]
        self._geometry_05 = [[3700.0, 0.0],
         [4100.0, 0.0],
         [4500.0, 0.0],
         [4900.0, 0.0],
         [4900.0, 90.0],
         [5071.0, 180.0],
         [5071.0, 270.0],
         [5071.0, 380.0],
         [4900.0, 490.0],
         [4900.0, 600.0],
         [4900.0, 710.0],
         [4729.0, 820.0],
         [4729.0, 930.0],
         [4729.0, 1020.0],
         [4900.0, 1110.0],
         [4900.0, 1200.0],
         [4850.0, 1200.0],
         [4800.0, 1290.0],
         [4750.0, 1290.0],
         [4700.0, 1290.0],
         [4650.0, 1200.0],
         [4600.0, 1200.0],
         [4550.0, 1200.0],
         [4500.0, 1110.0],
         [4450.0, 1110.0],
         [4400.0, 1110.0],
         [4350.0, 1200.0],
         [4300.0, 1200.0],
         [4250.0, 1200.0],
         [4200.0, 1290.0],
         [4150.0, 1290.0],
         [4100.0, 1290.0],
         [4050.0, 1200.0],
         [4000.0, 1200.0],
         [3950.0, 1200.0],
         [3900.0, 1110.0],
         [3850.0, 1110.0],
         [3800.0, 1110.0],
         [3750.0, 1200.0],
         [3700.0, 1200.0],
         [3700.0, 800.0],
         [3700.0, 400.0],
         [3700.0, 0.0],
         [3700.0, 0.0]]
        self._geometry_06 = [1, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 79]
        self._geometry_07 = [[5550.0, 0.0],
         [5950.0, 0.0],
         [6350.0, 0.0],
         [6750.0, 0.0],
         [6750.0, 50.0],
         [6840.0, 100.0],
         [6840.0, 150.0],
         [6840.0, 200.0],
         [6750.0, 250.0],
         [6750.0, 300.0],
         [6750.0, 350.0],
         [6660.0, 400.0],
         [6660.0, 450.0],
         [6660.0, 500.0],
         [6750.0, 550.0],
         [6750.0, 600.0],
         [6750.0, 650.0],
         [6840.0, 700.0],
         [6840.0, 750.0],
         [6840.0, 800.0],
         [6750.0, 850.0],
         [6750.0, 900.0],
         [6750.0, 950.0],
         [6660.0, 1000.0],
         [6660.0, 1050.0],
         [6660.0, 1100.0],
         [6750.0, 1150.0],
         [6750.0, 1200.0],
         [6670.0, 1200.0],
         [6590.0, 1116.0],
         [6510.0, 1116.0],
         [6450.0, 1116.0],
         [6390.0, 1047.0],
         [6330.0, 1047.0],
         [6270.0, 1047.0],
         [6210.0, 1200.0],
         [6150.0, 1200.0],
         [6090.0, 1200.0],
         [6030.0, 1353.0],
         [5970.0, 1353.0],
         [5910.0, 1353.0],
         [5850.0, 1284.0],
         [5790.0, 1284.0],
         [5710.0, 1284.0],
         [5630.0, 1200.0],
         [5550.0, 1200.0],
         [5550.0, 800.0],
         [5550.0, 400.0],
         [5550.0, 0.0],
         [5550.0, 0.0]]
        self._geometry_08 = [1, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 79]
        self._geometry_09 = [[7400.0, 0.0],
         [7800.0, 0.0],
         [8200.0, 0.0],
         [8600.0, 0.0],
         [8600.0, 90.0],
         [8771.0, 180.0],
         [8771.0, 270.0],
         [8771.0, 380.0],
         [8600.0, 490.0],
         [8600.0, 600.0],
         [8600.0, 710.0],
         [8429.0, 820.0],
         [8429.0, 930.0],
         [8429.0, 1020.0],
         [8600.0, 1110.0],
         [8600.0, 1200.0],
         [8510.0, 1200.0],
         [8420.0, 1371.0],
         [8330.0, 1371.0],
         [8220.0, 1371.0],
         [8110.0, 1200.0],
         [8000.0, 1200.0],
         [7890.0, 1200.0],
         [7780.0, 1029.0],
         [7670.0, 1029.0],
         [7580.0, 1029.0],
         [7490.0, 1200.0],
         [7400.0, 1200.0],
         [7400.0, 800.0],
         [7400.0, 400.0],
         [7400.0, 0.0],
         [7400.0, 0.0]]
        self._geometry_10 = [1, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 79]
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane571.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=(-215.9762596899227, 8987.330426356588), ylim=(-4156.783551356589, 5046.523134689923), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
            for object_id, vertices, codes in [('piece_A', self._geometry_01, self._geometry_02), ('piece_B', self._geometry_03, self._geometry_04), ('piece_C', self._geometry_05, self._geometry_06), ('piece_D', self._geometry_07, self._geometry_08), ('piece_E', self._geometry_09, self._geometry_10)]:
                c.path(vertices, codes, id=object_id, zorder=1, joinstyle='round', simplify=False)
            for object_id, text, anchor in [('label_A', 'A', (600, 600)), ('choice_label_A', '(A) A', (600, -360)), ('label_B', 'B', (2450, 600)), ('choice_label_B', '(B) B', (2450, -360)), ('label_C', 'C', (4300, 600)), ('choice_label_C', '(C) C', (4300, -360)), ('label_D', 'D', (6150, 600)), ('choice_label_D', '(D) D', (6150, -360)), ('label_E', 'E', (8000, 600)), ('choice_label_E', '(E) E', (8000, -360))]:
                c.text(text, anchor, id=object_id, zorder=3, rotation_mode='default')
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane571().draw(sys.argv[1] if len(sys.argv) > 1 else None))
