"""Frozen MathVerse question Plane16; source key s3849."""
from pathlib import Path
import sys
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.geometry_dataset import draw_question, read_json

class Plane16:
    def __init__(self):
        self.id = 'Plane16'
        self.source_dataset = 'MathVerse'
        self.query = 'In the figure above, the seven small circles have equal radii. The area of the shaded portion is how many times the area of one of the small circles?'
        self.answer = '1'
        self.answer_type = 'ratio'
        self.subject = 'PlaneGeometry'
        self.level = 'high_school'
        self.scene_path = Path(__file__).with_name("scenes") / "Plane16.json"

    def get_scene(self):
        return read_json(self.scene_path)

    def draw(self, output_path=None):
        return draw_question('PlaneGeometry', self.scene_path, output_path)

if __name__ == "__main__":
    result = Plane16().draw()
    print(result["image_path"])
