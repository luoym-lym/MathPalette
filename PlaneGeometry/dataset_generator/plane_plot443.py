"""Frozen question Plane443; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane443:

    def __init__(self):
        self.id = 'Plane443'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:2196'
        self.question = 'A rectangular piece of paper whose length is $\\sqrt{3}$ times the width has area $A$. The paper is divided into equal sections along the opposite lengths, and then a dotted line is drawn from the first divider to the second divider on the opposite side as shown. The paper is then folded flat along this dotted line to create a new shape with area $B$. What is the ratio $B:A$?\n\nChoices:\nA:1:2\nB:3:5\nC:2:3\nD:3:4\nE:4:5'
        self.answer = 'C'
        self.answer_type = 'choice'
        self.choices = {'A': '1:2', 'B': '3:5', 'C': '2:3', 'D': '3:4', 'E': '4:5'}
        self.query = self.question
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane443.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-0.04327013791133705, 1.7790660241709069], ylim=[-0.4127605524532116, 1.4095756096290322]) as c:
            c.path([[0, 0], [1.7320508075688772, 0], [1.7320508075688772, 1], [0, 1], [0, 0]], [1, 2, 2, 2, 79], id='o0')
            c.line([[0.5773502691896257, 1], [0.5773502691896257, 0.95]], id='o1')
            c.line([[1.1547005383792515, 0], [1.1547005383792515, 0.05]], id='o2')
            c.line([[0.5773502691896257, 0], [1.1547005383792515, 1]], id='o3', linestyle=(0, [4, 3]))
            c.point([[0.5773502691896257, 0]], filled=True, id='o4')
            c.point([[1.1547005383792515, 1]], filled=True, id='o5')
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane443().draw(sys.argv[1] if len(sys.argv) > 1 else None))
