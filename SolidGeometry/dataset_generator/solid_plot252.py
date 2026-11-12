"""Frozen question Solid252; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Solid252:

    def __init__(self):
        self.id = 'Solid252'
        self.source_dataset = 'Author Designed'
        self.source_key = 'author-promote15:Solid259'
        self.question = 'The diagram is a net of a regular octahedron. When the net is folded, which labelled edge A, B, C, D, or E coincides with edge x? Give the letter.\nChoices:\nA: A\nB: B\nC: C\nD: D\nE: E'
        self.answer = 'B'
        self.answer_type = 'choice'
        self.choices = {'A': 'A', 'B': 'B', 'C': 'C', 'D': 'D', 'E': 'E'}
        self.query = self.question
        self.subject = 'SolidGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'SolidGeometry' / 'dataset_generator/scenes/Solid252.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('SolidGeometry', self.id, variant, output_path)
        with Canvas(SOLID, xlim=[-1.574038105676658, 2.074038105676658], ylim=[-1.3910254037844387, 2.257050807568877], axes_position=[0.05, 0.05, 0.9, 0.9], coordinate_axes=False) as c:
            c.line([[-1.0, 1.7320508075688772], [-0.5, 0.8660254037844386]], id='edge00', zorder=1)
            c.text('C', [-0.9145448267190434, 1.204038105676658], zorder=2, rotation_mode='default')
            c.line([[-1.0, 1.7320508075688772], [0.0, 1.7320508075688772]], id='edge01', zorder=1)
            c.text('x', [-0.5, 1.9220508075688771], zorder=2, rotation_mode='default')
            c.line([[-0.5, 0.8660254037844386], [0.0, 1.7320508075688772]], id='edge02', zorder=1)
            c.line([[-0.5, 0.8660254037844386], [0.0, 0.0]], id='edge03', zorder=1)
            c.text('E', [-0.41454482671904336, 0.3380127018922193], zorder=2, rotation_mode='default')
            for object_id, points in [('edge04', [[-0.5, 0.8660254037844386], [0.5, 0.8660254037844386]]), ('edge05', [[0.0, 1.7320508075688772], [0.5, 0.8660254037844386]]), ('edge06', [[0.0, 1.7320508075688772], [1.0, 1.7320508075688772]]), ('edge07', [[-0.5, -0.8660254037844386], [0.0, 0.0]])]:
                c.line(points, id=object_id, zorder=1)
            c.text('D', [-0.41454482671904336, -0.3380127018922193], zorder=2, rotation_mode='default')
            c.line([[-0.5, -0.8660254037844386], [0.5, -0.8660254037844386]], id='edge08', zorder=1)
            c.text('A', [0.0, -1.0560254037844385], zorder=2, rotation_mode='default')
            for object_id, points in [('edge09', [[0.0, 0.0], [0.5, 0.8660254037844386]]), ('edge10', [[0.0, 0.0], [0.5, -0.8660254037844386]]), ('edge11', [[0.0, 0.0], [1.0, 0.0]]), ('edge12', [[0.5, 0.8660254037844386], [1.0, 1.7320508075688772]]), ('edge13', [[0.5, 0.8660254037844386], [1.0, 0.0]]), ('edge14', [[0.5, -0.8660254037844386], [1.0, 0.0]]), ('edge15', [[0.5, -0.8660254037844386], [1.5, -0.8660254037844386]])]:
                c.line(points, id=object_id, zorder=1)
            c.text('B', [1.0, -1.0560254037844385], zorder=2, rotation_mode='default')
            c.line([[1.0, 0.0], [1.5, -0.8660254037844386]], id='edge16', zorder=1)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Solid252().draw(sys.argv[1] if len(sys.argv) > 1 else None))
