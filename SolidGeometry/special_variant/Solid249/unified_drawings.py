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
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / 'Solid249_C01.png'
    with Canvas(SOLID, xlim=(-5.0, 5.0), ylim=(-5.0, 5.0), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        for object_id, points in [('bottom', [[-4, -4], [4, -4]]), ('right', [[4, -4], [4, 4]]), ('top', [[4, 4], [-4, 4]]), ('left', [[-4, 4], [-4, -4]])]:
            c.line(points, id=object_id)
        c.circle([-2, 1], 0.14, id='hole0', zorder=1, edgecolor=(0.1450980392156863, 0.38823529411764707, 0.9215686274509803, 1.0), linewidth=1.5, fill=False)
        c.circle([2, 1], 0.14, id='hole1', zorder=1, edgecolor=(0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0), linewidth=1.5, fill=False)
        c.circle([-1, -2], 0.14, id='hole2', zorder=1, edgecolor=(0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0), linewidth=1.5, fill=False)
        c.circle([1, -2], 0.14, id='hole3', zorder=1, edgecolor=(0.1450980392156863, 0.38823529411764707, 0.9215686274509803, 1.0), linewidth=1.5, fill=False)
        return c.save(output_path)
