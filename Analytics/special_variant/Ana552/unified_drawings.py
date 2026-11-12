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
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Analytics' / 'Ana552_C01.png'
    with Canvas(ANALYTICS, xlim=(-8.0, 8.0), ylim=(-8.0, 8.0), axes_position=(0.12, 0.12, 0.8, 0.8), coordinate_axes=True) as c:
        c.line([[-6.0, 3.0], [-2.0, -1.0], [2.0, 3.0], [6.0, -1.0]], id='curve_001', solid_capstyle='butt')
        c.line([[-6.0, -1.0], [-2.0, 3.0], [2.0, -1.0], [6.0, 3.0]], id='curve_002', solid_capstyle='butt')
        c.point([[-6.0, 3.0], [6.0, -1.0], [-6.0, -1.0], [6.0, 3.0]], id='point_001')
        for object_id, text, anchor in [('text_001', '$f$', (6.5, -1.3)), ('text_002', '$g$', (6.5, 3.3)), ('text_003', '$f$', (-6.5, 3.3)), ('text_004', '$g$', (-6.5, -1.3))]:
            c.text(text, anchor, id=object_id, rotation_mode='default')
        c.line([[-6.5, 1.0], [-0.7, 1.0]], zorder=9, color='#2563EB', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
        c.line([[0.3, 1.0], [6.5, 1.0]], zorder=9, color='#2563EB', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
        for object_id, text, anchor in [(None, '$\\int f-\\int g$', (-4, 4.6)), (None, '$+$', (-5, 1.5)), (None, '$-$', (-1, 1.5)), (None, '$+$', (3, 1.5)), (None, '$-$', (5, 1.5))]:
            c.text(text, anchor, id=object_id, zorder=11, clip_on=True, color='#2563EB', rotation_mode='default')
        return c.save(output_path)
