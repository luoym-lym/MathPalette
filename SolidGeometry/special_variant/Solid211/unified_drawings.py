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
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / 'Solid211_C01.png'
    with Canvas(SOLID, xlim=(-1.124802844884659, 4.13491308342715), ylim=(-1.6311198433666836, 3.628596084945125), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        for object_id, vertices, codes in [('face3', [[1.0, 1.0], [2.0, 1.0], [2.0, 2.0], [1.0, 2.0], [1.0, 1.0]], [1, 2, 2, 2, 79]), ('face2', [[0.0, 0.0], [1.0, 0.0], [1.0, 1.0], [0.0, 1.0], [0.0, 0.0]], [1, 2, 2, 2, 79]), ('face1', [[2.0, 1.0], [3.0, 1.0], [3.0, 2.0], [2.0, 2.0], [2.0, 1.0]], [1, 2, 2, 2, 79]), ('face0', [[0.0, 1.0], [1.0, 1.0], [1.0, 2.0], [0.0, 2.0], [0.0, 1.0]], [1, 2, 2, 2, 79])]:
            c.path(vertices, codes, id=object_id, zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 1.0), linewidth=0.0, capstyle='butt')
        c.line([[0.0, 1.0], [1.0, 1.0]], id='line_4', zorder=3, clip_on=False, color='#DC2626', linestyle=(0.0, [4.0, 3.0]))
        c.line([[1.0, 1.0], [1.0, 2.0]], id='line_5', zorder=3, clip_on=False, color='#DC2626', linestyle=(0.0, [4.0, 3.0]))
        for object_id, points in [('line_6', [[0.0, 2.0], [1.0, 2.0]]), ('line_7', [[0.0, 1.0], [0.0, 2.0]]), ('line_8', [[1.0, 2.0], [2.0, 2.0]])]:
            c.line(points, id=object_id, zorder=3, clip_on=False)
        for object_id, points in [('line_9', [[2.0, 2.0], [2.0, 3.0]]), ('line_10', [[1.0, 3.0], [2.0, 3.0]]), ('line_11', [[1.0, 2.0], [1.0, 3.0]])]:
            c.line(points, id=object_id, zorder=3, clip_on=False, linestyle=(0.0, [4.0, 3.0]))
        for object_id, points in [('line_12', [[2.0, 1.0], [3.0, 1.0]]), ('line_13', [[3.0, 1.0], [3.0, 2.0]]), ('line_14', [[2.0, 2.0], [3.0, 2.0]])]:
            c.line(points, id=object_id, zorder=3, clip_on=False)
        c.line([[2.0, 1.0], [2.0, 2.0]], id='line_15', zorder=3, clip_on=False, color='#DC2626', linestyle=(0.0, [4.0, 3.0]))
        for object_id, points in [('line_16', [[0.0, 0.0], [1.0, 0.0]]), ('line_17', [[1.0, 0.0], [1.0, 1.0]]), ('line_18', [[0.0, 0.0], [0.0, 1.0]])]:
            c.line(points, id=object_id, zorder=3, clip_on=False)
        for object_id, points in [('line_19', [[3.0, 1.0], [4.0, 1.0]]), ('line_20', [[4.0, 1.0], [4.0, 2.0]]), ('line_21', [[3.0, 2.0], [4.0, 2.0]]), ('line_22', [[-1.0, 1.0], [0.0, 1.0]]), ('line_23', [[-1.0, 2.0], [0.0, 2.0]]), ('line_24', [[-1.0, 1.0], [-1.0, 2.0]])]:
            c.line(points, id=object_id, zorder=3, clip_on=False, linestyle=(0.0, [4.0, 3.0]))
        c.line([[1.0, 1.0], [2.0, 1.0]], id='line_25', zorder=3, clip_on=False)
        for object_id, points in [('line_26', [[2.0, 0.0], [3.0, 0.0]]), ('line_27', [[3.0, 0.0], [3.0, 1.0]]), ('line_28', [[2.0, 0.0], [2.0, 1.0]]), ('line_29', [[-1.0, 0.0], [0.0, 0.0]]), ('line_30', [[-1.0, 0.0], [-1.0, 1.0]]), ('line_31', [[0.0, 3.0], [1.0, 3.0]]), ('line_32', [[0.0, 2.0], [0.0, 3.0]]), ('line_33', [[3.0, 2.0], [3.0, 3.0]]), ('line_34', [[2.0, 3.0], [3.0, 3.0]]), ('line_35', [[1.0, 0.0], [2.0, 0.0]]), ('line_36', [[0.0, -1.0], [1.0, -1.0]]), ('line_37', [[1.0, -1.0], [1.0, 0.0]]), ('line_38', [[0.0, -1.0], [0.0, 0.0]])]:
            c.line(points, id=object_id, zorder=3, clip_on=False, linestyle=(0.0, [4.0, 3.0]))
        for object_id, text, anchor in [('label_0', '⑥', (1.5, 2.5)), ('label_1', '④', (3.5, 1.5)), ('label_2', '⑧', (-0.5, 1.5)), ('label_3', '③', (2.5, 0.5)), ('label_4', '⑨', (-0.5, 0.5)), ('label_5', '⑦', (0.5, 2.5)), ('label_6', '⑤', (2.5, 2.5)), ('label_7', '②', (1.5, 0.5)), ('label_8', '①', (0.5, -0.5))]:
            c.text(text, anchor, id=object_id, rotation_mode='default', offset_pt=(0, 0), annotation_clip=None)
        return c.save(output_path)
