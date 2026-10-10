"""Frozen MathVerse question Plane07; source key s429."""
from pathlib import Path
import sys
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.geometry_dataset import draw_question, read_json

class Plane07:
    def __init__(self):
        self.id = 'Plane07'
        self.source_dataset = 'MathVerse'
        self.query = 'As shown in the figure, circle O is the circumscribed circle of triangle ABC. then the length of BC is ()\nChoices:\nA:√{3}\nB:2√{3}\nC:4\nD:4√{3}'
        self.answer = 'B'
        self.answer_type = 'choice'
        self.subject = 'PlaneGeometry'
        self.level = 'middle_school'
        self.scene_path = Path(__file__).with_name("scenes") / "Plane07.json"

    def get_scene(self):
        return read_json(self.scene_path)

    def draw(self, output_path=None):
        return draw_question('PlaneGeometry', self.scene_path, output_path)

if __name__ == "__main__":
    result = Plane07().draw()
    print(result["image_path"])
