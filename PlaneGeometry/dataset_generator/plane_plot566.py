"""Frozen question Plane566; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane566:

    def __init__(self):
        self.id = 'Plane566'
        self.source_dataset = 'Author Designed'
        self.source_key = 'author-extensions95-v1:Plane248/extension_02'
        self.question = 'Two identical pieces may be rotated but may not be turned upside down. Which of the following pictures cannot be made with these two pieces?\nChoices:\nA:A\nB:B\nC:C\nD:D\nE:E'
        self.answer = 'E'
        self.answer_type = 'choice'
        self.choices = {'A': 'A', 'B': 'B', 'C': 'C', 'D': 'D', 'E': 'E'}
        self.query = self.question
        self.points = {'source0.v00': [10.5, 8.5],
         'source0.v01': [12.5, 8.5],
         'source0.v02': [12.5, 10.5],
         'source0.v03': [11.5, 10.5],
         'source0.v04': [11.5, 11.5],
         'source0.v05': [10.5, 11.5],
         'source1.v00': [15.5, 8.5],
         'source1.v01': [17.5, 8.5],
         'source1.v02': [17.5, 10.5],
         'source1.v03': [16.5, 10.5],
         'source1.v04': [16.5, 11.5],
         'source1.v05': [15.5, 11.5],
         'option_A.v00': [-1.5, 0.7999999999999998],
         'option_A.v01': [0.5, 0.7999999999999998],
         'option_A.v02': [0.5, 1.7999999999999998],
         'option_A.v03': [1.5, 1.7999999999999998],
         'option_A.v04': [1.5, 4.8],
         'option_A.v05': [-0.5, 4.8],
         'option_A.v06': [-0.5, 3.8],
         'option_A.v07': [-1.5, 3.8],
         'option_B.v00': [4.0, 1.2999999999999998],
         'option_B.v01': [7.0, 1.2999999999999998],
         'option_B.v02': [7.0, 2.3],
         'option_B.v03': [9.0, 2.3],
         'option_B.v04': [9.0, 3.3],
         'option_B.v05': [10.0, 3.3],
         'option_B.v06': [10.0, 4.3],
         'option_B.v07': [7.0, 4.3],
         'option_B.v08': [7.0, 3.3],
         'option_B.v09': [5.0, 3.3],
         'option_B.v10': [5.0, 2.3],
         'option_B.v11': [4.0, 2.3],
         'option_C.v00': [12.5, 0.7999999999999998],
         'option_C.v01': [13.5, 0.7999999999999998],
         'option_C.v02': [13.5, -0.20000000000000018],
         'option_C.v03': [14.5, -0.20000000000000018],
         'option_C.v04': [14.5, 2.8],
         'option_C.v05': [15.5, 2.8],
         'option_C.v06': [15.5, 4.8],
         'option_C.v07': [14.5, 4.8],
         'option_C.v08': [14.5, 5.8],
         'option_C.v09': [13.5, 5.8],
         'option_C.v10': [13.5, 2.8],
         'option_C.v11': [12.5, 2.8],
         'option_D.v00': [19.0, 1.7999999999999998],
         'option_D.v01': [20.0, 1.7999999999999998],
         'option_D.v02': [20.0, 0.7999999999999998],
         'option_D.v03': [21.0, 0.7999999999999998],
         'option_D.v04': [21.0, 1.7999999999999998],
         'option_D.v05': [23.0, 1.7999999999999998],
         'option_D.v06': [23.0, 3.8],
         'option_D.v07': [22.0, 3.8],
         'option_D.v08': [22.0, 4.8],
         'option_D.v09': [21.0, 4.8],
         'option_D.v10': [21.0, 3.8],
         'option_D.v11': [19.0, 3.8],
         'option_E.v00': [26.5, 0.7999999999999998],
         'option_E.v01': [28.5, 0.7999999999999998],
         'option_E.v02': [28.5, 1.7999999999999998],
         'option_E.v03': [29.5, 1.7999999999999998],
         'option_E.v04': [29.5, 3.8],
         'option_E.v05': [28.5, 3.8],
         'option_E.v06': [28.5, 4.8],
         'option_E.v07': [26.5, 4.8]}
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane566.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-2.2553862960490356, 30.255386296049036], ylim=[-10.605386296049037, 21.905386296049034]) as c:
            for object_id, vertices, codes in [('source0', [self.points['source0.v00'], self.points['source0.v01'], self.points['source0.v02'], self.points['source0.v03'], self.points['source0.v04'], self.points['source0.v05'], self.points['source0.v00']], [1, 2, 2, 2, 2, 2, 79]), ('source1', [self.points['source1.v00'], self.points['source1.v01'], self.points['source1.v02'], self.points['source1.v03'], self.points['source1.v04'], self.points['source1.v05'], self.points['source1.v00']], [1, 2, 2, 2, 2, 2, 79]), ('option_A', [self.points['option_A.v00'], self.points['option_A.v01'], self.points['option_A.v02'], self.points['option_A.v03'], self.points['option_A.v04'], self.points['option_A.v05'], self.points['option_A.v06'], self.points['option_A.v07'], self.points['option_A.v00']], [1, 2, 2, 2, 2, 2, 2, 2, 79]), ('option_B', [self.points['option_B.v00'], self.points['option_B.v01'], self.points['option_B.v02'], self.points['option_B.v03'], self.points['option_B.v04'], self.points['option_B.v05'], self.points['option_B.v06'], self.points['option_B.v07'], self.points['option_B.v08'], self.points['option_B.v09'], self.points['option_B.v10'], self.points['option_B.v11'], self.points['option_B.v00']], [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 79]), ('option_C', [self.points['option_C.v00'], self.points['option_C.v01'], self.points['option_C.v02'], self.points['option_C.v03'], self.points['option_C.v04'], self.points['option_C.v05'], self.points['option_C.v06'], self.points['option_C.v07'], self.points['option_C.v08'], self.points['option_C.v09'], self.points['option_C.v10'], self.points['option_C.v11'], self.points['option_C.v00']], [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 79]), ('option_D', [self.points['option_D.v00'], self.points['option_D.v01'], self.points['option_D.v02'], self.points['option_D.v03'], self.points['option_D.v04'], self.points['option_D.v05'], self.points['option_D.v06'], self.points['option_D.v07'], self.points['option_D.v08'], self.points['option_D.v09'], self.points['option_D.v10'], self.points['option_D.v11'], self.points['option_D.v00']], [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 79]), ('option_E', [self.points['option_E.v00'], self.points['option_E.v01'], self.points['option_E.v02'], self.points['option_E.v03'], self.points['option_E.v04'], self.points['option_E.v05'], self.points['option_E.v06'], self.points['option_E.v07'], self.points['option_E.v00']], [1, 2, 2, 2, 2, 2, 2, 2, 79])]:
                c.path(vertices, codes, id=object_id)
            for object_id, text, anchor in [('label_A', 'A', [0, 6.6]), ('label_B', 'B', [7, 6.6]), ('label_C', 'C', [14, 6.6]), ('label_D', 'D', [21, 6.6]), ('label_E', 'E', [28, 6.6])]:
                c.text(text, anchor, id=object_id, offset_pt=[0, 0], vertex=False)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane566().draw(sys.argv[1] if len(sys.argv) > 1 else None))
