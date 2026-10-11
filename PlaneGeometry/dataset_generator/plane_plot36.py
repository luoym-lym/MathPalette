"""Frozen MathVista testmini/304; user-reviewed import."""
from pathlib import Path
import sys
_ROOT = Path(__file__).resolve().parents[2]
if str(_ROOT) not in sys.path: sys.path.insert(0, str(_ROOT))
from dataset_tools.geometry_dataset import draw_question, read_json

class Plane36:
    def __init__(self):
        self.id = 'Plane36'
        self.source_dataset = 'MathVista'
        self.query = 'In the figure above, two line segments meet at a point on line l. If the value of y is equal to the square of the value of x, what is the value of y?'
        self.answer = '100'
        self.answer_type = 'number'
        self.subject = 'PlaneGeometry'
        self.level = 'high_school'
        self.scene_path = Path(__file__).with_name('scenes') / 'Plane36.json'
    def get_scene(self):
        return read_json(self.scene_path)
    def draw(self, output_path=None):
        return draw_question('PlaneGeometry', self.scene_path, output_path)

if __name__ == '__main__': print(Plane36().draw())
