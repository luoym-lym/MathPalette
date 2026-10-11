"""Frozen MathVista testmini/610; user-reviewed import."""
from pathlib import Path
import sys
_ROOT = Path(__file__).resolve().parents[2]
if str(_ROOT) not in sys.path: sys.path.insert(0, str(_ROOT))
from dataset_tools.geometry_dataset import draw_question, read_json

class Plane49:
    def __init__(self):
        self.id = 'Plane49'
        self.source_dataset = 'MathVista'
        self.query = 'In the figure above, P, Q, and R lie on the same line. P is the center of the larger circle, and Q is the center of the smaller circle. If the radius of the larger circle is 4, what is the radius of the smaller circle?\nChoices:\nA: 1\nB: 2\nC: 4\nD: 8\nE: 16'
        self.answer = 'B'
        self.answer_type = 'choice'
        self.subject = 'PlaneGeometry'
        self.level = 'high_school'
        self.scene_path = Path(__file__).with_name('scenes') / 'Plane49.json'
    def get_scene(self):
        return read_json(self.scene_path)
    def draw(self, output_path=None):
        return draw_question('PlaneGeometry', self.scene_path, output_path)

if __name__ == '__main__': print(Plane49().draw())
