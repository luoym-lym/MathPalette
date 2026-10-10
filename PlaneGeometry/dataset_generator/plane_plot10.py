"""Frozen MathVerse question Plane10; source key s479."""
from pathlib import Path
import sys
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.geometry_dataset import draw_question, read_json

class Plane10:
    def __init__(self):
        self.id = 'Plane10'
        self.source_dataset = 'MathVerse'
        self.query = 'As shown in the figure, then the degree of angle APB is ()\nChoices:\nA:80°\nB:140°\nC:20°\nD:50°'
        self.answer = 'C'
        self.answer_type = 'choice'
        self.subject = 'PlaneGeometry'
        self.level = 'middle_school'
        self.scene_path = Path(__file__).with_name("scenes") / "Plane10.json"

    def get_scene(self):
        return read_json(self.scene_path)

    def draw(self, output_path=None):
        return draw_question('PlaneGeometry', self.scene_path, output_path)

if __name__ == "__main__":
    result = Plane10().draw()
    print(result["image_path"])
