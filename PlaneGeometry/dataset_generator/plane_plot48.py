"""Frozen MathVista testmini/583; user-reviewed import."""
from pathlib import Path
import sys
_ROOT = Path(__file__).resolve().parents[2]
if str(_ROOT) not in sys.path: sys.path.insert(0, str(_ROOT))
from dataset_tools.geometry_dataset import draw_question, read_json

class Plane48:
    def __init__(self):
        self.id = 'Plane48'
        self.source_dataset = 'MathVista'
        self.query = 'Find x. Round to the nearest tenth.\r\n\nChoices:\nA: 5.8\nB: 6.5\nC: 14.2\nD: 44.3'
        self.answer = 'A'
        self.answer_type = 'choice'
        self.subject = 'PlaneGeometry'
        self.level = 'high_school'
        self.scene_path = Path(__file__).with_name('scenes') / 'Plane48.json'
    def get_scene(self):
        return read_json(self.scene_path)
    def draw(self, output_path=None):
        return draw_question('PlaneGeometry', self.scene_path, output_path)

if __name__ == '__main__': print(Plane48().draw())
