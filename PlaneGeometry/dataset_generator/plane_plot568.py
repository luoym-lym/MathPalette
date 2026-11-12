"""Frozen question Plane568; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane568:

    def __init__(self):
        self.id = 'Plane568'
        self.source_dataset = 'Author Designed'
        self.source_key = 'author-extensions95-v1:Plane248/extension_04'
        self.question = 'Two identical pieces may be rotated but may not be turned upside down. Which of the following pictures cannot be made with these two pieces?\nChoices:\nA:A\nB:B\nC:C\nD:D\nE:E'
        self.answer = 'D'
        self.answer_type = 'choice'
        self.choices = {'A': 'A', 'B': 'B', 'C': 'C', 'D': 'D', 'E': 'E'}
        self.query = self.question
        self.points = {'source0.v00': [10.5, 8.5],
         'source0.v01': [11.5, 8.5],
         'source0.v02': [11.5, 9.5],
         'source0.v03': [12.5, 9.5],
         'source0.v04': [12.5, 12.5],
         'source0.v05': [11.5, 12.5],
         'source0.v06': [11.5, 10.5],
         'source0.v07': [10.5, 10.5],
         'source1.v00': [15.5, 8.5],
         'source1.v01': [16.5, 8.5],
         'source1.v02': [16.5, 9.5],
         'source1.v03': [17.5, 9.5],
         'source1.v04': [17.5, 12.5],
         'source1.v05': [16.5, 12.5],
         'source1.v06': [16.5, 10.5],
         'source1.v07': [15.5, 10.5],
         'option_A.v00': [-1.5, 0.7999999999999998],
         'option_A.v01': [0.5, 0.7999999999999998],
         'option_A.v02': [0.5, 1.7999999999999998],
         'option_A.v03': [1.5, 1.7999999999999998],
         'option_A.v04': [1.5, 4.8],
         'option_A.v05': [-0.5, 4.8],
         'option_A.v06': [-0.5, 3.8],
         'option_A.v07': [-1.5, 3.8],
         'option_B.v00': [4.0, 0.7999999999999998],
         'option_B.v01': [5.0, 0.7999999999999998],
         'option_B.v02': [5.0, 1.7999999999999998],
         'option_B.v03': [6.0, 1.7999999999999998],
         'option_B.v04': [6.0, 2.8],
         'option_B.v05': [8.0, 2.8],
         'option_B.v06': [8.0, 1.7999999999999998],
         'option_B.v07': [10.0, 1.7999999999999998],
         'option_B.v08': [10.0, 2.8],
         'option_B.v09': [9.0, 2.8],
         'option_B.v10': [9.0, 3.8],
         'option_B.v11': [6.0, 3.8],
         'option_B.v12': [6.0, 4.8],
         'option_B.v13': [5.0, 4.8],
         'option_B.v14': [5.0, 2.8],
         'option_B.v15': [4.0, 2.8],
         'option_C.v00': [12.0, -0.20000000000000018],
         'option_C.v01': [13.0, -0.20000000000000018],
         'option_C.v02': [13.0, 1.7999999999999998],
         'option_C.v03': [15.0, 1.7999999999999998],
         'option_C.v04': [15.0, 2.8],
         'option_C.v05': [16.0, 2.8],
         'option_C.v06': [16.0, 5.8],
         'option_C.v07': [15.0, 5.8],
         'option_C.v08': [15.0, 3.8],
         'option_C.v09': [13.0, 3.8],
         'option_C.v10': [13.0, 2.8],
         'option_C.v11': [12.0, 2.8],
         'option_D.v00': [19.0, 0.7999999999999998],
         'option_D.v01': [20.0, 0.7999999999999998],
         'option_D.v02': [20.0, 1.7999999999999998],
         'option_D.v03': [21.0, 1.7999999999999998],
         'option_D.v04': [21.0, 2.8],
         'option_D.v05': [22.0, 2.8],
         'option_D.v06': [22.0, 0.7999999999999998],
         'option_D.v07': [23.0, 0.7999999999999998],
         'option_D.v08': [23.0, 3.8],
         'option_D.v09': [22.0, 3.8],
         'option_D.v10': [22.0, 4.8],
         'option_D.v11': [20.0, 4.8],
         'option_D.v12': [20.0, 2.8],
         'option_D.v13': [19.0, 2.8],
         'option_E.v00': [25.0, 2.3],
         'option_E.v01': [27.0, 2.3],
         'option_E.v02': [27.0, 1.2999999999999998],
         'option_E.v03': [29.0, 1.2999999999999998],
         'option_E.v04': [29.0, 2.3],
         'option_E.v05': [31.0, 2.3],
         'option_E.v06': [31.0, 3.3],
         'option_E.v07': [29.0, 3.3],
         'option_E.v08': [29.0, 4.3],
         'option_E.v09': [27.0, 4.3],
         'option_E.v10': [27.0, 3.3],
         'option_E.v11': [25.0, 3.3]}
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane568.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-2.2919372458578593, 31.79193724585786], ylim=[-10.891937245857859, 23.191937245857858]) as c:
            for object_id, vertices, codes in [('source0', [self.points['source0.v00'], self.points['source0.v01'], self.points['source0.v02'], self.points['source0.v03'], self.points['source0.v04'], self.points['source0.v05'], self.points['source0.v06'], self.points['source0.v07'], self.points['source0.v00']], [1, 2, 2, 2, 2, 2, 2, 2, 79]), ('source1', [self.points['source1.v00'], self.points['source1.v01'], self.points['source1.v02'], self.points['source1.v03'], self.points['source1.v04'], self.points['source1.v05'], self.points['source1.v06'], self.points['source1.v07'], self.points['source1.v00']], [1, 2, 2, 2, 2, 2, 2, 2, 79]), ('option_A', [self.points['option_A.v00'], self.points['option_A.v01'], self.points['option_A.v02'], self.points['option_A.v03'], self.points['option_A.v04'], self.points['option_A.v05'], self.points['option_A.v06'], self.points['option_A.v07'], self.points['option_A.v00']], [1, 2, 2, 2, 2, 2, 2, 2, 79]), ('option_B', [self.points['option_B.v00'], self.points['option_B.v01'], self.points['option_B.v02'], self.points['option_B.v03'], self.points['option_B.v04'], self.points['option_B.v05'], self.points['option_B.v06'], self.points['option_B.v07'], self.points['option_B.v08'], self.points['option_B.v09'], self.points['option_B.v10'], self.points['option_B.v11'], self.points['option_B.v12'], self.points['option_B.v13'], self.points['option_B.v14'], self.points['option_B.v15'], self.points['option_B.v00']], [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 79]), ('option_C', [self.points['option_C.v00'], self.points['option_C.v01'], self.points['option_C.v02'], self.points['option_C.v03'], self.points['option_C.v04'], self.points['option_C.v05'], self.points['option_C.v06'], self.points['option_C.v07'], self.points['option_C.v08'], self.points['option_C.v09'], self.points['option_C.v10'], self.points['option_C.v11'], self.points['option_C.v00']], [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 79]), ('option_D', [self.points['option_D.v00'], self.points['option_D.v01'], self.points['option_D.v02'], self.points['option_D.v03'], self.points['option_D.v04'], self.points['option_D.v05'], self.points['option_D.v06'], self.points['option_D.v07'], self.points['option_D.v08'], self.points['option_D.v09'], self.points['option_D.v10'], self.points['option_D.v11'], self.points['option_D.v12'], self.points['option_D.v13'], self.points['option_D.v00']], [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 79]), ('option_E', [self.points['option_E.v00'], self.points['option_E.v01'], self.points['option_E.v02'], self.points['option_E.v03'], self.points['option_E.v04'], self.points['option_E.v05'], self.points['option_E.v06'], self.points['option_E.v07'], self.points['option_E.v08'], self.points['option_E.v09'], self.points['option_E.v10'], self.points['option_E.v11'], self.points['option_E.v00']], [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 79])]:
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
    print(Plane568().draw(sys.argv[1] if len(sys.argv) > 1 else None))
