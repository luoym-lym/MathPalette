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
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Analytics' / 'Ana39_C01.png'
    with Canvas(ANALYTICS, xlim=(-8.0, 8.0), ylim=(-8.0, 8.0), axes_position=(0.12, 0.12, 0.8, 0.8), coordinate_axes=True) as c:
        c.line([[-5.0, 4.0], [-3.0, 3.0], [0.0, 7.0], [3.0, 1.0], [4.0, -5.0]], id='curve_001', solid_capstyle='butt')
        c.point([[-5.0, 4.0], [4.0, -5.0]], id='point_001')
        c.text('h', (2, 1.8), id='text_001', rotation_mode='default')
        c.line([[-5, 8], [-5, -8]], zorder=9, color='#2563EB', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
        c.line([[5, 8], [5, -8]], zorder=9, color='#2563EB', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
        return c.save(output_path)

def C02(output_path=None):
    if output_path is None:
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Analytics' / 'Ana39_C02.png'
    with Canvas(ANALYTICS, xlim=(-8.0, 8.0), ylim=(-8.0, 8.0), axes_position=(0.12, 0.12, 0.8, 0.8), coordinate_axes=True) as c:
        c.line([[-5.0, 4.0], [-3.0, 3.0], [0.0, 7.0], [3.0, 1.0], [4.0, -5.0]], id='curve_001', solid_capstyle='butt')
        c.point([[-5.0, 4.0], [4.0, -5.0]], id='point_001')
        c.text('h', (2, 1.8), id='text_001', rotation_mode='default')
        c.line([[-5, 8], [-5, -8]], zorder=9, color='#2563EB', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
        c.line([[7, 8], [7, -8]], zorder=9, color='#2563EB', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
        return c.save(output_path)
