"""Approved frozen SOLIDGEO question Solid19."""
from pathlib import Path
import sys
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.geometry_dataset import draw_question, read_json

class Solid19:
    def __init__(self):
        self.id = 'Solid19'
        self.source_dataset = 'SOLIDGEO'
        self.query = 'As shown in the figure, an ant crawls from point $A$ to point $B$ along the surface of a rectangular prism with length, width, and height of 2, 3, and 1 decimeters, respectively. Find the shortest distance the ant can crawl, in decimeters. Give your answer in radical form.'
        self.answer = '3√2 dm'
        self.answer_type = 'number'
        self.subject = 'SolidGeometry'
        self.level = 'unspecified'
        self.scene_path = Path(__file__).with_name('scenes') / 'Solid19.json'

    def get_scene(self):
        return read_json(self.scene_path)

    def draw(self, output_path=None):
        return draw_question('SolidGeometry', self.scene_path, output_path)

if __name__ == '__main__':
    print(Solid19().draw()['image_path'])
