"""Frozen question Solid100; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Solid100:

    def __init__(self):
        self.id = 'Solid100'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:309'
        self.question = 'Four identical rhombuses (diamonds) and two squares are fitted together to form a regular octagon as shown. How big are the obtuse interior angles in the rhombuses?\nChoices:\nA:$135^{\\circ}$\nB:$140^{\\circ}$\nC:$144^{\\circ}$\nD:$145^{\\circ}$\nE:$150^{\\circ}$'
        self.answer = 'A'
        self.answer_type = 'choice'
        self.choices = {'A': '$135^{\\circ}$', 'B': '$140^{\\circ}$', 'C': '$144^{\\circ}$', 'D': '$145^{\\circ}$', 'E': '$150^{\\circ}$'}
        self.query = self.question
        self.subject = 'SolidGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'SolidGeometry' / 'dataset_generator/scenes/Solid100.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('SolidGeometry', self.id, variant, output_path)
        with Canvas(SOLID, xlim=[-1.0513339633469772, 1.0513339633469772], ylim=[-1.0513339633469772, 1.0513339633469772], axes_position=[0.05, 0.05, 0.9, 0.9], coordinate_axes=False) as c:
            for object_id, points in [('boundary0', [[0.0, 1.0], [0.7071067811865475, 0.7071067811865476]]), ('boundary1', [[0.7071067811865475, 0.7071067811865476], [1.0, 6.123233995736766e-17]]), ('boundary2', [[1.0, 6.123233995736766e-17], [0.7071067811865476, -0.7071067811865475]]), ('boundary3', [[0.7071067811865476, -0.7071067811865475], [1.2246467991473532e-16, -1.0]]), ('boundary4', [[1.2246467991473532e-16, -1.0], [-0.7071067811865475, -0.7071067811865477]]), ('boundary5', [[-0.7071067811865475, -0.7071067811865477], [-1.0, -1.8369701987210297e-16]]), ('boundary6', [[-1.0, -1.8369701987210297e-16], [-0.7071067811865477, 0.7071067811865474]]), ('boundary7', [[-0.7071067811865477, 0.7071067811865474], [0.0, 1.0]]), ('seam0', [[-0.7071067811865477, 0.7071067811865474], [0.0, 0.41421356237309515]]), ('seam1', [[0.0, 0.41421356237309515], [0.7071067811865475, 0.7071067811865476]]), ('seam2', [[-1.0, -1.8369701987210297e-16], [-0.2928932188134524, -0.2928932188134524]]), ('seam3', [[-0.2928932188134524, -0.2928932188134524], [0.0, 0.41421356237309515]]), ('seam4', [[0.0, 0.41421356237309515], [0.2928932188134524, -0.2928932188134524]]), ('seam5', [[0.2928932188134524, -0.2928932188134524], [1.0, 6.123233995736766e-17]]), ('seam6', [[-0.2928932188134524, -0.2928932188134524], [1.2246467991473532e-16, -1.0]]), ('seam7', [[0.2928932188134524, -0.2928932188134524], [1.2246467991473532e-16, -1.0]])]:
                c.line(points, id=object_id, zorder=3, clip_on=False)
            for object_id, vertices, codes in [('rhombus0', [[-0.7071067811865477, 0.7071067811865474], [0.0, 1.0], [0.7071067811865475, 0.7071067811865476], [0.0, 0.41421356237309515], [-0.7071067811865477, 0.7071067811865474]], [1, 2, 2, 2, 79]), ('rhombus1', [[0.0, 0.41421356237309515], [-0.2928932188134524, -0.2928932188134524], [1.2246467991473532e-16, -1.0], [0.2928932188134524, -0.2928932188134524], [0.0, 0.41421356237309515]], [1, 2, 2, 2, 79]), ('rhombus2', [[-1.0, -1.8369701987210297e-16], [-0.7071067811865475, -0.7071067811865477], [1.2246467991473532e-16, -1.0], [-0.2928932188134524, -0.2928932188134524], [-1.0, -1.8369701987210297e-16]], [1, 2, 2, 2, 79]), ('rhombus3', [[1.0, 6.123233995736766e-17], [0.7071067811865476, -0.7071067811865475], [1.2246467991473532e-16, -1.0], [0.2928932188134524, -0.2928932188134524], [1.0, 6.123233995736766e-17]], [1, 2, 2, 2, 79])]:
                c.path(vertices, codes, id=object_id, zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 1.0], linewidth=0.0, capstyle='butt')
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Solid100().draw(sys.argv[1] if len(sys.argv) > 1 else None))
