"""Frozen MathVerse question Plane25; source key s1774."""
from pathlib import Path
import sys
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.geometry_dataset import draw_question, read_json

class Plane25:
    def __init__(self):
        self.id = 'Plane25'
        self.source_dataset = 'MathVerse'
        self.query = 'Consider the following diagram. Hence, find AD correct to two decimal places.'
        self.answer = '93.31'
        self.answer_type = 'length'
        self.subject = 'PlaneGeometry'
        self.level = 'high_school'
        self.scene_path = Path(__file__).with_name("scenes") / "Plane25.json"

    def get_scene(self):
        return read_json(self.scene_path)

    def draw(self, output_path=None):
        return draw_question('PlaneGeometry', self.scene_path, output_path)

if __name__ == "__main__":
    result = Plane25().draw()
    print(result["image_path"])
