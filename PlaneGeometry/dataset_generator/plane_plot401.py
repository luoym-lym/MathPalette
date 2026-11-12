"""Frozen question Plane401; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane401:

    def __init__(self):
        self.id = 'Plane401'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:1675'
        self.question = 'The diagram shows a shape made up of 36 identical small equilateral triangles. What is the smallest number of small triangles identical to these that could be added to the shape to turn it into a hexagon?'
        self.answer = '18'
        self.answer_type = 'number'
        self.query = self.question
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane401.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=(-0.22586601091616165, 5.225866010916162), ylim=(-0.12778979956284608, 5.323942222269477), axes_position=(0.05, 0.05000000000000006, 0.9, 0.8999999999999999), coordinate_axes=False) as c:
            c.path([[1.0, 1.7320508075688772], [1.5, 2.598076211353316], [0.5, 2.598076211353316], [1.0, 1.7320508075688772]], [1, 2, 2, 79], id='unittriangle0', alpha=0.45, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[1.0, 1.7320508075688772], [1.5, 2.598076211353316], [0.5, 2.598076211353316], [1.0, 1.7320508075688772]], [1, 2, 2, 79], id='unittriangle0', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[0.5, 2.598076211353316], [1.5, 2.598076211353316], [1.0, 3.4641016151377544], [0.5, 2.598076211353316]], [1, 2, 2, 79], id='unittriangle1', alpha=0.45, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[0.5, 2.598076211353316], [1.5, 2.598076211353316], [1.0, 3.4641016151377544], [0.5, 2.598076211353316]], [1, 2, 2, 79], id='unittriangle1', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[1.5, 2.598076211353316], [2.0, 3.4641016151377544], [1.0, 3.4641016151377544], [1.5, 2.598076211353316]], [1, 2, 2, 79], id='unittriangle2', alpha=0.45, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[1.5, 2.598076211353316], [2.0, 3.4641016151377544], [1.0, 3.4641016151377544], [1.5, 2.598076211353316]], [1, 2, 2, 79], id='unittriangle2', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[1.0, 3.4641016151377544], [2.0, 3.4641016151377544], [1.5, 4.330127018922193], [1.0, 3.4641016151377544]], [1, 2, 2, 79], id='unittriangle3', alpha=0.45, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[1.0, 3.4641016151377544], [2.0, 3.4641016151377544], [1.5, 4.330127018922193], [1.0, 3.4641016151377544]], [1, 2, 2, 79], id='unittriangle3', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[2.0, 3.4641016151377544], [2.5, 4.330127018922193], [1.5, 4.330127018922193], [2.0, 3.4641016151377544]], [1, 2, 2, 79], id='unittriangle4', alpha=0.45, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[2.0, 3.4641016151377544], [2.5, 4.330127018922193], [1.5, 4.330127018922193], [2.0, 3.4641016151377544]], [1, 2, 2, 79], id='unittriangle4', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[1.5, 0.8660254037844386], [2.0, 1.7320508075688772], [1.0, 1.7320508075688772], [1.5, 0.8660254037844386]], [1, 2, 2, 79], id='unittriangle5', alpha=0.45, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[1.5, 0.8660254037844386], [2.0, 1.7320508075688772], [1.0, 1.7320508075688772], [1.5, 0.8660254037844386]], [1, 2, 2, 79], id='unittriangle5', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[1.0, 1.7320508075688772], [2.0, 1.7320508075688772], [1.5, 2.598076211353316], [1.0, 1.7320508075688772]], [1, 2, 2, 79], id='unittriangle6', alpha=0.45, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[1.0, 1.7320508075688772], [2.0, 1.7320508075688772], [1.5, 2.598076211353316], [1.0, 1.7320508075688772]], [1, 2, 2, 79], id='unittriangle6', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[2.0, 1.7320508075688772], [2.5, 2.598076211353316], [1.5, 2.598076211353316], [2.0, 1.7320508075688772]], [1, 2, 2, 79], id='unittriangle7', alpha=0.45, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[2.0, 1.7320508075688772], [2.5, 2.598076211353316], [1.5, 2.598076211353316], [2.0, 1.7320508075688772]], [1, 2, 2, 79], id='unittriangle7', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[1.5, 2.598076211353316], [2.5, 2.598076211353316], [2.0, 3.4641016151377544], [1.5, 2.598076211353316]], [1, 2, 2, 79], id='unittriangle8', alpha=0.45, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[1.5, 2.598076211353316], [2.5, 2.598076211353316], [2.0, 3.4641016151377544], [1.5, 2.598076211353316]], [1, 2, 2, 79], id='unittriangle8', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[2.5, 2.598076211353316], [3.0, 3.4641016151377544], [2.0, 3.4641016151377544], [2.5, 2.598076211353316]], [1, 2, 2, 79], id='unittriangle9', alpha=0.45, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[2.5, 2.598076211353316], [3.0, 3.4641016151377544], [2.0, 3.4641016151377544], [2.5, 2.598076211353316]], [1, 2, 2, 79], id='unittriangle9', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[2.0, 3.4641016151377544], [3.0, 3.4641016151377544], [2.5, 4.330127018922193], [2.0, 3.4641016151377544]], [1, 2, 2, 79], id='unittriangle10', alpha=0.45, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[2.0, 3.4641016151377544], [3.0, 3.4641016151377544], [2.5, 4.330127018922193], [2.0, 3.4641016151377544]], [1, 2, 2, 79], id='unittriangle10', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[3.0, 3.4641016151377544], [3.5, 4.330127018922193], [2.5, 4.330127018922193], [3.0, 3.4641016151377544]], [1, 2, 2, 79], id='unittriangle11', alpha=0.45, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[3.0, 3.4641016151377544], [3.5, 4.330127018922193], [2.5, 4.330127018922193], [3.0, 3.4641016151377544]], [1, 2, 2, 79], id='unittriangle11', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[1.5, 0.8660254037844386], [2.5, 0.8660254037844386], [2.0, 1.7320508075688772], [1.5, 0.8660254037844386]], [1, 2, 2, 79], id='unittriangle12', alpha=0.45, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[1.5, 0.8660254037844386], [2.5, 0.8660254037844386], [2.0, 1.7320508075688772], [1.5, 0.8660254037844386]], [1, 2, 2, 79], id='unittriangle12', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[2.5, 0.8660254037844386], [3.0, 1.7320508075688772], [2.0, 1.7320508075688772], [2.5, 0.8660254037844386]], [1, 2, 2, 79], id='unittriangle13', alpha=0.45, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[2.5, 0.8660254037844386], [3.0, 1.7320508075688772], [2.0, 1.7320508075688772], [2.5, 0.8660254037844386]], [1, 2, 2, 79], id='unittriangle13', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[2.0, 1.7320508075688772], [3.0, 1.7320508075688772], [2.5, 2.598076211353316], [2.0, 1.7320508075688772]], [1, 2, 2, 79], id='unittriangle14', alpha=0.45, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[2.0, 1.7320508075688772], [3.0, 1.7320508075688772], [2.5, 2.598076211353316], [2.0, 1.7320508075688772]], [1, 2, 2, 79], id='unittriangle14', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[3.0, 1.7320508075688772], [3.5, 2.598076211353316], [2.5, 2.598076211353316], [3.0, 1.7320508075688772]], [1, 2, 2, 79], id='unittriangle15', alpha=0.45, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[3.0, 1.7320508075688772], [3.5, 2.598076211353316], [2.5, 2.598076211353316], [3.0, 1.7320508075688772]], [1, 2, 2, 79], id='unittriangle15', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[2.5, 2.598076211353316], [3.5, 2.598076211353316], [3.0, 3.4641016151377544], [2.5, 2.598076211353316]], [1, 2, 2, 79], id='unittriangle16', alpha=0.45, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[2.5, 2.598076211353316], [3.5, 2.598076211353316], [3.0, 3.4641016151377544], [2.5, 2.598076211353316]], [1, 2, 2, 79], id='unittriangle16', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[3.5, 2.598076211353316], [4.0, 3.4641016151377544], [3.0, 3.4641016151377544], [3.5, 2.598076211353316]], [1, 2, 2, 79], id='unittriangle17', alpha=0.45, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[3.5, 2.598076211353316], [4.0, 3.4641016151377544], [3.0, 3.4641016151377544], [3.5, 2.598076211353316]], [1, 2, 2, 79], id='unittriangle17', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[3.0, 3.4641016151377544], [4.0, 3.4641016151377544], [3.5, 4.330127018922193], [3.0, 3.4641016151377544]], [1, 2, 2, 79], id='unittriangle18', alpha=0.45, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[3.0, 3.4641016151377544], [4.0, 3.4641016151377544], [3.5, 4.330127018922193], [3.0, 3.4641016151377544]], [1, 2, 2, 79], id='unittriangle18', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[2.5, 0.8660254037844386], [3.5, 0.8660254037844386], [3.0, 1.7320508075688772], [2.5, 0.8660254037844386]], [1, 2, 2, 79], id='unittriangle19', alpha=0.45, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[2.5, 0.8660254037844386], [3.5, 0.8660254037844386], [3.0, 1.7320508075688772], [2.5, 0.8660254037844386]], [1, 2, 2, 79], id='unittriangle19', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[3.5, 0.8660254037844386], [4.0, 1.7320508075688772], [3.0, 1.7320508075688772], [3.5, 0.8660254037844386]], [1, 2, 2, 79], id='unittriangle20', alpha=0.45, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[3.5, 0.8660254037844386], [4.0, 1.7320508075688772], [3.0, 1.7320508075688772], [3.5, 0.8660254037844386]], [1, 2, 2, 79], id='unittriangle20', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[3.0, 1.7320508075688772], [4.0, 1.7320508075688772], [3.5, 2.598076211353316], [3.0, 1.7320508075688772]], [1, 2, 2, 79], id='unittriangle21', alpha=0.45, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[3.0, 1.7320508075688772], [4.0, 1.7320508075688772], [3.5, 2.598076211353316], [3.0, 1.7320508075688772]], [1, 2, 2, 79], id='unittriangle21', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[4.0, 1.7320508075688772], [4.5, 2.598076211353316], [3.5, 2.598076211353316], [4.0, 1.7320508075688772]], [1, 2, 2, 79], id='unittriangle22', alpha=0.45, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[4.0, 1.7320508075688772], [4.5, 2.598076211353316], [3.5, 2.598076211353316], [4.0, 1.7320508075688772]], [1, 2, 2, 79], id='unittriangle22', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[3.5, 2.598076211353316], [4.5, 2.598076211353316], [4.0, 3.4641016151377544], [3.5, 2.598076211353316]], [1, 2, 2, 79], id='unittriangle23', alpha=0.45, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[3.5, 2.598076211353316], [4.5, 2.598076211353316], [4.0, 3.4641016151377544], [3.5, 2.598076211353316]], [1, 2, 2, 79], id='unittriangle23', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[4.5, 2.598076211353316], [4.0, 3.4641016151377544], [5.0, 3.4641016151377544], [4.5, 2.598076211353316]], [1, 2, 2, 79], id='unittriangle24', alpha=0.45, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[4.5, 2.598076211353316], [4.0, 3.4641016151377544], [5.0, 3.4641016151377544], [4.5, 2.598076211353316]], [1, 2, 2, 79], id='unittriangle24', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[4.0, 3.4641016151377544], [3.5, 4.330127018922193], [4.5, 4.330127018922193], [4.0, 3.4641016151377544]], [1, 2, 2, 79], id='unittriangle25', alpha=0.45, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[4.0, 3.4641016151377544], [3.5, 4.330127018922193], [4.5, 4.330127018922193], [4.0, 3.4641016151377544]], [1, 2, 2, 79], id='unittriangle25', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[3.5, 4.330127018922193], [2.5, 4.330127018922193], [3.0, 5.196152422706631], [3.5, 4.330127018922193]], [1, 2, 2, 79], id='unittriangle26', alpha=0.45, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[3.5, 4.330127018922193], [2.5, 4.330127018922193], [3.0, 5.196152422706631], [3.5, 4.330127018922193]], [1, 2, 2, 79], id='unittriangle26', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[2.5, 4.330127018922193], [1.5, 4.330127018922193], [2.0, 5.196152422706631], [2.5, 4.330127018922193]], [1, 2, 2, 79], id='unittriangle27', alpha=0.45, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[2.5, 4.330127018922193], [1.5, 4.330127018922193], [2.0, 5.196152422706631], [2.5, 4.330127018922193]], [1, 2, 2, 79], id='unittriangle27', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[1.5, 4.330127018922193], [1.0, 3.4641016151377544], [0.5000000000000003, 4.330127018922193], [1.5, 4.330127018922193]], [1, 2, 2, 79], id='unittriangle28', alpha=0.45, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[1.5, 4.330127018922193], [1.0, 3.4641016151377544], [0.5000000000000003, 4.330127018922193], [1.5, 4.330127018922193]], [1, 2, 2, 79], id='unittriangle28', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[1.0, 3.4641016151377544], [0.5, 2.598076211353316], [3.3306690738754696e-16, 3.4641016151377544], [1.0, 3.4641016151377544]], [1, 2, 2, 79], id='unittriangle29', alpha=0.45, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[1.0, 3.4641016151377544], [0.5, 2.598076211353316], [3.3306690738754696e-16, 3.4641016151377544], [1.0, 3.4641016151377544]], [1, 2, 2, 79], id='unittriangle29', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[0.5, 2.598076211353316], [1.0, 1.7320508075688772], [-1.1102230246251565e-16, 1.7320508075688772], [0.5, 2.598076211353316]], [1, 2, 2, 79], id='unittriangle30', alpha=0.45, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[0.5, 2.598076211353316], [1.0, 1.7320508075688772], [-1.1102230246251565e-16, 1.7320508075688772], [0.5, 2.598076211353316]], [1, 2, 2, 79], id='unittriangle30', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[1.0, 1.7320508075688772], [1.5, 0.8660254037844386], [0.5000000000000001, 0.8660254037844387], [1.0, 1.7320508075688772]], [1, 2, 2, 79], id='unittriangle31', alpha=0.45, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[1.0, 1.7320508075688772], [1.5, 0.8660254037844386], [0.5000000000000001, 0.8660254037844387], [1.0, 1.7320508075688772]], [1, 2, 2, 79], id='unittriangle31', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[1.5, 0.8660254037844386], [2.5, 0.8660254037844386], [2.0, 0.0], [1.5, 0.8660254037844386]], [1, 2, 2, 79], id='unittriangle32', alpha=0.45, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[1.5, 0.8660254037844386], [2.5, 0.8660254037844386], [2.0, 0.0], [1.5, 0.8660254037844386]], [1, 2, 2, 79], id='unittriangle32', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[2.5, 0.8660254037844386], [3.5, 0.8660254037844386], [3.0, 0.0], [2.5, 0.8660254037844386]], [1, 2, 2, 79], id='unittriangle33', alpha=0.45, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[2.5, 0.8660254037844386], [3.5, 0.8660254037844386], [3.0, 0.0], [2.5, 0.8660254037844386]], [1, 2, 2, 79], id='unittriangle33', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[3.5, 0.8660254037844386], [4.0, 1.7320508075688772], [4.5, 0.8660254037844387], [3.5, 0.8660254037844386]], [1, 2, 2, 79], id='unittriangle34', alpha=0.45, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[3.5, 0.8660254037844386], [4.0, 1.7320508075688772], [4.5, 0.8660254037844387], [3.5, 0.8660254037844386]], [1, 2, 2, 79], id='unittriangle34', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[4.0, 1.7320508075688772], [4.5, 2.598076211353316], [5.0, 1.7320508075688772], [4.0, 1.7320508075688772]], [1, 2, 2, 79], id='unittriangle35', alpha=0.45, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[4.0, 1.7320508075688772], [4.5, 2.598076211353316], [5.0, 1.7320508075688772], [4.0, 1.7320508075688772]], [1, 2, 2, 79], id='unittriangle35', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane401().draw(sys.argv[1] if len(sys.argv) > 1 else None))
