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
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / 'Plane411_C01.png'
    with Canvas(PLANE, xlim=(-1.804695903400967, 22.61336199136393), ylim=(-11.078162338586152, 13.339895556178744), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        c.path([[0.0, 0.0], [2.0, 0.0], [1.5, 0.8660254037844386], [2.0, 1.7320508075688772], [0.0, 1.7320508075688772], [0.5, 0.8660254037844386], [0.0, 0.0]], [1, 2, 2, 2, 2, 2, 79], id='option0', capstyle='butt')
        c.path([[5.0, 1.0], [6.732050807568877, 0.0], [8.464101615137753, 1.0], [6.732050807568877, 2.0], [5.0, 1.0]], [1, 2, 2, 2, 79], id='option1', capstyle='butt')
        c.path([[10.0, 0.0], [10.866025403784437, 0.5], [10.866025403784437, 0.0], [12.598076211353316, 1.0], [10.866025403784437, 2.0], [10.866025403784437, 1.5], [10.0, 2.0], [10.0, 0.0]], [1, 2, 2, 2, 2, 2, 2, 79], id='option2', edgecolor=(0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0), capstyle='butt')
        c.path([[15.0, 0.0], [15.0, 2.0], [16.039230484541328, 1.4], [17.598076211353316, 2.3], [17.598076211353316, 0.3], [16.558845726811988, 0.9], [15.0, 0.0]], [1, 2, 2, 2, 2, 2, 79], id='option3', capstyle='butt')
        c.path([[20.0, 0.0], [22.0, 0.0], [22.0, 1.6], [20.0, 1.6], [20.0, 0.0]], [1, 2, 2, 2, 79], id='option4', capstyle='butt')
        for object_id, text, anchor in [('label0', 'A', (-1.0, 1.0)), ('label1', 'B', (4.0, 1.0)), ('label2', 'C', (9.0, 1.0)), ('label3', 'D', (14.0, 1.0)), ('label4', 'E', (19.0, 1.0))]:
            c.text(text, anchor, id=object_id, rotation_mode='default', offset_pt=(0, 0), annotation_clip=None)
        c.line([[10.866025403784437, 1.5], [10.866025403784437, 0.5]], zorder=9, color='#2563EB', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
        return c.save(output_path)
