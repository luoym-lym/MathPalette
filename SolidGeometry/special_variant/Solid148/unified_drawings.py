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
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / 'Solid148_C01.png'
    with Canvas(SOLID, xlim=(-0.12452579270404929, 5.132096044642034), ylim=(-1.1320960446420338, 4.124525792704049), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        for object_id, points in [('grid0', [[0.0, 0.0], [1.0, 0.0]]), ('grid1', [[1.0, 0.0], [1.0, 1.0]]), ('grid2', [[1.0, 1.0], [0.0, 1.0]]), ('grid3', [[0.0, 1.0], [0.0, 0.0]])]:
            c.line(points, id=object_id, zorder=3, clip_on=False, color='#DC2626')
        for object_id, points in [('grid4', [[1.0, 0.0], [2.0, 0.0]]), ('grid5', [[2.0, 0.0], [2.0, 1.0]]), ('grid6', [[2.0, 1.0], [1.0, 1.0]]), ('grid7', [[2.0, 0.0], [3.0, 0.0]]), ('grid8', [[3.0, 0.0], [3.0, 1.0]]), ('grid9', [[3.0, 1.0], [2.0, 1.0]])]:
            c.line(points, id=object_id, zorder=3, clip_on=False)
        c.line([[3.0, 1.0], [3.0, 2.0]], id='grid10', zorder=3, clip_on=False, color='#DC2626')
        c.line([[3.0, 2.0], [2.0, 2.0]], id='grid11', zorder=3, clip_on=False)
        c.line([[2.0, 2.0], [2.0, 1.0]], id='grid12', zorder=3, clip_on=False)
        for object_id, points in [('grid13', [[3.0, 1.0], [4.0, 1.0]]), ('grid14', [[4.0, 1.0], [4.0, 2.0]]), ('grid15', [[4.0, 2.0], [3.0, 2.0]])]:
            c.line(points, id=object_id, zorder=3, clip_on=False, color='#DC2626')
        for object_id, points in [('grid16', [[4.0, 2.0], [4.0, 3.0]]), ('grid17', [[4.0, 3.0], [3.0, 3.0]]), ('grid18', [[3.0, 3.0], [3.0, 2.0]]), ('grid19', [[4.0, 2.0], [5.0, 2.0]]), ('grid20', [[5.0, 2.0], [5.0, 3.0]]), ('grid21', [[5.0, 3.0], [4.0, 3.0]])]:
            c.line(points, id=object_id, zorder=3, clip_on=False)
        for object_id, text, anchor in [('position1', '1', (0.5, 0.5)), ('position2', '2', (1.5, 0.5)), ('position3', '3', (2.5, 0.5)), ('position4', '4', (2.5, 1.5)), ('position5', '5', (3.5, 1.5)), ('position6', '6', (3.5, 2.5)), ('position7', '7', (4.5, 2.5))]:
            c.text(text, anchor, id=object_id, rotation_mode='default', offset_pt=(0, 0), annotation_clip=None)
        return c.save(output_path)

def C02(output_path=None):
    if output_path is None:
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / 'Solid148_C02.png'
    with Canvas(SOLID, xlim=(-0.12452579270404929, 5.132096044642034), ylim=(-1.1320960446420338, 4.124525792704049), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        c.line([[0.0, 0.0], [1.0, 0.0]], id='grid0', zorder=3, clip_on=False)
        c.line([[1.0, 0.0], [1.0, 1.0]], id='grid1', zorder=3, clip_on=False, color='#DC2626')
        c.line([[1.0, 1.0], [0.0, 1.0]], id='grid2', zorder=3, clip_on=False)
        c.line([[0.0, 1.0], [0.0, 0.0]], id='grid3', zorder=3, clip_on=False)
        for object_id, points in [('grid4', [[1.0, 0.0], [2.0, 0.0]]), ('grid5', [[2.0, 0.0], [2.0, 1.0]]), ('grid6', [[2.0, 1.0], [1.0, 1.0]])]:
            c.line(points, id=object_id, zorder=3, clip_on=False, color='#DC2626')
        for object_id, points in [('grid7', [[2.0, 0.0], [3.0, 0.0]]), ('grid8', [[3.0, 0.0], [3.0, 1.0]]), ('grid9', [[3.0, 1.0], [2.0, 1.0]]), ('grid10', [[3.0, 1.0], [3.0, 2.0]]), ('grid11', [[3.0, 2.0], [2.0, 2.0]]), ('grid12', [[2.0, 2.0], [2.0, 1.0]]), ('grid13', [[3.0, 1.0], [4.0, 1.0]]), ('grid14', [[4.0, 1.0], [4.0, 2.0]])]:
            c.line(points, id=object_id, zorder=3, clip_on=False)
        for object_id, points in [('grid15', [[4.0, 2.0], [3.0, 2.0]]), ('grid16', [[4.0, 2.0], [4.0, 3.0]]), ('grid17', [[4.0, 3.0], [3.0, 3.0]]), ('grid18', [[3.0, 3.0], [3.0, 2.0]])]:
            c.line(points, id=object_id, zorder=3, clip_on=False, color='#DC2626')
        for object_id, points in [('grid19', [[4.0, 2.0], [5.0, 2.0]]), ('grid20', [[5.0, 2.0], [5.0, 3.0]]), ('grid21', [[5.0, 3.0], [4.0, 3.0]])]:
            c.line(points, id=object_id, zorder=3, clip_on=False)
        for object_id, text, anchor in [('position1', '1', (0.5, 0.5)), ('position2', '2', (1.5, 0.5)), ('position3', '3', (2.5, 0.5)), ('position4', '4', (2.5, 1.5)), ('position5', '5', (3.5, 1.5)), ('position6', '6', (3.5, 2.5)), ('position7', '7', (4.5, 2.5))]:
            c.text(text, anchor, id=object_id, rotation_mode='default', offset_pt=(0, 0), annotation_clip=None)
        return c.save(output_path)
