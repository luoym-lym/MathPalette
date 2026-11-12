"""Frozen question Plane570; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane570:

    def __init__(self):
        self.id = 'Plane570'
        self.source_dataset = 'Author Designed'
        self.source_key = 'author-extensions95-v1:Plane278/extension_01'
        self.question = 'A square can be made out of four of the given pieces, with both straight sides of each piece on the outside. Pieces may be rotated or turned over. Which piece will not be used?\nChoices:\nA:A\nB:B\nC:C\nD:D\nE:E'
        self.answer = 'C'
        self.answer_type = 'choice'
        self.choices = {'A': 'A', 'B': 'B', 'C': 'C', 'D': 'D', 'E': 'E'}
        self.query = self.question
        self._geometry_01 = [[0.0, 0.0],
         [400.0, 0.0],
         [800.0, 0.0],
         [1200.0, 0.0],
         [1200.0, 100.0],
         [1380.0, 200.0],
         [1380.0, 300.0],
         [1380.0, 400.0],
         [1200.0, 500.0],
         [1200.0, 600.0],
         [1200.0, 700.0],
         [1020.0, 800.0],
         [1020.0, 900.0],
         [1020.0, 1000.0],
         [1200.0, 1100.0],
         [1200.0, 1200.0],
         [1150.0, 1200.0],
         [1100.0, 1287.0],
         [1050.0, 1287.0],
         [1000.0, 1287.0],
         [950.0, 1200.0],
         [900.0, 1200.0],
         [850.0, 1200.0],
         [800.0, 1113.0],
         [750.0, 1113.0],
         [700.0, 1113.0],
         [650.0, 1200.0],
         [600.0, 1200.0],
         [550.0, 1200.0],
         [500.0, 1287.0],
         [450.0, 1287.0],
         [400.0, 1287.0],
         [350.0, 1200.0],
         [300.0, 1200.0],
         [250.0, 1200.0],
         [200.0, 1113.0],
         [150.0, 1113.0],
         [100.0, 1113.0],
         [50.0, 1200.0],
         [0.0, 1200.0],
         [0.0, 800.0],
         [0.0, 400.0],
         [0.0, 0.0],
         [0.0, 0.0]]
        self._geometry_02 = [1, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 79]
        self._geometry_03 = [[1850.0, 0.0],
         [2250.0, 0.0],
         [2650.0, 0.0],
         [3050.0, 0.0],
         [3050.0, 100.0],
         [3176.0, 200.0],
         [3176.0, 300.0],
         [3176.0, 400.0],
         [3050.0, 500.0],
         [3050.0, 600.0],
         [3050.0, 700.0],
         [2924.0, 800.0],
         [2924.0, 900.0],
         [2924.0, 1000.0],
         [3050.0, 1100.0],
         [3050.0, 1200.0],
         [2950.0, 1200.0],
         [2850.0, 1380.0],
         [2750.0, 1380.0],
         [2650.0, 1380.0],
         [2550.0, 1200.0],
         [2450.0, 1200.0],
         [2350.0, 1200.0],
         [2250.0, 1020.0],
         [2150.0, 1020.0],
         [2050.0, 1020.0],
         [1950.0, 1200.0],
         [1850.0, 1200.0],
         [1850.0, 800.0],
         [1850.0, 400.0],
         [1850.0, 0.0],
         [1850.0, 0.0]]
        self._geometry_04 = [1, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 79]
        self._geometry_05 = [[3700.0, 0.0],
         [4100.0, 0.0],
         [4500.0, 0.0],
         [4900.0, 0.0],
         [4900.0, 100.0],
         [5080.0, 200.0],
         [5080.0, 300.0],
         [5080.0, 400.0],
         [4900.0, 500.0],
         [4900.0, 600.0],
         [4900.0, 700.0],
         [4720.0, 800.0],
         [4720.0, 900.0],
         [4720.0, 1000.0],
         [4900.0, 1100.0],
         [4900.0, 1200.0],
         [4820.0, 1200.0],
         [4740.0, 1353.0],
         [4660.0, 1353.0],
         [4540.0, 1353.0],
         [4420.0, 1200.0],
         [4300.0, 1200.0],
         [4180.0, 1200.0],
         [4060.0, 1047.0],
         [3940.0, 1047.0],
         [3860.0, 1047.0],
         [3780.0, 1200.0],
         [3700.0, 1200.0],
         [3700.0, 800.0],
         [3700.0, 400.0],
         [3700.0, 0.0],
         [3700.0, 0.0]]
        self._geometry_06 = [1, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 79]
        self._geometry_07 = [[5550.0, 0.0],
         [5950.0, 0.0],
         [6350.0, 0.0],
         [6750.0, 0.0],
         [6750.0, 80.0],
         [6597.0, 160.0],
         [6597.0, 240.0],
         [6597.0, 360.0],
         [6750.0, 480.0],
         [6750.0, 600.0],
         [6750.0, 720.0],
         [6903.0, 840.0],
         [6903.0, 960.0],
         [6903.0, 1040.0],
         [6750.0, 1120.0],
         [6750.0, 1200.0],
         [6650.0, 1200.0],
         [6550.0, 1326.0],
         [6450.0, 1326.0],
         [6350.0, 1326.0],
         [6250.0, 1200.0],
         [6150.0, 1200.0],
         [6050.0, 1200.0],
         [5950.0, 1074.0],
         [5850.0, 1074.0],
         [5750.0, 1074.0],
         [5650.0, 1200.0],
         [5550.0, 1200.0],
         [5550.0, 800.0],
         [5550.0, 400.0],
         [5550.0, 0.0],
         [5550.0, 0.0]]
        self._geometry_08 = [1, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 79]
        self._geometry_09 = [[7400.0, 0.0],
         [7800.0, 0.0],
         [8200.0, 0.0],
         [8600.0, 0.0],
         [8600.0, 50.0],
         [8687.0, 100.0],
         [8687.0, 150.0],
         [8687.0, 200.0],
         [8600.0, 250.0],
         [8600.0, 300.0],
         [8600.0, 350.0],
         [8513.0, 400.0],
         [8513.0, 450.0],
         [8513.0, 500.0],
         [8600.0, 550.0],
         [8600.0, 600.0],
         [8600.0, 650.0],
         [8687.0, 700.0],
         [8687.0, 750.0],
         [8687.0, 800.0],
         [8600.0, 850.0],
         [8600.0, 900.0],
         [8600.0, 950.0],
         [8513.0, 1000.0],
         [8513.0, 1050.0],
         [8513.0, 1100.0],
         [8600.0, 1150.0],
         [8600.0, 1200.0],
         [8520.0, 1200.0],
         [8440.0, 1047.0],
         [8360.0, 1047.0],
         [8240.0, 1047.0],
         [8120.0, 1200.0],
         [8000.0, 1200.0],
         [7880.0, 1200.0],
         [7760.0, 1353.0],
         [7640.0, 1353.0],
         [7560.0, 1353.0],
         [7480.0, 1200.0],
         [7400.0, 1200.0],
         [7400.0, 800.0],
         [7400.0, 400.0],
         [7400.0, 0.0],
         [7400.0, 0.0]]
        self._geometry_10 = [1, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 79]
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane570.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=(-214.31080426356584, 8914.0503875969), ylim=(-4112.149345930233, 5016.211845930233), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
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
    print(Plane570().draw(sys.argv[1] if len(sys.argv) > 1 else None))
