"""Frozen MathVista testmini/744; user-reviewed import."""
from pathlib import Path
import sys
_ROOT = Path(__file__).resolve().parents[2]
if str(_ROOT) not in sys.path: sys.path.insert(0, str(_ROOT))
from dataset_tools.geometry_dataset import draw_question, read_json

class Plane57:
    def __init__(self):
        self.id = 'Plane57'
        self.source_dataset = 'MathVista'
        self.query = 'If RL = 5, RT = 9, and WS = 6, find RW.\nChoices:\nA: 5.4\nB: 6\nC: 6.6\nD: 7.5'
        self.answer = 'D'
        self.answer_type = 'choice'
        self.subject = 'PlaneGeometry'
        self.level = 'high_school'
        self.scene_path = Path(__file__).with_name('scenes') / 'Plane57.json'
    def get_scene(self):
        return read_json(self.scene_path)
    def draw(self, output_path=None):
        return draw_question('PlaneGeometry', self.scene_path, output_path)

if __name__ == '__main__': print(Plane57().draw())
