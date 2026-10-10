"""Frozen MathVerse question Plane34; source key s2099."""
from pathlib import Path
import sys
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.geometry_dataset import draw_question, read_json

class Plane34:
    def __init__(self):
        self.id = 'Plane34'
        self.source_dataset = 'MathVerse'
        self.query = 'Find the length of the missing side of the trapezium shown.'
        self.answer = '$5=s$'
        self.answer_type = 'length'
        self.subject = 'PlaneGeometry'
        self.level = 'high_school'
        self.scene_path = Path(__file__).with_name("scenes") / "Plane34.json"

    def get_scene(self):
        return read_json(self.scene_path)

    def draw(self, output_path=None):
        return draw_question('PlaneGeometry', self.scene_path, output_path)

if __name__ == "__main__":
    result = Plane34().draw()
    print(result["image_path"])
