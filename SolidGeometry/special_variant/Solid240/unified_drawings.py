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
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / 'Solid240_C01.png'
    with Canvas(SOLID, xlim=(-0.17661733968185622, 7.265553692550153), ylim=(-3.2880728142237854, 4.154098218008224), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        for object_id, points in [('line_0', [[0.0, 0.8660254037844386], [0.5, 0.0]]), ('line_1', [[0.0, 0.8660254037844386], [1.0, 0.8660254037844386]]), ('line_2', [[0.5, 0.0], [1.0, -0.8660254037844386]]), ('line_3', [[0.5, 0.0], [1.0, 0.8660254037844386]]), ('line_4', [[0.5, 0.0], [1.5, 0.0]]), ('line_5', [[1.0, -0.8660254037844386], [1.5, 0.0]]), ('line_6', [[1.0, 0.8660254037844386], [1.5, 0.0]]), ('line_7', [[1.0, 0.8660254037844386], [2.0, 0.8660254037844386]]), ('line_8', [[1.5, 0.0], [2.0, 0.8660254037844386]]), ('line_9', [[1.5, 0.0], [2.5, 0.0]])]:
            c.line(points, id=object_id, zorder=3, clip_on=False)
        c.line([[2.0, 0.8660254037844386], [2.5, 0.0]], id='line_10', zorder=3, clip_on=False, color='#16A34A')
        c.line([[2.0, 0.8660254037844386], [2.5, 1.7320508075688772]], id='line_11', zorder=3, clip_on=False)
        c.line([[2.0, 0.8660254037844386], [3.0, 0.8660254037844386]], id='line_12', zorder=3, clip_on=False, color='#DC2626')
        c.line([[2.5, 0.0], [3.0, 0.8660254037844386]], id='line_13', zorder=3, clip_on=False, color='#2563EB')
        c.line([[2.5, 0.0], [3.5, 0.0]], id='line_14', zorder=3, clip_on=False, color='#16A34A')
        c.line([[2.5, 1.7320508075688772], [3.0, 0.8660254037844386]], id='line_15', zorder=3, clip_on=False)
        c.line([[3.0, 0.8660254037844386], [3.5, 0.0]], id='line_16', zorder=3, clip_on=False, color='#DC2626')
        for object_id, points in [('line_17', [[6.1, 1.417333478872227], [5.111063647131703, 0.4123946153690259]]), ('line_18', [[6.1, 1.417333478872227], [7.088936352868297, 0.48760538463097414]]), ('line_19', [[6.1, 1.417333478872227], [6.248340452930244, 0.199297435793506]])]:
            c.line(points, id=object_id, zorder=3, clip_on=False)
        c.line([[6.1, 1.417333478872227], [5.951659547069755, 0.700702564206494]], id='line_20', clip_on=False, linestyle=(0.0, [4.0, 3.0]))
        for object_id, points in [('line_21', [[6.1, -0.5173334788722268], [5.111063647131703, 0.4123946153690259]]), ('line_22', [[6.1, -0.5173334788722268], [7.088936352868297, 0.48760538463097414]]), ('line_23', [[6.1, -0.5173334788722268], [6.248340452930244, 0.199297435793506]])]:
            c.line(points, id=object_id, zorder=3, clip_on=False)
        c.line([[6.1, -0.5173334788722268], [5.951659547069755, 0.700702564206494]], id='line_24', clip_on=False, linestyle=(0.0, [4.0, 3.0]))
        c.line([[5.111063647131703, 0.4123946153690259], [6.248340452930244, 0.199297435793506]], id='line_25', zorder=3, clip_on=False)
        c.line([[5.111063647131703, 0.4123946153690259], [5.951659547069755, 0.700702564206494]], id='line_26', clip_on=False, linestyle=(0.0, [4.0, 3.0]))
        c.line([[7.088936352868297, 0.48760538463097414], [6.248340452930244, 0.199297435793506]], id='line_27', zorder=3, clip_on=False)
        c.line([[7.088936352868297, 0.48760538463097414], [5.951659547069755, 0.700702564206494]], id='line_28', clip_on=False, linestyle=(0.0, [4.0, 3.0]))
        for object_id, points in [('line_29', [[3.75, 0.55], [4.8, 0.55]]), ('line_30', [[4.8, 0.55], [4.67, 0.61]]), ('line_31', [[4.8, 0.55], [4.67, 0.49]])]:
            c.line(points, id=object_id, zorder=3, clip_on=False)
        for object_id, text, anchor in [('label_0', '1', (0.5, 0.5773502691896257)), ('label_1', '3', (1.0, 0.28867513459481287)), ('label_2', '4', (1.5, 0.5773502691896257)), ('label_3', '5', (2.0, 0.28867513459481287)), ('label_4', '6', (2.5, 0.5773502691896257))]:
            c.text(text, anchor, id=object_id, rotation_mode='default', offset_pt=(0, 0), annotation_clip=None)
        c.text('Q', (3.0, 0.28867513459481287), id='label_5', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(0, 0), annotation_clip=None)
        c.text('2', (1.0, -0.28867513459481287), id='label_6', rotation_mode='default', offset_pt=(0, 0), annotation_clip=None)
        c.text('7', (2.5, 1.1547005383792515), id='label_7', rotation_mode='default', offset_pt=(0, 0), annotation_clip=None)
        c.text('Q', (5.7209077314004855, 0.843476886149249), id='label_8', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(6, 1), annotation_clip=None)
        c.text('?', (6.380198633312684, 0.8685471425698983), id='label_9', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(0, 0), annotation_clip=None)
        return c.save(output_path)

def C02(output_path=None):
    if output_path is None:
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / 'Solid240_C02.png'
    with Canvas(SOLID, xlim=(-0.17661733968185622, 7.265553692550153), ylim=(-3.2880728142237854, 4.154098218008224), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        for object_id, points in [('line_0', [[0.0, 0.8660254037844386], [0.5, 0.0]]), ('line_1', [[0.0, 0.8660254037844386], [1.0, 0.8660254037844386]]), ('line_2', [[0.5, 0.0], [1.0, -0.8660254037844386]])]:
            c.line(points, id=object_id, zorder=3, clip_on=False)
        c.line([[0.5, 0.0], [1.0, 0.8660254037844386]], id='line_3', zorder=3, clip_on=False, color='#2563EB')
        c.line([[0.5, 0.0], [1.5, 0.0]], id='line_4', zorder=3, clip_on=False, color='#DC2626')
        c.line([[1.0, -0.8660254037844386], [1.5, 0.0]], id='line_5', zorder=3, clip_on=False)
        c.line([[1.0, 0.8660254037844386], [1.5, 0.0]], id='line_6', zorder=3, clip_on=False, color='#16A34A')
        for object_id, points in [('line_7', [[1.0, 0.8660254037844386], [2.0, 0.8660254037844386]]), ('line_8', [[1.5, 0.0], [2.0, 0.8660254037844386]]), ('line_9', [[1.5, 0.0], [2.5, 0.0]]), ('line_10', [[2.0, 0.8660254037844386], [2.5, 0.0]]), ('line_11', [[2.0, 0.8660254037844386], [2.5, 1.7320508075688772]]), ('line_12', [[2.0, 0.8660254037844386], [3.0, 0.8660254037844386]])]:
            c.line(points, id=object_id, zorder=3, clip_on=False)
        c.line([[2.5, 0.0], [3.0, 0.8660254037844386]], id='line_13', zorder=3, clip_on=False, color='#DC2626')
        c.line([[2.5, 0.0], [3.5, 0.0]], id='line_14', zorder=3, clip_on=False, color='#16A34A')
        c.line([[2.5, 1.7320508075688772], [3.0, 0.8660254037844386]], id='line_15', zorder=3, clip_on=False)
        c.line([[3.0, 0.8660254037844386], [3.5, 0.0]], id='line_16', zorder=3, clip_on=False, color='#2563EB')
        for object_id, points in [('line_17', [[6.1, 1.417333478872227], [5.111063647131703, 0.4123946153690259]]), ('line_18', [[6.1, 1.417333478872227], [7.088936352868297, 0.48760538463097414]]), ('line_19', [[6.1, 1.417333478872227], [6.248340452930244, 0.199297435793506]])]:
            c.line(points, id=object_id, zorder=3, clip_on=False)
        c.line([[6.1, 1.417333478872227], [5.951659547069755, 0.700702564206494]], id='line_20', clip_on=False, linestyle=(0.0, [4.0, 3.0]))
        for object_id, points in [('line_21', [[6.1, -0.5173334788722268], [5.111063647131703, 0.4123946153690259]]), ('line_22', [[6.1, -0.5173334788722268], [7.088936352868297, 0.48760538463097414]]), ('line_23', [[6.1, -0.5173334788722268], [6.248340452930244, 0.199297435793506]])]:
            c.line(points, id=object_id, zorder=3, clip_on=False)
        c.line([[6.1, -0.5173334788722268], [5.951659547069755, 0.700702564206494]], id='line_24', clip_on=False, linestyle=(0.0, [4.0, 3.0]))
        c.line([[5.111063647131703, 0.4123946153690259], [6.248340452930244, 0.199297435793506]], id='line_25', zorder=3, clip_on=False)
        c.line([[5.111063647131703, 0.4123946153690259], [5.951659547069755, 0.700702564206494]], id='line_26', clip_on=False, linestyle=(0.0, [4.0, 3.0]))
        c.line([[7.088936352868297, 0.48760538463097414], [6.248340452930244, 0.199297435793506]], id='line_27', zorder=3, clip_on=False)
        c.line([[7.088936352868297, 0.48760538463097414], [5.951659547069755, 0.700702564206494]], id='line_28', clip_on=False, linestyle=(0.0, [4.0, 3.0]))
        for object_id, points in [('line_29', [[3.75, 0.55], [4.8, 0.55]]), ('line_30', [[4.8, 0.55], [4.67, 0.61]]), ('line_31', [[4.8, 0.55], [4.67, 0.49]])]:
            c.line(points, id=object_id, zorder=3, clip_on=False)
        for object_id, text, anchor in [('label_0', '1', (0.5, 0.5773502691896257)), ('label_1', '3', (1.0, 0.28867513459481287)), ('label_2', '4', (1.5, 0.5773502691896257)), ('label_3', '5', (2.0, 0.28867513459481287)), ('label_4', '6', (2.5, 0.5773502691896257))]:
            c.text(text, anchor, id=object_id, rotation_mode='default', offset_pt=(0, 0), annotation_clip=None)
        c.text('Q', (3.0, 0.28867513459481287), id='label_5', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(0, 0), annotation_clip=None)
        c.text('2', (1.0, -0.28867513459481287), id='label_6', rotation_mode='default', offset_pt=(0, 0), annotation_clip=None)
        c.text('7', (2.5, 1.1547005383792515), id='label_7', rotation_mode='default', offset_pt=(0, 0), annotation_clip=None)
        c.text('Q', (5.7209077314004855, 0.843476886149249), id='label_8', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(6, 1), annotation_clip=None)
        c.text('?', (6.380198633312684, 0.8685471425698983), id='label_9', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(0, 0), annotation_clip=None)
        return c.save(output_path)
