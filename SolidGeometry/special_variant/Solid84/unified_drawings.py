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
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / 'Solid84_C01.png'
    _geometry_01 = [('cube1rightline0', [[9.0, 7.0], [9.7, 9.7]]),
     ('cube1rightline1', [[9.0, 9.0], [9.7, 7.7]]),
     ('face0line0', [[0.0, 4.8], [1.0, 4.8]]),
     ('face0line1', [[1.0, 4.8], [1.0, 5.8]]),
     ('face0line2', [[1.0, 5.8], [0.0, 5.8]]),
     ('face0line3', [[0.0, 5.8], [0.0, 4.8]]),
     ('face0line4', [[0.0, 5.3], [0.5, 5.8]]),
     ('face0line5', [[0.5, 5.8], [1.0, 5.3]]),
     ('face0line6', [[1.0, 5.3], [0.5, 4.8]]),
     ('face0line7', [[0.5, 4.8], [0.0, 5.3]]),
     ('face1line0', [[2.1, 4.8], [3.1, 4.8]]),
     ('face1line1', [[3.1, 4.8], [3.1, 5.8]]),
     ('face1line2', [[3.1, 5.8], [2.1, 5.8]]),
     ('face1line3', [[2.1, 5.8], [2.1, 4.8]]),
     ('face1line4', [[2.3000000000000003, 5.3], [2.6, 5.6]]),
     ('face1line5', [[2.6, 5.6], [2.9000000000000004, 5.3]]),
     ('face1line6', [[2.9000000000000004, 5.3], [2.6, 5.0]]),
     ('face1line7', [[2.6, 5.0], [2.3000000000000003, 5.3]]),
     ('face2line0', [[4.2, 4.8], [5.2, 4.8]]),
     ('face2line1', [[5.2, 4.8], [5.2, 5.8]]),
     ('face2line2', [[5.2, 5.8], [4.2, 5.8]]),
     ('face2line3', [[4.2, 5.8], [4.2, 4.8]]),
     ('face2line4', [[4.2, 5.3], [5.2, 5.3]]),
     ('face3line0', [[6.300000000000001, 4.8], [7.300000000000001, 4.8]]),
     ('face3line1', [[7.300000000000001, 4.8], [7.300000000000001, 5.8]]),
     ('face3line2', [[7.300000000000001, 5.8], [6.300000000000001, 5.8]]),
     ('face3line3', [[6.300000000000001, 5.8], [6.300000000000001, 4.8]]),
     ('face3line4', [[6.550000000000001, 5.05], [7.050000000000001, 5.05]]),
     ('face3line5', [[7.050000000000001, 5.05], [7.050000000000001, 5.55]]),
     ('face3line6', [[7.050000000000001, 5.55], [6.550000000000001, 5.55]]),
     ('face3line7', [[6.550000000000001, 5.55], [6.550000000000001, 5.05]]),
     ('face4line0', [[8.4, 4.8], [9.4, 4.8]]),
     ('face4line1', [[9.4, 4.8], [9.4, 5.8]]),
     ('face4line2', [[9.4, 5.8], [8.4, 5.8]]),
     ('face4line3', [[8.4, 5.8], [8.4, 4.8]]),
     ('face4line4', [[8.4, 5.3], [9.4, 5.3]]),
     ('face4line5', [[8.9, 4.8], [8.9, 5.8]]),
     ('face5line0', [[10.5, 4.8], [11.5, 4.8]]),
     ('face5line1', [[11.5, 4.8], [11.5, 5.8]]),
     ('face5line2', [[11.5, 5.8], [10.5, 5.8]]),
     ('face5line3', [[10.5, 5.8], [10.5, 4.8]]),
     ('face5line4', [[10.5, 4.8], [11.5, 5.8]]),
     ('face5line5', [[10.5, 5.8], [11.5, 4.8]]),
     ('targetline0', [[5.25, 2.4], [6.25, 2.4]]),
     ('targetline1', [[6.25, 2.4], [6.25, 3.4]]),
     ('targetline2', [[6.25, 3.4], [5.25, 3.4]]),
     ('targetline3', [[5.25, 3.4], [5.25, 2.4]])]
    _geometry_02 = [('option0line0', [[0.6, 0.0], [1.6, 0.0]]),
     ('option0line1', [[1.6, 0.0], [1.6, 1.0]]),
     ('option0line2', [[1.6, 1.0], [0.6, 1.0]]),
     ('option0line3', [[0.6, 1.0], [0.6, 0.0]]),
     ('option0line4', [[0.8, 0.5], [1.1, 0.8]]),
     ('option0line5', [[1.1, 0.8], [1.4, 0.5]]),
     ('option0line6', [[1.4, 0.5], [1.1, 0.2]]),
     ('option0line7', [[1.1, 0.2], [0.8, 0.5]]),
     ('option1line0', [[2.95, 0.0], [3.95, 0.0]]),
     ('option1line1', [[3.95, 0.0], [3.95, 1.0]]),
     ('option1line2', [[3.95, 1.0], [2.95, 1.0]]),
     ('option1line3', [[2.95, 1.0], [2.95, 0.0]]),
     ('option1line4', [[2.95, 0.5], [3.95, 0.5]]),
     ('option2line0', [[5.3, 0.0], [6.3, 0.0]]),
     ('option2line1', [[6.3, 0.0], [6.3, 1.0]]),
     ('option2line2', [[6.3, 1.0], [5.3, 1.0]]),
     ('option2line3', [[5.3, 1.0], [5.3, 0.0]]),
     ('option2line4', [[5.55, 0.25], [6.05, 0.25]]),
     ('option2line5', [[6.05, 0.25], [6.05, 0.75]]),
     ('option2line6', [[6.05, 0.75], [5.55, 0.75]]),
     ('option2line7', [[5.55, 0.75], [5.55, 0.25]]),
     ('option3line0', [[7.65, 0.0], [8.65, 0.0]]),
     ('option3line1', [[8.65, 0.0], [8.65, 1.0]]),
     ('option3line2', [[8.65, 1.0], [7.65, 1.0]]),
     ('option3line3', [[7.65, 1.0], [7.65, 0.0]]),
     ('option3line4', [[7.65, 0.5], [8.65, 0.5]]),
     ('option3line5', [[8.15, 0.0], [8.15, 1.0]]),
     ('option4line0', [[10.0, 0.0], [11.0, 0.0]]),
     ('option4line1', [[11.0, 0.0], [11.0, 1.0]]),
     ('option4line2', [[11.0, 1.0], [10.0, 1.0]]),
     ('option4line3', [[10.0, 1.0], [10.0, 0.0]]),
     ('option4line4', [[10.0, 0.0], [11.0, 1.0]]),
     ('option4line5', [[10.0, 1.0], [11.0, 0.0]])]
    with Canvas(SOLID, xlim=(-0.28640932321931345, 11.803820902676676), ylim=(-1.482406173994507, 10.607824051901483), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        for object_id, points in [('cube0000_cube0100', [[1.4, 7.0], [3.4, 7.0]]), ('cube0000_cube0001', [[1.4, 7.0], [1.4, 9.0]]), ('cube0001_cube0101', [[1.4, 9.0], [3.4, 9.0]]), ('cube0001_cube0011', [[1.4, 9.0], [2.0999999999999996, 9.7]]), ('cube0011_cube0111', [[2.0999999999999996, 9.7], [4.1, 9.7]]), ('cube0100_cube0110', [[3.4, 7.0], [4.1, 7.7]]), ('cube0100_cube0101', [[3.4, 7.0], [3.4, 9.0]]), ('cube0101_cube0111', [[3.4, 9.0], [4.1, 9.7]]), ('cube0110_cube0111', [[4.1, 7.7], [4.1, 9.7]])]:
            c.line(points, id=object_id, zorder=3, clip_on=False)
        for object_id, points in [('cube0topline0', [[2.0749999999999997, 9.175], [3.0749999999999997, 9.175]]), ('cube0topline1', [[3.0749999999999997, 9.175], [3.425, 9.525]]), ('cube0topline2', [[3.425, 9.525], [2.425, 9.525]]), ('cube0topline3', [[2.425, 9.525], [2.0749999999999997, 9.175]])]:
            c.line(points, id=object_id, zorder=3, clip_on=False, color='#2563EB')
        c.line([[1.4, 8.0], [3.4, 8.0]], id='cube0frontline0', zorder=3, clip_on=False)
        for object_id, points in [('cube0rightline0', [[3.54, 8.14], [3.75, 8.95]]), ('cube0rightline1', [[3.75, 8.95], [3.96, 8.56]]), ('cube0rightline2', [[3.96, 8.56], [3.75, 7.75]]), ('cube0rightline3', [[3.75, 7.75], [3.54, 8.14]])]:
            c.line(points, id=object_id, zorder=3, clip_on=False, color='#2563EB')
        for object_id, points in [('cube1000_cube1100', [[7.0, 7.0], [9.0, 7.0]]), ('cube1000_cube1001', [[7.0, 7.0], [7.0, 9.0]]), ('cube1001_cube1101', [[7.0, 9.0], [9.0, 9.0]]), ('cube1001_cube1011', [[7.0, 9.0], [7.7, 9.7]]), ('cube1011_cube1111', [[7.7, 9.7], [9.7, 9.7]]), ('cube1100_cube1110', [[9.0, 7.0], [9.7, 7.7]]), ('cube1100_cube1101', [[9.0, 7.0], [9.0, 9.0]]), ('cube1101_cube1111', [[9.0, 9.0], [9.7, 9.7]]), ('cube1110_cube1111', [[9.7, 7.7], [9.7, 9.7]]), ('cube1topline0', [[7.35, 9.35], [9.35, 9.35]]), ('cube1topline1', [[8.0, 9.0], [8.7, 9.7]])]:
            c.line(points, id=object_id, zorder=3, clip_on=False)
        for object_id, points in [('cube1frontline0', [[7.5, 7.5], [8.5, 7.5]]), ('cube1frontline1', [[8.5, 7.5], [8.5, 8.5]]), ('cube1frontline2', [[8.5, 8.5], [7.5, 8.5]]), ('cube1frontline3', [[7.5, 8.5], [7.5, 7.5]])]:
            c.line(points, id=object_id, zorder=3, clip_on=False, color='#2563EB')
        for object_id, points in _geometry_01:
            c.line(points, id=object_id, zorder=3, clip_on=False)
        for object_id, points in [('targetline4', [[5.25, 2.9], [5.75, 3.4]]), ('targetline5', [[5.75, 3.4], [6.25, 2.9]]), ('targetline6', [[6.25, 2.9], [5.75, 2.4]]), ('targetline7', [[5.75, 2.4], [5.25, 2.9]])]:
            c.line(points, id=object_id, zorder=3, clip_on=False, color='#2563EB')
        for object_id, points in _geometry_02:
            c.line(points, id=object_id, zorder=3, clip_on=False)
        for object_id, text, anchor in [('optionlabel0', '(A)', (1.1, 0.0)), ('optionlabel1', '(B)', (3.45, 0.0)), ('optionlabel2', '(C)', (5.8, 0.0)), ('optionlabel3', '(D)', (8.15, 0.0)), ('optionlabel4', '(E)', (10.5, 0.0))]:
            c.text(text, anchor, id=object_id, rotation_mode='default', offset_pt=(0, -18), annotation_clip=None)
        return c.save(output_path)
