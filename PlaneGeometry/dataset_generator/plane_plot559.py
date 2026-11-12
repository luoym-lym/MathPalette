"""Frozen question Plane559; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane559:

    def __init__(self):
        self.id = 'Plane559'
        self.source_dataset = 'Author Designed'
        self.source_key = 'author-extensions95-v1:Plane236/extension_05'
        self.question = 'If a laser beam hits a mirror it changes its direction as shown. Each solid mirror has mirrored sides on both sides; dashed lines do not reflect. At which letter does the laser beam end?\nChoices:\nA:A\nB:B\nC:C\nD:D\nE:E'
        self.answer = 'C'
        self.answer_type = 'choice'
        self.choices = {'A': 'A', 'B': 'B', 'C': 'C', 'D': 'D', 'E': 'E'}
        self.query = self.question
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane559.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=(-0.35347746567176186, 5.3722853360421325), ylim=(-1.0912138678170027, 4.634548933896891), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
            for object_id, points in [('boundary_1', [[0.0, 0.0], [5.0, 0.0]]), ('boundary_2', [[5.0, 0.0], [5.0, 4.0]]), ('boundary_3', [[5.0, 4.0], [0.0, 4.0]]), ('boundary_4', [[0.0, 4.0], [0.0, 0.0]])]:
                c.line(points, id=object_id, zorder=3, simplify=False)
            for object_id, points in [('grid_column_1', [[1.0, 0.0], [1.0, 4.0]]), ('grid_column_2', [[2.0, 0.0], [2.0, 4.0]]), ('grid_column_3', [[3.0, 0.0], [3.0, 4.0]]), ('grid_column_4', [[4.0, 0.0], [4.0, 4.0]]), ('grid_row_1', [[0.0, 1.0], [5.0, 1.0]]), ('grid_row_2', [[0.0, 2.0], [5.0, 2.0]]), ('grid_row_3', [[0.0, 3.0], [5.0, 3.0]])]:
                c.line(points, id=object_id, zorder=1, color='#999999', linestyle=(0.0, [4.0, 3.0]), simplify=False)
            for object_id, points in [('mirror_c1_r2', [[0.66, 2.34], [1.34, 1.66]]), ('mirror_c1_r3', [[0.66, 2.66], [1.34, 3.34]]), ('mirror_c2_r2', [[1.66, 2.34], [2.34, 1.66]]), ('mirror_c2_r3', [[1.66, 3.34], [2.34, 2.66]]), ('mirror_c3_r1', [[2.66, 1.34], [3.34, 0.66]]), ('mirror_c3_r2', [[2.66, 2.34], [3.34, 1.66]]), ('mirror_c3_r3', [[2.66, 2.66], [3.34, 3.34]]), ('mirror_c4_r1', [[3.66, 1.34], [4.34, 0.66]]), ('mirror_c4_r2', [[3.66, 2.34], [4.34, 1.66]]), ('mirror_c4_r3', [[3.66, 3.34], [4.34, 2.66]])]:
                c.line(points, id=object_id, zorder=3, simplify=False)
            c.path([[322.50601008225385, 83.21202493374497], [322.50601008225385, 158.05689972871966], [322.50601008225385, 231.3489495393195]], [1, 3, 3], coordinates='pixels', id='incident_arrow', zorder=4, joinstyle='round', simplify=False)
            c.path([[319.17267674892054, 224.68228287265285], [322.50601008225385, 231.3489495393195], [325.83934341558717, 224.68228287265285], [0.0, 0.0]], [1, 2, 2, 79], coordinates='pixels', id='incident_arrow', zorder=4, facecolor=(0.0, 0.0, 0.0, 1.0), joinstyle='round', simplify=False)
            c.text('A', (2, 4), id='exit_label_A', fontsize=18.0, rotation_mode='default', offset_pt=(0, 15), annotation_clip=None)
            c.text('B', (0, 2), id='exit_label_B', fontsize=18.0, rotation_mode='default', offset_pt=(-15, 0), annotation_clip=None)
            c.text('C', (4, 0), id='exit_label_C', fontsize=18.0, rotation_mode='default', offset_pt=(0, -15), annotation_clip=None)
            c.text('D', (5, 1), id='exit_label_D', fontsize=18.0, rotation_mode='default', offset_pt=(15, 0), annotation_clip=None)
            c.text('E', (3, 4), id='exit_label_E', fontsize=18.0, rotation_mode='default', offset_pt=(0, 15), annotation_clip=None)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane559().draw(sys.argv[1] if len(sys.argv) > 1 else None))
