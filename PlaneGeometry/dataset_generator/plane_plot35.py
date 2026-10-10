"""Frozen MathVerse question Plane35; source key s2134."""
from pathlib import Path
import sys
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.geometry_dataset import draw_question, read_json

class Plane35:
    def __init__(self):
        self.id = 'Plane35'
        self.source_dataset = 'MathVerse'
        self.query = 'A boat is at the current point. Write down the bearing that the boat should travel on to return to the starting point.'
        self.answer = 'N 34° W'
        self.answer_type = 'text'
        self.subject = 'PlaneGeometry'
        self.level = 'high_school'
        self.scene_path = Path(__file__).with_name("scenes") / "Plane35.json"

    def get_scene(self):
        return read_json(self.scene_path)

    def draw(self, output_path=None):
        return draw_question('PlaneGeometry', self.scene_path, output_path)

if __name__ == "__main__":
    result = Plane35().draw()
    print(result["image_path"])
