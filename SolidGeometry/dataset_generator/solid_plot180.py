"""Frozen question Solid180; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Solid180:

    def __init__(self):
        self.id = 'Solid180'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:1657'
        self.question = 'The diagram shows a net of an unfolded rectangular box. What is the volume of the box (in $\\mathrm{cm}^{3}$ )?'
        self.answer = '80'
        self.answer_type = 'number'
        self.query = self.question
        self.subject = 'SolidGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'SolidGeometry' / 'dataset_generator/scenes/Solid180.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('SolidGeometry', self.id, variant, output_path)
        with Canvas(SOLID, xlim=[-5.748693168290014, 31.03360313902346], ylim=[-17.706526724199993, 19.07576958311348], axes_position=[0.05, 0.05, 0.9, 0.9], coordinate_axes=False) as c:
            for object_id, points in [('netedge0', [[0.0, 0.0], [26.0, 0.0]]), ('netedge1', [[0.0, 2.0], [26.0, 2.0]]), ('netedge2', [[0.0, 0.0], [0.0, 2.0]]), ('netedge3', [[8.0, 0.0], [8.0, 10.0]]), ('netedge4', [[13.0, -5.0], [13.0, 10.0]]), ('netedge5', [[21.0, -5.0], [21.0, 2.0]]), ('netedge6', [[26.0, 0.0], [26.0, 2.0]]), ('netedge7', [[8.0, 10.0], [13.0, 10.0]]), ('netedge8', [[13.0, -5.0], [21.0, -5.0]])]:
                c.line(points, id=object_id, zorder=3, clip_on=False)
            c.line([[-0.8869187959903904, 0.0], [-0.8869187959903904, 10.0]], id='height10_range', zorder=3, clip_on=False, linestyle=(0.0, [4.0, 3.0]))
            c.line([[0.0, 0.0], [-0.8869187959903904, 0.0]], id='height10_start', zorder=3, clip_on=False)
            c.line([[0.0, 10.0], [-0.8869187959903904, 10.0]], id='height10_end', zorder=3, clip_on=False)
            c.text('10 cm', [-0.8869187959903904, 5.0], id='netedge8', ha='right', rotation_mode='default', offset_pt=[-6, 0], annotation_clip=None)
            c.line([[26.88691879599039, -5.0], [26.88691879599039, 2.0]], id='height7_range', zorder=3, clip_on=False, linestyle=(0.0, [4.0, 3.0]))
            c.line([[26.0, -5.0], [26.88691879599039, -5.0]], id='height7_start', zorder=3, clip_on=False)
            c.line([[26.0, 2.0], [26.88691879599039, 2.0]], id='height7_end', zorder=3, clip_on=False)
            c.text('7 cm', [26.88691879599039, -1.5], id='netedge8', ha='left', rotation_mode='default', offset_pt=[6, 0], annotation_clip=None)
            c.line([[0.0, -7.390989966586586], [26.0, -7.390989966586586]], id='width26_range', zorder=3, clip_on=False, linestyle=(0.0, [4.0, 3.0]))
            c.line([[0.0, 0.0], [0.0, -7.390989966586586]], id='width26_start', zorder=3, clip_on=False)
            c.line([[26.0, 0.0], [26.0, -7.390989966586586]], id='width26_end', zorder=3, clip_on=False)
            c.text('26 cm', [13.0, -7.390989966586586], id='netedge8', rotation_mode='default', offset_pt=[0, -13], annotation_clip=None)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Solid180().draw(sys.argv[1] if len(sys.argv) > 1 else None))
