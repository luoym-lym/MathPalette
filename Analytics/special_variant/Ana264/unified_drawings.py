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
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Analytics' / 'Ana264_C01.png'
    with Canvas(ANALYTICS, xlim=(-8.0, 8.0), ylim=(-8.0, 8.0), axes_position=(0.12, 0.12, 0.8, 0.8), coordinate_axes=True) as c:
        c.line([[-7.5, -5.25], [1.0, 7.5]], id='curve_001', color='#2563EB', linewidth=0.5, linestyle=(0.0, [1.85, 0.8]), solid_capstyle='butt')
        c.point([[-4.0, 0.0]], id='point_001')
        c.point([[0.0, 6.0]], id='point_002')
        c.text('A', (-4.25, 0.37), id='text_001', ha='right', va='bottom', rotation_mode='default')
        c.text('B', (-0.75, 6.37), id='text_002', ha='right', va='bottom', rotation_mode='default')
        c.line([[-7.5, -2.625], [6.0, 7.5]], zorder=9, color='#EA580C', solid_capstyle='butt')
        c.point([[0.0, 3.0]], zorder=10, s=[50], facecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]], edgecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]])
        return c.save(output_path)
