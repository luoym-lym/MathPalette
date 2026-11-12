"""Frozen question Solid197; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Solid197:

    def __init__(self):
        self.id = 'Solid197'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:1877'
        self.question = 'A cube has sides of length $10 \\mathrm{~cm}$. Identical square stickers are placed: one sticker in the centre of each face of the cube, and one across each edge, so that the stickers meet at their corners, as shown in the diagram. What is the total area in $\\mathrm{cm}^{2}$ of the stickers used?'
        self.answer = '225'
        self.answer_type = 'number'
        self.query = self.question
        self.subject = 'SolidGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'SolidGeometry' / 'dataset_generator/scenes/Solid197.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('SolidGeometry', self.id, variant, output_path)
        with Canvas(SOLID, xlim=[-0.03362196403009343, 1.3856659320533493], ylim=[-0.035665932053349225, 1.3836219640300935], axes_position=[0.05, 0.05, 0.9, 0.9], coordinate_axes=False) as c:
            for object_id, points in [('cube000_cube100', [[0.0, 0.0], [1.0, 0.0]]), ('cube000_cube001', [[0.0, 0.0], [0.0, 1.0]]), ('cube001_cube101', [[0.0, 1.0], [1.0, 1.0]]), ('cube001_cube011', [[0.0, 1.0], [0.35, 1.35]]), ('cube011_cube111', [[0.35, 1.35], [1.35, 1.35]]), ('cube100_cube110', [[1.0, 0.0], [1.35, 0.35]]), ('cube100_cube101', [[1.0, 0.0], [1.0, 1.0]]), ('cube101_cube111', [[1.0, 1.0], [1.35, 1.35]]), ('cube110_cube111', [[1.35, 0.35], [1.35, 1.35]])]:
                c.line(points, id=object_id, zorder=3, clip_on=False)
            for object_id, vertices, codes in [('frontsticker0', [[0.5, 0.25], [0.75, 0.5], [0.5, 0.75], [0.25, 0.5], [0.5, 0.25]], [1, 2, 2, 2, 79]), ('frontsticker1', [[0.25, 0.0], [0.75, 0.0], [0.5, 0.25], [0.25, 0.0]], [1, 2, 2, 79]), ('frontsticker2', [[1.0, 0.25], [1.0, 0.75], [0.75, 0.5], [1.0, 0.25]], [1, 2, 2, 79]), ('frontsticker3', [[0.75, 1.0], [0.25, 1.0], [0.5, 0.75], [0.75, 1.0]], [1, 2, 2, 79]), ('frontsticker4', [[0.0, 0.75], [0.0, 0.25], [0.25, 0.5], [0.0, 0.75]], [1, 2, 2, 79]), ('rightsticker0', [[1.175, 0.425], [1.2625, 0.7625], [1.175, 0.925], [1.0875, 0.5875], [1.175, 0.425]], [1, 2, 2, 2, 79]), ('rightsticker1', [[1.0875, 0.0875], [1.2625, 0.26249999999999996], [1.175, 0.425], [1.0875, 0.0875]], [1, 2, 2, 79]), ('rightsticker2', [[1.35, 0.6], [1.35, 1.1], [1.2625, 0.7625], [1.35, 0.6]], [1, 2, 2, 79]), ('rightsticker3', [[1.2625, 1.2625], [1.0875, 1.0875], [1.175, 0.925], [1.2625, 1.2625]], [1, 2, 2, 79]), ('rightsticker4', [[1.0, 0.75], [1.0, 0.25], [1.0875, 0.5875], [1.0, 0.75]], [1, 2, 2, 79]), ('topsticker0', [[0.5875, 1.0875], [0.925, 1.175], [0.7625, 1.2625], [0.425, 1.175], [0.5875, 1.0875]], [1, 2, 2, 2, 79]), ('topsticker1', [[0.25, 1.0], [0.75, 1.0], [0.5875, 1.0875], [0.25, 1.0]], [1, 2, 2, 79]), ('topsticker2', [[1.0875, 1.0875], [1.2625, 1.2625], [0.925, 1.175], [1.0875, 1.0875]], [1, 2, 2, 79]), ('topsticker3', [[1.1, 1.35], [0.6, 1.35], [0.7625, 1.2625], [1.1, 1.35]], [1, 2, 2, 79]), ('topsticker4', [[0.26249999999999996, 1.2625], [0.0875, 1.0875], [0.425, 1.175], [0.26249999999999996, 1.2625]], [1, 2, 2, 79])]:
                c.path(vertices, codes, id=object_id, zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 1.0], linewidth=0.0, capstyle='butt')
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Solid197().draw(sys.argv[1] if len(sys.argv) > 1 else None))
