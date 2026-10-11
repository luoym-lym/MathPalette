"""Frozen MathVista testmini/30; user-reviewed import."""
from pathlib import Path
import sys
_ROOT = Path(__file__).resolve().parents[2]
if str(_ROOT) not in sys.path: sys.path.insert(0, str(_ROOT))
from dataset_tools.geometry_dataset import draw_question, read_json

class Plane18:
    def __init__(self):
        self.id = 'Plane18'
        self.source_dataset = 'MathVista'
        self.query = 'As shown in the figure, the two chords AB and CD in the circle intersect at E, ∠D = 35.0, ∠AEC = 105.0, then ∠C = ()\nChoices:\nA: 60°\nB: 70°\nC: 80°\nD: 85°'
        self.answer = 'B'
        self.answer_type = 'choice'
        self.subject = 'PlaneGeometry'
        self.level = 'high_school'
        self.scene_path = Path(__file__).with_name('scenes') / 'Plane18.json'
    def get_scene(self):
        return read_json(self.scene_path)
    def draw(self, output_path=None):
        return draw_question('PlaneGeometry', self.scene_path, output_path)

if __name__ == '__main__': print(Plane18().draw())
