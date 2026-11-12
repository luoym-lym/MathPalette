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
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / 'Solid254_C01.png'
    with Canvas(SOLID, xlim=(-2.025, 2.525), ylim=(-1.8419872981077807, 2.708012701892219), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        c.line([[-1.5, 0.8660254037844386], [-1.0, 0.0]], id='edge00', zorder=1, color='#DC2626', linewidth=3.0)
        c.text('x', (-1.4145448267190432, 0.3380127018922193), zorder=2, rotation_mode='default')
        for object_id, points in [('edge01', [[-1.5, 0.8660254037844386], [-0.5, 0.8660254037844386]]), ('edge02', [[-1.0, 0.0], [-0.5, 0.8660254037844386]]), ('edge03', [[-1.0, 0.0], [0.0, 0.0]])]:
            c.line(points, id=object_id, zorder=1)
        c.text('C', (-0.5, -0.19), zorder=2, rotation_mode='default')
        for object_id, points in [('edge04', [[-0.5, 0.8660254037844386], [0.0, 1.7320508075688772]]), ('edge05', [[-0.5, 0.8660254037844386], [0.0, 0.0]]), ('edge06', [[-0.5, 0.8660254037844386], [0.5, 0.8660254037844386]]), ('edge07', [[0.0, 1.7320508075688772], [0.5, 0.8660254037844386]]), ('edge08', [[0.0, 0.0], [0.5, 0.8660254037844386]]), ('edge09', [[0.0, 0.0], [0.5, -0.8660254037844386]]), ('edge10', [[0.0, 0.0], [1.0, 0.0]]), ('edge11', [[0.5, 0.8660254037844386], [1.0, 0.0]])]:
            c.line(points, id=object_id, zorder=1)
        c.line([[0.5, 0.8660254037844386], [1.5, 0.8660254037844386]], id='edge12', zorder=1, color='#DC2626', linewidth=3.0)
        c.text('E', (1.0, 1.0560254037844385), zorder=2, rotation_mode='default')
        c.line([[0.5, -0.8660254037844386], [1.0, 0.0]], id='edge13', zorder=1)
        c.text('D', (0.9145448267190434, -0.5280127018922193), zorder=2, rotation_mode='default')
        c.line([[1.0, 0.0], [1.5, 0.8660254037844386]], id='edge14', zorder=1)
        c.line([[1.0, 0.0], [2.0, 0.0]], id='edge15', zorder=1)
        c.text('A', (1.5, -0.19), zorder=2, rotation_mode='default')
        c.line([[1.5, 0.8660254037844386], [2.0, 0.0]], id='edge16', zorder=1)
        c.text('B', (1.9145448267190432, 0.5280127018922193), zorder=2, rotation_mode='default')
        c.point([[-1.5, 0.8660254037844386]], zorder=10, s=[50], facecolors=[[0.1450980392156863, 0.38823529411764707, 0.9215686274509803, 1.0]], edgecolors=[[0.1450980392156863, 0.38823529411764707, 0.9215686274509803, 1.0]])
        c.point([[1.5, 0.8660254037844386]], zorder=10, s=[50], facecolors=[[0.1450980392156863, 0.38823529411764707, 0.9215686274509803, 1.0]], edgecolors=[[0.1450980392156863, 0.38823529411764707, 0.9215686274509803, 1.0]])
        return c.save(output_path)
