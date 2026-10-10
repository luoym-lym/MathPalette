"""Frozen MathVerse question Plane13; source key s719."""
from pathlib import Path
import sys
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.geometry_dataset import draw_question, read_json

class Plane13:
    def __init__(self):
        self.id = 'Plane13'
        self.source_dataset = 'MathVerse'
        self.query = '\\[The height h of the racket hit is ()\nChoices:\nA:\\frac{8}{5}m\nB:\\frac{4}{3}m\nC:1m\nD:\\frac{8}{15}m\\]'
        self.answer = 'D'
        self.answer_type = 'choice'
        self.subject = 'PlaneGeometry'
        self.level = 'high_school'
        self.scene_path = Path(__file__).with_name("scenes") / "Plane13.json"

    def get_scene(self):
        return read_json(self.scene_path)

    def draw(self, output_path=None):
        return draw_question('PlaneGeometry', self.scene_path, output_path)

if __name__ == "__main__":
    result = Plane13().draw()
    print(result["image_path"])
