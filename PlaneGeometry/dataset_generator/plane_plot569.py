"""Frozen question Plane569; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane569:

    def __init__(self):
        self.id = 'Plane569'
        self.source_dataset = 'Author Designed'
        self.source_key = 'author-extensions95-v1:Plane248/extension_05'
        self.question = 'Two identical pieces may be rotated but may not be turned upside down. Which of the following pictures cannot be made with these two pieces?\nChoices:\nA:A\nB:B\nC:C\nD:D\nE:E'
        self.answer = 'A'
        self.answer_type = 'choice'
        self.choices = {'A': 'A', 'B': 'B', 'C': 'C', 'D': 'D', 'E': 'E'}
        self.query = self.question
        self.points = {'source0.v00': [10.5, 8.5],
         'source0.v01': [11.5, 8.5],
         'source0.v02': [11.5, 10.5],
         'source0.v03': [12.5, 10.5],
         'source0.v04': [12.5, 11.5],
         'source0.v05': [11.5, 11.5],
         'source0.v06': [11.5, 12.5],
         'source0.v07': [10.5, 12.5],
         'source1.v00': [15.5, 8.5],
         'source1.v01': [16.5, 8.5],
         'source1.v02': [16.5, 10.5],
         'source1.v03': [17.5, 10.5],
         'source1.v04': [17.5, 11.5],
         'source1.v05': [16.5, 11.5],
         'source1.v06': [16.5, 12.5],
         'source1.v07': [15.5, 12.5],
         'option_A.v00': [-2.0, 0.2999999999999998],
         'option_A.v01': [2.0, 0.2999999999999998],
         'option_A.v02': [2.0, 1.2999999999999998],
         'option_A.v03': [0.0, 1.2999999999999998],
         'option_A.v04': [0.0, 3.3],
         'option_A.v05': [-1.0, 3.3],
         'option_A.v06': [-1.0, 5.3],
         'option_A.v07': [-2.0, 5.3],
         'option_B.v00': [5.0, 1.7999999999999998],
         'option_B.v01': [7.0, 1.7999999999999998],
         'option_B.v02': [7.0, 0.7999999999999998],
         'option_B.v03': [8.0, 0.7999999999999998],
         'option_B.v04': [8.0, 1.7999999999999998],
         'option_B.v05': [9.0, 1.7999999999999998],
         'option_B.v06': [9.0, 3.8],
         'option_B.v07': [7.0, 3.8],
         'option_B.v08': [7.0, 4.8],
         'option_B.v09': [6.0, 4.8],
         'option_B.v10': [6.0, 3.8],
         'option_B.v11': [5.0, 3.8],
         'option_C.v00': [11.0, 1.2999999999999998],
         'option_C.v01': [12.0, 1.2999999999999998],
         'option_C.v02': [12.0, 0.2999999999999998],
         'option_C.v03': [13.0, 0.2999999999999998],
         'option_C.v04': [13.0, 3.3],
         'option_C.v05': [17.0, 3.3],
         'option_C.v06': [17.0, 4.3],
         'option_C.v07': [15.0, 4.3],
         'option_C.v08': [15.0, 5.3],
         'option_C.v09': [14.0, 5.3],
         'option_C.v10': [14.0, 4.3],
         'option_C.v11': [12.0, 4.3],
         'option_C.v12': [12.0, 2.3],
         'option_C.v13': [11.0, 2.3],
         'option_D.v00': [18.0, 1.7999999999999998],
         'option_D.v01': [23.0, 1.7999999999999998],
         'option_D.v02': [23.0, 2.8],
         'option_D.v03': [24.0, 2.8],
         'option_D.v04': [24.0, 3.8],
         'option_D.v05': [19.0, 3.8],
         'option_D.v06': [19.0, 2.8],
         'option_D.v07': [18.0, 2.8],
         'option_E.v00': [26.5, -0.20000000000000018],
         'option_E.v01': [27.5, -0.20000000000000018],
         'option_E.v02': [27.5, 1.7999999999999998],
         'option_E.v03': [29.5, 1.7999999999999998],
         'option_E.v04': [29.5, 5.8],
         'option_E.v05': [28.5, 5.8],
         'option_E.v06': [28.5, 3.8],
         'option_E.v07': [26.5, 3.8]}
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane569.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-2.7675699459853114, 30.26756994598532], ylim=[-10.367569945985313, 22.667569945985317]) as c:
            for object_id, vertices, codes in [('source0', [self.points['source0.v00'], self.points['source0.v01'], self.points['source0.v02'], self.points['source0.v03'], self.points['source0.v04'], self.points['source0.v05'], self.points['source0.v06'], self.points['source0.v07'], self.points['source0.v00']], [1, 2, 2, 2, 2, 2, 2, 2, 79]), ('source1', [self.points['source1.v00'], self.points['source1.v01'], self.points['source1.v02'], self.points['source1.v03'], self.points['source1.v04'], self.points['source1.v05'], self.points['source1.v06'], self.points['source1.v07'], self.points['source1.v00']], [1, 2, 2, 2, 2, 2, 2, 2, 79]), ('option_A', [self.points['option_A.v00'], self.points['option_A.v01'], self.points['option_A.v02'], self.points['option_A.v03'], self.points['option_A.v04'], self.points['option_A.v05'], self.points['option_A.v06'], self.points['option_A.v07'], self.points['option_A.v00']], [1, 2, 2, 2, 2, 2, 2, 2, 79]), ('option_B', [self.points['option_B.v00'], self.points['option_B.v01'], self.points['option_B.v02'], self.points['option_B.v03'], self.points['option_B.v04'], self.points['option_B.v05'], self.points['option_B.v06'], self.points['option_B.v07'], self.points['option_B.v08'], self.points['option_B.v09'], self.points['option_B.v10'], self.points['option_B.v11'], self.points['option_B.v00']], [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 79]), ('option_C', [self.points['option_C.v00'], self.points['option_C.v01'], self.points['option_C.v02'], self.points['option_C.v03'], self.points['option_C.v04'], self.points['option_C.v05'], self.points['option_C.v06'], self.points['option_C.v07'], self.points['option_C.v08'], self.points['option_C.v09'], self.points['option_C.v10'], self.points['option_C.v11'], self.points['option_C.v12'], self.points['option_C.v13'], self.points['option_C.v00']], [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 79]), ('option_D', [self.points['option_D.v00'], self.points['option_D.v01'], self.points['option_D.v02'], self.points['option_D.v03'], self.points['option_D.v04'], self.points['option_D.v05'], self.points['option_D.v06'], self.points['option_D.v07'], self.points['option_D.v00']], [1, 2, 2, 2, 2, 2, 2, 2, 79]), ('option_E', [self.points['option_E.v00'], self.points['option_E.v01'], self.points['option_E.v02'], self.points['option_E.v03'], self.points['option_E.v04'], self.points['option_E.v05'], self.points['option_E.v06'], self.points['option_E.v07'], self.points['option_E.v00']], [1, 2, 2, 2, 2, 2, 2, 2, 79])]:
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
    print(Plane569().draw(sys.argv[1] if len(sys.argv) > 1 else None))
