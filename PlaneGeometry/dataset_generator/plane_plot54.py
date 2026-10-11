"""Frozen MathVista testmini/698; user-reviewed import."""
from pathlib import Path
import sys
_ROOT = Path(__file__).resolve().parents[2]
if str(_ROOT) not in sys.path: sys.path.insert(0, str(_ROOT))
from dataset_tools.geometry_dataset import draw_question, read_json

class Plane54:
    def __init__(self):
        self.id = 'Plane54'
        self.source_dataset = 'MathVista'
        self.query = 'In the triangle in the figure above, what is the value of x?\nChoices:\nA: 2*\\sqrt{3}\nB: 6*\\sqrt{2}\nC: 6*\\sqrt{3}\nD: 6\nE: 12'
        self.answer = 'A'
        self.answer_type = 'choice'
        self.subject = 'PlaneGeometry'
        self.level = 'high_school'
        self.scene_path = Path(__file__).with_name('scenes') / 'Plane54.json'
    def get_scene(self):
        return read_json(self.scene_path)
    def draw(self, output_path=None):
        return draw_question('PlaneGeometry', self.scene_path, output_path)

if __name__ == '__main__': print(Plane54().draw())
