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
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / 'Solid253_C01.png'
    with Canvas(SOLID, xlim=(-2.007050807568877, 2.507050807568877), ylim=(-2.257050807568877, 2.257050807568877), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        c.line([[-1.0, 0.0], [-0.5, 0.8660254037844386]], id='edge00', zorder=1)
        c.text('D', (-0.9145448267190434, 0.5280127018922193), zorder=2, rotation_mode='default')
        c.line([[-1.0, 0.0], [0.0, 0.0]], id='edge01', zorder=1)
        c.text('C', (-0.5, -0.19), zorder=2, rotation_mode='default')
        for object_id, points in [('edge02', [[-0.5, 0.8660254037844386], [0.0, 0.0]]), ('edge03', [[-0.5, 0.8660254037844386], [0.5, 0.8660254037844386]]), ('edge04', [[0.0, 0.0], [0.5, 0.8660254037844386]])]:
            c.line(points, id=object_id, zorder=1)
        c.line([[0.0, 0.0], [0.5, -0.8660254037844386]], id='edge05', zorder=1, color='#2563EB', linewidth=2.0)
        c.text('x', (0.08545517328095664, -0.5280127018922193), zorder=2, rotation_mode='default')
        for object_id, points in [('edge06', [[0.0, 0.0], [1.0, 0.0]]), ('edge07', [[0.5, 0.8660254037844386], [1.0, 1.7320508075688772]]), ('edge08', [[0.5, 0.8660254037844386], [1.0, 0.0]]), ('edge09', [[0.5, 0.8660254037844386], [1.5, 0.8660254037844386]]), ('edge10', [[1.0, 1.7320508075688772], [1.5, 0.8660254037844386]])]:
            c.line(points, id=object_id, zorder=1)
        c.text('E', (1.4145448267190432, 1.394038105676658), zorder=2, rotation_mode='default')
        for object_id, points in [('edge11', [[0.5, -0.8660254037844386], [1.0, 0.0]]), ('edge12', [[0.5, -0.8660254037844386], [1.0, -1.7320508075688772]]), ('edge13', [[0.5, -0.8660254037844386], [1.5, -0.8660254037844386]]), ('edge14', [[1.0, 0.0], [1.5, 0.8660254037844386]])]:
            c.line(points, id=object_id, zorder=1)
        c.text('B', (1.4145448267190432, 0.3380127018922193), zorder=2, rotation_mode='default')
        c.line([[1.0, 0.0], [1.5, -0.8660254037844386]], id='edge15', zorder=1)
        c.line([[1.0, -1.7320508075688772], [1.5, -0.8660254037844386]], id='edge16', zorder=1, color='#2563EB', linewidth=2.0)
        c.text('A', (1.4145448267190432, -1.394038105676658), zorder=2, rotation_mode='default')
        return c.save(output_path)

def C02(output_path=None):
    if output_path is None:
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / 'Solid253_C02.png'
    with Canvas(SOLID, xlim=(-2.007050807568877, 2.507050807568877), ylim=(-2.257050807568877, 2.257050807568877), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        c.path([[-0.9999999999999994, -4.440892098500626e-16], [-0.8349999999999994, 0.2857883832488643]], [1, 2], id='edge00', zorder=1, edgecolor=(0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0), linewidth=3.0, joinstyle='round', fill=False)
        c.path([[-0.8349999999999994, 0.2857883832488643], [-0.4999999999999995, 0.866025403784438]], [1, 2], id='edge00', zorder=1, joinstyle='round', fill=False)
        c.text('D', (-0.9145448267190434, 0.5280127018922193), zorder=2, rotation_mode='default')
        c.line([[-1.0, 0.0], [0.0, 0.0]], id='edge01', zorder=1)
        c.text('C', (-0.5, -0.19), zorder=2, rotation_mode='default')
        for object_id, points in [('edge02', [[-0.5, 0.8660254037844386], [0.0, 0.0]]), ('edge03', [[-0.5, 0.8660254037844386], [0.5, 0.8660254037844386]]), ('edge04', [[0.0, 0.0], [0.5, 0.8660254037844386]])]:
            c.line(points, id=object_id, zorder=1)
        c.path([[4.440892098500626e-16, -4.440892098500626e-16], [0.33500000000000046, -0.5802370205355742]], [1, 2], id='edge05', zorder=1, joinstyle='round', fill=False)
        c.path([[0.33500000000000046, -0.5802370205355742], [0.5000000000000004, -0.8660254037844389]], [1, 2], id='edge05', zorder=1, edgecolor=(0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0), linewidth=3.0, joinstyle='round', fill=False)
        c.text('x', (0.08545517328095664, -0.5280127018922193), zorder=2, rotation_mode='default')
        for object_id, points in [('edge06', [[0.0, 0.0], [1.0, 0.0]]), ('edge07', [[0.5, 0.8660254037844386], [1.0, 1.7320508075688772]]), ('edge08', [[0.5, 0.8660254037844386], [1.0, 0.0]]), ('edge09', [[0.5, 0.8660254037844386], [1.5, 0.8660254037844386]]), ('edge10', [[1.0, 1.7320508075688772], [1.5, 0.8660254037844386]])]:
            c.line(points, id=object_id, zorder=1)
        c.text('E', (1.4145448267190432, 1.394038105676658), zorder=2, rotation_mode='default')
        for object_id, points in [('edge11', [[0.5, -0.8660254037844386], [1.0, 0.0]]), ('edge12', [[0.5, -0.8660254037844386], [1.0, -1.7320508075688772]]), ('edge13', [[0.5, -0.8660254037844386], [1.5, -0.8660254037844386]]), ('edge14', [[1.0, 0.0], [1.5, 0.8660254037844386]])]:
            c.line(points, id=object_id, zorder=1)
        c.text('B', (1.4145448267190432, 0.3380127018922193), zorder=2, rotation_mode='default')
        c.line([[1.0, 0.0], [1.5, -0.8660254037844386]], id='edge15', zorder=1)
        c.line([[1.0, -1.7320508075688772], [1.5, -0.8660254037844386]], id='edge16', zorder=1)
        c.text('A', (1.4145448267190432, -1.394038105676658), zorder=2, rotation_mode='default')
        return c.save(output_path)
