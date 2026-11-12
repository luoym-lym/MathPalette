"""Frozen question Plane112; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane112:

    def __init__(self):
        self.id = 'Plane112'
        self.source_dataset = 'Author Designed'
        self.source_key = 'intersection-counting:two_circles_offcenter_line'
        self.question = 'What is the total number of intersection points in the diagram?'
        self.answer = 6
        self.answer_type = 'number'
        self.query = self.question
        self.points = {'left_circle_center': [-0.9, 0.25],
         'right_circle_center': [1.0, 0.05],
         'line_a': [-3.0, -1.08],
         'line_b': [3.0, -0.12],
         'crossing_1': [-1.9926368849521967, -0.9188219015923516],
         'crossing_2': [-0.3255463966993375, -0.6520874234718941],
         'crossing_3': [0.0030760337958954387, -1.0707776789389936],
         'crossing_4': [0.25829382921780325, 1.3537913775691304],
         'crossing_5': [0.5027772905684218, -0.5195556335090525],
         'crossing_6': [2.4784325121439554, -0.20345079805696709]}
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane112.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-3.1395348837209305, 3.1395348837209305], ylim=[-2.9395348837209303, 3.3395348837209307]) as c:
            c.circle(self.points['left_circle_center'], 1.6, id='left_circle')
            c.circle(self.points['right_circle_center'], 1.5, id='right_circle')
            c.line([self.points['line_a'], self.points['line_b']], id='line')
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane112().draw(sys.argv[1] if len(sys.argv) > 1 else None))
