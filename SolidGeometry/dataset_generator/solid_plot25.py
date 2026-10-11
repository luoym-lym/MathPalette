"""Approved frozen SOLIDGEO question Solid25."""
from pathlib import Path
import sys
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.geometry_dataset import draw_question, read_json

class Solid25:
    def __init__(self):
        self.id = 'Solid25'
        self.source_dataset = 'SOLIDGEO'
        self.query = 'During a three-dimensional model sketching lesson, an art teacher arranges 14 cubes, each with edge length 1 decimeter, on a desk as shown in the figure. The teacher paints the exposed surfaces with different colors. Find the total area of the painted surfaces, in square decimeters.'
        self.answer = '33 dm²'
        self.answer_type = 'number'
        self.subject = 'SolidGeometry'
        self.level = 'unspecified'
        self.scene_path = Path(__file__).with_name('scenes') / 'Solid25.json'

    def get_scene(self):
        return read_json(self.scene_path)

    def draw(self, output_path=None):
        return draw_question('SolidGeometry', self.scene_path, output_path)

if __name__ == '__main__':
    print(Solid25().draw()['image_path'])
