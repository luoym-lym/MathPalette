"""Frozen MathVista testmini/234; user-reviewed import."""
from pathlib import Path
import sys
_ROOT = Path(__file__).resolve().parents[2]
if str(_ROOT) not in sys.path: sys.path.insert(0, str(_ROOT))
from dataset_tools.geometry_dataset import draw_question, read_json

class Plane29:
    def __init__(self):
        self.id = 'Plane29'
        self.source_dataset = 'MathVista'
        self.query = 'In the figure shown above, AC = 6. What is the length of segment AB?\nChoices:\nA: 3\nB: 5\nC: 6\nD: 7\nE: It cannot be determined from the information given'
        self.answer = 'C'
        self.answer_type = 'choice'
        self.subject = 'PlaneGeometry'
        self.level = 'high_school'
        self.scene_path = Path(__file__).with_name('scenes') / 'Plane29.json'
    def get_scene(self):
        return read_json(self.scene_path)
    def draw(self, output_path=None):
        return draw_question('PlaneGeometry', self.scene_path, output_path)

if __name__ == '__main__': print(Plane29().draw())
