"""Frozen MathVerse question Plane27; source key s1789."""
from pathlib import Path
import sys
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.geometry_dataset import draw_question, read_json

class Plane27:
    def __init__(self):
        self.id = 'Plane27'
        self.source_dataset = 'MathVerse'
        self.query = 'Consider the following diagram. Hence, use the rounded values of y and w to find x, correct to 1 decimal place.'
        self.answer = '24.6'
        self.answer_type = 'numeric'
        self.subject = 'PlaneGeometry'
        self.level = 'high_school'
        self.scene_path = Path(__file__).with_name("scenes") / "Plane27.json"

    def get_scene(self):
        return read_json(self.scene_path)

    def draw(self, output_path=None):
        return draw_question('PlaneGeometry', self.scene_path, output_path)

if __name__ == "__main__":
    result = Plane27().draw()
    print(result["image_path"])
