"""Approved frozen SOLIDGEO question Solid24."""
from pathlib import Path
import sys
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.geometry_dataset import draw_question, read_json

class Solid24:
    def __init__(self):
        self.id = 'Solid24'
        self.source_dataset = 'SOLIDGEO'
        self.query = 'Two cubes with equal edge lengths are placed as shown in the figure. Each face is labeled with a number, and the numbers on opposite faces of each cube sum to 10. Find the sum of the numbers on all faces that are not visible in the figure.'
        self.answer = '50'
        self.answer_type = 'number'
        self.subject = 'SolidGeometry'
        self.level = 'unspecified'
        self.scene_path = Path(__file__).with_name('scenes') / 'Solid24.json'

    def get_scene(self):
        return read_json(self.scene_path)

    def draw(self, output_path=None):
        return draw_question('SolidGeometry', self.scene_path, output_path)

if __name__ == '__main__':
    print(Solid24().draw()['image_path'])
