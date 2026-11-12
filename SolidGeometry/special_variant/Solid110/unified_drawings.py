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
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / 'Solid110_C01.png'
    _geometry_01 = [('structuree0', [[0.35, 0.35], [1.0, 0.35]]),
     ('structuree1', [[0.35, 1.35], [1.35, 1.35]]),
     ('structuree2', [[0.7, 1.7], [1.35, 1.7]]),
     ('structuree3', [[0.35, 1.35], [0.7, 1.7]]),
     ('structuree4', [[0.35, 0.35], [0.35, 1.35]]),
     ('structuree5', [[1.35, 1.35], [2.35, 1.35]]),
     ('structuree6', [[2.35, 1.35], [2.7, 1.7]]),
     ('structuree7', [[2.35, 0.35], [2.35, 1.35]]),
     ('structuree8', [[2.35, 0.35], [3.0, 0.35]]),
     ('structuree9', [[2.35, 1.35], [3.35, 1.35]]),
     ('structuree10', [[2.7, 1.7], [3.3499999999999996, 1.7]]),
     ('structuree11', [[3.35, 1.35], [4.35, 1.35]]),
     ('structuree12', [[4.35, 1.35], [4.7, 1.7]]),
     ('structuree13', [[4.35, 0.35], [4.35, 1.35]]),
     ('structuree14', [[4.35, 0.35], [5.35, 0.35]]),
     ('structuree15', [[4.35, 1.35], [5.35, 1.35]]),
     ('structuree16', [[4.7, 1.7], [5.7, 1.7]]),
     ('structuree17', [[5.35, 0.35], [5.7, 0.7]]),
     ('structuree18', [[5.35, 1.35], [5.7, 1.7]]),
     ('structuree19', [[5.35, 0.35], [5.35, 1.35]]),
     ('structuree20', [[5.7, 0.7], [5.7, 1.7]]),
     ('structuree21', [[1.0, 0.0], [2.0, 0.0]]),
     ('structuree22', [[1.0, 1.0], [2.0, 1.0]]),
     ('structuree23', [[1.0, 1.0], [1.35, 1.35]]),
     ('structuree24', [[2.0, 0.0], [2.35, 0.35]]),
     ('structuree25', [[2.0, 1.0], [2.35, 1.35]]),
     ('structuree26', [[1.0, 0.0], [1.0, 1.0]]),
     ('structuree27', [[2.0, 0.0], [2.0, 1.0]]),
     ('structuree28', [[3.0, 0.0], [4.0, 0.0]]),
     ('structuree29', [[3.0, 1.0], [4.0, 1.0]]),
     ('structuree30', [[3.0, 1.0], [3.35, 1.35]]),
     ('structuree31', [[4.0, 0.0], [4.35, 0.35]]),
     ('structuree32', [[4.0, 1.0], [4.35, 1.35]]),
     ('structuree33', [[3.0, 0.0], [3.0, 1.0]]),
     ('structuree34', [[4.0, 0.0], [4.0, 1.0]]),
     ('structuree35', [[1.35, 2.35], [2.35, 2.35]]),
     ('structuree36', [[1.7, 2.7], [2.7, 2.7]]),
     ('structuree37', [[1.35, 2.35], [1.7, 2.7]]),
     ('structuree38', [[2.35, 2.35], [2.7, 2.7]]),
     ('structuree39', [[1.35, 1.35], [1.35, 2.35]]),
     ('structuree40', [[2.35, 1.35], [2.35, 2.35]]),
     ('structuree41', [[2.7, 1.7], [2.7, 2.7]]),
     ('structuree42', [[3.35, 2.35], [4.35, 2.35]]),
     ('structuree43', [[3.7, 2.7], [4.7, 2.7]]),
     ('structuree44', [[3.35, 2.35], [3.7, 2.7]]),
     ('structuree45', [[4.35, 2.35], [4.7, 2.7]]),
     ('structuree46', [[3.35, 1.35], [3.35, 2.35]]),
     ('structuree47', [[4.35, 1.35], [4.35, 2.35]]),
     ('structuree48', [[4.7, 1.7], [4.7, 2.7]])]
    with Canvas(SOLID, xlim=(0.2167574018066678, 5.841342767766978), ylim=(-1.4663427677669767, 4.158242598193333), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        for object_id, points in _geometry_01:
            c.line(points, id=object_id, zorder=3, clip_on=False)
        for object_id, points in [(None, [[1.8802377142883933, 1.9031239149049153]]), (None, [[1.5987786835162783, 0.5360371940117843]]), (None, [[0.7486575293474405, 0.869192781456329]]), (None, [[2.78205542512966, 0.955353709243711]]), (None, [[3.517295342248655, 0.4728525136343702]]), (None, [[3.902147486365629, 1.8284511108225172]]), (None, [[4.993519238339136, 0.8232402866363913]])]:
            c.point(points, id=object_id, zorder=10, s=[50], facecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]], edgecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]])
        return c.save(output_path)
