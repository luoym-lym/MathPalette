"""Collected question Plane106; construction on the shared drawing protocol."""
from pathlib import Path
import sys
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from MathPalette_Dataset.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane106:
    variants = ('C01', 'C02', 'C03', 'C04')

    def __init__(self):
        self._samples_001 = [[-1.921539030917347, 3.4],
         [-2.1321673450494085, 3.764818941589308],
         [-2.4351810584106923, 4.067832654950592],
         [-2.8000000000000003, 4.278460969082653],
         [-3.1648189415893087, 4.489089283214714],
         [-3.578743371735877, 4.6],
         [-4.0, 4.6],
         [-4.421256628264123, 4.6],
         [-4.835181058410693, 4.489089283214714],
         [-5.2, 4.278460969082653],
         [-5.564818941589309, 4.067832654950591],
         [-5.8678326549505915, 3.764818941589308],
         [-6.078460969082653, 3.4]]
        self._samples_002 = [[1.6, 5.199999999999999],
         [1.6, 4.563724543620873],
         [1.8530290352440404, 3.952858415060531],
         [2.3029437251522857, 3.5029437251522855],
         [2.7528584150605306, 3.05302903524404],
         [3.3637245436208736, 2.7999999999999994],
         [3.9999999999999996, 2.7999999999999994],
         [4.636275456379126, 2.7999999999999994],
         [5.2471415849394685, 3.0530290352440397],
         [5.697056274847713, 3.502943725152285],
         [6.146970964755959, 3.95285841506053],
         [6.3999999999999995, 4.563724543620873],
         [6.4, 5.199999999999998]]
        self._samples_003 = [[-2.44115427318801, -4.449999999999999],
         [-2.5991255087870564, -4.176385793808018],
         [-2.826385793808019, -3.949125508787056],
         [-3.1, -3.7911542731880097],
         [-3.3736142061919816, -3.6331830375889638],
         [-3.6840575288019077, -3.55],
         [-4.0, -3.55],
         [-4.315942471198092, -3.55],
         [-4.626385793808019, -3.6331830375889638],
         [-4.9, -3.79115427318801],
         [-5.173614206191981, -3.9491255087870565],
         [-5.400874491212944, -4.176385793808018],
         [-5.55884572681199, -4.449999999999999]]
        self.id = 'Plane106'
        self.source_dataset = 'Author Designed'
        self.source_key = 'visual-matching:arc_radius'
        self.question = 'All arcs use the same scale. Which arc, A, B, or C, belongs to a circle with the same radius as R?\nChoices:\nA: Arc A\nB: Arc B\nC: Arc C'
        self.answer = 'A'
        self.answer_type = 'choice'
        self.choices = {'A': 'Arc A', 'B': 'Arc B', 'C': 'Arc C'}
        self.query = self.question
        self.points = {'R_0': [-1.921539030917347, 3.4],
         'R_1': [-4.0, 4.6],
         'R_2': [-6.078460969082653, 3.4],
         'name_anchor_R': [-4.0, 3.4],
         'A_0': [1.6, 5.199999999999999],
         'A_1': [3.9999999999999996, 2.7999999999999994],
         'A_2': [6.4, 5.199999999999998],
         'name_anchor_A': [4.0, 2.7999999999999994],
         'B_0': [-2.44115427318801, -4.449999999999999],
         'B_1': [-4.0, -3.55],
         'B_2': [-5.55884572681199, -4.449999999999999],
         'name_anchor_B': [-4.0, -4.449999999999999],
         'C_0': [6.121320343559643, -4.439339828220178],
         'C_1': [4.0, -3.560660171779821],
         'C_2': [1.8786796564403576, -4.439339828220178],
         'name_anchor_C': [4.0, -4.439339828220178]}

    def draw(self, output_path=None, *, variant=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if variant not in self.variants:
                raise ValueError('Unknown Special variant: ' + str(variant))
            return getattr(self, 'draw_' + variant)(output_path)
        with Canvas(PLANE, xlim=[-6.368657735805505, 6.690196766722852], ylim=[-6.548031806823602, 6.510822695704755]) as c:
            for object_id, center, radius, start, end in [('arc_R', [-4.0, 2.2], 2.4, 30, 150), ('arc_A', [4.0, 5.199999999999999], 2.4, 180, 360), ('arc_B', [-4.0, -5.35], 1.8, 30, 150), ('arc_C', [4.0, -6.560660171779821], 3.0, 45, 135)]:
                c.arc(center, radius, start, end, id=object_id)
            for object_id, text, anchor in [('name_R', 'R', self.points['name_anchor_R']), ('name_A', 'A', self.points['name_anchor_A']), ('name_B', 'B', self.points['name_anchor_B']), ('name_C', 'C', self.points['name_anchor_C'])]:
                c.text(text, anchor, id=object_id, offset_pt=[0, -22], vertex=False)
            return c.save(output_path)

    def draw_C01(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane106_C01.png'
        with Canvas(PLANE, xlim=(-6.368657735805505, 6.690196766722852), ylim=(-6.548031806823602, 6.510822695704755), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
            c.path(self._samples_001, [1, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4], id='arc_R', edgecolor=(0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0), capstyle='butt', fill=False)
            c.path(self._samples_002, [1, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4], id='arc_A', edgecolor=(0.1450980392156863, 0.38823529411764707, 0.9215686274509803, 1.0), capstyle='butt', fill=False)
            c.path(self._samples_003, [1, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4], id='arc_B', edgecolor=(0.1450980392156863, 0.38823529411764707, 0.9215686274509803, 1.0), capstyle='butt', fill=False)
            c.path([[6.121320343559643, -4.439339828220179], [5.558926981174336, -3.876946465834872], [4.795344320473908, -3.560660171779821], [4.0, -3.560660171779821], [3.204655679526093, -3.560660171779821], [2.4410730188256644, -3.876946465834872], [1.8786796564403576, -4.439339828220178]], [1, 4, 4, 4, 4, 4, 4], id='arc_C', edgecolor=(0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0), capstyle='butt', fill=False)
            for object_id, text, anchor in [('name_R', 'R', (-4.0, 3.4)), ('name_A', 'A', (4.0, 2.7999999999999994)), ('name_B', 'B', (-4.0, -4.449999999999999)), ('name_C', 'C', (4.0, -4.439339828220178))]:
                c.text(text, anchor, id=object_id, rotation_mode='default', offset_pt=(0, -22), annotation_clip=None)
            return c.save(output_path)

    def draw_C02(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane106_C02.png'
        with Canvas(PLANE, xlim=(-6.368657735805505, 6.690196766722852), ylim=(-6.548031806823602, 6.510822695704755), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
            c.path(self._samples_001, [1, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4], id='arc_R', edgecolor=(0.1450980392156863, 0.38823529411764707, 0.9215686274509803, 1.0), capstyle='butt', fill=False)
            c.path(self._samples_002, [1, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4], id='arc_A', capstyle='butt', fill=False)
            c.path(self._samples_003, [1, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4], id='arc_B', capstyle='butt', fill=False)
            c.path([[6.121320343559643, -4.439339828220179], [5.558926981174336, -3.876946465834872], [4.795344320473908, -3.560660171779821], [4.0, -3.560660171779821], [3.204655679526093, -3.560660171779821], [2.4410730188256644, -3.876946465834872], [1.8786796564403576, -4.439339828220178]], [1, 4, 4, 4, 4, 4, 4], id='arc_C', edgecolor=(0.1450980392156863, 0.38823529411764707, 0.9215686274509803, 1.0), capstyle='butt', fill=False)
            for object_id, text, anchor in [('name_R', 'R', (-4.0, 3.4)), ('name_A', 'A', (4.0, 2.7999999999999994)), ('name_B', 'B', (-4.0, -4.449999999999999)), ('name_C', 'C', (4.0, -4.439339828220178))]:
                c.text(text, anchor, id=object_id, rotation_mode='default', offset_pt=(0, -22), annotation_clip=None)
            return c.save(output_path)

    def draw_C03(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane106_C03.png'
        with Canvas(PLANE, xlim=(-6.368657735805505, 6.690196766722852), ylim=(-6.548031806823602, 6.510822695704755), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
            c.path(self._samples_001, [1, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4], id='arc_R', edgecolor=(0.9176470588235294, 0.34509803921568627, 0.047058823529411764, 1.0), capstyle='butt', fill=False)
            c.path(self._samples_002, [1, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4], id='arc_A', capstyle='butt', fill=False)
            c.path(self._samples_003, [1, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4], id='arc_B', edgecolor=(0.9176470588235294, 0.34509803921568627, 0.047058823529411764, 1.0), capstyle='butt', fill=False)
            c.path([[6.121320343559643, -4.439339828220179], [5.558926981174336, -3.876946465834872], [4.795344320473908, -3.560660171779821], [4.0, -3.560660171779821], [3.204655679526093, -3.560660171779821], [2.4410730188256644, -3.876946465834872], [1.8786796564403576, -4.439339828220178]], [1, 4, 4, 4, 4, 4, 4], id='arc_C', capstyle='butt', fill=False)
            for object_id, text, anchor in [('name_R', 'R', (-4.0, 3.4)), ('name_A', 'A', (4.0, 2.7999999999999994)), ('name_B', 'B', (-4.0, -4.449999999999999)), ('name_C', 'C', (4.0, -4.439339828220178))]:
                c.text(text, anchor, id=object_id, rotation_mode='default', offset_pt=(0, -22), annotation_clip=None)
            return c.save(output_path)

    def draw_C04(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane106_C04.png'
        with Canvas(PLANE, xlim=(-6.368657735805505, 6.690196766722852), ylim=(-6.548031806823602, 6.510822695704755), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
            c.path(self._samples_001, [1, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4], id='arc_R', linestyle=(0, [3.7, 1.6]), capstyle='butt', fill=False)
            c.path(self._samples_002, [1, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4], id='arc_A', capstyle='butt', fill=False)
            c.path(self._samples_003, [1, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4], id='arc_B', linestyle=(0, [3.7, 1.6]), capstyle='butt', fill=False)
            c.path([[6.121320343559643, -4.439339828220179], [5.558926981174336, -3.876946465834872], [4.795344320473908, -3.560660171779821], [4.0, -3.560660171779821], [3.204655679526093, -3.560660171779821], [2.4410730188256644, -3.876946465834872], [1.8786796564403576, -4.439339828220178]], [1, 4, 4, 4, 4, 4, 4], id='arc_C', capstyle='butt', fill=False)
            for object_id, text, anchor in [('name_R', 'R', (-4.0, 3.4)), ('name_A', 'A', (4.0, 2.7999999999999994)), ('name_B', 'B', (-4.0, -4.449999999999999)), ('name_C', 'C', (4.0, -4.439339828220178))]:
                c.text(text, anchor, id=object_id, rotation_mode='default', offset_pt=(0, -22), annotation_clip=None)
            return c.save(output_path)
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Plane106')
    parser.add_argument('output', nargs='?')
    parser.add_argument('--variant', choices=('C01', 'C02', 'C03', 'C04'))
    args = parser.parse_args()
    print(Plane106().draw(args.output, variant=args.variant))
