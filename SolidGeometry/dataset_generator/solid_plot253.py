"""Frozen question Solid253; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Solid253:

    def __init__(self):
        self.id = 'Solid253'
        self.source_dataset = 'Author Designed'
        self.source_key = 'author-promote15:Solid260'
        self.question = 'The diagram is a net of a regular octahedron. When the net is folded, which labelled edge A, B, C, D, or E coincides with edge x? Give the letter.\nChoices:\nA: A\nB: B\nC: C\nD: D\nE: E'
        self.answer = 'C'
        self.answer_type = 'choice'
        self.choices = {'A': 'A', 'B': 'B', 'C': 'C', 'D': 'D', 'E': 'E'}
        self.query = self.question
        self.subject = 'SolidGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'SolidGeometry' / 'dataset_generator/scenes/Solid253.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('SolidGeometry', self.id, variant, output_path)
        with Canvas(SOLID, xlim=[-2.007050807568877, 2.507050807568877], ylim=[-2.257050807568877, 2.257050807568877], axes_position=[0.05, 0.05, 0.9, 0.9], coordinate_axes=False) as c:
            c.line([[-1.0, 0.0], [-0.5, 0.8660254037844386]], id='edge00', zorder=1)
            c.text('D', [-0.9145448267190434, 0.5280127018922193], zorder=2, rotation_mode='default')
            c.line([[-1.0, 0.0], [0.0, 0.0]], id='edge01', zorder=1)
            c.text('C', [-0.5, -0.19], zorder=2, rotation_mode='default')
            for object_id, points in [('edge02', [[-0.5, 0.8660254037844386], [0.0, 0.0]]), ('edge03', [[-0.5, 0.8660254037844386], [0.5, 0.8660254037844386]]), ('edge04', [[0.0, 0.0], [0.5, 0.8660254037844386]]), ('edge05', [[0.0, 0.0], [0.5, -0.8660254037844386]])]:
                c.line(points, id=object_id, zorder=1)
            c.text('x', [0.08545517328095664, -0.5280127018922193], zorder=2, rotation_mode='default')
            for object_id, points in [('edge06', [[0.0, 0.0], [1.0, 0.0]]), ('edge07', [[0.5, 0.8660254037844386], [1.0, 1.7320508075688772]]), ('edge08', [[0.5, 0.8660254037844386], [1.0, 0.0]]), ('edge09', [[0.5, 0.8660254037844386], [1.5, 0.8660254037844386]]), ('edge10', [[1.0, 1.7320508075688772], [1.5, 0.8660254037844386]])]:
                c.line(points, id=object_id, zorder=1)
            c.text('E', [1.4145448267190432, 1.394038105676658], zorder=2, rotation_mode='default')
            for object_id, points in [('edge11', [[0.5, -0.8660254037844386], [1.0, 0.0]]), ('edge12', [[0.5, -0.8660254037844386], [1.0, -1.7320508075688772]]), ('edge13', [[0.5, -0.8660254037844386], [1.5, -0.8660254037844386]]), ('edge14', [[1.0, 0.0], [1.5, 0.8660254037844386]])]:
                c.line(points, id=object_id, zorder=1)
            c.text('B', [1.4145448267190432, 0.3380127018922193], zorder=2, rotation_mode='default')
            c.line([[1.0, 0.0], [1.5, -0.8660254037844386]], id='edge15', zorder=1)
            c.line([[1.0, -1.7320508075688772], [1.5, -0.8660254037844386]], id='edge16', zorder=1)
            c.text('A', [1.4145448267190432, -1.394038105676658], zorder=2, rotation_mode='default')
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Solid253().draw(sys.argv[1] if len(sys.argv) > 1 else None))
