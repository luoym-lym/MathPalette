"""Frozen MathVerse question Plane04; source key s244."""
from pathlib import Path
import sys
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.geometry_dataset import draw_question, read_json

class Plane04:
    def __init__(self):
        self.id = 'Plane04'
        self.source_dataset = 'MathVerse'
        self.query = 'As shown in the figure, in the inscribed pentagon ABCDE of circle O, then the degree of angle B is ()\nChoices:\nA:50°\nB:75°\nC:80°\nD:100°'
        self.answer = 'D'
        self.answer_type = 'numeric'
        self.subject = 'PlaneGeometry'
        self.level = 'middle_school'
        self.scene_path = Path(__file__).with_name("scenes") / "Plane04.json"

    def get_scene(self):
        return read_json(self.scene_path)

    def draw(self, output_path=None):
        return draw_question('PlaneGeometry', self.scene_path, output_path)

if __name__ == "__main__":
    result = Plane04().draw()
    print(result["image_path"])
