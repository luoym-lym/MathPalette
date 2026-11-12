"""Frozen question Solid171; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Solid171:

    def __init__(self):
        self.id = 'Solid171'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:1554'
        self.question = 'A shape is made by cutting all the corners off a cube, as shown in the diagram. How many edges does the shape have?'
        self.answer = '36'
        self.answer_type = 'number'
        self.query = self.question
        self.subject = 'SolidGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'SolidGeometry' / 'dataset_generator/scenes/Solid171.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('SolidGeometry', self.id, variant, output_path)
        with Canvas(SOLID, xlim=(-0.037357737811214875, 1.5396288133926102), ylim=(-0.03962881339261015, 1.5373577378112149), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
            for object_id, vertices, codes in [('truncatedface7', [[0.18, 1.0], [0.09, 1.09], [0.0, 0.8200000000000001], [0.18, 1.0]], [1, 2, 2, 79]), ('truncatedface10', [[0.8200000000000001, 0.0], [1.09, 0.09], [1.0, 0.18], [0.8200000000000001, 0.0]], [1, 2, 2, 79]), ('truncatedface11', [[0.8200000000000001, 1.0], [1.09, 1.09], [1.0, 0.8200000000000001], [0.8200000000000001, 1.0]], [1, 2, 2, 79])]:
                c.path(vertices, codes, id=object_id, alpha=1.0, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            for object_id, points in [('truncatedv10v4', [[0.41000000000000003, 1.4100000000000001], [0.09, 1.09]]), ('truncatedv4v5', [[0.09, 1.09], [0.0, 0.8200000000000001]]), ('truncatedv2v5', [[0.0, 0.18], [0.0, 0.8200000000000001]]), ('truncatedv13v14', [[1.09, 0.09], [1.0, 0.18]]), ('truncatedv13v19', [[1.09, 0.09], [1.4100000000000001, 0.41000000000000003]]), ('truncatedv19v20', [[1.4100000000000001, 0.41000000000000003], [1.5, 0.6799999999999999]]), ('truncatedv20v23', [[1.5, 0.6799999999999999], [1.5, 1.32]]), ('truncatedv22v23', [[1.4100000000000001, 1.4100000000000001], [1.5, 1.32]]), ('truncatedv16v22', [[1.09, 1.09], [1.4100000000000001, 1.4100000000000001]]), ('truncatedv16v17', [[1.09, 1.09], [1.0, 0.8200000000000001]]), ('truncatedv14v17', [[1.0, 0.18], [1.0, 0.8200000000000001]]), ('truncatedv0v2', [[0.18, 0.0], [0.0, 0.18]]), ('truncatedv0v12', [[0.18, 0.0], [0.8200000000000001, 0.0]]), ('truncatedv12v14', [[0.8200000000000001, 0.0], [1.0, 0.18]]), ('truncatedv15v17', [[0.8200000000000001, 1.0], [1.0, 0.8200000000000001]]), ('truncatedv15v3', [[0.8200000000000001, 1.0], [0.18, 1.0]]), ('truncatedv3v5', [[0.18, 1.0], [0.0, 0.8200000000000001]]), ('truncatedv21v9', [[1.32, 1.5], [0.6799999999999999, 1.5]]), ('truncatedv12v13', [[0.8200000000000001, 0.0], [1.09, 0.09]]), ('truncatedv3v4', [[0.18, 1.0], [0.09, 1.09]]), ('truncatedv15v16', [[0.8200000000000001, 1.0], [1.09, 1.09]]), ('truncatedv21v22', [[1.32, 1.5], [1.4100000000000001, 1.4100000000000001]]), ('truncatedv10v9', [[0.41000000000000003, 1.4100000000000001], [0.6799999999999999, 1.5]])]:
                c.line(points, id=object_id, zorder=3, clip_on=False)
            for object_id, points in [('phantom0000', [[0.0, 0.0], [0.18, 0.0]]), ('phantom0002', [[0.0, 0.0], [0.0, 0.18]]), ('phantom0010', [[0.0, 1.0], [0.18, 1.0]]), ('phantom0011', [[0.0, 1.0], [0.09, 1.09]]), ('phantom0012', [[0.0, 1.0], [0.0, 0.8200000000000001]]), ('phantom0110', [[0.5, 1.5], [0.6799999999999999, 1.5]]), ('phantom0111', [[0.5, 1.5], [0.41000000000000003, 1.4100000000000001]]), ('phantom1000', [[1.0, 0.0], [0.8200000000000001, 0.0]]), ('phantom1001', [[1.0, 0.0], [1.09, 0.09]]), ('phantom1002', [[1.0, 0.0], [1.0, 0.18]]), ('phantom1010', [[1.0, 1.0], [0.8200000000000001, 1.0]]), ('phantom1011', [[1.0, 1.0], [1.09, 1.09]]), ('phantom1012', [[1.0, 1.0], [1.0, 0.8200000000000001]]), ('phantom1101', [[1.5, 0.5], [1.4100000000000001, 0.41000000000000003]]), ('phantom1102', [[1.5, 0.5], [1.5, 0.6799999999999999]]), ('phantom1110', [[1.5, 1.5], [1.32, 1.5]]), ('phantom1111', [[1.5, 1.5], [1.4100000000000001, 1.4100000000000001]]), ('phantom1112', [[1.5, 1.5], [1.5, 1.32]])]:
                c.line(points, id=object_id, zorder=3, clip_on=False, linestyle=(0.0, [4.0, 3.0]))
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Solid171().draw(sys.argv[1] if len(sys.argv) > 1 else None))
