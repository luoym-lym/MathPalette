"""Frozen MathVista testmini/716; user-reviewed import."""
from pathlib import Path
import sys
_ROOT = Path(__file__).resolve().parents[2]
if str(_ROOT) not in sys.path: sys.path.insert(0, str(_ROOT))
from dataset_tools.geometry_dataset import draw_question, read_json

class Plane55:
    def __init__(self):
        self.id = 'Plane55'
        self.source_dataset = 'MathVista'
        self.query = 'Find y.\nChoices:\nA: 16 \\sqrt { 2 }\nB: 16 \\sqrt { 3 }\nC: 32\nD: 16 \\sqrt { 5 }'
        self.answer = 'D'
        self.answer_type = 'choice'
        self.subject = 'PlaneGeometry'
        self.level = 'high_school'
        self.scene_path = Path(__file__).with_name('scenes') / 'Plane55.json'
    def get_scene(self):
        return read_json(self.scene_path)
    def draw(self, output_path=None):
        return draw_question('PlaneGeometry', self.scene_path, output_path)

if __name__ == '__main__': print(Plane55().draw())
