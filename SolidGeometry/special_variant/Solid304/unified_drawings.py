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
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / 'Solid304_C01.png'
    _geometry_01 = [('s0', [[3.7600000000000002, 2.115], [-4.16, -2.3400000000000003]]),
     ('s1', [[3.1681330194238835, 1.8566524099130957], [3.231866980576117, 1.7433475900869044]]),
     ('s2', [[2.3681330194238837, 1.4066524099130955], [2.4318669805761166, 1.2933475900869045]]),
     ('s3', [[1.5681330194238838, 0.9566524099130957], [1.6318669805761166, 0.8433475900869044]]),
     ('s4', [[0.7681330194238838, 0.5066524099130957], [0.8318669805761163, 0.3933475900869043]]),
     ('s5', [[-0.8318669805761163, -0.3933475900869043], [-0.7681330194238838, -0.5066524099130957]]),
     ('s6', [[-1.6318669805761166, -0.8433475900869044], [-1.5681330194238838, -0.9566524099130957]]),
     ('s7', [[-2.4318669805761166, -1.2933475900869045], [-2.3681330194238837, -1.4066524099130955]]),
     ('s8', [[-3.231866980576117, -1.7433475900869044], [-3.1681330194238835, -1.8566524099130957]]),
     ('s9', [[-4.16, -2.3400000000000003], [-4.033621547116941, -2.1771243214998504]]),
     ('s10', [[-4.16, -2.3400000000000003], [-3.955179748775732, -2.316576407439778]]),
     ('s11', [[-3.7600000000000002, 2.115], [4.16, -2.3400000000000003]]),
     ('s12', [[-3.2318669805761164, 1.7433475900869044], [-3.168133019423884, 1.8566524099130957]]),
     ('s13', [[-2.4318669805761166, 1.2933475900869045], [-2.3681330194238837, 1.4066524099130957]]),
     ('s14', [[-1.6318669805761166, 0.8433475900869043], [-1.5681330194238838, 0.9566524099130959]]),
     ('s15', [[-0.8318669805761163, 0.3933475900869043], [-0.7681330194238837, 0.5066524099130957]]),
     ('s16', [[0.7681330194238837, -0.5066524099130957], [0.8318669805761163, -0.3933475900869043]]),
     ('s17', [[1.5681330194238838, -0.9566524099130959], [1.6318669805761166, -0.8433475900869043]]),
     ('s18', [[2.3681330194238837, -1.4066524099130957], [2.4318669805761166, -1.2933475900869045]]),
     ('s19', [[3.168133019423884, -1.8566524099130957], [3.2318669805761164, -1.7433475900869044]]),
     ('s20', [[4.16, -2.3400000000000003], [3.9551797487757314, -2.316576407439778]]),
     ('s21', [[4.16, -2.3400000000000003], [4.033621547116941, -2.1771243214998504]]),
     ('s22', [[0.0, -4.7], [0.0, 5.2]]),
     ('s23', [[0.06499999999999999, -4.0], [-0.06499999999999999, -4.0]]),
     ('s24', [[0.06499999999999999, -3.0], [-0.06499999999999999, -3.0]]),
     ('s25', [[0.06499999999999999, -2.0], [-0.06499999999999999, -2.0]]),
     ('s26', [[0.06499999999999999, -1.0], [-0.06499999999999999, -1.0]]),
     ('s27', [[0.06499999999999999, 1.0], [-0.06499999999999999, 1.0]]),
     ('s28', [[0.06499999999999999, 2.0], [-0.06499999999999999, 2.0]]),
     ('s29', [[0.06499999999999999, 3.0], [-0.06499999999999999, 3.0]]),
     ('s30', [[0.06499999999999999, 4.0], [-0.06499999999999999, 4.0]]),
     ('s31', [[0.0, 5.2], [0.07999999999999999, 5.01]]),
     ('s32', [[0.0, 5.2], [-0.07999999999999997, 5.01]])]
    with Canvas(SOLID, xlim=(-5.45576447969006, 5.455764479690062), ylim=(-4.94247842131956, 5.9690505380605625), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        for object_id, points in _geometry_01:
            c.line(points, id=object_id, zorder=3, clip_on=False)
        c.line([[-2.4000000000000004, -1.35]], id='p_A', zorder=4, color=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765), linewidth=1.5, linestyle='None', solid_capstyle='projecting', marker='o', markersize=6.0, markeredgewidth=1.0, markeredgecolor='#000000', markerfacecolor='#000000')
        c.line([[3.2, -1.8]], id='p_B', zorder=4, color=(1.0, 0.4980392156862745, 0.054901960784313725), linewidth=1.5, linestyle='None', solid_capstyle='projecting', marker='o', markersize=6.0, markeredgewidth=1.0, markeredgecolor='#000000', markerfacecolor='#000000')
        c.line([[0.0, 2.0]], id='p_C', zorder=4, color=(0.17254901960784313, 0.6274509803921569, 0.17254901960784313), linewidth=1.5, linestyle='None', solid_capstyle='projecting', marker='o', markersize=6.0, markeredgewidth=1.0, markeredgecolor='#000000', markerfacecolor='#000000')
        c.line([[-2.4000000000000004, -1.35], [3.2, -1.8]], id='s36', zorder=3, clip_on=False, color='#2563EB')
        c.line([[3.2, -1.8], [0.0, 2.0]], id='s37', zorder=3, clip_on=False)
        c.line([[0.0, 2.0], [-2.4000000000000004, -1.35]], id='s38', zorder=3, clip_on=False)
        c.text('-4', (3.2, 1.8), rotation_mode='default', offset_pt=(-3.6234666314352886, 13.522961568046956), annotation_clip=None)
        c.text('-2', (1.6, 0.9), rotation_mode='default', offset_pt=(-3.6234666314352886, 13.522961568046956), annotation_clip=None)
        c.text('2', (-1.6, -0.9), rotation_mode='default', offset_pt=(12.124355652982137, -7.000000000000006), annotation_clip=None)
        c.text('4', (-3.2, -1.8), rotation_mode='default', offset_pt=(8.572527594031472e-16, 14.0), annotation_clip=None)
        c.text('x', (-4.16, -2.3400000000000003), fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(-13.073633056868239, -7.353918594488384), annotation_clip=None)
        c.text('-4', (-3.2, 1.8), rotation_mode='default', offset_pt=(7.000000000000002, 12.12435565298214), annotation_clip=None)
        c.text('-2', (-1.6, 0.9), rotation_mode='default', offset_pt=(7.000000000000002, 12.12435565298214), annotation_clip=None)
        c.text('2', (1.6, -0.9), rotation_mode='default', offset_pt=(3.6234666314352935, 13.522961568046956), annotation_clip=None)
        c.text('4', (3.2, -1.8), rotation_mode='default', offset_pt=(12.124355652982143, 6.999999999999999), annotation_clip=None)
        c.text('y', (4.16, -2.3400000000000003), fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(13.073633056868239, -7.353918594488384), annotation_clip=None)
        c.text('-4', (0.0, -4.0), rotation_mode='default', offset_pt=(14.0, 0.0), annotation_clip=None)
        c.text('-2', (0.0, -2.0), rotation_mode='default', offset_pt=(14.0, 0.0), annotation_clip=None)
        c.text('2', (0.0, 2.0), rotation_mode='default', offset_pt=(13.522961568046956, 3.6234666314352904), annotation_clip=None)
        c.text('4', (0.0, 4.0), rotation_mode='default', offset_pt=(-12.0, 0.0), annotation_clip=None)
        c.text('z', (0.0, 5.2), fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(0.0, 15.0), annotation_clip=None)
        c.text('O', (0.0, 0.0), fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(13.500000000000004, 23.38268590217984), annotation_clip=None)
        c.text('A', (-2.4000000000000004, -1.35), fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(-9.899494936611664, 9.899494936611665), annotation_clip=None)
        c.text('B', (3.2, -1.8), fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(-3.623466631435301, -13.522961568046954), annotation_clip=None)
        c.text('C', (0.0, 2.0), fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(-12.124355652982139, 7.000000000000004), annotation_clip=None)
        return c.save(output_path)
