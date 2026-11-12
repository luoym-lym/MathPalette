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
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / 'Plane324_C01.png'
    with Canvas(PLANE, xlim=(-0.16814956219310906, 3.172145258471985), ylim=(-0.3707154221712696, 2.9695793984938246), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        for object_id, center, radius in [('dot0', [0.0, 0.0], 0.09), ('dot1', [1.0, 0.0], 0.09), ('dot2', [2.0, 0.0], 0.09), ('dot3', [3.0, 0.0], 0.09), ('dot4', [0.5, 0.8660254037844386], 0.09), ('dot5', [1.5, 0.8660254037844386], 0.09), ('dot6', [2.5, 0.8660254037844386], 0.09), ('dot7', [1.0, 1.7320508075688772], 0.09), ('dot8', [2.0, 1.7320508075688772], 0.09), ('dot9', [1.5, 2.598076211353316], 0.09)]:
            c.circle(center, radius, id=object_id, facecolor=(0.0, 0.0, 0.0, 1.0))
        for object_id, points in [(None, [[1.5019978481394378, 2.6059402768813866], [0.9834880312061307, 1.7258380876130102]]), (None, [[0.9971330263885863, 1.7326605852042378], [2.0136851674815173, 1.7258380876130102]]), (None, [[1.4917641017525962, 2.6059402768813866], [2.0102739186859035, 1.7258380876130102]])]:
            c.line(points, id=object_id, zorder=9, color='#2563EB', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
        for object_id, points in [(None, [[0.4990907022289624, 0.8764371375051585], [-0.01941911470434471, 0.009979943419236914]]), (None, [[-0.0057741195218892205, -0.00025380296760468823], [1.0141892703666555, 0.006568694623623639]]), (None, [[0.49226820463773474, 0.8696146399139306], [1.0141892703666555, -0.010487549354445402]])]:
            c.line(points, id=object_id, zorder=9, color='#DC2626', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
        for object_id, points in [(None, [[2.494671247663072, 0.8798483863007722], [1.9932176747078338, 0.02021368980607896]]), (None, [[2.0034514210946757, 0.0031574458280094753], [2.999536069413924, 0.0031574458280094753]]), (None, [[2.498082496458686, 0.8832596350963859], [3.0268260597788346, 0.013391192214851078]])]:
            c.line(points, id=object_id, zorder=9, color='#16A34A', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
        return c.save(output_path)
