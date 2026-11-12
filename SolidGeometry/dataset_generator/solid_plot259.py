"""Frozen question Solid259; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Solid259:

    def __init__(self):
        self.id = 'Solid259'
        self.source_dataset = 'Author Designed'
        self.source_key = 'author-expand24:Solid94/extension_02'
        self.question = 'The pictured rectangular cuboid has side lengths 2, 3 and 4. At each of its eight vertices, mark the point on each of its three incident edges that is 1/2 of the way from that vertex to the other end of the edge. For example, P, Q and R are the three points at vertex A. Cut the rectangular cuboid by the plane through the three marked points at each vertex. Describe the shape of the piece containing the centre by giving the number and shape of all its faces. The figure shows only the three marks at A; all eight planes are included in the cuts.'
        self.answer = 'A convex polyhedron with 8 congruent scalene triangular faces and 6 rhombic faces (an affine cuboctahedron).'
        self.answer_type = 'text'
        self.query = self.question
        self.subject = 'SolidGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'SolidGeometry' / 'dataset_generator/scenes/Solid259.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('SolidGeometry', self.id, variant, output_path)
        with Canvas(SOLID, xlim=[-1.1743526281893089, 4.472302080233002], ylim=[-0.8925800875269747, 4.754074620895335], axes_position=[0.05, 0.05000000000000006, 0.9, 0.8999999999999999], coordinate_axes=False) as c:
            for object_id, points in [('edge_000_010', [[0.0, 0.0], [1.6106264765794776, 1.7870346869633513]]), ('edge_010_110', [[1.6106264765794776, 1.7870346869633513], [3.2979494520436923, 1.0288987591607173]]), ('edge_010_011', [[1.6106264765794776, 1.7870346869633513], [1.6106264765794776, 4.619630461170995]])]:
                c.line(points, id=object_id, linestyle=(0.0, [4.0, 3.0]))
            for object_id, points in [('edge_000_100', [[0.0, 0.0], [1.687322975464215, -0.758135927802634]]), ('edge_000_001', [[0.0, 0.0], [0.0, 2.8325957742076433]]), ('edge_001_101', [[0.0, 2.8325957742076433], [1.687322975464215, 2.0744598464050092]]), ('edge_001_011', [[0.0, 2.8325957742076433], [1.6106264765794776, 4.619630461170995]]), ('edge_011_111', [[1.6106264765794776, 4.619630461170995], [3.2979494520436923, 3.8614945333683606]]), ('edge_100_110', [[1.687322975464215, -0.758135927802634], [3.2979494520436923, 1.0288987591607173]]), ('edge_100_101', [[1.687322975464215, -0.758135927802634], [1.687322975464215, 2.0744598464050092]]), ('edge_101_111', [[1.687322975464215, 2.0744598464050092], [3.2979494520436923, 3.8614945333683606]]), ('edge_110_111', [[3.2979494520436923, 1.0288987591607173], [3.2979494520436923, 3.8614945333683606]])]:
                c.line(points, id=object_id)
            for object_id, points in [(None, [[0.8436614877321075, 2.4535278103063263]]), (None, [[2.4926362137539537, 2.967977189886685]]), (None, [[1.687322975464215, 0.6581619593011877]])]:
                c.point(points, id=object_id)
            c.text('A', [1.687322975464215, 2.0744598464050092], zorder=3, clip_on=True, fontsize=18.0, fontstyle='italic', ha='left', va='top', rotation_mode='default', offset_pt=[9, -7], annotation_clip=None)
            c.text('P', [0.8436614877321075, 2.4535278103063263], zorder=3, clip_on=True, fontsize=18.0, fontstyle='italic', ha='right', va='bottom', rotation_mode='default', offset_pt=[-4, 7], annotation_clip=None)
            c.text('Q', [2.4926362137539537, 2.967977189886685], zorder=3, clip_on=True, fontsize=18.0, fontstyle='italic', ha='right', va='bottom', rotation_mode='default', offset_pt=[-6, 8], annotation_clip=None)
            c.text('R', [1.687322975464215, 0.6581619593011877], zorder=3, clip_on=True, fontsize=18.0, fontstyle='italic', ha='left', rotation_mode='default', offset_pt=[9, 0], annotation_clip=None)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Solid259().draw(sys.argv[1] if len(sys.argv) > 1 else None))
