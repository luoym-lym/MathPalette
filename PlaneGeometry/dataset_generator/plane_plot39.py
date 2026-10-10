"""Frozen MathVerse question Plane39; source key s3874."""
from pathlib import Path
import sys
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.geometry_dataset import draw_question, read_json

class Plane39:
    def __init__(self):
        self.id = 'Plane39'
        self.source_dataset = 'MathVerse'
        self.query = 'The perimeter of the rectangle above is p and the area of the rectangle is 36. If l and w are integers, what is one possible value of p?'
        self.answer = '24'
        self.answer_type = 'integer'
        self.subject = 'PlaneGeometry'
        self.level = 'high_school'
        self.scene_path = Path(__file__).with_name("scenes") / "Plane39.json"

    def get_scene(self):
        return read_json(self.scene_path)

    def draw(self, output_path=None):
        return draw_question('PlaneGeometry', self.scene_path, output_path)

if __name__ == "__main__":
    result = Plane39().draw()
    print(result["image_path"])
