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
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / 'Solid289_C01.png'
    with Canvas(SOLID, xlim=(-0.4094781999452133, 6.022402342750617), ylim=(-0.5836299143344066, 5.8482506283614235), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        c.line([[0.0, 0.0], [0.0, 4.0]], id='edge0', zorder=3, clip_on=False, color='#2563EB')
        c.line([[0.0, 0.0], [1.6, 1.2]], id='edge1', clip_on=False, linestyle=(0, [4, 3]))
        c.line([[0.0, 0.0], [4.0, 0.0]], id='edge2', zorder=3, clip_on=False, color='#DC2626')
        c.line([[0.0, 4.0], [1.6, 5.2]], id='edge3', zorder=3, clip_on=False)
        c.line([[0.0, 4.0], [4.0, 4.0]], id='edge4', zorder=3, clip_on=False)
        c.line([[1.6, 1.2], [1.6, 5.2]], id='edge5', clip_on=False, linestyle=(0, [4, 3]))
        c.line([[1.6, 1.2], [5.6, 1.2]], id='edge6', clip_on=False, linestyle=(0, [4, 3]))
        for object_id, points in [('edge7', [[1.6, 5.2], [5.6, 5.2]]), ('edge8', [[4.0, 0.0], [4.0, 4.0]]), ('edge9', [[4.0, 0.0], [5.6, 1.2]]), ('edge10', [[4.0, 4.0], [5.6, 5.2]]), ('edge11', [[5.6, 1.2], [5.6, 5.2]])]:
            c.line(points, id=object_id, zorder=3, clip_on=False)
        c.text('A', (0.0, 0.0), fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(-14, -12), annotation_clip=None)
        c.text('B', (5.6, 1.2), fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(15, -5), annotation_clip=None)
        c.text('D', (1.6, 5.2), fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(0, 17), annotation_clip=None)
        return c.save(output_path)
