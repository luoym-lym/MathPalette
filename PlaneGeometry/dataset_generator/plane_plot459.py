"""Frozen question Plane459; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane459:

    def __init__(self):
        self.id = 'Plane459'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:2597'
        self.question = 'How many triangles are in this figure? (Some triangles may overlap other triangles.)'
        self.answer = '5'
        self.answer_type = 'number'
        self.query = self.question
        self.points = {'A': [0, 0], 'B': [2, 3], 'C': [6, 0], 'D': [2.6, 0], 'E': [3.7199999999999998, 1.71]}
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane459.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-0.14756257214905721, 6.147569736501865], ylim=[-1.647566154325461, 4.647566154325461]) as c:
            c.path([self.points['A'], self.points['B'], self.points['C'], self.points['A']], [1, 2, 2, 79], id='outer')
            c.line([self.points['B'], self.points['D']], id='BD')
            c.line([self.points['D'], self.points['E']], id='DE')
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane459().draw(sys.argv[1] if len(sys.argv) > 1 else None))
