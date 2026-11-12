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
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / 'Solid166_C01.png'
    with Canvas(SOLID, xlim=(-0.17034455212169997, 6.856642330527192), ylim=(-3.0834934413244457, 3.943493441324446), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        c.path([[0.0, 0.8660254037844386], [1.0, 0.8660254037844386], [0.5, 0.0], [0.0, 0.8660254037844386]], [1, 2, 2, 79], id='netface0', alpha=1.0, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt', simplify=False)
        c.line([[0.0, 0.8660254037844386], [1.0, 0.8660254037844386]], id='netedge0', zorder=3, clip_on=False, simplify=False)
        c.line([[1.0, 0.8660254037844386], [0.5, 0.0]], id='netedge1', zorder=3, clip_on=False, simplify=False)
        c.line([[0.5, 0.0], [0.0, 0.8660254037844386]], id='netedge2', zorder=3, clip_on=False, color='#DC2626', linewidth=1.5, solid_capstyle='butt', simplify=False)
        c.path([[0.5, 0.0], [1.0, 0.8660254037844386], [1.5, 0.0], [0.5, 0.0]], [1, 2, 2, 79], id='netface1', alpha=1.0, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt', simplify=False)
        c.line([[1.0, 0.8660254037844386], [1.5, 0.0]], id='netedge3', zorder=3, clip_on=False, simplify=False)
        c.line([[1.5, 0.0], [0.5, 0.0]], id='netedge4', zorder=3, clip_on=False, simplify=False)
        c.path([[1.0, 0.8660254037844386], [2.0, 0.8660254037844386], [1.5, 0.0], [1.0, 0.8660254037844386]], [1, 2, 2, 79], id='netface2', alpha=1.0, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt', simplify=False)
        c.line([[1.0, 0.8660254037844386], [2.0, 0.8660254037844386]], id='netedge5', zorder=3, clip_on=False, simplify=False)
        c.line([[2.0, 0.8660254037844386], [1.5, 0.0]], id='netedge6', zorder=3, clip_on=False, simplify=False)
        c.path([[1.5, 0.0], [2.0, 0.8660254037844386], [2.5, 0.0], [1.5, 0.0]], [1, 2, 2, 79], id='netface3', alpha=1.0, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt', simplify=False)
        c.line([[2.0, 0.8660254037844386], [2.5, 0.0]], id='netedge7', zorder=3, clip_on=False, simplify=False)
        c.line([[2.5, 0.0], [1.5, 0.0]], id='netedge8', zorder=3, clip_on=False, simplify=False)
        c.path([[2.0, 0.8660254037844386], [3.0, 0.8660254037844386], [2.5, 0.0], [2.0, 0.8660254037844386]], [1, 2, 2, 79], id='netface4', alpha=1.0, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt', simplify=False)
        c.line([[2.0, 0.8660254037844386], [3.0, 0.8660254037844386]], id='netedge9', zorder=3, clip_on=False, simplify=False)
        c.line([[3.0, 0.8660254037844386], [2.5, 0.0]], id='netedge10', zorder=3, clip_on=False, simplify=False)
        c.path([[2.5, 0.0], [3.0, 0.8660254037844386], [3.5, 0.0], [2.5, 0.0]], [1, 2, 2, 79], id='netface5', alpha=1.0, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt', simplify=False)
        c.line([[3.0, 0.8660254037844386], [3.5, 0.0]], id='netedge11', zorder=3, clip_on=False, simplify=False)
        c.line([[3.5, 0.0], [2.5, 0.0]], id='netedge12', zorder=3, clip_on=False, simplify=False)
        c.path([[0.0, 0.8660254037844386], [0.5, 1.7320508075688772], [1.0, 0.8660254037844386], [0.0, 0.8660254037844386]], [1, 2, 2, 79], id='netface6', alpha=1.0, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt', simplify=False)
        c.line([[0.0, 0.8660254037844386], [0.5, 1.7320508075688772]], id='netedge13', zorder=3, clip_on=False, simplify=False)
        c.line([[0.5, 1.7320508075688772], [1.0, 0.8660254037844386]], id='netedge14', zorder=3, clip_on=False, simplify=False)
        c.path([[2.5, 0.0], [3.5, 0.0], [3.0, -0.8660254037844386], [2.5, 0.0]], [1, 2, 2, 79], id='netface7', alpha=1.0, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt', simplify=False)
        c.line([[3.5, 0.0], [3.0, -0.8660254037844386]], id='netedge15', zorder=3, clip_on=False, color='#DC2626', linewidth=1.5, solid_capstyle='butt', simplify=False)
        for object_id, points in [('netedge16', [[3.0, -0.8660254037844386], [2.5, 0.0]]), ('octa0-11-1', [[4.014935923627798, 0.4780638448170429], [5.14974038854417, 0.10957436788638075]]), ('octa1-12-1', [[5.14974038854417, 0.10957436788638075], [5.35, -0.8805408353447026]]), ('octa0-12-1', [[4.014935923627798, 0.4780638448170429], [5.35, -0.8805408353447026]]), ('octa1-121', [[5.14974038854417, 0.10957436788638075], [5.35, 1.7405408353447025]]), ('octa0-121', [[4.014935923627798, 0.4780638448170429], [5.35, 1.7405408353447025]])]:
            c.line(points, id=object_id, zorder=3, clip_on=False, simplify=False)
        for object_id, points in [('octa0-111', [[4.014935923627798, 0.4780638448170429], [5.55025961145583, 0.7504256321136192]]), ('octa112-1', [[5.55025961145583, 0.7504256321136192], [5.35, -0.8805408353447026]]), ('octa1121', [[5.55025961145583, 0.7504256321136192], [5.35, 1.7405408353447025]])]:
            c.line(points, id=object_id, clip_on=False, linestyle=(0.0, [4.0, 3.0]), simplify=False)
        for object_id, points in [('octa011-1', [[6.685064076372202, 0.3819361551829571], [5.14974038854417, 0.10957436788638075]]), ('octa012-1', [[6.685064076372202, 0.3819361551829571], [5.35, -0.8805408353447026]]), ('octa0121', [[6.685064076372202, 0.3819361551829571], [5.35, 1.7405408353447025]])]:
            c.line(points, id=object_id, zorder=3, clip_on=False, simplify=False)
        c.line([[6.685064076372202, 0.3819361551829571], [5.55025961145583, 0.7504256321136192]], id='octa0111', clip_on=False, linestyle=(0.0, [4.0, 3.0]), simplify=False)
        c.text('3', (0.25, 1.299038105676658), id='edge_label3', rotation_mode='default', offset_pt=(-14, 4), annotation_clip=None)
        c.text('4', (0.25, 0.4330127018922193), id='edge_label4', rotation_mode='default', offset_pt=(-14, -4), annotation_clip=None)
        c.text('5', (1.0, 0.0), id='edge_label5', rotation_mode='default', offset_pt=(0, -17), annotation_clip=None)
        c.text('2', (2.5, 0.8660254037844386), id='edge_label2', rotation_mode='default', offset_pt=(0, 18), annotation_clip=None)
        c.text('1', (3.25, 0.4330127018922193), id='edge_label1', rotation_mode='default', offset_pt=(16, 4), annotation_clip=None)
        c.text('x', (3.25, -0.4330127018922193), id='edge_labelx', rotation_mode='default', offset_pt=(17, -3), annotation_clip=None)
        return c.save(output_path)

def C02(output_path=None):
    if output_path is None:
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / 'Solid166_C02.png'
    with Canvas(SOLID, xlim=(-0.17034455212169997, 6.856642330527192), ylim=(-3.0834934413244457, 3.943493441324446), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        c.path([[0.0, 0.8660254037844386], [1.0, 0.8660254037844386], [0.5, 0.0], [0.0, 0.8660254037844386]], [1, 2, 2, 79], id='netface0', alpha=1.0, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt', simplify=False)
        c.line([[0.0, 0.8660254037844386], [1.0, 0.8660254037844386]], id='netedge0', zorder=3, clip_on=False, simplify=False)
        c.line([[1.0, 0.8660254037844386], [0.5, 0.0]], id='netedge1', zorder=3, clip_on=False, simplify=False)
        c.line([[0.5, 0.0], [0.0, 0.8660254037844386]], id='netedge2', zorder=3, clip_on=False, color='#DC2626', linewidth=1.5, solid_capstyle='butt', simplify=False)
        c.path([[0.5, 0.0], [1.0, 0.8660254037844386], [1.5, 0.0], [0.5, 0.0]], [1, 2, 2, 79], id='netface1', alpha=1.0, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt', simplify=False)
        c.line([[1.0, 0.8660254037844386], [1.5, 0.0]], id='netedge3', zorder=3, clip_on=False, simplify=False)
        c.line([[1.5, 0.0], [0.5, 0.0]], id='netedge4', zorder=3, clip_on=False, simplify=False)
        c.path([[1.0, 0.8660254037844386], [2.0, 0.8660254037844386], [1.5, 0.0], [1.0, 0.8660254037844386]], [1, 2, 2, 79], id='netface2', alpha=1.0, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt', simplify=False)
        c.line([[1.0, 0.8660254037844386], [2.0, 0.8660254037844386]], id='netedge5', zorder=3, clip_on=False, simplify=False)
        c.line([[2.0, 0.8660254037844386], [1.5, 0.0]], id='netedge6', zorder=3, clip_on=False, simplify=False)
        c.path([[1.5, 0.0], [2.0, 0.8660254037844386], [2.5, 0.0], [1.5, 0.0]], [1, 2, 2, 79], id='netface3', alpha=1.0, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt', simplify=False)
        c.line([[2.0, 0.8660254037844386], [2.5, 0.0]], id='netedge7', zorder=3, clip_on=False, simplify=False)
        c.line([[2.5, 0.0], [1.5, 0.0]], id='netedge8', zorder=3, clip_on=False, simplify=False)
        c.path([[2.0, 0.8660254037844386], [3.0, 0.8660254037844386], [2.5, 0.0], [2.0, 0.8660254037844386]], [1, 2, 2, 79], id='netface4', alpha=1.0, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt', simplify=False)
        c.line([[2.0, 0.8660254037844386], [3.0, 0.8660254037844386]], id='netedge9', zorder=3, clip_on=False, simplify=False)
        c.line([[3.0, 0.8660254037844386], [2.5, 0.0]], id='netedge10', zorder=3, clip_on=False, simplify=False)
        c.path([[2.5, 0.0], [3.0, 0.8660254037844386], [3.5, 0.0], [2.5, 0.0]], [1, 2, 2, 79], id='netface5', alpha=1.0, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt', simplify=False)
        c.line([[3.0, 0.8660254037844386], [3.5, 0.0]], id='netedge11', zorder=3, clip_on=False, simplify=False)
        c.line([[3.5, 0.0], [2.5, 0.0]], id='netedge12', zorder=3, clip_on=False, simplify=False)
        c.path([[0.0, 0.8660254037844386], [0.5, 1.7320508075688772], [1.0, 0.8660254037844386], [0.0, 0.8660254037844386]], [1, 2, 2, 79], id='netface6', alpha=1.0, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt', simplify=False)
        c.line([[0.0, 0.8660254037844386], [0.5, 1.7320508075688772]], id='netedge13', zorder=3, clip_on=False, color='#2563EB', simplify=False)
        c.line([[0.5, 1.7320508075688772], [1.0, 0.8660254037844386]], id='netedge14', zorder=3, clip_on=False, simplify=False)
        c.path([[2.5, 0.0], [3.5, 0.0], [3.0, -0.8660254037844386], [2.5, 0.0]], [1, 2, 2, 79], id='netface7', alpha=1.0, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt', simplify=False)
        c.line([[3.5, 0.0], [3.0, -0.8660254037844386]], id='netedge15', zorder=3, clip_on=False, color='#DC2626', linewidth=1.5, solid_capstyle='butt', simplify=False)
        c.line([[3.0, -0.8660254037844386], [2.5, 0.0]], id='netedge16', zorder=3, clip_on=False, color='#2563EB', simplify=False)
        for object_id, points in [('octa0-11-1', [[4.014935923627798, 0.4780638448170429], [5.14974038854417, 0.10957436788638075]]), ('octa1-12-1', [[5.14974038854417, 0.10957436788638075], [5.35, -0.8805408353447026]]), ('octa0-12-1', [[4.014935923627798, 0.4780638448170429], [5.35, -0.8805408353447026]]), ('octa1-121', [[5.14974038854417, 0.10957436788638075], [5.35, 1.7405408353447025]]), ('octa0-121', [[4.014935923627798, 0.4780638448170429], [5.35, 1.7405408353447025]])]:
            c.line(points, id=object_id, zorder=3, clip_on=False, simplify=False)
        for object_id, points in [('octa0-111', [[4.014935923627798, 0.4780638448170429], [5.55025961145583, 0.7504256321136192]]), ('octa112-1', [[5.55025961145583, 0.7504256321136192], [5.35, -0.8805408353447026]]), ('octa1121', [[5.55025961145583, 0.7504256321136192], [5.35, 1.7405408353447025]])]:
            c.line(points, id=object_id, clip_on=False, linestyle=(0.0, [4.0, 3.0]), simplify=False)
        for object_id, points in [('octa011-1', [[6.685064076372202, 0.3819361551829571], [5.14974038854417, 0.10957436788638075]]), ('octa012-1', [[6.685064076372202, 0.3819361551829571], [5.35, -0.8805408353447026]]), ('octa0121', [[6.685064076372202, 0.3819361551829571], [5.35, 1.7405408353447025]])]:
            c.line(points, id=object_id, zorder=3, clip_on=False, simplify=False)
        c.line([[6.685064076372202, 0.3819361551829571], [5.55025961145583, 0.7504256321136192]], id='octa0111', clip_on=False, linestyle=(0.0, [4.0, 3.0]), simplify=False)
        c.text('3', (0.25, 1.299038105676658), id='edge_label3', rotation_mode='default', offset_pt=(-14, 4), annotation_clip=None)
        c.text('4', (0.25, 0.4330127018922193), id='edge_label4', rotation_mode='default', offset_pt=(-14, -4), annotation_clip=None)
        c.text('5', (1.0, 0.0), id='edge_label5', rotation_mode='default', offset_pt=(0, -17), annotation_clip=None)
        c.text('2', (2.5, 0.8660254037844386), id='edge_label2', rotation_mode='default', offset_pt=(0, 18), annotation_clip=None)
        c.text('1', (3.25, 0.4330127018922193), id='edge_label1', rotation_mode='default', offset_pt=(16, 4), annotation_clip=None)
        c.text('x', (3.25, -0.4330127018922193), id='edge_labelx', rotation_mode='default', offset_pt=(17, -3), annotation_clip=None)
        return c.save(output_path)

def C03(output_path=None):
    if output_path is None:
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / 'Solid166_C03.png'
    with Canvas(SOLID, xlim=(-0.17034455212169997, 6.856642330527192), ylim=(-3.0834934413244457, 3.943493441324446), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        c.path([[0.0, 0.8660254037844386], [1.0, 0.8660254037844386], [0.5, 0.0], [0.0, 0.8660254037844386]], [1, 2, 2, 79], id='netface0', alpha=1.0, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
        for object_id, points in [('netedge0', [[0.0, 0.8660254037844386], [1.0, 0.8660254037844386]]), ('netedge1', [[1.0, 0.8660254037844386], [0.5, 0.0]]), ('netedge2', [[0.5, 0.0], [0.0, 0.8660254037844386]])]:
            c.line(points, id=object_id, zorder=3, clip_on=False)
        c.path([[0.5, 0.0], [1.0, 0.8660254037844386], [1.5, 0.0], [0.5, 0.0]], [1, 2, 2, 79], id='netface1', alpha=1.0, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
        c.line([[1.0, 0.8660254037844386], [1.5, 0.0]], id='netedge3', zorder=3, clip_on=False)
        c.line([[1.5, 0.0], [0.5, 0.0]], id='netedge4', zorder=3, clip_on=False)
        c.path([[1.0, 0.8660254037844386], [2.0, 0.8660254037844386], [1.5, 0.0], [1.0, 0.8660254037844386]], [1, 2, 2, 79], id='netface2', alpha=1.0, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
        c.line([[1.0, 0.8660254037844386], [2.0, 0.8660254037844386]], id='netedge5', zorder=3, clip_on=False)
        c.line([[2.0, 0.8660254037844386], [1.5, 0.0]], id='netedge6', zorder=3, clip_on=False)
        c.path([[1.5, 0.0], [2.0, 0.8660254037844386], [2.5, 0.0], [1.5, 0.0]], [1, 2, 2, 79], id='netface3', alpha=1.0, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
        c.line([[2.0, 0.8660254037844386], [2.5, 0.0]], id='netedge7', zorder=3, clip_on=False)
        c.line([[2.5, 0.0], [1.5, 0.0]], id='netedge8', zorder=3, clip_on=False)
        c.path([[2.0, 0.8660254037844386], [3.0, 0.8660254037844386], [2.5, 0.0], [2.0, 0.8660254037844386]], [1, 2, 2, 79], id='netface4', alpha=1.0, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
        c.line([[2.0, 0.8660254037844386], [3.0, 0.8660254037844386]], id='netedge9', zorder=3, clip_on=False)
        c.line([[3.0, 0.8660254037844386], [2.5, 0.0]], id='netedge10', zorder=3, clip_on=False)
        c.path([[2.5, 0.0], [3.0, 0.8660254037844386], [3.5, 0.0], [2.5, 0.0]], [1, 2, 2, 79], id='netface5', alpha=1.0, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
        c.line([[3.0, 0.8660254037844386], [3.5, 0.0]], id='netedge11', zorder=3, clip_on=False)
        c.line([[3.5, 0.0], [2.5, 0.0]], id='netedge12', zorder=3, clip_on=False)
        c.path([[0.0, 0.8660254037844386], [0.5, 1.7320508075688772], [1.0, 0.8660254037844386], [0.0, 0.8660254037844386]], [1, 2, 2, 79], id='netface6', alpha=1.0, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
        c.line([[0.0, 0.8660254037844386], [0.5, 1.7320508075688772]], id='netedge13', zorder=3, clip_on=False, color='#DC2626')
        c.line([[0.5, 1.7320508075688772], [1.0, 0.8660254037844386]], id='netedge14', zorder=3, clip_on=False, color='#2563EB')
        c.path([[2.5, 0.0], [3.5, 0.0], [3.0, -0.8660254037844386], [2.5, 0.0]], [1, 2, 2, 79], id='netface7', alpha=1.0, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
        c.line([[3.5, 0.0], [3.0, -0.8660254037844386]], id='netedge15', zorder=3, clip_on=False, color='#DC2626')
        c.line([[3.0, -0.8660254037844386], [2.5, 0.0]], id='netedge16', zorder=3, clip_on=False, color='#2563EB')
        for object_id, points in [('octa0-11-1', [[4.014935923627798, 0.4780638448170429], [5.14974038854417, 0.10957436788638075]]), ('octa1-12-1', [[5.14974038854417, 0.10957436788638075], [5.35, -0.8805408353447026]]), ('octa0-12-1', [[4.014935923627798, 0.4780638448170429], [5.35, -0.8805408353447026]]), ('octa1-121', [[5.14974038854417, 0.10957436788638075], [5.35, 1.7405408353447025]]), ('octa0-121', [[4.014935923627798, 0.4780638448170429], [5.35, 1.7405408353447025]])]:
            c.line(points, id=object_id, zorder=3, clip_on=False)
        for object_id, points in [('octa0-111', [[4.014935923627798, 0.4780638448170429], [5.55025961145583, 0.7504256321136192]]), ('octa112-1', [[5.55025961145583, 0.7504256321136192], [5.35, -0.8805408353447026]]), ('octa1121', [[5.55025961145583, 0.7504256321136192], [5.35, 1.7405408353447025]])]:
            c.line(points, id=object_id, clip_on=False, linestyle=(0.0, [4.0, 3.0]))
        for object_id, points in [('octa011-1', [[6.685064076372202, 0.3819361551829571], [5.14974038854417, 0.10957436788638075]]), ('octa012-1', [[6.685064076372202, 0.3819361551829571], [5.35, -0.8805408353447026]]), ('octa0121', [[6.685064076372202, 0.3819361551829571], [5.35, 1.7405408353447025]])]:
            c.line(points, id=object_id, zorder=3, clip_on=False)
        c.line([[6.685064076372202, 0.3819361551829571], [5.55025961145583, 0.7504256321136192]], id='octa0111', clip_on=False, linestyle=(0.0, [4.0, 3.0]))
        c.text('3', (0.25, 1.299038105676658), id='edge_label3', rotation_mode='default', offset_pt=(-14, 4), annotation_clip=None)
        c.text('4', (0.25, 0.4330127018922193), id='edge_label4', rotation_mode='default', offset_pt=(-14, -4), annotation_clip=None)
        c.text('5', (1.0, 0.0), id='edge_label5', rotation_mode='default', offset_pt=(0, -17), annotation_clip=None)
        c.text('2', (2.5, 0.8660254037844386), id='edge_label2', rotation_mode='default', offset_pt=(0, 18), annotation_clip=None)
        c.text('1', (3.25, 0.4330127018922193), id='edge_label1', rotation_mode='default', offset_pt=(16, 4), annotation_clip=None)
        c.text('x', (3.25, -0.4330127018922193), id='edge_labelx', rotation_mode='default', offset_pt=(17, -3), annotation_clip=None)
        return c.save(output_path)

def C04(output_path=None):
    if output_path is None:
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / 'Solid166_C04.png'
    with Canvas(SOLID, xlim=(-0.17034455212169997, 6.856642330527192), ylim=(-3.0834934413244457, 3.943493441324446), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        c.path([[0.0, 0.8660254037844386], [1.0, 0.8660254037844386], [0.5, 0.0], [0.0, 0.8660254037844386]], [1, 2, 2, 79], id='netface0', alpha=1.0, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
        c.line([[0.0, 0.8660254037844386], [1.0, 0.8660254037844386]], id='netedge0', zorder=3, clip_on=False, color='#EA580C')
        c.line([[1.0, 0.8660254037844386], [0.5, 0.0]], id='netedge1', zorder=3, clip_on=False)
        c.line([[0.5, 0.0], [0.0, 0.8660254037844386]], id='netedge2', zorder=3, clip_on=False)
        c.path([[0.5, 0.0], [1.0, 0.8660254037844386], [1.5, 0.0], [0.5, 0.0]], [1, 2, 2, 79], id='netface1', alpha=1.0, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
        c.line([[1.0, 0.8660254037844386], [1.5, 0.0]], id='netedge3', zorder=3, clip_on=False)
        c.line([[1.5, 0.0], [0.5, 0.0]], id='netedge4', zorder=3, clip_on=False)
        c.path([[1.0, 0.8660254037844386], [2.0, 0.8660254037844386], [1.5, 0.0], [1.0, 0.8660254037844386]], [1, 2, 2, 79], id='netface2', alpha=1.0, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
        c.line([[1.0, 0.8660254037844386], [2.0, 0.8660254037844386]], id='netedge5', zorder=3, clip_on=False)
        c.line([[2.0, 0.8660254037844386], [1.5, 0.0]], id='netedge6', zorder=3, clip_on=False)
        c.path([[1.5, 0.0], [2.0, 0.8660254037844386], [2.5, 0.0], [1.5, 0.0]], [1, 2, 2, 79], id='netface3', alpha=1.0, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
        c.line([[2.0, 0.8660254037844386], [2.5, 0.0]], id='netedge7', zorder=3, clip_on=False)
        c.line([[2.5, 0.0], [1.5, 0.0]], id='netedge8', zorder=3, clip_on=False)
        c.path([[2.0, 0.8660254037844386], [3.0, 0.8660254037844386], [2.5, 0.0], [2.0, 0.8660254037844386]], [1, 2, 2, 79], id='netface4', alpha=1.0, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
        c.line([[2.0, 0.8660254037844386], [3.0, 0.8660254037844386]], id='netedge9', zorder=3, clip_on=False)
        c.line([[3.0, 0.8660254037844386], [2.5, 0.0]], id='netedge10', zorder=3, clip_on=False)
        c.path([[2.5, 0.0], [3.0, 0.8660254037844386], [3.5, 0.0], [2.5, 0.0]], [1, 2, 2, 79], id='netface5', alpha=1.0, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
        c.line([[3.0, 0.8660254037844386], [3.5, 0.0]], id='netedge11', zorder=3, clip_on=False)
        c.line([[3.5, 0.0], [2.5, 0.0]], id='netedge12', zorder=3, clip_on=False, color='#EA580C')
        c.path([[0.0, 0.8660254037844386], [0.5, 1.7320508075688772], [1.0, 0.8660254037844386], [0.0, 0.8660254037844386]], [1, 2, 2, 79], id='netface6', alpha=1.0, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
        c.line([[0.0, 0.8660254037844386], [0.5, 1.7320508075688772]], id='netedge13', zorder=3, clip_on=False)
        c.line([[0.5, 1.7320508075688772], [1.0, 0.8660254037844386]], id='netedge14', zorder=3, clip_on=False, color='#16A34A')
        c.path([[2.5, 0.0], [3.5, 0.0], [3.0, -0.8660254037844386], [2.5, 0.0]], [1, 2, 2, 79], id='netface7', alpha=1.0, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
        c.line([[3.5, 0.0], [3.0, -0.8660254037844386]], id='netedge15', zorder=3, clip_on=False)
        c.line([[3.0, -0.8660254037844386], [2.5, 0.0]], id='netedge16', zorder=3, clip_on=False, color='#16A34A')
        for object_id, points in [('octa0-11-1', [[4.014935923627798, 0.4780638448170429], [5.14974038854417, 0.10957436788638075]]), ('octa1-12-1', [[5.14974038854417, 0.10957436788638075], [5.35, -0.8805408353447026]]), ('octa0-12-1', [[4.014935923627798, 0.4780638448170429], [5.35, -0.8805408353447026]]), ('octa1-121', [[5.14974038854417, 0.10957436788638075], [5.35, 1.7405408353447025]]), ('octa0-121', [[4.014935923627798, 0.4780638448170429], [5.35, 1.7405408353447025]])]:
            c.line(points, id=object_id, zorder=3, clip_on=False)
        for object_id, points in [('octa0-111', [[4.014935923627798, 0.4780638448170429], [5.55025961145583, 0.7504256321136192]]), ('octa112-1', [[5.55025961145583, 0.7504256321136192], [5.35, -0.8805408353447026]]), ('octa1121', [[5.55025961145583, 0.7504256321136192], [5.35, 1.7405408353447025]])]:
            c.line(points, id=object_id, clip_on=False, linestyle=(0.0, [4.0, 3.0]))
        for object_id, points in [('octa011-1', [[6.685064076372202, 0.3819361551829571], [5.14974038854417, 0.10957436788638075]]), ('octa012-1', [[6.685064076372202, 0.3819361551829571], [5.35, -0.8805408353447026]]), ('octa0121', [[6.685064076372202, 0.3819361551829571], [5.35, 1.7405408353447025]])]:
            c.line(points, id=object_id, zorder=3, clip_on=False)
        c.line([[6.685064076372202, 0.3819361551829571], [5.55025961145583, 0.7504256321136192]], id='octa0111', clip_on=False, linestyle=(0.0, [4.0, 3.0]))
        c.text('3', (0.25, 1.299038105676658), id='edge_label3', rotation_mode='default', offset_pt=(-14, 4), annotation_clip=None)
        c.text('4', (0.25, 0.4330127018922193), id='edge_label4', rotation_mode='default', offset_pt=(-14, -4), annotation_clip=None)
        c.text('5', (1.0, 0.0), id='edge_label5', rotation_mode='default', offset_pt=(0, -17), annotation_clip=None)
        c.text('2', (2.5, 0.8660254037844386), id='edge_label2', rotation_mode='default', offset_pt=(0, 18), annotation_clip=None)
        c.text('1', (3.25, 0.4330127018922193), id='edge_label1', rotation_mode='default', offset_pt=(16, 4), annotation_clip=None)
        c.text('x', (3.25, -0.4330127018922193), id='edge_labelx', rotation_mode='default', offset_pt=(17, -3), annotation_clip=None)
        return c.save(output_path)
