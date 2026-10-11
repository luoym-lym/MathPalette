"""Frozen MathVista testmini/690; user-reviewed import."""
from pathlib import Path
import sys
_ROOT = Path(__file__).resolve().parents[2]
if str(_ROOT) not in sys.path: sys.path.insert(0, str(_ROOT))
from dataset_tools.geometry_dataset import draw_question, read_json

class Plane53:
    def __init__(self):
        self.id = 'Plane53'
        self.source_dataset = 'MathVista'
        self.query = 'In the diagram above, lines M and N are parallel. All of the following are true except\nChoices:\nA: a + b = j + l\nB: g = h\nC: c + f = f + b\nD: g + e + f + h = 360\nE: d + e = f + j'
        self.answer = 'E'
        self.answer_type = 'choice'
        self.subject = 'PlaneGeometry'
        self.level = 'high_school'
        self.scene_path = Path(__file__).with_name('scenes') / 'Plane53.json'
    def get_scene(self):
        return read_json(self.scene_path)
    def draw(self, output_path=None):
        return draw_question('PlaneGeometry', self.scene_path, output_path)

if __name__ == '__main__': print(Plane53().draw())
