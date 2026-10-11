"""Approved frozen SOLIDGEO question Solid17."""
from pathlib import Path
import sys
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.geometry_dataset import draw_question, read_json

class Solid17:
    def __init__(self):
        self.id = 'Solid17'
        self.source_dataset = 'SOLIDGEO'
        self.query = 'As shown in the figure, a rectangular piece of cardboard is $3 \\mathrm{cm}$ long and $2 \\mathrm{cm}$ wide. Find the volume of the solid obtained by rotating it as shown.'
        self.answer = '12π cm³'
        self.answer_type = 'number'
        self.subject = 'SolidGeometry'
        self.level = 'unspecified'
        self.scene_path = Path(__file__).with_name('scenes') / 'Solid17.json'

    def get_scene(self):
        return read_json(self.scene_path)

    def draw(self, output_path=None):
        return draw_question('SolidGeometry', self.scene_path, output_path)

if __name__ == '__main__':
    print(Solid17().draw()['image_path'])
