"""Frozen MathVerse question Plane12; source key s704."""
from pathlib import Path
import sys
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.geometry_dataset import draw_question, read_json

class Plane12:
    def __init__(self):
        self.id = 'Plane12'
        self.source_dataset = 'MathVerse'
        self.query = 'then the height of the building is ()\nChoices:\nA:10m\nB:12m\nC:15m\nD:22.5m'
        self.answer = 'A'
        self.answer_type = 'numeric'
        self.subject = 'PlaneGeometry'
        self.level = 'high_school'
        self.scene_path = Path(__file__).with_name("scenes") / "Plane12.json"

    def get_scene(self):
        return read_json(self.scene_path)

    def draw(self, output_path=None):
        return draw_question('PlaneGeometry', self.scene_path, output_path)

if __name__ == "__main__":
    result = Plane12().draw()
    print(result["image_path"])
