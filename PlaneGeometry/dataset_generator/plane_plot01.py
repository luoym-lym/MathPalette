"""Frozen MathVerse question Plane01; source key s34."""
from pathlib import Path
import sys
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.geometry_dataset import draw_question, read_json

class Plane01:
    def __init__(self):
        self.id = 'Plane01'
        self.source_dataset = 'MathVerse'
        self.query = 'As shown in the figure, triangle ABC congruent triangle ADE, then the degree of angle EAC is ()\nChoices:\nA:40°\nB:45°\nC:35°\nD:25°'
        self.answer = 'B'
        self.answer_type = 'choice'
        self.subject = 'PlaneGeometry'
        self.level = 'middle_school'
        self.scene_path = Path(__file__).with_name("scenes") / "Plane01.json"

    def get_scene(self):
        return read_json(self.scene_path)

    def draw(self, output_path=None):
        return draw_question('PlaneGeometry', self.scene_path, output_path)

if __name__ == "__main__":
    result = Plane01().draw()
    print(result["image_path"])
