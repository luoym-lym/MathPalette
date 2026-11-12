"""Frozen question Plane354; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane354:

    def __init__(self):
        self.id = 'Plane354'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:1214'
        self.question = 'Five identical right-angled triangles can be arranged so that their larger acute angles touch to form the star shown in the diagram. It is also possible to form a different star by arranging more of these triangles so that their smaller acute angles touch. How many triangles are needed to form the second star?'
        self.answer = '20'
        self.answer_type = 'number'
        self.query = self.question
        self.points = {'O': [0, 0],
         'T0': [6.123233995736766e-17, 1.0],
         'F0': [-0.29389262614623657, 0.09549150281252632],
         'T1': [-0.9510565162951535, 0.3090169943749475],
         'F1': [-0.18163563200134028, -0.25],
         'T2': [-0.5877852522924732, -0.8090169943749473],
         'F2': [0.18163563200134017, -0.25000000000000006],
         'T3': [0.5877852522924729, -0.8090169943749476],
         'F3': [0.2938926261462366, 0.09549150281252622],
         'T4': [0.9510565162951536, 0.3090169943749472],
         'F4': [9.460916826085377e-17, 0.30901699437494745]}
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane354.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-0.9978354833859573, 0.9978354833859575], ylim=[-0.9039221276544258, 1.091748839117489]) as c:
            for object_id, vertices, codes in [('triangle0', [self.points['O'], self.points['T0'], self.points['F0'], self.points['O']], [1, 2, 2, 79]), ('triangle1', [self.points['O'], self.points['T1'], self.points['F1'], self.points['O']], [1, 2, 2, 79]), ('triangle2', [self.points['O'], self.points['T2'], self.points['F2'], self.points['O']], [1, 2, 2, 79]), ('triangle3', [self.points['O'], self.points['T3'], self.points['F3'], self.points['O']], [1, 2, 2, 79]), ('triangle4', [self.points['O'], self.points['T4'], self.points['F4'], self.points['O']], [1, 2, 2, 79])]:
                c.path(vertices, codes, id=object_id)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane354().draw(sys.argv[1] if len(sys.argv) > 1 else None))
