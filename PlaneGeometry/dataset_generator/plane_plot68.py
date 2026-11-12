"""Frozen question Plane68; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane68:

    def __init__(self):
        self.id = 'Plane68'
        self.source_dataset = 'MathVista'
        self.source_key = 'testmini/897'
        self.question = 'Use a calculator to find the measure of $∠J$ to the nearest degree.\nChoices:\nA: 33\nB: 40\nC: 50\nD: 57'
        self.answer = 'B'
        self.answer_type = 'choice'
        self.choices = {'A': '33', 'B': '40', 'C': '50', 'D': '57'}
        self.query = self.question
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane68.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-10.238821666609615, 5.4786617619861495], ylim=[-11.619270132277995, 4.09821329631777], axes_position=[0.05, 0.05, 0.9, 0.9], coordinate_axes=False) as c:
            for object_id, points in [('segment4', [[-9.287087810503355, -5.361902647381805], [0.0, 0.0]]), ('segment5', [[0.0, 0.0], [4.500000000000001, -7.794228634059947]]), ('segment6', [[4.500000000000001, -7.794228634059947], [-9.287087810503355, -5.361902647381805]])]:
                c.line(points, id=object_id)
            c.line([[-0.24616138477873392, -0.1421213417660931], [-0.10404004301264083, -0.388282726544827]], id='right_angle7', zorder=3)
            c.line([[-0.10404004301264083, -0.388282726544827], [0.1421213417660931, -0.2461613847787339]], id='right_angle7', zorder=3)
            c.text('L', [0.0, 0.0], id='label1', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[0, 15], annotation_clip=None)
            c.text('J', [-9.287087810503355, -5.361902647381805], id='label2', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[-14, -4], annotation_clip=None)
            c.text('K', [4.500000000000001, -7.794228634059947], id='label3', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[12, -10], annotation_clip=None)
            c.text('9', [2.2500000000000004, -3.8971143170299736], id='text10', rotation_mode='default', offset_pt=[18, 0], annotation_clip=None)
            c.text('14', [-2.393543905251677, -6.578065640720876], id='text12', rotation_mode='default', offset_pt=[0, -15], annotation_clip=None)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane68().draw(sys.argv[1] if len(sys.argv) > 1 else None))
