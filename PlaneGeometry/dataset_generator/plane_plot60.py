"""Frozen MathVista testmini/776; user-reviewed import."""
from pathlib import Path
import sys
_ROOT = Path(__file__).resolve().parents[2]
if str(_ROOT) not in sys.path: sys.path.insert(0, str(_ROOT))
from dataset_tools.geometry_dataset import draw_question, read_json

class Plane60:
    def __init__(self):
        self.id = 'Plane60'
        self.source_dataset = 'MathVista'
        self.query = 'Find $JQ$ if $Q$ is the incenter of $\\triangle JLN$.  Rounded to the nearest hundredth.\nChoices:\nA: 16.50\nB: 18.79\nC: 20.32\nD: 25.50'
        self.answer = 'B'
        self.answer_type = 'choice'
        self.subject = 'PlaneGeometry'
        self.level = 'high_school'
        self.scene_path = Path(__file__).with_name('scenes') / 'Plane60.json'
    def get_scene(self):
        return read_json(self.scene_path)
    def draw(self, output_path=None):
        return draw_question('PlaneGeometry', self.scene_path, output_path)

if __name__ == '__main__': print(Plane60().draw())
