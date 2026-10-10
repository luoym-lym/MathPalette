"""Frozen MathVerse question Plane32; source key s2054."""
from pathlib import Path
import sys
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.geometry_dataset import draw_question, read_json

class Plane32:
    def __init__(self):
        self.id = 'Plane32'
        self.source_dataset = 'MathVerse'
        self.query = 'Consider the sector below. \n\nCalculate the perimeter of the sector. Round your answer to two decimal places.'
        self.answer = 'Perimeter $=257.73 \\mathrm{~m}$'
        self.answer_type = 'numeric'
        self.subject = 'PlaneGeometry'
        self.level = 'high_school'
        self.scene_path = Path(__file__).with_name("scenes") / "Plane32.json"

    def get_scene(self):
        return read_json(self.scene_path)

    def draw(self, output_path=None):
        return draw_question('PlaneGeometry', self.scene_path, output_path)

if __name__ == "__main__":
    result = Plane32().draw()
    print(result["image_path"])
