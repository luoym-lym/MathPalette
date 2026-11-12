"""Frozen question Plane110; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane110:

    def __init__(self):
        self.id = 'Plane110'
        self.source_dataset = 'Author Designed'
        self.source_key = 'intersection-counting:unequal_circles_four_crossings'
        self.question = 'How many points of intersection are shown in the figure?'
        self.answer = 4
        self.answer_type = 'number'
        self.query = self.question
        self.points = {'center_0': [-0.85, 0.35],
         'center_1': [0.9, 0.05],
         'center_2': [1.65, 1.4],
         'crossing_1': [0.15902991149963308, -1.0181588495854723],
         'crossing_2': [0.557108074225981, 1.303963766318224],
         'crossing_3': [1.002249241804092, 1.3459726434421708],
         'crossing_4': [1.9463356638562852, 0.8214801867465081]}
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane110.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-2.662790697674419, 2.412790697674419], ylim=[-2.1877906976744192, 2.8877906976744185]) as c:
            for object_id, center, radius in [('curve_0', self.points['center_0'], 1.7), ('curve_1', self.points['center_1'], 1.3), ('curve_2', self.points['center_2'], 0.65)]:
                c.circle(center, radius, id=object_id)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane110().draw(sys.argv[1] if len(sys.argv) > 1 else None))
