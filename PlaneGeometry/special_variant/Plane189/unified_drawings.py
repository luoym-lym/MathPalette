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
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / 'Plane189_C01.png'
    with Canvas(PLANE, xlim=(-0.21014089856961427, 8.616984881607177), ylim=(-0.8883804470166909, 7.9387453331601), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        c.path([[0.0, 2.2], [8.4, 2.2], [8.4, 4.4], [0.0, 4.4], [0.0, 2.2]], [1, 2, 2, 2, 79], id='rectangle', edgecolor=(0.1450980392156863, 0.38823529411764707, 0.9215686274509803, 1.0), capstyle='butt')
        c.path([[0.3, 1.2], [6.15, 0.0], [6.15, 7.05], [0.3, 1.2]], [1, 2, 2, 79], id='triangle', linestyle=(0, [3.7, 1.6]), capstyle='butt')
        c.circle([4.65, 3.15], 2.6, id='circle', edgecolor=(0.1450980392156863, 0.38823529411764707, 0.9215686274509803, 1.0), fill=False)
        for object_id, text, anchor in [('label0', '1', (2.65, 4.0)), ('label1', '2', (1.2, 3.3)), ('label2', '3', (1.9, 2.45)), ('label3', '4', (4.5, 1.4)), ('label4', '5', (1.8, 1.55)), ('label5', '6', (3.4, 4.9)), ('label6', '7', (5.1, 5.0)), ('label7', '8', (5.8, 6.2)), ('label8', '9', (6.4, 4.85)), ('label9', '10', (6.65, 3.3)), ('label10', '11', (7.8, 3.3)), ('label11', '12', (6.5, 1.8)), ('label12', '13', (4.3, 3.3))]:
            c.text(text, anchor, id=object_id, rotation_mode='default', offset_pt=(0, 0), annotation_clip=None)
        return c.save(output_path)

def C02(output_path=None):
    if output_path is None:
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / 'Plane189_C02.png'
    with Canvas(PLANE, xlim=(-0.21014089856961427, 8.616984881607177), ylim=(-0.8883804470166909, 7.9387453331601), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        c.path([[0.0, 2.2], [8.4, 2.2], [8.4, 4.4], [0.0, 4.4], [0.0, 2.2]], [1, 2, 2, 2, 79], id='rectangle', capstyle='butt')
        c.path([[0.3, 1.2], [6.15, 0.0], [6.15, 7.05], [0.3, 1.2]], [1, 2, 2, 79], id='triangle', edgecolor=(0.1450980392156863, 0.38823529411764707, 0.9215686274509803, 1.0), capstyle='butt')
        c.circle([4.65, 3.15], 2.6, id='circle', edgecolor=(0.1450980392156863, 0.38823529411764707, 0.9215686274509803, 1.0), fill=False)
        for object_id, text, anchor in [('label0', '1', (2.65, 4.0)), ('label1', '2', (1.2, 3.3)), ('label2', '3', (1.9, 2.45)), ('label3', '4', (4.5, 1.4)), ('label4', '5', (1.8, 1.55)), ('label5', '6', (3.4, 4.9)), ('label6', '7', (5.1, 5.0)), ('label7', '8', (5.8, 6.2)), ('label8', '9', (6.4, 4.85)), ('label9', '10', (6.65, 3.3)), ('label10', '11', (7.8, 3.3)), ('label11', '12', (6.5, 1.8)), ('label12', '13', (4.3, 3.3))]:
            c.text(text, anchor, id=object_id, rotation_mode='default', offset_pt=(0, 0), annotation_clip=None)
        return c.save(output_path)

def C03(output_path=None):
    if output_path is None:
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / 'Plane189_C03.png'
    with Canvas(PLANE, xlim=(-0.21014089856961427, 8.616984881607177), ylim=(-0.8883804470166909, 7.9387453331601), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        c.path([[0.0, 2.2], [8.4, 2.2], [8.4, 4.4], [0.0, 4.4], [0.0, 2.2]], [1, 2, 2, 2, 79], id='rectangle', edgecolor='none', capstyle='butt')
        c.path([[0.0, 2.2], [1.2826818436661662, 2.2]], [1, 2], id='rectangle', capstyle='butt', fill=False)
        c.path([[1.2826818436661662, 2.2], [2.2652765230363365, 2.2]], [1, 2], id='rectangle', edgecolor=(0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0), linewidth=2.0, capstyle='butt', fill=False)
        c.path([[2.2652765230363365, 2.2], [8.4, 2.2], [8.4, 4.4], [6.943869537652099, 4.4]], [1, 2, 2, 2], id='rectangle', capstyle='butt', fill=False)
        c.path([[6.943869537652098, 4.4], [6.159596720173154, 4.4]], [1, 2], id='rectangle', edgecolor=(0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0), linewidth=2.0, capstyle='butt', fill=False)
        c.path([[6.159596720173154, 4.4], [0.0, 4.4], [0.0, 2.2]], [1, 2, 2], id='rectangle', capstyle='butt', fill=False)
        c.path([[0.3, 1.2], [6.15, 0.0], [6.15, 7.05], [0.3, 1.2]], [1, 2, 2, 79], id='triangle', edgecolor='none', capstyle='butt')
        c.path([[0.3, 1.2], [6.15, 0.0], [6.15, 4.435660081754153]], [1, 2, 2], id='triangle', capstyle='butt', fill=False)
        c.path([[6.15, 4.435660081754153], [6.15, 5.246976789490991]], [1, 2], id='triangle', edgecolor=(0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0), linewidth=2.0, capstyle='butt', fill=False)
        c.path([[6.15, 5.246976789490991], [6.15, 7.05], [2.062107704400514, 2.962107704400514]], [1, 2, 2], id='triangle', capstyle='butt', fill=False)
        c.path([[2.062107704400514, 2.9621077044005144], [1.3138934072654314, 2.2138934072654313]], [1, 2], id='triangle', edgecolor=(0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0), linewidth=2.0, capstyle='butt', fill=False)
        c.path([[1.3138934072654314, 2.2138934072654313], [0.3, 1.2]], [1, 2], id='triangle', capstyle='butt', fill=False)
        c.path([[4.65, 0.5500000000000003], [5.33952806, 0.5500000000000003], [6.00090766404062, 0.8239524018705717], [6.488477631085024, 1.3115223689149766], [6.976047598129429, 1.7990923359593813], [7.25, 2.46047194], [7.25, 3.1500000000000004], [7.25, 3.5925908302557064], [7.137130643876112, 4.023584397343346], [6.927347766910275, 4.404459907326269]], [1, 4, 4, 4, 4, 4, 4, 4, 4, 4], id='circle', capstyle='butt', fill=False)
        c.path([[6.927347766910275, 4.404459907326269], [6.81030240820774, 4.616963955948989], [6.6630886207646345, 4.813866641405413], [6.488477631085024, 4.988477631085024], [6.379794268978247, 5.0971609931918005], [6.262474639300891, 5.195230108111255], [6.138132068235652, 5.282016714257982]], [1, 4, 4, 4, 4, 4, 4], id='circle', edgecolor=(0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0), linewidth=2.0, capstyle='butt', fill=False)
        c.path([[6.138132068235652, 5.282016714257982], [5.704655097272621, 5.584567922829235], [5.18582657530429, 5.75], [4.65, 5.75], [3.96047194, 5.75], [3.299092335959381, 5.476047598129429], [2.811522368914977, 4.988477631085024], [2.3239524018705717, 4.50090766404062], [2.0500000000000003, 3.8395280600000006], [2.0500000000000003, 3.1500000000000004], [2.0500000000000003, 3.0854476630936243], [2.0524010165969537, 3.021142029298721], [2.057153544887609, 2.9572026140241245]], [1, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4], id='circle', capstyle='butt', fill=False)
        c.path([[2.0571535448876093, 2.957202614024125], [2.077239103037951, 2.6869761650575885], [2.139326231779802, 2.4232909351178424], [2.239677907880897, 2.1751688963751215]], [1, 4, 4, 4], id='circle', edgecolor=(0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0), linewidth=2.0, capstyle='butt', fill=False)
        c.path([[2.239677907880897, 2.1751688963751215], [2.369214397627353, 1.85488667313565], [2.5625084296261456, 1.560536308203808], [2.811522368914977, 1.3115223689149766], [3.299092335959381, 0.8239524018705717], [3.96047194, 0.5500000000000003], [4.65, 0.5500000000000003]], [1, 4, 4, 4, 4, 4, 4], id='circle', capstyle='butt', fill=False)
        for object_id, text, anchor in [('label0', '1', (2.65, 4.0)), ('label1', '2', (1.2, 3.3)), ('label2', '3', (1.9, 2.45)), ('label3', '4', (4.5, 1.4)), ('label4', '5', (1.8, 1.55)), ('label5', '6', (3.4, 4.9)), ('label6', '7', (5.1, 5.0)), ('label7', '8', (5.8, 6.2)), ('label8', '9', (6.4, 4.85)), ('label9', '10', (6.65, 3.3)), ('label10', '11', (7.8, 3.3)), ('label11', '12', (6.5, 1.8)), ('label12', '13', (4.3, 3.3))]:
            c.text(text, anchor, id=object_id, rotation_mode='default', offset_pt=(0, 0), annotation_clip=None)
        return c.save(output_path)
