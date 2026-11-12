"""Frozen question Solid258; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Solid258:

    def __init__(self):
        self.id = 'Solid258'
        self.source_dataset = 'Author Designed'
        self.source_key = 'author-expand24:Solid94/extension_01'
        self.question = 'The pictured cube. At each of its eight vertices, mark the point on each of its three incident edges that is 1/3 of the way from that vertex to the other end of the edge. For example, P, Q and R are the three points at vertex A. Cut the cube by the plane through the three marked points at each vertex. Describe the shape of the piece containing the centre by giving the number and shape of all its faces. The figure shows only the three marks at A; all eight planes are included in the cuts.'
        self.answer = 'A convex polyhedron with 8 equilateral triangular faces and 6 equiangular non-regular octagonal faces (a truncated cube with unequal edge lengths).'
        self.answer_type = 'text'
        self.query = self.question
        self.subject = 'SolidGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'SolidGeometry' / 'dataset_generator/scenes/Solid258.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('SolidGeometry', self.id, variant, output_path)
        with Canvas(SOLID, xlim=[-0.5797543700066932, 4.7213653097824935], ylim=[-1.263421026937027, 4.03769865285216], axes_position=[0.05, 0.05, 0.9, 0.9], coordinate_axes=False) as c:
            for object_id, points in [('edge_000_010', [[0.0, 0.0], [1.6106264765794776, 1.7870346869633513]]), ('edge_010_110', [[1.6106264765794776, 1.7870346869633513], [4.1416109397758, 0.6498307952594005]]), ('edge_010_011', [[1.6106264765794776, 1.7870346869633513], [1.6106264765794776, 3.911481517619084]])]:
                c.line(points, id=object_id, linestyle=(0.0, [4.0, 3.0]))
            for object_id, points in [('edge_000_100', [[0.0, 0.0], [2.5309844631963223, -1.1372038917039509]]), ('edge_000_001', [[0.0, 0.0], [0.0, 2.1244468306557325]]), ('edge_001_101', [[0.0, 2.1244468306557325], [2.5309844631963223, 0.9872429389517816]]), ('edge_001_011', [[0.0, 2.1244468306557325], [1.6106264765794776, 3.911481517619084]]), ('edge_011_111', [[1.6106264765794776, 3.911481517619084], [4.1416109397758, 2.7742776259151327]]), ('edge_100_110', [[2.5309844631963223, -1.1372038917039509], [4.1416109397758, 0.6498307952594005]]), ('edge_100_101', [[2.5309844631963223, -1.1372038917039509], [2.5309844631963223, 0.9872429389517816]]), ('edge_101_111', [[2.5309844631963223, 0.9872429389517816], [4.1416109397758, 2.7742776259151327]]), ('edge_110_111', [[4.1416109397758, 0.6498307952594005], [4.1416109397758, 2.7742776259151327]])]:
                c.line(points, id=object_id)
            for object_id, points in [(None, [[1.687322975464215, 1.3663109028530984]]), (None, [[3.0678599553894816, 1.5829211679395654]]), (None, [[2.5309844631963223, 0.2790939953998708]])]:
                c.point(points, id=object_id)
            c.text('A', [2.5309844631963223, 0.9872429389517816], zorder=3, clip_on=True, fontsize=18.0, fontstyle='italic', ha='left', va='top', rotation_mode='default', offset_pt=[9, -7], annotation_clip=None)
            c.text('P', [1.687322975464215, 1.3663109028530984], zorder=3, clip_on=True, fontsize=18.0, fontstyle='italic', ha='right', va='bottom', rotation_mode='default', offset_pt=[-4, 7], annotation_clip=None)
            c.text('Q', [3.0678599553894816, 1.5829211679395654], zorder=3, clip_on=True, fontsize=18.0, fontstyle='italic', ha='right', va='bottom', rotation_mode='default', offset_pt=[-6, 8], annotation_clip=None)
            c.text('R', [2.5309844631963223, 0.2790939953998708], zorder=3, clip_on=True, fontsize=18.0, fontstyle='italic', ha='left', rotation_mode='default', offset_pt=[9, 0], annotation_clip=None)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Solid258().draw(sys.argv[1] if len(sys.argv) > 1 else None))
