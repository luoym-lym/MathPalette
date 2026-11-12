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
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / 'Solid252_C01.png'
    with Canvas(SOLID, xlim=(-1.574038105676658, 2.074038105676658), ylim=(-1.3910254037844387, 2.257050807568877), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        c.line([[-1.0, 1.7320508075688772], [-0.5, 0.8660254037844386]], id='edge00', zorder=1)
        c.text('C', (-0.9145448267190434, 1.204038105676658), zorder=2, rotation_mode='default')
        c.line([[-1.0, 1.7320508075688772], [0.0, 1.7320508075688772]], id='edge01', zorder=1, color='#EA580C', linewidth=2.0)
        c.text('x', (-0.5, 1.9220508075688771), zorder=2, rotation_mode='default')
        c.line([[-0.5, 0.8660254037844386], [0.0, 1.7320508075688772]], id='edge02', zorder=1)
        c.line([[-0.5, 0.8660254037844386], [0.0, 0.0]], id='edge03', zorder=1)
        c.text('E', (-0.41454482671904336, 0.3380127018922193), zorder=2, rotation_mode='default')
        for object_id, points in [('edge04', [[-0.5, 0.8660254037844386], [0.5, 0.8660254037844386]]), ('edge05', [[0.0, 1.7320508075688772], [0.5, 0.8660254037844386]]), ('edge06', [[0.0, 1.7320508075688772], [1.0, 1.7320508075688772]])]:
            c.line(points, id=object_id, zorder=1)
        c.line([[-0.5, -0.8660254037844386], [0.0, 0.0]], id='edge07', zorder=1, color='#EA580C', linewidth=2.0)
        c.text('D', (-0.41454482671904336, -0.3380127018922193), zorder=2, rotation_mode='default')
        c.line([[-0.5, -0.8660254037844386], [0.5, -0.8660254037844386]], id='edge08', zorder=1)
        c.text('A', (0.0, -1.0560254037844385), zorder=2, rotation_mode='default')
        for object_id, points in [('edge09', [[0.0, 0.0], [0.5, 0.8660254037844386]]), ('edge10', [[0.0, 0.0], [0.5, -0.8660254037844386]]), ('edge11', [[0.0, 0.0], [1.0, 0.0]]), ('edge12', [[0.5, 0.8660254037844386], [1.0, 1.7320508075688772]]), ('edge13', [[0.5, 0.8660254037844386], [1.0, 0.0]]), ('edge14', [[0.5, -0.8660254037844386], [1.0, 0.0]]), ('edge15', [[0.5, -0.8660254037844386], [1.5, -0.8660254037844386]])]:
            c.line(points, id=object_id, zorder=1)
        c.text('B', (1.0, -1.0560254037844385), zorder=2, rotation_mode='default')
        c.line([[1.0, 0.0], [1.5, -0.8660254037844386]], id='edge16', zorder=1)
        return c.save(output_path)
