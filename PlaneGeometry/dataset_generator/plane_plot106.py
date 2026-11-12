"""Frozen question Plane106; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane106:

    def __init__(self):
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
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane106.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-6.368657735805505, 6.690196766722852], ylim=[-6.548031806823602, 6.510822695704755]) as c:
            for object_id, center, radius, start, end in [('arc_R', [-4.0, 2.2], 2.4, 30, 150), ('arc_A', [4.0, 5.199999999999999], 2.4, 180, 360), ('arc_B', [-4.0, -5.35], 1.8, 30, 150), ('arc_C', [4.0, -6.560660171779821], 3.0, 45, 135)]:
                c.arc(center, radius, start, end, id=object_id)
            for object_id, text, anchor in [('name_R', 'R', self.points['name_anchor_R']), ('name_A', 'A', self.points['name_anchor_A']), ('name_B', 'B', self.points['name_anchor_B']), ('name_C', 'C', self.points['name_anchor_C'])]:
                c.text(text, anchor, id=object_id, offset_pt=[0, -22], vertex=False)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane106().draw(sys.argv[1] if len(sys.argv) > 1 else None))
