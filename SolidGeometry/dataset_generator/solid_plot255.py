"""Frozen question Solid255; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Solid255:

    def __init__(self):
        self.id = 'Solid255'
        self.source_dataset = 'Author Designed'
        self.source_key = 'author-promote15:Solid262'
        self.question = 'The diagram is a net of a regular octahedron. Face Q has a boundary edge marked x. After folding, which numbered face shares the entire edge x with face Q? Give its number.'
        self.answer = '3'
        self.answer_type = 'number'
        self.query = self.question
        self.subject = 'SolidGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'SolidGeometry' / 'dataset_generator/scenes/Solid255.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('SolidGeometry', self.id, variant, output_path)
        with Canvas(SOLID, xlim=[-1.525, 2.525], ylim=[-2.458012701892219, 1.5919872981077807], axes_position=[0.05, 0.05, 0.9, 0.9], coordinate_axes=False) as c:
            for object_id, points in [('edge00', [[-1.0, 0.0], [-0.5, 0.8660254037844386]]), ('edge01', [[-1.0, 0.0], [0.0, 0.0]]), ('edge02', [[-0.5, 0.8660254037844386], [0.0, 0.0]]), ('edge03', [[-0.5, 0.8660254037844386], [0.5, 0.8660254037844386]]), ('edge04', [[0.0, 0.0], [0.5, 0.8660254037844386]]), ('edge05', [[0.0, 0.0], [0.5, -0.8660254037844386]]), ('edge06', [[0.0, 0.0], [1.0, 0.0]]), ('edge07', [[0.5, 0.8660254037844386], [1.0, 0.0]]), ('edge08', [[0.5, 0.8660254037844386], [1.5, 0.8660254037844386]]), ('edge09', [[0.5, -0.8660254037844386], [1.0, 0.0]]), ('edge10', [[0.5, -0.8660254037844386], [1.0, -1.7320508075688772]])]:
                c.line(points, id=object_id, zorder=1)
            c.text('x', [0.5854551732809566, -1.394038105676658], zorder=2, rotation_mode='default')
            for object_id, points in [('edge11', [[0.5, -0.8660254037844386], [1.5, -0.8660254037844386]]), ('edge12', [[1.0, 0.0], [1.5, 0.8660254037844386]]), ('edge13', [[1.0, 0.0], [1.5, -0.8660254037844386]]), ('edge14', [[1.0, -1.7320508075688772], [1.5, -0.8660254037844386]]), ('edge15', [[1.0, -1.7320508075688772], [2.0, -1.7320508075688772]]), ('edge16', [[1.5, -0.8660254037844386], [2.0, -1.7320508075688772]])]:
                c.line(points, id=object_id, zorder=1)
            for object_id, text, anchor in [(None, '1', [0.5, 0.28867513459481287]), (None, '6', [0.5, -0.28867513459481287]), (None, '7', [1.0, 0.5773502691896257]), (None, '5', [1.0, -0.5773502691896257]), (None, 'Q', [1.0, -1.1547005383792515]), (None, '4', [1.5, -1.4433756729740643]), (None, '2', [0.0, 0.5773502691896257]), (None, '3', [-0.5, 0.28867513459481287])]:
                c.text(text, anchor, id=object_id, zorder=3, rotation_mode='default')
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Solid255().draw(sys.argv[1] if len(sys.argv) > 1 else None))
