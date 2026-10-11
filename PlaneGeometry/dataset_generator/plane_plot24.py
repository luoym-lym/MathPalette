"""Frozen MathVista testmini/84; user-reviewed import."""
from pathlib import Path
import sys
_ROOT = Path(__file__).resolve().parents[2]
if str(_ROOT) not in sys.path: sys.path.insert(0, str(_ROOT))
from dataset_tools.geometry_dataset import draw_question, read_json

class Plane24:
    def __init__(self):
        self.id = 'Plane24'
        self.source_dataset = 'MathVista'
        self.query = 'ABCD is a square. Inscribed Circle center is O. Find the the angle of ∠AMK. Return the numeric value.'
        self.answer = '130.9'
        self.answer_type = 'number'
        self.subject = 'PlaneGeometry'
        self.level = 'high_school'
        self.scene_path = Path(__file__).with_name('scenes') / 'Plane24.json'
    def get_scene(self):
        return read_json(self.scene_path)
    def draw(self, output_path=None):
        return draw_question('PlaneGeometry', self.scene_path, output_path)

if __name__ == '__main__': print(Plane24().draw())
