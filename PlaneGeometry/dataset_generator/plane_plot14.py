"""Frozen MathVerse question Plane14; source key s3824."""
from pathlib import Path
import sys
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.geometry_dataset import draw_question, read_json

class Plane14:
    def __init__(self):
        self.id = 'Plane14'
        self.source_dataset = 'MathVerse'
        self.query = 'In the figure above, PQRS is a rectangle. The area of triangle RST is 7 and PT=2/5*PS. What is the area of PQRS?'
        self.answer = '70/3'
        self.answer_type = 'number'
        self.subject = 'PlaneGeometry'
        self.level = 'high_school'
        self.scene_path = Path(__file__).with_name("scenes") / "Plane14.json"

    def get_scene(self):
        return read_json(self.scene_path)

    def draw(self, output_path=None):
        return draw_question('PlaneGeometry', self.scene_path, output_path)

if __name__ == "__main__":
    result = Plane14().draw()
    print(result["image_path"])
