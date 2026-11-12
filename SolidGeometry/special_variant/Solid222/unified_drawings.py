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
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / 'Solid222_C01.png'
    with Canvas(SOLID, xlim=(-0.1287965359209693, 5.299230302096819), ylim=(-0.5103156783544183, 4.91771115966337), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        for object_id, vertices, codes in [('paint_top_1_1', [[1.72, 3.4699999999999998], [2.7199999999999998, 3.4699999999999998], [3.44, 3.94], [2.44, 3.94], [1.72, 3.4699999999999998]], [1, 2, 2, 2, 79]), ('paint_right_2_1', [[4.4399999999999995, 1.94], [5.16, 2.41], [5.16, 3.41], [4.4399999999999995, 2.94], [4.4399999999999995, 1.94]], [1, 2, 2, 2, 79]), ('paint_right_1_2', [[3.7199999999999998, 2.4699999999999998], [4.4399999999999995, 2.94], [4.4399999999999995, 3.94], [3.7199999999999998, 3.4699999999999998], [3.7199999999999998, 2.4699999999999998]], [1, 2, 2, 2, 79]), ('paint_right_1_0', [[3.7199999999999998, 0.47], [4.4399999999999995, 0.94], [4.4399999999999995, 1.94], [3.7199999999999998, 1.47], [3.7199999999999998, 0.47]], [1, 2, 2, 2, 79]), ('paint_right_0_1', [[3.0, 1.0], [3.7199999999999998, 1.47], [3.7199999999999998, 2.4699999999999998], [3.0, 2.0], [3.0, 1.0]], [1, 2, 2, 2, 79]), ('paint_front_2_2', [[2.0, 2.0], [3.0, 2.0], [3.0, 3.0], [2.0, 3.0], [2.0, 2.0]], [1, 2, 2, 2, 79]), ('paint_front_2_0', [[2.0, 0.0], [3.0, 0.0], [3.0, 1.0], [2.0, 1.0], [2.0, 0.0]], [1, 2, 2, 2, 79]), ('paint_front_1_1', [[1.0, 1.0], [2.0, 1.0], [2.0, 2.0], [1.0, 2.0], [1.0, 1.0]], [1, 2, 2, 2, 79]), ('paint_front_0_2', [[0.0, 2.0], [1.0, 2.0], [1.0, 3.0], [0.0, 3.0], [0.0, 2.0]], [1, 2, 2, 2, 79]), ('paint_front_0_0', [[0.0, 0.0], [1.0, 0.0], [1.0, 1.0], [0.0, 1.0], [0.0, 0.0]], [1, 2, 2, 2, 79])]:
            c.path(vertices, codes, id=object_id, zorder=1, edgecolor='none', facecolor=(0.0, 0.0, 0.0, 1.0), linewidth=0.0, capstyle='butt', simplify=False)
        for object_id, points in [('line_0', [[0.0, 0.0], [3.0, 0.0]]), ('line_1', [[0.0, 3.0], [3.0, 3.0]]), ('line_2', [[2.16, 4.41], [5.16, 4.41]]), ('line_3', [[0.0, 3.0], [2.16, 4.41]]), ('line_4', [[3.0, 0.0], [5.16, 1.41]]), ('line_5', [[3.0, 3.0], [5.16, 4.41]]), ('line_6', [[0.0, 0.0], [0.0, 3.0]]), ('line_7', [[3.0, 0.0], [3.0, 3.0]]), ('line_8', [[5.16, 1.41], [5.16, 4.41]]), ('line_10', [[0.0, 0.0], [1.0, 0.0]])]:
            c.line(points, id=object_id, zorder=3, clip_on=False, color='#EA580C', linewidth=1.5, solid_capstyle='butt', simplify=False)
        c.line([[1.0, 0.0], [1.0, 1.0]], id='line_11', zorder=3, clip_on=False, simplify=False)
        c.line([[1.0, 1.0], [0.0, 1.0]], id='line_12', zorder=3, clip_on=False, simplify=False)
        c.line([[0.0, 1.0], [0.0, 0.0]], id='line_13', zorder=3, clip_on=False, color='#EA580C', linewidth=1.5, solid_capstyle='butt', simplify=False)
        for object_id, points in [('line_14', [[0.0, 1.0], [1.0, 1.0]]), ('line_15', [[1.0, 1.0], [1.0, 2.0]]), ('line_16', [[1.0, 2.0], [0.0, 2.0]])]:
            c.line(points, id=object_id, zorder=3, clip_on=False, simplify=False)
        c.line([[0.0, 2.0], [0.0, 1.0]], id='line_17', zorder=3, clip_on=False, color='#EA580C', linewidth=1.5, solid_capstyle='butt', simplify=False)
        c.line([[0.0, 2.0], [1.0, 2.0]], id='line_19', zorder=3, clip_on=False, simplify=False)
        c.line([[1.0, 2.0], [1.0, 3.0]], id='line_20', zorder=3, clip_on=False, simplify=False)
        for object_id, points in [('line_21', [[1.0, 3.0], [0.0, 3.0]]), ('line_22', [[0.0, 3.0], [0.0, 2.0]]), ('line_23', [[1.0, 0.0], [2.0, 0.0]])]:
            c.line(points, id=object_id, zorder=3, clip_on=False, color='#EA580C', linewidth=1.5, solid_capstyle='butt', simplify=False)
        for object_id, points in [('line_24', [[2.0, 0.0], [2.0, 1.0]]), ('line_25', [[2.0, 1.0], [1.0, 1.0]]), ('line_26', [[1.0, 1.0], [1.0, 0.0]]), ('line_28', [[1.0, 1.0], [2.0, 1.0]]), ('line_29', [[2.0, 1.0], [2.0, 2.0]]), ('line_30', [[2.0, 2.0], [1.0, 2.0]]), ('line_31', [[1.0, 2.0], [1.0, 1.0]]), ('line_32', [[1.0, 2.0], [2.0, 2.0]]), ('line_33', [[2.0, 2.0], [2.0, 3.0]])]:
            c.line(points, id=object_id, zorder=3, clip_on=False, simplify=False)
        c.line([[2.0, 3.0], [1.0, 3.0]], id='line_34', zorder=3, clip_on=False, color='#EA580C', linewidth=1.5, solid_capstyle='butt', simplify=False)
        c.line([[1.0, 3.0], [1.0, 2.0]], id='line_35', zorder=3, clip_on=False, simplify=False)
        c.line([[2.0, 0.0], [3.0, 0.0]], id='line_37', zorder=3, clip_on=False, color='#EA580C', linewidth=1.5, solid_capstyle='butt', simplify=False)
        c.line([[3.0, 0.0], [3.0, 1.0]], id='line_38', zorder=3, clip_on=False, color='#EA580C', linewidth=1.5, solid_capstyle='butt', simplify=False)
        for object_id, points in [('line_39', [[3.0, 1.0], [2.0, 1.0]]), ('line_40', [[2.0, 1.0], [2.0, 0.0]]), ('line_41', [[2.0, 1.0], [3.0, 1.0]])]:
            c.line(points, id=object_id, zorder=3, clip_on=False, simplify=False)
        c.line([[3.0, 1.0], [3.0, 2.0]], id='line_42', zorder=3, clip_on=False, color='#EA580C', linewidth=1.5, solid_capstyle='butt', simplify=False)
        for object_id, points in [('line_43', [[3.0, 2.0], [2.0, 2.0]]), ('line_44', [[2.0, 2.0], [2.0, 1.0]]), ('line_46', [[2.0, 2.0], [3.0, 2.0]])]:
            c.line(points, id=object_id, zorder=3, clip_on=False, simplify=False)
        c.line([[3.0, 2.0], [3.0, 3.0]], id='line_47', zorder=3, clip_on=False, color='#EA580C', linewidth=1.5, solid_capstyle='butt', simplify=False)
        c.line([[3.0, 3.0], [2.0, 3.0]], id='line_48', zorder=3, clip_on=False, color='#EA580C', linewidth=1.5, solid_capstyle='butt', simplify=False)
        c.line([[2.0, 3.0], [2.0, 2.0]], id='line_49', zorder=3, clip_on=False, simplify=False)
        c.line([[3.0, 0.0], [3.7199999999999998, 0.47]], id='line_50', zorder=3, clip_on=False, color='#EA580C', linewidth=1.5, solid_capstyle='butt', simplify=False)
        c.line([[3.7199999999999998, 0.47], [3.7199999999999998, 1.47]], id='line_51', zorder=3, clip_on=False, simplify=False)
        c.line([[3.7199999999999998, 1.47], [3.0, 1.0]], id='line_52', zorder=3, clip_on=False, simplify=False)
        c.line([[3.0, 1.0], [3.0, 0.0]], id='line_53', zorder=3, clip_on=False, color='#EA580C', linewidth=1.5, solid_capstyle='butt', simplify=False)
        for object_id, points in [('line_55', [[3.0, 1.0], [3.7199999999999998, 1.47]]), ('line_56', [[3.7199999999999998, 1.47], [3.7199999999999998, 2.4699999999999998]]), ('line_57', [[3.7199999999999998, 2.4699999999999998], [3.0, 2.0]])]:
            c.line(points, id=object_id, zorder=3, clip_on=False, simplify=False)
        c.line([[3.0, 2.0], [3.0, 1.0]], id='line_58', zorder=3, clip_on=False, color='#EA580C', linewidth=1.5, solid_capstyle='butt', simplify=False)
        c.line([[3.0, 2.0], [3.7199999999999998, 2.4699999999999998]], id='line_59', zorder=3, clip_on=False, simplify=False)
        c.line([[3.7199999999999998, 2.4699999999999998], [3.7199999999999998, 3.4699999999999998]], id='line_60', zorder=3, clip_on=False, simplify=False)
        for object_id, points in [('line_61', [[3.7199999999999998, 3.4699999999999998], [3.0, 3.0]]), ('line_62', [[3.0, 3.0], [3.0, 2.0]]), ('line_64', [[3.7199999999999998, 0.47], [4.4399999999999995, 0.94]])]:
            c.line(points, id=object_id, zorder=3, clip_on=False, color='#EA580C', linewidth=1.5, solid_capstyle='butt', simplify=False)
        for object_id, points in [('line_65', [[4.4399999999999995, 0.94], [4.4399999999999995, 1.94]]), ('line_66', [[4.4399999999999995, 1.94], [3.7199999999999998, 1.47]]), ('line_67', [[3.7199999999999998, 1.47], [3.7199999999999998, 0.47]]), ('line_68', [[3.7199999999999998, 1.47], [4.4399999999999995, 1.94]]), ('line_69', [[4.4399999999999995, 1.94], [4.4399999999999995, 2.94]]), ('line_70', [[4.4399999999999995, 2.94], [3.7199999999999998, 2.4699999999999998]]), ('line_71', [[3.7199999999999998, 2.4699999999999998], [3.7199999999999998, 1.47]]), ('line_73', [[3.7199999999999998, 2.4699999999999998], [4.4399999999999995, 2.94]]), ('line_74', [[4.4399999999999995, 2.94], [4.4399999999999995, 3.94]])]:
            c.line(points, id=object_id, zorder=3, clip_on=False, simplify=False)
        c.line([[4.4399999999999995, 3.94], [3.7199999999999998, 3.4699999999999998]], id='line_75', zorder=3, clip_on=False, color='#EA580C', linewidth=1.5, solid_capstyle='butt', simplify=False)
        c.line([[3.7199999999999998, 3.4699999999999998], [3.7199999999999998, 2.4699999999999998]], id='line_76', zorder=3, clip_on=False, simplify=False)
        c.line([[4.4399999999999995, 0.94], [5.16, 1.41]], id='line_77', zorder=3, clip_on=False, color='#EA580C', linewidth=1.5, solid_capstyle='butt', simplify=False)
        c.line([[5.16, 1.41], [5.16, 2.41]], id='line_78', zorder=3, clip_on=False, color='#EA580C', linewidth=1.5, solid_capstyle='butt', simplify=False)
        for object_id, points in [('line_79', [[5.16, 2.41], [4.4399999999999995, 1.94]]), ('line_80', [[4.4399999999999995, 1.94], [4.4399999999999995, 0.94]]), ('line_82', [[4.4399999999999995, 1.94], [5.16, 2.41]])]:
            c.line(points, id=object_id, zorder=3, clip_on=False, simplify=False)
        c.line([[5.16, 2.41], [5.16, 3.41]], id='line_83', zorder=3, clip_on=False, color='#EA580C', linewidth=1.5, solid_capstyle='butt', simplify=False)
        for object_id, points in [('line_84', [[5.16, 3.41], [4.4399999999999995, 2.94]]), ('line_85', [[4.4399999999999995, 2.94], [4.4399999999999995, 1.94]]), ('line_86', [[4.4399999999999995, 2.94], [5.16, 3.41]])]:
            c.line(points, id=object_id, zorder=3, clip_on=False, simplify=False)
        c.line([[5.16, 3.41], [5.16, 4.41]], id='line_87', zorder=3, clip_on=False, color='#EA580C', linewidth=1.5, solid_capstyle='butt', simplify=False)
        c.line([[5.16, 4.41], [4.4399999999999995, 3.94]], id='line_88', zorder=3, clip_on=False, color='#EA580C', linewidth=1.5, solid_capstyle='butt', simplify=False)
        c.line([[4.4399999999999995, 3.94], [4.4399999999999995, 2.94]], id='line_89', zorder=3, clip_on=False, simplify=False)
        c.line([[0.0, 3.0], [1.0, 3.0]], id='line_90', zorder=3, clip_on=False, color='#EA580C', linewidth=1.5, solid_capstyle='butt', simplify=False)
        c.line([[1.0, 3.0], [1.72, 3.4699999999999998]], id='line_91', zorder=3, clip_on=False, simplify=False)
        c.line([[1.72, 3.4699999999999998], [0.72, 3.4699999999999998]], id='line_92', zorder=3, clip_on=False, simplify=False)
        c.line([[0.72, 3.4699999999999998], [0.0, 3.0]], id='line_93', zorder=3, clip_on=False, color='#EA580C', linewidth=1.5, solid_capstyle='butt', simplify=False)
        for object_id, points in [('line_94', [[0.72, 3.4699999999999998], [1.72, 3.4699999999999998]]), ('line_95', [[1.72, 3.4699999999999998], [2.44, 3.94]]), ('line_96', [[2.44, 3.94], [1.44, 3.94]])]:
            c.line(points, id=object_id, zorder=3, clip_on=False, simplify=False)
        c.line([[1.44, 3.94], [0.72, 3.4699999999999998]], id='line_97', zorder=3, clip_on=False, color='#EA580C', linewidth=1.5, solid_capstyle='butt', simplify=False)
        c.line([[1.44, 3.94], [2.44, 3.94]], id='line_98', zorder=3, clip_on=False, simplify=False)
        c.line([[2.44, 3.94], [3.16, 4.41]], id='line_99', zorder=3, clip_on=False, simplify=False)
        for object_id, points in [('line_100', [[3.16, 4.41], [2.16, 4.41]]), ('line_101', [[2.16, 4.41], [1.44, 3.94]]), ('line_102', [[1.0, 3.0], [2.0, 3.0]])]:
            c.line(points, id=object_id, zorder=3, clip_on=False, color='#EA580C', linewidth=1.5, solid_capstyle='butt', simplify=False)
        for object_id, points in [('line_103', [[2.0, 3.0], [2.7199999999999998, 3.4699999999999998]]), ('line_104', [[2.7199999999999998, 3.4699999999999998], [1.72, 3.4699999999999998]]), ('line_105', [[1.72, 3.4699999999999998], [1.0, 3.0]]), ('line_107', [[1.72, 3.4699999999999998], [2.7199999999999998, 3.4699999999999998]]), ('line_108', [[2.7199999999999998, 3.4699999999999998], [3.44, 3.94]]), ('line_109', [[3.44, 3.94], [2.44, 3.94]]), ('line_110', [[2.44, 3.94], [1.72, 3.4699999999999998]]), ('line_111', [[2.44, 3.94], [3.44, 3.94]]), ('line_112', [[3.44, 3.94], [4.16, 4.41]])]:
            c.line(points, id=object_id, zorder=3, clip_on=False, simplify=False)
        c.line([[4.16, 4.41], [3.16, 4.41]], id='line_113', zorder=3, clip_on=False, color='#EA580C', linewidth=1.5, solid_capstyle='butt', simplify=False)
        c.line([[3.16, 4.41], [2.44, 3.94]], id='line_114', zorder=3, clip_on=False, simplify=False)
        c.line([[2.0, 3.0], [3.0, 3.0]], id='line_115', zorder=3, clip_on=False, color='#EA580C', linewidth=1.5, solid_capstyle='butt', simplify=False)
        c.line([[3.0, 3.0], [3.7199999999999998, 3.4699999999999998]], id='line_116', zorder=3, clip_on=False, color='#EA580C', linewidth=1.5, solid_capstyle='butt', simplify=False)
        for object_id, points in [('line_117', [[3.7199999999999998, 3.4699999999999998], [2.7199999999999998, 3.4699999999999998]]), ('line_118', [[2.7199999999999998, 3.4699999999999998], [2.0, 3.0]]), ('line_119', [[2.7199999999999998, 3.4699999999999998], [3.7199999999999998, 3.4699999999999998]])]:
            c.line(points, id=object_id, zorder=3, clip_on=False, simplify=False)
        c.line([[3.7199999999999998, 3.4699999999999998], [4.4399999999999995, 3.94]], id='line_120', zorder=3, clip_on=False, color='#EA580C', linewidth=1.5, solid_capstyle='butt', simplify=False)
        for object_id, points in [('line_121', [[4.4399999999999995, 3.94], [3.44, 3.94]]), ('line_122', [[3.44, 3.94], [2.7199999999999998, 3.4699999999999998]]), ('line_123', [[3.44, 3.94], [4.4399999999999995, 3.94]])]:
            c.line(points, id=object_id, zorder=3, clip_on=False, simplify=False)
        c.line([[4.4399999999999995, 3.94], [5.16, 4.41]], id='line_124', zorder=3, clip_on=False, color='#EA580C', linewidth=1.5, solid_capstyle='butt', simplify=False)
        c.line([[5.16, 4.41], [4.16, 4.41]], id='line_125', zorder=3, clip_on=False, color='#EA580C', linewidth=1.5, solid_capstyle='butt', simplify=False)
        c.line([[4.16, 4.41], [3.44, 3.94]], id='line_126', zorder=3, clip_on=False, simplify=False)
        return c.save(output_path)
