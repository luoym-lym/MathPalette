"""Frozen question Plane334; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane334:

    def __init__(self):
        self.id = 'Plane334'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:1083'
        self.question = 'Each of the nine paths shown is $100 \\mathrm{~m}$ long. What is the length of the longest route from $A$ to $B$ that does not use any path twice?\nChoices:\nA:$900 \\mathrm{~m}$\nB:$800 \\mathrm{~m}$\nC:$700 \\mathrm{~m}$\nD:$500 \\mathrm{~m}$\nE:$400 \\mathrm{~m}$'
        self.answer = 'C'
        self.answer_type = 'choice'
        self.choices = {'A': '$900 \\mathrm{~m}$', 'B': '$800 \\mathrm{~m}$', 'C': '$700 \\mathrm{~m}$', 'D': '$500 \\mathrm{~m}$', 'E': '$400 \\mathrm{~m}$'}
        self.query = self.question
        self.points = {'L': [0, 0], 'M': [1, 0], 'A': [2, 0], 'U': [0.5, 0.8660254037844386], 'V': [1.5, 0.8660254037844386], 'B': [1, 1.7320508075688772]}
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane334.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-0.0514865034906451, 2.141325625542783], ylim=[-0.19702959364009454, 1.9957825353933334]) as c:
            for object_id, points in [('path0', [self.points['L'], self.points['M']]), ('path1', [self.points['M'], self.points['A']]), ('path2', [self.points['L'], self.points['U']]), ('path3', [self.points['U'], self.points['B']]), ('path4', [self.points['B'], self.points['V']]), ('path5', [self.points['V'], self.points['A']]), ('path6', [self.points['U'], self.points['V']]), ('path7', [self.points['U'], self.points['M']]), ('path8', [self.points['M'], self.points['V']])]:
                c.line(points, id=object_id)
            c.text('A', self.points['A'], offset_pt=[15, 0], vertex=True, id='Aname')
            c.text('B', self.points['B'], offset_pt=[12, 12], vertex=True, id='Bname')
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane334().draw(sys.argv[1] if len(sys.argv) > 1 else None))
