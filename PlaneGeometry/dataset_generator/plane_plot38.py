"""Frozen MathVista testmini/333; user-reviewed import."""
from pathlib import Path
import sys
_ROOT = Path(__file__).resolve().parents[2]
if str(_ROOT) not in sys.path: sys.path.insert(0, str(_ROOT))
from dataset_tools.geometry_dataset import draw_question, read_json

class Plane38:
    def __init__(self):
        self.id = 'Plane38'
        self.source_dataset = 'MathVista'
        self.query = 'Find tan X\nChoices:\nA: \\frac { 5 } { 12 }\nB: \\frac { 12 } { 13 }\nC: \\frac { 17 } { 12 }\nD: \\frac { 12 } { 5 }'
        self.answer = 'A'
        self.answer_type = 'choice'
        self.subject = 'PlaneGeometry'
        self.level = 'high_school'
        self.scene_path = Path(__file__).with_name('scenes') / 'Plane38.json'
    def get_scene(self):
        return read_json(self.scene_path)
    def draw(self, output_path=None):
        return draw_question('PlaneGeometry', self.scene_path, output_path)

if __name__ == '__main__': print(Plane38().draw())
