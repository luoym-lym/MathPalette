"""Frozen question Solid254; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Solid254:

    def __init__(self):
        self.id = 'Solid254'
        self.source_dataset = 'Author Designed'
        self.source_key = 'author-promote15:Solid261'
        self.question = 'The diagram is a net of a regular octahedron. When the net is folded, which labelled edge A, B, C, D, or E coincides with edge x? Give the letter.\nChoices:\nA: A\nB: B\nC: C\nD: D\nE: E'
        self.answer = 'B'
        self.answer_type = 'choice'
        self.choices = {'A': 'A', 'B': 'B', 'C': 'C', 'D': 'D', 'E': 'E'}
        self.query = self.question
        self.subject = 'SolidGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'SolidGeometry' / 'dataset_generator/scenes/Solid254.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('SolidGeometry', self.id, variant, output_path)
        with Canvas(SOLID, xlim=[-2.025, 2.525], ylim=[-1.8419872981077807, 2.708012701892219], axes_position=[0.05, 0.05, 0.9, 0.9], coordinate_axes=False) as c:
            c.line([[-1.5, 0.8660254037844386], [-1.0, 0.0]], id='edge00', zorder=1)
            c.text('x', [-1.4145448267190432, 0.3380127018922193], zorder=2, rotation_mode='default')
            for object_id, points in [('edge01', [[-1.5, 0.8660254037844386], [-0.5, 0.8660254037844386]]), ('edge02', [[-1.0, 0.0], [-0.5, 0.8660254037844386]]), ('edge03', [[-1.0, 0.0], [0.0, 0.0]])]:
                c.line(points, id=object_id, zorder=1)
            c.text('C', [-0.5, -0.19], zorder=2, rotation_mode='default')
            for object_id, points in [('edge04', [[-0.5, 0.8660254037844386], [0.0, 1.7320508075688772]]), ('edge05', [[-0.5, 0.8660254037844386], [0.0, 0.0]]), ('edge06', [[-0.5, 0.8660254037844386], [0.5, 0.8660254037844386]]), ('edge07', [[0.0, 1.7320508075688772], [0.5, 0.8660254037844386]]), ('edge08', [[0.0, 0.0], [0.5, 0.8660254037844386]]), ('edge09', [[0.0, 0.0], [0.5, -0.8660254037844386]]), ('edge10', [[0.0, 0.0], [1.0, 0.0]]), ('edge11', [[0.5, 0.8660254037844386], [1.0, 0.0]]), ('edge12', [[0.5, 0.8660254037844386], [1.5, 0.8660254037844386]])]:
                c.line(points, id=object_id, zorder=1)
            c.text('E', [1.0, 1.0560254037844385], zorder=2, rotation_mode='default')
            c.line([[0.5, -0.8660254037844386], [1.0, 0.0]], id='edge13', zorder=1)
            c.text('D', [0.9145448267190434, -0.5280127018922193], zorder=2, rotation_mode='default')
            c.line([[1.0, 0.0], [1.5, 0.8660254037844386]], id='edge14', zorder=1)
            c.line([[1.0, 0.0], [2.0, 0.0]], id='edge15', zorder=1)
            c.text('A', [1.5, -0.19], zorder=2, rotation_mode='default')
            c.line([[1.5, 0.8660254037844386], [2.0, 0.0]], id='edge16', zorder=1)
            c.text('B', [1.9145448267190432, 0.5280127018922193], zorder=2, rotation_mode='default')
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Solid254().draw(sys.argv[1] if len(sys.argv) > 1 else None))
