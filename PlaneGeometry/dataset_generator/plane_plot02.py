"""Frozen MathVerse question Plane02; source key s209."""
from pathlib import Path
import sys
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.geometry_dataset import draw_question, read_json

class Plane02:
    def __init__(self):
        self.id = 'Plane02'
        self.source_dataset = 'MathVerse'
        self.query = 'It is known that BC parallel PQ, AB:AP = 2.0:5.0, then the length of CQ is ()\nChoices:\nA:8cm\nB:12cm\nC:30cm\nD:50cm'
        self.answer = 'B'
        self.answer_type = 'choice'
        self.subject = 'PlaneGeometry'
        self.level = 'middle_school'
        self.scene_path = Path(__file__).with_name("scenes") / "Plane02.json"

    def get_scene(self):
        return read_json(self.scene_path)

    def draw(self, output_path=None):
        return draw_question('PlaneGeometry', self.scene_path, output_path)

if __name__ == "__main__":
    result = Plane02().draw()
    print(result["image_path"])
