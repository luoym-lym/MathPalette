"""Frozen MathVerse question Plane29; source key s1839."""
from pathlib import Path
import sys
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.geometry_dataset import draw_question, read_json

class Plane29:
    def __init__(self):
        self.id = 'Plane29'
        self.source_dataset = 'MathVerse'
        self.query = 'A farmer wants to build a fence around the entire perimeter of his land, as shown in the diagram. The fencing costs £37 per metre.\nAt £37 per metre of fencing, how much will it cost him to build the fence along the entire perimeter of the land?'
        self.answer = '777'
        self.answer_type = 'numeric'
        self.subject = 'PlaneGeometry'
        self.level = 'high_school'
        self.scene_path = Path(__file__).with_name("scenes") / "Plane29.json"

    def get_scene(self):
        return read_json(self.scene_path)

    def draw(self, output_path=None):
        return draw_question('PlaneGeometry', self.scene_path, output_path)

if __name__ == "__main__":
    result = Plane29().draw()
    print(result["image_path"])
