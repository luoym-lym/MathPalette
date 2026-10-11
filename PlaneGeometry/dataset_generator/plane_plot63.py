"""Frozen MathVista testmini/804; user-reviewed import."""
from pathlib import Path
import sys
_ROOT = Path(__file__).resolve().parents[2]
if str(_ROOT) not in sys.path: sys.path.insert(0, str(_ROOT))
from dataset_tools.geometry_dataset import draw_question, read_json

class Plane63:
    def __init__(self):
        self.id = 'Plane63'
        self.source_dataset = 'MathVista'
        self.query = 'In $\\odot B$, $CE=13.5$. Find $BD$. Round to the nearest hundredth.\nChoices:\nA: 3.71\nB: 4.29\nC: 4.53\nD: 6.75'
        self.answer = 'B'
        self.answer_type = 'choice'
        self.subject = 'PlaneGeometry'
        self.level = 'high_school'
        self.scene_path = Path(__file__).with_name('scenes') / 'Plane63.json'
    def get_scene(self):
        return read_json(self.scene_path)
    def draw(self, output_path=None):
        return draw_question('PlaneGeometry', self.scene_path, output_path)

if __name__ == '__main__': print(Plane63().draw())
