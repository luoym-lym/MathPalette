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
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / 'Plane200_C01.png'
    with Canvas(PLANE, xlim=(-1.4878458591050734, 18.994709910248375), ylim=(-8.505176642386582, 11.977379126966868), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        c.circle([0.0, 0.0], 1.0, id='tri0', edgecolor=(0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0))
        c.circle([2.0, 0.0], 1.0, id='tri1')
        c.circle([4.0, 0.0], 1.0, id='tri2', edgecolor=(0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0))
        c.circle([1.0, 1.7320508075688772], 1.0, id='tri3')
        c.circle([3.0, 1.7320508075688772], 1.0, id='tri4')
        c.circle([2.0, 3.4641016151377544], 1.0, id='tri5', edgecolor=(0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0))
        for object_id, center, radius in [('hex0', [17.5, 1.7320508075688772], 1.0), ('hex1', [16.5, 3.4641016151377544], 1.0), ('hex2', [14.5, 3.4641016151377544], 1.0), ('hex3', [13.5, 1.7320508075688774], 1.0), ('hex4', [14.5, 4.440892098500626e-16], 1.0), ('hex5', [16.5, 0.0], 1.0)]:
            c.circle(center, radius, id=object_id)
        c.path([[6.5, 1.2320508075688772], [10.5, 1.2320508075688772], [10.5, 0.7320508075688772], [11.5, 1.7320508075688772], [10.5, 2.732050807568877], [10.5, 2.232050807568877], [6.5, 2.232050807568877], [6.5, 1.2320508075688772]], [1, 2, 2, 2, 2, 2, 2, 79], id='transformation_arrow', capstyle='butt')
        return c.save(output_path)

def C02(output_path=None):
    if output_path is None:
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / 'Plane200_C02.png'
    with Canvas(PLANE, xlim=(-1.4878458591050734, 18.994709910248375), ylim=(-8.505176642386582, 11.977379126966868), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        c.circle([0.0, 0.0], 1.0, id='tri0')
        c.circle([2.0, 0.0], 1.0, id='tri1', edgecolor=(0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0))
        c.circle([4.0, 0.0], 1.0, id='tri2')
        c.circle([1.0, 1.7320508075688772], 1.0, id='tri3', edgecolor=(0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0))
        c.circle([3.0, 1.7320508075688772], 1.0, id='tri4', edgecolor=(0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0))
        for object_id, center, radius in [('tri5', [2.0, 3.4641016151377544], 1.0), ('hex0', [17.5, 1.7320508075688772], 1.0), ('hex1', [16.5, 3.4641016151377544], 1.0), ('hex2', [14.5, 3.4641016151377544], 1.0), ('hex3', [13.5, 1.7320508075688774], 1.0), ('hex4', [14.5, 4.440892098500626e-16], 1.0), ('hex5', [16.5, 0.0], 1.0)]:
            c.circle(center, radius, id=object_id)
        c.path([[6.5, 1.2320508075688772], [10.5, 1.2320508075688772], [10.5, 0.7320508075688772], [11.5, 1.7320508075688772], [10.5, 2.732050807568877], [10.5, 2.232050807568877], [6.5, 2.232050807568877], [6.5, 1.2320508075688772]], [1, 2, 2, 2, 2, 2, 2, 79], id='transformation_arrow', capstyle='butt')
        return c.save(output_path)

def C03(output_path=None):
    if output_path is None:
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / 'Plane200_C03.png'
    with Canvas(PLANE, xlim=(-1.4878458591050734, 18.994709910248375), ylim=(-8.505176642386582, 11.977379126966868), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        for object_id, center, radius in [('tri0', [0.0, 0.0], 1.0), ('tri1', [2.0, 0.0], 1.0), ('tri2', [4.0, 0.0], 1.0), ('tri3', [1.0, 1.7320508075688772], 1.0), ('tri4', [3.0, 1.7320508075688772], 1.0), ('tri5', [2.0, 3.4641016151377544], 1.0), ('hex0', [17.5, 1.7320508075688772], 1.0)]:
            c.circle(center, radius, id=object_id)
        c.circle([16.5, 3.4641016151377544], 1.0, id='hex1', edgecolor=(0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0))
        c.circle([14.5, 3.4641016151377544], 1.0, id='hex2', edgecolor=(0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0))
        c.circle([13.5, 1.7320508075688774], 1.0, id='hex3')
        c.circle([14.5, 4.440892098500626e-16], 1.0, id='hex4', edgecolor=(0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0))
        c.circle([16.5, 0.0], 1.0, id='hex5', edgecolor=(0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0))
        c.path([[6.5, 1.2320508075688772], [10.5, 1.2320508075688772], [10.5, 0.7320508075688772], [11.5, 1.7320508075688772], [10.5, 2.732050807568877], [10.5, 2.232050807568877], [6.5, 2.232050807568877], [6.5, 1.2320508075688772]], [1, 2, 2, 2, 2, 2, 2, 79], id='transformation_arrow', capstyle='butt')
        return c.save(output_path)

def C04(output_path=None):
    if output_path is None:
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / 'Plane200_C04.png'
    with Canvas(PLANE, xlim=(-1.4878458591050734, 18.994709910248375), ylim=(-8.505176642386582, 11.977379126966868), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        c.circle([0.0, 0.0], 1.0, id='tri0')
        c.circle([2.0, 0.0], 1.0, id='tri1', edgecolor=(0.1450980392156863, 0.38823529411764707, 0.9215686274509803, 1.0))
        c.circle([4.0, 0.0], 1.0, id='tri2')
        c.circle([1.0, 1.7320508075688772], 1.0, id='tri3', edgecolor=(0.1450980392156863, 0.38823529411764707, 0.9215686274509803, 1.0))
        c.circle([3.0, 1.7320508075688772], 1.0, id='tri4', edgecolor=(0.1450980392156863, 0.38823529411764707, 0.9215686274509803, 1.0))
        for object_id, center, radius in [('tri5', [2.0, 3.4641016151377544], 1.0), ('hex0', [17.5, 1.7320508075688772], 1.0), ('hex1', [16.5, 3.4641016151377544], 1.0), ('hex2', [14.5, 3.4641016151377544], 1.0), ('hex3', [13.5, 1.7320508075688774], 1.0), ('hex4', [14.5, 4.440892098500626e-16], 1.0), ('hex5', [16.5, 0.0], 1.0)]:
            c.circle(center, radius, id=object_id)
        c.path([[6.5, 1.2320508075688772], [10.5, 1.2320508075688772], [10.5, 0.7320508075688772], [11.5, 1.7320508075688772], [10.5, 2.732050807568877], [10.5, 2.232050807568877], [6.5, 2.232050807568877], [6.5, 1.2320508075688772]], [1, 2, 2, 2, 2, 2, 2, 79], id='transformation_arrow', capstyle='butt')
        return c.save(output_path)

def C05(output_path=None):
    if output_path is None:
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / 'Plane200_C05.png'
    with Canvas(PLANE, xlim=(-1.4878458591050734, 18.994709910248375), ylim=(-8.505176642386582, 11.977379126966868), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        c.circle([0.0, 0.0], 1.0, id='tri0', edgecolor=(0.08627450980392157, 0.6392156862745098, 0.2901960784313726, 1.0))
        c.circle([2.0, 0.0], 1.0, id='tri1')
        c.circle([4.0, 0.0], 1.0, id='tri2', edgecolor=(0.08627450980392157, 0.6392156862745098, 0.2901960784313726, 1.0))
        c.circle([1.0, 1.7320508075688772], 1.0, id='tri3')
        c.circle([3.0, 1.7320508075688772], 1.0, id='tri4')
        c.circle([2.0, 3.4641016151377544], 1.0, id='tri5', edgecolor=(0.08627450980392157, 0.6392156862745098, 0.2901960784313726, 1.0))
        for object_id, center, radius in [('hex0', [17.5, 1.7320508075688772], 1.0), ('hex1', [16.5, 3.4641016151377544], 1.0), ('hex2', [14.5, 3.4641016151377544], 1.0), ('hex3', [13.5, 1.7320508075688774], 1.0), ('hex4', [14.5, 4.440892098500626e-16], 1.0), ('hex5', [16.5, 0.0], 1.0)]:
            c.circle(center, radius, id=object_id)
        c.path([[6.5, 1.2320508075688772], [10.5, 1.2320508075688772], [10.5, 0.7320508075688772], [11.5, 1.7320508075688772], [10.5, 2.732050807568877], [10.5, 2.232050807568877], [6.5, 2.232050807568877], [6.5, 1.2320508075688772]], [1, 2, 2, 2, 2, 2, 2, 79], id='transformation_arrow', capstyle='butt')
        return c.save(output_path)

def C06(output_path=None):
    if output_path is None:
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / 'Plane200_C06.png'
    with Canvas(PLANE, xlim=(-1.4878458591050734, 18.994709910248375), ylim=(-8.505176642386582, 11.977379126966868), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        c.circle([0.0, 0.0], 1.0, id='tri0')
        for object_id, center, radius in [('tri1', [2.0, 0.0], 1.0), ('tri2', [4.0, 0.0], 1.0), ('tri3', [1.0, 1.7320508075688772], 1.0), ('tri4', [3.0, 1.7320508075688772], 1.0)]:
            c.circle(center, radius, id=object_id, edgecolor=(0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0))
        for object_id, center, radius in [('tri5', [2.0, 3.4641016151377544], 1.0), ('hex0', [17.5, 1.7320508075688772], 1.0), ('hex1', [16.5, 3.4641016151377544], 1.0), ('hex2', [14.5, 3.4641016151377544], 1.0), ('hex3', [13.5, 1.7320508075688774], 1.0), ('hex4', [14.5, 4.440892098500626e-16], 1.0), ('hex5', [16.5, 0.0], 1.0)]:
            c.circle(center, radius, id=object_id)
        c.path([[6.5, 1.2320508075688772], [10.5, 1.2320508075688772], [10.5, 0.7320508075688772], [11.5, 1.7320508075688772], [10.5, 2.732050807568877], [10.5, 2.232050807568877], [6.5, 2.232050807568877], [6.5, 1.2320508075688772]], [1, 2, 2, 2, 2, 2, 2, 79], id='transformation_arrow', capstyle='butt')
        return c.save(output_path)
