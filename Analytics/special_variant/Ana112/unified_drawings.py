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
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Analytics' / 'Ana112_C01.png'
    with Canvas(ANALYTICS, xlim=(-8.0, 8.0), ylim=(-8.0, 8.0), axes_position=(0.12, 0.12, 0.8, 0.8), coordinate_axes=True) as c:
        c.line([[-8.0, -3.0], [-6.0, -3.0]], id='curve_001', solid_capstyle='butt')
        c.point([[-8.0, -3.0]], id='point_001', clip_on=False)
        c.point([[-6.0, -3.0]], id='point_002', clip_on=False, facecolors=[[1.0, 1.0, 1.0, 1.0]])
        c.line([[-6.0, -2.0], [-4.0, -2.0]], id='curve_002', solid_capstyle='butt')
        c.point([[-6.0, -2.0]], id='point_003', clip_on=False)
        c.point([[-4.0, -2.0]], id='point_004', clip_on=False, facecolors=[[1.0, 1.0, 1.0, 1.0]])
        c.line([[-4.0, -1.0], [-2.0, -1.0]], id='curve_003', solid_capstyle='butt')
        c.point([[-4.0, -1.0]], id='point_005', clip_on=False)
        c.point([[-2.0, -1.0]], id='point_006', clip_on=False, facecolors=[[1.0, 1.0, 1.0, 1.0]])
        c.line([[-2.0, 0.0], [0.0, 0.0]], id='curve_004', solid_capstyle='butt')
        c.point([[-2.0, 0.0]], id='point_007', clip_on=False)
        c.point([[0.0, 0.0]], id='point_008', clip_on=False, facecolors=[[1.0, 1.0, 1.0, 1.0]])
        c.line([[0.0, 1.0], [2.0, 1.0]], id='curve_005', solid_capstyle='butt')
        c.point([[0.0, 1.0]], id='point_009', clip_on=False)
        c.point([[2.0, 1.0]], id='point_010', clip_on=False, facecolors=[[1.0, 1.0, 1.0, 1.0]])
        c.line([[2.0, 2.0], [4.0, 2.0]], id='curve_006', solid_capstyle='butt')
        c.point([[2.0, 2.0]], id='point_011', clip_on=False)
        c.point([[4.0, 2.0]], id='point_012', clip_on=False, facecolors=[[1.0, 1.0, 1.0, 1.0]])
        c.line([[4.0, 3.0], [6.0, 3.0]], id='curve_007', solid_capstyle='butt')
        c.point([[4.0, 3.0]], id='point_013', clip_on=False)
        c.point([[6.0, 3.0]], id='point_014', clip_on=False, facecolors=[[1.0, 1.0, 1.0, 1.0]])
        c.line([[6.0, 4.0], [8.0, 4.0]], id='curve_008', solid_capstyle='butt')
        c.point([[6.0, 4.0]], id='point_015', clip_on=False)
        c.point([[8.0, 4.0]], id='point_016', clip_on=False, facecolors=[[1.0, 1.0, 1.0, 1.0]])
        c.point([[8.0, 5.0]], id='point_017', clip_on=False)
        c.line([[0.0, 2.0], [1.6, 2.0]], zorder=9, color='#2563EB', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
        c.point([[0.0, 2.0]], zorder=10, s=[50], facecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]], edgecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]])
        return c.save(output_path)
