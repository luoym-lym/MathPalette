"""Frozen MathVista testmini/250; user-reviewed import."""
from pathlib import Path
import sys
_ROOT = Path(__file__).resolve().parents[2]
if str(_ROOT) not in sys.path: sys.path.insert(0, str(_ROOT))
from dataset_tools.geometry_dataset import draw_question, read_json

class Plane32:
    def __init__(self):
        self.id = 'Plane32'
        self.source_dataset = 'MathVista'
        self.query = 'The area $A$ of the shaded region is given. Find $x$. $A = 66$ cm$^2$ .\nChoices:\nA: 4.6\nB: 6.5\nC: 13.0\nD: 26.0'
        self.answer = 'C'
        self.answer_type = 'choice'
        self.subject = 'PlaneGeometry'
        self.level = 'high_school'
        self.scene_path = Path(__file__).with_name('scenes') / 'Plane32.json'
    def get_scene(self):
        return read_json(self.scene_path)
    def draw(self, output_path=None):
        return draw_question('PlaneGeometry', self.scene_path, output_path)

if __name__ == '__main__': print(Plane32().draw())
