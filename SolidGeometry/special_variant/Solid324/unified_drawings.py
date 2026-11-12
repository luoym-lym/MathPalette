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
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / 'Solid324_C01.png'
    with Canvas(SOLID, xlim=(-4.721292885447766, 4.721292885447766), ylim=(-3.2429949789043433, 6.199590791991188), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        c.line([[-2.4000000000000004, -1.35], [-4.16, -2.3400000000000003]], id='frame_0', zorder=3, clip_on=False)
        c.line([[-0.8318669805761163, -0.3933475900869043], [-0.7681330194238838, -0.5066524099130957]], id='frame_1', zorder=3, clip_on=False)
        c.line([[-1.6318669805761166, -0.8433475900869044], [-1.5681330194238838, -0.9566524099130957]], id='frame_2', zorder=3, clip_on=False, color='#DC2626', linewidth=2.0)
        for object_id, points in [('frame_3', [[-2.4318669805761166, -1.2933475900869045], [-2.3681330194238837, -1.4066524099130955]]), ('frame_4', [[-3.231866980576117, -1.7433475900869044], [-3.1681330194238835, -1.8566524099130957]]), ('frame_5', [[-4.16, -2.3400000000000003], [-4.033621547116941, -2.1771243214998504]]), ('frame_6', [[-4.16, -2.3400000000000003], [-3.955179748775732, -2.316576407439778]]), ('frame_7', [[2.4000000000000004, -1.35], [4.16, -2.3400000000000003]]), ('frame_8', [[0.7681330194238837, -0.5066524099130957], [0.8318669805761163, -0.3933475900869043]])]:
            c.line(points, id=object_id, zorder=3, clip_on=False)
        c.line([[1.5681330194238838, -0.9566524099130959], [1.6318669805761166, -0.8433475900869043]], id='frame_9', zorder=3, clip_on=False, color='#DC2626', linewidth=2.0)
        for object_id, points in [('frame_10', [[2.3681330194238837, -1.4066524099130957], [2.4318669805761166, -1.2933475900869045]]), ('frame_11', [[3.168133019423884, -1.8566524099130957], [3.2318669805761164, -1.7433475900869044]]), ('frame_12', [[4.16, -2.3400000000000003], [3.9551797487757314, -2.316576407439778]]), ('frame_13', [[4.16, -2.3400000000000003], [4.033621547116941, -2.1771243214998504]]), ('frame_14', [[0.0, 3.0], [0.0, 5.2]]), ('frame_15', [[0.06499999999999999, 1.0], [-0.06499999999999999, 1.0]])]:
            c.line(points, id=object_id, zorder=3, clip_on=False)
        c.line([[0.06499999999999999, 2.0], [-0.06499999999999999, 2.0]], id='frame_16', zorder=3, clip_on=False, color='#DC2626', linewidth=2.0)
        for object_id, points in [('frame_17', [[0.06499999999999999, 3.0], [-0.06499999999999999, 3.0]]), ('frame_18', [[0.06499999999999999, 4.0], [-0.06499999999999999, 4.0]]), ('frame_19', [[0.0, 5.2], [0.07999999999999999, 5.01]]), ('frame_20', [[0.0, 5.2], [-0.07999999999999997, 5.01]])]:
            c.line(points, id=object_id, zorder=3, clip_on=False)
        c.line([[-2.4000000000000004, -1.35]], id='frame_21', zorder=4, color=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765), linewidth=1.5, linestyle='None', solid_capstyle='projecting', marker='o', markersize=6.0, markeredgewidth=1.0, markeredgecolor='#000000', markerfacecolor='#000000')
        c.line([[2.4000000000000004, -1.35]], id='frame_22', zorder=4, color=(1.0, 0.4980392156862745, 0.054901960784313725), linewidth=1.5, linestyle='None', solid_capstyle='projecting', marker='o', markersize=6.0, markeredgewidth=1.0, markeredgecolor='#000000', markerfacecolor='#000000')
        c.line([[0.0, 3.0]], id='frame_23', zorder=4, color=(0.17254901960784313, 0.6274509803921569, 0.17254901960784313), linewidth=1.5, linestyle='None', solid_capstyle='projecting', marker='o', markersize=6.0, markeredgewidth=1.0, markeredgecolor='#000000', markerfacecolor='#000000')
        for object_id, points in [('s24', [[0.0, 0.0], [-2.4000000000000004, -1.35]]), ('s25', [[0.0, 0.0], [2.4000000000000004, -1.35]]), ('s26', [[0.0, 0.0], [0.0, 3.0]])]:
            c.line(points, id=object_id, clip_on=False, linestyle=(0, [4, 3]))
        for object_id, points in [('s27', [[0.0, 3.0], [-2.4000000000000004, 1.65]]), ('s28', [[0.0, 3.0], [2.4000000000000004, 1.65]]), ('s29', [[2.4000000000000004, -1.35], [-2.220446049250313e-16, -2.7]]), ('s30', [[2.4000000000000004, -1.35], [2.4000000000000004, 1.65]]), ('s31', [[2.4000000000000004, 1.65], [-2.220446049250313e-16, 0.2999999999999998]]), ('s32', [[-2.4000000000000004, -1.35], [-2.220446049250313e-16, -2.7]]), ('s33', [[-2.4000000000000004, -1.35], [-2.4000000000000004, 1.65]]), ('s34', [[-2.4000000000000004, 1.65], [-2.220446049250313e-16, 0.2999999999999998]]), ('s35', [[-2.220446049250313e-16, -2.7], [-2.220446049250313e-16, 0.2999999999999998]])]:
            c.line(points, id=object_id, zorder=3, clip_on=False)
        c.text('2', (-1.6, -0.9), rotation_mode='default', offset_pt=(8.572527594031472e-16, 14.0), annotation_clip=None)
        c.text('4', (-3.2, -1.8), rotation_mode='default', offset_pt=(8.572527594031472e-16, 14.0), annotation_clip=None)
        c.text('x', (-4.16, -2.3400000000000003), fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(-13.073633056868239, -7.353918594488384), annotation_clip=None)
        c.text('2', (1.6, -0.9), rotation_mode='default', offset_pt=(12.124355652982143, 6.999999999999999), annotation_clip=None)
        c.text('4', (3.2, -1.8), rotation_mode='default', offset_pt=(12.124355652982143, 6.999999999999999), annotation_clip=None)
        c.text('y', (4.16, -2.3400000000000003), fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(13.073633056868239, -7.353918594488384), annotation_clip=None)
        c.text('2', (0.0, 2.0), rotation_mode='default', offset_pt=(-12.0, 0.0), annotation_clip=None)
        c.text('4', (0.0, 4.0), rotation_mode='default', offset_pt=(-12.0, 0.0), annotation_clip=None)
        c.text('z', (0.0, 5.2), fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(0.0, 15.0), annotation_clip=None)
        c.text('O', (0.0, 0.0), fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(19.318516525781366, 5.176380902050415), annotation_clip=None)
        c.text('A', (-2.4000000000000004, -1.35), fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(-9.899494936611664, 9.899494936611665), annotation_clip=None)
        c.text('B', (2.4000000000000004, -1.35), fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(12, 12), annotation_clip=None)
        c.text('C', (0.0, 3.0), fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(12, 12), annotation_clip=None)
        return c.save(output_path)
