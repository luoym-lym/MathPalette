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
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Analytics' / 'Ana562_C01.png'
    with Canvas(ANALYTICS, xlim=(-8.0, 8.0), ylim=(-8.0, 8.0), axes_position=(0.12, 0.12, 0.8, 0.8), coordinate_axes=True) as c:
        c.line([[-3.0, -2.0], [6.0, 4.0]], id='curve_001', solid_capstyle='butt')
        c.point([[-3.0, -2.0], [6.0, 4.0], [1.0, 3.0]], id='point_001')
        for object_id, text, anchor in [('text_001', 'A', (-3.4, -2.5)), ('text_002', 'B', (6.4, 4.4)), ('text_003', 'P', (0.5, 3.5))]:
            c.text(text, anchor, id=object_id, rotation_mode='default')
        c.line([[1.0, 3.0], [2.076923076923077, 1.3846153846153846]], zorder=9, color='#2563EB', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
        c.point([[2.076923076923077, 1.3846153846153846]], zorder=10, s=[50], facecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]], edgecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]])
        c.text('H', (2.8, 0.8), zorder=11, clip_on=True, color='#2563EB', rotation_mode='default')
        return c.save(output_path)
