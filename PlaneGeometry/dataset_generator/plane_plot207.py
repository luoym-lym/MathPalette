"""Frozen question Plane207; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane207:

    def __init__(self):
        self.id = 'Plane207'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:503'
        self.question = 'The rectangular mirror has broken. Which piece is missing?\nChoices:\nA:(A)\nB:(B)\nC:(C)\nD:(D)\nE:(E)'
        self.answer = 'B'
        self.answer_type = 'choice'
        self.choices = {'A': '(A)', 'B': '(B)', 'C': '(C)', 'D': '(D)', 'E': '(E)'}
        self.query = self.question
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane207.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-1.771491528731305, 22.76698405277603], ylim=[-7.805848790834414, 16.73262679067292]) as c:
            c.path([[8.5, 9.5], [11.6, 9.5], [11.6, 4.5], [10.05, 4.5], [10.45, 7.35], [8.5, 5.5], [8.5, 9.5]], [1, 2, 2, 2, 2, 2, 79], id='broken_mirror')
            for object_id, points in [('fracture0', [[10.45, 7.35], [9.95, 9.5]]), ('fracture1', [[10.45, 7.35], [8.5, 7.8]]), ('fracture2', [[10.45, 7.35], [8.5, 7.1]]), ('fracture3', [[10.45, 7.35], [8.5, 6.3]]), ('fracture4', [[10.45, 7.35], [11.6, 8.0]]), ('fracture5', [[10.45, 7.35], [11.6, 6.05]])]:
                c.line(points, id=object_id)
            for object_id, vertices, codes in [('option0', [[0, 0.4], [0, 1.9], [2.7, 0.0], [0, 0.4]], [1, 2, 2, 79]), ('option1', [[5.0, 1.5349155065494342], [5.215718306488101, 0.0], [8.093651542785604, 0.0005361102395586848], [5.99026806874157, 1.6740886075094996], [5.0, 1.5349155065494342]], [1, 2, 2, 2, 79]), ('option2', [[10, 0.35], [10, 1.85], [10.9, 1.85], [11.8, 1.35], [12.6, 0.0], [10, 0.35]], [1, 2, 2, 2, 2, 79]), ('option3', [[15, 0.4], [15.25, 1.65], [15.95, 1.9], [17.7, 0.0], [15, 0.4]], [1, 2, 2, 2, 79]), ('option4', [[20, 0.35], [19.65, 2.05], [21, 1.9], [22.2, 0.0], [20, 0.35]], [1, 2, 2, 2, 79])]:
                c.path(vertices, codes, id=object_id)
            for object_id, text, anchor in [('label0', '(A)', [-0.7, -0.3]), ('label1', '(B)', [4.3, -0.3]), ('label2', '(C)', [9.3, -0.3]), ('label3', '(D)', [14.3, -0.3]), ('label4', '(E)', [19.3, -0.3])]:
                c.text(text, anchor, id=object_id, offset_pt=[0, 0], vertex=False)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane207().draw(sys.argv[1] if len(sys.argv) > 1 else None))
