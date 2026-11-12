"""Frozen question Solid260; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Solid260:

    def __init__(self):
        self.id = 'Solid260'
        self.source_dataset = 'Author Designed'
        self.source_key = 'author-expand24:Solid94/extension_03'
        self.question = 'The pictured cube. At each of its eight vertices, mark the point on each of its three incident edges that is 3/4 of the way from that vertex to the other end of the edge. For example, P, Q and R are the three points at vertex A. Cut the cube by the plane through the three marked points at each vertex. Describe the shape of the piece containing the centre by giving the number and shape of all its faces. The figure shows only the three marks at A; all eight planes are included in the cuts.'
        self.answer = 'A convex polyhedron with 6 square faces and 8 regular hexagonal faces (a truncated octahedron).'
        self.answer_type = 'text'
        self.query = self.question
        self.subject = 'SolidGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'SolidGeometry' / 'dataset_generator/scenes/Solid260.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('SolidGeometry', self.id, variant, output_path)
        with Canvas(SOLID, xlim=[-0.773005826675591, 6.295153746376657], ylim=[-1.6845613692493693, 5.38359820380288], axes_position=[0.05, 0.05, 0.9, 0.9], coordinate_axes=False) as c:
            for object_id, points in [('edge_000_010', [[0.0, 0.0], [2.147501968772637, 2.382712915951135]]), ('edge_010_110', [[2.147501968772637, 2.382712915951135], [5.522147919701067, 0.8664410603458672]]), ('edge_010_011', [[2.147501968772637, 2.382712915951135], [2.147501968772637, 5.215308690158778]])]:
                c.line(points, id=object_id, linestyle=(0.0, [4.0, 3.0]))
            for object_id, points in [('edge_000_100', [[0.0, 0.0], [3.37464595092843, -1.516271855605268]]), ('edge_000_001', [[0.0, 0.0], [0.0, 2.8325957742076433]]), ('edge_001_101', [[0.0, 2.8325957742076433], [3.37464595092843, 1.3163239186023754]]), ('edge_001_011', [[0.0, 2.8325957742076433], [2.147501968772637, 5.215308690158778]]), ('edge_011_111', [[2.147501968772637, 5.215308690158778], [5.522147919701067, 3.6990368345535103]]), ('edge_100_110', [[3.37464595092843, -1.516271855605268], [5.522147919701067, 0.8664410603458672]]), ('edge_100_101', [[3.37464595092843, -1.516271855605268], [3.37464595092843, 1.3163239186023754]]), ('edge_101_111', [[3.37464595092843, 1.3163239186023754], [5.522147919701067, 3.6990368345535103]]), ('edge_110_111', [[5.522147919701067, 0.8664410603458672], [5.522147919701067, 3.6990368345535103]])]:
                c.line(points, id=object_id)
            for object_id, points in [(None, [[0.8436614877321075, 2.4535278103063263]]), (None, [[4.9852724275079074, 3.1033586055657265]]), (None, [[3.37464595092843, -0.8081229120533571]])]:
                c.point(points, id=object_id)
            c.text('A', [3.37464595092843, 1.3163239186023754], zorder=3, clip_on=True, fontsize=18.0, fontstyle='italic', ha='left', va='top', rotation_mode='default', offset_pt=[9, -7], annotation_clip=None)
            c.text('P', [0.8436614877321075, 2.4535278103063263], zorder=3, clip_on=True, fontsize=18.0, fontstyle='italic', ha='right', va='bottom', rotation_mode='default', offset_pt=[-4, 7], annotation_clip=None)
            c.text('Q', [4.9852724275079074, 3.1033586055657265], zorder=3, clip_on=True, fontsize=18.0, fontstyle='italic', ha='right', va='bottom', rotation_mode='default', offset_pt=[-6, 8], annotation_clip=None)
            c.text('R', [3.37464595092843, -0.8081229120533571], zorder=3, clip_on=True, fontsize=18.0, fontstyle='italic', ha='left', rotation_mode='default', offset_pt=[9, 0], annotation_clip=None)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Solid260().draw(sys.argv[1] if len(sys.argv) > 1 else None))
