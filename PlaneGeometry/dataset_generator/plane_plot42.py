"""Frozen MathVista testmini/388; user-reviewed import."""
from pathlib import Path
import sys
_ROOT = Path(__file__).resolve().parents[2]
if str(_ROOT) not in sys.path: sys.path.insert(0, str(_ROOT))
from dataset_tools.geometry_dataset import draw_question, read_json

class Plane42:
    def __init__(self):
        self.id = 'Plane42'
        self.source_dataset = 'MathVista'
        self.query = 'Express the ratio of $\\tan M$ as a decimal to the nearest hundredth.\nChoices:\nA: 0.38\nB: 0.42\nC: 0.92\nD: 2.40'
        self.answer = 'B'
        self.answer_type = 'choice'
        self.subject = 'PlaneGeometry'
        self.level = 'high_school'
        self.scene_path = Path(__file__).with_name('scenes') / 'Plane42.json'
    def get_scene(self):
        return read_json(self.scene_path)
    def draw(self, output_path=None):
        return draw_question('PlaneGeometry', self.scene_path, output_path)

if __name__ == '__main__': print(Plane42().draw())
