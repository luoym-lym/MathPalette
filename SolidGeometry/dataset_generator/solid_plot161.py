"""Frozen question Solid161; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Solid161:

    def __init__(self):
        self.id = 'Solid161'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:1352'
        self.question = 'A glass cube has side length $1 \\mathrm{dm}$. Equally sized black squares are attached as shown on the right so that all faces look the same. How many $\\mathrm{cm}^{2}$ are covered?'
        self.answer = '225'
        self.answer_type = 'number'
        self.query = self.question
        self.subject = 'SolidGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'SolidGeometry' / 'dataset_generator/scenes/Solid161.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('SolidGeometry', self.id, variant, output_path)
        with Canvas(SOLID, xlim=[-0.19607454330049812, 1.7488755365175526], ylim=[-0.3488755365175521, 1.5960745433004986], axes_position=[0.05, 0.05, 0.9, 0.9], coordinate_axes=False) as c:
            for object_id, points in [('cube000_cube100', [[0.0, 0.0], [1.0, -0.3]]), ('cube000_cube001', [[0.0, 0.0], [0.0, 1.0]]), ('cube001_cube101', [[0.0, 1.0], [1.0, 0.7]]), ('cube001_cube011', [[0.0, 1.0], [0.55, 1.55]]), ('cube011_cube111', [[0.55, 1.55], [1.55, 1.25]]), ('cube100_cube110', [[1.0, -0.3], [1.55, 0.25000000000000006]]), ('cube100_cube101', [[1.0, -0.3], [1.0, 0.7]]), ('cube101_cube111', [[1.0, 0.7], [1.55, 1.25]]), ('cube110_cube111', [[1.55, 0.25000000000000006], [1.55, 1.25]])]:
                c.line(points, id=object_id, zorder=3, clip_on=False)
            for object_id, vertices, codes in [('frontsticker0', [[0.5, 0.1], [0.75, 0.275], [0.5, 0.6], [0.25, 0.425], [0.5, 0.1]], [1, 2, 2, 2, 79]), ('frontsticker1', [[0.25, -0.075], [0.75, -0.22499999999999998], [0.5, 0.1], [0.25, -0.075]], [1, 2, 2, 79]), ('frontsticker2', [[1.0, -0.04999999999999999], [1.0, 0.45], [0.75, 0.275], [1.0, -0.04999999999999999]], [1, 2, 2, 79]), ('frontsticker3', [[0.75, 0.775], [0.25, 0.925], [0.5, 0.6], [0.75, 0.775]], [1, 2, 2, 79]), ('frontsticker4', [[0.0, 0.75], [0.0, 0.25], [0.25, 0.425], [0.0, 0.75]], [1, 2, 2, 79]), ('rightsticker0', [[1.275, 0.22500000000000003], [1.4125, 0.6125], [1.275, 0.7250000000000001], [1.1375, 0.3375], [1.275, 0.22500000000000003]], [1, 2, 2, 2, 79]), ('rightsticker1', [[1.1375, -0.16249999999999998], [1.4125, 0.11250000000000004], [1.275, 0.22500000000000003], [1.1375, -0.16249999999999998]], [1, 2, 2, 79]), ('rightsticker2', [[1.55, 0.5], [1.55, 1.0], [1.4125, 0.6125], [1.55, 0.5]], [1, 2, 2, 79]), ('rightsticker3', [[1.4125, 1.1125], [1.1375, 0.8375], [1.275, 0.7250000000000001], [1.4125, 1.1125]], [1, 2, 2, 79]), ('rightsticker4', [[1.0, 0.45], [1.0, -0.04999999999999999], [1.1375, 0.3375], [1.0, 0.45]], [1, 2, 2, 79]), ('topsticker0', [[0.6375, 0.9875], [1.025, 1.05], [0.9125000000000001, 1.2625000000000002], [0.525, 1.2], [0.6375, 0.9875]], [1, 2, 2, 2, 79]), ('topsticker1', [[0.25, 0.925], [0.75, 0.775], [0.6375, 0.9875], [0.25, 0.925]], [1, 2, 2, 79]), ('topsticker2', [[1.1375, 0.8375], [1.4125, 1.1125], [1.025, 1.05], [1.1375, 0.8375]], [1, 2, 2, 79]), ('topsticker3', [[1.3, 1.3250000000000002], [0.8, 1.475], [0.9125000000000001, 1.2625000000000002], [1.3, 1.3250000000000002]], [1, 2, 2, 79]), ('topsticker4', [[0.41250000000000003, 1.4125], [0.1375, 1.1375], [0.525, 1.2], [0.41250000000000003, 1.4125]], [1, 2, 2, 79])]:
                c.path(vertices, codes, id=object_id, zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.0, 0.0, 0.0, 1.0], linewidth=0.0, capstyle='butt')
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Solid161().draw(sys.argv[1] if len(sys.argv) > 1 else None))
