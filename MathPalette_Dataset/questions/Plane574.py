"""Collected question Plane574; construction on the shared drawing protocol."""
from pathlib import Path
import sys
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from MathPalette_Dataset.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane574:
    variants = ('C01', 'C02', 'C03', 'C04', 'C05', 'C06')

    def __init__(self):
        self._samples_001 = [[0.0, 0.0],
         [400.0, 0.0],
         [800.0, 0.0],
         [1200.0, 0.0],
         [1200.0, 80.0],
         [1302.0, 160.0],
         [1302.0, 240.0],
         [1302.0, 300.0],
         [1359.0, 360.0],
         [1359.0, 420.0],
         [1359.0, 480.0],
         [1200.0, 540.0],
         [1200.0, 600.0],
         [1200.0, 660.0],
         [1041.0, 720.0],
         [1041.0, 780.0],
         [1041.0, 840.0],
         [1098.0, 900.0],
         [1098.0, 960.0],
         [1098.0, 1040.0],
         [1200.0, 1120.0],
         [1200.0, 1200.0],
         [1120.0, 1200.0],
         [1040.0, 1098.0],
         [960.0, 1098.0],
         [900.0, 1098.0],
         [840.0, 1041.0],
         [780.0, 1041.0],
         [720.0, 1041.0],
         [660.0, 1200.0],
         [600.0, 1200.0],
         [540.0, 1200.0],
         [480.0, 1359.0],
         [420.0, 1359.0],
         [360.0, 1359.0],
         [300.0, 1302.0],
         [240.0, 1302.0],
         [160.0, 1302.0],
         [80.0, 1200.0],
         [0.0, 1200.0],
         [0.0, 800.0],
         [0.0, 400.0],
         [0.0, 0.0],
         [0.0, 0.0]]
        self._samples_002 = [[1850.0, 0.0],
         [2250.0, 0.0],
         [2650.0, 0.0],
         [3050.0, 0.0],
         [3050.0, 120.0],
         [2873.0, 240.0],
         [2873.0, 360.0],
         [2873.0, 440.0],
         [3050.0, 520.0],
         [3050.0, 600.0],
         [3050.0, 680.0],
         [3227.0, 760.0],
         [3227.0, 840.0],
         [3227.0, 960.0],
         [3050.0, 1080.0],
         [3050.0, 1200.0],
         [3000.0, 1200.0],
         [2950.0, 1284.0],
         [2900.0, 1284.0],
         [2850.0, 1284.0],
         [2800.0, 1200.0],
         [2750.0, 1200.0],
         [2700.0, 1200.0],
         [2650.0, 1116.0],
         [2600.0, 1116.0],
         [2550.0, 1116.0],
         [2500.0, 1200.0],
         [2450.0, 1200.0],
         [2400.0, 1200.0],
         [2350.0, 1284.0],
         [2300.0, 1284.0],
         [2250.0, 1284.0],
         [2200.0, 1200.0],
         [2150.0, 1200.0],
         [2100.0, 1200.0],
         [2050.0, 1116.0],
         [2000.0, 1116.0],
         [1950.0, 1116.0],
         [1900.0, 1200.0],
         [1850.0, 1200.0],
         [1850.0, 800.0],
         [1850.0, 400.0],
         [1850.0, 0.0],
         [1850.0, 0.0]]
        self._samples_003 = [[3700.0, 0.0],
         [4100.0, 0.0],
         [4500.0, 0.0],
         [4900.0, 0.0],
         [4900.0, 120.0],
         [5077.0, 240.0],
         [5077.0, 360.0],
         [5077.0, 440.0],
         [4900.0, 520.0],
         [4900.0, 600.0],
         [4900.0, 680.0],
         [4723.0, 760.0],
         [4723.0, 840.0],
         [4723.0, 960.0],
         [4900.0, 1080.0],
         [4900.0, 1200.0],
         [4820.0, 1200.0],
         [4740.0, 1302.0],
         [4660.0, 1302.0],
         [4600.0, 1302.0],
         [4540.0, 1359.0],
         [4480.0, 1359.0],
         [4420.0, 1359.0],
         [4360.0, 1200.0],
         [4300.0, 1200.0],
         [4240.0, 1200.0],
         [4180.0, 1041.0],
         [4120.0, 1041.0],
         [4060.0, 1041.0],
         [4000.0, 1098.0],
         [3940.0, 1098.0],
         [3860.0, 1098.0],
         [3780.0, 1200.0],
         [3700.0, 1200.0],
         [3700.0, 800.0],
         [3700.0, 400.0],
         [3700.0, 0.0],
         [3700.0, 0.0]]
        self._samples_004 = [[5550.0, 0.0],
         [5950.0, 0.0],
         [6350.0, 0.0],
         [6750.0, 0.0],
         [6750.0, 80.0],
         [6852.0, 160.0],
         [6852.0, 240.0],
         [6852.0, 300.0],
         [6909.0, 360.0],
         [6909.0, 420.0],
         [6909.0, 480.0],
         [6750.0, 540.0],
         [6750.0, 600.0],
         [6750.0, 660.0],
         [6591.0, 720.0],
         [6591.0, 780.0],
         [6591.0, 840.0],
         [6648.0, 900.0],
         [6648.0, 960.0],
         [6648.0, 1040.0],
         [6750.0, 1120.0],
         [6750.0, 1200.0],
         [6630.0, 1200.0],
         [6510.0, 1377.0],
         [6390.0, 1377.0],
         [6310.0, 1377.0],
         [6230.0, 1200.0],
         [6150.0, 1200.0],
         [6070.0, 1200.0],
         [5990.0, 1023.0],
         [5910.0, 1023.0],
         [5790.0, 1023.0],
         [5670.0, 1200.0],
         [5550.0, 1200.0],
         [5550.0, 800.0],
         [5550.0, 400.0],
         [5550.0, 0.0],
         [5550.0, 0.0]]
        self._samples_005 = [[7400.0, 0.0],
         [7800.0, 0.0],
         [8200.0, 0.0],
         [8600.0, 0.0],
         [8600.0, 80.0],
         [8498.0, 160.0],
         [8498.0, 240.0],
         [8498.0, 300.0],
         [8441.0, 360.0],
         [8441.0, 420.0],
         [8441.0, 480.0],
         [8600.0, 540.0],
         [8600.0, 600.0],
         [8600.0, 660.0],
         [8759.0, 720.0],
         [8759.0, 780.0],
         [8759.0, 840.0],
         [8702.0, 900.0],
         [8702.0, 960.0],
         [8702.0, 1040.0],
         [8600.0, 1120.0],
         [8600.0, 1200.0],
         [8520.0, 1200.0],
         [8440.0, 1302.0],
         [8360.0, 1302.0],
         [8300.0, 1302.0],
         [8240.0, 1359.0],
         [8180.0, 1359.0],
         [8120.0, 1359.0],
         [8060.0, 1200.0],
         [8000.0, 1200.0],
         [7940.0, 1200.0],
         [7880.0, 1041.0],
         [7820.0, 1041.0],
         [7760.0, 1041.0],
         [7700.0, 1098.0],
         [7640.0, 1098.0],
         [7560.0, 1098.0],
         [7480.0, 1200.0],
         [7400.0, 1200.0],
         [7400.0, 800.0],
         [7400.0, 400.0],
         [7400.0, 0.0],
         [7400.0, 0.0]]
        self.id = 'Plane574'
        self.source_dataset = 'Author Designed'
        self.source_key = 'author-extensions95-v1:Plane278/extension_05'
        self.question = 'A square can be made out of four of the given pieces, with both straight sides of each piece on the outside. Pieces may be rotated or turned over. Which piece will not be used?\nChoices:\nA:A\nB:B\nC:C\nD:D\nE:E'
        self.answer = 'B'
        self.answer_type = 'choice'
        self.choices = {'A': 'A', 'B': 'B', 'C': 'C', 'D': 'D', 'E': 'E'}
        self.query = self.question
        self._geometry_01 = self._samples_001
        self._geometry_02 = [1, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 79]
        self._geometry_03 = self._samples_002
        self._geometry_04 = [1, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 79]
        self._geometry_05 = self._samples_003
        self._geometry_06 = [1, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 79]
        self._geometry_07 = self._samples_004
        self._geometry_08 = [1, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 79]
        self._geometry_09 = self._samples_005
        self._geometry_10 = [1, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 79]

    def draw(self, output_path=None, *, variant=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if variant not in self.variants:
                raise ValueError('Unknown Special variant: ' + str(variant))
            return getattr(self, 'draw_' + variant)(output_path)
        with Canvas(PLANE, xlim=(-215.9762596899227, 8987.330426356588), ylim=(-4149.622093023256, 5053.684593023256), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
            for object_id, vertices, codes in [('piece_A', self._geometry_01, self._geometry_02), ('piece_B', self._geometry_03, self._geometry_04), ('piece_C', self._geometry_05, self._geometry_06), ('piece_D', self._geometry_07, self._geometry_08), ('piece_E', self._geometry_09, self._geometry_10)]:
                c.path(vertices, codes, id=object_id, zorder=1, joinstyle='round', simplify=False)
            for object_id, text, anchor in [('label_A', 'A', (600, 600)), ('choice_label_A', '(A) A', (600, -360)), ('label_B', 'B', (2450, 600)), ('choice_label_B', '(B) B', (2450, -360)), ('label_C', 'C', (4300, 600)), ('choice_label_C', '(C) C', (4300, -360)), ('label_D', 'D', (6150, 600)), ('choice_label_D', '(D) D', (6150, -360)), ('label_E', 'E', (8000, 600)), ('choice_label_E', '(E) E', (8000, -360))]:
                c.text(text, anchor, id=object_id, zorder=3, rotation_mode='default')
            return c.save(output_path)

    def draw_C01(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane574_C01.png'
        _geometry_01 = self._samples_001
        _geometry_02 = [1, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 79]
        _geometry_03 = self._samples_002
        _geometry_04 = [1, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 79]
        _geometry_05 = self._samples_003
        _geometry_06 = [1, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 79]
        _geometry_07 = self._samples_004
        _geometry_08 = [1, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 79]
        _geometry_09 = self._samples_005
        _geometry_10 = [1, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 79]
        with Canvas(PLANE, xlim=(-215.9762596899227, 8987.330426356588), ylim=(-4149.622093023256, 5053.684593023256), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
            c.path(_geometry_01, _geometry_02, id='piece_A', zorder=1, joinstyle='round', simplify=False)
            c.path(_geometry_03, _geometry_04, id='piece_B', zorder=1, joinstyle='round', simplify=False)
            c.path(_geometry_05, _geometry_06, id='piece_C', zorder=1, edgecolor=(0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0), linewidth=2.0, joinstyle='round', simplify=False)
            c.path(_geometry_07, _geometry_08, id='piece_D', zorder=1, joinstyle='round', simplify=False)
            c.path(_geometry_09, _geometry_10, id='piece_E', zorder=1, joinstyle='round', simplify=False)
            for object_id, text, anchor in [('label_A', 'A', (600, 600)), ('choice_label_A', '(A) A', (600, -360)), ('label_B', 'B', (2450, 600)), ('choice_label_B', '(B) B', (2450, -360)), ('label_C', 'C', (4300, 600)), ('choice_label_C', '(C) C', (4300, -360)), ('label_D', 'D', (6150, 600)), ('choice_label_D', '(D) D', (6150, -360)), ('label_E', 'E', (8000, 600)), ('choice_label_E', '(E) E', (8000, -360))]:
                c.text(text, anchor, id=object_id, zorder=3, rotation_mode='default')
            return c.save(output_path)

    def draw_C02(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane574_C02.png'
        _geometry_01 = self._samples_001
        _geometry_02 = [1, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 79]
        _geometry_03 = self._samples_002
        _geometry_04 = [1, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 79]
        _geometry_05 = self._samples_003
        _geometry_06 = [1, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 79]
        _geometry_07 = self._samples_004
        _geometry_08 = [1, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 79]
        _geometry_09 = self._samples_005
        _geometry_10 = [1, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 79]
        with Canvas(PLANE, xlim=(-215.9762596899227, 8987.330426356588), ylim=(-4149.622093023256, 5053.684593023256), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
            c.path(_geometry_01, _geometry_02, id='piece_A', zorder=1, joinstyle='round', simplify=False)
            c.path(_geometry_03, _geometry_04, id='piece_B', zorder=1, joinstyle='round', simplify=False)
            c.path(_geometry_05, _geometry_06, id='piece_C', zorder=1, edgecolor=(0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0), linewidth=3.0, joinstyle='round', simplify=False)
            c.path(_geometry_07, _geometry_08, id='piece_D', zorder=1, joinstyle='round', simplify=False)
            c.path(_geometry_09, _geometry_10, id='piece_E', zorder=1, joinstyle='round', simplify=False)
            for object_id, text, anchor in [('label_A', 'A', (600, 600)), ('choice_label_A', '(A) A', (600, -360)), ('label_B', 'B', (2450, 600)), ('choice_label_B', '(B) B', (2450, -360)), ('label_C', 'C', (4300, 600)), ('choice_label_C', '(C) C', (4300, -360)), ('label_D', 'D', (6150, 600)), ('choice_label_D', '(D) D', (6150, -360)), ('label_E', 'E', (8000, 600)), ('choice_label_E', '(E) E', (8000, -360))]:
                c.text(text, anchor, id=object_id, zorder=3, rotation_mode='default')
            return c.save(output_path)

    def draw_C03(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane574_C03.png'
        _geometry_01 = self._samples_001
        _geometry_02 = [1, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 79]
        _geometry_03 = self._samples_002
        _geometry_04 = [1, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 79]
        _geometry_05 = self._samples_003
        _geometry_06 = [1, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 79]
        _geometry_07 = self._samples_004
        _geometry_08 = [1, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 79]
        _geometry_09 = self._samples_005
        _geometry_10 = [1, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 79]
        with Canvas(PLANE, xlim=(-215.9762596899227, 8987.330426356588), ylim=(-4149.622093023256, 5053.684593023256), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
            c.path(_geometry_01, _geometry_02, id='piece_A', zorder=1, joinstyle='round', simplify=False)
            c.path(_geometry_03, _geometry_04, id='piece_B', zorder=1, joinstyle='round', simplify=False)
            c.path(_geometry_05, _geometry_06, id='piece_C', zorder=1, edgecolor=(0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0), linewidth=2.0, joinstyle='round', simplify=False)
            c.path(_geometry_07, _geometry_08, id='piece_D', zorder=1, edgecolor=(0.08627450980392157, 0.6392156862745098, 0.2901960784313726, 1.0), joinstyle='round', simplify=False)
            c.path(_geometry_09, _geometry_10, id='piece_E', zorder=1, edgecolor=(0.08627450980392157, 0.6392156862745098, 0.2901960784313726, 1.0), joinstyle='round', simplify=False)
            for object_id, text, anchor in [('label_A', 'A', (600, 600)), ('choice_label_A', '(A) A', (600, -360)), ('label_B', 'B', (2450, 600)), ('choice_label_B', '(B) B', (2450, -360)), ('label_C', 'C', (4300, 600)), ('choice_label_C', '(C) C', (4300, -360)), ('label_D', 'D', (6150, 600)), ('choice_label_D', '(D) D', (6150, -360)), ('label_E', 'E', (8000, 600)), ('choice_label_E', '(E) E', (8000, -360))]:
                c.text(text, anchor, id=object_id, zorder=3, rotation_mode='default')
            return c.save(output_path)

    def draw_C04(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane574_C04.png'
        _geometry_01 = self._samples_001
        _geometry_02 = [1, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 79]
        _geometry_03 = self._samples_002
        _geometry_04 = [1, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 79]
        _geometry_05 = self._samples_003
        _geometry_06 = [1, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 79]
        _geometry_07 = self._samples_004
        _geometry_08 = [1, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 79]
        _geometry_09 = self._samples_005
        _geometry_10 = [1, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 79]
        with Canvas(PLANE, xlim=(-215.9762596899227, 8987.330426356588), ylim=(-4149.622093023256, 5053.684593023256), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
            c.path(_geometry_01, _geometry_02, id='piece_A', zorder=1, edgecolor=(0.9176470588235294, 0.34509803921568627, 0.047058823529411764, 1.0), joinstyle='round', simplify=False)
            c.path(_geometry_03, _geometry_04, id='piece_B', zorder=1, edgecolor=(0.9176470588235294, 0.34509803921568627, 0.047058823529411764, 1.0), joinstyle='round', simplify=False)
            c.path(_geometry_05, _geometry_06, id='piece_C', zorder=1, edgecolor=(0.1450980392156863, 0.38823529411764707, 0.9215686274509803, 1.0), linewidth=2.0, joinstyle='round', simplify=False)
            c.path(_geometry_07, _geometry_08, id='piece_D', zorder=1, edgecolor=(0.9176470588235294, 0.34509803921568627, 0.047058823529411764, 1.0), joinstyle='round', simplify=False)
            c.path(_geometry_09, _geometry_10, id='piece_E', zorder=1, edgecolor=(0.9176470588235294, 0.34509803921568627, 0.047058823529411764, 1.0), joinstyle='round', simplify=False)
            for object_id, text, anchor in [('label_A', 'A', (600, 600)), ('choice_label_A', '(A) A', (600, -360)), ('label_B', 'B', (2450, 600)), ('choice_label_B', '(B) B', (2450, -360)), ('label_C', 'C', (4300, 600)), ('choice_label_C', '(C) C', (4300, -360)), ('label_D', 'D', (6150, 600)), ('choice_label_D', '(D) D', (6150, -360)), ('label_E', 'E', (8000, 600)), ('choice_label_E', '(E) E', (8000, -360))]:
                c.text(text, anchor, id=object_id, zorder=3, rotation_mode='default')
            return c.save(output_path)

    def draw_C05(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane574_C05.png'
        _geometry_01 = self._samples_001
        _geometry_02 = [1, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 79]
        _geometry_03 = self._samples_002
        _geometry_04 = [1, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 79]
        _geometry_05 = self._samples_003
        _geometry_06 = [1, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 79]
        _geometry_07 = self._samples_004
        _geometry_08 = [1, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 79]
        _geometry_09 = self._samples_005
        _geometry_10 = [1, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 79]
        with Canvas(PLANE, xlim=(-215.9762596899227, 8987.330426356588), ylim=(-4149.622093023256, 5053.684593023256), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
            c.path(_geometry_01, _geometry_02, id='piece_A', zorder=1, edgecolor=(0.08627450980392157, 0.6392156862745098, 0.2901960784313726, 1.0), joinstyle='round', simplify=False)
            c.path(_geometry_03, _geometry_04, id='piece_B', zorder=1, joinstyle='round', simplify=False)
            c.path(_geometry_05, _geometry_06, id='piece_C', zorder=1, edgecolor=(0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0), linewidth=2.0, joinstyle='round', simplify=False)
            c.path(_geometry_07, _geometry_08, id='piece_D', zorder=1, joinstyle='round', simplify=False)
            c.path(_geometry_09, _geometry_10, id='piece_E', zorder=1, edgecolor=(0.08627450980392157, 0.6392156862745098, 0.2901960784313726, 1.0), joinstyle='round', simplify=False)
            for object_id, text, anchor in [('label_A', 'A', (600, 600)), ('choice_label_A', '(A) A', (600, -360)), ('label_B', 'B', (2450, 600)), ('choice_label_B', '(B) B', (2450, -360)), ('label_C', 'C', (4300, 600)), ('choice_label_C', '(C) C', (4300, -360)), ('label_D', 'D', (6150, 600)), ('choice_label_D', '(D) D', (6150, -360)), ('label_E', 'E', (8000, 600)), ('choice_label_E', '(E) E', (8000, -360))]:
                c.text(text, anchor, id=object_id, zorder=3, rotation_mode='default')
            return c.save(output_path)

    def draw_C06(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane574_C06.png'
        _geometry_01 = self._samples_001
        _geometry_02 = [1, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 79]
        _geometry_03 = self._samples_002
        _geometry_04 = [1, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 79]
        _geometry_05 = self._samples_003
        _geometry_06 = [1, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 79]
        _geometry_07 = self._samples_004
        _geometry_08 = [1, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 79]
        _geometry_09 = self._samples_005
        _geometry_10 = [1, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 79]
        with Canvas(PLANE, xlim=(-215.9762596899227, 8987.330426356588), ylim=(-4149.622093023256, 5053.684593023256), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
            c.path(_geometry_01, _geometry_02, id='piece_A', zorder=1, joinstyle='round', simplify=False)
            c.path(_geometry_03, _geometry_04, id='piece_B', zorder=1, joinstyle='round', simplify=False)
            c.path(_geometry_05, _geometry_06, id='piece_C', zorder=1, edgecolor=(0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0), linewidth=3.0, joinstyle='round', simplify=False)
            c.path(_geometry_07, _geometry_08, id='piece_D', zorder=1, edgecolor=(0.08627450980392157, 0.6392156862745098, 0.2901960784313726, 1.0), joinstyle='round', simplify=False)
            c.path(_geometry_09, _geometry_10, id='piece_E', zorder=1, edgecolor=(0.08627450980392157, 0.6392156862745098, 0.2901960784313726, 1.0), joinstyle='round', simplify=False)
            for object_id, text, anchor in [('label_A', 'A', (600, 600)), ('choice_label_A', '(A) A', (600, -360)), ('label_B', 'B', (2450, 600)), ('choice_label_B', '(B) B', (2450, -360)), ('label_C', 'C', (4300, 600)), ('choice_label_C', '(C) C', (4300, -360)), ('label_D', 'D', (6150, 600)), ('choice_label_D', '(D) D', (6150, -360)), ('label_E', 'E', (8000, 600)), ('choice_label_E', '(E) E', (8000, -360))]:
                c.text(text, anchor, id=object_id, zorder=3, rotation_mode='default')
            return c.save(output_path)
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Plane574')
    parser.add_argument('output', nargs='?')
    parser.add_argument('--variant', choices=('C01', 'C02', 'C03', 'C04', 'C05', 'C06'))
    args = parser.parse_args()
    print(Plane574().draw(args.output, variant=args.variant))
