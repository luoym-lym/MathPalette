"""Frozen question Plane55; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane55:

    def __init__(self):
        self.id = 'Plane55'
        self.source_dataset = 'MathVista'
        self.source_key = 'testmini/716'
        self.question = 'Find y.\nChoices:\nA: 16 \\sqrt { 2 }\nB: 16 \\sqrt { 3 }\nC: 32\nD: 16 \\sqrt { 5 }'
        self.answer = 'D'
        self.answer_type = 'choice'
        self.choices = {'A': '16 \\sqrt { 2 }', 'B': '16 \\sqrt { 3 }', 'C': '32', 'D': '16 \\sqrt { 5 }'}
        self.query = self.question
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane55.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-8.998508088198012, 33.07663308819801], ylim=[-26.78282120138842, 15.292319975007604], axes_position=[0.050000000000000114, 0.05, 0.8999999999999998, 0.9], coordinate_axes=False) as c:
            for object_id, points in [('segment1', [[-8.0, 0.0], [32.0, 0.0]]), ('segment2', [[32.0, 0.0], [0.0, -16.0]]), ('segment3', [[0.0, -16.0], [-8.0, 0.0]]), ('segment4', [[0.0, -16.0], [0.0, 0.0]])]:
                c.line(points, id=object_id)
            for object_id, points in [('right_angle5', [[-0.3402881793739945, -15.31942364125201], [0.3402881793739945, -14.979135461878016]]), ('right_angle5', [[0.3402881793739945, -14.979135461878016], [0.680576358747989, -15.659711820626006]]), ('right_angle7', [[0.0, -0.7609075010198936], [0.7609075010198936, -0.7609075010198936]]), ('right_angle7', [[0.7609075010198936, -0.7609075010198936], [0.7609075010198936, 0.0]])]:
                c.line(points, id=object_id, zorder=3)
            c.line([[-8.0, 3.0], [0.0, 3.0]], id='segment14', linestyle=(0, [4, 3]))
            c.line([[-8.0, 0.0], [-8.0, 3.0]], id='segment15')
            c.line([[0.0, 0.0], [0.0, 3.0]], id='segment16')
            c.line([[0.0, 3.0], [32.0, 3.0]], id='segment24', linestyle=(0, [4, 3]))
            c.line([[0.0, 0.0], [0.0, 3.0]], id='segment25')
            c.line([[32.0, 0.0], [32.0, 3.0]], id='segment26')
            c.text('8', [-4.0, 3.0], id='text18', rotation_mode='default', offset_pt=[-0.0, 12.0], annotation_clip=None)
            c.text('x', [16.0, 3.0], id='text28', rotation_mode='default', offset_pt=[-0.0, 12.0], annotation_clip=None)
            c.text('z', [-4.0, -8.0], id='text33', rotation_mode='default', offset_pt=[-15, 0], annotation_clip=None)
            c.text('16', [0.0, -8.0], id='text35', rotation_mode='default', offset_pt=[15, 0], annotation_clip=None)
            c.text('y', [16.0, -8.0], id='text37', rotation_mode='default', offset_pt=[8, -16], annotation_clip=None)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane55().draw(sys.argv[1] if len(sys.argv) > 1 else None))
