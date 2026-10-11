"""Frozen MathVista testmini/300; user-reviewed import."""
from pathlib import Path
import sys
_ROOT = Path(__file__).resolve().parents[2]
if str(_ROOT) not in sys.path: sys.path.insert(0, str(_ROOT))
from dataset_tools.geometry_dataset import draw_question, read_json

class Plane34:
    def __init__(self):
        self.id = 'Plane34'
        self.source_dataset = 'MathVista'
        self.query = '$\\overline{HK}$ and $\\overline{IG}$ are diameters of $\\odot L$. Find $m \\widehat {IHJ}$.\nChoices:\nA: 59\nB: 135\nC: 270\nD: 301'
        self.answer = 'C'
        self.answer_type = 'choice'
        self.subject = 'PlaneGeometry'
        self.level = 'high_school'
        self.scene_path = Path(__file__).with_name('scenes') / 'Plane34.json'
    def get_scene(self):
        return read_json(self.scene_path)
    def draw(self, output_path=None):
        return draw_question('PlaneGeometry', self.scene_path, output_path)

if __name__ == '__main__': print(Plane34().draw())
