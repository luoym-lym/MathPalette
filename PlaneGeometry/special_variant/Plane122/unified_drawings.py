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
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / 'Plane122_C01.png'
    with Canvas(PLANE, xlim=(0.38156223083548646, 7.096678509905254), ylim=(0.49270227713178283, 7.20781855620155), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        c.line([[0.54, 1.82], [6.94, 5.82]], id='axis_l', linewidth=2.0)
        for object_id, points in [('P_dot', [[3.48, 6.62]]), ('A_dot', [[6.142921348314605, 2.359325842696628]]), ('B_dot', [[5.230561797752809, 1.7891011235955059]]), ('C_dot', [[4.011685393258427, 1.0273033707865171]])]:
            c.point(points, id=object_id)
        c.text('P', (3.48, 6.62), id='P_label', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(0, 16), annotation_clip=None)
        c.text('A', (6.142921348314605, 2.359325842696628), id='A_label', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(9, -15), annotation_clip=None)
        c.text('B', (5.230561797752809, 1.7891011235955059), id='B_label', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(-9, -15), annotation_clip=None)
        c.text('C', (4.011685393258427, 1.0273033707865171), id='C_label', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(0, -16), annotation_clip=None)
        c.text('l', (6.94, 5.82), id='l_label', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(-13, 8), annotation_clip=None)
        c.point([[3.48, 6.62]], zorder=10, s=[50], facecolors=[[0.1450980392156863, 0.38823529411764707, 0.9215686274509803, 1.0]], edgecolors=[[0.1450980392156863, 0.38823529411764707, 0.9215686274509803, 1.0]])
        c.point([[5.230561797752809, 1.7891011235955059]], zorder=10, s=[50], facecolors=[[0.1450980392156863, 0.38823529411764707, 0.9215686274509803, 1.0]], edgecolors=[[0.1450980392156863, 0.38823529411764707, 0.9215686274509803, 1.0]])
        c.line([[3.48, 6.62], [5.230561797752809, 1.7891011235955059]], zorder=9, color='#2563EB', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
        return c.save(output_path)

def C02(output_path=None):
    if output_path is None:
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / 'Plane122_C02.png'
    with Canvas(PLANE, xlim=(0.38156223083548646, 7.096678509905254), ylim=(0.49270227713178283, 7.20781855620155), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        c.line([[0.54, 1.82], [6.94, 5.82]], id='axis_l', linewidth=2.0)
        for object_id, points in [('P_dot', [[3.48, 6.62]]), ('A_dot', [[6.142921348314605, 2.359325842696628]]), ('B_dot', [[5.230561797752809, 1.7891011235955059]]), ('C_dot', [[4.011685393258427, 1.0273033707865171]])]:
            c.point(points, id=object_id)
        c.text('P', (3.48, 6.62), id='P_label', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(0, 16), annotation_clip=None)
        c.text('A', (6.142921348314605, 2.359325842696628), id='A_label', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(9, -15), annotation_clip=None)
        c.text('B', (5.230561797752809, 1.7891011235955059), id='B_label', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(-9, -15), annotation_clip=None)
        c.text('C', (4.011685393258427, 1.0273033707865171), id='C_label', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(0, -16), annotation_clip=None)
        c.text('l', (6.94, 5.82), id='l_label', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(-13, 8), annotation_clip=None)
        c.point([[3.48, 6.62]], zorder=10, s=[50], facecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]], edgecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]])
        c.point([[5.230561797752809, 1.7891011235955059]], zorder=10, s=[50], facecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]], edgecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]])
        c.line([[3.48, 6.62], [5.230561797752809, 1.7891011235955059]], zorder=9, color='#DC2626', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
        return c.save(output_path)

def C03(output_path=None):
    if output_path is None:
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / 'Plane122_C03.png'
    with Canvas(PLANE, xlim=(0.38156223083548646, 7.096678509905254), ylim=(0.49270227713178283, 7.20781855620155), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        c.line([[0.54, 1.82], [6.94, 5.82]], id='axis_l')
        for object_id, points in [('P_dot', [[3.48, 6.62]]), ('A_dot', [[6.142921348314605, 2.359325842696628]]), ('B_dot', [[5.230561797752809, 1.7891011235955059]]), ('C_dot', [[4.011685393258427, 1.0273033707865171]])]:
            c.point(points, id=object_id)
        c.text('P', (3.48, 6.62), id='P_label', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(0, 16), annotation_clip=None)
        c.text('A', (6.142921348314605, 2.359325842696628), id='A_label', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(9, -15), annotation_clip=None)
        c.text('B', (5.230561797752809, 1.7891011235955059), id='B_label', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(-9, -15), annotation_clip=None)
        c.text('C', (4.011685393258427, 1.0273033707865171), id='C_label', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(0, -16), annotation_clip=None)
        c.text('l', (6.94, 5.82), id='l_label', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(-13, 8), annotation_clip=None)
        c.point([[3.48, 6.62]], zorder=10, s=[50], facecolors=[[0.9176470588235294, 0.34509803921568627, 0.047058823529411764, 1.0]], edgecolors=[[0.9176470588235294, 0.34509803921568627, 0.047058823529411764, 1.0]])
        c.point([[4.011685393258427, 1.0273033707865171]], zorder=10, s=[50], facecolors=[[0.9176470588235294, 0.34509803921568627, 0.047058823529411764, 1.0]], edgecolors=[[0.9176470588235294, 0.34509803921568627, 0.047058823529411764, 1.0]])
        c.line([[3.48, 6.62], [4.011685393258427, 1.0273033707865171]], zorder=9, color='#EA580C', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
        return c.save(output_path)

def C04(output_path=None):
    if output_path is None:
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / 'Plane122_C04.png'
    with Canvas(PLANE, xlim=(0.38156223083548646, 7.096678509905254), ylim=(0.49270227713178283, 7.20781855620155), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        c.line([[0.54, 1.82], [6.94, 5.82]], id='axis_l', linewidth=2.0)
        for object_id, points in [('P_dot', [[3.48, 6.62]]), ('A_dot', [[6.142921348314605, 2.359325842696628]]), ('B_dot', [[5.230561797752809, 1.7891011235955059]]), ('C_dot', [[4.011685393258427, 1.0273033707865171]])]:
            c.point(points, id=object_id)
        c.text('P', (3.48, 6.62), id='P_label', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(0, 16), annotation_clip=None)
        c.text('A', (6.142921348314605, 2.359325842696628), id='A_label', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(9, -15), annotation_clip=None)
        c.text('B', (5.230561797752809, 1.7891011235955059), id='B_label', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(-9, -15), annotation_clip=None)
        c.text('C', (4.011685393258427, 1.0273033707865171), id='C_label', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(0, -16), annotation_clip=None)
        c.text('l', (6.94, 5.82), id='l_label', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(-13, 8), annotation_clip=None)
        c.point([[3.48, 6.62]], zorder=10, s=[50], facecolors=[[0.1450980392156863, 0.38823529411764707, 0.9215686274509803, 1.0]], edgecolors=[[0.1450980392156863, 0.38823529411764707, 0.9215686274509803, 1.0]])
        c.point([[4.011685393258427, 1.0273033707865171]], zorder=10, s=[50], facecolors=[[0.1450980392156863, 0.38823529411764707, 0.9215686274509803, 1.0]], edgecolors=[[0.1450980392156863, 0.38823529411764707, 0.9215686274509803, 1.0]])
        c.line([[3.48, 6.62], [4.011685393258427, 1.0273033707865171]], zorder=9, color='#2563EB', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
        return c.save(output_path)

def C05(output_path=None):
    if output_path is None:
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / 'Plane122_C05.png'
    with Canvas(PLANE, xlim=(0.38156223083548646, 7.096678509905254), ylim=(0.49270227713178283, 7.20781855620155), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        c.line([[0.54, 1.82], [6.94, 5.82]], id='axis_l')
        for object_id, points in [('P_dot', [[3.48, 6.62]]), ('A_dot', [[6.142921348314605, 2.359325842696628]]), ('B_dot', [[5.230561797752809, 1.7891011235955059]]), ('C_dot', [[4.011685393258427, 1.0273033707865171]])]:
            c.point(points, id=object_id)
        c.text('P', (3.48, 6.62), id='P_label', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(0, 16), annotation_clip=None)
        c.text('A', (6.142921348314605, 2.359325842696628), id='A_label', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(9, -15), annotation_clip=None)
        c.text('B', (5.230561797752809, 1.7891011235955059), id='B_label', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(-9, -15), annotation_clip=None)
        c.text('C', (4.011685393258427, 1.0273033707865171), id='C_label', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(0, -16), annotation_clip=None)
        c.text('l', (6.94, 5.82), id='l_label', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(-13, 8), annotation_clip=None)
        c.point([[3.48, 6.62]], zorder=10, s=[50], facecolors=[[0.9176470588235294, 0.34509803921568627, 0.047058823529411764, 1.0]], edgecolors=[[0.9176470588235294, 0.34509803921568627, 0.047058823529411764, 1.0]])
        c.point([[4.011685393258427, 1.0273033707865171]], zorder=10, s=[50], facecolors=[[0.9176470588235294, 0.34509803921568627, 0.047058823529411764, 1.0]], edgecolors=[[0.9176470588235294, 0.34509803921568627, 0.047058823529411764, 1.0]])
        c.line([[3.48, 6.62], [4.011685393258427, 1.0273033707865171]], zorder=9, color='#EA580C', solid_capstyle='butt')
        return c.save(output_path)
