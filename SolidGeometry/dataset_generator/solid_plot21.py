"""Approved frozen SOLIDGEO question Solid21."""
from pathlib import Path
import sys
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.geometry_dataset import draw_question, read_json

class Solid21:
    def __init__(self):
        self.id = 'Solid21'
        self.source_dataset = 'SOLIDGEO'
        self.query = 'A cubic object slides down a slope, and its cross-section is shown in the figure. Square $DEFH$ has side length 2 meters, the slope angle is $\\angle A = 30^\\circ$, $\\angle B = 90^\\circ$, and $BC = 6$ meters. Find $AE$, in meters, when $DC^2 = AE^2 + BC^2$. (Hint: Connect $DC$.)'
        self.answer = '14/3 m'
        self.answer_type = 'number'
        self.subject = 'SolidGeometry'
        self.level = 'unspecified'
        self.scene_path = Path(__file__).with_name('scenes') / 'Solid21.json'

    def get_scene(self):
        return read_json(self.scene_path)

    def draw(self, output_path=None):
        return draw_question('SolidGeometry', self.scene_path, output_path)

if __name__ == '__main__':
    print(Solid21().draw()['image_path'])
