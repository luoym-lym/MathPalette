"""Frozen MathVista testmini/6; user-reviewed import."""
from pathlib import Path
import sys
_ROOT = Path(__file__).resolve().parents[2]
if str(_ROOT) not in sys.path: sys.path.insert(0, str(_ROOT))
from dataset_tools.geometry_dataset import draw_question, read_json

class Plane17:
    def __init__(self):
        self.id = 'Plane17'
        self.source_dataset = 'MathVista'
        self.query = 'As shown in the figure, if CB = 4.0, DB = 7.0, and D is the midpoint of AC, then the length of AC is ()\nChoices:\nA: 6cm\nB: 7cm\nC: 4cm\nD: 5cm'
        self.answer = 'A'
        self.answer_type = 'choice'
        self.subject = 'PlaneGeometry'
        self.level = 'high_school'
        self.scene_path = Path(__file__).with_name('scenes') / 'Plane17.json'
    def get_scene(self):
        return read_json(self.scene_path)
    def draw(self, output_path=None):
        return draw_question('PlaneGeometry', self.scene_path, output_path)

if __name__ == '__main__': print(Plane17().draw())
