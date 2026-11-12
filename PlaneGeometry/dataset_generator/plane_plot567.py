"""Frozen question Plane567; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane567:

    def __init__(self):
        self.id = 'Plane567'
        self.source_dataset = 'Author Designed'
        self.source_key = 'author-extensions95-v1:Plane248/extension_03'
        self.question = 'Two identical pieces may be rotated but may not be turned upside down. Which of the following pictures cannot be made with these two pieces?\nChoices:\nA:A\nB:B\nC:C\nD:D\nE:E'
        self.answer = 'B'
        self.answer_type = 'choice'
        self.choices = {'A': 'A', 'B': 'B', 'C': 'C', 'D': 'D', 'E': 'E'}
        self.query = self.question
        self.points = {'source0.v00': [10.0, 9.5],
         'source0.v01': [11.0, 9.5],
         'source0.v02': [11.0, 8.5],
         'source0.v03': [12.0, 8.5],
         'source0.v04': [12.0, 10.5],
         'source0.v05': [13.0, 10.5],
         'source0.v06': [13.0, 11.5],
         'source0.v07': [11.0, 11.5],
         'source0.v08': [11.0, 10.5],
         'source0.v09': [10.0, 10.5],
         'source1.v00': [15.0, 9.5],
         'source1.v01': [16.0, 9.5],
         'source1.v02': [16.0, 8.5],
         'source1.v03': [17.0, 8.5],
         'source1.v04': [17.0, 10.5],
         'source1.v05': [18.0, 10.5],
         'source1.v06': [18.0, 11.5],
         'source1.v07': [16.0, 11.5],
         'source1.v08': [16.0, 10.5],
         'source1.v09': [15.0, 10.5],
         'option_A.v00': [-2.0, 1.7999999999999998],
         'option_A.v01': [-1.0, 1.7999999999999998],
         'option_A.v02': [-1.0, 0.7999999999999998],
         'option_A.v03': [0.0, 0.7999999999999998],
         'option_A.v04': [0.0, 1.7999999999999998],
         'option_A.v05': [2.0, 1.7999999999999998],
         'option_A.v06': [2.0, 3.8],
         'option_A.v07': [1.0, 3.8],
         'option_A.v08': [1.0, 4.8],
         'option_A.v09': [0.0, 4.8],
         'option_A.v10': [0.0, 3.8],
         'option_A.v11': [-2.0, 3.8],
         'option_B.v00': [5.5, 0.2999999999999998],
         'option_B.v01': [6.5, 0.2999999999999998],
         'option_B.v02': [6.5, 1.2999999999999998],
         'option_B.v03': [8.5, 1.2999999999999998],
         'option_B.v04': [8.5, 4.3],
         'option_B.v05': [7.5, 4.3],
         'option_B.v06': [7.5, 5.3],
         'option_B.v07': [6.5, 5.3],
         'option_B.v08': [6.5, 4.3],
         'option_B.v09': [5.5, 4.3],
         'option_B.v10': [5.5, 3.3],
         'option_B.v11': [6.5, 3.3],
         'option_B.v12': [6.5, 2.3],
         'option_B.v13': [5.5, 2.3],
         'option_C.v00': [11.5, 0.7999999999999998],
         'option_C.v01': [12.5, 0.7999999999999998],
         'option_C.v02': [12.5, -0.20000000000000018],
         'option_C.v03': [13.5, -0.20000000000000018],
         'option_C.v04': [13.5, 1.7999999999999998],
         'option_C.v05': [14.5, 1.7999999999999998],
         'option_C.v06': [14.5, 2.8],
         'option_C.v07': [15.5, 2.8],
         'option_C.v08': [15.5, 3.8],
         'option_C.v09': [16.5, 3.8],
         'option_C.v10': [16.5, 4.8],
         'option_C.v11': [15.5, 4.8],
         'option_C.v12': [15.5, 5.8],
         'option_C.v13': [14.5, 5.8],
         'option_C.v14': [14.5, 3.8],
         'option_C.v15': [13.5, 3.8],
         'option_C.v16': [13.5, 2.8],
         'option_C.v17': [12.5, 2.8],
         'option_C.v18': [12.5, 1.7999999999999998],
         'option_C.v19': [11.5, 1.7999999999999998],
         'option_D.v00': [18.0, 1.2999999999999998],
         'option_D.v01': [20.0, 1.2999999999999998],
         'option_D.v02': [20.0, 2.3],
         'option_D.v03': [22.0, 2.3],
         'option_D.v04': [22.0, 1.2999999999999998],
         'option_D.v05': [23.0, 1.2999999999999998],
         'option_D.v06': [23.0, 3.3],
         'option_D.v07': [24.0, 3.3],
         'option_D.v08': [24.0, 4.3],
         'option_D.v09': [22.0, 4.3],
         'option_D.v10': [22.0, 3.3],
         'option_D.v11': [20.0, 3.3],
         'option_D.v12': [20.0, 4.3],
         'option_D.v13': [19.0, 4.3],
         'option_D.v14': [19.0, 2.3],
         'option_D.v15': [18.0, 2.3],
         'option_E.v00': [25.5, 1.7999999999999998],
         'option_E.v01': [27.5, 1.7999999999999998],
         'option_E.v02': [27.5, 0.7999999999999998],
         'option_E.v03': [28.5, 0.7999999999999998],
         'option_E.v04': [28.5, 1.7999999999999998],
         'option_E.v05': [29.5, 1.7999999999999998],
         'option_E.v06': [29.5, 2.8],
         'option_E.v07': [30.5, 2.8],
         'option_E.v08': [30.5, 3.8],
         'option_E.v09': [28.5, 3.8],
         'option_E.v10': [28.5, 4.8],
         'option_E.v11': [27.5, 4.8],
         'option_E.v12': [27.5, 3.8],
         'option_E.v13': [26.5, 3.8],
         'option_E.v14': [26.5, 2.8],
         'option_E.v15': [25.5, 2.8]}
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane567.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-2.791937245857863, 31.291937245857863], ylim=[-11.391937245857862, 22.691937245857865]) as c:
            for object_id, vertices, codes in [('source0', [self.points['source0.v00'], self.points['source0.v01'], self.points['source0.v02'], self.points['source0.v03'], self.points['source0.v04'], self.points['source0.v05'], self.points['source0.v06'], self.points['source0.v07'], self.points['source0.v08'], self.points['source0.v09'], self.points['source0.v00']], [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 79]), ('source1', [self.points['source1.v00'], self.points['source1.v01'], self.points['source1.v02'], self.points['source1.v03'], self.points['source1.v04'], self.points['source1.v05'], self.points['source1.v06'], self.points['source1.v07'], self.points['source1.v08'], self.points['source1.v09'], self.points['source1.v00']], [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 79]), ('option_A', [self.points['option_A.v00'], self.points['option_A.v01'], self.points['option_A.v02'], self.points['option_A.v03'], self.points['option_A.v04'], self.points['option_A.v05'], self.points['option_A.v06'], self.points['option_A.v07'], self.points['option_A.v08'], self.points['option_A.v09'], self.points['option_A.v10'], self.points['option_A.v11'], self.points['option_A.v00']], [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 79]), ('option_B', [self.points['option_B.v00'], self.points['option_B.v01'], self.points['option_B.v02'], self.points['option_B.v03'], self.points['option_B.v04'], self.points['option_B.v05'], self.points['option_B.v06'], self.points['option_B.v07'], self.points['option_B.v08'], self.points['option_B.v09'], self.points['option_B.v10'], self.points['option_B.v11'], self.points['option_B.v12'], self.points['option_B.v13'], self.points['option_B.v00']], [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 79]), ('option_C', [self.points['option_C.v00'], self.points['option_C.v01'], self.points['option_C.v02'], self.points['option_C.v03'], self.points['option_C.v04'], self.points['option_C.v05'], self.points['option_C.v06'], self.points['option_C.v07'], self.points['option_C.v08'], self.points['option_C.v09'], self.points['option_C.v10'], self.points['option_C.v11'], self.points['option_C.v12'], self.points['option_C.v13'], self.points['option_C.v14'], self.points['option_C.v15'], self.points['option_C.v16'], self.points['option_C.v17'], self.points['option_C.v18'], self.points['option_C.v19'], self.points['option_C.v00']], [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 79]), ('option_D', [self.points['option_D.v00'], self.points['option_D.v01'], self.points['option_D.v02'], self.points['option_D.v03'], self.points['option_D.v04'], self.points['option_D.v05'], self.points['option_D.v06'], self.points['option_D.v07'], self.points['option_D.v08'], self.points['option_D.v09'], self.points['option_D.v10'], self.points['option_D.v11'], self.points['option_D.v12'], self.points['option_D.v13'], self.points['option_D.v14'], self.points['option_D.v15'], self.points['option_D.v00']], [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 79]), ('option_E', [self.points['option_E.v00'], self.points['option_E.v01'], self.points['option_E.v02'], self.points['option_E.v03'], self.points['option_E.v04'], self.points['option_E.v05'], self.points['option_E.v06'], self.points['option_E.v07'], self.points['option_E.v08'], self.points['option_E.v09'], self.points['option_E.v10'], self.points['option_E.v11'], self.points['option_E.v12'], self.points['option_E.v13'], self.points['option_E.v14'], self.points['option_E.v15'], self.points['option_E.v00']], [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 79])]:
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
    print(Plane567().draw(sys.argv[1] if len(sys.argv) > 1 else None))
