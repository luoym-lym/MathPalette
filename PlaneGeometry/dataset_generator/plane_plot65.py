"""Frozen MathVista testmini/822; user-reviewed import."""
from pathlib import Path
import sys
_ROOT = Path(__file__).resolve().parents[2]
if str(_ROOT) not in sys.path: sys.path.insert(0, str(_ROOT))
from dataset_tools.geometry_dataset import draw_question, read_json

class Plane65:
    def __init__(self):
        self.id = 'Plane65'
        self.source_dataset = 'MathVista'
        self.query = 'Find the perimeter of the parallelogram. Round to the nearest tenth if necessary.\nChoices:\nA: 22\nB: 40\nC: 44\nD: 48'
        self.answer = 'C'
        self.answer_type = 'choice'
        self.subject = 'PlaneGeometry'
        self.level = 'high_school'
        self.scene_path = Path(__file__).with_name('scenes') / 'Plane65.json'
    def get_scene(self):
        return read_json(self.scene_path)
    def draw(self, output_path=None):
        return draw_question('PlaneGeometry', self.scene_path, output_path)

if __name__ == '__main__': print(Plane65().draw())
