"""Frozen question Plane237; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane237:

    def __init__(self):
        self.id = 'Plane237'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:666'
        self.question = 'Five cars are labelled with the numbers 1 to 5 . They drive in the direction of the arrow.\nFirst the last car overtakes the two cars in front of it.\nThen the now second to last car overtakes the two in front of it.\nIn the end the car that is now in the middle overtakes the two in front of it.\nIn which order do the cars now drive?\nChoices:\nA:$1,2,3,4,5$\nB:$2,1,3,5,4$\nC:$2,1,5,3,4$\nD:$3,1,4,2,5$\nE:$4,1,2,5,3$'
        self.answer = 'B'
        self.answer_type = 'choice'
        self.choices = {'A': '$1,2,3,4,5$', 'B': '$2,1,3,5,4$', 'C': '$2,1,5,3,4$', 'D': '$3,1,4,2,5$', 'E': '$4,1,2,5,3$'}
        self.query = self.question
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane237.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-3.2412416439836402, 24.959341402499454], ylim=[-13.252723875598319, 14.947859170884774], axes_position=[0.05, 0.05000000000000006, 0.9, 0.8999999999999999], coordinate_axes=False) as c:
            c.path([[0.0, 0.25], [-0.2, 0.25], [-0.2, 0.4], [-0.2, 0.65], [-0.2, 0.95], [0.0, 1.1], [0.3, 1.1], [0.8, 1.1], [1.65, 1.85], [1.75, 1.95], [1.9, 1.98], [2.1, 1.98], [3.2, 1.98], [3.4, 1.98], [3.5, 1.93], [3.65, 1.8], [4.3, 1.15], [4.3, 0.6], [4.3, 0.35], [4.2, 0.25], [4.0, 0.25], [0.0, 0.25], [0.0, 0.25]], [1, 4, 4, 4, 4, 4, 4, 2, 2, 4, 4, 4, 2, 4, 4, 4, 2, 2, 4, 4, 4, 2, 79], id='body0', facecolor=[0.0, 0.0, 0.0, 0.0], capstyle='butt')
            c.path([[1.25, 1.25], [1.85, 1.8], [2.5, 1.8], [2.5, 1.25], [1.25, 1.25]], [1, 2, 2, 2, 79], id='window0_0', edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[1.25, 1.25], [1.85, 1.8], [2.5, 1.8], [2.5, 1.25], [1.25, 1.25]], [1, 2, 2, 2, 79], id='window0_0', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[2.7, 1.25], [2.7, 1.8], [3.35, 1.8], [3.9, 1.25], [2.7, 1.25]], [1, 2, 2, 2, 79], id='window0_1', edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[2.7, 1.25], [2.7, 1.8], [3.35, 1.8], [3.9, 1.25], [2.7, 1.25]], [1, 2, 2, 2, 79], id='window0_1', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.circle([0.8, 0.25], 0.52, id='tire0_0', facecolor=[0.0, 0.0, 0.0, 1.0])
            c.circle([0.8, 0.25], 0.28, id='hub0_0', facecolor=[1.0, 1.0, 1.0, 1.0])
            c.circle([3.25, 0.25], 0.52, id='tire0_1', facecolor=[0.0, 0.0, 0.0, 1.0])
            c.circle([3.25, 0.25], 0.28, id='hub0_1', facecolor=[1.0, 1.0, 1.0, 1.0])
            c.circle([1.9, 0.73], 0.45, id='badge0', facecolor=[1.0, 1.0, 1.0, 1.0])
            c.path([[5.0, 0.25], [4.8, 0.25], [4.8, 0.4], [4.8, 0.65], [4.8, 0.95], [5.0, 1.1], [5.3, 1.1], [5.8, 1.1], [6.65, 1.85], [6.75, 1.95], [6.9, 1.98], [7.1, 1.98], [8.2, 1.98], [8.4, 1.98], [8.5, 1.93], [8.65, 1.8], [9.3, 1.15], [9.3, 0.6], [9.3, 0.35], [9.2, 0.25], [9.0, 0.25], [5.0, 0.25], [5.0, 0.25]], [1, 4, 4, 4, 4, 4, 4, 2, 2, 4, 4, 4, 2, 4, 4, 4, 2, 2, 4, 4, 4, 2, 79], id='body1', facecolor=[0.0, 0.0, 0.0, 0.0], capstyle='butt')
            c.path([[6.25, 1.25], [6.85, 1.8], [7.5, 1.8], [7.5, 1.25], [6.25, 1.25]], [1, 2, 2, 2, 79], id='window1_0', edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[6.25, 1.25], [6.85, 1.8], [7.5, 1.8], [7.5, 1.25], [6.25, 1.25]], [1, 2, 2, 2, 79], id='window1_0', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[7.7, 1.25], [7.7, 1.8], [8.35, 1.8], [8.9, 1.25], [7.7, 1.25]], [1, 2, 2, 2, 79], id='window1_1', edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[7.7, 1.25], [7.7, 1.8], [8.35, 1.8], [8.9, 1.25], [7.7, 1.25]], [1, 2, 2, 2, 79], id='window1_1', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.circle([5.8, 0.25], 0.52, id='tire1_0', facecolor=[0.0, 0.0, 0.0, 1.0])
            c.circle([5.8, 0.25], 0.28, id='hub1_0', facecolor=[1.0, 1.0, 1.0, 1.0])
            c.circle([8.25, 0.25], 0.52, id='tire1_1', facecolor=[0.0, 0.0, 0.0, 1.0])
            c.circle([8.25, 0.25], 0.28, id='hub1_1', facecolor=[1.0, 1.0, 1.0, 1.0])
            c.circle([6.9, 0.73], 0.45, id='badge1', facecolor=[1.0, 1.0, 1.0, 1.0])
            c.path([[10.0, 0.25], [9.8, 0.25], [9.8, 0.4], [9.8, 0.65], [9.8, 0.95], [10.0, 1.1], [10.3, 1.1], [10.8, 1.1], [11.65, 1.85], [11.75, 1.95], [11.9, 1.98], [12.1, 1.98], [13.2, 1.98], [13.4, 1.98], [13.5, 1.93], [13.65, 1.8], [14.3, 1.15], [14.3, 0.6], [14.3, 0.35], [14.2, 0.25], [14.0, 0.25], [10.0, 0.25], [10.0, 0.25]], [1, 4, 4, 4, 4, 4, 4, 2, 2, 4, 4, 4, 2, 4, 4, 4, 2, 2, 4, 4, 4, 2, 79], id='body2', facecolor=[0.0, 0.0, 0.0, 0.0], capstyle='butt')
            c.path([[11.25, 1.25], [11.85, 1.8], [12.5, 1.8], [12.5, 1.25], [11.25, 1.25]], [1, 2, 2, 2, 79], id='window2_0', edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[11.25, 1.25], [11.85, 1.8], [12.5, 1.8], [12.5, 1.25], [11.25, 1.25]], [1, 2, 2, 2, 79], id='window2_0', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[12.7, 1.25], [12.7, 1.8], [13.35, 1.8], [13.9, 1.25], [12.7, 1.25]], [1, 2, 2, 2, 79], id='window2_1', edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[12.7, 1.25], [12.7, 1.8], [13.35, 1.8], [13.9, 1.25], [12.7, 1.25]], [1, 2, 2, 2, 79], id='window2_1', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.circle([10.8, 0.25], 0.52, id='tire2_0', facecolor=[0.0, 0.0, 0.0, 1.0])
            c.circle([10.8, 0.25], 0.28, id='hub2_0', facecolor=[1.0, 1.0, 1.0, 1.0])
            c.circle([13.25, 0.25], 0.52, id='tire2_1', facecolor=[0.0, 0.0, 0.0, 1.0])
            c.circle([13.25, 0.25], 0.28, id='hub2_1', facecolor=[1.0, 1.0, 1.0, 1.0])
            c.circle([11.9, 0.73], 0.45, id='badge2', facecolor=[1.0, 1.0, 1.0, 1.0])
            c.path([[15.0, 0.25], [14.8, 0.25], [14.8, 0.4], [14.8, 0.65], [14.8, 0.95], [15.0, 1.1], [15.3, 1.1], [15.8, 1.1], [16.65, 1.85], [16.75, 1.95], [16.9, 1.98], [17.1, 1.98], [18.2, 1.98], [18.4, 1.98], [18.5, 1.93], [18.65, 1.8], [19.3, 1.15], [19.3, 0.6], [19.3, 0.35], [19.2, 0.25], [19.0, 0.25], [15.0, 0.25], [15.0, 0.25]], [1, 4, 4, 4, 4, 4, 4, 2, 2, 4, 4, 4, 2, 4, 4, 4, 2, 2, 4, 4, 4, 2, 79], id='body3', facecolor=[0.0, 0.0, 0.0, 0.0], capstyle='butt')
            c.path([[16.25, 1.25], [16.85, 1.8], [17.5, 1.8], [17.5, 1.25], [16.25, 1.25]], [1, 2, 2, 2, 79], id='window3_0', edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[16.25, 1.25], [16.85, 1.8], [17.5, 1.8], [17.5, 1.25], [16.25, 1.25]], [1, 2, 2, 2, 79], id='window3_0', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[17.7, 1.25], [17.7, 1.8], [18.35, 1.8], [18.9, 1.25], [17.7, 1.25]], [1, 2, 2, 2, 79], id='window3_1', edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[17.7, 1.25], [17.7, 1.8], [18.35, 1.8], [18.9, 1.25], [17.7, 1.25]], [1, 2, 2, 2, 79], id='window3_1', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.circle([15.8, 0.25], 0.52, id='tire3_0', facecolor=[0.0, 0.0, 0.0, 1.0])
            c.circle([15.8, 0.25], 0.28, id='hub3_0', facecolor=[1.0, 1.0, 1.0, 1.0])
            c.circle([18.25, 0.25], 0.52, id='tire3_1', facecolor=[0.0, 0.0, 0.0, 1.0])
            c.circle([18.25, 0.25], 0.28, id='hub3_1', facecolor=[1.0, 1.0, 1.0, 1.0])
            c.circle([16.9, 0.73], 0.45, id='badge3', facecolor=[1.0, 1.0, 1.0, 1.0])
            c.path([[20.0, 0.25], [19.8, 0.25], [19.8, 0.4], [19.8, 0.65], [19.8, 0.95], [20.0, 1.1], [20.3, 1.1], [20.8, 1.1], [21.65, 1.85], [21.75, 1.95], [21.9, 1.98], [22.1, 1.98], [23.2, 1.98], [23.4, 1.98], [23.5, 1.93], [23.65, 1.8], [24.3, 1.15], [24.3, 0.6], [24.3, 0.35], [24.2, 0.25], [24.0, 0.25], [20.0, 0.25], [20.0, 0.25]], [1, 4, 4, 4, 4, 4, 4, 2, 2, 4, 4, 4, 2, 4, 4, 4, 2, 2, 4, 4, 4, 2, 79], id='body4', facecolor=[0.0, 0.0, 0.0, 0.0], capstyle='butt')
            c.path([[21.25, 1.25], [21.85, 1.8], [22.5, 1.8], [22.5, 1.25], [21.25, 1.25]], [1, 2, 2, 2, 79], id='window4_0', edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[21.25, 1.25], [21.85, 1.8], [22.5, 1.8], [22.5, 1.25], [21.25, 1.25]], [1, 2, 2, 2, 79], id='window4_0', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[22.7, 1.25], [22.7, 1.8], [23.35, 1.8], [23.9, 1.25], [22.7, 1.25]], [1, 2, 2, 2, 79], id='window4_1', edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[22.7, 1.25], [22.7, 1.8], [23.35, 1.8], [23.9, 1.25], [22.7, 1.25]], [1, 2, 2, 2, 79], id='window4_1', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.circle([20.8, 0.25], 0.52, id='tire4_0', facecolor=[0.0, 0.0, 0.0, 1.0])
            c.circle([20.8, 0.25], 0.28, id='hub4_0', facecolor=[1.0, 1.0, 1.0, 1.0])
            c.circle([23.25, 0.25], 0.52, id='tire4_1', facecolor=[0.0, 0.0, 0.0, 1.0])
            c.circle([23.25, 0.25], 0.28, id='hub4_1', facecolor=[1.0, 1.0, 1.0, 1.0])
            c.circle([21.9, 0.73], 0.45, id='badge4', facecolor=[1.0, 1.0, 1.0, 1.0])
            c.path([[-2.6, 1.15], [-1.7, 1.6], [-1.7, 1.3], [-0.55, 1.3], [-0.55, 1.0], [-1.7, 1.0], [-1.7, 0.7], [-2.6, 1.15]], [1, 2, 2, 2, 2, 2, 2, 79], id='direction', edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.0, 0.0, 0.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[-2.6, 1.15], [-1.7, 1.6], [-1.7, 1.3], [-0.55, 1.3], [-0.55, 1.0], [-1.7, 1.0], [-1.7, 0.7], [-2.6, 1.15]], [1, 2, 2, 2, 2, 2, 2, 79], id='direction', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            for object_id, text, anchor in [('label0', '1', [1.9, 0.73]), ('label1', '2', [6.9, 0.73]), ('label2', '3', [11.9, 0.73]), ('label3', '4', [16.9, 0.73]), ('label4', '5', [21.9, 0.73])]:
                c.text(text, anchor, id=object_id, rotation_mode='default', offset_pt=[0, 0], annotation_clip=None)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane237().draw(sys.argv[1] if len(sys.argv) > 1 else None))
