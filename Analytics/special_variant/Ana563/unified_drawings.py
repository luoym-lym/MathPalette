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
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Analytics' / 'Ana563_C01.png'
    with Canvas(ANALYTICS, xlim=(-8.0, 8.0), ylim=(-8.0, 8.0), axes_position=(0.12, 0.12, 0.8, 0.8), coordinate_axes=True) as c:
        c.line([[1.0, 1.0], [4.0, 3.0]], id='curve_001', solid_capstyle='butt')
        c.point([[1.0, 1.0], [4.0, 3.0], [-3.0, 4.0]], id='point_001')
        for object_id, text, anchor in [('text_001', 'A', (1.1, 1.6)), ('text_002', 'B', (4.4, 3.3)), ('text_003', 'P', (-3.5, 4.4))]:
            c.text(text, anchor, id=object_id, rotation_mode='default')
        c.line([[-2, -1], [1, 1]], zorder=9, color='#2563EB', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
        c.line([[-3.0, 4.0], [-0.38461538461538464, 0.07692307692307693]], zorder=9, color='#2563EB', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
        c.point([[-0.38461538461538464, 0.07692307692307693]], zorder=10, s=[50], facecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]], edgecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]])
        c.text('H', (0.8, -1.1), zorder=11, clip_on=True, color='#2563EB', rotation_mode='default')
        return c.save(output_path)
