"""Frozen question Plane382; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane382:

    def __init__(self):
        self.id = 'Plane382'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:1511'
        self.question = 'The diagram shows a spiral of isosceles triangles. The largest angle in each triangle is $100^{\\circ}$. The grey triangle is number 0. Each subsequent triangle (numbered 1, 2, 3,...) joins the previous one along an edge, as shown. Triangle 3 only partially covers triangle 0. What is the number of the first triangle that exactly covers triangle 0?'
        self.answer = '18'
        self.answer_type = 'number'
        self.query = self.question
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane382.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-2.6547742008827497, 3.1756075342160828], ylim=[-3.088814251552175, 2.7415674835466577], axes_position=[0.05, 0.05, 0.9, 0.9], coordinate_axes=False) as c:
            c.path([[0.0, 0.0], [0.5209445330007912, -2.954423259036624], [2.8190778623577253, 1.0260604299770062], [0.0, 0.0]], [1, 2, 2, 79], id='o0', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45], linewidth=0.0, capstyle='butt')
            c.path([[0.0, 0.0], [0.5209445330007912, -2.954423259036624], [2.8190778623577253, 1.0260604299770062], [0.0, 0.0]], [1, 2, 2, 79], id='o0', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            for object_id, points in [('o1', [[2.8190778623577253, 1.0260604299770062], [-1.4999999999999993, 2.598076211353316]]), ('o2', [[-1.4999999999999993, 2.598076211353316], [-2.298133329356934, -1.9283628290596178]]), ('o3', [[-2.298133329356934, -1.9283628290596178], [2.2981333293569333, -1.9283628290596186]]), ('o6', [[0.0, 0.0], [-1.4999999999999993, 2.598076211353316]]), ('o7', [[0.0, 0.0], [-2.298133329356934, -1.9283628290596178]]), ('o8', [[0.0, 0.0], [2.2981333293569333, -1.9283628290596186]])]:
                c.line(points, id=object_id)
            for object_id, text, anchor in [('t0', '0', [1.1133407984528387, -0.6427876096865393]), ('t1', '1', [0.43969262078590865, 1.2080455471101075]), ('t2', '2', [-1.266044443118978, 0.22323779409789943]), ('t3', '3', [-2.6645352591003756e-16, -1.1570176974357709])]:
                c.text(text, anchor, id=object_id, rotation_mode='default', offset_pt=[0, 0], annotation_clip=None)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane382().draw(sys.argv[1] if len(sys.argv) > 1 else None))
