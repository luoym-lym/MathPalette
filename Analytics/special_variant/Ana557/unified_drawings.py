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
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Analytics' / 'Ana557_C01.png'
    with Canvas(ANALYTICS, xlim=(-8.0, 8.0), ylim=(-8.0, 8.0), axes_position=(0.12, 0.12, 0.8, 0.8), coordinate_axes=True) as c:
        c.line([[2.0, -1.0], [5.0, 1.0]], id='curve_001', solid_capstyle='butt')
        c.point([[2.0, -1.0]], id='point_001')
        c.point([[5.0, 1.0]], id='point_002')
        c.text('C', (2.4, -1.4), id='text_001', rotation_mode='default')
        c.text('P', (5.4, 1.3), id='text_002', rotation_mode='default')
        for object_id, points in [(None, [[0, 0], [5, 1]]), (None, [[0, 0], [-1, 5]]), (None, [[4.999999999999999, 0.9999999999999999], [4.826698114649, 1.6440758224740681]]), (None, [[4.826698114649, 1.6440758224740681], [4.570810086342821, 2.2600210518016715]]), (None, [[4.570810086342821, 2.2600210518016715], [4.236714230191343, 2.8372966943367355]]), (None, [[4.236714230191343, 2.8372966943367355], [3.8301270189221928, 3.366025403784438]]), (None, [[3.8301270189221928, 3.366025403784438], [3.3580052724474547, 3.8371604853348384]]), (None, [[3.3580052724474547, 3.8371604853348384], [2.82842712474619, 4.242640687119285]]), (None, [[2.82842712474619, 4.242640687119285], [2.250453804752368, 4.575528130464896]]), (None, [[2.250453804752368, 4.575528130464896], [1.6339745962155623, 4.830127018922193]]), (None, [[1.6339745962155623, 4.830127018922193], [0.9895376293141628, 5.0020810949215235]]), (None, [[0.9895376293141628, 5.0020810949215235], [0.3281693992235359, 5.088448176547862]]), (None, [[0.3281693992235359, 5.088448176547862], [-0.3388139002735513, 5.087750499089103]]), (None, [[-0.3388139002735513, 5.087750499089103], [-0.9999999999999991, 5.0]])]:
            c.line(points, id=object_id, zorder=9, color='#2563EB', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
        c.point([[-1.0, 5.0]], zorder=10, s=[50], facecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]], edgecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]])
        return c.save(output_path)
