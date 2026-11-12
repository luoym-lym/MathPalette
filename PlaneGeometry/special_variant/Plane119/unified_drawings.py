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
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / 'Plane119_C01.png'
    with Canvas(PLANE, xlim=(0.395, 7.275), ylim=(0.405, 7.285), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        for object_id, points in [('edge_01', [[1.86, 6.58], [5.81, 7.13]]), ('edge_02', [[5.81, 7.13], [7.12, 3.84]]), ('edge_03', [[7.12, 3.84], [6.03, 1.1]]), ('edge_04', [[6.03, 1.1], [2.74, 0.56]]), ('edge_05', [[2.74, 0.56], [0.55, 1.65]]), ('edge_06', [[0.55, 1.65], [1.86, 6.58]])]:
            c.line(points, id=object_id)
        for object_id, points in [(None, [[1.86, 6.58]]), (None, [[0.55, 1.65]]), (None, [[2.74, 0.56]]), (None, [[6.03, 1.1]]), (None, [[7.12, 3.84]]), (None, [[5.81, 7.13]]), (None, [[3.870130718954248, 6.859215686274511]]), (None, [[1.172091503267974, 4.048758169934642]]), (None, [[1.5093464052287582, 1.189117647058823]]), (None, [[4.48140522875817, 0.8518627450980389]]), (None, [[6.6243790849673205, 2.55921568627451]]), (None, [[6.4768300653594775, 5.425882352941177]])]:
            c.point(points, id=object_id, zorder=10, s=[50], facecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]], edgecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]])
        return c.save(output_path)
