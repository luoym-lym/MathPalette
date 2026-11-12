"""Frozen, previously passed Special drawings on the unified protocol. No new Pass/Collect."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[3]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

def C01(output_path=None):
    if output_path is None:
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / 'Solid259_C01.png'
    with Canvas(SOLID, xlim=(-1.1743526281893089, 4.472302080233002), ylim=(-0.8925800875269747, 4.754074620895335), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        for object_id, points in [('edge_000_010', [[0.0, 0.0], [1.6106264765794776, 1.7870346869633513]]), ('edge_010_110', [[1.6106264765794776, 1.7870346869633513], [3.2979494520436923, 1.0288987591607173]]), ('edge_010_011', [[1.6106264765794776, 1.7870346869633513], [1.6106264765794776, 4.619630461170995]])]:
            c.line(points, id=object_id, color='#EA580C', linewidth=1.5, linestyle=(0.0, [4.0, 3.0]))
        for object_id, points in [('edge_000_100', [[0.0, 0.0], [1.687322975464215, -0.758135927802634]]), ('edge_000_001', [[0.0, 0.0], [0.0, 2.8325957742076433]]), ('edge_001_101', [[0.0, 2.8325957742076433], [1.687322975464215, 2.0744598464050092]]), ('edge_001_011', [[0.0, 2.8325957742076433], [1.6106264765794776, 4.619630461170995]]), ('edge_011_111', [[1.6106264765794776, 4.619630461170995], [3.2979494520436923, 3.8614945333683606]]), ('edge_100_110', [[1.687322975464215, -0.758135927802634], [3.2979494520436923, 1.0288987591607173]]), ('edge_100_101', [[1.687322975464215, -0.758135927802634], [1.687322975464215, 2.0744598464050092]]), ('edge_101_111', [[1.687322975464215, 2.0744598464050092], [3.2979494520436923, 3.8614945333683606]]), ('edge_110_111', [[3.2979494520436923, 1.0288987591607173], [3.2979494520436923, 3.8614945333683606]])]:
            c.line(points, id=object_id)
        for object_id, points in [(None, [[0.8436614877321075, 2.4535278103063263]]), (None, [[2.4926362137539537, 2.967977189886685]]), (None, [[1.687322975464215, 0.6581619593011877]])]:
            c.point(points, id=object_id)
        c.text('A', (1.687322975464215, 2.0744598464050092), zorder=3, clip_on=True, fontsize=18.0, fontstyle='italic', ha='left', va='top', rotation_mode='default', offset_pt=(9, -7), annotation_clip=None)
        c.text('P', (0.8436614877321075, 2.4535278103063263), zorder=3, clip_on=True, fontsize=18.0, fontstyle='italic', ha='right', va='bottom', rotation_mode='default', offset_pt=(-4, 7), annotation_clip=None)
        c.text('Q', (2.4926362137539537, 2.967977189886685), zorder=3, clip_on=True, fontsize=18.0, fontstyle='italic', ha='right', va='bottom', rotation_mode='default', offset_pt=(-6, 8), annotation_clip=None)
        c.text('R', (1.687322975464215, 0.6581619593011877), zorder=3, clip_on=True, fontsize=18.0, fontstyle='italic', ha='left', rotation_mode='default', offset_pt=(9, 0), annotation_clip=None)
        c.line([[2.4926362137539537, 2.967977189886685], [1.687322975464215, 0.6581619593011877]], zorder=9, color='#2563EB', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
        c.line([[1.687322975464215, 0.6581619593011877], [0.8436614877321075, 2.4535278103063263]], zorder=9, color='#2563EB', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
        return c.save(output_path)
