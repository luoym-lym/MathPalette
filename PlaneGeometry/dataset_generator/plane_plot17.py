"""Frozen MathVerse question Plane17; source key s999."""
from pathlib import Path
import sys
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.geometry_dataset import draw_question, read_json

class Plane17:
    def __init__(self):
        self.id = 'Plane17'
        self.source_dataset = 'MathVerse'
        self.query = 'There is an isosceles triangle. Find x. Round to the nearest tenth.\nChoices:\nA:18.8\nB:23.2\nC:25.9\nD:44.0'
        self.answer = 'A'
        self.answer_type = 'choice'
        self.subject = 'PlaneGeometry'
        self.level = 'high_school'
        self.scene_path = Path(__file__).with_name("scenes") / "Plane17.json"

    def get_scene(self):
        return read_json(self.scene_path)

    def draw(self, output_path=None):
        return draw_question('PlaneGeometry', self.scene_path, output_path)

if __name__ == "__main__":
    result = Plane17().draw()
    print(result["image_path"])
