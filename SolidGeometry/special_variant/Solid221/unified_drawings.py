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
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / 'Solid221_C01.png'
    with Canvas(SOLID, xlim=(-0.628596084945126, 4.631119843366685), ylim=(-0.13491308342715014, 5.124802844884661), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        c.line([[1.0, 1.0], [2.0, 1.0]], id='line_0', zorder=3, clip_on=False, color='#DC2626', linewidth=2.0, solid_capstyle='butt', simplify=False)
        c.line([[2.0, 1.0], [2.0, 2.0]], id='line_1', zorder=3, clip_on=False, color='#DC2626', linewidth=2.0, solid_capstyle='butt', simplify=False)
        c.line([[1.0, 2.0], [2.0, 2.0]], id='line_2', zorder=3, clip_on=False, simplify=False)
        c.line([[1.0, 1.0], [1.0, 2.0]], id='line_3', zorder=3, clip_on=False, color='#DC2626', linewidth=2.0, solid_capstyle='butt', simplify=False)
        c.line([[2.0, 2.0], [2.0, 3.0]], id='line_4', zorder=3, clip_on=False, color='#DC2626', linewidth=2.0, solid_capstyle='butt', simplify=False)
        c.line([[1.0, 3.0], [2.0, 3.0]], id='line_5', zorder=3, clip_on=False, simplify=False)
        for object_id, points in [('line_6', [[1.0, 2.0], [1.0, 3.0]]), ('line_7', [[2.0, 3.0], [2.0, 4.0]]), ('line_8', [[1.0, 4.0], [2.0, 4.0]]), ('line_9', [[1.0, 3.0], [1.0, 4.0]])]:
            c.line(points, id=object_id, zorder=3, clip_on=False, color='#DC2626', linewidth=2.0, solid_capstyle='butt', simplify=False)
        for object_id, points in [('line_10', [[2.0, 2.0], [3.0, 2.0]]), ('line_11', [[3.0, 2.0], [3.0, 3.0]]), ('line_12', [[2.0, 3.0], [3.0, 3.0]])]:
            c.line(points, id=object_id, zorder=3, clip_on=False, color='#2563EB', linewidth=2.0, solid_capstyle='butt', simplify=False)
        for object_id, points in [('line_13', [[2.0, 4.0], [2.0, 5.0]]), ('line_14', [[1.0, 5.0], [2.0, 5.0]]), ('line_15', [[1.0, 4.0], [1.0, 5.0]]), ('line_16', [[0.0, 3.0], [1.0, 3.0]]), ('line_17', [[0.0, 4.0], [1.0, 4.0]]), ('line_18', [[0.0, 3.0], [0.0, 4.0]]), ('line_19', [[3.0, 3.0], [3.0, 4.0]]), ('line_20', [[2.0, 4.0], [3.0, 4.0]]), ('line_21', [[0.0, 2.0], [1.0, 2.0]]), ('line_22', [[0.0, 2.0], [0.0, 3.0]]), ('line_23', [[3.0, 2.0], [4.0, 2.0]]), ('line_24', [[4.0, 2.0], [4.0, 3.0]]), ('line_25', [[3.0, 3.0], [4.0, 3.0]]), ('line_26', [[0.0, 1.0], [1.0, 1.0]]), ('line_27', [[0.0, 1.0], [0.0, 2.0]]), ('line_28', [[2.0, 1.0], [3.0, 1.0]]), ('line_29', [[3.0, 1.0], [3.0, 2.0]]), ('line_30', [[1.0, 0.0], [2.0, 0.0]]), ('line_31', [[2.0, 0.0], [2.0, 1.0]]), ('line_32', [[1.0, 0.0], [1.0, 1.0]])]:
            c.line(points, id=object_id, zorder=3, clip_on=False, simplify=False)
        for object_id, text, anchor in [('label_0', 'A', (1.5, 4.5)), ('label_1', 'B', (0.5, 3.5)), ('label_2', 'C', (2.5, 3.5)), ('label_3', 'D', (0.5, 2.5)), ('label_4', 'E', (3.5, 2.5)), ('label_5', 'F', (0.5, 1.5)), ('label_6', 'G', (2.5, 1.5)), ('label_7', 'H', (1.5, 0.5))]:
            c.text(text, anchor, id=object_id, rotation_mode='default', offset_pt=(0, 0), annotation_clip=None)
        return c.save(output_path)
