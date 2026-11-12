"""Frozen question Plane320; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane320:

    def __init__(self):
        self.id = 'Plane320'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:1007'
        self.question = 'A spiral of isosceles triangles is constructed counterclockwise, starting with the shaded triangle $B A C$, whose top angle is $\\angle B A C=100^{\\circ}$. Triangle $\\triangle A B C$ is numbered 0. Each subsequent triangle (numbered 1, 2, $3, \\ldots$ ) shares exactly one edge with the previous triangle, as shown. What is the number of the first triangle that precisely covers triangle $\\mathrm{nr}$. 0?'
        self.answer = '18'
        self.answer_type = 'number'
        self.query = self.question
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane320.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-2.4303994153869843, 2.9512327487203174], ylim=[-3.0398379286795736, 2.341794235427728], axes_position=[0.05, 0.05, 0.9, 0.9], coordinate_axes=False) as c:
            c.path([[0.0, 0.0], [1.5000000000000004, -2.598076211353316], [2.298133329356934, 1.9283628290596178], [0.0, 0.0]], [1, 2, 2, 79], id='o0', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45], linewidth=0.0, capstyle='butt')
            c.path([[0.0, 0.0], [1.5000000000000004, -2.598076211353316], [2.298133329356934, 1.9283628290596178], [0.0, 0.0]], [1, 2, 2, 79], id='o0', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            for object_id, points in [('o1', [[2.298133329356934, 1.9283628290596178], [-2.2981333293569337, 1.9283628290596184]]), ('o2', [[-2.2981333293569337, 1.9283628290596184], [-1.5000000000000013, -2.598076211353315]]), ('o3', [[-1.5000000000000013, -2.598076211353315], [2.8190778623577253, -1.0260604299770058]]), ('o6', [[0.0, 0.0], [-2.2981333293569337, 1.9283628290596184]]), ('o7', [[0.0, 0.0], [-1.5000000000000013, -2.598076211353315]]), ('o8', [[0.0, 0.0], [2.8190778623577253, -1.0260604299770058]])]:
                c.line(points, id=object_id)
            for object_id, text, anchor in [('t0', '0', [1.2660444431189781, -0.22323779409789943]), ('t1', '1', [1.4802973661668753e-16, 1.2855752193730787]), ('t2', '2', [-1.2660444431189783, -0.2232377940978989]), ('t3', '3', [0.3957233587073172, -1.0872409923990964])]:
                c.text(text, anchor, id=object_id, rotation_mode='default', offset_pt=[0, 0], annotation_clip=None)
            c.text('A', [0.0, 0.0], id='lA', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[-14, -3], annotation_clip=None)
            c.text('B', [2.298133329356934, 1.9283628290596178], id='lB', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[10, 12], annotation_clip=None)
            c.text('C', [1.5000000000000004, -2.598076211353316], id='lC', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[0, -17], annotation_clip=None)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane320().draw(sys.argv[1] if len(sys.argv) > 1 else None))
