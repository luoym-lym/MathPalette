"""Frozen question Plane442; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane442:

    def __init__(self):
        self.id = 'Plane442'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:2181'
        self.question = 'A dart board is a regular octagon divided into regions as shown. Suppose that a dart thrown at the board is equally likely to land anywhere on the board. What is the probability that the dart lands within the center square?\n\nChoices:\nA:$\\frac{\\sqrt{2} - 1}{2}$\nB:$\\frac{1}{4}$\nC:$\\frac{2 - \\sqrt{2}}{2}$\nD:$\\frac{\\sqrt{2}}{4}$\nE:$2 - \\sqrt{2}$'
        self.answer = 'A'
        self.answer_type = 'choice'
        self.choices = {'A': '$\\frac{\\sqrt{2} - 1}{2}$', 'B': '$\\frac{1}{4}$', 'C': '$\\frac{2 - \\sqrt{2}}{2}$', 'D': '$\\frac{\\sqrt{2}}{4}$', 'E': '$2 - \\sqrt{2}$'}
        self.query = self.question
        self.points = {'0': [-1, 2.414213562373095],
         '1': [1, 2.414213562373095],
         '2': [2.414213562373095, 1],
         '3': [2.414213562373095, -1],
         '4': [1, -2.414213562373095],
         '5': [-1, -2.414213562373095],
         '6': [-2.414213562373095, -1],
         '7': [-2.414213562373095, 1]}
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane442.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-2.5338808617794584, 2.5419147096572354], ylim=[-2.5419147096572354, 2.5338808617794584]) as c:
            c.path([self.points['0'], self.points['1'], self.points['2'], self.points['3'], self.points['4'], self.points['5'], self.points['6'], self.points['7'], self.points['0']], [1, 2, 2, 2, 2, 2, 2, 2, 79], id='octagon')
            for object_id, points in [('interior0', [self.points['0'], self.points['5']]), ('interior1', [self.points['1'], self.points['4']]), ('interior2', [self.points['7'], self.points['2']]), ('interior3', [self.points['6'], self.points['3']])]:
                c.line(points, id=object_id)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane442().draw(sys.argv[1] if len(sys.argv) > 1 else None))
