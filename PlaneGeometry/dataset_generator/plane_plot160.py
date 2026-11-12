"""Frozen question Plane160; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane160:

    def __init__(self):
        self.id = 'Plane160'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:103'
        self.question = 'Several of the cards shown on the left are used to assemble the tower shown on the right. Which cards are not used?\nChoices:\nA:A\nB:B\nC:C\nD:D\nE:E'
        self.answer = 'C'
        self.answer_type = 'choice'
        self.choices = {'A': 'A', 'B': 'B', 'C': 'C', 'D': 'D', 'E': 'E'}
        self.query = self.question
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane160.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=(-2.2384687384788524, 22.22198307329395), ylim=(-3.4638728897976403, 20.996578921975157), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
            c.circle([10.0, 17.0], 0.42, id='source0')
            c.circle([11.1, 17.7], 0.42, id='source1')
            c.path([[12.17, 17.27], [13.03, 17.27], [13.03, 18.13], [12.17, 18.13], [12.17, 17.27]], [1, 2, 2, 2, 79], id='source2', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[12.17, 17.27], [13.03, 17.27], [13.03, 18.13], [12.17, 18.13], [12.17, 17.27]], [1, 2, 2, 2, 79], id='source2', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.circle([14.3, 16.8], 0.42, id='source3')
            c.path([[11.1, 16.38], [12.200000000000001, 16.38], [11.65, 17.33], [11.1, 16.38]], [1, 2, 2, 79], id='source4', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[11.1, 16.38], [12.200000000000001, 16.38], [11.65, 17.33], [11.1, 16.38]], [1, 2, 2, 79], id='source4', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[10.02, 15.47], [10.879999999999999, 15.47], [10.879999999999999, 16.330000000000002], [10.02, 16.330000000000002], [10.02, 15.47]], [1, 2, 2, 2, 79], id='source5', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[10.02, 15.47], [10.879999999999999, 15.47], [10.879999999999999, 16.330000000000002], [10.02, 16.330000000000002], [10.02, 15.47]], [1, 2, 2, 2, 79], id='source5', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.circle([12.6, 15.9], 0.42, id='source6')
            c.path([[13.68, 16.05], [13.68, 14.95], [14.63, 15.5], [13.68, 16.05]], [1, 2, 2, 79], id='source7', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[13.68, 16.05], [13.68, 14.95], [14.63, 15.5], [13.68, 16.05]], [1, 2, 2, 79], id='source7', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[10.52, 14.149999999999999], [10.52, 15.25], [9.569999999999999, 14.7], [10.52, 14.149999999999999]], [1, 2, 2, 79], id='source8', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[10.52, 14.149999999999999], [10.52, 15.25], [9.569999999999999, 14.7], [10.52, 14.149999999999999]], [1, 2, 2, 79], id='source8', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[10.95, 14.879999999999999], [12.05, 14.879999999999999], [11.5, 15.83], [10.95, 14.879999999999999]], [1, 2, 2, 79], id='source9', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[10.95, 14.879999999999999], [12.05, 14.879999999999999], [11.5, 15.83], [10.95, 14.879999999999999]], [1, 2, 2, 79], id='source9', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[12.149999999999999, 14.08], [13.25, 14.08], [12.7, 15.030000000000001], [12.149999999999999, 14.08]], [1, 2, 2, 79], id='source10', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[12.149999999999999, 14.08], [13.25, 14.08], [12.7, 15.030000000000001], [12.149999999999999, 14.08]], [1, 2, 2, 79], id='source10', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[13.67, 13.97], [14.53, 13.97], [14.53, 14.83], [13.67, 14.83], [13.67, 13.97]], [1, 2, 2, 2, 79], id='source11', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[13.67, 13.97], [14.53, 13.97], [14.53, 14.83], [13.67, 14.83], [13.67, 13.97]], [1, 2, 2, 2, 79], id='source11', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[12.75, 13.92], [11.649999999999999, 13.92], [12.2, 12.969999999999999], [12.75, 13.92]], [1, 2, 2, 79], id='source12', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[12.75, 13.92], [11.649999999999999, 13.92], [12.2, 12.969999999999999], [12.75, 13.92]], [1, 2, 2, 79], id='source12', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.circle([11.1, 13.5], 0.42, id='source13')
            c.circle([13.1, 13.3], 0.42, id='source14')
            c.path([[9.57, 12.870000000000001], [10.43, 12.870000000000001], [10.43, 13.73], [9.57, 13.73], [9.57, 12.870000000000001]], [1, 2, 2, 2, 79], id='source15', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[9.57, 12.870000000000001], [10.43, 12.870000000000001], [10.43, 13.73], [9.57, 13.73], [9.57, 12.870000000000001]], [1, 2, 2, 2, 79], id='source15', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[13.870000000000001, 12.870000000000001], [14.73, 12.870000000000001], [14.73, 13.73], [13.870000000000001, 13.73], [13.870000000000001, 12.870000000000001]], [1, 2, 2, 2, 79], id='source16', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[13.870000000000001, 12.870000000000001], [14.73, 12.870000000000001], [14.73, 13.73], [13.870000000000001, 13.73], [13.870000000000001, 12.870000000000001]], [1, 2, 2, 2, 79], id='source16', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            for object_id, center, radius in [('tower0', [11.0, 5.0], 0.42), ('tower1', [12.1, 5.0], 0.42), ('tower2', [13.2, 5.0], 0.42)]:
                c.circle(center, radius, id=object_id)
            c.path([[10.57, 5.470000000000001], [11.43, 5.470000000000001], [11.43, 6.33], [10.57, 6.33], [10.57, 5.470000000000001]], [1, 2, 2, 2, 79], id='tower3', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[10.57, 5.470000000000001], [11.43, 5.470000000000001], [11.43, 6.33], [10.57, 6.33], [10.57, 5.470000000000001]], [1, 2, 2, 2, 79], id='tower3', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[11.67, 5.470000000000001], [12.53, 5.470000000000001], [12.53, 6.33], [11.67, 6.33], [11.67, 5.470000000000001]], [1, 2, 2, 2, 79], id='tower4', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[11.67, 5.470000000000001], [12.53, 5.470000000000001], [12.53, 6.33], [11.67, 6.33], [11.67, 5.470000000000001]], [1, 2, 2, 2, 79], id='tower4', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[12.77, 5.470000000000001], [13.629999999999999, 5.470000000000001], [13.629999999999999, 6.33], [12.77, 6.33], [12.77, 5.470000000000001]], [1, 2, 2, 2, 79], id='tower5', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[12.77, 5.470000000000001], [13.629999999999999, 5.470000000000001], [13.629999999999999, 6.33], [12.77, 6.33], [12.77, 5.470000000000001]], [1, 2, 2, 2, 79], id='tower5', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[11.120000000000001, 6.33], [11.98, 6.33], [11.98, 7.1899999999999995], [11.120000000000001, 7.1899999999999995], [11.120000000000001, 6.33]], [1, 2, 2, 2, 79], id='tower6', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[11.120000000000001, 6.33], [11.98, 6.33], [11.98, 7.1899999999999995], [11.120000000000001, 7.1899999999999995], [11.120000000000001, 6.33]], [1, 2, 2, 2, 79], id='tower6', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[12.22, 6.33], [13.08, 6.33], [13.08, 7.1899999999999995], [12.22, 7.1899999999999995], [12.22, 6.33]], [1, 2, 2, 2, 79], id='tower7', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[12.22, 6.33], [13.08, 6.33], [13.08, 7.1899999999999995], [12.22, 7.1899999999999995], [12.22, 6.33]], [1, 2, 2, 2, 79], id='tower7', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[10.899999999999999, 7.279999999999999], [12.0, 7.279999999999999], [11.45, 8.23], [10.899999999999999, 7.279999999999999]], [1, 2, 2, 79], id='tower8', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[10.899999999999999, 7.279999999999999], [12.0, 7.279999999999999], [11.45, 8.23], [10.899999999999999, 7.279999999999999]], [1, 2, 2, 79], id='tower8', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[12.1, 7.279999999999999], [13.200000000000001, 7.279999999999999], [12.65, 8.23], [12.1, 7.279999999999999]], [1, 2, 2, 79], id='tower9', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[12.1, 7.279999999999999], [13.200000000000001, 7.279999999999999], [12.65, 8.23], [12.1, 7.279999999999999]], [1, 2, 2, 79], id='tower9', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[12.600000000000001, 8.23], [11.5, 8.23], [12.05, 7.28], [12.600000000000001, 8.23]], [1, 2, 2, 79], id='tower10', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[12.600000000000001, 8.23], [11.5, 8.23], [12.05, 7.28], [12.600000000000001, 8.23]], [1, 2, 2, 79], id='tower10', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.circle([12.1, 8.7], 0.42, id='tower11')
            c.path([[11.549999999999999, 9.28], [12.65, 9.28], [12.1, 10.23], [11.549999999999999, 9.28]], [1, 2, 2, 79], id='tower12', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[11.549999999999999, 9.28], [12.65, 9.28], [12.1, 10.23], [11.549999999999999, 9.28]], [1, 2, 2, 79], id='tower12', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.circle([12.1, 10.6], 0.42, id='tower13')
            c.path([[-0.55, -0.32], [0.55, -0.32], [0.0, 0.63], [-0.55, -0.32]], [1, 2, 2, 79], id='option0_0', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[-0.55, -0.32], [0.55, -0.32], [0.0, 0.63], [-0.55, -0.32]], [1, 2, 2, 79], id='option0_0', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[0.77, -0.43], [1.63, -0.43], [1.63, 0.43], [0.77, 0.43], [0.77, -0.43]], [1, 2, 2, 2, 79], id='option0_1', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[0.77, -0.43], [1.63, -0.43], [1.63, 0.43], [0.77, 0.43], [0.77, -0.43]], [1, 2, 2, 2, 79], id='option0_1', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.circle([2.4, 0.0], 0.42, id='option0_2')
            c.path([[4.45, -0.32], [5.55, -0.32], [5.0, 0.63], [4.45, -0.32]], [1, 2, 2, 79], id='option1_0', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[4.45, -0.32], [5.55, -0.32], [5.0, 0.63], [4.45, -0.32]], [1, 2, 2, 79], id='option1_0', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[5.65, -0.32], [6.75, -0.32], [6.2, 0.63], [5.65, -0.32]], [1, 2, 2, 79], id='option1_1', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[5.65, -0.32], [6.75, -0.32], [6.2, 0.63], [5.65, -0.32]], [1, 2, 2, 79], id='option1_1', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[6.970000000000001, -0.43], [7.83, -0.43], [7.83, 0.43], [6.970000000000001, 0.43], [6.970000000000001, -0.43]], [1, 2, 2, 2, 79], id='option1_2', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[6.970000000000001, -0.43], [7.83, -0.43], [7.83, 0.43], [6.970000000000001, 0.43], [6.970000000000001, -0.43]], [1, 2, 2, 2, 79], id='option1_2', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[9.45, -0.32], [10.55, -0.32], [10.0, 0.63], [9.45, -0.32]], [1, 2, 2, 79], id='option2_0', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[9.45, -0.32], [10.55, -0.32], [10.0, 0.63], [9.45, -0.32]], [1, 2, 2, 79], id='option2_0', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[10.649999999999999, -0.32], [11.75, -0.32], [11.2, 0.63], [10.649999999999999, -0.32]], [1, 2, 2, 79], id='option2_1', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[10.649999999999999, -0.32], [11.75, -0.32], [11.2, 0.63], [10.649999999999999, -0.32]], [1, 2, 2, 79], id='option2_1', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.circle([12.4, 0.0], 0.42, id='option2_2')
            c.circle([15.0, 0.0], 0.42, id='option3_0')
            c.path([[15.77, -0.43], [16.63, -0.43], [16.63, 0.43], [15.77, 0.43], [15.77, -0.43]], [1, 2, 2, 2, 79], id='option3_1', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[15.77, -0.43], [16.63, -0.43], [16.63, 0.43], [15.77, 0.43], [15.77, -0.43]], [1, 2, 2, 2, 79], id='option3_1', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[16.849999999999998, -0.32], [17.95, -0.32], [17.4, 0.63], [16.849999999999998, -0.32]], [1, 2, 2, 79], id='option3_2', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[16.849999999999998, -0.32], [17.95, -0.32], [17.4, 0.63], [16.849999999999998, -0.32]], [1, 2, 2, 79], id='option3_2', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[19.45, -0.32], [20.55, -0.32], [20.0, 0.63], [19.45, -0.32]], [1, 2, 2, 79], id='option4_0', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[19.45, -0.32], [20.55, -0.32], [20.0, 0.63], [19.45, -0.32]], [1, 2, 2, 79], id='option4_0', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.circle([21.2, 0.0], 0.42, id='option4_1')
            for object_id, text, anchor in [('label0', '(A)', (-1.2, -0.3)), ('label1', '(B)', (3.8, -0.3)), ('label2', '(C)', (8.8, -0.3)), ('label3', '(D)', (13.8, -0.3)), ('label4', '(E)', (18.8, -0.3))]:
                c.text(text, anchor, id=object_id, rotation_mode='default', offset_pt=(0, 0), annotation_clip=None)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane160().draw(sys.argv[1] if len(sys.argv) > 1 else None))
