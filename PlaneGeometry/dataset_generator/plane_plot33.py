"""Frozen MathVista testmini/283; user-reviewed import."""
from pathlib import Path
import sys
_ROOT = Path(__file__).resolve().parents[2]
if str(_ROOT) not in sys.path: sys.path.insert(0, str(_ROOT))
from dataset_tools.geometry_dataset import draw_question, read_json

class Plane33:
    def __init__(self):
        self.id = 'Plane33'
        self.source_dataset = 'MathVista'
        self.query = '$\\overline{WTY} \\cong \\overline{TWY}$. Find $x$.\nChoices:\nA: 2\nB: 4\nC: 5\nD: 10'
        self.answer = 'C'
        self.answer_type = 'choice'
        self.subject = 'PlaneGeometry'
        self.level = 'high_school'
        self.scene_path = Path(__file__).with_name('scenes') / 'Plane33.json'
    def get_scene(self):
        return read_json(self.scene_path)
    def draw(self, output_path=None):
        return draw_question('PlaneGeometry', self.scene_path, output_path)

if __name__ == '__main__': print(Plane33().draw())
