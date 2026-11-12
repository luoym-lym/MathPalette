"""Frozen question Plane158; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane158:

    def __init__(self):
        self.id = 'Plane158'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:93'
        self.question = 'Which of the figures can be cut into these 3 pieces?\nChoices:\nA:A\nB:B\nC:C\nD:D\nE:E'
        self.answer = 'C'
        self.answer_type = 'choice'
        self.choices = {'A': 'A', 'B': 'B', 'C': 'C', 'D': 'D', 'E': 'E'}
        self.query = self.question
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane158.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=(-2.1506186337868964, 25.68591803131092), ylim=(-10.772995373724154, 17.063541291373664), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
            c.path([[8.0, 9.0], [7.447715250169207, 9.0], [7.0, 8.552284749830793], [7.0, 8.0], [7.0, 7.447715250169207], [7.447715250169207, 7.0], [8.0, 7.0], [10.0, 9.0], [8.0, 9.0], [8.0, 9.0]], [1, 4, 4, 4, 4, 4, 4, 2, 2, 79], id='given_compound', capstyle='butt')
            c.path([[12.0, 9.0], [11.447715250169207, 9.0], [11.0, 8.552284749830793], [11.0, 8.0], [11.0, 7.447715250169207], [11.447715250169207, 7.0], [12.0, 7.0], [12.0, 9.0], [12.0, 9.0]], [1, 4, 4, 4, 4, 4, 4, 2, 79], id='given_semicircle', capstyle='butt')
            c.path([[14.0, 9.0], [16.0, 9.0], [16.0, 7.0], [14.0, 9.0]], [1, 2, 2, 79], id='given_triangle', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[14.0, 9.0], [16.0, 9.0], [16.0, 7.0], [14.0, 9.0]], [1, 2, 2, 79], id='given_triangle', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[0.0, -1.7320508075688772], [0.47829262347620033, -2.0081931824842743], [1.0898830288690415, -1.8443180272606394], [1.3660254037844384, -1.3660254037844388], [1.6421677786998352, -0.8877327803082383], [1.478292623476201, -0.276142374915397], [1.0000000000000004, -1.1102230246251565e-16], [1.0, 0.5522847498307935], [0.5522847498307936, 1.0], [6.123233995736766e-17, 1.0], [-0.5522847498307933, 1.0], [-0.9999999999999999, 0.5522847498307936], [-1.0, 1.2246467991473532e-16], [-1.4782926234762008, -0.27614237491539684], [-1.6421677786998354, -0.8877327803082382], [-1.3660254037844386, -1.3660254037844388], [-1.0898830288690418, -1.8443180272606394], [-0.47829262347620044, -2.008193182484274], [1.1102230246251565e-16, -1.7320508075688772], [0.0, -1.7320508075688772]], [1, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 79], id='A_three_lobes', capstyle='butt')
            c.circle([6.0, -0.3], 1.5, id='B_circle')
            c.path([[12.0, -1.800213562373095], [13.414213562373096, -0.386], [13.804737854124365, 0.004524291751270115], [13.804737854124365, 0.637689270621825], [13.414213562373096, 1.028213562373095], [13.023689270621826, 1.4187378541243651], [12.39052429175127, 1.4187378541243651], [12.0, 1.0282135623730952], [11.60947570824873, 1.4187378541243651], [10.976310729378174, 1.4187378541243651], [10.585786437626904, 1.0282135623730952], [10.195262145875635, 0.6376892706218253], [10.195262145875635, 0.004524291751270171], [10.585786437626904, -0.3859999999999999], [12.0, -1.800213562373095], [12.0, -1.800213562373095]], [1, 2, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 2, 79], id='C_heart', capstyle='butt')
            c.path([[17.0, -1.8], [19.0, -1.8], [19.0, 1.2], [17.0, 1.2], [17.0, -1.8]], [1, 2, 2, 2, 79], id='D_rectangle', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[17.0, -1.8], [19.0, -1.8], [19.0, 1.2], [17.0, 1.2], [17.0, -1.8]], [1, 2, 2, 2, 79], id='D_rectangle', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[23.0, 1.2], [23.0, -0.8], [23.0, -1.3522847498307935], [23.447715250169207, -1.8], [24.0, -1.8], [24.552284749830793, -1.8], [25.0, -1.3522847498307937], [25.0, -0.8000000000000003], [25.0, 1.2], [23.0, 1.2], [23.0, 1.2]], [1, 2, 4, 4, 4, 4, 4, 4, 2, 2, 79], id='E_round_bottom', capstyle='butt')
            for object_id, text, anchor in [('label0', '(A)', (0.0, -2.4)), ('label1', '(B)', (6.0, -2.4)), ('label2', '(C)', (12.0, -2.4)), ('label3', '(D)', (18.0, -2.4)), ('label4', '(E)', (24.0, -2.4))]:
                c.text(text, anchor, id=object_id, rotation_mode='default', offset_pt=(0, 0), annotation_clip=None)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane158().draw(sys.argv[1] if len(sys.argv) > 1 else None))
