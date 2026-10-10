"""Frozen MathVerse question Plane28; source key s1829."""
from pathlib import Path
import sys
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.geometry_dataset import draw_question, read_json

class Plane28:
    def __init__(self):
        self.id = 'Plane28'
        self.source_dataset = 'MathVerse'
        self.query = 'Find the height of the lighthouse to the nearest tenth of a metre.'
        self.answer = '4.6 m'
        self.answer_type = 'numeric'
        self.subject = 'PlaneGeometry'
        self.level = 'high_school'
        self.scene_path = Path(__file__).with_name("scenes") / "Plane28.json"

    def get_scene(self):
        return read_json(self.scene_path)

    def draw(self, output_path=None):
        return draw_question('PlaneGeometry', self.scene_path, output_path)

if __name__ == "__main__":
    result = Plane28().draw()
    print(result["image_path"])
