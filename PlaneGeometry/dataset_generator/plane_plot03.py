"""Frozen MathVerse question Plane03; source key s244."""
from pathlib import Path
import sys
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.geometry_dataset import draw_question, read_json

class Plane03:
    def __init__(self):
        self.id = 'Plane03'
        self.source_dataset = 'MathVerse'
        self.query = 'As shown in the figure, in the inscribed pentagon ABCDE of circle O, find the measure of angle B: ____.'
        self.answer = '95°'
        self.answer_type = 'numeric'
        self.subject = 'PlaneGeometry'
        self.level = 'middle_school'
        self.scene_path = Path(__file__).with_name("scenes") / "Plane03.json"

    def get_scene(self):
        return read_json(self.scene_path)

    def draw(self, output_path=None):
        return draw_question('PlaneGeometry', self.scene_path, output_path)

if __name__ == "__main__":
    result = Plane03().draw()
    print(result["image_path"])
