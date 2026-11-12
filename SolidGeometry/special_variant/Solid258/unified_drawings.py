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
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / 'Solid258_C01.png'
    with Canvas(SOLID, xlim=(-0.5797543700066932, 4.7213653097824935), ylim=(-1.263421026937027, 4.03769865285216), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        for object_id, points in [('edge_000_010', [[0.0, 0.0], [1.6106264765794776, 1.7870346869633513]]), ('edge_010_110', [[1.6106264765794776, 1.7870346869633513], [4.1416109397758, 0.6498307952594005]]), ('edge_010_011', [[1.6106264765794776, 1.7870346869633513], [1.6106264765794776, 3.911481517619084]])]:
            c.line(points, id=object_id, linestyle=(0.0, [4.0, 3.0]))
        c.path([[1.1102230246251565e-16, 2.220446049250313e-16], [0.8436614877321075, -0.3790679639013167]], [1, 2], id='edge_000_100', joinstyle='round', fill=False)
        c.path([[0.8436614877321074, -0.3790679639013167], [1.6873229754642147, -0.7581359278026336]], [1, 2], id='edge_000_100', edgecolor=(0.1450980392156863, 0.38823529411764707, 0.9215686274509803, 1.0), linewidth=2.0, joinstyle='round', fill=False)
        c.path([[1.6873229754642147, -0.7581359278026336], [2.5309844631963223, -1.1372038917039506]], [1, 2], id='edge_000_100', joinstyle='round', fill=False)
        c.line([[0.0, 0.0], [0.0, 2.1244468306557325]], id='edge_000_001')
        c.path([[1.1102230246251565e-16, 2.1244468306557325], [0.8436614877321075, 1.745378866754416]], [1, 2], id='edge_001_101', joinstyle='round', fill=False)
        c.path([[0.8436614877321074, 1.7453788667544157], [1.6873229754642147, 1.3663109028530989]], [1, 2], id='edge_001_101', edgecolor=(0.1450980392156863, 0.38823529411764707, 0.9215686274509803, 1.0), linewidth=2.0, joinstyle='round', fill=False)
        c.path([[1.6873229754642147, 1.3663109028530989], [2.5309844631963223, 0.9872429389517818]], [1, 2], id='edge_001_101', joinstyle='round', fill=False)
        for object_id, points in [('edge_001_011', [[0.0, 2.1244468306557325], [1.6106264765794776, 3.911481517619084]]), ('edge_011_111', [[1.6106264765794776, 3.911481517619084], [4.1416109397758, 2.7742776259151327]]), ('edge_100_110', [[2.5309844631963223, -1.1372038917039509], [4.1416109397758, 0.6498307952594005]]), ('edge_100_101', [[2.5309844631963223, -1.1372038917039509], [2.5309844631963223, 0.9872429389517816]]), ('edge_101_111', [[2.5309844631963223, 0.9872429389517816], [4.1416109397758, 2.7742776259151327]]), ('edge_110_111', [[4.1416109397758, 0.6498307952594005], [4.1416109397758, 2.7742776259151327]])]:
            c.line(points, id=object_id)
        for object_id, points in [(None, [[1.687322975464215, 1.3663109028530984]]), (None, [[3.0678599553894816, 1.5829211679395654]]), (None, [[2.5309844631963223, 0.2790939953998708]])]:
            c.point(points, id=object_id)
        c.text('A', (2.5309844631963223, 0.9872429389517816), zorder=3, clip_on=True, fontsize=18.0, fontstyle='italic', ha='left', va='top', rotation_mode='default', offset_pt=(9, -7), annotation_clip=None)
        c.text('P', (1.687322975464215, 1.3663109028530984), zorder=3, clip_on=True, fontsize=18.0, fontstyle='italic', ha='right', va='bottom', rotation_mode='default', offset_pt=(-4, 7), annotation_clip=None)
        c.text('Q', (3.0678599553894816, 1.5829211679395654), zorder=3, clip_on=True, fontsize=18.0, fontstyle='italic', ha='right', va='bottom', rotation_mode='default', offset_pt=(-6, 8), annotation_clip=None)
        c.text('R', (2.5309844631963223, 0.2790939953998708), zorder=3, clip_on=True, fontsize=18.0, fontstyle='italic', ha='left', rotation_mode='default', offset_pt=(9, 0), annotation_clip=None)
        c.line([[1.687322975464215, 1.3663109028530984], [2.5309844631963223, 0.2790939953998708]], zorder=9, color='#EA580C', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
        return c.save(output_path)

def C02(output_path=None):
    if output_path is None:
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / 'Solid258_C02.png'
    with Canvas(SOLID, xlim=(-0.5797543700066932, 4.7213653097824935), ylim=(-1.263421026937027, 4.03769865285216), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        for object_id, points in [('edge_000_010', [[0.0, 0.0], [1.6106264765794776, 1.7870346869633513]]), ('edge_010_110', [[1.6106264765794776, 1.7870346869633513], [4.1416109397758, 0.6498307952594005]]), ('edge_010_011', [[1.6106264765794776, 1.7870346869633513], [1.6106264765794776, 3.911481517619084]])]:
            c.line(points, id=object_id, linestyle=(0.0, [4.0, 3.0]))
        for object_id, points in [('edge_000_100', [[0.0, 0.0], [2.5309844631963223, -1.1372038917039509]]), ('edge_000_001', [[0.0, 0.0], [0.0, 2.1244468306557325]]), ('edge_001_101', [[0.0, 2.1244468306557325], [2.5309844631963223, 0.9872429389517816]]), ('edge_001_011', [[0.0, 2.1244468306557325], [1.6106264765794776, 3.911481517619084]]), ('edge_011_111', [[1.6106264765794776, 3.911481517619084], [4.1416109397758, 2.7742776259151327]])]:
            c.line(points, id=object_id)
        c.path([[2.5309844631963223, -1.1372038917039506], [3.0678599553894816, -0.541525662716167]], [1, 2], id='edge_100_110', edgecolor=(0.1450980392156863, 0.38823529411764707, 0.9215686274509803, 1.0), linewidth=2.0, joinstyle='round', fill=False)
        c.path([[3.0678599553894816, -0.5415256627161669], [3.604735447582641, 0.05415256627161685]], [1, 2], id='edge_100_110', joinstyle='round', fill=False)
        c.path([[3.604735447582641, 0.05415256627161685], [4.1416109397758, 0.6498307952594007]], [1, 2], id='edge_100_110', edgecolor=(0.1450980392156863, 0.38823529411764707, 0.9215686274509803, 1.0), linewidth=2.0, joinstyle='round', fill=False)
        c.path([[2.5309844631963223, -1.1372038917039506], [2.5309844631963223, -0.42905494815203993]], [1, 2], id='edge_100_101', edgecolor=(0.1450980392156863, 0.38823529411764707, 0.9215686274509803, 1.0), linewidth=2.0, joinstyle='round', fill=False)
        c.path([[2.5309844631963223, -0.4290549481520399], [2.5309844631963223, 0.2790939953998709]], [1, 2], id='edge_100_101', joinstyle='round', fill=False)
        c.path([[2.5309844631963223, 0.2790939953998709], [2.5309844631963223, 0.9872429389517818]], [1, 2], id='edge_100_101', edgecolor=(0.1450980392156863, 0.38823529411764707, 0.9215686274509803, 1.0), linewidth=2.0, joinstyle='round', fill=False)
        c.path([[2.5309844631963223, 0.9872429389517818], [3.0678599553894816, 1.5829211679395656]], [1, 2], id='edge_101_111', edgecolor=(0.1450980392156863, 0.38823529411764707, 0.9215686274509803, 1.0), linewidth=2.0, joinstyle='round', fill=False)
        c.path([[3.0678599553894816, 1.5829211679395654], [3.604735447582641, 2.178599396927349]], [1, 2], id='edge_101_111', joinstyle='round', fill=False)
        c.path([[3.604735447582641, 2.178599396927349], [4.1416109397758, 2.7742776259151327]], [1, 2], id='edge_101_111', edgecolor=(0.1450980392156863, 0.38823529411764707, 0.9215686274509803, 1.0), linewidth=2.0, joinstyle='round', fill=False)
        c.path([[4.1416109397758, 0.6498307952594007], [4.1416109397758, 1.3579797388113115]], [1, 2], id='edge_110_111', edgecolor=(0.1450980392156863, 0.38823529411764707, 0.9215686274509803, 1.0), linewidth=2.0, joinstyle='round', fill=False)
        c.path([[4.1416109397758, 1.3579797388113113], [4.1416109397758, 2.066128682363222]], [1, 2], id='edge_110_111', joinstyle='round', fill=False)
        c.path([[4.1416109397758, 2.066128682363222], [4.1416109397758, 2.7742776259151327]], [1, 2], id='edge_110_111', edgecolor=(0.1450980392156863, 0.38823529411764707, 0.9215686274509803, 1.0), linewidth=2.0, joinstyle='round', fill=False)
        for object_id, points in [(None, [[1.687322975464215, 1.3663109028530984]]), (None, [[3.0678599553894816, 1.5829211679395654]]), (None, [[2.5309844631963223, 0.2790939953998708]])]:
            c.point(points, id=object_id)
        c.text('A', (2.5309844631963223, 0.9872429389517816), zorder=3, clip_on=True, fontsize=18.0, fontstyle='italic', ha='left', va='top', rotation_mode='default', offset_pt=(9, -7), annotation_clip=None)
        c.text('P', (1.687322975464215, 1.3663109028530984), zorder=3, clip_on=True, fontsize=18.0, fontstyle='italic', ha='right', va='bottom', rotation_mode='default', offset_pt=(-4, 7), annotation_clip=None)
        c.text('Q', (3.0678599553894816, 1.5829211679395654), zorder=3, clip_on=True, fontsize=18.0, fontstyle='italic', ha='right', va='bottom', rotation_mode='default', offset_pt=(-6, 8), annotation_clip=None)
        c.text('R', (2.5309844631963223, 0.2790939953998708), zorder=3, clip_on=True, fontsize=18.0, fontstyle='italic', ha='left', rotation_mode='default', offset_pt=(9, 0), annotation_clip=None)
        for object_id, points in [(None, [[1.687322975464215, 1.3663109028530984], [3.0678599553894816, 1.5829211679395654]]), (None, [[3.0678599553894816, 1.5829211679395654], [2.5309844631963223, 0.2790939953998708]]), (None, [[2.5309844631963223, 0.2790939953998708], [1.687322975464215, 1.3663109028530984]])]:
            c.line(points, id=object_id, zorder=9, color='#EA580C', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
        return c.save(output_path)

def C03(output_path=None):
    if output_path is None:
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / 'Solid258_C03.png'
    with Canvas(SOLID, xlim=(-0.5797543700066932, 4.7213653097824935), ylim=(-1.263421026937027, 4.03769865285216), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        for object_id, points in [('edge_000_010', [[0.0, 0.0], [1.6106264765794776, 1.7870346869633513]]), ('edge_010_110', [[1.6106264765794776, 1.7870346869633513], [4.1416109397758, 0.6498307952594005]]), ('edge_010_011', [[1.6106264765794776, 1.7870346869633513], [1.6106264765794776, 3.911481517619084]])]:
            c.line(points, id=object_id, linestyle=(0.0, [4.0, 3.0]))
        for object_id, points in [('edge_000_100', [[0.0, 0.0], [2.5309844631963223, -1.1372038917039509]]), ('edge_000_001', [[0.0, 0.0], [0.0, 2.1244468306557325]]), ('edge_001_101', [[0.0, 2.1244468306557325], [2.5309844631963223, 0.9872429389517816]]), ('edge_001_011', [[0.0, 2.1244468306557325], [1.6106264765794776, 3.911481517619084]]), ('edge_011_111', [[1.6106264765794776, 3.911481517619084], [4.1416109397758, 2.7742776259151327]]), ('edge_100_110', [[2.5309844631963223, -1.1372038917039509], [4.1416109397758, 0.6498307952594005]]), ('edge_100_101', [[2.5309844631963223, -1.1372038917039509], [2.5309844631963223, 0.9872429389517816]])]:
            c.line(points, id=object_id)
        c.path([[2.5309844631963223, 0.9872429389517818], [3.0678599553894816, 1.5829211679395656]], [1, 2], id='edge_101_111', joinstyle='round', fill=False)
        c.path([[3.0678599553894816, 1.5829211679395654], [3.604735447582641, 2.178599396927349]], [1, 2], id='edge_101_111', edgecolor=(0.1450980392156863, 0.38823529411764707, 0.9215686274509803, 1.0), linewidth=2.0, joinstyle='round', fill=False)
        c.path([[3.604735447582641, 2.178599396927349], [4.1416109397758, 2.7742776259151327]], [1, 2], id='edge_101_111', joinstyle='round', fill=False)
        c.line([[4.1416109397758, 0.6498307952594005], [4.1416109397758, 2.7742776259151327]], id='edge_110_111')
        for object_id, points in [(None, [[1.687322975464215, 1.3663109028530984]]), (None, [[3.0678599553894816, 1.5829211679395654]]), (None, [[2.5309844631963223, 0.2790939953998708]])]:
            c.point(points, id=object_id)
        c.text('A', (2.5309844631963223, 0.9872429389517816), zorder=3, clip_on=True, fontsize=18.0, fontstyle='italic', ha='left', va='top', rotation_mode='default', offset_pt=(9, -7), annotation_clip=None)
        c.text('P', (1.687322975464215, 1.3663109028530984), zorder=3, clip_on=True, fontsize=18.0, fontstyle='italic', ha='right', va='bottom', rotation_mode='default', offset_pt=(-4, 7), annotation_clip=None)
        c.text('Q', (3.0678599553894816, 1.5829211679395654), zorder=3, clip_on=True, fontsize=18.0, fontstyle='italic', ha='right', va='bottom', rotation_mode='default', offset_pt=(-6, 8), annotation_clip=None)
        c.text('R', (2.5309844631963223, 0.2790939953998708), zorder=3, clip_on=True, fontsize=18.0, fontstyle='italic', ha='left', rotation_mode='default', offset_pt=(9, 0), annotation_clip=None)
        for object_id, points in [(None, [[3.0678599553894816, 1.5829211679395654], [2.5309844631963223, 0.2790939953998708]]), (None, [[3.604735447582641, 2.178599396927349], [4.1416109397758, 2.066128682363222]]), (None, [[2.5309844631963223, -0.42905494815204004], [3.0678599553894816, -0.5415256627161671]])]:
            c.line(points, id=object_id, zorder=9, color='#2563EB', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
        return c.save(output_path)
