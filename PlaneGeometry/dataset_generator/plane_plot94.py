"""Frozen question Plane94; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane94:

    def __init__(self):
        self.id = 'Plane94'
        self.source_dataset = 'Author Designed'
        self.source_key = 'smooth-curve:02'
        self.question = 'Starting at D, which endpoint is reached along the same smooth curve, without switching curves at any crossing?'
        self.answer = 'A'
        self.answer_type = 'text'
        self.query = self.question
        self.points = {'C': [-1.0, 0.45], 'B': [1.0, 0.45], 'A': [-1.0, -0.45], 'D': [1.0, -0.45], 'J01': [-0.7071067811865475, 0.0], 'J02': [0.7071067811865476, 0.0]}
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane94.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-1.1497850639678173, 1.1497902978469967], ylim=[-1.1411083357346676, 1.1584670260801464]) as c:
            for object_id, vertices, codes in [('CB_s01_C_J01', [[-1.0, 0.45], [-0.9023689270621824, 0.27426406871192854], [-0.8047378541243649, 0.12426406871192855], [-0.7071067811865475, 0.0]], [1, 4, 4, 4]), ('CB_s02_J01_J02', [[-0.7071067811865475, 0.0], [-0.23570226039551587, -0.6], [0.2357022603955159, -0.5999999999999999], [0.7071067811865476, 0.0]], [1, 4, 4, 4]), ('CB_s03_J02_B', [[0.7071067811865476, 0.0], [0.804737854124365, 0.12426406871192856], [0.9023689270621825, 0.27426406871192854], [1.0, 0.45]], [1, 4, 4, 4]), ('AD_s01_A_J01', [[-1.0, -0.45], [-0.9023689270621824, -0.27426406871192854], [-0.8047378541243649, -0.12426406871192855], [-0.7071067811865475, 0.0]], [1, 4, 4, 4]), ('AD_s02_J01_J02', [[-0.7071067811865475, 0.0], [-0.23570226039551587, 0.6], [0.2357022603955159, 0.5999999999999999], [0.7071067811865476, 0.0]], [1, 4, 4, 4]), ('AD_s03_J02_D', [[0.7071067811865476, 0.0], [0.804737854124365, -0.12426406871192856], [0.9023689270621825, -0.27426406871192854], [1.0, -0.45]], [1, 4, 4, 4])]:
                c.path(vertices, codes, id=object_id, capstyle='butt', zorder=1)
            c.text('C', self.points['C'], offset_pt=[-8.0, -0.0], vertex=True, ha='right')
            c.text('B', self.points['B'], offset_pt=[8.0, 0.0], vertex=True, ha='left')
            c.text('A', self.points['A'], offset_pt=[-8.0, -0.0], vertex=True, ha='right')
            c.text('D', self.points['D'], offset_pt=[8.0, 0.0], vertex=True, ha='left')
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane94().draw(sys.argv[1] if len(sys.argv) > 1 else None))
