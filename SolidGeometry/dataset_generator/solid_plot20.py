"""Approved frozen SOLIDGEO question Solid20."""
from pathlib import Path
import sys
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.geometry_dataset import draw_question, read_json

class Solid20:
    def __init__(self):
        self.id = 'Solid20'
        self.source_dataset = 'SOLIDGEO'
        self.query = 'As shown in the figure, a cuboid has length 3, width 2, and height 4. Point $B$ lies on an edge, with $BC = 1$. Find the shortest distance an ant can crawl from point $A$ to point $B$ along the surface of the cuboid.'
        self.answer = '5'
        self.answer_type = 'number'
        self.subject = 'SolidGeometry'
        self.level = 'unspecified'
        self.scene_path = Path(__file__).with_name('scenes') / 'Solid20.json'

    def get_scene(self):
        return read_json(self.scene_path)

    def draw(self, output_path=None):
        return draw_question('SolidGeometry', self.scene_path, output_path)

if __name__ == '__main__':
    print(Solid20().draw()['image_path'])
