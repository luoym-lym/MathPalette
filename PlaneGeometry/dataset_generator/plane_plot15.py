"""Frozen MathVerse question Plane15; source key s874."""
from pathlib import Path
import sys
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.geometry_dataset import draw_question, read_json

class Plane15:
    def __init__(self):
        self.id = 'Plane15'
        self.source_dataset = 'MathVerse'
        self.query = 'As shown in the figure, then the degree of angle AOB is ()\nChoices:\nA:40°\nB:50°\nC:80°\nD:100°'
        self.answer = 'C'
        self.answer_type = 'choice'
        self.subject = 'PlaneGeometry'
        self.level = 'high_school'
        self.scene_path = Path(__file__).with_name("scenes") / "Plane15.json"

    def get_scene(self):
        return read_json(self.scene_path)

    def draw(self, output_path=None):
        return draw_question('PlaneGeometry', self.scene_path, output_path)

if __name__ == "__main__":
    result = Plane15().draw()
    print(result["image_path"])
