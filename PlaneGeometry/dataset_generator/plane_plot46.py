"""Frozen MathVista testmini/434; user-reviewed import."""
from pathlib import Path
import sys
_ROOT = Path(__file__).resolve().parents[2]
if str(_ROOT) not in sys.path: sys.path.insert(0, str(_ROOT))
from dataset_tools.geometry_dataset import draw_question, read_json

class Plane46:
    def __init__(self):
        self.id = 'Plane46'
        self.source_dataset = 'MathVista'
        self.query = 'In the figure above, side AC of triangle ABC is on line l. What is x in terms of k?\nChoices:\nA: 60-k\nB: k\nC: 60+k\nD: 120-k\nE: 120-2*k'
        self.answer = 'A'
        self.answer_type = 'choice'
        self.subject = 'PlaneGeometry'
        self.level = 'high_school'
        self.scene_path = Path(__file__).with_name('scenes') / 'Plane46.json'
    def get_scene(self):
        return read_json(self.scene_path)
    def draw(self, output_path=None):
        return draw_question('PlaneGeometry', self.scene_path, output_path)

if __name__ == '__main__': print(Plane46().draw())
